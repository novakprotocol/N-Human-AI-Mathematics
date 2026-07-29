#!/usr/bin/env python3
"""Validate the repository after the public visibility switch and status correction."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from public_status_checks import Finding, changed_text_files, scan_paths, status_surface_findings


def validate(root: Path) -> list[Finding]:
    findings = status_surface_findings(root)
    findings.extend(scan_paths(root, changed_text_files(root)))
    site = (root / "docs/index.html").read_text(encoding="utf-8")
    for phrase in (
        "Active candidate review, bounded formal status.",
        "Active candidate public technical review",
        "Bounded Lean PASS",
        "Bounded A01 Lean PASS",
        "HOLD -- MATHEMATICAL BLOCKER",
        "No public theorem package released",
        "Peer reviewed</span><strong>No",
    ):
        if phrase.casefold() not in site.casefold():
            findings.append(Finding("ERROR", "docs/index.html", f"public website boundary missing: {phrase}", "per_file_state_mismatch"))
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
        "schema_version": "n.human_ai_mathematics.public_state_validation.v3",
        "root": "<repo>",
        "result": "PASS" if not errors else "FAIL",
        "error_count": len(errors),
        "private_reference_findings": sum(1 for item in errors if item.category == "private_reference"),
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
