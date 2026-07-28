# HINC-001 Hostile Technical Review — 2026-07-27

## Review posture

This review treats the manuscript, formal source, evidence package, and proposed website as if they had been submitted by an unknown author making claims near established algebraic-monoid, Hochschild/Gerstenhaber, finite-group-scheme, and computer-assisted-research literature.

The purpose is to find a counterexample, a fatal proof gap, an earlier equivalent result, or a status overclaim. It is not to make the package sound impressive.

## Executive verdict

```text
mathematical status:            serious candidate theorem package
explicit counterexample found:  no
coefficient classifications:    independently rederived; bounded Lean PASS
complete global classification: candidate; not yet fully formalized or externally audited
exact indexed match located:    no
historical priority:            unestablished
public-launch readiness:        blocked pending consolidated revision
journal-submission readiness:   no
```

The controlling even and odd coefficient systems, composition laws, clopen decomposition, center equations, idempotent schemes, finite-Artin counts, and principal polynomial identities survived the hostile audit. The package should nevertheless **not** be released unchanged.

The strongest plausible contribution is the explicit paired arbitrary-base classification and its common-core synthesis. The surrounding mechanisms—Hochschild and Gerstenhaber structure, upper-triangular matrix multiplication, functors of points, nonreduced finite group schemes, algebraic-monoid structure, semidirect products, idempotent splittings, and ordinary field points missing infinitesimal directions—are established.

---

## Release-blocking mathematical findings

### H-01 — The characteristic-two Hochschild foundation was asserted rather than derived

The paper begins from

```text
HH*(F[epsilon]/epsilon^2) = D[u]
```

and a specific bracket formula. A broad citation to truncated-polynomial Hochschild theory is not enough because characteristic, grading, and sign conventions differ across sources.

**Correction completed:** `FOUNDATIONAL_HOCHSCHILD_DERIVATION_2026-07-27.md` now derives the normalized cochain complex, vanishing differential, cup product, circle products, and binary bracket directly in characteristic two.

### H-02 — “Strict Gerstenhaber endomorphism” was underspecified

In positive characteristic, Hochschild cohomology can carry operations beyond the graded-commutative product and binary Gerstenhaber bracket, including restricted or squaring operations and, at cochain level, brace or `E_2` structure.

The present classification checks only:

```text
unitality
base linearity
degree preservation
cup-product preservation
binary degree-minus-one Gerstenhaber-bracket preservation
```

It does not classify preservation of a BV operator, restricted power, Gerstenhaber square, brace algebra, or full `E_2` structure.

**Required wording:** use **binary Gerstenhaber endomorphism** or an equally explicit definition throughout the revised manuscript.

### H-03 — Generator-to-global preservation is the load-bearing proof gap

The Lean package proves coefficient equivalences and normalized composition laws. It does not yet prove that every normalized assignment extends to a cup-and-bracket endomorphism of the complete quotient algebra.

The paper needs a generator-to-global lemma:

> A unital algebra map between presented Gerstenhaber algebras that preserves the bracket on a generating set preserves it on all generated elements, because the bracket is a biderivation in each variable.

The proof must include the graded signs before specializing to characteristic two and must verify that the quotient presentations are complete.

**Correction added:** `GENERATOR_TO_GLOBAL_LEMMA_2026-07-27.md` records the exact lemma and its application boundary. Full Lean formalization remains pending.

### H-04 — The odd algebra presentation needed a completeness proof

The displayed relations hold in `D[u]`, but the original manuscript did not prove that they generate the full kernel.

A normal form is:

```text
F[b] + c F[b] + epsilon F[b] + epsilon c F[b] + F a.
```

Using

```text
c^2=b^3,
ab=epsilon c,
ac=epsilon b^2,
a^2=epsilon a=epsilon^2=0,
```

every word reduces to that form, and the images are distinct members of the visible basis of

```text
D + F epsilon u + u^2 D[u].
```

**Correction added:** `ODD_PRESENTATION_NORMAL_FORM_2026-07-27.md`.

### H-05 — Representability was compressed to one sentence

“Finite generators and relations imply representability” is correct in outline but inadequate in a paper whose principal result is a functor classification.

The revision must specify:

