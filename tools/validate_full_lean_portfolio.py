#!/usr/bin/env python3
"""Fail-closed validator for the full-Lean gold standard and active-review boundary."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "n.human_ai_mathematics.full_lean_portfolio_validation.v3"
STATUS_SCHEMA = "n.human_ai_mathematics.full_lean_portfolio.v2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"expected JSON object: {path}")
    return value


def validate(root: Path) -> dict[str, Any]:
    paths = {
        "portfolio": root / "formal-verification-status.json",
        "paper_status": root / "PAPER_1_3_FULL_LEAN_STATUS.json",
        "standard": root / "FULL_LEAN_RELEASE_STANDARD.md",
        "formalization_hold": root / "PUBLIC_REVIEW_FORMALIZATION_HOLD_2026-07-29.md",
        "program": root / "FULL_LEAN_VERIFICATION_PROGRAM.md",
        "status": root / "STATUS.md",
        "agents": root / "AGENTS.md",
        "release": root / "PUBLIC_REVIEW_RELEASE.md",
        "research_index": root / "research-index.json",
        "hinc_status": root / "papers/HINC-001/STATUS.json",
        "hinc_formal": root / "papers/HINC-001/FORMAL_VERIFICATION.md",
        "abf_status": root / "papers/ABF-001/STATUS.json",
        "abf_formal": root / "papers/ABF-001/FORMAL_VERIFICATION.md",
        "abf_lane_status": root / "papers/ABF-001/formal/FORMAL_STATUS_V1.json",
        "index": root / "docs/index.html",
        "learn": root / "docs/learn.html",
    }

    failures: list[dict[str, Any]] = []
    checks: dict[str, int] = {}

    def check(category: str, condition: bool, **context: Any) -> None:
        checks[category] = checks.get(category, 0) + 1
        if not condition:
            failures.append({"category": category, **context})

    for name, path in paths.items():
        check("required_file", path.is_file(), name=name, path=str(path.relative_to(root)))
    if not all(path.is_file() for path in paths.values()):
        return {"schema": SCHEMA, "result": "FAIL", "checks": checks, "failures": failures}

    portfolio = read_json(paths["portfolio"])
    paper_status = read_json(paths["paper_status"])
    research_index = read_json(paths["research_index"])
    hinc_status = read_json(paths["hinc_status"])
    abf_status = read_json(paths["abf_status"])
    abf_lane = read_json(paths["abf_lane_status"])

    texts = {name: path.read_text(encoding="utf-8") for name, path in paths.items() if path.suffix in {".md", ".html"}}
    public_site = texts["index"] + "\n" + texts["learn"]
    control_text = "\n".join(texts.values())

    check("status_schema", portfolio.get("schema") == STATUS_SCHEMA, actual=portfolio.get("schema"))
    policy = portfolio.get("policy", {})
    check("policy_selected", policy.get("selected") is True)
    check("full_pass_required_for_full_lean", policy.get("full_pass_required_for_fully_lean_verified_manuscript") is True)
    check("active_review_partial_allowed", policy.get("active_candidate_review_allowed_with_exact_bounded_partial_pass") is True)
    check("bounded_not_full", policy.get("bounded_pass_may_be_described_as_full_pass") is False)
    check("lean_boundary", policy.get("lean_establishes_novelty_or_peer_review") is False)
    check("portfolio_not_full", portfolio.get("portfolio_full_lean_verified") is False)
    check("no_full_pass_papers", portfolio.get("papers_with_full_pass") == [])
    check("no_fully_lean_verified_manuscripts", portfolio.get("fully_lean_verified_manuscripts") == [])
    check("active_candidate_packages", portfolio.get("active_public_candidate_review_packages") == ["HINC-001", "ABF-001"])
    check("fsg_not_authorized", portfolio.get("fsg_public_release_authorized") is False)

    expected = {
        "HINC-001": ("ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW", "PARTIAL_PASS", True),
        "ABF-001": ("ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW", "PARTIAL_PASS", True),
        "FSG-001": ("PRIVATE_CANDIDATE_MATHEMATICAL_BLOCKER_HOLD", "HOLD_MATHEMATICAL_BLOCKER", False),
        "ACM-001": ("HOLD_PENDING_CONSOLIDATION", "HOLD_PENDING_CONSOLIDATION", False),
    }
    for paper_id, (public_state, formal_state, active) in expected.items():
        paper = portfolio.get("portfolio", {}).get(paper_id, {})
        check("paper_public_state", paper.get("public_state") == public_state, paper_id=paper_id, expected=public_state, actual=paper.get("public_state"))
        check("paper_formal_state", paper.get("formal_status") == formal_state, paper_id=paper_id, expected=formal_state, actual=paper.get("formal_status"))
        check("paper_not_full", paper.get("full_manuscript_lean_verified") is False, paper_id=paper_id)
        if paper_id in {"HINC-001", "ABF-001"}:
            check("paper_no_claim_map", paper.get("claim_map_complete") is False, paper_id=paper_id)
            check("paper_active_authorized", paper.get("active_public_review_authorized") is True, paper_id=paper_id)
        if paper_id == "FSG-001":
            check("fsg_math_blocker", "item (v) false as written" in str(paper.get("mathematical_blocker", "")).casefold())
            check("fsg_no_public_package", paper.get("public_theorem_package_released") is False)
            check("fsg_no_release_auth", paper.get("public_mathematical_release_authorized") is False)

    check("hinc_status_partial", hinc_status.get("formal_verification", {}).get("status") == "PARTIAL_PASS_BOUNDED_LEAN_VERIFICATION")
    check("hinc_status_not_full", hinc_status.get("formal_verification", {}).get("full_manuscript_lean_verified") is False)
    check("hinc_release_active", hinc_status.get("release", {}).get("public_authorized") is True)
    check("abf_status_partial", abf_status.get("formal_verification", {}).get("status") == "PARTIAL_PASS_BOUNDED_A01_LEAN_VERIFICATION")
    check("abf_status_not_full", abf_status.get("formal_verification", {}).get("full_manuscript_lean_verified") is False)
    check("abf_release_active", abf_status.get("release", {}).get("public_authorized") is True)
    check("abf_a01_preserved", abf_lane.get("lanes", {}).get("A01_bidual_moment_kernel") == "COMPILED_PASS")
    check("abf_lane_not_full", abf_lane.get("full_manuscript_lean_verified") is False)

    expected_summary = {
        "HINC-001": "PARTIAL_PASS",
        "ABF-001": "PARTIAL_PASS",
        "FSG-001": "HOLD_MATHEMATICAL_BLOCKER",
        "ACM-001": "HOLD_PENDING_CONSOLIDATION",
    }
    for paper_id, status in expected_summary.items():
        actual = paper_status.get("papers", {}).get(paper_id, {}).get("formal_status")
        check("paper_summary_status", actual == status, paper_id=paper_id, expected=status, actual=actual)

    index_entries = {item.get("id"): item for item in research_index.get("papers", []) if isinstance(item, dict)}
    check("research_hinc_active", index_entries.get("HINC-001", {}).get("state") == "active_review")
    check("research_abf_active", index_entries.get("ABF-001", {}).get("state") == "active_review")
    check("research_fsg_hold", index_entries.get("FSG-001", {}).get("state") == "hold")
    check("research_acm_hold", index_entries.get("ACM-001", {}).get("state") == "hold")

    required_control_phrases = (
        "Full-manuscript Lean verification remains",
        "HINC-001  active public candidate technical review",
        "ABF-001   active public candidate technical review",
        "PARTIAL_PASS / bounded Lean verification",
        "PARTIAL_PASS / bounded A01 Lean verification",
        "HOLD -- MATHEMATICAL BLOCKER",
        "FULL_PASS` requires complete retained manuscript claim-to-Lean coverage",
    )
    for phrase in required_control_phrases:
        check("control_phrase", phrase.casefold() in control_text.casefold(), phrase=phrase)

    required_site_phrases = (
        "Active candidate public technical review",
        "Bounded Lean PASS",
        "Bounded A01 Lean PASS",
        "HOLD -- MATHEMATICAL BLOCKER",
        "FULL_PASS",
    )
    for phrase in required_site_phrases:
        check("site_phrase", phrase.casefold() in public_site.casefold(), phrase=phrase)

    forbidden_site_phrases = (
        "No active theorem packages",
        "Historical public artifacts",
        "Active theorem status suspended",
        "Public archive",
        "Private release edge",
        "all papers are Lean verified",
        "all claims are machine checked",
        "the manuscripts are fully formalized",
        "FSG-001 correction has passed",
    )
    for phrase in forbidden_site_phrases:
        check("site_overclaim_absent", phrase.casefold() not in public_site.casefold(), phrase=phrase)

    full_pass = portfolio.get("full_pass_definition", {})
    check("full_pass_unmapped_zero", full_pass.get("unmapped_mathematical_claims") == 0)
    check("full_pass_unresolved_zero", full_pass.get("unresolved_formal_claims") == 0)
    check("full_pass_sorry_zero", full_pass.get("sorry_count") == 0)
    check("full_pass_admit_zero", full_pass.get("admit_count") == 0)
    check("full_pass_axiom_zero", full_pass.get("project_axiom_count") == 0)
    check("full_pass_sorryax_false", full_pass.get("sorryAx_present") is False)
    check("full_pass_build", full_pass.get("clean_immutable_build") == "PASS")
    check("full_pass_fidelity", full_pass.get("claim_fidelity_review") == "PASS")
    check("full_pass_flag", full_pass.get("full_manuscript_lean_verified") is True)

    return {
        "schema": SCHEMA,
        "result": "PASS" if not failures else "FAIL",
        "total_checks": sum(checks.values()),
        "checks": dict(sorted(checks.items())),
        "failures": failures,
        "files": {str(path.relative_to(root)): {"sha256": sha256(path), "bytes": path.stat().st_size} for path in paths.values()},
        "portfolio_full_lean_verified": False,
        "papers_with_full_pass": [],
        "fully_lean_verified_manuscripts": [],
        "active_public_candidate_review_packages": ["HINC-001", "ABF-001"],
        "fsg_public_release_authorized": False,
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