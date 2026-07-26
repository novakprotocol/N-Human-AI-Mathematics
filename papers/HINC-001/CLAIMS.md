# HINC-001 Claim Matrix

## Object definition

Let `F` be a field of characteristic two, let

```text
D = F[epsilon]/(epsilon^2),
HH*(D) = D[u], |u| = 1,
```

with the displayed Hochschild Gerstenhaber bracket, and define the two explicit graded Gerstenhaber subalgebras `E` and `O` in the manuscript.

The classifications are intended functorially over arbitrary commutative `F`-algebras `R`.

## Principal claims

| ID | Claim | Current support | Status |
|---|---|---|---|
| `HINC-E-1a` | The direct even generator equations are equivalent to `beta=0`, `eta^2=0`, and `lambda(delta-1)=0`. | Human derivation plus public hosted Lean PASS. | Proof-assistant verified |
| `HINC-E-1b` | Every strict graded Gerstenhaber endomorphism of `E_R` has the resulting normal form. | Complete manuscript proof; coefficient theorem Lean PASS; generator-to-global sufficiency not yet formalized. | Candidate theorem with verified coefficient layer |
| `HINC-E-2` | Normalized composition is `(lambda,delta,eta)(lambda',delta',eta')=(lambda lambda',delta delta',lambda eta'+delta' eta)`, with identity and associativity. | Direct substitution; finite/symbolic verifier; public hosted Lean PASS. | Proof-assistant verified for normalized data |
| `HINC-E-3` | The representing monoid scheme is `Spec F[lambda,delta,eta]/(eta^2,lambda(delta-1))`. | Manuscript representability argument from finite homogeneous generators and relations. | Candidate theorem |
| `HINC-E-4` | The reduction is the crossing `C=Spec F[x,y]/(x(y-1))`; the full monoid is a connected nonreduced skew thickening and is noncommutative. | Manuscript proof; explicit dual-number witness; base Lean skew/defect kernel PASS. | Strongly supported candidate theorem |
| `HINC-E-5` | The scheme-theoretic center is exactly zero and identity. | Manuscript coefficient calculation; base Lean verifies sufficient center equations and one consequence, not the complete equality. | Candidate theorem; partial formal kernel |
| `HINC-E-6` | The unit group is `alpha_2 semidirect G_m`, with trivial center, derived subgroup `alpha_2`, and abelianization `G_m`. | Manuscript calculation; affine commutator formula Lean PASS; full group-scheme consequences not formalized. | Candidate theorem; partial formal kernel |
| `HINC-O-1a` | The direct odd coefficient equations are equivalent to the stated diagonal normal form. | Human derivation plus public hosted Lean PASS. | Proof-assistant verified |
| `HINC-O-1b` | Every strict graded Gerstenhaber endomorphism of `O_R` is diagonal with those equations. | Complete manuscript proof; coefficient theorem Lean PASS; generator-to-global sufficiency not yet formalized. | Candidate theorem with verified coefficient layer |
| `HINC-O-2` | The normalized odd endomorphism composition is closed, unital, associative, and commutative. | Manuscript proof and public hosted Lean PASS. | Proof-assistant verified for normalized data |
| `HINC-O-3` | The odd monoid is reduced and splits as a clopen unit component disjoint from the common crossing core. | Manuscript algebraic/scheme proof; not yet formalized. | Candidate theorem |
| `HINC-C-1` | The even and odd monoids contain the same crossing core but differ by infinitesimal skew thickening versus discrete unit doubling. | Consequence of the two classifications and scheme decompositions. | Candidate synthesis theorem |
| `HINC-P-1` | Ordinary field-valued points fail to detect the even infinitesimal noncommutativity and universal center. | Explicit square-zero analysis; base Lean defect kernel; formal field/reduced-base comparison not complete. | Strongly supported candidate consequence |

## Secondary claims

The manuscript also derives:

- idempotent schemes;
- connected-component structure;
- normalization of the crossing core;
- tangent dimensions;
- finite-field point counts;
- zeta functions;
- application to the even/odd MCRC singular-corner images.

These claims are subordinate to the principal classification. Their correctness depends on the classification and their individual calculations.

## Computational claims

The standalone verifier checks:

- the common-core laws over finite Artin rings `F_2[t]/(t^n)` for `1 <= n <= 4`;
- the declared finite cases and symbolic identities;
- semantic negative controls;
- deterministic certificate regeneration.

The finite checks support implementation consistency. They do not prove the arbitrary-base theorem by enumeration.

## Formal claims

### Base public hosted PASS

Lean 4.30.0 with Mathlib v4.30.0 verifies:

- crossing multiplication laws;
- skew-extension multiplication laws;
- exact commutativity defect;
- commutativity iff zero defect;
- sufficient center equations and an idempotent-coordinate consequence;
- affine unit commutator formula.

### Principal-classification public hosted PASS

The immutable repaired `HINC/Classification.lean` verifies:

- even generator equations iff normal form;
- even normalized composition closure, identity, and associativity;
- even coefficient-level principal classification;
- odd generator equations iff normal form;
- odd normalized composition closure, identity, associativity, and commutativity;
- odd coefficient-level principal classification.

```text
workflow run:           30174213006
workflow job:           89720259114
artifact SHA-256:       2dee88b9a248dee8719c27aa23a27ca3281e697cf67202bb50c1fe60a4809dc9
Classification SHA-256:56267aba47fd67e94be5842057aaec5bd0718829e860af212eedcdb43efbb084
sorryAx:                absent
```

The first run failed on proof recursion depth and is preserved; the repaired proof passed without changing the normal-form statement.

### Formal scope still missing

The current Lean package does not yet prove the complete generator-to-global strict Gerstenhaber extension, scheme representability, odd clopen decomposition, complete center equality, or derived-subgroup theorem.

## Claims explicitly prohibited at this stage

Do not state that:

- the full manuscript is formally verified;
- worldwide novelty is established;
- publication priority is established;
- no equivalent general theorem exists;
- an external specialist has approved the result;
- the work is peer reviewed;
- the result solves an open problem;
- the result has a cryptographic weakness or security consequence;
- AI assistance proves autonomy, correctness, or authorship;
- test counts replace the universal proof.

## Promotion rule

Any status upgrade must identify the exact new evidence, source commit, reviewer or proof environment, and the precise claims affected.