1. the finite affine coefficient space for the images of homogeneous generators;
2. the polynomial equations expressing unitality, relations, products, and brackets;
3. the natural bijection between solutions over each base algebra and endomorphisms;
4. the polynomial composition law;
5. the induced coordinate-bialgebra comultiplication and counit.

Until expanded, representability remains a candidate scheme-level consequence rather than part of the formally checked coefficient kernel.

### H-06 — Scheme-theoretic center and derived subgroup conventions were not fixed

The paper must define:

- the center as the closed subfunctor of elements commuting after every base change;
- the derived subgroup as the appropriate fppf sheaf/closed normal subgroup generated by commutators;
- abelianization as the corresponding fppf quotient.

The explicit commutator formula is supported. The identification of the full fppf-derived subgroup with `alpha_2` remains a specialist-review item.

### H-07 — “Only zero and identity” needs a functor-of-points qualification

The center is the constant finite étale two-point scheme

```text
Spec F sqcup Spec F.
```

On a connected test algebra, its points are zero and identity. On a disconnected algebra, a point may select zero and identity on different clopen components through an idempotent. The original wording was safe as a scheme description but too literal as an all-rings point statement.

### H-08 — The original evidence section is stale

The pre-review manuscript says that proof-assistant verification, immutable hosted execution, and release authorization are absent. The current project has two bounded Lean PASS scopes and an owner-authorized **private draft** review lane. It does not have a public release, full-manuscript formalization, external reproduction, or peer review.

---

## Major scientific-framing corrections

### H-09 — The even multiplication is a constrained triangular-matrix monoid

The law

```text
(x,y,e)(x',y',e') = (xx', yy', x e' + y' e)
```

is ordinary multiplication of upper-triangular matrices

```text
[x e]
[0 y]
```

restricted by

```text
x(y-1)=0,
e^2=0.
```

The multiplication mechanism is not new. The candidate contribution is that this exact constrained nonreduced matrix monoid arises as the binary-Gerstenhaber endomorphism monoid of `E`, with the claimed center and field-point invisibility.

### H-10 — `M_E = C × alpha_2` is an isomorphism of schemes only

The product description is not an isomorphism of monoid schemes: the square-zero coordinate has unequal left and right weights. Every abstract and summary should include “as schemes” at first use.

### H-11 — “Unit doubling” is project terminology, not a novelty mechanism

The odd monoid is a commutative clopen union of a torus component and a crossing ideal, split by a group-like idempotent. This belongs to established idempotent/semilattice-of-groups mechanisms. Prefer:

```text
adjoining a separate clopen unit component
```

unless `Dbl_G(C)` is explicitly defined as local shorthand.

### H-12 — Field-point centrality versus universal center needs exact wording

For each field extension `K/F`, the even unit group on `K`-points is `K^×` and is abelian. Except for identity, those points do not factor through the universal center subgroup scheme. The result contrasts pointwise centers with a natural scheme-valued center; it is not a contradiction in ordinary group theory.

### H-13 — The MCRC application should not control the paper

The classification is standalone. Move the private-project application to an appendix or companion note so that external review does not depend on acceptance of the larger MCRC program.

### H-14 — Novelty language must be narrower

The exact paired coordinate classification was not located in the indexed search. The following are established and cannot carry novelty:

- algebraic and affine monoid-scheme language;
- upper-triangular matrix monoids;
- endomorphism-monoid realization;
- nonreduced automorphism and endomorphism schemes;
- `alpha_2`, semidirect products, and infinitesimal group schemes;
- idempotent decompositions and semilattice-of-groups behavior;
- Hochschild/Gerstenhaber and restricted-operation frameworks;
- ordinary field points failing to detect nilpotent scheme structure.

The defensible candidate contribution is the explicit Gerstenhaber-derived pair, the common crossing core, and the exact contrast between skew infinitesimal thickening and a separate clopen unit component.

---

## Concrete manuscript defects

### H-15 — Incorrect internal references

- Theorem 3.3 cites “Lemmas 2.1 and 2.2”; it should cite Lemmas 3.1 and 3.2.
- Lemma 4.2 says “After Lemma 3.1”; it should say “After Lemma 4.1.”
- Theorem 4.3 cites Lemmas 3.1 and 3.2; it should cite Lemmas 4.1 and 4.2.

### H-16 — Bibliography defects

