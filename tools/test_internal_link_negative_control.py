#!/usr/bin/env python3
"""Verify internal-link validation rejects a missing local fragment."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


SCHEMA = "n.human_ai_mathematics.internal_link_negative_control.v1"


@dataclass(frozen=True)
class Record:
    control_id: str
    changed_file: str
    mutation: str
    command: list[str]
    expected_nonzero_exit: bool
    actual_exit: int
    expected_category: str
    expected_path: str
    expected_category_present: bool
    expected_path_present: bool
    stdout: str
    stderr: str
    result: str


def copy_repo(root: Path, work_root: Path) -> Path:
    if work_root.exists():
        shutil.rmtree(work_root)
    target = work_root / "repo"

    def ignore(dir_name: str, names: list[str]) -> set[str]:
        ignored = {".git", "__pycache__", ".pytest_cache", "_mutation_work", "_schema_negative_work", "_internal_link_work"}
        return {name for name in names if name in ignored or name == ".lake"}

    shutil.copytree(root, target, ignore=ignore)
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    work_root = root / "reports" / "_internal_link_work"
    temp_repo = copy_repo(root, work_root)
    target = temp_repo / "docs" / "index.html"
    text = target.read_text(encoding="utf-8")
    marker = '<a href="learn.html#missing-fragment-synthetic">synthetic missing fragment</a>'
    target.write_text(text.replace("</body>", f"{marker}\n</body>"), encoding="utf-8", newline="\n")
    command = [sys.executable, "tools/validate_internal_links.py", "--root", str(temp_repo)]
    completed = subprocess.run(
        command,
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    stdout = completed.stdout
    stderr = completed.stderr
    recorded_command = ["python", "tools/validate_internal_links.py", "--root", "<internal-link-mutation-repo>"]
    expected_category = "missing fragment"
    expected_path = "docs/index.html"
    passed = (
        completed.returncode != 0
        and expected_category in stdout.casefold()
        and expected_path in stdout
    )
    record = Record(
        control_id="INTERNAL_LINK_NEG_01",
        changed_file=expected_path,
        mutation="Add a local link to a missing synthetic fragment in docs/learn.html.",
        command=recorded_command,
        expected_nonzero_exit=True,
        actual_exit=completed.returncode,
        expected_category=expected_category,
        expected_path=expected_path,
        expected_category_present=expected_category in stdout.casefold(),
        expected_path_present=expected_path in stdout,
        stdout=stdout,
        stderr=stderr,
        result="PASS" if passed else "FAIL",
    )
    payload = {
        "schema": SCHEMA,
        "result": record.result,
        "records": [asdict(record)],
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    shutil.rmtree(work_root, ignore_errors=True)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
