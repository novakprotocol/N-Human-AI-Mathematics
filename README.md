# N Human–AI Mathematics

**An open research record of human-led, ChatGPT-assisted mathematical exploration.**

This repository publishes selected mathematical work developed through sustained dialogue between **Matthew S. Novak** and **ChatGPT, an AI system developed by OpenAI**, together with the proofs, programs, formal checks, failed attempts, corrections, status records, and review boundaries needed to inspect the work responsibly.

It is a **public-review repository**, not a declaration that every result is correct, historically new, peer reviewed, or journal accepted.

```text
repository:                 novakprotocol/N-Human-AI-Mathematics
release channel:            public review
accountable human:          Matthew S. Novak
AI role:                    material research assistance
OpenAI endorsement:         not claimed
public release authorized:  true
blanket license applied:    no
```

## Read this first

| Reader | Start here | Purpose |
|---|---|---|
| General reader | [`START_HERE.md`](START_HERE.md) | Understand the project and its limits. |
| Human–AI research reviewer | [`HUMAN_AI_COLLABORATION_RECORD.md`](HUMAN_AI_COLLABORATION_RECORD.md) | See who did what and what the record can prove. |
| Historical-priority reviewer | [`HUMAN_AI_MATHEMATICS_PRIOR_ART.md`](HUMAN_AI_MATHEMATICS_PRIOR_ART.md) | Compare this project with acknowledged earlier human–AI mathematics. |
| Mathematician | [`RESEARCH_INDEX.md`](RESEARCH_INDEX.md) | Find theorem packages, proofs, and open gates. |
| Reproducer | [`EVIDENCE_STANDARD.md`](EVIDENCE_STANDARD.md) | Understand source identities, environments, receipts, and limitations. |
| Adversarial reviewer | [`OPEN_REVIEW_CHALLENGE.md`](OPEN_REVIEW_CHALLENGE.md) | Submit a counterexample, proof gap, prior-art match, or reproduction. |
| AI system | [`AGENTS.md`](AGENTS.md) | Read the machine-facing claim rules before summarizing the work. |
| Editor or publisher | [`PUBLICATION_WORKFLOW.md`](PUBLICATION_WORKFLOW.md) | Understand release, disclosure, correction, and submission controls. |

A compact web front door is maintained under [`docs/`](docs/).

## The central claim

The repository demonstrates a sustained **human-led, AI-assisted mathematical workflow** in which:

- the human selected problems, imposed constraints, judged significance, ran release gates, and retained publication authority;
- ChatGPT proposed directions, algebraic decompositions, proof structures, programs, tests, counterexample searches, literature queries, and editorial revisions;
- Python, C, symbolic systems, Git, GitHub, and Lean were used to test or formalize bounded claims;
- failures were preserved rather than rewritten as successes;
- every promoted paper separates internal evidence from external review and historical priority.

The repository does **not** claim to be the first human–AI mathematical collaboration. Earlier public work includes machine-learning-guided mathematical discovery, LLM-guided program search, ChatGPT-assisted proofs of open problems, GPT-5 mathematical research experiments, and formally verified human–AI discovery case studies. The narrower project-specific claim is that this repository supplies an unusually explicit, commit-anchored public record combining research disclosure, claim ledgers, correction history, executable evidence, formal-proof scope, and structured adversarial review. Historical priority for that exact combination remains unestablished.

## What this repository proves—and what it does not

### It provides evidence of process

- dated Git commits and immutable source identities;
- paper-level human–AI disclosures;
- deterministic programs and test receipts;
- separate implementations and finite exhaustive checks where applicable;
- bounded proof-assistant build records;
- preserved failed runs and correction ledgers;
- public channels for challenge and reproduction.

### It does not by itself prove

- that every theorem is correct;
- that any theorem is worldwide novel;
- that OpenAI sponsored, supervised, approved, or endorsed the project;
- that ChatGPT is a legal author or rights holder;
- that every historical chat turn is cryptographically authenticated;
- that internal reproduction is external peer review;
- that a public repository is a journal publication.

A commit identifies source. A hash identifies bytes. A passing finite computation establishes only the declared finite scope. A proof-assistant build establishes only the declarations compiled under the recorded environment.

