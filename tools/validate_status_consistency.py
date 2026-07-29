#!/usr/bin/env python3
"""Reconcile each public status surface against the canonical corrected state."""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict
from pathlib import Path

from public_status_checks import (
    CANONICAL_STATE,
    CONTROLLED_JSON_FILES,
    CONTROLLED_TEXT_FILES,
    changed_text_files,
    scan_paths,
    status_surface_findings,
    tracked_text_files,
)


SCHEMA = "n.human_ai_mathematics.status_consistency_validation.v3"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path, scan_changed_against: str | None = "origin/main") -> dict:
    findings = status_surface_findings(root)

    if scan_changed_against:
        try:
            paths = changed_text_files(root, scan_changed_against)
        except Exception:
            paths = tracked_text_files(root)
    else:
        paths = tracked_text_files(root)
    findings.extend(scan_paths(root, paths))

    errors = [item for item in findings if item.level == "ERROR"]
    per_file_state_mismatches = sum(1 for item in errors if item.category == "per_file_state_mismatch")
    publication_conflicts = sum(
        1
        for item in errors
        if item.category
        in {
            "publication_state",
            "current_release_channel",
            "per_file_state_mismatch",
            "obsolete_current_state",
            "fsg_hold",
            "fsg_release",
            "acm_hold",
        }
    )
    formal_conflicts = sum(
        1
        for item in errors
        if item.category in {"formal_state", "full_lean_boundary", "full_lean_overclaim"}
    )
    private_references = sum(1 for item in errors if item.category == "private_reference")
    validator_exclusions = sum(1 for item in errors if item.category == "validator_workflow_exclusion")
    credential_or_personal = sum(1 for item in errors if item.category == "credential_or_personal_path")
    full_lean_overclaim = sum(1 for item in errors if item.category == "full_lean_overclaim")
    peer_review_overclaim = sum(1 for item in errors if item.category == "peer_review_overclaim")
    priority_overclaim = sum(1 for item in errors if item.category == "historical_priority_overclaim")

    controlled_files = [root / rel for rel in (*CONTROLLED_JSON_FILES, *CONTROLLED_TEXT_FILES)]
    return {
        "schema": SCHEMA,
        "result": "PASS" if not errors else "FAIL",
        "canonical_state": CANONICAL_STATE,
        "total_findings": len(findings),
        "error_count": len(errors),
        "findings": [asdict(item) for item in findings],
        "conflicting_publication_states": publication_conflicts,
        "conflicting_formal_states": formal_conflicts,
        "per_file_state_mismatches": per_file_state_mismatches,
        "private_fsg_references_in_changed_files": private_references,
        "private_detector_literals": private_references,
        "validator_workflow_private_scan_exclusions": validator_exclusions,
        "credential_or_personal_path_findings": credential_or_personal,
        "hinc_active_status_present": "yes"
        if not any("HINC-001" in item.message for item in errors if item.category == "per_file_state_mismatch")
        else "no",
        "abf_active_status_present": "yes"
        if not any("ABF-001" in item.message for item in errors if item.category == "per_file_state_mismatch")
        else "no",
        "fsg_mathematical_hold_present": "yes"
        if not any(item.category in {"fsg_hold", "fsg_release"} for item in errors)
        else "no",
        "acm_hold_present": "yes"
        if not any(item.category == "acm_hold" for item in errors)
        else "no",
        "full_lean_overclaim": full_lean_overclaim,
        "peer_review_overclaim": peer_review_overclaim,
        "historical_priority_overclaim": priority_overclaim,
        "scanned_text_file_count": len(paths),
        "files": {
            path.relative_to(root).as_posix(): {
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in controlled_files
            if path.is_file()
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    parser.add_argument("--scan-all", action="store_true")
    parser.add_argument("--changed-against", default="origin/main")
    args = parser.parse_args()

    payload = validate(args.root.resolve(), None if args.scan_all else args.changed_against)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
