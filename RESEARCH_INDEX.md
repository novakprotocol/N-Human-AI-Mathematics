# Research index

This index lists only results selected for paper-scale review packages. It is not an inventory of every N-MathLab experiment.

## Repository state

```text
repository visibility:        public
public-review release:        0.1.0-public-review
public review active:         true
visibility switch executed:   true
complete candidate package:   HINC-001
index-only hold entries:      ABF-001, FSG-001, ACM-001
peer reviewed:                no
journal submitted:            no
historical priority:          unestablished
```

## Publication order

| Order | ID | Working title | Field | Current state |
|---:|---|---|---|---|
| 1 | `HINC-001` | Hidden Infinitesimal Noncommutativity in Two Binary-Gerstenhaber Endomorphism Monoid Schemes | Affine monoid schemes, binary Gerstenhaber algebras, nonreduced geometry | Active candidate package; open for public technical review |
| 2 | `ABF-001` | Affine-Hyperplane Degree-Drop Spectra of a Vectorial Boolean Map | Boolean functions, finite linear algebra | Planned second package; exact finite theorem internally reproduced |
| 3 | `FSG-001` | Fibonacci Critical Groups of Carry-Rees Petal Graphs | Critical groups, graph theory, Fibonacci divisibility | Hold pending specialist and formal review |
| 4 | `ACM-001` | ANF Code and Matroid Geometry of a Reduced Vectorial Map | Coding theory, matroids, Boolean functions | Hold pending final consolidation |

## Status rules

- `active_review`: a complete candidate package prepared for public technical review.
- `hold`: mathematically substantial but not yet released as a complete package.
- `archived_case_study`: retained mainly as process history.
- `rejected`: invalidated as stated.
- `superseded`: replaced while preserving the prior record.
- `published`: reserved for an identified archival or journal publication, not ordinary GitHub visibility.

## HINC-001 — first package

### Controlling source

- [`papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md`](papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md)

### Core claim

Two explicit characteristic-two binary-Gerstenhaber endomorphism monoid schemes share the crossing

```text
C = Spec F[x,y]/(x(y-1)).
```

The even object adds a constrained skew square-zero direction. The odd object adds a separate clopen torus unit component.

### Current evidence

- one consolidated, self-contained revised human manuscript;
- complete characteristic-two Hochschild foundation;
- complete even and odd presentations;
- odd normal-form proof;
- generator-to-global proof;
- explicit natural representability arguments;
- corrected center and disconnected-base language;
- expanded fppf-derived-subgroup proof;
- Python, C, Gröbner, finite-Artin, and common-core internal challenge routes;
- public hosted Lean PASS for the algebraic kernel;
- public hosted Lean PASS for the even and odd coefficient classifications and normalized monoid laws;
- preserved failed runs and correction records;
- exact formal and historical-priority limits.

### Pending outside work

- qualified external algebraic-monoid and Gerstenhaber review;
- independent external reproduction;
- source-level historical-equivalence review;
- optional formalization of presently unformalized manuscript nodes;
- journal submission and peer review, if pursued later.

These are objectives of the public technical-review release. They are not falsely represented as already completed.

### Public status

```text
candidate package:       complete
public review active:    yes
repository public:       yes
peer reviewed:           no
historical priority:     unestablished
```

Start with [`papers/HINC-001/README.md`](papers/HINC-001/README.md).

---

## ABF-001 — second package

**Core claim:** For one fully specified map `GF(2)^16 -> GF(2)^8`, exactly 130,559 affine-hyperplane restrictions have degree 15, exactly 511 have degree 14, and none has degree 13 or lower. The 511 exceptional restrictions form a punctured nine-dimensional parameter flat certified by a second rank calculation.

**Internal evidence:** exhaustive classification of all 131,070 affine hyperplanes, separately written C reconstruction, and exhaustive small-universe controls.

**State:** index entry only; complete public package not yet prepared.

---

## FSG-001 — third package

**Core package:** spanning-tree, forest, resistance, critical-group Smith-form, Fibonacci-divisibility, torsion, density, and chip-firing results for Carry-Rees petal graphs.

**State:** hold pending complete standalone packaging, critical-groups review, Fibonacci-divisibility review, formal proof work, and deeper equivalence review.

---

## ACM-001 — fourth package

**Core package:** ANF degree-layer codes, generalized Hamming weights, complete support spectra, chain-condition behavior, coefficient-multiplicity rigidity, automorphism groups, and top-layer code/matroid geometry.

**State:** hold pending consolidation of the v36–v40 line, equivalence review, and exact benchmark framing.

## Process record

The mathematical paper index is separate from the Human + LLM process record. Read:

- [`HUMAN_AI_COLLABORATION_RECORD.md`](HUMAN_AI_COLLABORATION_RECORD.md)
- [`HUMAN_AI_MATHEMATICS_PRIOR_ART.md`](HUMAN_AI_MATHEMATICS_PRIOR_ART.md)
- [`PUBLIC_SWITCH_READINESS.md`](PUBLIC_SWITCH_READINESS.md)

The project does not claim to be the first human–AI mathematics collaboration.

## Selection rule

A result enters the principal index only when it has:

- a precise object and bounded claims;
- a coherent proof or exact finite classification;
- reproducible evidence where relevant;
- explicit formal-verification limits;
- a Human + LLM disclosure boundary;
- a credible external-review question;
- a fail-closed correction and release process.
