<!--
NHAIM_STATUS_BLOCK_V1
HINC-001:
  public_state: active_review
  formal_state: PARTIAL_PASS
  full_manuscript_lean_verified: false
  external_review: pending
  historical_priority: not_established
  peer_review: not_submitted
  release_authorized: true
ABF-001:
  public_state: active_review
  formal_state: PARTIAL_PASS
  compiled_lane: A01
  a02_a06_status: incomplete
  full_manuscript_lean_verified: false
  external_review: pending
  historical_priority: not_established
  peer_review: not_submitted
  release_authorized: true
FSG-001:
  public_state: hold
  private_candidate: true
  mathematical_blocker: true
  public_theorem_package_released: false
  release_authorized: false
ACM-001:
  public_state: hold
  controlling_manuscript_complete: false
  release_authorized: false
END_NHAIM_STATUS_BLOCK_V1
-->

# N Human-LLM Mathematics

**Human-led, LLM-assisted mathematical research open for public candidate technical review.**

This repository curates selected mathematics developed through sustained work led by **Matthew S. Novak** with material assistance from one or more large language models. It preserves exact claims, human proofs, programs, bounded formal checks, failed attempts, corrections, status records, rights boundaries, and review instructions.

The repository is public for candidate technical review. Public visibility opens the work to challenge; it does not establish peer review, journal acceptance, worldwide priority, outside reproduction, or complete formal verification.

```text
repository:                      novakprotocol/N-Human-AI-Mathematics
visibility:                      public
public-review release:           0.1.0-public-review
active public candidate review:  HINC-001, ABF-001
fully Lean-verified manuscripts: none
FSG-001:                         private; HOLD -- MATHEMATICAL BLOCKER
ACM-001:                         hold pending consolidation
accountable human:               Matthew S. Novak
specific model/provider:         not disclosed
peer reviewed:                   no
journal submitted:               no
DOI:                             none
blanket license applied:         no
```

## Current Status

- `HINC-001` is in **active public candidate technical review**. Its formal status is `PARTIAL_PASS` / bounded Lean verification. The full manuscript is not fully formalized. External review is pending, and historical priority is unestablished.
- `ABF-001` is in **active public candidate technical review**. Its formal status is `PARTIAL_PASS` / bounded A01 Lean verification. The full manuscript is not fully formalized. External review is pending, and historical priority is unestablished.
- `FSG-001` is private and paused on **HOLD -- MATHEMATICAL BLOCKER**. C06 / main theorem item (v) is false as written in the private candidate manuscript. No public FSG theorem package has been released, and no public FSG release is authorized.
- `ACM-001` is on hold pending consolidation.

PR #57 is preserved, but its interpretation that HINC-001 and ABF-001 became inactive historical artifacts is superseded by the 29 July 2026 owner clarification.

## Read This First

| Reader | Start here | Purpose |
|---|---|---|
| General reader | [`START_HERE.md`](START_HERE.md) | Understand the project, its status, and its limits. |
| Research index reader | [`RESEARCH_INDEX.md`](RESEARCH_INDEX.md) and [`research-index.json`](research-index.json) | Inspect the paper order and current machine-readable status. |
| Formal methods reviewer | [`formal-verification-status.json`](formal-verification-status.json) | See exactly what is bounded `PARTIAL_PASS` and what is not `FULL_PASS`. |
| HINC reviewer | [`papers/HINC-001/README.md`](papers/HINC-001/README.md) | Review the first active candidate package. |
| ABF reviewer | [`papers/ABF-001/README.md`](papers/ABF-001/README.md) | Review the second active candidate package. |
| FSG status reader | [`FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md`](FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md) | Read the public teaching-hold correction. |
| LLM system | [`AGENTS.md`](AGENTS.md) | Read the machine-facing interpretation rules. |

The public technical-review site is published from [`docs/`](docs/) at https://novakprotocol.github.io/N-Human-AI-Mathematics/.

## HINC-001

**Working title:** *Hidden Infinitesimal Noncommutativity in Two Binary-Gerstenhaber Endomorphism Monoid Schemes*

HINC-001 is an active public candidate technical-review package. The consolidated human candidate manuscript is complete within its stated scope. Bounded Lean verification passes for the algebraic kernel and coefficient classifications; the full revised manuscript is not fully formalized.

## ABF-001

**Title:** *Affine Restriction Moment Kernels and Radical Incidence Geometry of a Vectorial Boolean Map*

ABF-001 is an active public candidate technical-review package. Its exact public-review package records the specified finite classification and supporting evidence. A bounded A01 Lean lane passes; A02-A06 and the complete manuscript are not fully formalized.

The immutable candidate release is [`abf-001-public-review-v1`](https://github.com/novakprotocol/N-Human-AI-Mathematics/releases/tag/abf-001-public-review-v1).

## Paper Order

| Order | ID | Current state |
|---:|---|---|
| 1 | `HINC-001` | Active candidate public technical review; `PARTIAL_PASS` bounded Lean |
| 2 | `ABF-001` | Active candidate public technical review; `PARTIAL_PASS` bounded A01 Lean |
| 3 | `FSG-001` | Private candidate; HOLD -- MATHEMATICAL BLOCKER |
| 4 | `ACM-001` | Hold pending consolidation |

## Evidence Vocabulary

| Status | Meaning |
|---|---|
| `candidate theorem` | A precise statement and human proof are supplied; outside review remains pending. |
| `internally reproduced` | A separate route inside the project agrees; this is not external review. |
| `proof-assistant verified` | Only the listed declarations compiled in the pinned environment. |
| `FULL_PASS` | Every retained manuscript claim is covered by compiled Lean and fidelity review. Not currently claimed. |
| `externally reproduced` | An independent person or institution published a reproduction. Not currently claimed. |
| `peer reviewed` | An identified external peer-review process completed. Not currently claimed. |
| `historical priority established` | A qualified source-level review supports the exact priority statement. Not currently claimed. |

A commit identifies source. A hash identifies bytes. A finite computation establishes only its declared finite scope. A proof-assistant build establishes only the declarations compiled under the recorded environment.

## Human + LLM Boundary

Matthew S. Novak is the accountable human author, repository owner, and release authority. AI systems are not listed as authors, do not own the work, and do not exercise publication authority. The public source does not identify a specific model or provider.

## Rights

No blanket MIT license applies. Manuscripts, code, data, evidence, figures, and formal source may have different terms. Unless a file-specific notice states otherwise:

```text
Copyright (c) 2026 Matthew S. Novak. All rights reserved.
```

See [`RIGHTS_AND_LICENSING.md`](RIGHTS_AND_LICENSING.md).

> Inspect the exact statement, proof, source, evidence, and limitations. Provide a counterexample, identify a proof gap, locate earlier equivalent work, or reproduce the result independently.