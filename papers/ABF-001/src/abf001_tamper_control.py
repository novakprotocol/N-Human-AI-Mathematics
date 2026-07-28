#!/usr/bin/env python3
"""Negative control: one-bit truth-table tamper must be rejected."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from abf001_independent_bitset import truth_table, xor_moment, rank_rows

EXPECTED_TRUTH_SHA = "2a861e09dcb5b00e208ede53e1b29615a5309389a83da40f81d663ec760e7e52"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    table = truth_table()
    original = hashlib.sha256(bytes(table)).hexdigest()
    table[0] ^= 1
    tampered = hashlib.sha256(bytes(table)).hexdigest()

    # Recompute the eight-row top-layer signature rank after the one-bit flip.
    full = 0
    for value in table:
        full ^= value
    degree15 = []
    for j in range(16):
        coefficient = 0
        for x, value in enumerate(table):
            if ((x >> j) & 1) == 0:
                coefficient ^= value
        degree15.append(coefficient)
    columns = [value ^ full for value in degree15]
    rows = []
    for bit in range(8):
        row = (full >> bit) & 1
        for j, column in enumerate(columns):
            row |= ((column >> bit) & 1) << (j + 1)
        rows.append(row)
    tampered_signature_rank = rank_rows(rows, 17)[0]

    if original != EXPECTED_TRUTH_SHA:
        raise AssertionError((EXPECTED_TRUTH_SHA, original))
    if tampered == EXPECTED_TRUTH_SHA:
        raise AssertionError("one-bit tamper did not change the truth-table identity")

    report = {
        "schema_version": "n.human_llm_mathematics.abf001.tamper_control.v1",
        "result": "PASS",
        "tamper": "output bit 0 at input 0 flipped",
        "original_truth_sha256": original,
        "tampered_truth_sha256": tampered,
        "expected_identity_rejected": True,
        "tampered_signature_rank": tampered_signature_rank,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
