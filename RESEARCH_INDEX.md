# Research Index

This index lists only results selected for a clean paper-scale review package. It is not an inventory of every experiment in N-MathLab.

## Status rules

- `active_review`: complete candidate package being prepared or reviewed.
- `hold`: mathematically substantial but not yet clean enough for public review.
- `archived_case_study`: correct or useful work retained primarily as process history.
- `rejected`: invalidated as stated.
- `superseded`: replaced by a later statement.

## Principal papers

### HINC-001 — Hidden Infinitesimal Noncommutativity

**Working title:** *Hidden Infinitesimal Noncommutativity in Endomorphism Monoids of Two Graded Gerstenhaber Algebras*

**Field:** algebraic monoids, Gerstenhaber algebras, nonreduced algebraic geometry.

**Core claim:** Two explicit characteristic-two Gerstenhaber endomorphism monoids share a crossing core but differ by an infinitesimal skew thickening versus a discrete clopen unit addition. The even monoid can appear commutative on ordinary field-valued points while remaining universally noncommutative.

**Current evidence:**

- complete candidate manuscript and specialist packet;
- independent local and fresh-copy verifier passes;
- public hosted Lean PASS for the crossing, skew extension, commutativity defect, center consequences, and affine commutator kernel;
- public hosted Lean PASS for the principal even and odd coefficient classifications and normalized monoid laws;
- the failed first classification run and explicit proof repair are preserved;
- generator-to-global Gerstenhaber preservation and the remaining scheme-level manuscript are not fully formalized;
- external specialist and historical-equivalence review remain pending.

**Current status:** `active_review`.

---

### ABF-001 — Affine-Hyperplane Degree-Drop Spectra

**Working title:** *Affine-Hyperplane Degree-Drop Spectra of a Vectorial Boolean Map*

**Field:** Boolean functions, vectorial Boolean functions, finite linear algebra.

**Core claim:** For one fully specified map `GF(2)^16 -> GF(2)^8`, exactly 130,559 affine-hyperplane restrictions have degree 15, exactly 511 have degree 14, and none has degree 13 or lower. The 511 exceptional restrictions form a punctured nine-dimensional parameter flat certified by a second rank calculation.

**Current evidence:**

- complete theorem and proof packet;
- primary exhaustive calculation over all 131,070 affine hyperplanes;
- separately written C reconstruction;
- exhaustive control over all 65,536 maps `GF(2)^3 -> GF(2)^2`, totaling 917,504 checks;
- proof-assistant and external specialist review pending.

**Current status:** `hold` pending conversion to the clean publication format.

---

### FSG-001 — Fibonacci Critical Groups of Carry–Rees Petal Graphs

**Field:** critical groups, graph theory, Fibonacci divisibility, chip firing.

**Core package:** closed spanning-tree, forest, and resistance formulas; complete critical-group Smith forms; prime-power torsion progressions; a conditional Wall–Sun–Sun detector; unbounded prime-factor complexity; density laws; and a constructive chip-firing classifier.

**Current evidence:** multiple internal proof and computational routes with preserved correction history.

**Blocking gates:** external critical-groups review, external Fibonacci-divisibility review, formal verification of the graph-to-small-matrix reduction and Smith form, and deeper historical-equivalence review.

**Current status:** `hold`.

---

### ACM-001 — ANF Code and Matroid Geometry

**Field:** coding theory, matroids, Boolean functions.

**Core package:** exact ANF degree-layer codes, generalized Hamming weights, complete subcode support spectra, chain-condition behavior, coefficient-multiplicity rigidity, exact automorphism groups, and a top-layer code/matroid classification.

**Current evidence:** exhaustive finite classification with separate Python and native implementations for the merged portions.

**Blocking gates:** consolidate the controlling manuscript, incorporate the later matroid continuation, perform equivalence review, and define the exact public benchmark object without cryptographic overstatement.

**Current status:** `hold`.

## Results intentionally excluded as standalone papers

The following may appear as supplements or process case studies but should not be promoted as independent mathematical breakthroughs:

- broad black-box measurement atlases;
- bounded dictionary or brute-force preimage searches;
- ordinary avalanche statistics;
- a blind phrase-oracle replay;
- low-entropy public-hash coordinate demonstrations;
- intermediate theorem versions already subsumed by controlling papers;
- proposed invariants determined to be re-encodings of established Hall or probabilistic-zeta data.

## Selection rule

A result is added to the principal index only when it has a precise object, bounded claims, a coherent proof or exact classification, reproducible evidence where relevant, and a credible external-review question.
