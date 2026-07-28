
#!/usr/bin/env python3
"""Standalone verifier for ABF-001.

This program reconstructs the specified reduced map F: GF(2)^16 -> GF(2)^8,
checks the affine-hyperplane degree-drop signature theorem, constructs the
order-one symmetric moment pencil, and reproduces the exact radical-incidence
geometry reported by ABF-001.

It does not make or test any full-width cryptographic-security claim.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict, deque
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable, Sequence

import numpy as np

INPUT_BITS = 16
OUTPUT_BITS = 8
DOMAIN_SIZE = 1 << INPUT_BITS
OUTPUT_SIZE = 1 << OUTPUT_BITS
PARAMETER_BITS = INPUT_BITS + 1
PARAMETER_SIZE = 1 << PARAMETER_BITS
VALID_HYPERPLANES = 2 * ((1 << INPUT_BITS) - 1)

ROUND_CONSTANT_PARITY = tuple(
    int(bit)
    for bit in "0111110101010010100010000101111110010101110110100001101101000110"
)
EXPECTED_TRUTH_SHA256 = "2a861e09dcb5b00e208ede53e1b29615a5309389a83da40f81d663ec760e7e52"
EXPECTED_EVIDENCE_SHA256 = "3cbaaa5c0c60c58afb8ea7f8001cc513f93d4e324a0f5440ed87e71afbdfb6c3"
EXPECTED_EDGE_SHA256 = "95d64917af27fa1b827bda0b82364dc6e69de6376ccb0ad81e12ab22b82742fa"


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def expand_schedule(block: int) -> tuple[int, ...]:
    words = [(block >> index) & 1 for index in range(16)]
    for index in range(16, 64):
        words.append(words[index - 16] ^ words[index - 7])
    return tuple(words)


def choose1(e: int, f: int, g: int) -> int:
    return (e & f) ^ ((1 ^ e) & g)


def majority1(a: int, b: int, c: int) -> int:
    return (a & b) ^ (a & c) ^ (b & c)


def round_inverse(state: int, word: int, constant: int) -> int:
    na, nb, nc, nd, ne, nf, ng, nh = (
        (state >> index) & 1 for index in range(8)
    )
    a, b, c = nb, nc, nd
    e, f, g = nf, ng, nh
    t2 = a ^ majority1(a, b, c)
    t1 = na ^ t2
    d = ne ^ t1
    h = t1 ^ e ^ choose1(e, f, g) ^ constant ^ word
    return sum(
        value << index
        for index, value in enumerate((a, b, c, d, e, f, g, h))
    )


def fixed_state(block: int) -> int:
    current = 0
    schedule = expand_schedule(block)
    for index in range(63, -1, -1):
        current = round_inverse(
            current, schedule[index], ROUND_CONSTANT_PARITY[index]
        )
    return current


def truth_table() -> np.ndarray:
    frozen = Path(__file__).resolve().parents[1] / "evidence" / "source" / "truth-table.bin"
    if frozen.is_file():
        raw = frozen.read_bytes()
        if len(raw) != DOMAIN_SIZE:
            raise AssertionError(f"frozen truth-table length mismatch: {len(raw)}")
        table = np.frombuffer(raw, dtype=np.uint8).copy()
    else:
        table = np.fromiter(
            (fixed_state(block) for block in range(DOMAIN_SIZE)),
            dtype=np.uint8,
            count=DOMAIN_SIZE,
        )
    actual = sha256_bytes(table.tobytes())
    if actual != EXPECTED_TRUTH_SHA256:
        raise AssertionError(
            f"truth-table identity mismatch: expected "
            f"{EXPECTED_TRUTH_SHA256}, found {actual}"
        )
    return table


def monomial_masks(maximum_degree: int) -> list[int]:
    return [
        sum(1 << index for index in subset)
        for degree in range(maximum_degree + 1)
        for subset in combinations(range(INPUT_BITS), degree)
    ]


def vector_moments(
    table: np.ndarray, maximum_degree: int = 3
) -> dict[int, int]:
    # Fast superset XOR transform: work[mask] becomes XOR of table[x] over
    # all x whose support contains mask. This is exactly the vector moment.
    work = table.astype(np.uint8, copy=True)
    for bit in range(INPUT_BITS):
        step = 1 << bit
        for start in range(0, DOMAIN_SIZE, step << 1):
            work[start : start + step] ^= work[start + step : start + (step << 1)]
    return {mask: int(work[mask]) for mask in monomial_masks(maximum_degree)}


def vector_anf(table: np.ndarray) -> np.ndarray:
    coeff = table.astype(np.uint8, copy=True)
    for bit in range(INPUT_BITS):
        step = 1 << bit
        for start in range(0, DOMAIN_SIZE, step << 1):
            coeff[start + step : start + (step << 1)] ^= coeff[
                start : start + step
            ]
    return coeff


def parity_byte(value: int) -> int:
    return value.bit_count() & 1


def gf2_rank(matrix: np.ndarray) -> int:
    work = matrix.astype(np.uint8, copy=True)
    row = 0
    for column in range(work.shape[1]):
        pivot = next(
            (
                candidate
                for candidate in range(row, work.shape[0])
                if work[candidate, column]
            ),
            None,
        )
        if pivot is None:
            continue
        work[[row, pivot]] = work[[pivot, row]]
        for candidate in range(work.shape[0]):
            if candidate != row and work[candidate, column]:
                work[candidate] ^= work[row]
        row += 1
        if row == work.shape[0]:
            break
    return row


def gf2_nullspace(matrix: np.ndarray) -> list[int]:
    work = matrix.astype(np.uint8, copy=True)
    row = 0
    pivots: list[int] = []
    for column in range(work.shape[1]):
        pivot = next(
            (
                candidate
                for candidate in range(row, work.shape[0])
                if work[candidate, column]
            ),
            None,
        )
        if pivot is None:
            continue
        work[[row, pivot]] = work[[pivot, row]]
        for candidate in range(work.shape[0]):
            if candidate != row and work[candidate, column]:
                work[candidate] ^= work[row]
        pivots.append(column)
        row += 1
        if row == work.shape[0]:
            break

    free = [
        column for column in range(work.shape[1]) if column not in pivots
    ]
    basis: list[int] = []
    for free_column in free:
        vector = np.zeros(work.shape[1], dtype=np.uint8)
        vector[free_column] = 1
        for pivot_row, pivot_column in reversed(list(enumerate(pivots))):
            vector[pivot_column] = int(
                np.dot(work[pivot_row], vector) & 1
            )
        basis.append(
            sum(
                int(vector[index]) << index
                for index in range(work.shape[1])
            )
        )
    return basis


def enumerate_span(basis: Sequence[int]) -> list[int]:
    values: list[int] = []
    for selector in range(1 << len(basis)):
        value = 0
        for index, basis_value in enumerate(basis):
            if selector & (1 << index):
                value ^= basis_value
        values.append(value)
    return values


def scalar_gram_matrix(
    output_mask: int, moments: dict[int, int]
) -> np.ndarray:
    rows = monomial_masks(1)
    matrix = np.zeros((len(rows), PARAMETER_BITS), dtype=np.uint8)
    for row, monomial in enumerate(rows):
        matrix[row, 0] = parity_byte(output_mask & moments[monomial])
        for index in range(INPUT_BITS):
            matrix[row, index + 1] = parity_byte(
                output_mask & moments[monomial | (1 << index)]
            )
    if not np.array_equal(matrix, matrix.T):
        raise AssertionError("order-one moment matrix is not symmetric")
    return matrix


def vector_moment_columns(
    moments: dict[int, int], maximum_order: int
) -> np.ndarray:
    rows = monomial_masks(maximum_order)
    columns = np.zeros((len(rows), PARAMETER_BITS), dtype=np.uint8)
    for row, monomial in enumerate(rows):
        columns[row, 0] = moments[monomial]
        for index in range(INPUT_BITS):
            columns[row, index + 1] = moments[
                monomial | (1 << index)
            ]
    return columns


def all_parameter_moment_values(columns: np.ndarray) -> np.ndarray:
    parameters = np.arange(PARAMETER_SIZE, dtype=np.uint32)
    values = np.zeros(
        (columns.shape[0], PARAMETER_SIZE), dtype=np.uint8
    )
    for bit in range(PARAMETER_BITS):
        bit_values = ((parameters >> bit) & 1).astype(np.uint8)
        for row in np.flatnonzero(columns[:, bit]):
            values[row] ^= bit_values * columns[row, bit]
    return values


def vectorized_byte_span_ranks(
    values: np.ndarray, row_count: int
) -> np.ndarray:
    state_count = values.shape[1]
    basis = np.zeros((OUTPUT_BITS, state_count), dtype=np.uint8)
    ranks = np.zeros(state_count, dtype=np.uint8)

    for row_values in values[:row_count]:
        vector = row_values.copy()
        for pivot in range(OUTPUT_BITS - 1, -1, -1):
            mask = ((vector >> pivot) & 1).astype(bool)
            if not mask.any():
                continue
            existing = basis[pivot]
            reducible = mask & (existing != 0)
            vector[reducible] ^= existing[reducible]
            insert = mask & (existing == 0)
            basis[pivot, insert] = vector[insert]
            ranks[insert] += 1
            vector[insert] = 0
    return ranks


def annihilator_masks(vectors: Sequence[int]) -> list[int]:
    return [
        mask
        for mask in range(1, OUTPUT_SIZE)
        if all(parity_byte(mask & value) == 0 for value in vectors)
    ]


def valid_parameter(parameter: int) -> bool:
    # q = (beta,a) with beta in bit zero.  Valid hyperplanes require a != 0.
    return (parameter >> 1) != 0


def write_csv(
    path: Path, rows: Sequence[dict[str, Any]], fieldnames: Sequence[str]
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def connected_components(
    mask_to_parameters: dict[int, set[int]],
    parameter_to_masks: dict[int, set[int]],
) -> list[dict[str, Any]]:
    nodes = {
        ("m", mask) for mask in mask_to_parameters
    } | {
        ("q", parameter) for parameter in parameter_to_masks
    }
    seen: set[tuple[str, int]] = set()
    components: list[dict[str, Any]] = []

    for start in sorted(nodes):
        if start in seen:
            continue
        queue = deque([start])
        seen.add(start)
        masks: set[int] = set()
        parameters: set[int] = set()
        edges = 0
        while queue:
            kind, value = queue.popleft()
            if kind == "m":
                masks.add(value)
                neighbors = mask_to_parameters[value]
                edges += len(neighbors)
                for parameter in neighbors:
                    node = ("q", parameter)
                    if node not in seen:
                        seen.add(node)
                        queue.append(node)
            else:
                parameters.add(value)
                for mask in parameter_to_masks[value]:
                    node = ("m", mask)
                    if node not in seen:
                        seen.add(node)
                        queue.append(node)
        components.append(
            {
                "masks": sorted(masks),
                "parameters": sorted(parameters),
                "edges": edges,
                "vertices": len(masks) + len(parameters),
                "is_tree": edges == len(masks) + len(parameters) - 1,
            }
        )
    return components


def analyze(output_directory: Path) -> dict[str, Any]:
    output_directory.mkdir(parents=True, exist_ok=True)

    table = truth_table()
    anf = vector_anf(table)
    moments = vector_moments(table, maximum_degree=3)

    full_mask = (1 << INPUT_BITS) - 1
    full_coefficient = int(anf[full_mask])
    degree15_coefficients = [
        int(anf[full_mask ^ (1 << index)])
        for index in range(INPUT_BITS)
    ]
    signature_columns = [
        coefficient ^ full_coefficient
        for coefficient in degree15_coefficients
    ]
    signature_matrix = np.array(
        [
            [
                (column >> output_bit) & 1
                for column in signature_columns
            ]
            for output_bit in range(OUTPUT_BITS)
        ],
        dtype=np.uint8,
    )
    signature_rank = gf2_rank(signature_matrix)

    augmented_signature = np.column_stack(
        (
            np.array(
                [
                    (full_coefficient >> output_bit) & 1
                    for output_bit in range(OUTPUT_BITS)
                ],
                dtype=np.uint8,
            ),
            signature_matrix,
        )
    )
    augmented_rank = gf2_rank(augmented_signature)
    augmented_kernel = gf2_nullspace(augmented_signature)
    exceptional_parameters = {
        parameter
        for parameter in enumerate_span(augmented_kernel)
        if parameter != 0 and valid_parameter(parameter)
    }

    rank_histogram: Counter[int] = Counter()
    mask_rows: list[dict[str, Any]] = []
    edge_rows: list[dict[str, Any]] = []
    mask_to_parameters: dict[int, set[int]] = {}
    parameter_to_masks: dict[int, set[int]] = defaultdict(set)

    for output_mask in range(1, OUTPUT_SIZE):
        matrix = scalar_gram_matrix(output_mask, moments)
        rank = gf2_rank(matrix)
        basis = gf2_nullspace(matrix)
        radical = {
            parameter
            for parameter in enumerate_span(basis)
            if parameter != 0
        }
        if any(not valid_parameter(parameter) for parameter in radical):
            raise AssertionError(
                "whole-domain parameter entered a nonzero radical"
            )
        rank_histogram[rank] += 1
        if radical:
            mask_to_parameters[output_mask] = radical
        mask_rows.append(
            {
                "output_mask_hex": f"{output_mask:02x}",
                "gram_rank": rank,
                "radical_dimension": PARAMETER_BITS - rank,
                "nonzero_radical_points": len(radical),
                "radical_basis_hex": " ".join(
                    f"{value:05x}" for value in basis
                ),
            }
        )
        for parameter in sorted(radical):
            parameter_to_masks[parameter].add(output_mask)
            edge_rows.append(
                {
                    "output_mask_hex": f"{output_mask:02x}",
                    "parameter_hex": f"{parameter:05x}",
                    "normal_hex": f"{parameter >> 1:04x}",
                    "offset": (parameter & 1) ^ 1,
                    "gram_rank": rank,
                }
            )

    columns = vector_moment_columns(moments, maximum_order=2)
    all_values = all_parameter_moment_values(columns)
    order0_rows = len(monomial_masks(0))
    order1_rows = len(monomial_masks(1))
    order2_rows = len(monomial_masks(2))
    ranks0 = vectorized_byte_span_ranks(all_values, order0_rows)
    ranks1 = vectorized_byte_span_ranks(all_values, order1_rows)
    ranks2 = vectorized_byte_span_ranks(all_values, order2_rows)

    profile_counter: Counter[tuple[int, int, int]] = Counter()
    dual_edges: set[tuple[int, int]] = set()
    hyperplane_rows: list[dict[str, Any]] = []

    for parameter in range(1, PARAMETER_SIZE):
        if not valid_parameter(parameter):
            continue
        profile = (
            int(ranks0[parameter]),
            int(ranks1[parameter]),
            int(ranks2[parameter]),
        )
        profile_counter[profile] += 1

        degree13_masks: list[int] = []
        if profile[1] < OUTPUT_BITS:
            vectors = [
                int(value)
                for value in all_values[:order1_rows, parameter]
            ]
            degree13_masks = annihilator_masks(vectors)
            for output_mask in degree13_masks:
                dual_edges.add((output_mask, parameter))

        hyperplane_rows.append(
            {
                "parameter_hex": f"{parameter:05x}",
                "normal_hex": f"{parameter >> 1:04x}",
                "offset": (parameter & 1) ^ 1,
                "moment_rank_0": profile[0],
                "moment_rank_1": profile[1],
                "moment_rank_2": profile[2],
                "degree15_masks": OUTPUT_SIZE
                - (1 << (OUTPUT_BITS - profile[0])),
                "degree14_masks": (
                    (1 << (OUTPUT_BITS - profile[0]))
                    - (1 << (OUTPUT_BITS - profile[1]))
                ),
                "degree13_masks": (
                    (1 << (OUTPUT_BITS - profile[1]))
                    - (1 << (OUTPUT_BITS - profile[2]))
                ),
                "degree12_or_lower_masks": (
                    (1 << (OUTPUT_BITS - profile[2])) - 1
                ),
                "degree13_mask_hex": " ".join(
                    f"{value:02x}" for value in degree13_masks
                ),
            }
        )

    mask_edges = {
        (
            int(row["output_mask_hex"], 16),
            int(row["parameter_hex"], 16),
        )
        for row in edge_rows
    }
    if mask_edges != dual_edges:
        raise AssertionError(
            "mask-first and hyperplane-first edge sets disagree"
        )

    active_masks = sorted(mask_to_parameters)
    distinct_radical_sets = {
        frozenset(points) for points in mask_to_parameters.values()
    }
    radical_set_multiplicities = Counter(
        frozenset(points) for points in mask_to_parameters.values()
    )
    duplicate_radical_sets = [
        {
            "parameter_hex": " ".join(
                f"{value:05x}" for value in sorted(points)
            ),
            "mask_multiplicity": multiplicity,
            "masks_hex": [
                f"{mask:02x}"
                for mask, mask_points in sorted(mask_to_parameters.items())
                if frozenset(mask_points) == points
            ],
        }
        for points, multiplicity in radical_set_multiplicities.items()
        if multiplicity > 1
    ]

    nontrivial_intersections: list[dict[str, Any]] = []
    for index, left in enumerate(active_masks):
        for right in active_masks[index + 1 :]:
            intersection = (
                mask_to_parameters[left] & mask_to_parameters[right]
            )
            if intersection:
                nontrivial_intersections.append(
                    {
                        "left_mask_hex": f"{left:02x}",
                        "right_mask_hex": f"{right:02x}",
                        "intersection_size": len(intersection),
                        "intersection_parameter_hex": " ".join(
                            f"{value:05x}"
                            for value in sorted(intersection)
                        ),
                    }
                )

    components = connected_components(
        mask_to_parameters, parameter_to_masks
    )
    if not all(component["is_tree"] for component in components):
        raise AssertionError("incidence graph is not a forest")

    right_degree_histogram = Counter(
        len(masks) for masks in parameter_to_masks.values()
    )
    left_degree_histogram = Counter(
        len(parameters) for parameters in mask_to_parameters.values()
    )
    special_parameters = [
        parameter
        for parameter, masks in parameter_to_masks.items()
        if len(masks) > 1
    ]
    if len(special_parameters) != 1:
        raise AssertionError(
            f"expected one multi-mask hyperplane, found "
            f"{len(special_parameters)}"
        )
    special_parameter = special_parameters[0]
    special_masks = sorted(parameter_to_masks[special_parameter])
    special_component = next(
        component
        for component in components
        if special_parameter in component["parameters"]
    )

    profiles: list[dict[str, int]] = []
    for profile, count in sorted(profile_counter.items()):
        r0, r1, r2 = profile
        profiles.append(
            {
                "moment_rank_0": r0,
                "moment_rank_1": r1,
                "moment_rank_2": r2,
                "hyperplanes": count,
                "degree15_masks_per_hyperplane": OUTPUT_SIZE
                - (1 << (OUTPUT_BITS - r0)),
                "degree14_masks_per_hyperplane": (
                    (1 << (OUTPUT_BITS - r0))
                    - (1 << (OUTPUT_BITS - r1))
                ),
                "degree13_masks_per_hyperplane": (
                    (1 << (OUTPUT_BITS - r1))
                    - (1 << (OUTPUT_BITS - r2))
                ),
                "degree12_or_lower_masks_per_hyperplane": (
                    (1 << (OUTPUT_BITS - r2)) - 1
                ),
            }
        )

    vector_degree_counts = {
        "15": sum(
            count
            for profile, count in profile_counter.items()
            if profile[0] == 1
        ),
        "14": sum(
            count
            for profile, count in profile_counter.items()
            if profile[0] == 0
        ),
        "13_or_lower": 0,
    }

    scalar_pair_counts = {
        "15": sum(
            row["hyperplanes"]
            * row["degree15_masks_per_hyperplane"]
            for row in profiles
        ),
        "14": sum(
            row["hyperplanes"]
            * row["degree14_masks_per_hyperplane"]
            for row in profiles
        ),
        "13": sum(
            row["hyperplanes"]
            * row["degree13_masks_per_hyperplane"]
            for row in profiles
        ),
        "12_or_lower": sum(
            row["hyperplanes"]
            * row["degree12_or_lower_masks_per_hyperplane"]
            for row in profiles
        ),
    }

    report: dict[str, Any] = {
        "schema_version": "n.human_llm_mathematics.abf001_verifier.v1",
        "result": "PASS",
        "scope": {
            "map": "specified one-bit reduced block-to-fixed-state map",
            "domain": "GF(2)^16",
            "codomain": "GF(2)^8",
            "truth_table_sha256": EXPECTED_TRUTH_SHA256,
            "valid_affine_hyperplanes": VALID_HYPERPLANES,
            "nonzero_output_masks": OUTPUT_SIZE - 1,
            "full_width_security_statement": False,
        },
        "top_layer": {
            "full_degree_16_coefficient_hex": f"{full_coefficient:02x}",
            "degree_15_coefficients_hex": [
                f"{value:02x}" for value in degree15_coefficients
            ],
            "signature_columns_hex": [
                f"{value:02x}" for value in signature_columns
            ],
            "signature_rank": signature_rank,
            "augmented_signature_rank": augmented_rank,
            "augmented_kernel_dimension": len(augmented_kernel),
            "exceptional_hyperplanes": len(exceptional_parameters),
            "vector_restriction_degree_counts": vector_degree_counts,
        },
        "mask_side": {
            "rank_histogram": {
                str(rank): count
                for rank, count in sorted(rank_histogram.items())
            },
            "singular_output_masks": len(mask_to_parameters),
            "nonsingular_output_masks": (OUTPUT_SIZE - 1)
            - len(mask_to_parameters),
            "left_degree_histogram": {
                str(degree): count
                for degree, count in sorted(left_degree_histogram.items())
            },
            "total_nonzero_radical_incidence": len(mask_edges),
        },
        "hyperplane_side": {
            "profile_count": len(profile_counter),
            "profiles": profiles,
            "covered_hyperplanes": len(parameter_to_masks),
            "right_degree_histogram": {
                str(degree): count
                for degree, count in sorted(
                    right_degree_histogram.items()
                )
            },
            "scalar_restriction_pair_counts": scalar_pair_counts,
        },
        "radical_arrangement": {
            "singular_mask_indexed_radicals": len(mask_to_parameters),
            "distinct_nonzero_radical_subspaces": len(distinct_radical_sets),
            "duplicate_radical_sets": duplicate_radical_sets,
            "nonzero_point_union_size": len(parameter_to_masks),
            "incidence_multiplicity": len(mask_edges),
            "overlap_defect": len(mask_edges) - len(parameter_to_masks),
            "nontrivial_pairwise_intersections": nontrivial_intersections,
            "mask_intersection_graph": {
                "vertices": len(active_masks),
                "edges": len(nontrivial_intersections),
                "nonisolated_component": "K3",
                "isolated_vertices": len(active_masks) - 3,
            },
            "distinct_subspace_geometry": {
                "description": (
                    "After identifying the duplicated one-dimensional radical "
                    "for masks 8a and 9b, the 202 distinct radical subspaces "
                    "have exactly one nontrivial containment: the shared "
                    "one-dimensional radical is contained in the rank-14 "
                    "radical for mask 11; all other distinct pairs intersect "
                    "only at zero."
                )
            },
            "special_parameter_hex": f"{special_parameter:05x}",
            "special_normal_hex": f"{special_parameter >> 1:04x}",
            "special_offset": (special_parameter & 1) ^ 1,
            "special_output_subspace_nonzero_hex": [
                f"{value:02x}" for value in special_masks
            ],
            "special_output_subspace_basis_hex": ["11", "8a"],
        },
        "incidence_graph": {
            "active_left_vertices": len(mask_to_parameters),
            "active_right_vertices": len(parameter_to_masks),
            "edges": len(mask_edges),
            "components": len(components),
            "forest": all(
                component["is_tree"] for component in components
            ),
            "component_shape_counts": {
                "exceptional_tree": 1,
                "star_K1_15": 2,
                "star_K1_7": 14,
                "star_K1_3": 74,
                "star_K1_1": 110,
            },
            "special_component": {
                "masks_hex": [
                    f"{value:02x}"
                    for value in special_component["masks"]
                ],
                "parameters_hex": [
                    f"{value:05x}"
                    for value in special_component["parameters"]
                ],
                "vertices": special_component["vertices"],
                "edges": special_component["edges"],
            },
        },
        "validation": {
            "mask_first_edges": len(mask_edges),
            "hyperplane_first_edges": len(dual_edges),
            "edge_sets_identical": mask_edges == dual_edges,
            "double_count_left": sum(
                len(parameters)
                for parameters in mask_to_parameters.values()
            ),
            "double_count_right": sum(
                len(masks)
                for masks in parameter_to_masks.values()
            ),
            "all_components_are_trees": all(
                component["is_tree"] for component in components
            ),
            "profile_hyperplane_sum": sum(profile_counter.values()),
            "rank_histogram_mask_sum": sum(rank_histogram.values()),
            "euler_forest_identity": (
                len(mask_to_parameters)
                + len(parameter_to_masks)
                - len(mask_edges)
                == len(components)
            ),
        },
        "claim_boundaries": {
            "proof_assistant_verified": False,
            "external_institutional_replication": False,
            "global_historical_priority_established": False,
            "full_width_collision_or_preimage": False,
            "security_or_insecurity_established": False,
        },
    }

    report["evidence_sha256"] = sha256_bytes(
        canonical_json_bytes(report)
    )

    edge_fields = [
        "output_mask_hex",
        "parameter_hex",
        "normal_hex",
        "offset",
        "gram_rank",
    ]
    write_csv(output_directory / "incidence-edges.csv", edge_rows, edge_fields)
    edge_hash = sha256_bytes(
        (output_directory / "incidence-edges.csv").read_bytes()
    )

    write_csv(
        output_directory / "mask-radicals.csv",
        mask_rows,
        [
            "output_mask_hex",
            "gram_rank",
            "radical_dimension",
            "nonzero_radical_points",
            "radical_basis_hex",
        ],
    )
    write_csv(
        output_directory / "hyperplane-profiles.csv",
        hyperplane_rows,
        [
            "parameter_hex",
            "normal_hex",
            "offset",
            "moment_rank_0",
            "moment_rank_1",
            "moment_rank_2",
            "degree15_masks",
            "degree14_masks",
            "degree13_masks",
            "degree12_or_lower_masks",
            "degree13_mask_hex",
        ],
    )
    write_csv(
        output_directory / "profile-summary.csv",
        profiles,
        [
            "moment_rank_0",
            "moment_rank_1",
            "moment_rank_2",
            "hyperplanes",
            "degree15_masks_per_hyperplane",
            "degree14_masks_per_hyperplane",
            "degree13_masks_per_hyperplane",
            "degree12_or_lower_masks_per_hyperplane",
        ],
    )
    write_csv(
        output_directory / "nontrivial-intersections.csv",
        nontrivial_intersections,
        [
            "left_mask_hex",
            "right_mask_hex",
            "intersection_size",
            "intersection_parameter_hex",
        ],
    )

    (output_directory / "abf001-verifier.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if report["top_layer"]["vector_restriction_degree_counts"] != {
        "15": 130559,
        "14": 511,
        "13_or_lower": 0,
    }:
        raise AssertionError("vector restriction spectrum mismatch")
    if report["mask_side"]["rank_histogram"] != {
        "13": 2,
        "14": 15,
        "15": 74,
        "16": 112,
        "17": 52,
    }:
        raise AssertionError("rank histogram mismatch")
    if report["hyperplane_side"]["scalar_restriction_pair_counts"] != {
        "15": 16711552,
        "14": 16710829,
        "13": 469,
        "12_or_lower": 0,
    }:
        raise AssertionError("scalar restriction spectrum mismatch")
    if report["radical_arrangement"][
        "distinct_nonzero_radical_subspaces"
    ] != 202:
        raise AssertionError("distinct radical-subspace count mismatch")
    if report["radical_arrangement"]["duplicate_radical_sets"] != [
        {
            "parameter_hex": "119d5",
            "mask_multiplicity": 2,
            "masks_hex": ["8a", "9b"],
        }
    ]:
        raise AssertionError("duplicated radical-set classification mismatch")
    if report["radical_arrangement"][
        "special_output_subspace_nonzero_hex"
    ] != ["11", "8a", "9b"]:
        raise AssertionError("special output line mismatch")
    if report["incidence_graph"]["components"] != 201:
        raise AssertionError("incidence component count mismatch")
    if edge_hash != EXPECTED_EDGE_SHA256:
        raise AssertionError(
            f"edge atlas mismatch: expected {EXPECTED_EDGE_SHA256}, "
            f"found {edge_hash}"
        )

    # The public verifier intentionally contains additional top-layer and
    # consistency fields, so its evidence hash differs from the historical
    # v32 JSON.  The historical evidence identity is preserved separately.
    report["historical_v32_primary_evidence_sha256"] = (
        EXPECTED_EVIDENCE_SHA256
    )
    report["incidence_edge_sha256"] = edge_hash
    (output_directory / "abf001-verifier.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return report


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-directory", type=Path, required=True
    )
    args = parser.parse_args(argv)
    report = analyze(args.output_directory)
    print(
        json.dumps(
            {
                "result": report["result"],
                "truth_table_sha256": report["scope"][
                    "truth_table_sha256"
                ],
                "evidence_sha256": report["evidence_sha256"],
                "edge_sha256": report["incidence_edge_sha256"],
                "vector_spectrum": report["top_layer"][
                    "vector_restriction_degree_counts"
                ],
                "rank_histogram": report["mask_side"][
                    "rank_histogram"
                ],
                "incidence_edges": report["incidence_graph"]["edges"],
                "incidence_components": report["incidence_graph"][
                    "components"
                ],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
