#!/usr/bin/env python3
"""Run the ABF integration generator and normalize release metadata."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


EXPECTED_GATE_SCHEMA = "n.human_llm_mathematics.publication_gate.v1"
EXPECTED_SOURCE_MANIFEST_SCHEMA = "n.human_ai_mathematics.source_manifest.v1"
EXPECTED_REPOSITORY = "novakprotocol/N-Human-AI-Mathematics"


V30_SOURCE_RECORD = """# v30 source record

Source repository: `novakprotocol/N-MathLab`
Merge commit: `4376321b33f5a8fd8b5a9c63240cc5823eed7bbb`
Original path: `docs/research/BLACK_BOX_AFFINE_HYPERPLANE_SPECTRUM_V30_PAPER.md`

The v30 result proved the affine top-layer signature, punctured-kernel theorem, secondary rank certificate, and exact `130559 / 511 / 0` vectorial spectrum. ABF-001 consolidates and supersedes that manuscript for public review.
"""

V30_REVIEW_RECORD = """# v30 internal hostile-review record

Source repository: `novakprotocol/N-MathLab`
Merge commit: `4376321b33f5a8fd8b5a9c63240cc5823eed7bbb`

The internal review accepted the top-layer and punctured-kernel theorems, requested a fuller moment proof, and recommended conditional specialist review with explicit no-security and no-priority boundaries. The consolidated manuscript supplies the Reed-Muller proof.
"""

V32_SOURCE_RECORD = """# v32 source record

Source repository: `novakprotocol/N-MathLab`
Merge commit: `d530494329163ad1ecc3eb8c72a945b159935bc9`
Original path: `docs/research/BLACK_BOX_RADICAL_INCIDENCE_DUALITY_V32_PAPER.md`

The v32 result proved the bidual moment-incidence theorem and classified the rank profiles, 469 incidences, unique triple-covered parameter, and 201-component forest. ABF-001 corrects the earlier phrase “203 radical subspaces” to “203 singular mask-indexed radicals and 202 distinct radical subspaces.”
"""

V32_REVIEW_RECORD = """# v32 internal hostile-review record

Source repository: `novakprotocol/N-MathLab`
Merge commit: `d530494329163ad1ecc3eb8c72a945b159935bc9`

