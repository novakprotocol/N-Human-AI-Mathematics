#!/usr/bin/env python3
"""Cross-check publication and formal states across all public control surfaces."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "n.human_ai_mathematics.status_consistency_validation.v1"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"expected JSON object: {path}")
    return value


def validate(root: Path) -> dict[str, Any]:
    files = {
        "status": root / "STATUS.md",
        "agents": root / "AGENTS.md",
        "release": root / "PUBLIC_REVIEW_RELEASE.md",
        "hold": root / "PUBLIC_REVIEW_FORMALIZATION_HOLD_2026-07-29.md",
        "standard": root / "FULL_LEAN_RELEASE_STANDARD.md",
        "paper_matrix": root / "PAPER_1_3_FULL_LEAN_STATUS.json",
        "portfolio": root / "formal-verification-status.json",
        "research_index": root / "research-index.json",
        "hinc_status": root / "papers/HINC-001/STATUS.json",
        "hinc_formal": root / "papers/HINC-001/FORMAL_VERIFICATION.md",
        "abf_status": root / "papers/ABF-001/STATUS.json",
        "abf_formal": root / "papers/ABF-001/FORMAL_VERIFICATION.md",
        "abf_lane": root / "papers/ABF-001/formal/FORMAL_STATUS_V1.json",
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
    abf_lane = load_json(files["abf_lane"])

    text = {
        name: path.read_text(encoding="utf-8")
        for name, path in files.items()
        if path.suffix in {".md", ".html"}
    }
    combined = "\n".join(text.values()).lower()
    current_status_text = "\n".join(
        text[name]
        for name in (
            "status",
            "release",
            "hold",
            "hinc_formal",
            "abf_formal",
            "index",
            "learn",
        )
    ).lower()

    canonical = {
        "HINC-001": {
            "public": "PUBLIC_ARCHIVE_FULL_LEAN_REQUALIFICATION_HOLD",
            "formal": "PARTIAL_PASS",
            "full": False,
        },
        "ABF-001": {
            "public": "PUBLIC_ARCHIVE_FULL_LEAN_REQUALIFICATION_HOLD",
            "formal": "PARTIAL_PASS",
            "full": False,
        },
        "FSG-001": {
            "public": "PRIVATE_FULL_LEAN_COMPLETION_HOLD",
            "formal": "PARTIAL_BOOTSTRAP_PASS",
            "full": False,
        },
        "ACM-001": {
            "public": "TEACHING_PREVIEW_BLOCKED_UNTIL_PAPERS_1_3_FULL_PASS",
            "formal": "BLOCKED_BY_CONSOLIDATION",
            "full": False,
        },
    }

    for paper_id, expected in canonical.items():
        record = portfolio.get("portfolio", {}).get(paper_id, {})
        check(
            "canonical_public_state",
            record.get("public_state") == expected["public"],
            paper_id=paper_id,
            expected=expected["public"],
            actual=record.get("public_state"),
        )
        check(
            "canonical_formal_state",
            record.get("formal_status") == expected["formal"],
            paper_id=paper_id,
            expected=expected["formal"],
            actual=record.get("formal_status"),
        )
        check(
            "canonical_full_state",
            record.get("full_manuscript_lean_verified") is expected["full"],
            paper_id=paper_id,
        )
        matrix_record = matrix.get("papers", {}).get(paper_id, {})
        check(
            "matrix_formal_state",
            matrix_record.get("formal_status") == expected["formal"],
            paper_id=paper_id,
            expected=expected["formal"],
            actual=matrix_record.get("formal_status"),
        )

    research = {
        item.get("id"): item for item in index_data.get("papers", []) if isinstance(item, dict)
    }
    expected_index_states = {
        "HINC-001": "public_archive_full_lean_requalification_hold",
        "ABF-001": "public_archive_full_lean_requalification_hold",
        "FSG-001": "private_full_lean_completion_hold",
        "ACM-001": "blocked_until_papers_1_3_full_pass",
    }
    for paper_id, expected in expected_index_states.items():
        check(
            "research_index_state",
            research.get(paper_id, {}).get("state") == expected,
            paper_id=paper_id,
            expected=expected,
            actual=research.get(paper_id, {}).get("state"),
        )

    check(
        "hinc_formal_state",
        hinc.get("formal_verification", {}).get("status")
        == "PARTIAL_PASS_FULL_MANUSCRIPT_REQUALIFICATION_HOLD",
    )
    check("hinc_not_authorized", hinc.get("release", {}).get("public_authorized") is False)
    check(
        "abf_formal_state",
        abf.get("formal_verification", {}).get("status")
        == "PARTIAL_PASS_FULL_MANUSCRIPT_REQUALIFICATION_HOLD",
    )
    check("abf_not_authorized", abf.get("release", {}).get("public_authorized") is False)
    check("abf_a01_pass", abf_lane.get("lanes", {}).get("A01_bidual_moment_kernel") == "COMPILED_PASS")
    check("abf_lane_not_full", abf_lane.get("full_manuscript_lean_verified") is False)
    check("abf_lane_not_authorized", abf_lane.get("public_release_authorized") is False)

    required_phrases = (
        "active theorem packages under the current rule: none",
        "historical public artifacts",
        "full-lean requalification hold",
        "full-lean completion",
        "blocked until papers 1–3",
        "full-manuscript lean",
    )
    for phrase in required_phrases:
        check("required_status_wording", phrase in combined, phrase=phrase)

    contradictions = (
        "hinc-001 and abf-001 are active candidate packages",
        "hinc-001 is the only released package",
        "abf-001 — standalone public package pending",
        "active public review",
        "two active packages",
        "private release edge",
        "public technical review:     active",
    )
    for phrase in contradictions:
        check("contradiction_absent", phrase not in current_status_text, phrase=phrase)

    check("portfolio_no_active", portfolio.get("active_theorem_packages") == [])
    check("portfolio_no_full", portfolio.get("papers_with_full_pass") == [])
    check("portfolio_no_auth", portfolio.get("public_release_authorized") is False)
    check("matrix_no_auth", matrix.get("public_release_authorized") is False)

    return {
        "schema": SCHEMA,
        "result": "PASS" if not failures else "FAIL",
        "total_checks": sum(counts.values()),
        "checks": dict(sorted(counts.items())),
        "failures": failures,
        "conflicting_publication_states": sum(
            1
            for item in failures
            if item["category"]
            in {"canonical_public_state", "research_index_state", "contradiction_absent"}
        ),
        "conflicting_formal_states": sum(
            1
            for item in failures
            if item["category"]
            in {"canonical_formal_state", "matrix_formal_state", "hinc_formal_state", "abf_formal_state"}
        ),
        "files": {
            str(path.relative_to(root)): {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in files.values()
        },
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
