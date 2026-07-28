# HINC-001 Controlling Manuscript Errata — 2026-07-27

This file is controlling for the private legal-review branch until the manuscript is consolidated and rerendered. It does not silently alter the earlier source identity.

## Status

```text
errata_status:                    active
manuscript_status:                candidate pending consolidated revision
mathematical_counterexample_found:no
load-bearing proof additions:     supplied in controlling addenda
Lean integration of additions:    pending
public release blocked:           yes
```

## E-001 — Part 1 theorem cross-reference

**Location:** `manuscript/MANUSCRIPT_PART_1.md`, Theorem 3.3 proof.

Replace:

```text
Lemmas 2.1 and 2.2 prove necessity.
```

with:

```text
Lemmas 3.1 and 3.2 prove necessity.
```

**Effect:** editorial only.

## E-002 — Part 2 cross-references

**Location:** `manuscript/MANUSCRIPT_PART_2.md`.

Replace:

```text
After Lemma 3.1 ...
```

with:

```text
After Lemma 4.1 ...
```

In Theorem 4.3, replace the citation to Lemmas 3.1 and 3.2 with Lemmas 4.1 and 4.2.

**Effect:** editorial only.

## E-003 — Characteristic-two structure convention

Every HINC claim is interpreted as a **binary Gerstenhaber endomorphism** claim:

```text
unital
base-linear
degree-preserving
cup-product-preserving
binary degree-minus-one bracket-preserving
```

No preservation of a BV operator, restricted power, Gerstenhaber square, brace algebra, or full `E_2` structure is claimed.

**Effect:** claim-scope clarification; load bearing if a stronger structure had been intended.

## E-004 — Generator-to-global sufficiency

The Lean source proves coefficient equivalence and normalized monoid laws, not the global extension theorem.

The human proof is now supplied in:

```text
GENERATOR_TO_GLOBAL_LEMMA_2026-07-27.md
```

Until formalized and externally audited, replace unqualified uses of:

```text
complete endomorphism functor
```

with:

```text
candidate complete binary-Gerstenhaber endomorphism functor; coefficient classification formally verified, global extension human-proved and formalization pending
```

**Effect:** load-bearing status correction; no counterexample currently known.

## E-005 — Representability terminology and proof

Use:

```text
affine monoid scheme
```

rather than unqualified “algebraic monoid” when discussing the nonreduced even object or reducible odd object.

The consolidated paper must explicitly construct the finite coefficient affine space, polynomial relation/bracket equations, natural functorial bijection, polynomial composition map, and coordinate bialgebra.

**Effect:** terminology and proof-detail correction.

## E-006 — Clopen-unit terminology

Replace undefined promotional uses of:

```text
unit doubling
```

with:

```text
adjoining a separate clopen unit component
```

or define `Dbl_G(C)` formally as local shorthand after acknowledging the standard idempotent/semilattice-of-groups mechanism.

**Effect:** terminology and novelty-boundary correction.

## E-007 — Center and derived subgroup boundary

The explicit commutator calculation remains supported.

The paper must define:

- the center as a closed subfunctor after arbitrary base change;
- the fppf sheaf/closed subgroup convention for the derived subgroup;
- the abelianization quotient convention.

The statement

```text
[G_E,G_E] = alpha_2
```

remains a candidate group-scheme consequence pending specialist audit of pointwise image, scheme image, fppf sheaf image, and closed normal subgroup generation.

**Effect:** claim-status narrowing.

## E-008 — Ambient Hochschild/Gerstenhaber foundation

The exact identification and bracket are now proved in:

```text
FOUNDATIONAL_HOCHSCHILD_DERIVATION_2026-07-27.md
```

The consolidated manuscript must incorporate that proof rather than merely cite broad truncated-polynomial literature.

**Effect:** foundational proof addition.

## E-009 — Bibliography metadata

