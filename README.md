# N Human–AI Mathematics

**Private staging for human-led, LLM-assisted mathematical research.**

This repository curates selected mathematics developed through sustained interaction between **Matthew S. Novak** and one or more **large language models**, together with the proof sources, programs, formal checks, failed attempts, corrections, status records, and review boundaries needed to inspect the work responsibly.

It is currently a **private hostile-review and legal/editorial staging repository**. No paper is publicly released from this branch.

```text
repository:                 novakprotocol/N-Human-AI-Mathematics
visibility:                 private
release channel:            private staging
accountable human:          Matthew S. Novak
LLM role:                   material research assistance
specific model/provider:    not disclosed
public release authorized:  false pending revised approval
peer reviewed:              no
blanket license applied:    no
```

## Read this first

| Reader | Start here | Purpose |
|---|---|---|
| General reader | [`START_HERE.md`](START_HERE.md) | Understand the project and its limits. |
| Mathematician | [`RESEARCH_INDEX.md`](RESEARCH_INDEX.md) | Find candidate theorem packages and open gates. |
| HINC hostile reviewer | [`papers/HINC-001/HOSTILE_REVIEW_2026-07-27.md`](papers/HINC-001/HOSTILE_REVIEW_2026-07-27.md) | See the adversarial findings and release blockers. |
| Proof auditor | [`papers/HINC-001/CLAIMS.md`](papers/HINC-001/CLAIMS.md) | Read the narrowed claim-by-claim status. |
| Reproducer | [`EVIDENCE_STANDARD.md`](EVIDENCE_STANDARD.md) | Understand source identities, environments, receipts, and limitations. |
| Historical-priority reviewer | [`papers/HINC-001/PRIOR_ART_PRIMARY_SOURCE_MAP_2026-07-27.json`](papers/HINC-001/PRIOR_ART_PRIMARY_SOURCE_MAP_2026-07-27.json) | Inspect the closest established frameworks and search limits. |
| LLM system | [`AGENTS.md`](AGENTS.md) | Read the machine-facing claim rules before summarizing the work. |
| Editor or publisher | [`PUBLICATION_WORKFLOW.md`](PUBLICATION_WORKFLOW.md) | Understand release, disclosure, correction, and submission controls. |

The proposed static site under [`docs/`](docs/) is a private preview and is blocked from deployment by [`docs/PRIVATE_PREVIEW_BLOCKERS_2026-07-27.md`](docs/PRIVATE_PREVIEW_BLOCKERS_2026-07-27.md).

## Current hostile-review result

The 2026-07-27 audit did **not** find an explicit counterexample to the controlling even or odd coefficient systems. It did find release-blocking defects in foundation, terminology, global-proof presentation, representability, center/derived-subgroup conventions, citations, status language, and website framing.

The following records now control HINC-001:

- [`HOSTILE_REVIEW_2026-07-27.md`](papers/HINC-001/HOSTILE_REVIEW_2026-07-27.md)
- [`MANUSCRIPT_ERRATA_2026-07-27.md`](papers/HINC-001/MANUSCRIPT_ERRATA_2026-07-27.md)
- [`FOUNDATIONAL_HOCHSCHILD_DERIVATION_2026-07-27.md`](papers/HINC-001/FOUNDATIONAL_HOCHSCHILD_DERIVATION_2026-07-27.md)
- [`GENERATOR_TO_GLOBAL_LEMMA_2026-07-27.md`](papers/HINC-001/GENERATOR_TO_GLOBAL_LEMMA_2026-07-27.md)
- [`ODD_PRESENTATION_NORMAL_FORM_2026-07-27.md`](papers/HINC-001/ODD_PRESENTATION_NORMAL_FORM_2026-07-27.md)

The pre-review four-part manuscript remains preserved, but it must not be cited without the controlling corrections.

## Central research claim

The repository documents a sustained **human-led, LLM-assisted mathematical workflow** in which:

- the human selected problems, imposed constraints, judged significance, ran release gates, and retained publication authority;
- LLMs proposed directions, algebraic decompositions, proof structures, programs, tests, counterexample searches, literature queries, and editorial revisions;
- Python, C, symbolic systems, Git, GitHub, and Lean tested or formalized bounded claims;
- failures were preserved rather than rewritten as successes;
- internal evidence remains separate from external review and historical priority.

The repository does not claim to be the first human–AI mathematics project. Historical priority for either the process architecture or the mathematics remains unestablished.

## Current paper portfolio

| ID | Working title | Current state |
|---|---|---|
| `HINC-001` | Hidden Infinitesimal Noncommutativity in Two Gerstenhaber Endomorphism Monoids | **Hold — private hostile-review revision** |
| `ABF-001` | Affine-Hyperplane Degree-Drop Spectra of a Vectorial Boolean Map | Hold |
| `FSG-001` | Fibonacci Critical Groups of Carry–Rees Petal Graphs | Hold |
| `ACM-001` | ANF Code and Matroid Geometry of a Reduced Vectorial Map | Hold |

The machine-readable source is [`research-index.json`](research-index.json).

## Evidence vocabulary

| Status | Meaning |
|---|---|
| `candidate theorem` | Precise statement and human proof supplied; external review incomplete. |
| `internally reproduced` | A separate route inside the project agrees; not outside review. |
| `proof-assistant verified` | Only the listed declarations compiled in the pinned environment. |
| `externally reproduced` | An independent person or institution published a reproduction. |
| `peer reviewed` | Accepted through an identified external process. |
| `historical priority established` | A qualified source-level review supports the exact priority boundary. |
| `rejected` | A counterexample or proof failure invalidated the claim as stated. |
| `superseded` | Replaced while preserving the earlier record. |

A commit identifies source. A hash identifies bytes. A finite computation establishes only its declared finite scope. A proof-assistant build establishes only the declarations compiled under the recorded environment.

## What remains before any public release

1. consolidate every HINC erratum into a new manuscript identity;
2. formalize or clearly isolate the new foundation and global-extension proofs;
3. expand representability and group-scheme conventions;
4. complete external algebra/monoid and historical-equivalence review;
5. regenerate and inspect derived artifacts;
6. correct and approve the private website preview;
7. rerun privacy, rights, citation, link, and accessibility gates;
8. obtain a fresh explicit owner release decision.

## Authorship and LLM assistance

Matthew S. Novak is the accountable human author and repository owner. LLMs materially assisted the research. AI systems are not listed as authors, do not own the work, and do not exercise publication authority.

The proposed public wording identifies assistance only at the category level—**LLM-assisted**—without naming a model or provider.

## Rights

No blanket MIT license applies. Manuscripts, code, data, evidence, figures, and formal source may have different terms. Unless a file-specific notice states otherwise:

```text
Copyright © 2026 Matthew S. Novak. All rights reserved.
```

Private access does not grant unrestricted republication or commercial reuse. See [`RIGHTS_AND_LICENSING.md`](RIGHTS_AND_LICENSING.md).

## Review principle

> Inspect the exact statement, proof, source, evidence, and limitations. Provide a counterexample, identify a proof gap, locate earlier equivalent work, or reproduce the result independently.

All four outcomes improve the record.
