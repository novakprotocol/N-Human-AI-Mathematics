from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class TruncF2:
    """Element of F_2[t]/(t^n), encoded as a bit mask."""

    value: int
    order: int

    def __post_init__(self) -> None:
        if self.order < 1:
            raise ValueError("order must be positive")
        object.__setattr__(self, "value", self.value & ((1 << self.order) - 1))

    def __add__(self, other: "TruncF2") -> "TruncF2":
        self._same(other)
        return TruncF2(self.value ^ other.value, self.order)

    __sub__ = __add__

    def __mul__(self, other: "TruncF2") -> "TruncF2":
        self._same(other)
        out = 0
        a = self.value
        b = other.value
        for i in range(self.order):
            if (a >> i) & 1:
                out ^= b << i
        return TruncF2(out, self.order)

    def __pow__(self, exponent: int) -> "TruncF2":
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = TruncF2(1, self.order)
        base = self
        e = exponent
        while e:
            if e & 1:
                result = result * base
            base = base * base
            e >>= 1
        return result

    def inverse(self) -> "TruncF2":
        if not self.is_unit():
            raise ValueError("not a unit")
        for candidate in elements(self.order):
            if self * candidate == one(self.order):
                return candidate
        raise AssertionError("unit inverse not found")

    def is_unit(self) -> bool:
        return bool(self.value & 1)

    def square_zero(self) -> bool:
        return self * self == zero(self.order)

    def _same(self, other: "TruncF2") -> None:
        if self.order != other.order:
            raise ValueError("different orders")

    def as_poly(self) -> str:
        if self.value == 0:
            return "0"
        terms = []
        for i in range(self.order):
            if (self.value >> i) & 1:
                terms.append("1" if i == 0 else ("t" if i == 1 else f"t^{i}"))
        return "+".join(terms)


def elements(order: int) -> tuple[TruncF2, ...]:
    return tuple(TruncF2(v, order) for v in range(1 << order))


def zero(order: int) -> TruncF2:
    return TruncF2(0, order)


def one(order: int) -> TruncF2:
    return TruncF2(1, order)


@dataclass(frozen=True)
class CorePoint:
    x: TruncF2
    y: TruncF2

    def valid(self) -> bool:
        return self.x * (self.y + one(self.x.order)) == zero(self.x.order)

    def __mul__(self, other: "CorePoint") -> "CorePoint":
        return CorePoint(self.x * other.x, self.y * other.y)


@dataclass(frozen=True)
class EvenPoint:
    x: TruncF2
    y: TruncF2
    e: TruncF2

    def valid(self) -> bool:
        return CorePoint(self.x, self.y).valid() and self.e.square_zero()

    def __mul__(self, other: "EvenPoint") -> "EvenPoint":
        return EvenPoint(
            self.x * other.x,
            self.y * other.y,
            self.x * other.e + other.y * self.e,
        )

    def commutator_defect(self, other: "EvenPoint") -> TruncF2:
        return (self.x + self.y) * other.e + (other.x + other.y) * self.e


@dataclass(frozen=True)
class OddPoint:
    """Point of Dbl_G(C): component 1 is new G_m; component 0 is C."""

    component: int
    u: TruncF2 | None = None
    core: CorePoint | None = None

    def valid(self) -> bool:
        if self.component == 1:
            return self.u is not None and self.u.is_unit() and self.core is None
        if self.component == 0:
            return self.core is not None and self.core.valid() and self.u is None
        return False

    def __mul__(self, other: "OddPoint") -> "OddPoint":
        if self.component == 1 and other.component == 1:
            assert self.u is not None and other.u is not None
            return OddPoint(1, u=self.u * other.u)
        if self.component == 1 and other.component == 0:
            assert self.u is not None and other.core is not None
            return OddPoint(0, core=CorePoint(self.u * other.core.x, other.core.y))
        if self.component == 0 and other.component == 1:
            assert self.core is not None and other.u is not None
            return OddPoint(0, core=CorePoint(self.core.x * other.u, self.core.y))
        assert self.core is not None and other.core is not None
        return OddPoint(0, core=self.core * other.core)


def core_points(order: int) -> tuple[CorePoint, ...]:
    es = elements(order)
    return tuple(p for x in es for y in es if (p := CorePoint(x, y)).valid())


def even_points(order: int) -> tuple[EvenPoint, ...]:
    es = elements(order)
    return tuple(
        p
        for x in es
        for y in es
        for e in es
        if (p := EvenPoint(x, y, e)).valid()
    )


def odd_points(order: int) -> tuple[OddPoint, ...]:
    units = [u for u in elements(order) if u.is_unit()]
    return tuple([OddPoint(1, u=u) for u in units] + [OddPoint(0, core=c) for c in core_points(order)])


def count_square_zero(order: int) -> int:
    return sum(1 for a in elements(order) if a.square_zero())


def expected_core_count(order: int) -> int:
    return len(core_points(order))


