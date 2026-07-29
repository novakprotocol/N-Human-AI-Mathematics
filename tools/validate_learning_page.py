#!/usr/bin/env python3
"""Fail-closed checks for the public four-path learning page."""
from __future__ import annotations

import argparse
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

SCHEMA = "n.human_ai_mathematics.learning_page_validation.v12"


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

    for phrase in (
        "Four Mathematical Mysteries | Learn, Explore, Review",
        "Public review:</strong> HINC-001 and ABF-001",
        "Private release edge:</strong> FSG-001",
        "Private release edge · not yet public technical review.",
        "public release is not authorized",
        "Private source, branch, and review materials are not exposed",
        "Clean exact-head execution",
        "final package/manifest",
        "release-day literature delta",
        "exact authorization",
        "Consolidation hold",
    ):
        check("required_boundary_text", phrase.lower() in page.lower(), phrase=phrase)

    for forbidden in (
        "github.com/novakprotocol/N-MathLab",
        "agent/mcrc-fibonacci-sandpile-groups-v3",
        "papers/mcrc-fibonacci-sandpile-v3",
        "PASS_PUBLIC_TECHNICAL_REVIEW_FSG",
    ):
        check("private_reference_absent", forbidden not in page, token=forbidden)

    check("unique_ids", len(parser.ids) == len(set(parser.ids)), count=len(parser.ids))
    check("four_paths", all(f'#{name}' in parser.hrefs for name in ("hinc", "abf", "fsg", "acm")))
    check("one_inline_script", len(parser.inline_scripts) == 1, actual=len(parser.inline_scripts))
    check("interactive_petal", "renderPetal" in page and "mSlider" in page)
    check("interactive_hinc", "hincRecord" in page and "hincReadout" in page)
    check("interactive_abf", "abfOut" in page and "restrict" in page)
    check("interactive_acm", "renderLights" in page and "lightReadout" in page)

    for phrase in (
        'href="learn.html"',
        "FSG-001 has reached a private release edge",
        "Private release edge · not public",
        "Two active packages. One private release edge. One consolidation hold.",
    ):
        check("index_integration", phrase in index, phrase=phrase)

    check("index_no_private_source", "github.com/novakprotocol/N-MathLab" not in index)
    check("page_size", 15_000 <= len(page.encode("utf-8")) <= 80_000, bytes=len(page.encode("utf-8")))

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
            "hinc_001_public_review": True,
            "abf_001_public_review": True,
            "fsg_001_private_release_edge": True,
            "fsg_001_public_release_authorized": False,
            "acm_001_consolidation_hold": True,
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