- Reiner Hermann’s arXiv identifier is `1403.3597`, not `1411.0836`.
- Alberto Elduque’s preprint `2507.12321` was first posted in 2025; later revision dates should be stated separately.
- Add direct sources for truncated-polynomial Hochschild rings, BV/Gerstenhaber structures, positive-characteristic restricted operations, nonreduced automorphism schemes, and algebraic-monoid classifications.

**Effect:** bibliographic correction only.

## E-010 — Stale status in Part 4

Replace the stale status section with the current machine-readable status:

```text
two bounded Lean PASS scopes: yes
full manuscript Lean proof:   no
private draft review lane:     yes
public release:                no
external specialist review:   no
historical priority:           unestablished
```

**Effect:** evidence-status correction.

## E-011 — Novelty wording

The following concepts are established and must not be claimed as new:

- algebraic and affine monoid-scheme language;
- upper-triangular matrix monoids;
- functors of points;
- nonreduced automorphism or endomorphism schemes;
- Hochschild/Gerstenhaber structure of truncated polynomial algebras;
- positive-characteristic restricted operations;
- field-valued points missing infinitesimal scheme structure;
- `alpha_2`, semidirect products, and infinitesimal commutators;
- idempotent and clopen decompositions.

The candidate contribution is narrowed to the explicit paired arbitrary-base classification, common reduced crossing, and exact contrasting modifications.

**Effect:** novelty-boundary correction.

## E-012 — MCRC application

The MCRC application is not a logical prerequisite. Move it to an optional appendix or companion application note.

**Effect:** editorial and positioning correction.

## E-013 — Odd presentation completeness

The relations for the odd algebra require a kernel/completeness proof. This is now supplied in:

```text
ODD_PRESENTATION_NORMAL_FORM_2026-07-27.md
```

The unique normal form is:

```text
f(b) + c g(b) + epsilon h(b) + epsilon c k(b) + tau a.
```

The consolidated manuscript must integrate that argument.

**Effect:** load-bearing presentation proof addition.

## E-014 — Even triangular-matrix framing

Identify

```text
(x,y,e)
```

with the upper-triangular matrix

```text
[x e]
[0 y].
```

The even law is ordinary matrix multiplication restricted by `x(y-1)=0` and `e^2=0`. The multiplication mechanism is not a novelty claim.

**Effect:** scientific framing correction.

## E-015 — Scheme product qualifier

Whenever stating

```text
M_E = C × alpha_2,
```

add:

```text
as schemes, not as monoid schemes.
```

The square-zero coordinate has unequal left and right weights.

**Effect:** mathematical-structure clarification.

## E-016 — Center points over disconnected bases

Replace literal all-base wording “the center consists only of zero and identity” with:

> The center is the constant finite étale two-point scheme. On connected test algebras its points are zero and identity; on disconnected bases its points correspond to idempotent clopen decompositions.

**Effect:** functor-of-points correction.

## E-017 — Point taxonomy

Distinguish explicitly:

```text
F-rational points
field-extension points
geometric points
reduced-base points
arbitrary-base points
```

Use “ordinary points” only as informal prose after the exact category is named.

**Effect:** terminology correction.

## E-018 — Zeta-function framing

State that Hasse–Weil point counts ignore nilpotent thickening because maps from fields factor through the reduction. Present equality of the even monoid and reduced-crossing zeta functions as an illustration of nilpotent invisibility, not an independent arithmetic anomaly.

**Effect:** interpretation correction.

## Required consolidated rewrite

Before public release:

1. integrate E-001 through E-018 into a new manuscript identity;
2. rerun all source, computation, and formal-status checks;
3. update evidence maps and hashes;
4. regenerate PDF/DOCX/anonymous artifacts;
5. inspect every rendered page;
6. run external algebra/monoid and historical-equivalence review;
7. approve a corrected private website preview;
8. keep the repository private until those gates are resolved.

The earlier manuscript remains preserved as the pre-hostile-review source.