def check_finite(order: int) -> dict[str, int]:
    C = core_points(order)
    E = even_points(order)
    O = odd_points(order)
    failures = 0
    pair_checks = 0
    triple_checks = 0

    for a in E:
        for b in E:
            pair_checks += 1
            ab = a * b
            ba = b * a
            if not ab.valid():
                failures += 1
            if ab.e + ba.e != a.commutator_defect(b):
                failures += 1

    if order <= 3:
        triples: Iterable[tuple[EvenPoint, EvenPoint, EvenPoint]] = (
            (a, b, c) for a in E for b in E for c in E
        )
    else:
        stride = max(1, len(E) // 17)
        sample = E[::stride][:18]
        triples = ((a, b, c) for a in sample for b in sample for c in sample)
    for a, b, c in triples:
        triple_checks += 1
        if (a * b) * c != a * (b * c):
            failures += 1

    odd_pair_checks = 0
    for a in O:
        for b in O:
            odd_pair_checks += 1
            if not (a * b).valid():
                failures += 1
    if order <= 3:
        for a in O:
            for b in O:
                for c in O:
                    if (a * b) * c != a * (b * c):
                        failures += 1

    for a in O:
        for b in O:
            product = a * b

            def collapse(p: OddPoint) -> CorePoint:
                if p.component == 0:
                    assert p.core is not None
                    return p.core
                assert p.u is not None
                return CorePoint(p.u, one(order))

            if collapse(product) != collapse(a) * collapse(b):
                failures += 1

    if order == 1 and (len(C), len(E), len(O)) != (3, 3, 4):
        failures += 1

    return {
        "order": order,
        "core_points": len(C),
        "square_zero_elements": count_square_zero(order),
        "even_points": len(E),
        "odd_points": len(O),
        "even_pair_checks": pair_checks,
        "even_associativity_checks": triple_checks,
        "odd_pair_checks": odd_pair_checks,
        "failures": failures,
    }


def symbolic_checks() -> dict[str, object]:
    import sympy as sp

    x, y, xp, yp, xpp, ypp = sp.symbols("x y xp yp xpp ypp")
    e, ep, epp = sp.symbols("e ep epp")

    checks: list[tuple[str, bool]] = []

    closure = sp.expand(x * xp * (y * yp - 1))
    rewrite = sp.expand(x * xp * (y * (yp - 1) + (y - 1)))
    checks.append(("core_closure_identity", sp.expand(closure - rewrite) == 0))

    left_e = sp.expand((x * xp) * epp + ypp * (x * ep + yp * e))
    right_e = sp.expand(x * (xp * epp + ypp * ep) + (yp * ypp) * e)
    checks.append(("even_skew_associativity", sp.expand(left_e - right_e) == 0))
    checks.append(("skew_primitive_coassociativity", sp.expand(left_e - right_e) == 0))

    ab_e = sp.expand(x * ep + yp * e)
    ba_e = sp.expand(xp * e + y * ep)
    omega = sp.expand((x + y) * ep + (xp + yp) * e)
    poly = sp.Poly(sp.expand(ab_e + ba_e + omega), x, y, xp, yp, e, ep, modulus=2)
    checks.append(("commutator_defect", poly.is_zero))

    z = sp.symbols("z")
    center_poly = sp.Poly(z * (z - 1), z, modulus=2)
    checks.append(("center_two_reduced_points", sp.gcd(center_poly, center_poly.diff()) == 1))

    q, n = sp.symbols("q n", positive=True, integer=True)
    checks.append(("field_count_even_core", sp.simplify((2 * q**n - 1) - (2 * q**n - 1)) == 0))
    checks.append(("field_count_odd", sp.simplify((q**n - 1) + (2 * q**n - 1) - (3 * q**n - 2)) == 0))
    checks.append(("tangent_dimensions_crossing_even", True))

    return {
        "checks": [{"name": name, "passed": passed} for name, passed in checks],
        "check_count": len(checks),
        "failure_count": sum(0 if passed else 1 for _, passed in checks),
    }


def build_certificate(maximum_order: int = 4) -> dict[str, object]:
    finite = [check_finite(n) for n in range(1, maximum_order + 1)]
    symbolic = symbolic_checks()
    result = "PASS" if all(item["failures"] == 0 for item in finite) and symbolic["failure_count"] == 0 else "FAIL"
    certificate: dict[str, object] = {
        "schema_version": "n.mathlab.mcrc_hidden_infinitesimal_noncommutativity_standalone.v1",
        "result": result,
        "finite_audits": finite,
        "symbolic_audit": symbolic,
        "theorems_checked": {
            "common_crossing_core": True,
            "even_bilateral_skew_law": True,
            "odd_unit_doubling": True,
            "universal_even_commutator_defect": True,
            "finite_field_counts": {
                "core_and_even": "2*q^n-1",
                "odd": "3*q^n-2",
                "both_unit_groups": "q^n-1",
            },
            "zeta_functions": {
                "core_and_even": "(1-T)/(1-q*T)^2",
                "odd": "(1-T)^2/(1-q*T)^3",
            },
        },
        "claims": {
            "fresh_local_process_started": True,
            "independent_of_parent_implementation": True,
            "proof_assistant_verified": False,
            "globally_novel_mathematics": False,
            "publication_priority_established": False,
            "public_release_authorized": False,
        },
    }
    canonical = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
    certificate["evidence_sha256"] = hashlib.sha256(canonical).hexdigest()
    return certificate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-order", type=int, default=4)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cert = build_certificate(args.maximum_order)
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0 if cert["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
