#!/usr/bin/env python3
"""Run the ABF integration generator and correct release-evidence references."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--root", type=Path, required=True)
    known, _ = parser.parse_known_args()

    v2 = Path(__file__).with_name("prepare_abf001_integration_v2.py")
    subprocess.run([sys.executable, str(v2), *sys.argv[1:]], check=True)

    root = known.root.resolve()
    gate_path = root / "reports" / "publication-gates" / "ABF-001.json"
    gate = json.loads(gate_path.read_text(encoding="utf-8"))
    gate["gates"]["provenance"]["evidence"] = [
        "papers/ABF-001/SOURCE_SHA256SUMS.txt",
        "papers/ABF-001/ABF-001_RELEASE_CANDIDATE.json",
        gate["source_identity"]["release_url"],
    ]
    gate_path.write_text(
        json.dumps(gate, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"result": "PASS", "provenance_evidence_corrected": True}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
