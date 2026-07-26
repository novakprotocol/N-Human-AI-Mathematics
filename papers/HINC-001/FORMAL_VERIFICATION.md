# HINC-001 Formal Verification

## Verification summary

Two public immutable Lean gates now pass:

1. the base crossing, skew-extension, center-consequence, and commutator kernel;
2. the principal even and odd coefficient classifications and normalized monoid laws.

The complete paper is still not formalized.

## Base kernel — public hosted PASS

```text
proof assistant:      Lean 4.30.0
Lean commit:          d024af099ca4bf2c86f649261ebf59565dc8c622
Lake:                 5.0.0-src+d024af0
Mathlib:              v4.30.0
compiled source:      8ccf90b05a0ab4fb45774e9dd8ba7b3c9a59cd8c
checker repository:   novakprotocol/novak-sdt
checker PR:           #57
workflow run:         30119931881
workflow job:         89569737408
artifact:             8606983225
artifact SHA-256:     63b2b160da40f722818820679da7c9d22eb7640694e48a5abc08fccf78f47133
lake build:           PASS
build jobs:           8,477
sorryAx:              absent
```

The retained axiom report lists Lean's standard `propext` and `Quot.sound` dependencies for the displayed declarations and no `sorryAx`.

### Declarations covered by the base kernel

Over an arbitrary commutative characteristic-two ring, Lean verifies:

1. closure of the crossing equation under coordinatewise multiplication;
2. crossing associativity, identity, and commutativity;
3. closure of the square-zero skew extension;
4. skew-extension associativity and identity;
5. the exact universal commutativity-defect formula;
6. equivalence of commutativity with zero defect;
7. sufficiency of the displayed center equations;
8. the resulting `x(x-1)=0` coordinate consequence;
9. the affine unit-group commutator formula with explicit inverse witnesses.

## Principal classifications — public hosted PASS

```text
checker repository:          novakprotocol/novak-sdt
checker PR:                  #58
immutable source commit:     d7751d1de76253407016ef4bf92738cffa800e82
workflow run:                30174213006
workflow job:                89720259114
artifact:                    8623775718
artifact SHA-256:            2dee88b9a248dee8719c27aa23a27ca3281e697cf67202bb50c1fe60a4809dc9
Classification.lean SHA-256: 56267aba47fd67e94be5842057aaec5bd0718829e860af212eedcdb43efbb084
axiom-report SHA-256:        dcd0bbefb6d88e0c70a57dabc0e45c408fe7998ace6b33e330f6f6d44fb5b7ce
lake build:                  PASS
build jobs:                  8,478
placeholder gate:            PASS
sorryAx:                     absent
```

The retained classification report lists only `propext` and `Quot.sound` for the displayed declarations and contains no `sorryAx`.

### Verified even coefficient theorem

For the general degree-one candidate

```text
r -> lambda r + beta s
s -> eta r + delta s,
```

Lean verifies equivalence between the direct generator equations and:

```text
beta = 0
eta^2 = 0
lambda(delta - 1) = 0.
```

It also verifies:

- closure of the normalized data under composition;
- identity;
- associativity;
- the coefficient-level principal classification theorem.

The verified composition law is:

```text
(lambda,delta,eta) o (lambda',delta',eta')
  = (lambda lambda', delta delta', lambda eta' + delta' eta).
```

### Verified odd coefficient theorem

Lean verifies equivalence between the direct homogeneous coefficient equations and:

```text
x = q = sigma = 0
p = lambda rho
rho = lambda p^2
lambda(mu - 1) = 0
rho(mu - 1) = 0.
```

It also verifies:

- closure of the normalized data under coordinatewise composition;
- identity;
- associativity;
- commutativity;
- the coefficient-level principal classification theorem.

## Preserved failed run and repair

The first expanded run checked out the intended immutable source, passed the placeholder gate, installed the pinned toolchain, resolved Mathlib, and reached compilation. It failed because `OddEndoData.ext` used `simp_all` in a way that exceeded Lean's recursion depth.

```text
failed run:          30173789803
failed job:          89719185539
failed artifact:     8623660266
failure class:       formal proof engineering
```

The proof was replaced by explicit substitution of the four data-field equalities followed by reflexivity. The mathematical normal form did not change. The repaired immutable source produced the PASS above.

## Deliberately unverified scope

Lean does not yet verify:

- that the normalized assignments preserve every generated cup product;
- that they preserve every generated Gerstenhaber bracket;
- uniqueness and extension through a fully formal quotient/universal property;
- representability of the complete endomorphism functors;
- the coordinate bialgebra formulas as full scheme-level monoid laws;
- the odd clopen decomposition;
- the complete scheme-theoretic center equality;
- the fppf-derived subgroup theorem;
- normalization, tangent, counting, and zeta consequences;
- the complete paper;
- novelty, priority, importance, or peer-review status.

## Next formal target

The next load-bearing theorem is:

> A normalized assignment satisfying the verified coefficient equations extends uniquely to a strict graded Gerstenhaber endomorphism of the presented algebra.

This should be proved separately for `E` and `O`, using explicit generated-algebra structures or quotient/universal-property formalization.

## Interpretation

The public PASS is a substantial correctness upgrade for the coefficient calculations and monoid laws. It is not a substitute for external equivalence review or formalization of the remaining manuscript.
