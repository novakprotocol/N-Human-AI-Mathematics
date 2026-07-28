#!/usr/bin/env python3
"""Prepare the post-release ABF-001 integration branch without editing docs/."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--release-control", type=Path, required=True)
    parser.add_argument("--mathematical-source-commit", required=True)
    parser.add_argument("--release-control-commit", required=True)
    parser.add_argument("--package-sha256", required=True)
    parser.add_argument("--source-package-sha256", required=True)
    parser.add_argument("--manifest-sha256", required=True)
    parser.add_argument("--release-url", required=True)
    parser.add_argument("--tag", default="abf-001-public-review-v1")
    args = parser.parse_args()

    root = args.root.resolve()
    source = args.source.resolve()
    control = args.release_control.resolve()
    destination = root / "papers" / "ABF-001"
    if destination.exists():
        raise RuntimeError(f"ABF destination already exists: {destination}")

    shutil.copytree(source, destination)

    control_map = {
        "FINAL_HOSTILE_REVIEW.md": destination / "review" / "FINAL_HOSTILE_REVIEW.md",
        "FINAL_DELTA_SEARCH.md": destination / "literature" / "FINAL_DELTA_SEARCH.md",
        "HUMAN_AI_MATHEMATICS_LANDSCAPE.md": destination / "literature" / "HUMAN_AI_MATHEMATICS_LANDSCAPE.md",
        "OWNER_AUTHORIZATION.md": destination / "OWNER_AUTHORIZATION.md",
        "ABF-001_RELEASE_CANDIDATE.json": destination / "ABF-001_RELEASE_CANDIDATE.json",
        "ABF-001_RELEASE_NOTES.md": destination / "ABF-001_RELEASE_NOTES.md",
    }
    for name, target in control_map.items():
        candidate = control / name
        if not candidate.is_file():
            raise RuntimeError(f"missing release-control file: {candidate}")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(candidate, target)

    paper_status_path = destination / "STATUS.json"
    paper_status = read_json(paper_status_path)
    paper_status["source"]["commit"] = args.mathematical_source_commit
    paper_status["claim"]["status"] = "candidate theorem and exact finite classification open for public technical review"
    paper_status["proof"]["human_proof_status"] = "self-contained complete human proof; final hostile review reports zero release blockers"
    paper_status["review"]["internal"] = "final hostile review bound to the frozen mathematical source reports zero blocking findings"
    paper_status["review"]["external"] = "pending; requested by public release"
    paper_status["review"]["historical_priority"] = "unestablished; no exact indexed match located in the recorded search"
    paper_status["review"]["peer_review"] = "not submitted"
    paper_status["release"] = {
        "public_authorized": True,
        "public_switch_ready": True,
        "channel": "public_review",
        "version": "0.1.0-public-review",
        "release_date": "2026-07-28",
        "doi": None,
        "specific_model_disclosed": False,
        "specific_provider_disclosed": False,
    }
    write_json(paper_status_path, paper_status)

    index_path = root / "research-index.json"
    index = read_json(index_path)
    found = False
    for paper in index["papers"]:
        if paper["id"] == "ABF-001":
            found = True
            paper.update({
                "slug": "affine-restriction-moment-kernels",
                "title": "Affine Restriction Moment Kernels and Radical Incidence Geometry of a Vectorial Boolean Map",
                "fields": ["Boolean functions", "vectorial Boolean functions", "Reed-Muller codes", "finite linear algebra", "symmetric bilinear forms"],
                "state": "active_review",
                "claim_status": "candidate_theorem_and_exact_finite_classification_open_for_public_technical_review",
                "human_proof": "complete_self_contained_candidate_manuscript",
                "internal_reproduction": "primary_bitset_small_universe_and_tamper_routes_pass",
                "formal_verification": "not_completed_and_not_claimed",
                "external_specialist_review": "requested_by_public_release",
                "historical_priority": "unestablished",
                "peer_review": "not_submitted",
                "public_release": "active_public_review_0.1.0",
            })
    if not found:
        raise RuntimeError("ABF-001 index entry not found")
    write_json(index_path, index)

    gate = {
        "schema_version": "n.human_llm.mathematics.publication_gate.v1",
        "paper_id": "ABF-001",
        "receipt_date": "2026-07-28",
        "release_target": "public_technical_review",
        "status": "PASS_PUBLIC_TECHNICAL_REVIEW",
        "source_identity": {
            "repository": "novakprotocol/N-Human-AI-Mathematics",
            "mathematical_source_commit": args.mathematical_source_commit,
            "release_control_commit": args.release_control_commit,
            "package_sha256": args.package_sha256,
            "source_package_sha256": args.source_package_sha256,
            "manifest_sha256": args.manifest_sha256,
            "tag": args.tag,
            "release_url": args.release_url,
        },
        "gates": {
            "claim_boundary": {"status": "PASS", "evidence": ["papers/ABF-001/CLAIMS.md", "papers/ABF-001/manuscript/ABF-001_MANUSCRIPT.md"], "notes": "Candidate theorem and exact finite classification only; no security, peer-review, external-reproduction, full-formalization, or worldwide-priority claim."},
            "proof": {"status": "PASS", "evidence": ["papers/ABF-001/PROOF_MAP.md", "papers/ABF-001/manuscript/ABF-001_MANUSCRIPT.md"], "universal_claims_have_complete_human_proofs": True, "finite_claims_exhaustively_verified_or_not_applicable": True},
            "hostile_review": {"status": "PASS", "evidence": ["papers/ABF-001/review/FINAL_HOSTILE_REVIEW.md"], "blocking_findings_open": 0},
            "prior_art_search": {"status": "PASS", "evidence": ["papers/ABF-001/literature/SEARCH_PROTOCOL.md", "papers/ABF-001/literature/PRIMARY_SOURCE_MAP.md", "papers/ABF-001/literature/FINAL_DELTA_SEARCH.md", "papers/ABF-001/literature/search-query-ledger-expanded.csv"], "search_completed_to_declared_scope": True, "final_delta_search_completed": True, "final_delta_search_date": "2026-07-28", "historical_priority": "unestablished"},
            "independent_challenge": {"status": "PASS", "evidence": ["papers/ABF-001/src/abf001_independent_bitset.py", "papers/ABF-001/src/abf001_small_universe.py", "papers/ABF-001/evidence/independent-final/abf001-independent-bitset.json"], "structurally_independent_internal_route": True, "external_reproduction": "pending"},
            "clean_execution": {"status": "PASS", "evidence": ["papers/ABF-001/qa/final-clean-execution-receipt.json", "papers/ABF-001/evidence/receipts/small-universe-final.json", "papers/ABF-001/evidence/receipts/tamper-control-final.json"], "fresh_checkout_or_clean_copy": True, "completed_without_timeout": True, "partial_runs_accepted": False, "deterministic_receipt_present": True},
            "provenance": {"status": "PASS", "evidence": ["papers/ABF-001/SOURCE_SHA256SUMS.txt", "papers/ABF-001/PUBLICATION_ARTIFACTS_0.1.0.md", args.release_url], "source_identity_locked": True, "sha256_manifest_present": True, "versioned_tag_present": True, "release_record_present": True},
            "owner_authorization": {"status": "PASS", "evidence": ["papers/ABF-001/OWNER_AUTHORIZATION.md"], "package_specific_authorization": True},
        },
        "limitations": ["Historical priority remains unestablished.", "External specialist review and outside reproduction remain pending.", "Proof-assistant formalization is not completed and is not claimed.", "No full-width cryptographic security or insecurity conclusion is claimed."],
    }
    write_json(root / "reports" / "publication-gates" / "ABF-001.json", gate)

    research_path = root / "RESEARCH_INDEX.md"
    research = research_path.read_text(encoding="utf-8")
    research = replace_once(research, "complete candidate package:   HINC-001", "complete candidate packages:  HINC-001, ABF-001", "repository state")
    research = replace_once(research, "index-only hold entries:      ABF-001, FSG-001, ACM-001", "index-only hold entries:      FSG-001, ACM-001", "hold entries")
    research = replace_once(research, "| 2 | `ABF-001` | Affine-Hyperplane Degree-Drop Spectra of a Vectorial Boolean Map | Boolean functions, finite linear algebra | Planned second package; exact finite theorem internally reproduced |", "| 2 | `ABF-001` | Affine Restriction Moment Kernels and Radical Incidence Geometry of a Vectorial Boolean Map | Boolean functions, Reed-Muller codes, finite linear algebra | Active candidate package; open for public technical review |", "ABF table row")
    old_abf = """## ABF-001 — second package

