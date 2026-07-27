# HINC-001 Hostile Review — 2026-07-27

## Review posture

This review treats the manuscript, evidence package, and proposed website as if they were submitted by an unknown author making claims near established algebraic-monoid, Hochschild/Gerstenhaber, group-scheme, and AI-assisted-research literature.

The goal is not to make the package sound impressive. The goal is to identify every place where a skeptical specialist, editor, referee, or adversarial reproducer could reasonably reject, narrow, or reclassify the work.

## Overall verdict

```text
mathematical status:       serious candidate theorem package
coefficient classifications: strongly supported; bounded Lean PASS
complete manuscript proof: candidate; external audit still required
exact indexed match:       none located in focused search
historical priority:       unestablished
public-launch readiness:   blocked pending listed corrections
journal-submission status: not ready
```

The strongest plausible contribution is the **explicit paired arbitrary-base classification** and common-core synthesis. The surrounding concepts—Hochschild/Gerstenhaber structure, functors of points, nonreduced group schemes, algebraic-monoid structure, and field points missing infinitesimal directions—are established prior art.

## Critical mathematical findings

### 1. Generator-to-global preservation is the load-bearing gap

The Lean package verifies coefficient equivalences and normalized composition laws, not the theorem that each normalized assignment extends uniquely to a strict graded Gerstenhaber endomorphism of the complete presented algebra.

The manuscript must either:

1. add and prove a generator-to-global lemma for presented graded Gerstenhaber algebras; or
2. downgrade every “complete endomorphism functor” theorem until that step is formalized or independently audited.

The proof must show that preserving the defining algebra relations and the complete generator bracket table implies preservation of every bracket under the biderivation identity over an arbitrary commutative characteristic-two base algebra.

### 2. Characteristic-two structure convention is underspecified

The paper defines a strict Gerstenhaber endomorphism as preserving cup product and bracket. In positive characteristic, Hochschild cohomology also carries restricted/squaring operations. The manuscript must state explicitly whether the classified maps preserve:

- cup product and Gerstenhaber bracket only; or
- cup product, bracket, and the relevant characteristic-two squaring/restricted operation.

If the latter is not claimed, the title, definitions, abstract, and claim matrix must say “cup-and-bracket endomorphism” or an equally precise term.

### 3. The fppf-derived subgroup claim needs a specialist scheme audit

The commutator formula is directly checkable. The assertion that the fppf-derived subgroup is exactly `alpha_2` must distinguish:

- pointwise commutators on each test algebra;
- the scheme-theoretic image of the commutator morphism;
- the fppf sheaf image;
- the smallest closed normal subgroup scheme with commutative quotient.

Until that distinction is audited, the derived-subgroup and abelianization statements remain candidate consequences.

### 4. Representability language is too compressed

The sentence “finite homogeneous generators and finitely many relations imply representability” is plausible, but the paper should construct the coefficient affine space, impose every product/bracket equation, and verify functorial bijection explicitly.

Use **affine monoid scheme** consistently. Much algebraic-monoid literature uses “algebraic monoid” for reduced varieties, sometimes irreducible ones. The even HINC object is nonreduced and the odd object is reducible.

## High-priority manuscript corrections

1. Part 1, Theorem 3.3 cites “Lemmas 2.1 and 2.2”; the relevant results are Lemmas 3.1 and 3.2.
2. Part 2, Lemma 4.2 says “After Lemma 3.1”; it should say Lemma 4.1.
3. Add the characteristic-two cup/bracket/squaring convention.
4. Add a generator-to-global lemma or narrow the complete-classification wording.
5. Replace or define “unit doubling”; “adjoining a separate clopen unit component” is clearer.
6. Distinguish the exact HINC example from the established general phenomenon that field-valued points miss infinitesimal scheme structure.
7. Move the MCRC application out of the lead theorem flow or into a clearly optional appendix.
8. Correct Reiner Hermann’s arXiv identifier to `1403.3597`.
9. Record Alberto Elduque’s preprint as first posted in 2025, with later revisions stated separately.
10. Remove stale status text saying that no proof-assistant verification or public-review authorization exists.
11. Replace “publication-grade potential: plausible” with “specialist-review candidate” until external review is complete.
12. State whether the ambient identification `HH*(F[epsilon]/epsilon^2) = D[u]` and the exact bracket formula are proved in the manuscript or imported from a specific source.

## Website hostile-review findings

### Critical

- The original preview said “Public Review” while the repository and PR remained private and draft.
- The polished evidence instrument created an authority halo and was not labeled as a visualization.
- Coefficient-level formal verification, candidate global proofs, scheme consequences, and historical priority were visually collapsed.

### High

- Mobile navigation disappeared without a replacement.
- Explain/Inspect/Reproduce depended on JavaScript.
- Draft links pointed to `main`, where unmerged files could return 404.
- No `noindex` directive, restrictive referrer policy, or static-content security policy was present.
- The collaboration narrative could be mistaken for independent attestation rather than a self-reported, commit-anchored record.

### Corrected private-preview behavior

The v2 private preview now:

- states `PRIVATE LEGAL-REVIEW PREVIEW` above the fold;
- says “proposed public review,” not “released”;
- uses `noindex,nofollow,noarchive,nosnippet`;
- uses a no-referrer policy and static CSP;
- links to the draft branch rather than `main`;
- exposes all reading levels without JavaScript;
- provides mobile navigation;
- labels the observatory as a visualization, not evidence;
- separates correctness, global extension, scheme consequences, novelty, and process attestation;
- specifies what evidence could downgrade each claim;
- keeps model and provider identities undisclosed.

## Release decision

Do not merge the public-review PR or enable Pages until:

1. the manuscript errata are integrated or made controlling;
2. the characteristic-two structure convention is explicit;
3. the generator-to-global claim is narrowed or proved;
4. the prior-art addendum is included;
5. the corrected private website is approved;
6. the remaining accessibility/manual QA gates are completed;
7. legal/editorial review approves the category-level LLM disclosure.
