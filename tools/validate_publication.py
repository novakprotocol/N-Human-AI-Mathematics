#!/usr/bin/env python3
"""Fail-closed validator for the N Human-AI Mathematics publication tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

EXPECTED_REPOSITORY = "novakprotocol/N-Human-AI-Mathematics"
ROOT_REQUIRED = {
    "README.md", "START_HERE.md", "STATUS.md", "RESEARCH_INDEX.md",
    "research-index.json", "AGENTS.md", "CLAIM_LEVELS.md",
    "EVIDENCE_STANDARD.md", "REVIEW_PROTOCOL.md", "PUBLICATION_WORKFLOW.md",
    "CONTRIBUTING.md", "CORRECTIONS.md", "RIGHTS_AND_LICENSING.md",
    "CITATION.cff", "schemas/research-index.schema.json",
    "schemas/paper-status.schema.json", "tools/validate_publication.py",
    "tools/Initialize-N-Human-AI-Mathematics.ps1",
    ".github/workflows/validate.yml",
    ".github/ISSUE_TEMPLATE/counterexample.yml",
    ".github/ISSUE_TEMPLATE/proof-gap.yml",
    ".github/ISSUE_TEMPLATE/prior-art.yml",
    ".github/ISSUE_TEMPLATE/reproduction.yml",
    ".github/pull_request_template.md",
}
PAPER_REQUIRED = {
    "README.md", "PLAIN_LANGUAGE.md", "STATUS.json", "CLAIMS.md",
    "PROOF_MAP.md", "FORMAL_VERIFICATION.md", "PRIOR_ART.md",
    "REPRODUCE.md", "REVIEW_REQUEST.md", "AI_DISCLOSURE.md",
    "EVIDENCE_MAP.md", "SOURCE_MANIFEST.json", "CITATION.cff",
    "MANUSCRIPT_TERMS.md", "CODE_TERMS.md", "DATA_AND_EVIDENCE_TERMS.md",
    "THIRD_PARTY_NOTICES.md",
}
VALID_STATES = {
    "active_review", "hold", "archived_case_study", "rejected",
    "superseded", "published",
}
TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".yml", ".yaml", ".cff", ".py", ".ps1",
    ".lean", ".tex", ".bib", ".toml",
}
# This checker embeds its detection signatures, so its own source is the only
# explicitly excluded text file. The exclusion is recorded in every receipt.
SCAN_EXCLUDED_PATHS = frozenset({"tools/validate_publication.py"})
MIT_LICENSE_GRANT = (
    r"Permission is hereby granted, free of charge, "
    r"to any person obtaining a copy"
)
FORBIDDEN_PATTERNS = (
    ("personal Windows path", re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+", re.I)),
    ("private key material", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("GitHub classic token", re.compile(r"ghp_[A-Za-z0-9]{30,}")),
    ("GitHub fine-grained token", re.compile(r"github_pat_[A-Za-z0-9_]{30,}")),
    ("blanket MIT license text", re.compile(MIT_LICENSE_GRANT)),
)
PAPER_ID_RE = re.compile(r"^[A-Z]{2,8}-[0-9]{3}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class Finding:
    level: str
    path: str
    message: str


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"missing JSON file: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"invalid JSON at {path}:{exc.lineno}:{exc.colno}: {exc.msg}"
        ) from exc


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def missing_keys(obj: dict[str, Any], keys: Iterable[str], label: str) -> list[Finding]:
    return [
        Finding("ERROR", label, f"missing required field: {key}")
        for key in sorted(keys) if key not in obj
    ]


def validate_status(root: Path, paper_id: str, path: Path, allow_public: bool) -> list[Finding]:
    rel = relative(path, root)
    try:
        data = load_json(path)
    except ValueError as exc:
        return [Finding("ERROR", rel, str(exc))]
    if not isinstance(data, dict):
        return [Finding("ERROR", rel, "top level must be an object")]
    findings = missing_keys(data, {
        "schema_version", "paper_id", "title", "source", "claim", "proof",
        "computation", "formal_verification", "review", "release", "limitations",
    }, rel)
    if data.get("schema_version") != "n.human_ai_mathematics.paper_status.v1":
        findings.append(Finding("ERROR", rel, "unexpected schema_version"))
    if data.get("paper_id") != paper_id:
        findings.append(Finding("ERROR", rel, "paper_id does not match directory"))
    source = data.get("source")
    if not isinstance(source, dict):
        findings.append(Finding("ERROR", rel, "source must be an object"))
    else:
        commit = source.get("commit")
        if commit is not None and (not isinstance(commit, str) or not COMMIT_RE.fullmatch(commit)):
            findings.append(Finding("ERROR", rel, f"invalid source commit: {commit!r}"))
    release = data.get("release")
    if not isinstance(release, dict):
        findings.append(Finding("ERROR", rel, "release must be an object"))
    else:
        flag = release.get("public_authorized")
        if not isinstance(flag, bool):
            findings.append(Finding("ERROR", rel, "release.public_authorized must be Boolean"))
        elif flag and not allow_public:
            findings.append(Finding("ERROR", rel, "paper public release is authorized without --allow-public"))
    if not isinstance(data.get("limitations"), list) or not data.get("limitations"):
        findings.append(Finding("ERROR", rel, "limitations must be a nonempty array"))
    formal = data.get("formal_verification")
    if not isinstance(formal, dict):
        findings.append(Finding("ERROR", rel, "formal_verification must be an object"))
    else:
        status_text = str(formal.get("status", "")).lower()
        receipts = formal.get("receipts")
        if "pass" in status_text and (not isinstance(receipts, list) or not receipts):
            findings.append(Finding("ERROR", rel, "formal PASS lacks receipts"))
        unverified = " ".join(map(str, formal.get("unverified_scope", []))).lower()
        if "full manuscript" in status_text and "incomplete" not in status_text and "full manuscript" in unverified:
            findings.append(Finding("ERROR", rel, "formal status conflicts with unverified full manuscript"))
    return findings


def safe_target(root: Path, name: str) -> Path | None:
    pure = PurePosixPath(name)
    if pure.is_absolute() or not pure.parts or ".." in pure.parts:
        return None
    target = (root / Path(*pure.parts)).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        return None
    return target


def validate_manifest(root: Path, paper_id: str, path: Path) -> list[Finding]:
    rel = relative(path, root)
    try:
        data = load_json(path)
    except ValueError as exc:
        return [Finding("ERROR", rel, str(exc))]
    if not isinstance(data, dict):
        return [Finding("ERROR", rel, "top level must be an object")]
    findings = missing_keys(data, {
        "schema_version", "paper_id", "generated_repository", "sources",
        "external_evidence", "materialization_status", "public_release_authorized",
    }, rel)
    if data.get("schema_version") != "n.human_ai_mathematics.source_manifest.v1":
        findings.append(Finding("ERROR", rel, "unexpected schema_version"))
    if data.get("paper_id") != paper_id:
        findings.append(Finding("ERROR", rel, "manifest paper_id does not match directory"))
    if data.get("generated_repository") != EXPECTED_REPOSITORY:
        findings.append(Finding("ERROR", rel, f"generated_repository must be {EXPECTED_REPOSITORY}"))
    if data.get("public_release_authorized") is not False:
        findings.append(Finding("ERROR", rel, "staging manifest must keep public release unauthorized"))
    seen: set[str] = set()
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        findings.append(Finding("ERROR", rel, "sources must be a nonempty array"))
    else:
        for i, source in enumerate(sources):
            label = f"{rel}:sources[{i}]"
            if not isinstance(source, dict):
                findings.append(Finding("ERROR", label, "source must be an object")); continue
            commit = source.get("commit")
            if not isinstance(commit, str) or not COMMIT_RE.fullmatch(commit):
                findings.append(Finding("ERROR", label, f"invalid source commit: {commit!r}"))
            files = source.get("files")
            if not isinstance(files, list) or not files:
                findings.append(Finding("ERROR", label, "files must be a nonempty array")); continue
            for j, mapping in enumerate(files):
                item = f"{label}:files[{j}]"
                if not isinstance(mapping, dict):
                    findings.append(Finding("ERROR", item, "mapping must be an object")); continue
                source_name, target_name = mapping.get("source"), mapping.get("target")
                if not isinstance(source_name, str) or not source_name:
                    findings.append(Finding("ERROR", item, "source path is missing"))
                if not isinstance(target_name, str) or not target_name:
                    findings.append(Finding("ERROR", item, "target path is missing")); continue
                if target_name in seen:
                    findings.append(Finding("ERROR", item, f"duplicate target path: {target_name}"))
                seen.add(target_name)
                target = safe_target(root, target_name)
                if target is None:
                    findings.append(Finding("ERROR", item, f"unsafe target path: {target_name}"))
                elif not target.is_file():
                    findings.append(Finding("ERROR", target_name, "materialized source target is missing"))
    evidence = data.get("external_evidence")
    if not isinstance(evidence, list):
        findings.append(Finding("ERROR", rel, "external_evidence must be an array"))
    else:
        for i, item in enumerate(evidence):
            label = f"{rel}:external_evidence[{i}]"
            if not isinstance(item, dict):
                findings.append(Finding("ERROR", label, "external evidence must be an object")); continue
            value = item.get("sha256")
            if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
                findings.append(Finding("ERROR", label, f"invalid SHA-256: {value!r}"))
    return findings


def validate_paper(root: Path, paper_id: str, allow_public: bool) -> list[Finding]:
    directory = root / "papers" / paper_id
    if not directory.is_dir():
        return [Finding("ERROR", f"papers/{paper_id}", "active-review paper directory is missing")]
    findings: list[Finding] = []
    for required in sorted(PAPER_REQUIRED):
        target = directory / required
        if not target.is_file():
            findings.append(Finding("ERROR", relative(target, root), "required active-review paper file is missing"))
    status = directory / "STATUS.json"
    manifest = directory / "SOURCE_MANIFEST.json"
    if status.is_file():
        findings.extend(validate_status(root, paper_id, status, allow_public))
    if manifest.is_file():
        findings.extend(validate_manifest(root, paper_id, manifest))
    return findings


def validate_index(root: Path, allow_public: bool) -> list[Finding]:
    path = root / "research-index.json"
    rel = relative(path, root)
    try:
        data = load_json(path)
    except ValueError as exc:
        return [Finding("ERROR", rel, str(exc))]
    if not isinstance(data, dict):
        return [Finding("ERROR", rel, "top level must be an object")]
    findings = missing_keys(data, {
        "schema_version", "repository", "accountable_owner", "operating_mode",
        "public_release_authorized", "papers",
    }, rel)
    if data.get("schema_version") != "n.human_ai_mathematics.research_index.v1":
        findings.append(Finding("ERROR", rel, "unexpected schema_version"))
    if data.get("repository") != EXPECTED_REPOSITORY:
        findings.append(Finding("ERROR", rel, f"repository must be {EXPECTED_REPOSITORY}"))
    if data.get("operating_mode") != "human-led-ai-assisted":
        findings.append(Finding("ERROR", rel, "operating_mode must be human-led-ai-assisted"))
    flag = data.get("public_release_authorized")
    if not isinstance(flag, bool):
        findings.append(Finding("ERROR", rel, "public_release_authorized must be Boolean"))
    elif flag and not allow_public:
        findings.append(Finding("ERROR", rel, "public release is authorized but --allow-public was not supplied"))
    papers = data.get("papers")
    if not isinstance(papers, list):
        findings.append(Finding("ERROR", rel, "papers must be an array")); return findings
    ids: set[str] = set(); slugs: set[str] = set()
    for i, paper in enumerate(papers):
        label = f"{rel}:papers[{i}]"
        if not isinstance(paper, dict):
            findings.append(Finding("ERROR", label, "paper entry must be an object")); continue
        findings.extend(missing_keys(paper, {
            "id", "slug", "title", "fields", "state", "claim_status",
            "human_proof", "internal_reproduction", "formal_verification",
            "external_specialist_review", "historical_priority", "peer_review",
            "public_release",
        }, label))
        paper_id, slug, state = paper.get("id"), paper.get("slug"), paper.get("state")
        if not isinstance(paper_id, str) or not PAPER_ID_RE.fullmatch(paper_id):
            findings.append(Finding("ERROR", label, f"invalid paper id: {paper_id!r}")); continue
        if paper_id in ids:
            findings.append(Finding("ERROR", label, f"duplicate paper id: {paper_id}"))
        ids.add(paper_id)
        if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
            findings.append(Finding("ERROR", label, f"invalid slug: {slug!r}"))
        elif slug in slugs:
            findings.append(Finding("ERROR", label, f"duplicate slug: {slug}"))
        else:
            slugs.add(slug)
        if state not in VALID_STATES:
            findings.append(Finding("ERROR", label, f"invalid state: {state!r}"))
        if state == "active_review":
            findings.extend(validate_paper(root, paper_id, allow_public))
    return findings


def scan_text(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = relative(path, root)
        if rel in SCAN_EXCLUDED_PATHS:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(Finding("ERROR", rel, "declared text file is not UTF-8")); continue
        for label, pattern in FORBIDDEN_PATTERNS:
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                findings.append(Finding("ERROR", f"{rel}:{line}", f"forbidden {label}"))
        lowered = text.lower()
        if "globally novel" in lowered and "unestablished" not in lowered and "not" not in lowered:
            findings.append(Finding("WARNING", rel, "contains 'globally novel' without an obvious local limitation marker"))
    return findings


def inventory(root: Path) -> dict[str, Any]:
    files = [path for path in root.rglob("*") if path.is_file()]
    return {
        "file_count": len(files),
        "text_file_count": sum(path.suffix.lower() in TEXT_SUFFIXES for path in files),
        "total_bytes": sum(path.stat().st_size for path in files),
        "scan_excluded_paths": sorted(SCAN_EXCLUDED_PATHS),
        "research_index_sha256": digest(root / "research-index.json") if (root / "research-index.json").is_file() else None,
        "hinc_status_sha256": digest(root / "papers/HINC-001/STATUS.json") if (root / "papers/HINC-001/STATUS.json").is_file() else None,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--allow-public", action="store_true")
    parser.add_argument("--json-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args(); root = args.root.resolve(); findings: list[Finding] = []
    if not root.is_dir():
        findings.append(Finding("ERROR", str(root), "repository root does not exist")); report_inventory = {}
    else:
        for required in sorted(ROOT_REQUIRED):
            if not (root / required).is_file():
                findings.append(Finding("ERROR", required, "required repository file is missing"))
        findings.extend(validate_index(root, args.allow_public))
        findings.extend(scan_text(root))
        report_inventory = inventory(root)
    errors = [item for item in findings if item.level == "ERROR"]
    warnings = [item for item in findings if item.level == "WARNING"]
    result = {
        "schema_version": "n.human_ai_mathematics.validation.v1",
        "root": str(root), "result": "PASS" if not errors else "FAIL",
        "error_count": len(errors), "warning_count": len(warnings),
        "inventory": report_inventory, "findings": [asdict(item) for item in findings],
    }
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for item in findings:
        print(f"{item.level}: {item.path}: {item.message}")
    print(json.dumps({key: result[key] for key in ("result", "error_count", "warning_count")}, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
