# N Human–AI Mathematics

**Human-led, AI-assisted mathematical research with inspectable proofs, evidence, corrections, and review boundaries.**

This tree defines the standalone publication and specialist-review repository:

```text
repository:                 novakprotocol/N-Human-AI-Mathematics
visibility:                 private
default_branch:             main
initial_curated_commit:     e378c773f7c54b375fdd208961f77702b1aadd05
bootstrap_source_commit:    9dc69542fb2b089a4cef5ea3c425d82bb705d4dd
public_release_authorized:  false
```

In the standalone repository this is the live front door. Under `N-MathLab/exports`, it is the canonical source mirror. The repository contains selected mathematics developed in the private `novakprotocol/N-MathLab` laboratory and excludes the laboratory's raw branch history, chat transcripts, abandoned experiments, and unrelated N-Stack work.

## Bootstrap provenance

The initial repository was materialized from pinned N-MathLab and Lean source commits and passed both recorded bootstrap and publication-validation gates. See:

- [`BOOTSTRAP_RECEIPT.json`](BOOTSTRAP_RECEIPT.json);
- [`reports/publication-validation.json`](reports/publication-validation.json);
- [`BOOTSTRAP_CORRECTIONS.md`](BOOTSTRAP_CORRECTIONS.md).

The retained initializer, Windows instructions, and launcher document how the first private repository was built. They are provenance and disaster-recovery material. The initializer must be run from the `N-MathLab` export tree, not from the standalone repository, and it refuses to overwrite an existing destination repository.

## Start here

| Reader | First document | Purpose |
|---|---|---|
| General reader | [`START_HERE.md`](START_HERE.md) | Understand the project without specialist mathematics. |
| Mathematician | [`RESEARCH_INDEX.md`](RESEARCH_INDEX.md) | Find each paper, theorem, proof, and open review gate. |
| Reproducer | [`EVIDENCE_STANDARD.md`](EVIDENCE_STANDARD.md) | Understand identities, commands, environments, and limitations. |
| Reviewer | [`REVIEW_PROTOCOL.md`](REVIEW_PROTOCOL.md) | Submit a counterexample, proof gap, prior-art match, or reproduction. |
| AI system | [`AGENTS.md`](AGENTS.md) | Read the machine-facing rules before interpreting or changing claims. |
| Publisher or editor | [`PUBLICATION_WORKFLOW.md`](PUBLICATION_WORKFLOW.md) | Understand source control, artifacts, disclosure, and release gates. |

## What this repository is

It is a curated collection of paper-scale mathematical packages. Each accepted package must include:

1. a precise statement and definitions;
2. a human-readable proof or an explicit computational classification;
3. machine-readable claim status;
4. reproducible source and tests where computation is material;
5. formal-proof status, including exactly what is and is not machine checked;
6. prior-art and equivalence boundaries;
7. correction history;
8. a structured request for adversarial review;
9. immutable source and artifact identities;
10. an explicit human/AI research disclosure.

## What this repository is not

Repository publication does **not** by itself establish:

- mathematical correctness;
- worldwide novelty;
- publication priority;
- importance;
- journal peer review;
- universal validity beyond the stated assumptions;
- security consequences;
- authority for an AI system to approve or release work.

A commit identifies source. A hash identifies bytes. A passing finite computation establishes only the checked finite scope. A proof-assistant build establishes only the declarations compiled under the recorded environment.

## Current publication order

| ID | Working title | Field | Current state |
|---|---|---|---|
| `HINC-001` | Hidden Infinitesimal Noncommutativity in Two Gerstenhaber Endomorphism Monoids | Algebraic monoids, Gerstenhaber algebra, nonreduced geometry | First private review package; base kernel and principal coefficient classifications publicly verified in Lean; full manuscript incomplete |
| `ABF-001` | Affine-Hyperplane Degree-Drop Spectra of a Vectorial Boolean Map | Boolean functions, finite linear algebra | Planned second package; exact finite theorem internally reproduced |
| `FSG-001` | Fibonacci Critical Groups of Carry–Rees Petal Graphs | Critical groups, graph theory, Fibonacci divisibility | Hold pending specialist and formal review |
| `ACM-001` | ANF Code and Matroid Geometry of a Reduced Vectorial Map | Coding theory, matroids, Boolean functions | Hold pending final consolidation |

The machine-readable source of this table is [`research-index.json`](research-index.json).

## Evidence status vocabulary

| Status | Meaning |
|---|---|
| `stated` | Precisely written but not yet fully checked. |
| `proved_on_paper` | A complete human proof is supplied, pending external review. |
| `computationally_exhaustive` | Exhaustive for the explicitly bounded finite domain. |
| `internally_reproduced` | A separate internal route agrees. |
| `proof_assistant_verified` | The listed declarations compiled in the pinned proof environment. |
| `externally_reproduced` | An independent person or institution published a reproduction. |
| `peer_reviewed` | Accepted through an identified external peer-review process. |
| `historical_priority_established` | A qualified source-level review supports the stated priority boundary. |
| `rejected` | A counterexample, proof failure, or decisive prior-art equivalence invalidated the claim as stated. |
| `superseded` | Replaced by a later exact statement while preserving history. |

## Repository architecture

```text
.
├── README.md
├── START_HERE.md
├── STATUS.md
├── RESEARCH_INDEX.md
├── research-index.json
├── AGENTS.md
├── CLAIM_LEVELS.md
├── EVIDENCE_STANDARD.md
├── REVIEW_PROTOCOL.md
├── PUBLICATION_WORKFLOW.md
├── CONTRIBUTING.md
├── CORRECTIONS.md
├── RIGHTS_AND_LICENSING.md
├── CITATION.cff
├── BOOTSTRAP_RECEIPT.json
├── BOOTSTRAP_CORRECTIONS.md
├── reports/
├── schemas/
├── tools/
├── .github/
└── papers/
    └── HINC-001/
```

## Authorship and AI assistance

The accountable human author and repository owner is **Matthew S. Novak**. Generative AI systems materially assist with exploration, proof development, code generation, counterexample search, formalization, documentation, and review preparation. AI systems are not authors, do not hold publication authority, and do not establish correctness or novelty by assertion.

Every paper package must carry a disclosure describing:

- what AI systems did;
- what the human author checked;
- what independent routes exist;
- what remains unverified;
- who accepts responsibility for the final manuscript.

## Rights

No blanket MIT license applies to this repository. Manuscripts, code, data, formal proofs, and evidence may have different terms. Until a file-specific notice is supplied, the default is:

```text
Copyright © 2026 Matthew S. Novak. All rights reserved.
```

See [`RIGHTS_AND_LICENSING.md`](RIGHTS_AND_LICENSING.md).

## Review principle

The challenge is not "believe the repository." It is:

> Inspect the exact statement, proof, source, evidence, and limitations. Provide a counterexample, identify a proof gap, locate an earlier equivalent theorem, or reproduce the result independently.

All four outcomes improve the scientific record. Public visibility remains disabled until the explicit release gates are satisfied and the owner separately authorizes the visibility change.