- Reiner Hermann’s arXiv identifier is `1403.3597`, not `1411.0836`.
- Alberto Elduque’s preprint was first posted in 2025; later revision dates must be separated from publication year.
- The revised foundation should cite direct truncated-polynomial Hochschild sources while remaining self-contained in characteristic two.

### H-17 — Point terminology is inconsistent

Distinguish:

```text
F-rational points
field-extension points
geometric points
points over reduced algebras
points over arbitrary algebras
```

“Ordinary points” may remain in exposition only after the exact category is stated.

### H-18 — Hasse–Weil counts ignore nilpotents by definition

The equality of field-point zeta functions for `M_E` and its reduction is expected because field-valued points factor through the reduction. Present it as a clear illustration of nilpotent invisibility, not as an independent arithmetic surprise.

---

## Independent algebraic audit summary

The following identities were independently rederived with no discrepancy:

```text
even normal form:
  beta = 0
  eta^2 = 0
  lambda(delta-1) = 0

even composition:
  (lambda,delta,eta)(lambda',delta',eta')
  = (lambda lambda', delta delta', lambda eta' + delta' eta)

odd normal form:
  x = q = sigma = 0
  p = lambda rho
  rho = lambda p^2
  lambda(mu-1) = 0
  rho(mu-1) = 0

odd component idempotent:
  z = lambda^3 rho
  z^2 = z

center equations:
  e = 0
  x = y
  x(x-1) = 0

unit commutator:
  [(a,c),(b,d)] = (1,(a+1)d+(b+1)c)
```

The audit supports continued review. It is not external validation.

---

## Website hostile review

### W-01 — The polished design creates an authority halo

The hero, orbital instrument, and “released” language visually outrank the candidate status. The private preview must say **private legal-review preview** and **proposed public review** above the fold.

### W-02 — Mathematics must precede the collaboration narrative

The exact object, theorem, and unresolved proof nodes should appear before the process story. The collaboration record is relevant but self-reported and should not function as mathematical evidence.

### W-03 — Draft links must not target stale `main`

Until merge, use branch-qualified links or disable links that would show older status.

### W-04 — Replace performative challenge language

Replace “Break it” with:

```text
Challenge or reproduce the work.
```

The method may be adversarial without sounding promotional.

### W-05 — Add a citation warning

Display prominently:

> Do not cite HINC-001 as established or peer reviewed. Cite the exact candidate source and status record.

### W-06 — Separate verification levels visually

Do not collapse:

- algebraic kernel Lean PASS;
- coefficient-classification Lean PASS;
- candidate generator-to-global proof;
- unformalized scheme consequences;
- historical-priority search;
- self-reported collaboration record.

### W-07 — Private-preview safety controls

Before release, require:

- `noindex,nofollow,noarchive,nosnippet` during private review;
- restrictive referrer policy and static CSP;
- mobile navigation;
- no-JavaScript access to all substantive content;
- keyboard, forced-colors, reduced-motion, contrast, and 400% zoom checks;
- exact review branch and source identity in the footer.

### W-08 — Repository name versus public wording

The repository name contains “AI,” while the proposed public wording is “Human + LLM.” Resolve that branding/legal mismatch before public visibility.

---

## Prior-art search determination

The search covered exact titles and equations, arXiv, Crossref/DOI-indexed journal records, GitHub, HAL, Zenodo, theses, public MathSciNet/zbMATH surfaces, and nearby terminology in algebraic monoids, endomorphism schemes, Hochschild/Gerstenhaber theory, positive-characteristic restricted operations, and nonreduced group schemes.

No exact indexed match to the complete paired HINC classification was located. This does not exclude:

- nonlinear changes of generators;
- an unnamed specialization of a general theorem;
- theses, non-English literature, or subscription-only records;
- unpublished or private work;
- a classification stored as a matrix monoid rather than a Gerstenhaber endomorphism problem.

A qualified source-level MathSciNet/zbMATH and thesis review remains required.

---

## Release decision

```text
release unchanged:    NO
revise and re-audit:  YES
withdraw theorem:     NO current basis
claim global novelty: NO
request specialists:  YES
keep repository private: YES
```

The revised work should be described as an explicit candidate classification with strong internal evidence, bounded formal verification, and unresolved external correctness and equivalence review.
