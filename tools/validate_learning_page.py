#!/usr/bin/env python3
"""Fail-closed checks for the corrected learning page and FSG hold notice."""
from __future__ import annotations

import argparse
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from public_status_checks import private_reference_findings

SCHEMA = "n.human_ai_mathematics.learning_page_validation.v14"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.inline_scripts: list[str] = []
        self._script: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if data.get("id"):
            self.ids.append(str(data["id"]))
        if tag == "a" and data.get("href"):
            self.hrefs.append(str(data["href"]))
        if tag == "script" and not data.get("src"):
            self._script = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script is not None:
            self.inline_scripts.append("".join(self._script))
            self._script = None

    def handle_data(self, data: str) -> None:
        if self._script is not None:
            self._script.append(data)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path) -> dict[str, Any]:
    page_path = root / "docs/learn.html"
    index_path = root / "docs/index.html"
    correction_path = root / "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md"
    failures: list[dict[str, Any]] = []
    checks: dict[str, int] = {}

    def check(category: str, condition: bool, **context: Any) -> None:
        checks[category] = checks.get(category, 0) + 1
        if not condition:
            failures.append({"category": category, **context})

    check("page_file", page_path.is_file(), path=str(page_path))
    check("index_file", index_path.is_file(), path=str(index_path))
    check("correction_file", correction_path.is_file(), path=str(correction_path))
    page = page_path.read_text(encoding="utf-8") if page_path.is_file() else ""
    index = index_path.read_text(encoding="utf-8") if index_path.is_file() else ""
    correction = correction_path.read_text(encoding="utf-8") if correction_path.is_file() else ""

    parser = PageParser()
    parser.feed(page)

    required_page_phrases = (
        "Mathematical Review Paths | Corrected Public Status",
        "Active candidate public technical review",
        "bounded Lean PASS",
        "bounded A01 Lean PASS",
        "HOLD -- MATHEMATICAL BLOCKER",
        "No FSG theorem package has been publicly released",
        "general educational explanation is disabled",
        "no public theorem package released",
        "Hold pending consolidation",
    )
    for phrase in required_page_phrases:
        check("required_boundary_text", phrase.casefold() in page.casefold(), phrase=phrase)

    forbidden_page_phrases = (
        "No active theorem packages",
        "Historical public artifacts",
        "full-Lean requalification hold",
        "Active theorem status suspended",
        "Private release edge",
        "renderPetal",
        "mSlider",
        "Interactive Carry-Rees petal teaching diagram",
    )
    for phrase in forbidden_page_phrases:
        check("forbidden_text_absent", phrase.casefold() not in page.casefold(), phrase=phrase)

    check("unique_ids", len(parser.ids) == len(set(parser.ids)), count=len(parser.ids))
    check("one_inline_script", len(parser.inline_scripts) == 1, actual=len(parser.inline_scripts))
    check("interactive_hinc", "hincRecord" in page and "hincReadout" in page)
    check("interactive_abf", "abfOut" in page and "restrict" in page)
    check("interactive_acm", "renderLights" in page and "lightReadout" in page)
    check("fsg_noninteractive", "hold-notice" in page and "renderPetal" not in page and "mSlider" not in page)
    check("page_size", 12_000 <= len(page.encode("utf-8")) <= 90_000, bytes=len(page.encode("utf-8")))
    for finding in private_reference_findings("docs/learn.html", page):
        check("private_reference_absent", False, path=finding.path, message=finding.message)
    for finding in private_reference_findings("docs/index.html", index):
        check("private_reference_absent", False, path=finding.path, message=finding.message)
    for finding in private_reference_findings("FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md", correction):
        check("private_reference_absent", False, path=finding.path, message=finding.message)

    required_index_phrases = (
        'href="learn.html"',
        "Active candidate review, bounded formal status.",
        "Active review</span>",
        "Bounded Lean PASS",
        "Bounded A01 Lean PASS",
        "HOLD -- MATHEMATICAL BLOCKER",
        "No public theorem package released",
    )
    for phrase in required_index_phrases:
        check("index_integration", phrase.casefold() in index.casefold(), phrase=phrase)

    for phrase in (
        "No active theorem packages",
        "Historical public artifacts",
        "Active theorem status suspended",
        "Private release edge",
    ):
        check("index_overclaim_absent", phrase.casefold() not in index.casefold(), phrase=phrase)

    required_correction_phrases = (
        "FSG-001 was never released as a public theorem package",
        "confirmed counterexample",
        "teaching preview is paused",
        "private correction is under internal review",
        "HINC-001 and ABF-001 are unaffected",
        "No external review, historical priority, peer-review status",
    )
    for phrase in required_correction_phrases:
        check("correction_record", phrase.casefold() in correction.casefold(), phrase=phrase)

    return {
        "schema": SCHEMA,
        "result": "PASS" if not failures else "FAIL",
        "checks": dict(sorted(checks.items())),
        "total_checks": sum(checks.values()),
        "failures": failures,
        "files": {
            "docs/learn.html": {"bytes": page_path.stat().st_size if page_path.is_file() else 0, "sha256": sha256(page_path) if page_path.is_file() else None},
            "docs/index.html": {"bytes": index_path.stat().st_size if index_path.is_file() else 0, "sha256": sha256(index_path) if index_path.is_file() else None},
            "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md": {"bytes": correction_path.stat().st_size if correction_path.is_file() else 0, "sha256": sha256(correction_path) if correction_path.is_file() else None},
        },
        "boundaries": {
            "hinc_001_active_review": True,
            "abf_001_active_review": True,
            "fsg_001_private_mathematical_hold": True,
            "fsg_interactive_preview_disabled": True,
            "acm_001_hold": True,
            "private_fsg_source_exposed": False,
        },
        "inline_javascript": parser.inline_scripts[0] if len(parser.inline_scripts) == 1 else "",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    parser.add_argument("--javascript-output", type=Path)
    args = parser.parse_args()
    payload = validate(args.root.resolve())
    if args.javascript_output:
        args.javascript_output.parent.mkdir(parents=True, exist_ok=True)
        args.javascript_output.write_text(str(payload.pop("inline_javascript")), encoding="utf-8", newline="\n")
    else:
        payload.pop("inline_javascript", None)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
