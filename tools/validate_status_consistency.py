#!/usr/bin/env python3
"""Cross-check corrected public candidate-review and formal states."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

SCHEMA = "n.human_ai_mathematics.status_consistency_validation.v2"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"expected JSON object: {path}")
    return value


def text_files(root: Path) -> dict[str, str]:
    names = {
        "status": "STATUS.md",
        "agents": "AGENTS.md",
        "release": "PUBLIC_REVIEW_RELEASE.md",
        "formalization_hold": "PUBLIC_REVIEW_FORMALIZATION_HOLD_2026-07-29.md",
        "standard": "FULL_LEAN_RELEASE_STANDARD.md",
        "program": "FULL_LEAN_VERIFICATION_PROGRAM.md",
        "correction": "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md",
        "readme": "README.md",
        "start": "START_HERE.md",
        "research_md": "RESEARCH_INDEX.md",
        "index": "docs/index.html",
        "learn": "docs/learn.html",
    }
    return {key: (root / rel).read_text(encoding="utf-8") for key, rel in names.items()}


def count_patterns(text: str, patterns: tuple[str, ...]) -> int:
    lowered = text.casefold()
    return sum(len(re.findall(pattern, lowered)) for pattern in patterns)


def validate(root: Path) -> dict[str, Any]:
    files = {
        "status": root / "STATUS.md",
        "agents": root / "AGENTS.md",
        "release": root / "PUBLIC_REVIEW_RELEASE.md",
        "formalization_hold": root / "PUBLIC_REVIEW_FORMALIZATION_HOLD_2026-07-29.md",
        "standard": root / "FULL_LEAN_RELEASE_STANDARD.md",
        "program": root / "FULL_LEAN_VERIFICATION_PROGRAM.md",
        "correction": root / "FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md",
        "paper_matrix": root / "PAPER_1_3_FULL_LEAN_STATUS.json",
        "portfolio": root / "formal-verification-status.json",
        "research_index": root / "research-index.json",
        "hinc_status": root / "papers/HINC-001/STATUS.json",
        "hinc_formal": root / "papers/HINC-001/FORMAL_VERIFICATION.md",
        "abf_status": root / "papers/ABF-001/STATUS.json",
        "abf_formal": root / "papers/ABF-001/FORMAL_VERIFICATION.md",
        "abf_lane": root / "papers/ABF-001/formal/FORMAL_STATUS_V1.json",
        "hinc_gate": root / "reports/publication-gates/HINC-001.json",
        "abf_gate": root / "reports/publication-gates/ABF-001.json",
        "index": root / "docs/index.html",
        "learn": root / "docs/learn.html",
    }

    failures: list[dict[str, Any]] = []
    counts: dict[str, int] = {}

    def check(category: str, condition: bool, **context: Any) -> None:
        counts[category] = counts.get(category, 0) + 1
        if not condition:
            failures.append({"category": category, **context})

    for name, path in files.items():
        check("required_file", path.is_file(), name=name, path=str(path.relative_to(root)))
    if not all(path.is_file() for path in files.values()):
        return {"schema": SCHEMA, "result": "FAIL", "checks": counts, "failures": failures}

    portfolio = load_json(files["portfolio"])
    matrix = load_json(files["paper_matrix"])
    index_data = load_json(files["research_index"])
    hinc = load_json(files["hinc_status"])
    abf = load_json(files["abf_status"])
    hinc_gate = load_json(files["hinc_gate"])
    abf_gate = load_json(files["abf_gate"])
    abf_lane = load_json(files["abf_lane"])
    texts = text_files(root)
    combined = "\n".join(texts.values())
    combined_fold = combined.casefold()
    site = texts["index"] + "\n" + texts["learn"]
    site_fold = site.casefold()

    expected_portfolio = {
        "HINC-001": ("ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW", "PARTIAL_PASS", True),
        "ABF-001": ("ACTIVE_PUBLIC_CANDIDATE_TECHNICAL_REVIEW", "PARTIAL_PASS", True),
        "FSG-001": ("PRIVATE_CANDIDATE_MATHEMATICAL_BLOCKER_HOLD", "HOLD_MATHEMATICAL_BLOCKER", False),
        "ACM-001": ("HOLD_PENDING_CONSOLIDATION", "HOLD_PENDING_CONSOLIDATION", False),
    }
    for paper_id, (public_state, formal_state, active) in expected_portfolio.items():
        record = portfolio.get("portfolio", {}).get(paper_id, {})
        check("canonical_public_state", record.get("public_state") == public_state, paper_id=paper_id, expected=public_state, actual=record.get("public_state"))
        check("canonical_formal_state", record.get("formal_status") == formal_state, paper_id=paper_id, expected=formal_state, actual=record.get("formal_status"))
        check("canonical_full_state", record.get("full_manuscript_lean_verified") is False, paper_id=paper_id)
        matrix_record = matrix.get("papers", {}).get(paper_id, {})
        check("matrix_formal_state", matrix_record.get("formal_status") == formal_state, paper_id=paper_id, expected=formal_state, actual=matrix_record.get("formal_status"))
        if active:
            check("matrix_active_state", matrix_record.get("active_public_review_authorized") is True, paper_id=paper_id)

    research = {item.get("id"): item for item in index_data.get("papers", []) if isinstance(item, dict)}
    expected_index_states = {"HINC-001": "active_review", "ABF-001": "active_review", "FSG-001": "hold", "ACM-001": "hold"}
    for paper_id, expected in expected_index_states.items():
        check("research_index_state", research.get(paper_id, {}).get("state") == expected, paper_id=paper_id, expected=expected, actual=research.get(paper_id, {}).get("state"))

    check("hinc_formal_state", hinc.get("formal_verification", {}).get("status") == "PARTIAL_PASS_BOUNDED_LEAN_VERIFICATION")
    check("hinc_public_review_authorized", hinc.get("release", {}).get("public_authorized") is True)
    check("hinc_channel", hinc.get("release", {}).get("channel") == "public_review")
    check("abf_formal_state", abf.get("formal_verification", {}).get("status") == "PARTIAL_PASS_BOUNDED_A01_LEAN_VERIFICATION")
    check("abf_public_review_authorized", abf.get("release", {}).get("public_authorized") is True)
    check("abf_channel", abf.get("release", {}).get("channel") == "public_review")
    check("abf_a01_pass", abf_lane.get("lanes", {}).get("A01_bidual_moment_kernel") == "COMPILED_PASS")
    check("abf_lane_not_full", abf_lane.get("full_manuscript_lean_verified") is False)
    check("hinc_gate_pass", hinc_gate.get("status") == "PASS_PUBLIC_TECHNICAL_REVIEW")
    check("abf_gate_pass", abf_gate.get("status") == "PASS_PUBLIC_TECHNICAL_REVIEW")

    required_phrases = (
        "HINC-001  active public candidate technical review".casefold(),
        "ABF-001   active public candidate technical review".casefold(),
        "PARTIAL_PASS / bounded Lean verification".casefold(),
        "PARTIAL_PASS / bounded A01 Lean verification".casefold(),
        "HOLD -- MATHEMATICAL BLOCKER".casefold(),
        "C06 / main theorem item (v) false as written".casefold(),
        "No public FSG theorem package has been released".casefold(),
        "ACM-001   hold pending consolidation".casefold(),
    )
    for phrase in required_phrases:
        check("required_status_wording", phrase in combined_fold, phrase=phrase)

    required_site_phrases = (
        "Active candidate public technical review".casefold(),
        "Bounded Lean PASS".casefold(),
        "Bounded A01 Lean PASS".casefold(),
        "full manuscript incomplete".casefold(),
        "HOLD -- MATHEMATICAL BLOCKER".casefold(),
        "No public theorem package released".casefold(),
        "Hold pending consolidation".casefold(),
    )
    for phrase in required_site_phrases:
        check("required_site_wording", phrase in site_fold, phrase=phrase)

    old_current_state_phrases = (
        "no active theorem packages",
        "active theorem status suspended",
        "suspended pending full lean",
        "public archive full-lean hold",
        "public archive full-lean hold",
        "blocked until papers 1",
        "blocked until papers 1",
        "full_pass sole active",
    )
    for phrase in old_current_state_phrases:
        check("superseded_current_wording_absent", phrase not in combined_fold, phrase=phrase)

    private_fsg_patterns = (
        "pr #428",
        "github.com/novakprotocol/n-mathlab",
        "papers/mcrc-fibonacci-sandpile-v3",
        "agent/mcrc-fibonacci",
        "pass_public_technical_review_fsg",
    )
    private_fsg_links_exposed = sum(combined_fold.count(pattern) for pattern in private_fsg_patterns)
    check("private_fsg_links_absent", private_fsg_links_exposed == 0, count=private_fsg_links_exposed)

    full_lean_overclaim = count_patterns(
        combined,
        (
            r"hinc-001\s+is\s+fully\s+lean",
            r"abf-001\s+is\s+fully\s+lean",
            r"the\s+manuscripts\s+are\s+fully\s+formalized",
            r"all\s+claims\s+are\s+machine\s+checked",
        ),
    )
    peer_review_overclaim = count_patterns(combined, (r"peer\s+reviewed\s*:\s*yes", r"peer\s+reviewed</span><strong>yes", r"peer_reviewed\s*=\s*true"))
    historical_priority_overclaim = count_patterns(combined, (r"historical\s+priority\s*:\s*established", r"historical_priority_established\s*=\s*true"))
    check("full_lean_overclaim_absent", full_lean_overclaim == 0, count=full_lean_overclaim)
    check("peer_review_overclaim_absent", peer_review_overclaim == 0, count=peer_review_overclaim)
    check("historical_priority_overclaim_absent", historical_priority_overclaim == 0, count=historical_priority_overclaim)

    return {
        "schema": SCHEMA,
        "result": "PASS" if not failures else "FAIL",
        "total_checks": sum(counts.values()),
        "checks": dict(sorted(counts.items())),
        "failures": failures,
        "conflicting_publication_states": sum(1 for item in failures if item["category"] in {"canonical_public_state", "research_index_state", "matrix_active_state", "hinc_public_review_authorized", "abf_public_review_authorized", "hinc_gate_pass", "abf_gate_pass"}),
        "conflicting_formal_states": sum(1 for item in failures if item["category"] in {"canonical_formal_state", "matrix_formal_state", "hinc_formal_state", "abf_formal_state"}),
        "private_fsg_links_exposed": private_fsg_links_exposed,
        "hinc_active_status_present": "yes" if not any(item for item in failures if item.get("paper_id") == "HINC-001" and item["category"] in {"research_index_state", "canonical_public_state", "matrix_active_state"}) else "no",
        "abf_active_status_present": "yes" if not any(item for item in failures if item.get("paper_id") == "ABF-001" and item["category"] in {"research_index_state", "canonical_public_state", "matrix_active_state"}) else "no",
        "fsg_mathematical_hold_present": "yes" if "hold -- mathematical blocker" in combined_fold else "no",
        "acm_hold_present": "yes" if "hold pending consolidation" in combined_fold else "no",
        "full_lean_overclaim": full_lean_overclaim,
        "peer_review_overclaim": peer_review_overclaim,
        "historical_priority_overclaim": historical_priority_overclaim,
        "files": {str(path.relative_to(root)): {"sha256": digest(path), "bytes": path.stat().st_size} for path in files.values()},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = validate(args.root.resolve())
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if result["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
