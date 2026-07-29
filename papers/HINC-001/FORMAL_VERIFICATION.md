# HINC-001 formal verification

## Summary

Three bounded Lean gates pass:

1. the base crossing, skew-extension, center consequence, and commutator kernel;
2. the principal even and odd coefficient classifications and normalized monoid laws;
3. the first dual-number Hochschild foundation: the square-zero generator,
   characteristic-two boundary cancellation, represented differential
   vanishing, represented cup associativity, and the epsilon-coefficient product
   rule.

The controlling revised manuscript is:

```text
manuscript/HINC-001_REVISED_MANUSCRIPT.md
```

The full revised manuscript is **not** formalized. Public technical review must
preserve that boundary.

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

The retained axiom report lists Lean's standard `propext` and `Quot.sound`
dependencies for the displayed declarations and no `sorryAx`.

### Base declarations covered

Over an arbitrary commutative characteristic-two ring, Lean verifies:

1. closure of the crossing equation under coordinatewise multiplication;
2. crossing associativity, identity, and commutativity;
3. closure of the square-zero skew extension;
4. skew-extension associativity and identity;
5. the exact commutativity-defect formula;
6. equivalence of commutativity with zero defect;
7. sufficiency of the displayed center equations;
8. the resulting `x(x-1)=0` consequence;
9. the affine unit-group commutator formula with explicit inverse witnesses.

## Principal coefficient classifications — public hosted PASS

```text
checker repository:          novakprotocol/novak-sdt
checker PR:                  #58
immutable source commit:     d7751d1de76253407016ef4bf92738cffa800e82
workflow run:                30174213006
workflow job:                89720259114
artifact:                    8623775718
artifact SHA-256:            2dee88b9a248dee8719c27aa23a27ca3281e697cf67202bb50c1fe60a4809dc9
Classification.lean SHA-256: 56267aba47fd67e94be5842057aaec5bd0718829e860af212eedcdb43efbb084
axiom-report SHA-256:         dcd0bbefb6d88e0c70a57dabc0e45c408fe7998ace6b33e330f6f6d44fb5b7ce
lake build:                  PASS
build jobs:                  8,478
placeholder gate:            PASS
sorryAx:                     absent
```

### Verified even coefficient theorem

For

```text
r -> lambda r + beta s
s -> eta r + delta s,
```

Lean verifies equivalence between the direct generator equations and

```text
beta=0
eta^2=0
lambda(delta-1)=0.
```

It also verifies closure, identity, associativity, and the normalized
coefficient-level classification under

```text
(lambda,delta,eta)(lambda',delta',eta')
 = (lambda lambda',delta delta',lambda eta'+delta' eta).
```

### Verified odd coefficient theorem

Lean verifies equivalence between the direct homogeneous coefficient equations
and

```text
x=q=sigma=0
p=lambda rho
rho=lambda p^2
lambda(mu-1)=0
rho(mu-1)=0.
```

It also verifies closure, identity, associativity, commutativity, and the
normalized coefficient-level classification under coordinatewise composition.

## Dual-number Hochschild foundation — hosted PASS

Exact formal source:

```text
formal/HINC/HochschildFoundation.lean
```

Validated identity:

```text
exact source head:      6670525b00a18b70ec4918982faca0898ecc8e27
workflow run:           30417097923
workflow job:           90465882595
artifact:               8710568867
artifact SHA-256:       2c50072b1c455c45b4d8720762b1451ad1f7e0c2aa5002b79eb0dc9b69828887
Lean:                   4.30.0
Mathlib:                v4.30.0
placeholder gate:       PASS
lake build:             PASS
publication gate:       PASS
full-manuscript PASS:   no
```

Lean models the dual numbers as Mathlib's trivial square-zero extension and
verifies:

1. `epsilon^2 = 0` for the distinguished generator;
2. cancellation of the two remaining normalized Hochschild boundary terms in
   characteristic two;
3. vanishing of the represented normalized-differential value;
4. associativity of represented cup-product multiplication;
5. evaluation of the epsilon-coefficient projection on the generator;
6. the epsilon-coefficient product rule.

This lane does **not** yet identify the complete normalized cochain complex in
all degrees, construct the full Gerstenhaber insertion/bracket operation, prove
the closed bracket formula, or connect those constructions to every presented
source-algebra relation. Those are separate lanes.

## Preserved failed runs and repairs

The first expanded classification run reached Lean compilation but failed because
`OddEndoData.ext` used recursive simplification that exceeded Lean's recursion
depth. The proof was replaced by explicit substitution followed by reflexivity;
the mathematical normal form did not change.

The first Hochschild-foundation attempts exposed two proof-engineering defects:
an invalid Mathlib module path, followed by an incorrect characteristic-two lemma
name and an attempted definitional proof of the coefficient formula. The accepted
source uses the pinned umbrella import, `CharTwo.add_self_eq_zero`, and Mathlib's
trivial-square-zero multiplication simplification. No failed attempt is counted
as formal evidence.

## Deliberately unverified scope

Lean does not yet verify:

- the complete normalized Hochschild cochain identification in every degree;
- the complete insertion and Gerstenhaber-bracket derivation;
- the complete presented source algebras;
- the odd presentation normal-form theorem;
- the generator-to-global binary-bracket lemma;
- the natural representability bijections;
- the coordinate bialgebras as complete affine monoid schemes;
- the clopen decomposition as a functorial scheme statement;
- complete scheme-theoretic center equality;
- the fppf-derived subgroup and abelianization;
- idempotent, normalization, tangent, counting, and zeta consequences;
- the full revised manuscript;
- correctness under external review;
- historical priority, importance, or peer-review status.

## Formal interpretation rule

The correct statement is:

> The algebraic kernel, coefficient equations, normalized monoid laws, and the
> first dual-number Hochschild boundary foundation have bounded public Lean
> verification under a pinned environment with no `sorryAx`. The complete
> revised HINC-001 manuscript has a human proof but is not fully formalized.

Do not replace that with “HINC-001 is formally proved.”

## Next formal targets

The highest-value next targets are:

1. the complete normalized Hochschild cochain and Gerstenhaber-bracket
   calculation;
2. the even and odd presented source algebras;
3. the odd normal-form theorem;
4. the generator-to-global biderivation lemma;
5. the natural representability bijections;
6. the scheme center and fppf-derived subgroup.

Public visibility is intended to solicit formalization and review; it does not
claim those tasks are complete.