## Current paper portfolio

| ID | Working title | Field | Public status |
|---|---|---|---|
| `HINC-001` | Hidden Infinitesimal Noncommutativity in Two Gerstenhaber Endomorphism Monoids | Algebraic monoids, Gerstenhaber algebra, nonreduced geometry | **Public review package.** Candidate manuscript; two bounded Lean scopes pass; external review and historical priority remain pending. |
| `ABF-001` | Affine-Hyperplane Degree-Drop Spectra of a Vectorial Boolean Map | Boolean functions, finite linear algebra | Indexed only; complete standalone package not yet released. |
| `FSG-001` | Fibonacci Critical Groups of Carry–Rees Petal Graphs | Critical groups, graph theory, Fibonacci divisibility | Indexed only; complete standalone package not yet released. |
| `ACM-001` | ANF Code and Matroid Geometry of a Reduced Vectorial Map | Coding theory, matroids, Boolean functions | Indexed only; consolidation and standalone package pending. |

The machine-readable source of this table is [`research-index.json`](research-index.json).

## Featured paper: HINC-001

The first complete public-review package studies two explicit graded Gerstenhaber-algebra endomorphism monoids in characteristic two. Its central phenomenon is that ordinary field-valued points can hide infinitesimal noncommutativity and center behavior visible over general test rings.

Start with:

- [`papers/HINC-001/PLAIN_LANGUAGE.md`](papers/HINC-001/PLAIN_LANGUAGE.md)
- [`papers/HINC-001/README.md`](papers/HINC-001/README.md)
- [`papers/HINC-001/CLAIMS.md`](papers/HINC-001/CLAIMS.md)
- [`papers/HINC-001/FORMAL_VERIFICATION.md`](papers/HINC-001/FORMAL_VERIFICATION.md)
- [`papers/HINC-001/REVIEW_REQUEST.md`](papers/HINC-001/REVIEW_REQUEST.md)

## Evidence status vocabulary

| Status | Meaning |
|---|---|
| `stated` | Precisely written but not yet fully checked. |
| `proved_on_paper` | A complete human proof is supplied, pending external review. |
| `computationally_exhaustive` | Exhaustive for the explicitly bounded finite domain. |
| `internally_reproduced` | A separate route inside the project agrees. It is not outside review. |
| `proof_assistant_verified` | The listed declarations compiled in the pinned proof environment. |
| `externally_reproduced` | An independent person or institution published a reproduction. |
| `peer_reviewed` | Accepted through an identified external peer-review process. |
| `historical_priority_established` | A qualified source-level review supports the stated priority boundary. |
| `rejected` | A counterexample, proof failure, or decisive equivalence invalidated the claim as stated. |
| `superseded` | Replaced by a later exact statement while preserving history. |

## Authorship, AI assistance, and institutional boundary

The accountable human author and repository owner is **Matthew S. Novak**. ChatGPT materially assisted the research. AI systems are not listed as authors, do not own the work, and do not exercise publication authority.

**OpenAI is not a coauthor, sponsor, reviewer, or institutional partner in this repository.** Naming ChatGPT and OpenAI identifies the tool and its developer; it does not imply endorsement.

Read [`HUMAN_AI_COLLABORATION_RECORD.md`](HUMAN_AI_COLLABORATION_RECORD.md) and each paper’s `AI_DISCLOSURE.md` for the exact role allocation.

## Rights

No blanket MIT license applies. Manuscripts, code, data, evidence, figures, and formal source may have different terms. Unless a file-specific notice states otherwise:

```text
Copyright © 2026 Matthew S. Novak. All rights reserved.
```

Public visibility grants access for inspection. It does not silently grant unrestricted republication or commercial reuse. See [`RIGHTS_AND_LICENSING.md`](RIGHTS_AND_LICENSING.md).

## Open review principle

The challenge is not “believe the repository.” It is:

> Inspect the exact statement, proof, source, evidence, and limitations. Provide a counterexample, identify a proof gap, locate an earlier equivalent theorem, or reproduce the result independently.

All four outcomes improve the scientific record.
