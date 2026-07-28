#!/usr/bin/env python3
"""Separately written bitset verifier for core ABF-001 finite claims.

This implementation deliberately avoids NumPy and does not import the primary
ABF-001 verifier. It reconstructs the reduced truth table, derives the top
restriction signature, builds all scalar order-one moment matrices as bit rows,
and independently reproduces the rank and radical-incidence invariants.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

N = 16
M = 8
PARAM = 17
TRUTH_SHA = "2a861e09dcb5b00e208ede53e1b29615a5309389a83da40f81d663ec760e7e52"
EDGE_SHA = "95d64917af27fa1b827bda0b82364dc6e69de6376ccb0ad81e12ab22b82742fa"
K = tuple(int(x) for x in "0111110101010010100010000101111110010101110110100001101101000110")


def schedule(block: int) -> list[int]:
    w = [(block >> i) & 1 for i in range(16)]
    while len(w) < 64:
        w.append(w[-16] ^ w[-7])
    return w


def reverse_round(state: int, word: int, constant: int) -> int:
    q = [(state >> i) & 1 for i in range(8)]
    a, b, c = q[1], q[2], q[3]
    e, f, g = q[5], q[6], q[7]
    maj = (a & b) ^ (a & c) ^ (b & c)
    t2 = a ^ maj
    t1 = q[0] ^ t2
    d = q[4] ^ t1
    ch = (e & f) ^ ((1 ^ e) & g)
    h = t1 ^ e ^ ch ^ constant ^ word
    return sum(bit << i for i, bit in enumerate((a,b,c,d,e,f,g,h)))


def fixed(block: int) -> int:
    state = 0
    w = schedule(block)
    for i in range(63, -1, -1):
        state = reverse_round(state, w[i], K[i])
    return state


def truth_table() -> list[int]:
    frozen = Path(__file__).resolve().parents[1] / "evidence" / "source" / "truth-table.bin"
    if frozen.is_file():
        raw = frozen.read_bytes()
        if len(raw) != 1 << N:
            raise AssertionError((1 << N, len(raw)))
        table = list(raw)
    else:
        table = [fixed(x) for x in range(1 << N)]
    digest = hashlib.sha256(bytes(table)).hexdigest()
    if digest != TRUTH_SHA:
        raise AssertionError((TRUTH_SHA, digest))
    return table


def xor_moment(table: list[int], mask: int) -> int:
    value = 0
    for x, y in enumerate(table):
        if x & mask == mask:
            value ^= y
    return value


def superset_xor_transform(table: list[int]) -> list[int]:
    work = list(table)
    for bit in range(N):
        step = 1 << bit
        for start in range(0, 1 << N, step << 1):
            for offset in range(step):
                work[start + offset] ^= work[start + step + offset]
    return work


def vector_anf(table: list[int]) -> list[int]:
    work = list(table)
    for bit in range(N):
        step = 1 << bit
        for mask in range(1 << N):
            if mask & step:
                work[mask] ^= work[mask ^ step]
    return work


def rank_rows(rows: list[int], width: int) -> tuple[int, list[int], list[int]]:
    rows = [r for r in rows]
    pivot_cols: list[int] = []
    r = 0
    for col in range(width):
        pivot = next((i for i in range(r, len(rows)) if (rows[i] >> col) & 1), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> col) & 1):
                rows[i] ^= rows[r]
        pivot_cols.append(col)
        r += 1
        if r == len(rows):
            break
    return r, rows, pivot_cols


def nullspace(rows: list[int], width: int) -> list[int]:
    rank, reduced, pivots = rank_rows(rows, width)
    free = [c for c in range(width) if c not in pivots]
    basis: list[int] = []
    for free_col in free:
        v = 1 << free_col
        for row_index in range(rank - 1, -1, -1):
            p = pivots[row_index]
            if (reduced[row_index] & v).bit_count() & 1:
                v |= 1 << p
        basis.append(v)
    return basis


def span(basis: list[int]):
    for selector in range(1 << len(basis)):
        value = 0
        for i, b in enumerate(basis):
            if selector >> i & 1:
                value ^= b
        yield value


def analyze(out: Path) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    table = truth_table()
    anf = vector_anf(table)
    full_mask = (1 << N) - 1
    full = anf[full_mask]
    degree15 = [anf[full_mask ^ (1 << j)] for j in range(N)]
    columns = [degree15[j] ^ full for j in range(N)]

    # Eight output-bit equations in 17 affine-parameter variables (beta,a).
    signature_rows = []
    for bit in range(M):
        row = ((full >> bit) & 1)
        for j, col in enumerate(columns):
            row |= ((col >> bit) & 1) << (j + 1)
        signature_rows.append(row)
    signature_rank = rank_rows(signature_rows, PARAM)[0]
    exceptional = [q for q in span(nullspace(signature_rows, PARAM)) if q and (q >> 1)]

    # Moments indexed by empty, singleton, and pair masks.
    moment_masks = [0] + [1 << i for i in range(N)]
    transformed = superset_xor_transform(table)
    moments = {mask: transformed[mask] for mask in moment_masks}
    for i in range(N):
        for j in range(i, N):
            mask = (1 << i) | (1 << j)
            moments[mask] = transformed[mask]

    histogram = Counter()
    radicals: dict[int, frozenset[int]] = {}
    edges = []
    point_masks: dict[int, list[int]] = defaultdict(list)
    for v in range(1, 256):
        rows = []
        basis_masks = [0] + [1 << i for i in range(N)]
        for mi in basis_masks:
            row = ((v & moments[mi]).bit_count() & 1)
            for j in range(N):
                mij = mi | (1 << j)
                row |= (((v & moments[mij]).bit_count() & 1) << (j + 1))
            rows.append(row)
        rank = rank_rows(rows, PARAM)[0]
        histogram[rank] += 1
        radical = frozenset(q for q in span(nullspace(rows, PARAM)) if q)
        if radical:
            radicals[v] = radical
        for q in sorted(radical):
            if not q >> 1:
                raise AssertionError("invalid parameter")
            point_masks[q].append(v)
            edges.append({
                "output_mask_hex": f"{v:02x}",
                "parameter_hex": f"{q:05x}",
                "normal_hex": f"{q >> 1:04x}",
                "offset": (q & 1) ^ 1,
                "gram_rank": rank,
            })

    edge_file = out / "independent-incidence-edges.csv"
    with edge_file.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["output_mask_hex","parameter_hex","normal_hex","offset","gram_rank"])
        writer.writeheader(); writer.writerows(edges)
    edge_hash = hashlib.sha256(edge_file.read_bytes()).hexdigest()
    if edge_hash != EDGE_SHA:
        raise AssertionError((EDGE_SHA, edge_hash))

    distinct = {radical for radical in radicals.values()}
    duplicates = sorted(
        (sorted(masks), radical)
        for radical in distinct
        if len(masks := [v for v, r in radicals.items() if r == radical]) > 1
    )
    multi = {q: masks for q, masks in point_masks.items() if len(masks) > 1}
    report = {
        "schema_version": "n.human_llm_mathematics.abf001_independent_bitset.v1",
        "result": "PASS",
        "truth_table_sha256": TRUTH_SHA,
        "full_coefficient_hex": f"{full:02x}",
        "signature_rank": signature_rank,
        "exceptional_hyperplanes": len(exceptional),
        "rank_histogram": {str(k): histogram[k] for k in sorted(histogram)},
        "singular_mask_indexed_radicals": len(radicals),
        "distinct_nonzero_radical_subspaces": len(distinct),
        "radical_incidence_edges": len(edges),
        "covered_parameter_points": len(point_masks),
        "multi_covered_points": {f"{q:05x}": [f"{v:02x}" for v in masks] for q, masks in multi.items()},
        "duplicate_radical_mask_sets": [
            {"masks_hex": [f"{v:02x}" for v in masks], "radical_hex": [f"{q:05x}" for q in sorted(radical)]}
            for masks, radical in duplicates
        ],
        "edge_sha256": edge_hash,
    }
    encoded = json.dumps(report, sort_keys=True, separators=(",", ":")).encode()
    report["evidence_sha256"] = hashlib.sha256(encoded).hexdigest()
    (out / "abf001-independent-bitset.json").write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    report = analyze(args.output_directory)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
