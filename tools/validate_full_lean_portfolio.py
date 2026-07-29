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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path) -> dict[str, Any]:
    status_path = root / "formal-verification-status.json"
    policy_path = root / "FULL_LEAN_VERIFICATION_PROGRAM.md"
    hinc_path = root / "papers/HINC-001/FORMAL_VERIFICATION.md"
    abf_path = root / "papers/ABF-001/FORMAL_VERIFICATION.md"
    index_path = root / "docs/index.html"
    learn_path = root / "docs/learn.html"

    failures: list[dict[str, Any]] = []
    checks: dict[str, int] = {}

    def check(category: str, condition: bool, **context: Any) -> None:
        checks[category] = checks.get(category, 0) + 1
        if not condition:
            failures.append({"category": category, **context})

    for path in (status_path, policy_path, hinc_path, abf_path, index_path, learn_path):
        check("required_file", path.is_file(), path=str(path.relative_to(root)))

    if not all(path.is_file() for path in (status_path, policy_path, hinc_path, abf_path, index_path, learn_path)):
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
        "ABF-001": ("NOT_STARTED", False),
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

    check(
        "hinc_boundary",
        "The full revised manuscript is **not** formalized" in hinc,
    )
    check(
        "hinc_wording_rule",
        "Do not replace that with “HINC-001 is formally proved.”" in hinc,
    )
    check("abf_no_assistant", "proof assistant:             none" in abf)
    check("abf_no_pass", "formal PASS:                 no" in abf)
    check(
        "abf_boundary",
        "No ABF-001 theorem is represented as formally verified." in abf,
    )

    for phrase in (
        "fully Lean-verified",
        "zero `sorry`",
        "Complete claim map",
        "Literal-source bridge",
        "Fidelity review",
        "FSG-001:  HOLD",
        "ACM-001:  HOLD",
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
        "Formal verification</strong><span>Not completed or claimed",
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
            for path in (status_path, policy_path, hinc_path, abf_path, index_path, learn_path)
        },
        "portfolio_full_lean_verified": False,
        "papers_with_full_pass": [],
        "public_release_effect": {
            "HINC-001": "UNCHANGED_BOUNDED_PUBLIC_REVIEW",
            "ABF-001": "UNCHANGED_PUBLIC_REVIEW_NO_FORMAL_PASS",
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
