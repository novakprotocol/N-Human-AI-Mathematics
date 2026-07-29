#!/usr/bin/env python3
"""Run adversarial public-status mutations against the real validator."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable


SCHEMA = "n.human_ai_mathematics.public_status_mutation_tests.v1"


@dataclass(frozen=True)
class MutationResult:
    id: str
    changed_file: str
    mutation: str
    command: list[str]
    expected_nonzero_exit: bool
    actual_exit: int
    detected_finding: str
    result: str


Mutation = Callable[[Path], tuple[str, str]]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=False) + "\n", encoding="utf-8", newline="\n")


def append_text(path: Path, value: str) -> None:
    body = path.read_text(encoding="utf-8")
    path.write_text(body.rstrip() + "\n\n" + value + "\n", encoding="utf-8", newline="\n")


def replace_text(path: Path, old: str, new: str) -> None:
    body = path.read_text(encoding="utf-8")
    if old not in body:
        raise AssertionError(f"expected text not found in {path}: {old}")
    path.write_text(body.replace(old, new, 1), encoding="utf-8", newline="\n")


def m01(root: Path) -> tuple[str, str]:
    rel = "research-index.json"
    data = load_json(root / rel)
    data["papers"][0]["state"] = "hold"
    write_json(root / rel, data)
    return rel, "Change HINC from active_review to hold."


def m02(root: Path) -> tuple[str, str]:
    rel = "research-index.json"
    data = load_json(root / rel)
    data["papers"][1]["state"] = "hold"
    write_json(root / rel, data)
    return rel, "Change ABF from active_review to hold."


def m03(root: Path) -> tuple[str, str]:
    rel = "research-index.json"
    data = load_json(root / rel)
    data["papers"][2]["state"] = "active_review"
    write_json(root / rel, data)
    return rel, "Change FSG from hold to active_review."


def m04(root: Path) -> tuple[str, str]:
    rel = "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md"
    append_text(root / rel, "Current FSG-001 status: zero blocking findings.")
    return rel, "Add current FSG wording equivalent to zero blocking findings."


def m05(root: Path) -> tuple[str, str]:
    rel = "docs/learn.html"
    sentinel = "https://" + "example.invalid/" + "private-research" + "/pull/428"
    append_text(root / rel, f'<a href="{sentinel}">synthetic private review</a>')
    return rel, "Add a synthetic nonpublic repository or private-style link to a public FSG surface."


def m06(root: Path) -> tuple[str, str]:
    rel = "README.md"
    append_text(root / rel, "Current claim: HINC-001 is fully Lean verified.")
    return rel, "Claim HINC or ABF is fully Lean verified."


def m07(root: Path) -> tuple[str, str]:
    rel = "README.md"
    append_text(root / rel, "Peer reviewed: yes.")
    return rel, "Claim peer review has been completed."


def m08(root: Path) -> tuple[str, str]:
    rel = "README.md"
    append_text(root / rel, "Historical priority established; world-first status is claimed.")
    return rel, "Claim historical priority or a world-first status."


def m09(root: Path) -> tuple[str, str]:
    rel = "docs/index.html"
    replace_text(root / rel, "Active candidate public technical review", "Hold pending full Lean review")
    return rel, "Create a contradiction between machine-readable and human-readable state."


def m10(root: Path) -> tuple[str, str]:
    rel = "docs/index.html"
    append_text(root / rel, "No active theorem packages under the current rule.")
    return rel, "Restore No active theorem packages to the current landing page."


def m11(root: Path) -> tuple[str, str]:
    rel = "README.md"
    append_text(root / rel, "HINC-001 and ABF-001 are historical artifacts only.")
    return rel, "Restore HINC/ABF historical artifact only wording."


def m12(root: Path) -> tuple[str, str]:
    rel = "docs/learn.html"
    append_text(root / rel, "FSG-001 correction has passed review and is established.")
    return rel, "Represent the private FSG correction as passed or established."


def m13(root: Path) -> tuple[str, str]:
    rel = "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md"
    branch = "fix/" + "private-fsg-branch-v1"
    manuscript = "manuscript/" + "private-fsg/candidate.tex"
    artifact = "artifacts/" + "private-fsg/package.zip"
    append_text(root / rel, f"Synthetic private source: {branch} {manuscript} {artifact}")
    return rel, "Expose a synthetic private branch, manuscript path, or artifact path."


def m14(root: Path) -> tuple[str, str]:
    rel = "research-index.json"
    data = load_json(root / rel)
    data["release_channel"] = "full_lean_requalification_hold"
    write_json(root / rel, data)
    return rel, "Use obsolete full-Lean requalification-hold state as the current release channel."


MUTATIONS: tuple[tuple[str, Mutation], ...] = (
    ("M01", m01),
    ("M02", m02),
    ("M03", m03),
    ("M04", m04),
    ("M05", m05),
    ("M06", m06),
    ("M07", m07),
    ("M08", m08),
    ("M09", m09),
    ("M10", m10),
    ("M11", m11),
    ("M12", m12),
    ("M13", m13),
    ("M14", m14),
)


def ignore(_: str, names: list[str]) -> set[str]:
    return {name for name in names if name in {".git", ".lake", ".venv", "__pycache__", ".artifacts", "_mutation_work"}}


def first_finding(stdout: str, stderr: str) -> str:
    try:
        payload = json.loads(stdout)
        findings = payload.get("findings", [])
        if findings:
            first = findings[0]
            return f"{first.get('category')}: {first.get('path')}: {first.get('message')}"
    except json.JSONDecodeError:
        pass
    return (stderr or stdout).strip().splitlines()[-1] if (stderr or stdout).strip() else "no finding emitted"


def run_mutation(repo: Path, mutation_id: str, mutation: Mutation) -> MutationResult:
    work_parent = repo / "reports" / "_mutation_work"
    work_dir = work_parent / mutation_id.lower()
    if work_dir.exists():
        shutil.rmtree(work_dir, ignore_errors=True)
    work_dir.mkdir(parents=True, exist_ok=True)
    try:
        temp_root = work_dir / "repo"
        shutil.copytree(repo, temp_root, ignore=ignore)
        changed_file, description = mutation(temp_root)
        command = [sys.executable, "tools/validate_status_consistency.py", "--root", str(temp_root)]
        recorded_command = ["python", "tools/validate_status_consistency.py", "--root", "<mutation-repo>"]
        completed = subprocess.run(command, cwd=temp_root, text=True, capture_output=True)
        detected = first_finding(completed.stdout, completed.stderr)
        result = "PASS" if completed.returncode != 0 else "FAIL"
        return MutationResult(
            id=mutation_id,
            changed_file=changed_file,
            mutation=description,
            command=recorded_command,
            expected_nonzero_exit=True,
            actual_exit=completed.returncode,
            detected_finding=detected,
            result=result,
        )
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    parser.add_argument("--log", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()

    records = [run_mutation(root, mutation_id, mutation) for mutation_id, mutation in MUTATIONS]
    failures = [record for record in records if record.result != "PASS"]
    payload = {
        "schema": SCHEMA,
        "result": "PASS" if not failures else "FAIL",
        "mutation_count": len(records),
        "passed": sum(1 for record in records if record.result == "PASS"),
        "failed": len(failures),
        "records": [asdict(record) for record in records],
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    if args.log:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        args.log.write_text("\n".join(f"{record.id}: {record.result}: exit={record.actual_exit}: {record.detected_finding}" for record in records) + "\n", encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
