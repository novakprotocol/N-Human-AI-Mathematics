#!/usr/bin/env python3
"""Verify internal-link validation rejects controlled invalid HTML mutations."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable


SCHEMA = "n.human_ai_mathematics.internal_link_negative_control.v2"


@dataclass(frozen=True)
class ControlSpec:
    control_id: str
    expected_category: str
    expected_path: str
    apply: Callable[[Path], tuple[str, str]]


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


def insert_before_body(path: Path, marker: str) -> None:
    body = path.read_text(encoding="utf-8")
    if "</body>" not in body:
        raise AssertionError(f"missing </body> in {path}")
    path.write_text(body.replace("</body>", f"{marker}\n</body>", 1), encoding="utf-8", newline="\n")


def c01(root: Path) -> tuple[str, str]:
    rel = "docs/index.html"
    insert_before_body(root / rel, '<a href="missing-synthetic.html">synthetic missing file</a>')
    return rel, "Add a local link to a missing synthetic file."


def c02(root: Path) -> tuple[str, str]:
    rel = "docs/index.html"
    insert_before_body(root / rel, '<a href="learn.html#missing-fragment-synthetic">synthetic missing fragment</a>')
    return rel, "Add a local link to a missing synthetic fragment in docs/learn.html."


def c03(root: Path) -> tuple[str, str]:
    rel = "docs/index.html"
    insert_before_body(root / rel, '<a href="../../private-synthetic.html">synthetic unsafe traversal</a>')
    return rel, "Add an unsafe parent-directory traversal link."


def c04(root: Path) -> tuple[str, str]:
    rel = "docs/learn.html"
    target = root / rel
    ids = re.findall(r'\bid="([^"]+)"', target.read_text(encoding="utf-8"))
    if not ids:
        raise AssertionError("docs/learn.html has no id to duplicate")
    insert_before_body(target, f'<div id="{ids[0]}">synthetic duplicate id</div>')
    return rel, "Duplicate an existing HTML id in docs/learn.html."


CONTROLS: tuple[ControlSpec, ...] = (
    ControlSpec("INTERNAL_LINK_NEG_01", "missing local href target", "docs/index.html", c01),
    ControlSpec("INTERNAL_LINK_NEG_02", "missing fragment", "docs/index.html", c02),
    ControlSpec("INTERNAL_LINK_NEG_03", "unsafe traversal", "docs/index.html", c03),
    ControlSpec("INTERNAL_LINK_NEG_04", "duplicate id", "docs/learn.html", c04),
)


def ignore(_: str, names: list[str]) -> set[str]:
    ignored = {".git", ".lake", "__pycache__", ".pytest_cache", "_mutation_work", "_schema_negative_work", "_internal_link_work"}
    return {name for name in names if name in ignored}


def copy_repo(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target, ignore=ignore)


def run_validator(temp_repo: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "tools/validate_internal_links.py", "--root", str(temp_repo)],
        cwd=temp_repo,
        text=True,
        capture_output=True,
        check=False,
    )


def git_status(root: Path) -> str:
    if not (root / ".git").exists():
        return "NO_GIT"
    completed = subprocess.run(["git", "status", "--short"], cwd=root, text=True, capture_output=True)
    return completed.stdout


def safe_reset_work_root(work_root: Path, allowed_parent: Path) -> None:
    resolved = work_root.resolve()
    allowed = allowed_parent.resolve()
    if work_root.name != "_internal_link_work" or not (resolved == allowed or allowed in resolved.parents):
        raise SystemExit(f"refusing unsafe internal-link work directory: {work_root}")
    if work_root.exists():
        shutil.rmtree(work_root)
    work_root.mkdir(parents=True, exist_ok=True)


def run_control(baseline_repo: Path, work_root: Path, spec: ControlSpec) -> Record:
    temp_repo = work_root / spec.control_id.lower() / "repo"
    copy_repo(baseline_repo, temp_repo)
    changed_file, mutation = spec.apply(temp_repo)
    completed = run_validator(temp_repo)
    stdout_folded = completed.stdout.casefold()
    category_ok = spec.expected_category.casefold() in stdout_folded
    path_ok = spec.expected_path in completed.stdout
    passed = completed.returncode != 0 and category_ok and path_ok
    return Record(
        control_id=spec.control_id,
        changed_file=changed_file,
        mutation=mutation,
        command=["python", "tools/validate_internal_links.py", "--root", "<internal-link-mutation-repo>"],
        expected_nonzero_exit=True,
        actual_exit=completed.returncode,
        expected_category=spec.expected_category,
        expected_path=spec.expected_path,
        expected_category_present=category_ok,
        expected_path_present=path_ok,
        stdout=completed.stdout,
        stderr=completed.stderr,
        result="PASS" if passed else "FAIL",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output_path = args.output if args.output is None or args.output.is_absolute() else root / args.output
    output_anchor = (output_path or (root / "reports" / "internal-link-negative-control.json")).resolve().parent
    work_root = output_anchor / "_internal_link_work"
    if output_path and output_path.exists():
        if not output_path.is_file():
            raise SystemExit(f"refusing to remove non-file output path: {output_path}")
        output_path.unlink()

    status_before = git_status(root)
    safe_reset_work_root(work_root, output_anchor)
    baseline_repo = work_root / "baseline" / "repo"
    copy_repo(root, baseline_repo)
    baseline = run_validator(baseline_repo)
    baseline_ok = baseline.returncode == 0
    records = [run_control(baseline_repo, work_root, spec) for spec in CONTROLS] if baseline_ok else []
    shutil.rmtree(work_root, ignore_errors=True)
    worktree_unchanged = status_before == git_status(root)
    failures = [record for record in records if record.result != "PASS"]
    result = "PASS" if baseline_ok and not failures and worktree_unchanged else "FAIL"
    payload = {
        "schema": SCHEMA,
        "result": result,
        "baseline": {
            "command": ["python", "tools/validate_internal_links.py", "--root", "<internal-link-baseline-repo>"],
            "exit": baseline.returncode,
            "result": "PASS" if baseline_ok else "FAIL",
            "stdout": baseline.stdout,
            "stderr": baseline.stderr,
        },
        "control_count": len(records),
        "passed": sum(1 for record in records if record.result == "PASS"),
        "failed": len(failures),
        "expected_category_checks_passed": sum(1 for record in records if record.expected_category_present),
        "expected_path_checks_passed": sum(1 for record in records if record.expected_path_present),
        "worktree_unchanged": worktree_unchanged,
        "records": [asdict(record) for record in records],
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
