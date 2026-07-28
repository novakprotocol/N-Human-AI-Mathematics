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


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


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