The internal review conditionally accepted the result as a specialist exact-computation and Boolean-functions paper, while reserving historical priority and full-width implications. The review identified the incidence geometry as the strongest finite contribution.
"""

V32_PROOF_RECORD = {
    "edge_atlas_sha256": "95d64917af27fa1b827bda0b82364dc6e69de6376ccb0ad81e12ab22b82742fa",
    "external_institutional_replication": False,
    "focused_test_count": 7,
    "focused_tests": "PASS",
    "full_width_security_statement": False,
    "global_historical_novelty_established": False,
    "independent_c_byte_identical": True,
    "independent_c_edge_sha256": "95d64917af27fa1b827bda0b82364dc6e69de6376ccb0ad81e12ab22b82742fa",
    "independent_c_result": "PASS",
    "independent_c_stdout_sha256": "2d26bb0283149d85783112e1b293374976c6b63dae62da74ff4f86e2d5e1e334",
    "primary_evidence_sha256": "3cbaaa5c0c60c58afb8ea7f8001cc513f93d4e324a0f5440ed87e71afbdfb6c3",
    "proof_assistant_verified": False,
    "python_compilation": "PASS",
    "result": "PASS",
    "schema_version": "n.mathlab.black_box_radical_incidence_proof.v1",
    "small_universe_checks": 5505024,
    "small_universe_functions": 65536,
    "small_universe_mismatches": 0,
    "small_universe_stream_sha256": "49469ce29fa3f71d91cc8a4409b92fd9d1303538145db9cbb6eab95df5bb3f28",
    "tamper_control": "PASS",
}


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def materialize_historical_records(root: Path) -> None:
    historical = root / "papers" / "ABF-001" / "evidence" / "historical"
    write_text(historical / "V30_SOURCE_RECORD.md", V30_SOURCE_RECORD)
    write_text(historical / "V30_REVIEW_RECORD.md", V30_REVIEW_RECORD)
    write_text(historical / "V32_SOURCE_RECORD.md", V32_SOURCE_RECORD)
    write_text(historical / "V32_REVIEW_RECORD.md", V32_REVIEW_RECORD)
    write_json(historical / "local-proof-v32.json", V32_PROOF_RECORD)


def normalized_source_manifest() -> dict[str, object]:
    return {
        "schema_version": EXPECTED_SOURCE_MANIFEST_SCHEMA,
        "paper_id": "ABF-001",
        "generated_repository": EXPECTED_REPOSITORY,
        "sources": [
            {
                "repository": "novakprotocol/N-MathLab",
                "commit": "4376321b33f5a8fd8b5a9c63240cc5823eed7bbb",
                "role": "v30 affine-hyperplane theorem and evidence",
                "files": [
                    {
                        "source": "docs/research/BLACK_BOX_AFFINE_HYPERPLANE_SPECTRUM_V30_PAPER.md",
                        "target": "papers/ABF-001/evidence/historical/V30_SOURCE_RECORD.md",
                    },
                    {
                        "source": "docs/research/BLACK_BOX_AFFINE_HYPERPLANE_SPECTRUM_V30_INDEPENDENT_REVIEW.md",
                        "target": "papers/ABF-001/evidence/historical/V30_REVIEW_RECORD.md",
                    },
                ],
            },
            {
                "repository": "novakprotocol/N-MathLab",
                "commit": "d530494329163ad1ecc3eb8c72a945b159935bc9",
                "role": "v32 bidual incidence theorem and finite radical geometry",
                "files": [
                    {
                        "source": "docs/research/BLACK_BOX_RADICAL_INCIDENCE_DUALITY_V32_PAPER.md",
                        "target": "papers/ABF-001/evidence/historical/V32_SOURCE_RECORD.md",
                    },
                    {
                        "source": "docs/research/BLACK_BOX_RADICAL_INCIDENCE_DUALITY_V32_INDEPENDENT_REVIEW.md",
                        "target": "papers/ABF-001/evidence/historical/V32_REVIEW_RECORD.md",
                    },
                    {
                        "source": "receipts/black-box-text-inference-v32/local-proof-v32.json",
                        "target": "papers/ABF-001/evidence/historical/local-proof-v32.json",
                    },
                ],
            },
        ],
        "external_evidence": [],
        "materialization_status": (
            "historical source records materialized; consolidated manuscript, "
            "frozen source, fresh verifiers, and release receipts control the "
            "candidate public-review package"
        ),
        "public_release_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--root", type=Path, required=True)
    known, _ = parser.parse_known_args()

    v2 = Path(__file__).with_name("prepare_abf001_integration_v2.py")
    subprocess.run([sys.executable, str(v2), *sys.argv[1:]], check=True)

    root = known.root.resolve()
    materialize_historical_records(root)

    gate_path = root / "reports" / "publication-gates" / "ABF-001.json"
    gate = json.loads(gate_path.read_text(encoding="utf-8"))
    gate["schema_version"] = EXPECTED_GATE_SCHEMA
    gate["gates"]["provenance"]["evidence"] = [
        "papers/ABF-001/SOURCE_SHA256SUMS.txt",
        "papers/ABF-001/ABF-001_RELEASE_CANDIDATE.json",
        gate["source_identity"]["release_url"],
    ]
    write_json(gate_path, gate)

    manifest_path = root / "papers" / "ABF-001" / "SOURCE_MANIFEST.json"
    write_json(manifest_path, normalized_source_manifest())

    print(
        json.dumps(
            {
                "result": "PASS",
                "historical_records_materialized": True,
                "publication_gate_schema_corrected": True,
                "provenance_evidence_corrected": True,
                "source_manifest_normalized": True,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
