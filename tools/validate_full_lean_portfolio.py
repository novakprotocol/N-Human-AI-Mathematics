#!/usr/bin/env python3
"""Fail-closed validator for the portfolio-wide full-Lean policy."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "n.human_ai_mathematics.full_lean_portfolio_validation.v1"
STATUS_SCHEMA = "n.human_ai_mathematics.full_lean_portfolio.v1"
ABF_STATUS_SCHEMA = "n.human_ai_mathematics.abf001.formal_status.v1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path) -> dict[str, Any]:
    status_path = root / "formal-verification-status.json"
    policy_path = root / "FULL_LEAN_VERIFICATION_PROGRAM.md"
    hinc_path = root / "papers/HINC-001/FORMAL_VERIFICATION.md"
    abf_path = root / "papers/ABF-001/FORMAL_VERIFICATION.md"
    abf_status_path = root / "papers/ABF-001/formal/FORMAL_STATUS_V1.json"
    abf_root_path = root / "papers/ABF-001/formal/ABF.lean"
    abf_lane_path = root / "papers/ABF-001/formal/ABF/MomentKernel.lean"
    abf_toolchain_path = root / "papers/ABF-001/formal/lean-toolchain"
    index_path = root / "docs/index.html"
    learn_path = root / "docs/learn.html"

    required_paths = (
        status_path,
        policy_path,
        hinc_path,
        abf_path,
        abf_status_path,
        abf_root_path,
        abf_lane_path,
        abf_toolchain_path,
        index_path,
        learn_path,
    )

    failures: list[dict[str, Any]] = []
    checks: dict[str, int] = {}

    def check(category: str, condition: bool, **context: Any) -> None:
        checks[category] = checks.get(category, 0) + 1
        if not condition:
            failures.append({"category": category, **context})

    for path in required_paths:
        check("required_file", path.is_file(), path=str(path.relative_to(root)))

    if not all(path.is_file() for path in required_paths):
        return {
            "schema": SCHEMA,
            "result": "FAIL",
            "checks": checks,
            "failures": failures,
        }

    status = json.loads(status_path.read_text(encoding="utf-8"))
    policy = policy_path.read_text(encoding="utf-8")
    hinc = hinc_path.read_text(encoding="utf-8")
    abf = abf_path.read_text(encoding="utf-8")
    abf_status = json.loads(abf_status_path.read_text(encoding="utf-8"))
    abf_root = abf_root_path.read_text(encoding="utf-8")
    abf_lane = abf_lane_path.read_text(encoding="utf-8")
    index = index_path.read_text(encoding="utf-8")
    learn = learn_path.read_text(encoding="utf-8")

    check("status_schema", status.get("schema") == STATUS_SCHEMA, actual=status.get("schema"))
    check("policy_selected", status["policy"]["selected"] is True)
    check(
        "new_release_gold_gate",
        status["policy"]["full_pass_required_for_new_fsg_or_acm_release"] is True,
    )
    check(
        "lean_boundary",
        status["policy"]["lean_establishes_novelty_or_peer_review"] is False,
    )
    check("portfolio_not_full", status["portfolio_full_lean_verified"] is False)
    check("no_full_pass_papers", status["papers_with_full_pass"] == [])

    expected = {
        "HINC-001": ("PARTIAL_PASS", False),
        "ABF-001": ("PARTIAL_PASS", False),
        "FSG-001": ("BOOTSTRAP_COMPILE_PENDING", False),
        "ACM-001": ("BLOCKED_BY_CONSOLIDATION", False),
    }
    for paper_id, (formal_status, full_verified) in expected.items():
        paper = status["portfolio"].get(paper_id, {})
        check(
            "paper_formal_status",
            paper.get("formal_status") == formal_status,
            paper_id=paper_id,
            expected=formal_status,
            actual=paper.get("formal_status"),
        )
        check(
            "paper_not_full",
            paper.get("full_manuscript_lean_verified") is full_verified,
            paper_id=paper_id,
        )

    abf_portfolio = status["portfolio"].get("ABF-001", {})
    check("abf_project_present", abf_portfolio.get("proof_assistant_project_present") is True)
    check(
        "abf_compiled_lane",
        abf_portfolio.get("compiled_bounded_lanes") == ["A01_bidual_moment_kernel"],
    )
    check("abf_scope_unresolved", abf_portfolio.get("unresolved_formal_scope") is True)

    check(
        "hinc_boundary",
        "The full revised manuscript is **not** formalized" in hinc,
    )
    check(
        "hinc_wording_rule",
        "Do not replace that with “HINC-001 is formally proved.”" in hinc,
    )

    check("abf_status_schema", abf_status.get("schema") == ABF_STATUS_SCHEMA)
    check("abf_partial_status", abf_status.get("status") == "PARTIAL_PASS")
    check(
        "abf_a01_pass",
        abf_status.get("lanes", {}).get("A01_bidual_moment_kernel") == "COMPILED_PASS",
    )
    check("abf_not_full", abf_status.get("full_manuscript_lean_verified") is False)
    check("abf_toolchain", abf_toolchain_path.read_text(encoding="utf-8").strip() == "leanprover/lean4:v4.30.0")
    check("abf_root_import", "import ABF.MomentKernel" in abf_root)
    for declaration in (
        "generatorSpan_le_ker_iff",
        "mem_ker_iff_coordinatesZero",
        "bidual_moment_incidence",
        "bidual_span_kernel_incidence",
    ):
        check("abf_required_declaration", f"theorem {declaration}" in abf_lane, declaration=declaration)
    for forbidden in ("sorry", "admit", "axiom "):
        check("abf_placeholder_absent", forbidden not in abf_lane, token=forbidden)

    for phrase in (
        "bounded formal PASS:             yes — A01 bidual moment-kernel bridge",
        "full-manuscript formal PASS:     no",
        "partially formalized candidate manuscript",
    ):
        check("abf_boundary", phrase in abf, phrase=phrase)

    for phrase in (
        "fully Lean-verified",
        "zero `sorry`",
        "Complete claim map",
        "Literal-source bridge",
        "Fidelity review",
        "FSG-001:  HOLD",
        "ACM-001:  HOLD",
        "ABF-001:  remain active with bounded A01 formal PASS",
    ):
        check("policy_content", phrase.lower() in policy.lower(), phrase=phrase)

    site = index + "\n" + learn
    for forbidden in (
        "all papers are Lean verified",
        "all claims are machine checked",
        "the portfolio is formally proved",
        "the manuscripts are fully formalized",
        "FSG-001</td><td>Critical groups and Fibonacci divisibility</td><td><span class=\"state active\"",
        "ACM-001</td><td>Coding theory, matroids, Boolean functions</td><td><span class=\"state active\"",
    ):
        check("public_overclaim_absent", forbidden.lower() not in site.lower(), token=forbidden)

    for required in (
        "Private release edge · not public",
        "Hold pending consolidation",
        "Lean verification</span><strong>Covers listed declarations—not the full manuscript",
        "Formal verification</strong><span>Bounded A01 Lean PASS; full manuscript incomplete",
    ):
        check("public_boundary_present", required in index, phrase=required)

    return {
        "schema": SCHEMA,
        "result": "PASS" if not failures else "FAIL",
        "total_checks": sum(checks.values()),
        "checks": dict(sorted(checks.items())),
        "failures": failures,
        "files": {
            str(path.relative_to(root)): {"sha256": sha256(path), "bytes": path.stat().st_size}
            for path in required_paths
        },
        "portfolio_full_lean_verified": False,
        "papers_with_full_pass": [],
        "public_release_effect": {
            "HINC-001": "UNCHANGED_BOUNDED_PUBLIC_REVIEW",
            "ABF-001": "UNCHANGED_PUBLIC_REVIEW_BOUNDED_A01_PASS",
            "FSG-001": "HOLD",
            "ACM-001": "HOLD",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
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
