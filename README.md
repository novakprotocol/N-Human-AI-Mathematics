# N Human–LLM Mathematics

**Human-led, LLM-assisted mathematical research open for public technical review.**

This repository curates selected mathematics developed through sustained work led by **Matthew S. Novak** with material assistance from one or more **large language models**. It preserves exact claims, human proofs, programs, bounded formal checks, failed attempts, corrections, status records, rights boundaries, and review instructions.

The repository is public for candidate technical review. Public visibility opens the work to challenge; it does not establish peer review, journal acceptance, worldwide priority, outside reproduction, or complete formal verification.

```text
repository:                 novakprotocol/N-Human-AI-Mathematics
visibility:                 public
public-review release:      0.1.0-public-review
public review active:       true
visibility switch executed: true
accountable human:          Matthew S. Novak
LLM role:                   material research assistance
specific model/provider:    not disclosed
peer reviewed:              no
journal submitted:          no
DOI:                        none
blanket license applied:    no
```

## Read this first

| Reader | Start here | Purpose |
|---|---|---|
| General reader | [`START_HERE.md`](START_HERE.md) | Understand the project, its status, and its limits. |
| Mathematician | [`papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md`](papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md) | Read the controlling candidate manuscript. |
| Proof auditor | [`papers/HINC-001/CLAIMS.md`](papers/HINC-001/CLAIMS.md) and [`papers/HINC-001/PROOF_MAP.md`](papers/HINC-001/PROOF_MAP.md) | Inspect claim-by-claim and dependency status. |
| Formal methods reviewer | [`papers/HINC-001/FORMAL_VERIFICATION.md`](papers/HINC-001/FORMAL_VERIFICATION.md) | See exactly what Lean verifies and what it does not. |
| Reproducer | [`papers/HINC-001/REPRODUCE.md`](papers/HINC-001/REPRODUCE.md) | Run the declared source and report the first discrepancy. |
| Historical-priority reviewer | [`papers/HINC-001/PRIOR_ART.md`](papers/HINC-001/PRIOR_ART.md) | Compare the result against established frameworks and search records. |
| Release reviewer | [`PUBLIC_SWITCH_READINESS.md`](PUBLIC_SWITCH_READINESS.md) | Inspect the final pre-publication gates and switch procedure. |
| LLM system | [`AGENTS.md`](AGENTS.md) | Read the machine-facing interpretation rules. |

The public technical-review site is published from [`docs/`](docs/) at https://novakprotocol.github.io/N-Human-AI-Mathematics/.

## HINC-001

**Working title:** *Hidden Infinitesimal Noncommutativity in Two Binary-Gerstenhaber Endomorphism Monoid Schemes*

The controlling candidate manuscript classifies binary-Gerstenhaber endomorphisms of two explicit characteristic-two subalgebras of the Hochschild cohomology of the dual numbers.

Its paired structural result is:

```text
even: common crossing + constrained skew square-zero direction
odd:  common crossing + separate clopen torus unit component
```

The manuscript now integrates the complete human proof route, including:

- the characteristic-two normalized Hochschild calculation;
- complete presentations of both source algebras;
- the odd normal-form proof;
- the generator-to-global biderivation lemma;
- explicit natural representability;
- corrected center and disconnected-base language;
- the fppf-derived-subgroup argument;
- exact evidence and novelty boundaries.

### Evidence status

| Layer | Status |
|---|---|
| Consolidated self-contained human manuscript | Complete candidate source |
| Internal Python/C/Gröbner/Artin/common-core routes | Passed for declared scopes |
| Lean algebraic kernel | Public hosted PASS |
| Lean coefficient classifications | Public hosted PASS |
| Full revised manuscript Lean proof | Not completed and not claimed |
| External specialist review | Pending; requested by public release |
| Independent external reproduction | Pending; requested by public release |
| Historical priority | Unestablished |
| Peer review | Not submitted |

Public visibility is intended to obtain the pending outside review. It does not pretend that review has already happened.


## ABF-001

**Title:** *Affine Restriction Moment Kernels and Radical Incidence Geometry of a Vectorial Boolean Map*

ABF-001 supplies a self-contained moment-kernel theorem and a complete finite classification of a specified `GF(2)^16 -> GF(2)^8` map. Its exact public-review package records the `130,559 / 511 / 0` restriction spectrum, corrected `203 / 202` radical distinction, 469-edge incidence atlas, independent implementations, complete finite controls, hostile review, and bounded prior-art conclusion.

Start with [`papers/ABF-001/README.md`](papers/ABF-001/README.md). The immutable candidate release is [`abf-001-public-review-v1`](https://github.com/novakprotocol/N-Human-AI-Mathematics/releases/tag/abf-001-public-review-v1).

## Paper order

| Order | ID | State at first public launch |
|---:|---|---|
| 1 | `HINC-001` | Complete candidate technical-review package |
| 2 | `ABF-001` | Complete candidate technical-review package |
| 3 | `FSG-001` | Hold |
| 4 | `ACM-001` | Hold pending consolidation |

The machine-readable source is [`research-index.json`](research-index.json).

## Human + LLM boundary

Matthew S. Novak is the accountable human author, repository owner, and release authority. One or more LLMs materially assisted with exploration, proof development, code and test generation, counterexample search, formalization support, evidence design, and editorial work.

AI systems are not listed as authors, do not own the work, and do not exercise publication authority. The public source does not identify a specific model or provider.

The repository does not claim to be the first human–AI mathematics project.

## Evidence vocabulary

| Status | Meaning |
|---|---|
| `candidate theorem` | A precise statement and human proof are supplied; outside review remains pending. |
| `internally reproduced` | A separate route inside the project agrees; this is not external review. |
| `proof-assistant verified` | Only the listed declarations compiled in the pinned environment. |
| `externally reproduced` | An independent person or institution published a reproduction. |
| `peer reviewed` | An identified external peer-review process completed. |
| `historical priority established` | A qualified source-level review supports the exact priority statement. |

A commit identifies source. A hash identifies bytes. A finite computation establishes only its declared finite scope. A proof-assistant build establishes only the declarations compiled under the recorded environment.

## Public technical-review status

HINC-001 and ABF-001 are active candidate packages. Counterexamples, proof-gap reports, prior-art equivalence reports, independent reproductions, and further formalization are invited. External review remains pending until an identified outside process completes it.

See [`PUBLIC_SWITCH_READINESS.md`](PUBLIC_SWITCH_READINESS.md).

## Rights

No blanket MIT license applies. Manuscripts, code, data, evidence, figures, and formal source may have different terms. Unless a file-specific notice states otherwise:

```text
Copyright © 2026 Matthew S. Novak. All rights reserved.
```

See [`RIGHTS_AND_LICENSING.md`](RIGHTS_AND_LICENSING.md).

> Inspect the exact statement, proof, source, evidence, and limitations. Provide a counterexample, identify a proof gap, locate earlier equivalent work, or reproduce the result independently.
