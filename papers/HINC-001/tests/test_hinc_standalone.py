from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from standalone_common_core_verifier import (  # noqa: E402
    CorePoint,
    EvenPoint,
    OddPoint,
    TruncF2,
    build_certificate,
    core_points,
    even_points,
    odd_points,
    one,
)


class CommonCoreTests(unittest.TestCase):
    def test_field_point_counts(self) -> None:
        self.assertEqual(len(core_points(1)), 3)
        self.assertEqual(len(even_points(1)), 3)
        self.assertEqual(len(odd_points(1)), 4)

    def test_even_identity(self) -> None:
        for n in range(1, 5):
            identity = EvenPoint(one(n), one(n), TruncF2(0, n))
            for p in even_points(n):
                self.assertEqual(identity * p, p)
                self.assertEqual(p * identity, p)

    def test_odd_identity_and_local_identity(self) -> None:
        for n in range(1, 5):
            identity = OddPoint(1, u=one(n))
            local = OddPoint(0, core=CorePoint(one(n), one(n)))
            for p in odd_points(n):
                self.assertEqual(identity * p, p)
                self.assertEqual(p * identity, p)
                if p.component == 0:
                    self.assertEqual(local * p, p)
                    self.assertEqual(p * local, p)

    def test_certificate(self) -> None:
        cert = build_certificate(4)
        self.assertEqual(cert["result"], "PASS")
        self.assertEqual(cert["symbolic_audit"]["failure_count"], 0)
        self.assertTrue(all(item["failures"] == 0 for item in cert["finite_audits"]))

    def test_deterministic_certificate(self) -> None:
        a = json.dumps(build_certificate(4), sort_keys=True)
        b = json.dumps(build_certificate(4), sort_keys=True)
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
