#!/usr/bin/env python3
"""Fail-closed validator for the corrected public candidate-review state."""

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
    "formal-verification-status.json",
    "PAPER_1_3_FULL_LEAN_STATUS.json",
    "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md",
    "PUBLIC_REVIEW_RELEASE.md",
    "PUBLIC_REVIEW_FORMALIZATION_HOLD_2026-07-29.md",
    "FULL_LEAN_VERIFICATION_PROGRAM.md",
    "FULL_LEAN_RELEASE_STANDARD.md",
    "PUBLICATION_WORKFLOW.md",
    "HUMAN_AI_COLLABORATION_RECORD.md",
    "HUMAN_AI_MATHEMATICS_PRIOR_ART.md",
    "OPEN_REVIEW_CHALLENGE.md",
    "RIGHTS_AND_LICENSING.md",
    "CITATION.cff",
    "papers/HINC-001/README.md",
    "papers/HINC-001/STATUS.json",
    "papers/HINC-001/FORMAL_VERIFICATION.md",
    "papers/ABF-001/README.md",
    "papers/ABF-001/STATUS.json",
    "papers/ABF-001/FORMAL_VERIFICATION.md",
    "reports/publication-gates/HINC-001.json",
    "reports/publication-gates/ABF-001.json",
    "schemas/research-index.schema.json",
    "schemas/paper-status.schema.json",
    "docs/index.html",
    "docs/learn.html",
    "docs/styles.css",
    "docs/404.html",
    "docs/.nojekyll",
    ".github/workflows/pages.yml",
    ".github/workflows/validate.yml",
    ".github/workflows/validate-status-consistency.yml",
    "tools/validate_publication.py",
    "tools/validate_publication_v2.py",
    "tools/validate_public_release.py",
    "tools/validate_public_release_v2.py",
    "tools/validate_public_state.py",
    "tools/validate_status_consistency.py",
    "tools/validate_learning_page.py",
    "tools/validate_full_lean_portfolio.py",
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

