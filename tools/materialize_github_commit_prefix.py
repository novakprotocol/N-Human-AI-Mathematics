#!/usr/bin/env python3
"""Materialize a path prefix from an exact GitHub commit via the object API.

The release gate uses this for commits that are intentionally not ordinary
publication branches. Every downloaded blob is checked against its Git object
SHA before writing.

ABF-001 uses a two-stage freeze. The mathematical-source commit fixes the
controlling theorem, proof, source, tests, and search ledger. Its one-commit
release-control child may add a strict allowlist of disclosure, rights, and
package records. It may also replace one exact release-runtime dependency file;
that replacement is identified by both its old and new SHA-256 values and does
not alter mathematical source or claims.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import shutil
import stat
import urllib.error
import urllib.request
from pathlib import Path, PurePosixPath
from typing import Any

ABF_MATHEMATICAL_PREFIX = "staging/ABF-001/mathematical-source"
ABF_RELEASE_OVERLAY = Path("/tmp/abf-freeze/mathematical-source")
ABF_ALLOWED_ADDITIONS = frozenset(
    {
        "AI_DISCLOSURE.md",
        "CITATION.cff",
        "CODE_TERMS.md",
        "DATA_AND_EVIDENCE_TERMS.md",
        "EVIDENCE_MAP.md",
        "FORMAL_VERIFICATION.md",
        "MANUSCRIPT_TERMS.md",
        "PLAIN_LANGUAGE.md",
        "PRIOR_ART.md",
        "REVIEW_REQUEST.md",
        "SOURCE_MANIFEST.json",
        "THIRD_PARTY_NOTICES.md",
    }
)
ABF_ALLOWED_REPLACEMENTS = {
    "requirements-release.txt": {
        "frozen_sha256": "81794646d1034c4f16ed368949e6ec21f1c182b1778785a238b9b14a43e57524",
        "released_sha256": "54afc6f1c04f582ebdc4f495a48b34c467a5e94b6cba67cdc4030aa3f2f39de6",
        "classification": "release_runtime_dependency_pin",
        "reason": (
            "WeasyPrint 63.0 is the first line with declared Python 3.13 and "
            "pydyf 0.11 support; mathematical source and claims are unchanged"
        ),
    }
}


def api_json(url: str, token: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "n-human-llm-mathematics-release-gate",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {exc.code} for {url}: {body}") from exc


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_output_path(root: Path, relative: str) -> Path:
    pure = PurePosixPath(relative)
    if pure.is_absolute() or ".." in pure.parts:
        raise RuntimeError(f"unsafe repository path: {relative}")
    target = root.joinpath(*pure.parts).resolve()
    root_resolved = root.resolve()
    try:
        target.relative_to(root_resolved)
    except ValueError as exc:
        raise RuntimeError(f"path escapes output root: {relative}") from exc
    return target


def should_descend(path: str, prefix: str) -> bool:
    return (
        not path
        or path == prefix
        or prefix.startswith(path + "/")
        or path.startswith(prefix + "/")
    )


def walk_tree(
    *,
    repository: str,
    tree_sha: str,
    token: str,
    prefix: str,
    output: Path,
    current_path: str = "",
) -> list[dict[str, Any]]:
    owner, name = repository.split("/", 1)
    tree = api_json(
        f"https://api.github.com/repos/{owner}/{name}/git/trees/{tree_sha}",
        token,
    )
    materialized: list[dict[str, Any]] = []

    for entry in tree.get("tree", []):
        path = (
            f"{current_path}/{entry['path']}"
            if current_path
            else entry["path"]
        )
        entry_type = entry["type"]
        mode = entry["mode"]
        sha = entry["sha"]

        if entry_type == "tree":
            if should_descend(path, prefix):
                materialized.extend(
                    walk_tree(
                        repository=repository,
                        tree_sha=sha,
                        token=token,
                        prefix=prefix,
                        output=output,
                        current_path=path,
                    )
                )
            continue

        if not (path == prefix or path.startswith(prefix + "/")):
            continue
        if entry_type != "blob":
            raise RuntimeError(f"unsupported Git tree entry {entry_type} at {path}")

        owner, name = repository.split("/", 1)
        blob = api_json(
            f"https://api.github.com/repos/{owner}/{name}/git/blobs/{sha}",
            token,
        )
        if blob.get("encoding") != "base64":
            raise RuntimeError(
                f"unexpected blob encoding at {path}: {blob.get('encoding')}"
            )
        data = base64.b64decode(blob["content"], validate=False)
        actual_sha = git_blob_sha(data)
        if actual_sha != sha:
            raise RuntimeError(
                f"Git blob identity mismatch at {path}: {actual_sha} != {sha}"
            )

        relative = path[len(prefix) :].lstrip("/")
        target = safe_output_path(output, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        if mode == "120000":
            target.symlink_to(data.decode("utf-8"))
        else:
            target.write_bytes(data)
            if mode == "100755":
                target.chmod(
                    target.stat().st_mode
                    | stat.S_IXUSR
                    | stat.S_IXGRP
                    | stat.S_IXOTH
                )
        materialized.append(
            {
                "repository_path": path,
                "relative_path": relative,
                "blob_sha": sha,
                "bytes": len(data),
                "mode": mode,
            }
        )
    return materialized


def regular_files(root: Path) -> dict[str, Path]:
    return {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*")
        if path.is_file() and not path.is_symlink()
    }


def verify_and_apply_abf_release_overlay(
    *, prefix: str, output: Path
) -> list[dict[str, Any]]:
    if prefix != ABF_MATHEMATICAL_PREFIX:
        return []
    if not ABF_RELEASE_OVERLAY.is_dir():
        raise RuntimeError(
            f"ABF release overlay is unavailable: {ABF_RELEASE_OVERLAY}"
        )

    frozen = regular_files(output)
    released = regular_files(ABF_RELEASE_OVERLAY)
    missing = sorted(set(frozen) - set(released))
    if missing:
        raise RuntimeError(
            "release-control child deleted frozen files: " + ", ".join(missing)
        )

    additions = set(released) - set(frozen)
    if additions != ABF_ALLOWED_ADDITIONS:
        raise RuntimeError(
            "unexpected ABF release-control additions: "
            f"expected={sorted(ABF_ALLOWED_ADDITIONS)} actual={sorted(additions)}"
        )

    changed = {
        relative
        for relative in frozen
        if frozen[relative].read_bytes() != released[relative].read_bytes()
    }
    expected_changed = set(ABF_ALLOWED_REPLACEMENTS)
    if changed != expected_changed:
        raise RuntimeError(
            "unexpected ABF release-control replacements: "
            f"expected={sorted(expected_changed)} actual={sorted(changed)}"
        )

    receipt: list[dict[str, Any]] = []
    for relative in sorted(changed):
        policy = ABF_ALLOWED_REPLACEMENTS[relative]
        old_hash = sha256_file(frozen[relative])
        new_hash = sha256_file(released[relative])
        if old_hash != policy["frozen_sha256"]:
            raise RuntimeError(
                f"unexpected frozen identity for {relative}: {old_hash}"
            )
        if new_hash != policy["released_sha256"]:
            raise RuntimeError(
                f"unexpected released identity for {relative}: {new_hash}"
            )
        shutil.copyfile(released[relative], frozen[relative])
        receipt.append(
            {
                "relative_path": relative,
                "sha256_before": old_hash,
                "sha256_after": new_hash,
                "bytes": frozen[relative].stat().st_size,
                "classification": policy["classification"],
                "reason": policy["reason"],
            }
        )

    for relative in sorted(additions):
        source = released[relative]
        target = safe_output_path(output, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        data = target.read_bytes()
        receipt.append(
            {
                "relative_path": relative,
                "sha256_after": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
                "classification": "allowed_additive_release_record",
            }
        )
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--expected-parent", required=True)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--token-env", default="GH_TOKEN")
    args = parser.parse_args()

    for label, value in (
        ("--commit", args.commit),
        ("--expected-parent", args.expected_parent),
    ):
        if len(value) != 40 or not all(c in "0123456789abcdef" for c in value):
            raise SystemExit(f"{label} must be a lowercase 40-character SHA")

    token = os.environ.get(args.token_env)
    if not token:
        raise SystemExit(f"missing token environment variable: {args.token_env}")

    owner, name = args.repository.split("/", 1)
    commit = api_json(
        f"https://api.github.com/repos/{owner}/{name}/git/commits/{args.commit}",
        token,
    )
    if commit.get("sha") != args.commit:
        raise RuntimeError("commit identity mismatch")
    parents = [item["sha"] for item in commit.get("parents", [])]
    if parents != [args.expected_parent]:
        raise RuntimeError(f"unexpected commit parents: {parents}")

    output = args.output.resolve()
    if output.exists() and any(output.iterdir()):
        raise RuntimeError(f"output directory is not empty: {output}")
    output.mkdir(parents=True, exist_ok=True)
    prefix = args.prefix.strip("/")
    entries = walk_tree(
        repository=args.repository,
        tree_sha=commit["tree"]["sha"],
        token=token,
        prefix=prefix,
        output=output,
    )
    if not entries:
        raise RuntimeError(f"no blobs found under prefix: {args.prefix}")
    overlay = verify_and_apply_abf_release_overlay(prefix=prefix, output=output)

    receipt = {
        "schema_version": (
            "n.human_llm.mathematics.github_object_materialization.v3"
        ),
        "result": "PASS",
        "repository": args.repository,
        "commit": args.commit,
        "expected_parent": args.expected_parent,
        "tree_sha": commit["tree"]["sha"],
        "prefix": prefix,
        "file_count": len(entries),
        "total_bytes": sum(item["bytes"] for item in entries),
        "files": sorted(entries, key=lambda item: item["repository_path"]),
        "release_control_overlay": {
            "applied": bool(overlay),
            "policy": (
                "frozen mathematical bytes unchanged except one exact "
                "release-runtime dependency pin; exact additive record allowlist"
            ),
            "files": overlay,
        },
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                key: receipt[key]
                for key in (
                    "result",
                    "repository",
                    "commit",
                    "prefix",
                    "file_count",
                    "total_bytes",
                )
            }
            | {"release_control_overlay_files": len(overlay)},
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
