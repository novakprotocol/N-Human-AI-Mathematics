#!/usr/bin/env python3
"""Validate the repository after the public visibility switch and status correction."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    level: str
    path: str
    message: str


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, path: str, message: str) -> list[Finding]:
    return [] if condition else [Finding("ERROR", path, message)]


def validate(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    required = [
        "research-index.json",
        "formal-verification-status.json",
        "PAPER_1_3_FULL_LEAN_STATUS.json",
        "papers/HINC-001/STATUS.json",
        "papers/ABF-001/STATUS.json",
        "reports/publication-gates/HINC-001.json",
        "reports/publication-gates/ABF-001.json",
        "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md",
        "docs/index.html",
        "docs/learn.html",
        "docs/styles.css",
        "docs/404.html",
        "docs/.nojekyll",
    ]
    for relative in required:
        if not (root / relative).is_file():
            findings.append(Finding("ERROR", relative, "required public file missing"))
    if findings:
        return findings

    index = load(root / "research-index.json")
    portfolio = load(root / "formal-verification-status.json")
    hinc = load(root / "papers/HINC-001/STATUS.json")
    abf = load(root / "papers/ABF-001/STATUS.json")
    hinc_gate = load(root / "reports/publication-gates/HINC-001.json")
    abf_gate = load(root / "reports/publication-gates/ABF-001.json")
    site = (root / "docs/index.html").read_text(encoding="utf-8")
    learn = (root / "docs/learn.html").read_text(encoding="utf-8")
    correction = (root / "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md").read_text(encoding="utf-8")

    findings += require(index.get("repository_visibility_required") == "public", "research-index.json", "repository_visibility_required must be public")
    findings += require(index.get("public_release_authorized") is True, "research-index.json", "public_release_authorized must be true for existing HINC/ABF candidate releases")
    findings += require(index.get("public_switch_ready") is True, "research-index.json", "public_switch_ready must remain true")
    findings += require(index.get("release_channel") == "public_review", "research-index.json", "release_channel must be public_review")
    findings += require(index.get("release_version") == "0.1.0-public-review", "research-index.json", "unexpected public version")

    papers = {item.get("id"): item for item in index.get("papers", [])}
    findings += require(papers.get("HINC-001", {}).get("state") == "active_review", "research-index.json", "HINC-001 must be active_review")
    findings += require(papers.get("ABF-001", {}).get("state") == "active_review", "research-index.json", "ABF-001 must be active_review")
    findings += require(papers.get("FSG-001", {}).get("state") == "hold", "research-index.json", "FSG-001 must remain hold")
    findings += require(papers.get("ACM-001", {}).get("state") == "hold", "research-index.json", "ACM-001 must remain hold")
    findings += require("item (v) false as written" in str(papers.get("FSG-001", {}).get("formal_verification", {})).casefold(), "research-index.json", "FSG mathematical blocker missing")

    for paper_id, status in (("HINC-001", hinc), ("ABF-001", abf)):
        release = status.get("release", {})
        findings += require(release.get("public_authorized") is True, f"papers/{paper_id}/STATUS.json", f"{paper_id} public_authorized must be true")
        findings += require(release.get("public_switch_ready") is True, f"papers/{paper_id}/STATUS.json", f"{paper_id} public_switch_ready must remain true")
        findings += require(release.get("channel") == "public_review", f"papers/{paper_id}/STATUS.json", f"{paper_id} channel must be public_review")
        findings += require(status.get("formal_verification", {}).get("full_manuscript_lean_verified") is False, f"papers/{paper_id}/STATUS.json", f"{paper_id} must not claim full manuscript Lean verification")

    findings += require(hinc_gate.get("status") == "PASS_PUBLIC_TECHNICAL_REVIEW", "reports/publication-gates/HINC-001.json", "HINC publication gate must be public technical review PASS")
    findings += require(abf_gate.get("status") == "PASS_PUBLIC_TECHNICAL_REVIEW", "reports/publication-gates/ABF-001.json", "ABF publication gate must be public technical review PASS")
    findings += require(portfolio.get("active_public_candidate_review_packages") == ["HINC-001", "ABF-001"], "formal-verification-status.json", "active candidate review package list mismatch")
    findings += require(portfolio.get("papers_with_full_pass") == [], "formal-verification-status.json", "no paper may have FULL_PASS")
    findings += require(portfolio.get("fsg_public_release_authorized") is False, "formal-verification-status.json", "FSG public release must remain unauthorized")

    for phrase in (
        "Active candidate review, bounded formal status.",
        "Active candidate public technical review",
        "Bounded Lean PASS",
        "Bounded A01 Lean PASS",
        "HOLD -- MATHEMATICAL BLOCKER",
        "No public theorem package released",
        "Peer reviewed</span><strong>No",
    ):
        findings += require(phrase.casefold() in site.casefold(), "docs/index.html", f"public website boundary missing: {phrase}")

    for phrase in (
        "No active theorem packages",
        "Historical public artifacts",
        "Active theorem status suspended",
        "github.com/novakprotocol/N-MathLab",
        "PR #428",
    ):
        findings += require(phrase.casefold() not in (site + learn + correction).casefold(), "docs", f"forbidden public/private or superseded wording remains: {phrase}")

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
        "schema_version": "n.human_ai_mathematics.public_state_validation.v2",
        "root": str(root),
        "result": "PASS" if not errors else "FAIL",
        "error_count": len(errors),
        "findings": [asdict(item) for item in findings],
    }
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for item in findings:
        print(f"{item.level}: {item.path}: {item.message}")
    print(json.dumps({"result": result["result"], "error_count": len(errors)}))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())