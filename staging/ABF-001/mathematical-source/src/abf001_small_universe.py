#!/usr/bin/env python3
"""Complete small-universe control for the ABF-001 moment criterion.

Enumerates all 65,536 vectorial maps F: GF(2)^3 -> GF(2)^2, all 14 affine
hyperplanes, all three nonzero output masks, and moment orders r=0,1.
It compares direct restriction ANF degree with ambient moment vanishing.
Total exact comparisons: 65,536 * 14 * 3 * 2 = 5,505,024.

This implementation is standalone and imports neither ABF primary verifier.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from pathlib import Path

FUNCTIONS = 1 << 16  # two output bits at each of eight input points
NORMALS = tuple(range(1, 8))
OFFSETS = (0, 1)
MASKS = (1, 2, 3)
ORDERS = (0, 1)
EXPECTED_COMPARISONS = FUNCTIONS * len(NORMALS) * len(OFFSETS) * len(MASKS) * len(ORDERS)


def parity(x: int) -> int:
    return x.bit_count() & 1


def kernel_basis(a: int) -> tuple[int, int]:
    vectors = [x for x in range(1, 8) if parity(a & x) == 0]
    u = vectors[0]
    v = next(x for x in vectors[1:] if x != u)
    if v == u:
        raise AssertionError
    return u, v


def affine_points(a: int, b: int) -> tuple[int, int, int, int]:
    p0 = next(x for x in range(8) if parity(a & x) == b)
    u, v = kernel_basis(a)
    points = (p0, p0 ^ u, p0 ^ v, p0 ^ u ^ v)
    if len(set(points)) != 4:
        raise AssertionError((a, b, points))
    return points


def scalar_value(function: int, x: int, mask: int) -> int:
    output = (function >> (2 * x)) & 3
    return parity(output & mask)


def anf_degree_four(values: tuple[int, int, int, int]) -> int:
    coeff = list(values)
    coeff[1] ^= coeff[0]
    coeff[3] ^= coeff[2]
    coeff[2] ^= coeff[0]
    coeff[3] ^= coeff[1]
    degrees = (-1, 1, 1, 2)
    degree = -1
    for index, value in enumerate(coeff):
        if value:
            degree = max(degree, degrees[index] if index else 0)
    return degree


def moments_vanish(function: int, a: int, b: int, mask: int, order: int) -> bool:
    points = affine_points(a, b)
    # empty monomial
    total = 0
    for x in points:
        total ^= scalar_value(function, x, mask)
    if total:
        return False
    if order == 0:
        return True
    for coordinate in range(3):
        total = 0
        for x in points:
            if (x >> coordinate) & 1:
                total ^= scalar_value(function, x, mask)
        if total:
            return False
    return True


def run() -> dict:
    start = time.perf_counter()
    comparisons = 0
    failures: list[dict] = []
    hyperplanes = [(a, b, affine_points(a, b)) for a in NORMALS for b in OFFSETS]

    for function in range(FUNCTIONS):
        for a, b, points in hyperplanes:
            for mask in MASKS:
                values = tuple(scalar_value(function, x, mask) for x in points)
                degree = anf_degree_four(values)
                for order in ORDERS:
                    threshold = 1 - order
                    direct = degree <= threshold
                    moment = moments_vanish(function, a, b, mask, order)
                    comparisons += 1
                    if direct != moment:
                        failures.append({
                            "function_hex": f"{function:04x}",
                            "normal": a,
                            "offset": b,
                            "mask": mask,
                            "order": order,
                            "degree": degree,
                            "direct": direct,
                            "moment": moment,
                        })
                        if len(failures) >= 20:
                            raise AssertionError(failures)

    elapsed = time.perf_counter() - start
    if comparisons != EXPECTED_COMPARISONS:
        raise AssertionError((comparisons, EXPECTED_COMPARISONS))
    if failures:
        raise AssertionError(failures)

    report = {
        "schema_version": "n.human_llm_mathematics.abf001.small_universe.v1",
        "result": "PASS",
        "universe": {
            "maps": FUNCTIONS,
            "affine_hyperplanes_per_map": 14,
            "nonzero_output_masks": 3,
            "moment_orders": [0, 1],
            "comparisons": comparisons,
        },
        "failures": 0,
        "implementation": "standalone direct restriction ANF versus ambient moment sums",
        "python": sys.version,
        "platform": platform.platform(),
        "elapsed_seconds": round(elapsed, 6),
    }
    canonical = json.dumps(report, sort_keys=True, separators=(",", ":")).encode("utf-8")
    report["evidence_sha256"] = hashlib.sha256(canonical).hexdigest()
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
