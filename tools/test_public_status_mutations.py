#!/usr/bin/env python3
"""Run adversarial public-status and private-reference mutations."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable


SCHEMA = "n.human_ai_mathematics.public_status_mutation_tests.v2"


@dataclass(frozen=True)
class MutationSpec:
    id: str
    group: str
    expected_category: str
    expected_path: str
    apply: Callable[[Path], tuple[str, str]]


@dataclass(frozen=True)
class MutationResult:
    id: str
    group: str
    changed_file: str
    mutation: str
    command: list[str]
    expected_nonzero_exit: bool
    actual_exit: int
    expected_category: str
    expected_path: str
    expected_category_present: bool
    expected_path_present: bool
    detected_categories: list[str]
    detected_paths: list[str]
    detected_finding: str
    stdout: str
    stderr: str
    result: str


def join(*parts: str) -> str:
    return "".join(parts)


def words(*parts: str) -> str:
    return " ".join(parts)


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
    sentinel = join("https://example.invalid/", "nonpublic-sentinel", "/pull/", "SYNTHETIC-0001")
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
    append_text(root / rel, "FSG-001 corrected theorem has passed review and is established.")
    return rel, "Represent the private FSG correction as passed or established."


def m13(root: Path) -> tuple[str, str]:
    rel = "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md"
    branch = join("fix/", "nonpublic-sentinel-branch-v1")
    manuscript = join("manuscript/", "nonpublic-sentinel", "/candidate.tex")
    artifact = join("artifacts/", "nonpublic-sentinel", "/package.zip")
    append_text(root / rel, f"Synthetic private source: {branch} {manuscript} {artifact}")
    return rel, "Expose a synthetic private branch, manuscript path, or artifact path."


def m14(root: Path) -> tuple[str, str]:
    rel = "research-index.json"
    data = load_json(root / rel)
    data["release_channel"] = "full_lean_requalification_hold"
    write_json(root / rel, data)
    return rel, "Use obsolete full-Lean requalification-hold state as the current release channel."


def p01(root: Path) -> tuple[str, str]:
    rel = "docs/learn.html"
    url = join("https://github.com/", "novakprotocol/", "nonpublic-sentinel", "/pull/", "SYNTHETIC-0001")
    append_text(root / rel, f'<a href="{url}">synthetic nonpublic review</a>')
    return rel, "Expose a direct private-style URL."


def p02(root: Path) -> tuple[str, str]:
    rel = "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md"
    append_text(root / rel, words("Synthetic", "reference:", "private", "lab", "PR", "#SYNTHETIC"))
    return rel, "Expose private-lab PR shorthand."


def p03(root: Path) -> tuple[str, str]:
    rel = "tools/synthetic_private_url.py"
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    line = join('url = "https://github.com/"', ' + "novakprotocol/', 'nonpublic-sentinel"', ' + "/pull/', 'SYNTHETIC-0001"')
    path.write_text(line + "\n", encoding="utf-8", newline="\n")
    return rel, "Expose concatenated URL pieces."


def p04(root: Path) -> tuple[str, str]:
    rel = ".github/workflows/synthetic-private.yml"
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    line = join('branch: ${{ "fix/"', ' + "nonpublic-sentinel-branch-v1" }}')
    path.write_text(line + "\n", encoding="utf-8", newline="\n")
    return rel, "Expose dynamically assembled branch-like path."


def p05(root: Path) -> tuple[str, str]:
    rel = "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md"
    append_text(root / rel, join("Synthetic path: manuscript/", "nonpublic-sentinel", "/candidate.tex"))
    return rel, "Expose a private manuscript path."


def p06(root: Path) -> tuple[str, str]:
    rel = "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md"
    append_text(root / rel, join("Synthetic path: artifacts/", "nonpublic-sentinel", "/package.zip"))
    return rel, "Expose a private artifact path."


MUTATIONS: tuple[MutationSpec, ...] = (
    MutationSpec("M01", "status", "per_file_state_mismatch", "research-index.json", m01),
    MutationSpec("M02", "status", "per_file_state_mismatch", "research-index.json", m02),
    MutationSpec("M03", "status", "per_file_state_mismatch", "research-index.json", m03),
    MutationSpec("M04", "status", "fsg_blocker_contradiction", "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md", m04),
    MutationSpec("M05", "status", "private_reference", "docs/learn.html", m05),
    MutationSpec("M06", "status", "full_lean_overclaim", "README.md", m06),
    MutationSpec("M07", "status", "peer_review_overclaim", "README.md", m07),
    MutationSpec("M08", "status", "historical_priority_overclaim", "README.md", m08),
    MutationSpec("M09", "status", "obsolete_current_state", "docs/index.html", m09),
    MutationSpec("M10", "status", "obsolete_current_state", "docs/index.html", m10),
    MutationSpec("M11", "status", "obsolete_current_state", "README.md", m11),
    MutationSpec("M12", "status", "fsg_correction_overclaim", "docs/learn.html", m12),
    MutationSpec("M13", "status", "private_reference", "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md", m13),
    MutationSpec("M14", "status", "current_release_channel", "research-index.json", m14),
    MutationSpec("P01", "private_reference", "private_reference", "docs/learn.html", p01),
    MutationSpec("P02", "private_reference", "private_reference", "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md", p02),
    MutationSpec("P03", "private_reference", "private_reference", "tools/synthetic_private_url.py", p03),
    MutationSpec("P04", "private_reference", "private_reference", ".github/workflows/synthetic-private.yml", p04),
    MutationSpec("P05", "private_reference", "private_reference", "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md", p05),
    MutationSpec("P06", "private_reference", "private_reference", "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md", p06),
)


def ignore(_: str, names: list[str]) -> set[str]:
    skipped = {".git", ".lake", ".venv", "__pycache__", ".artifacts", "_mutation_work", "_schema_negative_work", "_internal_link_work"}
    return {name for name in names if name in skipped}


def git_status(root: Path) -> str:
    if not (root / ".git").exists():
        return "NO_GIT"
    completed = subprocess.run(["git", "status", "--short"], cwd=root, text=True, capture_output=True)
    return completed.stdout


def copy_repo(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target, ignore=ignore)


def run_validator(temp_root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "tools/validate_status_consistency.py", "--root", str(temp_root), "--scan-all"],
        cwd=temp_root,
        text=True,
        capture_output=True,
    )


def parse_findings(stdout: str) -> tuple[list[str], list[str], str]:
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError:
        return [], [], "no JSON finding emitted"
    findings = payload.get("findings", [])
    categories = sorted({str(item.get("category", "")) for item in findings if item.get("category")})
    paths = sorted({str(item.get("path", "")) for item in findings if item.get("path")})
    if findings:
        first = findings[0]
        detected = f"{first.get('category')}: {first.get('path')}: {first.get('message')}"
    else:
        detected = "no finding emitted"
    return categories, paths, detected


def path_present(paths: list[str], expected: str) -> bool:
    return any(path == expected or path.startswith(expected + ":") for path in paths)


def run_mutation(clean_baseline: Path, work_parent: Path, spec: MutationSpec) -> MutationResult:
    work_dir = work_parent / spec.id.lower() / "repo"
    copy_repo(clean_baseline, work_dir)
    changed_file, description = spec.apply(work_dir)
    completed = run_validator(work_dir)
    categories, paths, detected = parse_findings(completed.stdout)
    category_ok = spec.expected_category in categories
    path_ok = path_present(paths, spec.expected_path)
    result = "PASS" if completed.returncode != 0 and category_ok and path_ok else "FAIL"
    return MutationResult(
        id=spec.id,
        group=spec.group,
        changed_file=changed_file,
        mutation=description,
        command=["python", "tools/validate_status_consistency.py", "--root", "<mutation-repo>", "--scan-all"],
        expected_nonzero_exit=True,
        actual_exit=completed.returncode,
        expected_category=spec.expected_category,
        expected_path=spec.expected_path,
        expected_category_present=category_ok,
        expected_path_present=path_ok,
        detected_categories=categories,
        detected_paths=paths,
        detected_finding=detected,
        stdout=completed.stdout,
        stderr=completed.stderr,
        result=result,
    )


def safe_reset_work_parent(root: Path, work_parent: Path) -> None:
    resolved = work_parent.resolve()
    resolved.relative_to(root.resolve())
    if work_parent.exists():
        shutil.rmtree(work_parent)
    work_parent.mkdir(parents=True, exist_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    parser.add_argument("--log", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    for stale in (args.output, args.log):
        if stale:
            stale_path = stale if stale.is_absolute() else root / stale
            try:
                stale_path.resolve().relative_to(root)
            except ValueError:
                raise SystemExit(f"refusing to remove output outside repository: {stale_path}")
            if stale_path.exists():
                stale_path.unlink()
    work_parent = root / "reports" / "_mutation_work"
    status_before = git_status(root)
    safe_reset_work_parent(root, work_parent)

    baseline_root = work_parent / "baseline" / "repo"
    copy_repo(root, baseline_root)
    baseline = run_validator(baseline_root)
    baseline_categories, baseline_paths, baseline_detected = parse_findings(baseline.stdout)
    records: list[MutationResult] = []
    baseline_ok = baseline.returncode == 0

    if baseline_ok:
        for spec in MUTATIONS:
            records.append(run_mutation(baseline_root, work_parent, spec))

    shutil.rmtree(work_parent)
    status_after = git_status(root)
    worktree_unchanged = status_before == status_after

    failures = [record for record in records if record.result != "PASS"]
    status_records = [record for record in records if record.group == "status"]
    private_records = [record for record in records if record.group == "private_reference"]
    result = "PASS" if baseline_ok and not failures and worktree_unchanged else "FAIL"
    payload = {
        "schema": SCHEMA,
        "result": result,
        "baseline": {
            "command": ["python", "tools/validate_status_consistency.py", "--root", "<baseline-repo>", "--scan-all"],
            "exit": baseline.returncode,
            "result": "PASS" if baseline_ok else "FAIL",
            "detected_categories": baseline_categories,
            "detected_paths": baseline_paths,
            "detected_finding": baseline_detected,
            "stdout": baseline.stdout,
            "stderr": baseline.stderr,
        },
        "mutation_count": len(records),
        "status_mutation_count": len(status_records),
        "private_reference_mutation_count": len(private_records),
        "passed": sum(1 for record in records if record.result == "PASS"),
        "failed": len(failures),
        "status_mutations_passed": sum(1 for record in status_records if record.result == "PASS"),
        "private_reference_mutations_passed": sum(1 for record in private_records if record.result == "PASS"),
        "expected_category_checks_passed": sum(1 for record in records if record.expected_category_present),
        "expected_path_checks_passed": sum(1 for record in records if record.expected_path_present),
        "worktree_unchanged": worktree_unchanged,
        "records": [asdict(record) for record in records],
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    if args.log:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            f"baseline: {'PASS' if baseline_ok else 'FAIL'} exit={baseline.returncode}: {baseline_detected}",
            f"worktree_unchanged: {worktree_unchanged}",
        ]
        lines.extend(
            f"{record.id}: {record.result}: exit={record.actual_exit}: category={record.expected_category_present}: path={record.expected_path_present}: {record.detected_finding}"
            for record in records
        )
        args.log.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