SCAN_EXCLUDED_PATHS = frozenset(
    {
        "tools/Invoke-PublicSwitchPreflight.ps1",
        "tools/validate_public_release.py",
        "tools/validate_public_release_v2.py",
        "tools/validate_publication.py",
    }
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

PRIVATE_FSG_PATTERNS = (
    "github.com/novakprotocol/N-MathLab",
    "PR #428",
    "papers/mcrc-fibonacci",
    "agent/mcrc-fibonacci",
    "PASS_PUBLIC_TECHNICAL_REVIEW_FSG",
)

OVERCLAIM_PATTERNS = (
    ("peer-review overclaim", re.compile(r"peer\\s+reviewed\\s*:\\s*yes|peer_reviewed\\s*=\\s*true", re.IGNORECASE)),
    ("historical-priority overclaim", re.compile(r"historical\\s+priority\\s*:\\s*established|historical_priority_established\\s*=\\s*true", re.IGNORECASE)),
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


def should_skip_path(path: Path) -> bool:
    return any(part in {".git", ".lake", ".venv", "__pycache__"} for part in path.parts)


def scan_text(root: Path) -> list[Finding]:
    findings: list[Finding] = []

    for path in sorted(root.rglob("*")):
        if should_skip_path(path) or not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue

        relative = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(Finding("ERROR", relative, "declared text file is not UTF-8"))
            continue

        is_detector_file = relative in SCAN_EXCLUDED_PATHS or relative.startswith("tools/validate_") or relative.startswith(".github/workflows/validate-")
        if not is_detector_file:
            for label, pattern in FORBIDDEN_PATTERNS:
                match = pattern.search(text)
                if match:
                    line = text.count("\n", 0, match.start()) + 1
                    findings.append(Finding("ERROR", f"{relative}:{line}", f"forbidden {label}"))

            folded = text.casefold()
            for pattern in PRIVATE_FSG_PATTERNS:
                position = folded.find(pattern.casefold())
                if position >= 0:
                    line = text.count("\n", 0, position) + 1
                    findings.append(Finding("ERROR", f"{relative}:{line}", "private FSG source or review link appears in public source"))

            for label, pattern in OVERCLAIM_PATTERNS:
                match = pattern.search(text)
                if match:
                    line = text.count("\n", 0, match.start()) + 1
                    findings.append(Finding("ERROR", f"{relative}:{line}", label))

    return findings


def validate(root: Path) -> list[Finding]:
    findings: list[Finding] = []

    for relative in sorted(REQUIRED_FILES):
        if not (root / relative).is_file():
            findings.append(Finding("ERROR", relative, "required public-state file missing"))

    if findings:
        return findings

    index = load_json(root / "research-index.json")
    portfolio = load_json(root / "formal-verification-status.json")
    matrix = load_json(root / "PAPER_1_3_FULL_LEAN_STATUS.json")
    hinc = load_json(root / "papers/HINC-001/STATUS.json")
    abf = load_json(root / "papers/ABF-001/STATUS.json")
    hinc_gate = load_json(root / "reports/publication-gates/HINC-001.json")
    abf_gate = load_json(root / "reports/publication-gates/ABF-001.json")

    findings += require(index.get("public_release_authorized") is True, "research-index.json", "public_release_authorized must be true for the already-public review state")
    findings += require(index.get("public_switch_ready") is True, "research-index.json", "public_switch_ready must remain true")
    findings += require(index.get("release_channel") == "public_review", "research-index.json", "release_channel must be public_review")
    findings += require(index.get("release_version") == "0.1.0-public-review", "research-index.json", "release_version must be 0.1.0-public-review")
    findings += require(index.get("specific_model_disclosed") is False, "research-index.json", "specific_model_disclosed must remain false")
    findings += require(index.get("specific_provider_disclosed") is False, "research-index.json", "specific_provider_disclosed must remain false")

    papers = {item.get("id"): item for item in index.get("papers", []) if isinstance(item, dict)}
    findings += require(set(papers) == {"HINC-001", "ABF-001", "FSG-001", "ACM-001"}, "research-index.json", "paper portfolio does not match the governed four-paper order")
    expected_states = {"HINC-001": "active_review", "ABF-001": "active_review", "FSG-001": "hold", "ACM-001": "hold"}
    for paper_id, expected in expected_states.items():
        findings += require(papers.get(paper_id, {}).get("state") == expected, "research-index.json", f"{paper_id} state must be {expected}")

    expected_releases = {
        "HINC-001": (hinc, "PARTIAL_PASS_BOUNDED_LEAN_VERIFICATION"),
        "ABF-001": (abf, "PARTIAL_PASS_BOUNDED_A01_LEAN_VERIFICATION"),
    }
    for paper_id, (status, formal_status) in expected_releases.items():
        release = status.get("release", {})
        formal = status.get("formal_verification", {})
        path = f"papers/{paper_id}/STATUS.json"
        findings += require(release.get("public_authorized") is True, path, f"{paper_id} public review must be authorized")
        findings += require(release.get("public_switch_ready") is True, path, f"{paper_id} public_switch_ready must be true")
        findings += require(release.get("channel") == "public_review", path, f"{paper_id} channel must be public_review")
        findings += require(release.get("version") == "0.1.0-public-review", path, f"{paper_id} version must be 0.1.0-public-review")
        findings += require(release.get("doi") is None, path, f"{paper_id} DOI must not be claimed")
        findings += require(formal.get("status") == formal_status, path, f"{paper_id} bounded formal status mismatch")
        findings += require(formal.get("full_manuscript_lean_verified") is False, path, f"{paper_id} must not claim full-manuscript Lean verification")
        findings += require(formal.get("claim_map_complete") is False, path, f"{paper_id} must not claim complete formal claim map")

    findings += require(hinc_gate.get("status") == "PASS_PUBLIC_TECHNICAL_REVIEW", "reports/publication-gates/HINC-001.json", "HINC publication gate must remain public technical review PASS")
    findings += require(abf_gate.get("status") == "PASS_PUBLIC_TECHNICAL_REVIEW", "reports/publication-gates/ABF-001.json", "ABF publication gate must remain public technical review PASS")

    expected_portfolio = {
        "HINC-001": ("ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW", "PARTIAL_PASS"),
        "ABF-001": ("ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW", "PARTIAL_PASS"),
        "FSG-001": ("PRIVATE_CANDIDATE_MATHEMATICAL_BLOCKER_HOLD", "HOLD_MATHEMATICAL_BLOCKER"),
        "ACM-001": ("HOLD_PENDING_CONSOLIDATION", "HOLD_PENDING_CONSOLIDATION"),
    }
    for paper_id, (public_state, formal_state) in expected_portfolio.items():
        record = portfolio.get("portfolio", {}).get(paper_id, {})
        findings += require(record.get("public_state") == public_state, "formal-verification-status.json", f"{paper_id} public state mismatch")
        findings += require(record.get("formal_status") == formal_state, "formal-verification-status.json", f"{paper_id} formal state mismatch")
        findings += require(record.get("full_manuscript_lean_verified") is False, "formal-verification-status.json", f"{paper_id} must not claim FULL_PASS")
        matrix_record = matrix.get("papers", {}).get(paper_id, {})
        findings += require(matrix_record.get("formal_status") == formal_state, "PAPER_1_3_FULL_LEAN_STATUS.json", f"{paper_id} matrix formal state mismatch")

    fsg = portfolio.get("portfolio", {}).get("FSG-001", {})
    findings += require(fsg.get("public_theorem_package_released") is False, "formal-verification-status.json", "FSG public theorem package must remain unreleased")
    findings += require(fsg.get("public_mathematical_release_authorized") is False, "formal-verification-status.json", "FSG public release must remain unauthorized")
    findings += require(fsg.get("private_correction_under_internal_review") is True, "formal-verification-status.json", "FSG private correction review marker missing")

    readme = (root / "README.md").read_text(encoding="utf-8")
    site = (root / "docs/index.html").read_text(encoding="utf-8")
    learn = (root / "docs/learn.html").read_text(encoding="utf-8")
    correction = (root / "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md").read_text(encoding="utf-8")

    for phrase in (
        "active public candidate review:  HINC-001, ABF-001",
        "FSG-001:                         private; HOLD -- MATHEMATICAL BLOCKER",
        "ACM-001:                         hold pending consolidation",
    ):
        findings += require(phrase in readme, "README.md", f"front-door status missing: {phrase}")

    for phrase in (
        "Active candidate public technical review",
        "Bounded Lean PASS",
        "Bounded A01 Lean PASS",
        "Full manuscript incomplete",
        "HOLD -- MATHEMATICAL BLOCKER",
        "No public theorem package released",
        "Hold pending consolidation",
    ):
        findings += require(phrase.casefold() in site.casefold(), "docs/index.html", f"website boundary missing: {phrase}")

    for phrase in (
        "FSG-001 is paused.",
        "disproved before public release",
        "No FSG theorem package has been publicly released",
        "does not publish private paths",
        "any claim that the private correction has passed review",
    ):
        findings += require(phrase.casefold() in learn.casefold(), "docs/learn.html", f"FSG hold notice missing: {phrase}")

    for phrase in (
        "FSG-001 was never released as a public theorem package",
        "confirmed counterexample",
        "teaching preview is paused",
        "private correction is under internal review",
        "HINC-001 and ABF-001 are unaffected",
        "No external review, historical priority, peer-review status, journal acceptance",
    ):
        findings += require(phrase.casefold() in correction.casefold(), "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md", f"correction record missing: {phrase}")

    pages = (root / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    findings += require("deploy-pages" in pages, ".github/workflows/pages.yml", "Pages workflow must retain deploy-pages job")

    findings.extend(scan_text(root))
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    findings = validate(root)
    errors = [item for item in findings if item.level == "ERROR"]
    result = {
        "schema_version": "n.human_ai_mathematics.corrected_public_review_validation.v2",
        "root": str(root),
        "result": "PASS" if not errors else "FAIL",
        "error_count": len(errors),
        "finding_count": len(findings),
        "findings": [asdict(item) for item in findings],
    }
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for item in findings:
        print(f"{item.level}: {item.path}: {item.message}")
    print(json.dumps({"result": result["result"], "error_count": result["error_count"]}, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())