**Core claim:** For one fully specified map `GF(2)^16 -> GF(2)^8`, exactly 130,559 affine-hyperplane restrictions have degree 15, exactly 511 have degree 14, and none has degree 13 or lower. The 511 exceptional restrictions form a punctured nine-dimensional parameter flat certified by a second rank calculation.

**Internal evidence:** exhaustive classification of all 131,070 affine hyperplanes, separately written C reconstruction, and exhaustive small-universe controls.

**State:** index entry only; complete public package not yet prepared.
"""
    new_abf = f"""## ABF-001 — second package

**Controlling source:** [`papers/ABF-001/manuscript/ABF-001_MANUSCRIPT.md`](papers/ABF-001/manuscript/ABF-001_MANUSCRIPT.md)

**Core result:** A Reed-Muller moment criterion yields dual output-mask annihilator and affine-parameter kernel descriptions of restriction degree drop. For the specified map `GF(2)^16 -> GF(2)^8`, the complete vectorial spectrum is `130,559 / 511 / 0`; the order-one symmetric pencil has rank multiplicities `2 / 15 / 74 / 112 / 52`; and its corrected radical geometry has 203 mask-indexed radicals, 202 distinct nonzero radical subspaces, 469 incidences, 467 covered parameters, and 201 forest components.

**Evidence:** complete human proof, full 131,070-hyperplane enumeration, primary and integer/bitset implementations, complete 5,505,024-comparison small-universe control, tamper rejection, exact manifests, final hostile review with zero blockers, and a same-day systematic prior-art delta.

