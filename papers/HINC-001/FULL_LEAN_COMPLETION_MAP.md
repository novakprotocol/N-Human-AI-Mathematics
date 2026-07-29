# HINC-001 full-Lean completion map

## Controlling rule

HINC-001 remains on `PUBLIC_ARCHIVE_FULL_LEAN_REQUALIFICATION_HOLD` until every retained mathematical claim C-01 through C-18 is mapped to compiled Lean. C-19 is excluded from the controlling core paper. C-20 is a historical-search boundary, not a mathematical theorem.

## Current compiled foundation

The existing immutable Lean gates cover parts of C-03, C-05, C-07, C-11, C-12, and C-13: the base crossing/skew kernel, coefficient equations, normalized composition laws, commutativity defect, sufficient center equations, and unit-group commutator.

Those passes are retained, but no claim is marked complete merely because one algebraic sublemma is formalized.

## Required lanes

| Lane | Claim IDs | Required formal result | Current state |
|---|---|---|---|
| H01 | C-01 | Normalized Hochschild cochain model for `D=F[ε]/(ε²)` in characteristic two; cup product; bracket formula; cohomology identification | PARTIAL FOUNDATION ONLY |
| H02 | C-02 | Even source algebra presentation and binary bracket, including normal forms and equivalence with the manuscript object | OPEN |
| H03 | C-03 | Complete even coefficient classification with all hypotheses and both directions | BOUNDED PASS; FIDELITY RECHECK REQUIRED |
| H04 | C-04 | Generator-to-global theorem proving that normalized coefficients classify every binary Gerstenhaber endomorphism over arbitrary commutative characteristic-two bases | OPEN |
| H05 | C-05 | Natural representability equivalence and monoid-scheme composition for the even functor | PARTIAL COMPOSITION PASS |
| H06 | C-06 | Odd source algebra presentation, relations, basis/normal-form theorem, and binary bracket | OPEN |
| H07 | C-07 | Complete odd coefficient classification with all hypotheses and both directions | BOUNDED PASS; FIDELITY RECHECK REQUIRED |
| H08 | C-08 | Odd generator-to-global endomorphism classification | OPEN |
| H09 | C-09 | Odd representability, coordinatewise composition, group-like idempotent, and functorial clopen split | OPEN |
| H10 | C-10 | Exact common reduced crossing identifications for the even reduction and odd nonunit component | PARTIAL ALGEBRAIC KERNEL |
| H11 | C-11 | Universal commutativity-defect theorem plus explicit noncommutative witness over a square-zero test algebra | BOUNDED PASS; MANUSCRIPT MAP REQUIRED |
| H12 | C-12 | Equality of the complete scheme-theoretic center subfunctor with the stated idempotent scheme | PARTIAL SUFFICIENCY PASS |
| H13 | C-13 | Unit-group law, inverse witnesses, and commutator formula | BOUNDED PASS; MANUSCRIPT MAP REQUIRED |
| H14 | C-14 | fppf image sheaf, derived subgroup `α₂`, and abelianization `G_m` | OPEN |
| H15 | C-15 | Complete even and odd idempotent-scheme classifications | OPEN |
| H16 | C-16 | Reduction, connectedness, normalization, components, and tangent-space calculations | OPEN |
| H17 | C-17 | General formulas for `F₂[t]/(t^n)` counts and idempotents with exact hypotheses | OPEN |
| H18 | C-18 | Finite-field point counts and zeta functions derived from the formal scheme decompositions | OPEN |

## Completion gate

HINC reaches `FULL_MANUSCRIPT_LEAN_PASS` only when:

- all H01–H18 lanes compile under one pinned project;
- every C-01–C-18 claim maps to exact declaration names;
- no `sorry`, `admit`, project-result axiom, or `sorryAx` occurs;
- an axiom report and human fidelity audit pass;
- the complete public source builds from a clean immutable commit;
- the release record and website display the exact formal scope and external-review boundary.
