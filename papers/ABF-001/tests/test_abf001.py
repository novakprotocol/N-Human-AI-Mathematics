from __future__ import annotations

import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from abf001_verifier import analyze


class ABF001VerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        output_root = os.environ.get("ABF001_TEST_OUTPUT_DIR")
        if output_root:
            cls.temp = None
            cls.output = Path(output_root)
            if cls.output.exists():
                shutil.rmtree(cls.output)
            cls.output.mkdir(parents=True, exist_ok=True)
        else:
            cls.temp = tempfile.TemporaryDirectory()
            cls.output = Path(cls.temp.name)
        cls.report = analyze(cls.output)

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.temp is not None:
            cls.temp.cleanup()

    def test_truth_table_and_top_layer(self) -> None:
        self.assertEqual(
            self.report["scope"]["truth_table_sha256"],
            "2a861e09dcb5b00e208ede53e1b29615a5309389a83da40f81d663ec760e7e52",
        )
        self.assertEqual(
            self.report["top_layer"]["vector_restriction_degree_counts"],
            {"15": 130559, "14": 511, "13_or_lower": 0},
        )
        self.assertEqual(self.report["top_layer"]["signature_rank"], 8)
        self.assertEqual(self.report["top_layer"]["augmented_kernel_dimension"], 9)

    def test_rank_histogram(self) -> None:
        self.assertEqual(
            self.report["mask_side"]["rank_histogram"],
            {"13": 2, "14": 15, "15": 74, "16": 112, "17": 52},
        )
        self.assertEqual(self.report["mask_side"]["singular_output_masks"], 203)
        self.assertEqual(self.report["mask_side"]["nonsingular_output_masks"], 52)

    def test_hyperplane_profiles(self) -> None:
        observed = {
            (row["moment_rank_0"], row["moment_rank_1"], row["moment_rank_2"]): row["hyperplanes"]
            for row in self.report["hyperplane_side"]["profiles"]
        }
        self.assertEqual(
            observed,
            {
                (0, 7, 8): 3,
                (0, 8, 8): 508,
                (1, 6, 8): 1,
                (1, 7, 8): 463,
                (1, 8, 8): 130095,
            },
        )
        self.assertEqual(
            self.report["hyperplane_side"]["scalar_restriction_pair_counts"],
            {"15": 16711552, "14": 16710829, "13": 469, "12_or_lower": 0},
        )

    def test_bidual_edge_identity(self) -> None:
        validation = self.report["validation"]
        self.assertTrue(validation["edge_sets_identical"])
        self.assertEqual(validation["mask_first_edges"], 469)
        self.assertEqual(validation["hyperplane_first_edges"], 469)
        self.assertEqual(validation["double_count_left"], 469)
        self.assertEqual(validation["double_count_right"], 469)
        self.assertEqual(
            self.report["incidence_edge_sha256"],
            "95d64917af27fa1b827bda0b82364dc6e69de6376ccb0ad81e12ab22b82742fa",
        )

    def test_radical_arrangement(self) -> None:
        arrangement = self.report["radical_arrangement"]
        self.assertEqual(arrangement["singular_mask_indexed_radicals"], 203)
        self.assertEqual(arrangement["distinct_nonzero_radical_subspaces"], 202)
        self.assertEqual(
            arrangement["duplicate_radical_sets"],
            [{"parameter_hex": "119d5", "mask_multiplicity": 2, "masks_hex": ["8a", "9b"]}],
        )
        self.assertEqual(arrangement["nonzero_point_union_size"], 467)
        self.assertEqual(arrangement["incidence_multiplicity"], 469)
        self.assertEqual(arrangement["overlap_defect"], 2)
        self.assertEqual(arrangement["special_parameter_hex"], "119d5")
        self.assertEqual(arrangement["special_normal_hex"], "8cea")
        self.assertEqual(arrangement["special_offset"], 0)
        self.assertEqual(arrangement["special_output_subspace_nonzero_hex"], ["11", "8a", "9b"])
        self.assertEqual(len(arrangement["nontrivial_pairwise_intersections"]), 3)
        self.assertEqual(
            arrangement["mask_intersection_graph"],
            {"vertices": 203, "edges": 3, "nonisolated_component": "K3", "isolated_vertices": 200},
        )

    def test_incidence_forest(self) -> None:
        graph = self.report["incidence_graph"]
        self.assertTrue(graph["forest"])
        self.assertTrue(self.report["validation"]["euler_forest_identity"])
        self.assertEqual(graph["active_left_vertices"], 203)
        self.assertEqual(graph["active_right_vertices"], 467)
        self.assertEqual(graph["edges"], 469)
        self.assertEqual(graph["components"], 201)
        self.assertEqual(
            graph["component_shape_counts"],
            {"exceptional_tree": 1, "star_K1_15": 2, "star_K1_7": 14, "star_K1_3": 74, "star_K1_1": 110},
        )
        self.assertEqual(graph["special_component"]["masks_hex"], ["11", "8a", "9b"])
        self.assertEqual(graph["special_component"]["vertices"], 10)
        self.assertEqual(graph["special_component"]["edges"], 9)


if __name__ == "__main__":
    unittest.main()
