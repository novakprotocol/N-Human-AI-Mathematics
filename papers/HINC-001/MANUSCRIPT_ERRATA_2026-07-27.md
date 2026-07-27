# HINC-001 Controlling Manuscript Errata — 2026-07-27

This file is controlling for the private legal-review branch until the manuscript is consolidated and rerendered. It does not silently alter the earlier source identity.

## Status

```text
errata_status: active
manuscript_status: candidate pending revision
mathematical_counterexample_found: no
load-bearing proof clarification required: yes
public release blocked: yes
```

## E-001 — Part 1 theorem cross-reference

**Location:** `manuscript/MANUSCRIPT_PART_1.md`, Theorem 3.3 proof.

**Current text:**

```text
Lemmas 2.1 and 2.2 prove necessity.
```

**Correction:**

```text
Lemmas 3.1 and 3.2 prove necessity.
```

**Effect:** editorial only.

## E-002 — Part 2 lemma cross-reference

**Location:** `manuscript/MANUSCRIPT_PART_2.md`, Lemma 4.2.

**Current text:**

```text
After Lemma 3.1, the defining algebra relations are equivalent to ...
```

**Correction:**

```text
After Lemma 4.1, the defining algebra relations are equivalent to ...
```

**Effect:** editorial only.

## E-003 — Characteristic-two structure convention

The manuscript must define whether “strict graded Gerstenhaber endomorphism” preserves:

1. graded-commutative cup product and Gerstenhaber bracket only; or
2. cup product, bracket, and the characteristic-two restricted/squaring operation on Hochschild cohomology.

Until revised, every HINC claim is interpreted as a **cup-and-bracket** endomorphism claim only. No preservation of a restricted or squaring operation is claimed.

**Effect:** claim-scope clarification; potentially load bearing if a stronger structure was intended.

## E-004 — Generator-to-global sufficiency

The current Lean source proves coefficient equivalence and normalized monoid laws, not the global theorem that the normalized generator assignment preserves all products and all brackets in the complete generated algebra.

Until a generator-to-global theorem is supplied and audited, replace:

```text
complete endomorphism functor
```

with:

```text
candidate complete cup-and-bracket endomorphism functor, with coefficient classification formally verified and generator-to-global sufficiency pending formalization
```

This applies to Theorems 3.3 and 4.3 and all downstream claims depending on them.

**Effect:** load-bearing status correction; no counterexample currently known.

## E-005 — Representability terminology

Use:

```text
affine monoid scheme
```

rather than unqualified:

```text
algebraic monoid
```

when discussing the nonreduced even object or the reducible odd object.

The paper must construct the coefficient scheme and functorial bijection explicitly rather than relying on a one-sentence finite-presentation assertion.

**Effect:** terminology and proof-detail correction.

## E-006 — Unit-doubling terminology

Replace undefined uses of:

```text
unit doubling
```

with:

```text
adjoining a separate clopen unit component
```

or define `Dbl_G(C)` formally before using the phrase.

**Effect:** terminology only.

## E-007 — Center and derived subgroup boundary

The explicit commutator calculation remains supported. The statement

```text
[G_E,G_E] = alpha_2
```

must be labeled as an fppf/group-scheme candidate until a specialist verifies the distinction between pointwise commutators, scheme image, fppf sheaf image, and the closed derived subgroup.

**Effect:** claim-status narrowing.

## E-008 — Ambient Hochschild/Gerstenhaber source

The identification

```text
HH*(F[epsilon]/epsilon^2) = D[u]
```

and the displayed bracket formula must either be derived in a standalone foundation lemma or tied to an exact source whose characteristic and convention match the manuscript.

The broad Hochschild/Gerstenhaber literature is not a substitute for this exact foundational identity.

**Effect:** source/proof completeness correction.

## E-009 — Bibliography metadata

- Reiner Hermann’s arXiv identifier is `1403.3597`, not `1411.0836`.
- Alberto Elduque’s preprint `2507.12321` was first posted in 2025; later revision dates should be stated separately.

**Effect:** bibliographic correction only.

## E-010 — Stale status in Part 4

Part 4 states that proof-assistant verification, immutable hosted execution, and public-release authorization are absent. Current project records include two bounded public Lean PASS scopes and an owner-authorized private public-review staging lane.

Replace the stale status section with the current machine-readable status. Do not state that the full manuscript is formally verified or publicly released.

**Effect:** evidence-status correction.

## E-011 — Novelty wording

The following concepts are established and must not be claimed as new:

- algebraic/affine monoid scheme language;
- functors of points;
- nonreduced automorphism or endomorphism schemes;
- Hochschild/Gerstenhaber structure of truncated polynomial algebras;
- ordinary field points missing infinitesimal scheme structure;
- `alpha_2`, semidirect products, and infinitesimal commutators.

The candidate contribution is narrowed to the explicit paired all-base classification, common reduced crossing, and exact contrasting modifications.

**Effect:** novelty-boundary correction.

## E-012 — MCRC application

The MCRC application is not a logical prerequisite and should be moved to an optional appendix or companion application note so that the lead paper remains a standalone algebra/scheme classification.

**Effect:** editorial and positioning correction.

## Required consolidated rewrite

Before public release, produce a new manuscript identity that incorporates E-001 through E-012, rerun all source/evidence checks, update hashes, and visually inspect all derived artifacts. The earlier manuscript remains preserved as the pre-hostile-review source.
