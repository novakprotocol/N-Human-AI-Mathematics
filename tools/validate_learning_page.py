#!/usr/bin/env python3
"""Fail-closed checks for the four-path full-Lean requalification page."""
from __future__ import annotations

import argparse
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

SCHEMA = "n.human_ai_mathematics.learning_page_validation.v13"


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
    failures: list[dict[str, Any]] = []
    checks: dict[str, int] = {}

    def check(category: str, condition: bool, **context: Any) -> None:
        checks[category] = checks.get(category, 0) + 1
        if not condition:
            failures.append({"category": category, **context})

    check("page_file", page_path.is_file(), path=str(page_path))
    check("index_file", index_path.is_file(), path=str(index_path))
    page = page_path.read_text(encoding="utf-8") if page_path.is_file() else ""
    index = index_path.read_text(encoding="utf-8") if index_path.is_file() else ""

    parser = PageParser()
    parser.feed(page)

    required_page_phrases = (
        "Four Mathematical Mysteries | Full-Lean Requalification",
        "No active theorem packages under the current rule",
        "Historical public artifacts · full-Lean requalification hold",
        "Private · exact-head bootstrap PASS · F01–F07 incomplete",
        "Blocked until papers 1–3 reach FULL_PASS",
        "A01, the abstract bidual moment-kernel bridge, compiles",
        "F03 and F05 are release-critical",
        "complete manuscript-to-formal-statement fidelity review",
    )
    for phrase in required_page_phrases:
        check("required_boundary_text", phrase.lower() in page.lower(), phrase=phrase)

    forbidden_page_phrases = (
        "Active public review",
        "Private release edge",
        "HINC-001 and ABF-001 have immutable public technical-review packages",
        "public release is not authorized",
        "github.com/novakprotocol/N-MathLab",
        "agent/mcrc-fibonacci-sandpile-groups-v3",
        "papers/mcrc-fibonacci-sandpile-v3",
        "PASS_PUBLIC_TECHNICAL_REVIEW_FSG",
    )
    for phrase in forbidden_page_phrases:
        check("forbidden_text_absent", phrase.lower() not in page.lower(), phrase=phrase)

    check("unique_ids", len(parser.ids) == len(set(parser.ids)), count=len(parser.ids))
    check("one_inline_script", len(parser.inline_scripts) == 1, actual=len(parser.inline_scripts))
    check("interactive_petal", "renderPetal" in page and "mSlider" in page)
    check("interactive_hinc", "hincRecord" in page and "hincReadout" in page)
    check("interactive_abf", "abfOut" in page and "restrict" in page)
    check("interactive_acm", "renderLights" in page and "lightReadout" in page)
    check("page_size", 12_000 <= len(page.encode("utf-8")) <= 80_000, bytes=len(page.encode("utf-8")))

    required_index_phrases = (
        'href="learn.html"',
        "Three papers. One strict Lean standard.",
        "No active theorem packages",
        "Public archive · full-Lean requalification hold",
        "Private full-Lean completion hold",
        "Blocked until papers 1–3 reach FULL_PASS",
    )
    for phrase in required_index_phrases:
        check("index_integration", phrase.lower() in index.lower(), phrase=phrase)

    for phrase in (
        "HINC-001 and ABF-001 are active candidate packages",
        "Active public review",
        "Private release edge",
        "Two active packages",
        "github.com/novakprotocol/N-MathLab",
    ):
        check("index_overclaim_absent", phrase.lower() not in index.lower(), phrase=phrase)

    return {
        "schema": SCHEMA,
        "result": "PASS" if not failures else "FAIL",
        "checks": dict(sorted(checks.items())),
        "total_checks": sum(checks.values()),
        "failures": failures,
        "files": {
            "docs/learn.html": {
                "bytes": page_path.stat().st_size if page_path.is_file() else 0,
                "sha256": sha256(page_path) if page_path.is_file() else None,
            },
            "docs/index.html": {
                "bytes": index_path.stat().st_size if index_path.is_file() else 0,
                "sha256": sha256(index_path) if index_path.is_file() else None,
            },
        },
        "boundaries": {
            "active_theorem_packages": [],
            "hinc_001_full_lean_hold": True,
            "abf_001_full_lean_hold": True,
            "fsg_001_private_full_lean_hold": True,
            "acm_001_blocked": True,
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
        args.javascript_output.write_text(
            str(payload.pop("inline_javascript")),
            encoding="utf-8",
            newline="\n",
        )
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
