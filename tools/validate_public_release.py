#!/usr/bin/env python3
"""Fail-closed validator for the Human + LLM public-switch candidate."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


REQUIRED_FILES = {
    "README.md",
    "START_HERE.md",
    "STATUS.md",
    "RESEARCH_INDEX.md",
    "research-index.json",
    "PUBLIC_SWITCH_READINESS.md",
    "HUMAN_AI_COLLABORATION_RECORD.md",
    "HUMAN_AI_MATHEMATICS_PRIOR_ART.md",
    "OPEN_REVIEW_CHALLENGE.md",
    "PUBLICATION_WORKFLOW.md",
    "RIGHTS_AND_LICENSING.md",
    "CITATION.cff",
    "reports/public-release-audit-2026-07-27.json",
    "reports/public-switch-readiness.json",
    "papers/HINC-001/README.md",
    "papers/HINC-001/STATUS.json",
    "papers/HINC-001/CLAIMS.md",
    "papers/HINC-001/PROOF_MAP.md",
    "papers/HINC-001/FORMAL_VERIFICATION.md",
    "papers/HINC-001/PRIOR_ART.md",
    "papers/HINC-001/REPRODUCE.md",
    "papers/HINC-001/AI_DISCLOSURE.md",
    "papers/HINC-001/THIRD_PARTY_NOTICES.md",
    "papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md",
    "papers/HINC-001/manuscript/MANUSCRIPT_INDEX.md",
    "papers/HINC-001/manuscript/references.bib",
    "schemas/research-index.schema.json",
    "schemas/paper-status.schema.json",
    "docs/index.html",
    "docs/styles.css",
    "docs/404.html",
    "docs/.nojekyll",
    ".github/workflows/pages.yml",
    ".github/workflows/validate.yml",
    "tools/validate_publication.py",
    "tools/validate_public_release.py",
}

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".yml",
    ".yaml",
    ".cff",
    ".py",
    ".ps1",
    ".lean",
    ".tex",
    ".bib",
    ".toml",
    ".html",
    ".css",
    ".js",
    ".xml",
    ".cmd",
}

# Construct withheld identifiers without embedding them contiguously in public
# prose. The validator source itself is excluded from this one scan because the
# strings below are its detection vocabulary.
WITHHELD_IDENTIFIERS = (
    "Chat" + "GPT",
    "Open" + "AI",
    "GPT" + "-5",
    "GPT" + "-4",
)

FORBIDDEN_PATTERNS = (
    (
        "personal Windows user path",
        re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+", re.IGNORECASE),
    ),
    (
        "GitHub token",
        re.compile(r"(?:gh[oprsu]_|github_pat_)[A-Za-z0-9_]{20,}"),
    ),
    (
        "private-key material",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ),
    (
        "blanket MIT grant sentence",
        re.compile(
            r"Permission is hereby granted, free of charge, to any person obtaining a copy",
            re.IGNORECASE,
        ),
    ),
)


@dataclass(frozen=True)
class Finding:
    level: str
    path: str
    message: str


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, path: str, message: str) -> list[Finding]:
    if condition:
        return []
    return [Finding("ERROR", path, message)]


def scan_text(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    validator_path = Path(__file__).resolve()

    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue

        relative = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(
                Finding("ERROR", relative, "declared text file is not UTF-8")
            )
            continue

        for label, pattern in FORBIDDEN_PATTERNS:
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    Finding("ERROR", f"{relative}:{line}", f"forbidden {label}")
                )

        if path.resolve() == validator_path:
            continue

        lowered = text.casefold()
        for identifier in WITHHELD_IDENTIFIERS:
            position = lowered.find(identifier.casefold())
            if position >= 0:
                line = text.count("\n", 0, position) + 1
                findings.append(
                    Finding(
                        "ERROR",
                        f"{relative}:{line}",
                        "withheld model or provider identifier appears in proposed public source",
                    )
                )

    return findings


def validate(root: Path) -> list[Finding]:
    findings: list[Finding] = []

    for relative in sorted(REQUIRED_FILES):
        if not (root / relative).is_file():
            findings.append(Finding("ERROR", relative, "required readiness file missing"))

    if findings:
        return findings

    index = load_json(root / "research-index.json")
    hinc = load_json(root / "papers/HINC-001/STATUS.json")
    audit = load_json(root / "reports/public-release-audit-2026-07-27.json")
    readiness = load_json(root / "reports/public-switch-readiness.json")
    research_schema = load_json(root / "schemas/research-index.schema.json")
    paper_schema = load_json(root / "schemas/paper-status.schema.json")

    findings += require(
        index.get("public_release_authorized") is False,
        "research-index.json",
        "visibility switch must remain unauthorized in the candidate commit",
    )
    findings += require(
        index.get("public_switch_ready") is True,
        "research-index.json",
        "public_switch_ready must be true",
    )
    findings += require(
        index.get("release_channel") == "private_staging",
        "research-index.json",
        "candidate commit must remain private_staging",
    )
    findings += require(
        index.get("release_version") == "0.1.0-public-review-candidate",
        "research-index.json",
        "unexpected candidate version",
    )
    findings += require(
        index.get("specific_model_disclosed") is False,
        "research-index.json",
        "specific_model_disclosed must be false",
    )
    findings += require(
        index.get("specific_provider_disclosed") is False,
        "research-index.json",
        "specific_provider_disclosed must be false",
    )

    papers = {item.get("id"): item for item in index.get("papers", [])}
    findings += require(
        set(papers) == {"HINC-001", "ABF-001", "FSG-001", "ACM-001"},
        "research-index.json",
        "paper portfolio does not match the governed four-paper order",
    )
    findings += require(
        papers.get("HINC-001", {}).get("state") == "active_review",
        "research-index.json",
        "HINC-001 must be the active candidate package",
    )
    for held_id in ("ABF-001", "FSG-001", "ACM-001"):
        findings += require(
            papers.get(held_id, {}).get("state") == "hold",
            "research-index.json",
            f"{held_id} must remain on hold",
        )

    hinc_release = hinc.get("release", {})
    findings += require(
        hinc_release.get("public_authorized") is False,
        "papers/HINC-001/STATUS.json",
        "HINC visibility switch must remain unauthorized in the candidate commit",
    )
    findings += require(
        hinc_release.get("public_switch_ready") is True,
        "papers/HINC-001/STATUS.json",
        "HINC public_switch_ready must be true",
    )
    findings += require(
        hinc_release.get("channel") == "private_staging",
        "papers/HINC-001/STATUS.json",
        "HINC channel must remain private_staging",
    )
    findings += require(
        hinc_release.get("version") == "0.1.0-public-review-candidate",
        "papers/HINC-001/STATUS.json",
        "HINC candidate version mismatch",
    )
    findings += require(
        hinc_release.get("release_date") is None and hinc_release.get("doi") is None,
        "papers/HINC-001/STATUS.json",
        "release date and DOI must remain null before the public switch",
    )
    findings += require(
        hinc_release.get("specific_model_disclosed") is False
        and hinc_release.get("specific_provider_disclosed") is False,
        "papers/HINC-001/STATUS.json",
        "HINC model/provider disclosure boundary failed",
    )

    findings += require(
        audit.get("result") == "READY_PENDING_VISIBILITY_SWITCH",
        "reports/public-release-audit-2026-07-27.json",
        "release audit is not switch-ready",
    )
    audit_scope = audit.get("release_scope", {})
    findings += require(
        audit_scope.get("complete_candidate_public_review_packages") == ["HINC-001"],
        "reports/public-release-audit-2026-07-27.json",
        "release audit must contain exactly HINC-001",
    )
    findings += require(
        audit_scope.get("repository_visibility") == "private"
        and audit_scope.get("public_switch_ready") is True
        and audit_scope.get("visibility_change_executed") is False,
        "reports/public-release-audit-2026-07-27.json",
        "release audit visibility boundary is inconsistent",
    )
    findings += require(
        audit_scope.get("peer_reviewed") is False
        and audit_scope.get("historical_priority_established") is False,
        "reports/public-release-audit-2026-07-27.json",
        "audit overstates peer review or historical priority",
    )

    findings += require(
        readiness.get("result") == "READY_PENDING_VISIBILITY_SWITCH",
        "reports/public-switch-readiness.json",
        "switch-readiness receipt is not ready",
    )
    findings += require(
        readiness.get("public_switch_ready") is True
        and readiness.get("visibility_change_executed") is False
        and readiness.get("pages_deployment_executed") is False,
        "reports/public-switch-readiness.json",
        "switch-readiness execution flags are inconsistent",
    )
    findings += require(
        readiness.get("active_package") == "HINC-001"
        and readiness.get("held_packages") == ["ABF-001", "FSG-001", "ACM-001"],
        "reports/public-switch-readiness.json",
        "switch-readiness portfolio order is inconsistent",
    )

    required_index_fields = set(research_schema.get("required", []))
    findings += require(
        "public_switch_ready" in required_index_fields,
        "schemas/research-index.schema.json",
        "research schema does not require public_switch_ready",
    )
    paper_release_required = set(
        paper_schema.get("properties", {})
        .get("release", {})
        .get("required", [])
    )
    findings += require(
        "public_switch_ready" in paper_release_required,
        "schemas/paper-status.schema.json",
        "paper schema does not require public_switch_ready",
    )

    revised = (
        root / "papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md"
    ).read_text(encoding="utf-8")
    manuscript_index = (
        root / "papers/HINC-001/manuscript/MANUSCRIPT_INDEX.md"
    ).read_text(encoding="utf-8")
    claims = (root / "papers/HINC-001/CLAIMS.md").read_text(encoding="utf-8")
    proof_map = (root / "papers/HINC-001/PROOF_MAP.md").read_text(encoding="utf-8")

    for required_phrase in (
        "binary Gerstenhaber endomorphism",
        "generator-to-global bracket preservation",
        "complete presentation of `O`",
        "explicit representability method",
        "Pointwise-center warning",
        "fppf-derived subgroup and abelianization",
        "public technical-review release:            prepared, not yet activated",
    ):
        findings += require(
            required_phrase in revised,
            "papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md",
            f"revised manuscript is missing: {required_phrase}",
        )

    findings += require(
        "HINC-001_REVISED_MANUSCRIPT.md" in manuscript_index,
        "papers/HINC-001/manuscript/MANUSCRIPT_INDEX.md",
        "manuscript index does not identify the revised controlling source",
    )
    findings += require(
        "public switch readiness" in claims.casefold(),
        "papers/HINC-001/CLAIMS.md",
        "claim matrix does not record switch readiness",
    )
    findings += require(
        "controlling source" in proof_map.casefold(),
        "papers/HINC-001/PROOF_MAP.md",
        "proof map does not identify the controlling source",
    )

    references = (
        root / "papers/HINC-001/manuscript/references.bib"
    ).read_text(encoding="utf-8")
    for required_reference in (
        "1403.3597",
        "2507.12321",
        "1103.3218",
        "1406.0036",
    ):
        findings += require(
            required_reference in references,
            "papers/HINC-001/manuscript/references.bib",
            f"required bibliography identifier missing: {required_reference}",
        )
    findings += require(
        "1411.0836" not in references,
        "papers/HINC-001/manuscript/references.bib",
        "superseded Hermann identifier remains",
    )

    readme = (root / "README.md").read_text(encoding="utf-8")
    site = (root / "docs/index.html").read_text(encoding="utf-8")
    pages = (root / ".github/workflows/pages.yml").read_text(encoding="utf-8")

    findings += require(
        "public switch ready:        true" in readme,
        "README.md",
        "repository front door does not state switch readiness",
    )
    for site_phrase in (
        "Private public-switch preview",
        "Public switch ready",
        "Peer reviewed</span><strong>No",
        "Model/provider</span><strong>Not disclosed",
        "noindex,nofollow,noarchive,nosnippet",
    ):
        findings += require(
            site_phrase in site,
            "docs/index.html",
            f"website boundary missing: {site_phrase}",
        )
    findings += require(
        "workflow_dispatch" in pages
        and "visibility switch" in pages.casefold()
        and "deploy-pages" in pages,
        ".github/workflows/pages.yml",
        "Pages workflow is not staged for the final controlled switch",
    )

    findings.extend(scan_text(root))
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--json-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    findings = validate(root)
    errors = [item for item in findings if item.level == "ERROR"]
    result = {
        "schema_version": "n.human_ai_mathematics.public_switch_validation.v1",
        "root": str(root),
        "result": "PASS" if not errors else "FAIL",
        "error_count": len(errors),
        "finding_count": len(findings),
        "findings": [asdict(item) for item in findings],
    }
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    for item in findings:
        print(f"{item.level}: {item.path}: {item.message}")
    print(
        json.dumps(
            {"result": result["result"], "error_count": result["error_count"]},
            sort_keys=True,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
