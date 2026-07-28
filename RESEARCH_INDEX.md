# Research index

This index lists only results selected for paper-scale review packages. It is not an inventory of every N-MathLab experiment.

## Repository state

```text
repository visibility:        public
public-review release:        0.1.0-public-review
public review active:         true
visibility switch executed:   true
complete candidate packages:  HINC-001, ABF-001
index-only hold entries:      FSG-001, ACM-001
peer reviewed:                no
journal submitted:            no
historical priority:          unestablished
```

## Publication order

| Order | ID | Working title | Field | Current state |
|---:|---|---|---|---|
| 1 | `HINC-001` | Hidden Infinitesimal Noncommutativity in Two Binary-Gerstenhaber Endomorphism Monoid Schemes | Affine monoid schemes, binary Gerstenhaber algebras, nonreduced geometry | Active candidate package; open for public technical review |
| 2 | `ABF-001` | Affine Restriction Moment Kernels and Radical Incidence Geometry of a Vectorial Boolean Map | Boolean functions, Reed-Muller codes, finite linear algebra | Active candidate package; open for public technical review |
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

**Controlling source:** [`papers/ABF-001/manuscript/ABF-001_MANUSCRIPT.md`](papers/ABF-001/manuscript/ABF-001_MANUSCRIPT.md)

**Core result:** A Reed-Muller moment criterion yields dual output-mask annihilator and affine-parameter kernel descriptions of restriction degree drop. For the specified map `GF(2)^16 -> GF(2)^8`, the complete vectorial spectrum is `130,559 / 511 / 0`; the order-one symmetric pencil has rank multiplicities `2 / 15 / 74 / 112 / 52`; and its corrected radical geometry has 203 mask-indexed radicals, 202 distinct nonzero radical subspaces, 469 incidences, 467 covered parameters, and 201 forest components.

**Evidence:** complete human proof, full 131,070-hyperplane enumeration, primary and integer/bitset implementations, complete 5,505,024-comparison small-universe control, tamper rejection, exact manifests, final hostile review with zero blockers, and a same-day systematic prior-art delta.

**Public status:** candidate technical review active at `abf-001-public-review-v1`. Historical priority, external reproduction, peer review, and complete formal verification remain unestablished.

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
