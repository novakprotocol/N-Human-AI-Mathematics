#!/usr/bin/env python3
"""Fail-closed validator for the corrected public candidate-review state."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from public_status_checks import Finding, require, changed_text_files, scan_paths, status_surface_findings


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
    "schemas/publication-gate.schema.json",
    "schemas/full-lean-portfolio.schema.json",
    "schemas/paper-1-3-full-lean-status.schema.json",
    "requirements-validation.txt",
    "docs/index.html",
    "docs/learn.html",
    "docs/styles.css",
    "docs/404.html",
    "docs/.nojekyll",
    ".github/workflows/pages.yml",
    ".github/workflows/validate.yml",
    ".github/workflows/validate-status-consistency.yml",
    ".github/workflows/validate-learning-page.yml",
    "tools/public_status_checks.py",
    "tools/validate_json_schema.py",
    "tools/validate_internal_links.py",
    "tools/validate_public_surface_scan.py",
    "tools/test_public_status_mutations.py",
    "tools/test_json_schema_negative_controls.py",
    "tools/test_internal_link_negative_control.py",
    "tools/validate_publication.py",
    "tools/validate_publication_v2.py",
    "tools/validate_publication_gate.py",
    "tools/validate_public_release.py",
    "tools/validate_public_release_v2.py",
    "tools/validate_public_state.py",
    "tools/validate_status_consistency.py",
    "tools/validate_learning_page.py",
    "tools/validate_full_lean_portfolio.py",
}


def validate(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for relative in sorted(REQUIRED_FILES):
        findings += require((root / relative).is_file(), relative, "required public-state file missing", "required_file")
    if any(item.category == "required_file" for item in findings):
        return findings

    findings.extend(status_surface_findings(root))
    findings.extend(scan_paths(root, changed_text_files(root)))

    readme = (root / "README.md").read_text(encoding="utf-8")
    site = (root / "docs/index.html").read_text(encoding="utf-8")
    learn = (root / "docs/learn.html").read_text(encoding="utf-8")
    correction = (root / "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md").read_text(encoding="utf-8")
    pages = (root / ".github/workflows/pages.yml").read_text(encoding="utf-8")

    for phrase in (
        "active public candidate review:  HINC-001, ABF-001",
        "FSG-001:                         private; HOLD -- MATHEMATICAL BLOCKER",
        "ACM-001:                         hold pending consolidation",
    ):
        findings += require(phrase in readme, "README.md", f"front-door status missing: {phrase}", "per_file_state_mismatch")

    for phrase in (
        "Active candidate public technical review",
        "Bounded Lean PASS",
        "Bounded A01 Lean PASS",
        "Full manuscript incomplete",
        "HOLD -- MATHEMATICAL BLOCKER",
        "No public theorem package released",
        "Hold pending consolidation",
    ):
        findings += require(phrase.casefold() in site.casefold(), "docs/index.html", f"website boundary missing: {phrase}", "per_file_state_mismatch")

    for phrase in (
        "FSG-001 is paused.",
        "disproved before public release",
        "No FSG theorem package has been publicly released",
        "does not publish private paths",
        "any claim that the private correction has passed review",
    ):
        findings += require(phrase.casefold() in learn.casefold(), "docs/learn.html", f"FSG hold notice missing: {phrase}", "fsg_hold")

    for phrase in (
        "FSG-001 was never released as a public theorem package",
        "confirmed counterexample",
        "teaching preview is paused",
        "private correction is under internal review",
        "HINC-001 and ABF-001 are unaffected",
        "ACM-001 remains on hold pending consolidation",
        "No external review, historical priority, peer-review status",
    ):
        findings += require(phrase.casefold() in correction.casefold(), "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md", f"correction record missing: {phrase}", "per_file_state_mismatch")

    for phrase in (
        "deploy-pages",
        "HINC-001</dt><dd>Active candidate public technical review",
        "ABF-001</dt><dd>Active candidate public technical review",
        "FSG private mathematical hold",
        "ACM consolidation hold",
    ):
        findings += require(phrase.casefold() in pages.casefold(), ".github/workflows/pages.yml", f"Pages workflow missing corrected assertion: {phrase}", "workflow_boundary")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    findings = validate(root)
    errors = [item for item in findings if item.level == "ERROR"]
    result = {
        "schema_version": "n.human_ai_mathematics.corrected_public_review_validation.v3",
        "root": "<repo>",
        "result": "PASS" if not errors else "FAIL",
        "error_count": len(errors),
        "finding_count": len(findings),
        "private_reference_findings": sum(1 for item in errors if item.category == "private_reference"),
        "private_detector_literals": sum(1 for item in errors if item.category == "private_reference"),
        "validator_workflow_private_scan_exclusions": 0,
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