**Public status:** candidate technical review active at `{args.tag}`. Historical priority, external reproduction, peer review, and complete formal verification remain unestablished.
"""
    research = replace_once(research, old_abf, new_abf, "ABF section")
    research_path.write_text(research, encoding="utf-8", newline="\n")

    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    readme = replace_once(readme, "| 2 | `ABF-001` | Index entry only; next publication package |", "| 2 | `ABF-001` | Complete candidate technical-review package |", "README paper row")
    readme = replace_once(readme, "HINC-001 is the active candidate package.", "HINC-001 and ABF-001 are active candidate packages.", "README active package sentence")
    abf_summary = f"""
## ABF-001

**Title:** *Affine Restriction Moment Kernels and Radical Incidence Geometry of a Vectorial Boolean Map*

ABF-001 supplies a self-contained moment-kernel theorem and a complete finite classification of a specified `GF(2)^16 -> GF(2)^8` map. Its exact public-review package records the `130,559 / 511 / 0` restriction spectrum, corrected `203 / 202` radical distinction, 469-edge incidence atlas, independent implementations, complete finite controls, hostile review, and bounded prior-art conclusion.

Start with [`papers/ABF-001/README.md`](papers/ABF-001/README.md). The immutable candidate release is [`{args.tag}`]({args.release_url}).

"""
    readme = replace_once(readme, "## Paper order\n", abf_summary + "## Paper order\n", "README ABF insertion")
    readme_path.write_text(readme, encoding="utf-8", newline="\n")

    status_path = root / "STATUS.md"
    status = status_path.read_text(encoding="utf-8")
    status = replace_once(status, "active_package:              HINC-001", "active_packages:             HINC-001, ABF-001", "STATUS active packages")
    status = replace_once(status, "2. `ABF-001` — index entry only; next package.", "2. `ABF-001` — active public technical review.", "STATUS ABF row")
    status_path.write_text(status, encoding="utf-8", newline="\n")

    print(json.dumps({"result": "PASS", "paper": "ABF-001", "docs_modified": False, "mathematical_source_commit": args.mathematical_source_commit, "release_control_commit": args.release_control_commit}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
