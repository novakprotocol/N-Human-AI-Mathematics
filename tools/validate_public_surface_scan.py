#!/usr/bin/env python3
"""Scan changed public text surfaces for credentials and private references."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from public_status_checks import credential_findings, private_reference_findings, tracked_text_files, validator_workflow_exclusion_findings


def validate(root: Path) -> dict:
    files = tracked_text_files(root)
    records = []
    findings = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        body = path.read_text(encoding='utf-8')
        file_findings = credential_findings(rel, body) + private_reference_findings(rel, body) + validator_workflow_exclusion_findings(rel, body)
        findings.extend(file_findings)
        records.append({'file': rel, 'finding_count': len(file_findings)})
    credential = [item for item in findings if item.message in {'GitHub token', 'private-key material'}]
    personal = [item for item in findings if item.category == 'credential_or_personal_path' and 'path' in item.message]
    private_reference = [item for item in findings if item.category == 'private_reference']
    private_branch_path = [item for item in private_reference if 'branch' in item.message or 'path' in item.message]
    exclusions = [item for item in findings if item.category == 'validator_workflow_exclusion']
    payload = {
        'schema': 'n.human_ai_mathematics.public_surface_scan.v1',
        'result': 'PASS' if not findings else 'FAIL',
        'tracked_text_files_scanned': len(files),
        'credential_pattern_findings': len(credential),
        'personal_path_findings': len(personal),
        'private_reference_findings': len(private_reference),
        'private_branch_path_findings': len(private_branch_path),
        'private_detector_literals': len(private_reference),
        'validator_workflow_exclusions': len(exclusions),
        'records': records,
        'findings': [asdict(item) for item in findings],
    }
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    payload = validate(args.root.resolve())
    text = json.dumps(payload, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8', newline='\n')
    print(text, end='')
    return 0 if payload['result'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
