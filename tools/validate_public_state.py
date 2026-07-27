#!/usr/bin/env python3
"""Validate the repository only after the final public visibility switch."""

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
        "papers/HINC-001/STATUS.json",
        "reports/public-release-audit-2026-07-27.json",
        "reports/public-switch-readiness.json",
        "docs/index.html",
        "docs/styles.css",
        "docs/404.html",
        "docs/.nojekyll",
        "papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md",
    ]
    for relative in required:
        if not (root / relative).is_file():
            findings.append(Finding("ERROR", relative, "required public file missing"))
    if findings:
        return findings

    index = load(root / "research-index.json")
    hinc = load(root / "papers/HINC-001/STATUS.json")
    audit = load(root / "reports/public-release-audit-2026-07-27.json")
    readiness = load(root / "reports/public-switch-readiness.json")
    site = (root / "docs/index.html").read_text(encoding="utf-8")

    findings += require(
        index.get("public_release_authorized") is True,
        "research-index.json",
        "public_release_authorized must be true after the switch",
    )
    findings += require(
        index.get("public_switch_ready") is True,
        "research-index.json",
        "public_switch_ready must remain true",
    )
    findings += require(
        index.get("release_channel") == "public_review",
        "research-index.json",
        "release_channel must be public_review",
    )
    findings += require(
        index.get("release_version") == "0.1.0-public-review",
        "research-index.json",
        "unexpected public version",
    )

    release = hinc.get("release", {})
    findings += require(
        release.get("public_authorized") is True,
        "papers/HINC-001/STATUS.json",
        "HINC public_authorized must be true",
    )
    findings += require(
        release.get("public_switch_ready") is True,
        "papers/HINC-001/STATUS.json",
        "HINC public_switch_ready must remain true",
    )
    findings += require(
        release.get("channel") == "public_review",
        "papers/HINC-001/STATUS.json",
        "HINC channel must be public_review",
    )
    findings += require(
        release.get("version") == "0.1.0-public-review",
        "papers/HINC-001/STATUS.json",
        "HINC public version mismatch",
    )
    findings += require(
        isinstance(release.get("release_date"), str) and bool(release.get("release_date")),
        "papers/HINC-001/STATUS.json",
        "release_date must be recorded",
    )
    findings += require(
        release.get("specific_model_disclosed") is False
        and release.get("specific_provider_disclosed") is False,
        "papers/HINC-001/STATUS.json",
        "model/provider disclosure boundary failed",
    )

    findings += require(
        audit.get("result") == "PUBLIC_RELEASED",
        "reports/public-release-audit-2026-07-27.json",
        "release audit must say PUBLIC_RELEASED",
    )
    audit_scope = audit.get("release_scope", {})
    findings += require(
        audit_scope.get("repository_visibility") == "public"
        and audit_scope.get("public_switch_ready") is True
        and audit_scope.get("visibility_change_executed") is True,
        "reports/public-release-audit-2026-07-27.json",
        "release audit visibility state is inconsistent",
    )

    findings += require(
        readiness.get("result") == "PUBLIC_RELEASED",
        "reports/public-switch-readiness.json",
        "switch receipt must say PUBLIC_RELEASED",
    )
    findings += require(
        readiness.get("repository_visibility") == "public"
        and readiness.get("visibility_change_executed") is True,
        "reports/public-switch-readiness.json",
        "switch receipt visibility state is inconsistent",
    )

    for phrase in (
        "Public technical review",
        "Candidate mathematics open for technical review",
        "Peer reviewed</span><strong>No",
        "Model/provider</span><strong>Not disclosed",
    ):
        findings += require(
            phrase in site,
            "docs/index.html",
            f"public website boundary missing: {phrase}",
        )
    findings += require(
        "noindex" not in site.casefold(),
        "docs/index.html",
        "public website still contains a noindex directive",
    )
    findings += require(
        "Private public-switch preview" not in site,
        "docs/index.html",
        "public website still uses private-preview language",
    )

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
        "schema_version": "n.human_ai_mathematics.public_state_validation.v1",
        "root": str(root),
        "result": "PASS" if not errors else "FAIL",
        "error_count": len(errors),
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
    print(json.dumps({"result": result["result"], "error_count": len(errors)}))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
