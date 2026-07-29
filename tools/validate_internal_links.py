#!/usr/bin/env python3
"""Validate local HTML links, fragment IDs, and duplicate IDs."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


SCHEMA = "n.human_ai_mathematics.internal_link_validation.v1"
HTML_FILES = ("docs/index.html", "docs/learn.html")


@dataclass(frozen=True)
class Finding:
    level: str
    path: str
    message: str


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if data.get("id"):
            self.ids.append(str(data["id"]))
        if data.get("href"):
            self.hrefs.append(str(data["href"]))


def parse_html(path: Path) -> LinkParser:
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def resolve_local(base_file: Path, href: str, root: Path) -> tuple[Path, str | None] | None:
    parsed = urlparse(href)
    if parsed.scheme in {"http", "https", "mailto"} or parsed.netloc:
        return None
    if parsed.scheme or href.startswith("javascript:"):
        return None
    raw_path = unquote(parsed.path)
    fragment = unquote(parsed.fragment) if parsed.fragment else None
    if raw_path in {"", "."}:
        target = base_file
    else:
        candidate = (base_file.parent / raw_path).resolve()
        try:
            candidate.relative_to(root.resolve())
        except ValueError as exc:
            raise ValueError(f"unsafe traversal in href {href!r}") from exc
        if candidate.is_dir():
            candidate = candidate / "index.html"
        target = candidate
    return target, fragment


def validate(root: Path) -> dict:
    findings: list[Finding] = []
    parsed_by_path: dict[Path, LinkParser] = {}
    for rel in HTML_FILES:
        path = root / rel
        if not path.is_file():
            findings.append(Finding("ERROR", rel, "required HTML file missing"))
            continue
        parser = parse_html(path)
        parsed_by_path[path.resolve()] = parser
        seen: set[str] = set()
        for item in parser.ids:
            if item in seen:
                findings.append(Finding("ERROR", rel, f"duplicate id: {item}"))
            seen.add(item)

    for rel in HTML_FILES:
        path = root / rel
        if not path.is_file():
            continue
        parser = parsed_by_path[path.resolve()]
        for href in parser.hrefs:
            try:
                resolved = resolve_local(path.resolve(), href, root)
            except ValueError as exc:
                findings.append(Finding("ERROR", rel, str(exc)))
                continue
            if resolved is None:
                continue
            target, fragment = resolved
            target_rel = target.relative_to(root.resolve()).as_posix() if target.exists() else str(target)
            if not target.is_file():
                findings.append(Finding("ERROR", rel, f"missing local href target: {href}"))
                continue
            target_parser = parsed_by_path.get(target.resolve())
            if target_parser is None and target.suffix.lower() == ".html":
                target_parser = parse_html(target)
                parsed_by_path[target.resolve()] = target_parser
            if fragment and target_parser is not None and fragment not in set(target_parser.ids):
                findings.append(Finding("ERROR", rel, f"missing fragment #{fragment} in {target_rel}"))

    errors = [item for item in findings if item.level == "ERROR"]
    return {
        "schema": SCHEMA,
        "result": "PASS" if not errors else "FAIL",
        "html_files": list(HTML_FILES),
        "error_count": len(errors),
        "findings": [asdict(item) for item in findings],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = validate(args.root.resolve())
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
