# HINC-001 Specialist Review Request

## Purpose

This package requests correctness and equivalence review of a self-contained classification theorem. It does not ask the reviewer to endorse novelty, importance, or the wider N-MathLab programme.

## Main theorem under review

Two explicit graded Gerstenhaber subalgebras of `HH*(F[epsilon]/epsilon^2)` in characteristic two have endomorphism monoid schemes built from the same reduced crossing:

```text
C = Spec F[x,y]/(x(y-1)).
```

The even object is a connected square-zero skew thickening of `C`; the odd object is a reduced commutative clopen unit doubling of `C`.

## Primary review questions

### A. Definitions and presentations

1. Are the presentations of `E` and `O` correct as subalgebras of `D[u]`?
2. Are all displayed Gerstenhaber brackets correct with the stated characteristic-two conventions?
3. Are the homogeneous pieces used for coefficient comparison free over arbitrary commutative base algebras?

### B. Even classification

4. Does preservation of `s^2=0` and `[r,s]=r` give exactly:

   ```text
   beta = 0
   eta^2 = 0
   lambda(delta - 1) = 0?
   ```

5. Are those conditions sufficient to preserve the complete generated Gerstenhaber algebra?
6. Is the composition law correct and closed over arbitrary base algebras?

### C. Odd classification

7. Do the relations force every strict graded endomorphism to be diagonal?
8. Are the four surviving coefficient equations necessary and sufficient?
9. Does the proof use any hidden field-only diagonalization or reducedness assumption?
10. Is coordinatewise composition correct on the normalized data?

### D. Scheme structure

11. Do the coefficient equations represent the complete functors of points?
12. Is the common crossing-core identification correct?
13. Is the odd group-like idempotent and clopen decomposition correct over arbitrary base algebras?
14. Is “unit doubling” already standard under another name?

### E. Center and commutators

15. Does the universal center proof quantify correctly over all base changes?
16. Is the even center exactly zero plus identity?
17. Is the affine unit-group commutator formula used correctly?
18. Is the derived-subgroup statement best formulated as an fppf sheaf-derived subgroup, schematic closure of commutators, or another standard object?

### F. Equivalence and priority

19. Is the full result an immediate specialization of a known theorem on endomorphism schemes of graded Poisson/Gerstenhaber algebras?
20. Are the monoid coordinate algebras already classified under a different normal form?
21. Which parts, if any, are genuinely publication-worthy explicit classification rather than routine calculation?

## Evidence supplied

- self-contained four-part manuscript;
- proof dependency map;
- claim matrix;
- standalone Python verifier and deterministic certificate;
- public hosted Lean base-kernel receipt;
- expanded principal-classification Lean source and hosted gate history;
- prior-art boundary;
- correction ledger;
- exact source commits.

## Requested response format

```text
Reviewer expertise:
Scope reviewed:
Source commit:

Correctness disposition:
- confirmed_for_scope / clarification_required / minor_repair /
  major_repair / counterexample_confirmed / inconclusive

Equivalence disposition:
- no containing theorem identified / likely known consequence /
  exact earlier theorem identified / inconclusive

Load-bearing comments:
1.
2.
3.

Suggested statement changes:

Recommended next action:
- submit / revise once / formalize more / archive as rediscovery /
  reject / seek another specialist
```

## What counts as a successful review

Any of the following is successful:

- confirmation that the proof is correct and nontrivial;
- identification of a repairable gap;
- a concrete counterexample;
- an earlier theorem containing the result;
- a clearer standard formulation of the derived subgroup or unit-doubling construction;
- a recommendation that the result is correct but too narrow for publication.

The objective is an accurate mathematical record, not a predetermined positive verdict.
