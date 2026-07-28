#!/usr/bin/env python3
"""Materialize a path prefix from an exact GitHub Git commit via the object API.

This is intended for immutable release sources that are deliberately not attached
to an ordinary branch. Every downloaded blob is checked against its Git object
SHA before it is written.

For the ABF-001 two-stage freeze, the mathematical-source commit contains the
controlling theorem, proof, source, tests, and search ledger. Its one-commit
release-control child adds a declared set of publication and rights records
without modifying any frozen mathematical-source byte. The second materializer
call verifies that exact additive overlay and copies the allowed records into the
comparison tree so the workflow can perform a complete directory comparison.
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
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


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
    url = f"https://api.github.com/repos/{owner}/{name}/git/trees/{tree_sha}"
    tree = api_json(url, token)
    materialized: list[dict[str, Any]] = []

    for entry in tree.get("tree", []):
        name_part = entry["path"]
        path = f"{current_path}/{name_part}" if current_path else name_part
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

        blob_url = f"https://api.github.com/repos/{owner}/{name}/git/blobs/{sha}"
        blob = api_json(blob_url, token)
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
            link_target = data.decode("utf-8")
            target.symlink_to(link_target)
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
    *,
    prefix: str,
    output: Path,
) -> list[dict[str, Any]]:
    """Verify the declared additive release-control overlay for ABF-001.

    The release-control child is allowed to add only publication, disclosure,
    rights, and package metadata records. It may not alter or delete any byte
    from the mathematical-source commit.
    """

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
            "release-control child deleted frozen mathematical-source files: "
            + ", ".join(missing)
        )

    changed = [
        relative
        for relative in sorted(frozen)
        if frozen[relative].read_bytes() != released[relative].read_bytes()
    ]
    if changed:
        raise RuntimeError(
            "release-control child modified frozen mathematical-source bytes: "
            + ", ".join(changed)
        )

    additions = set(released) - set(frozen)
    if additions != ABF_ALLOWED_ADDITIONS:
        raise RuntimeError(
            "unexpected ABF release-control additions: "
            f"expected={sorted(ABF_ALLOWED_ADDITIONS)} "
            f"actual={sorted(additions)}"
        )

    overlay_receipt: list[dict[str, Any]] = []
    for relative in sorted(additions):
        source = released[relative]
        target = safe_output_path(output, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        data = target.read_bytes()
        overlay_receipt.append(
            {
                "relative_path": relative,
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
                "classification": "allowed_additive_release_record",
            }
        )
    return overlay_receipt


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

    if (
        not all(c in "0123456789abcdef" for c in args.commit)
        or len(args.commit) != 40
    ):
        raise SystemExit("--commit must be a lowercase 40-character SHA")
    if (
        not all(c in "0123456789abcdef" for c in args.expected_parent)
        or len(args.expected_parent) != 40
    ):
        raise SystemExit("--expected-parent must be a lowercase 40-character SHA")

    token = os.environ.get(args.token_env)
    if not token:
        raise SystemExit(
            f"missing token environment variable: {args.token_env}"
        )

    owner, name = args.repository.split("/", 1)
    commit_url = (
        f"https://api.github.com/repos/{owner}/{name}/git/commits/{args.commit}"
    )
    commit = api_json(commit_url, token)
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

    overlay = verify_and_apply_abf_release_overlay(
        prefix=prefix,
        output=output,
    )

    receipt = {
        "schema_version": (
            "n.human_llm.mathematics.github_object_materialization.v2"
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
                "frozen mathematical bytes unchanged; exact additive "
                "publication-record allowlist"
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
            | {
                "release_control_overlay_files": len(overlay),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
