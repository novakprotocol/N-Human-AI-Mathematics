#!/usr/bin/env python3
"""Fail-closed validator for the Human + LLM public-review release."""

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
    "HUMAN_AI_COLLABORATION_RECORD.md",
    "HUMAN_AI_MATHEMATICS_PRIOR_ART.md",
    "OPEN_REVIEW_CHALLENGE.md",
    "PUBLIC_REVIEW_RELEASE.md",
    "RIGHTS_AND_LICENSING.md",
    "CITATION.cff",
    "reports/public-release-audit-2026-07-27.json",
    "papers/HINC-001/STATUS.json",
    "papers/HINC-001/AI_DISCLOSURE.md",
    "papers/HINC-001/THIRD_PARTY_NOTICES.md",
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

# Construct withheld identifiers without embedding them as contiguous public
# strings in this validator. The exact identities remain private pending
# separate human legal and editorial review.
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

        # Skip only the exact current validator source because its dynamically
        # assembled strings are the release gate's detection vocabulary.
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
                        "withheld model or provider identifier appears in public source",
                    )
                )

    return findings


def validate(root: Path) -> list[Finding]:
    findings: list[Finding] = []

    for relative in sorted(REQUIRED_FILES):
        if not (root / relative).is_file():
            findings.append(Finding("ERROR", relative, "required release file missing"))

    if findings:
        return findings

    index = load_json(root / "research-index.json")
    hinc = load_json(root / "papers/HINC-001/STATUS.json")
    audit = load_json(root / "reports/public-release-audit-2026-07-27.json")
    research_schema = load_json(root / "schemas/research-index.schema.json")
    paper_schema = load_json(root / "schemas/paper-status.schema.json")

    findings += require(
        index.get("public_release_authorized") is True,
        "research-index.json",
        "public release is not authorized",
    )
    findings += require(
        index.get("release_channel") == "public_review",
        "research-index.json",
        "release_channel must be public_review",
    )
    findings += require(
        index.get("release_version") == "0.1.0-public-review",
        "research-index.json",
        "unexpected public-review version",
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

    hinc_release = hinc.get("release", {})
    findings += require(
        hinc_release.get("public_authorized") is True,
        "papers/HINC-001/STATUS.json",
        "HINC public review is not authorized",
    )
    findings += require(
        hinc_release.get("channel") == "public_review",
        "papers/HINC-001/STATUS.json",
        "HINC release channel must be public_review",
    )
    findings += require(
        hinc_release.get("version") == "0.1.0-public-review",
        "papers/HINC-001/STATUS.json",
        "HINC public-review version mismatch",
    )
    findings += require(
        hinc_release.get("doi") is None,
        "papers/HINC-001/STATUS.json",
        "DOI must remain null until assigned",
    )
    findings += require(
        hinc_release.get("specific_model_disclosed") is False,
        "papers/HINC-001/STATUS.json",
        "HINC specific_model_disclosed must be false",
    )
    findings += require(
        hinc_release.get("specific_provider_disclosed") is False,
        "papers/HINC-001/STATUS.json",
        "HINC specific_provider_disclosed must be false",
    )

    findings += require(
        audit.get("result") == "PASS_WITH_DECLARED_LIMITATIONS",
        "reports/public-release-audit-2026-07-27.json",
        "public release audit is not PASS_WITH_DECLARED_LIMITATIONS",
    )
    scope = audit.get("release_scope", {})
    findings += require(
        scope.get("complete_public_review_packages") == ["HINC-001"],
        "reports/public-release-audit-2026-07-27.json",
        "release scope must contain exactly HINC-001",
    )
    findings += require(
        scope.get("peer_reviewed") is False,
        "reports/public-release-audit-2026-07-27.json",
        "peer-review boundary is not false",
    )
    findings += require(
        scope.get("specific_model_disclosed") is False,
        "reports/public-release-audit-2026-07-27.json",
        "audit specific_model_disclosed must be false",
    )
    findings += require(
        scope.get("specific_provider_disclosed") is False,
        "reports/public-release-audit-2026-07-27.json",
        "audit specific_provider_disclosed must be false",
    )

    required_index_fields = set(research_schema.get("required", []))
    for field in (
        "release_channel",
        "release_version",
        "specific_model_disclosed",
        "specific_provider_disclosed",
    ):
        findings += require(
            field in required_index_fields,
            "schemas/research-index.schema.json",
            f"research schema does not require {field}",
        )

    release_required = set(
        paper_schema.get("properties", {})
        .get("release", {})
        .get("required", [])
    )
    for field in (
        "channel",
        "release_date",
        "specific_model_disclosed",
        "specific_provider_disclosed",
    ):
        findings += require(
            field in release_required,
            "schemas/paper-status.schema.json",
            f"paper release schema does not require {field}",
        )

    references = (root / "papers/HINC-001/manuscript/references.bib").read_text(
        encoding="utf-8"
    )
    findings += require(
        "eprint = {1403.3597}" in references,
        "papers/HINC-001/manuscript/references.bib",
        "Hermann arXiv identifier is not corrected",
    )
    findings += require(
        "@misc{Elduque2025" in references and "year = {2025}" in references,
        "papers/HINC-001/manuscript/references.bib",
        "Elduque preprint metadata is not aligned to 2025",
    )
    findings += require(
        "1411.0836" not in references,
        "papers/HINC-001/manuscript/references.bib",
        "superseded Hermann identifier remains",
    )

    readme = (root / "README.md").read_text(encoding="utf-8")
    collaboration = (root / "HUMAN_AI_COLLABORATION_RECORD.md").read_text(
        encoding="utf-8"
    )
    prior_art = (root / "HUMAN_AI_MATHEMATICS_PRIOR_ART.md").read_text(
        encoding="utf-8"
    )
    site = (root / "docs/index.html").read_text(encoding="utf-8")

    findings += require(
        "human-led, LLM-assisted" in readme,
        "README.md",
        "approved public wording is missing",
    )
    findings += require(
        "one or more large language models" in collaboration,
        "HUMAN_AI_COLLABORATION_RECORD.md",
        "category-level collaboration disclosure is missing",
    )
    findings += require(
        "does **not** claim to be the first" in prior_art,
        "HUMAN_AI_MATHEMATICS_PRIOR_ART.md",
        "broad first-in-history claim is not rejected",
    )
    findings += require(
        "Peer reviewed</span><strong>No" in site,
        "docs/index.html",
        "website peer-review boundary missing",
    )
    findings += require(
        "Model/provider</span><strong>Not disclosed" in site,
        "docs/index.html",
        "website identity boundary missing",
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
        "schema_version": "n.human_ai_mathematics.public_release_validation.v2",
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
            {
                "result": result["result"],
                "error_count": result["error_count"],
            },
            sort_keys=True,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
