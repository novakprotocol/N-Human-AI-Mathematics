# ABF-001 — Affine Restriction Moment Kernels

## Full working title

**Affine Restriction Moment Kernels and Radical Incidence Geometry of a Vectorial Boolean Map**

```text
candidate version:           0.1.0-public-review
release state:               active immutable candidate public-review release
public technical review:     active
release tag:                 abf-001-public-review-v1
release date:                2026-07-28
peer reviewed:               no
journal submitted:           no
DOI:                         none
LLM disclosure:              human-led, LLM-assisted
specific model/provider:     not disclosed
```

## Controlling source

- [`manuscript/ABF-001_MANUSCRIPT.md`](manuscript/ABF-001_MANUSCRIPT.md)

The manuscript consolidates and supersedes the earlier v30 affine-hyperplane note and the later v32 radical-incidence note for public-review purposes.

## Immutable release identity

```text
mathematical source commit:  45dbf87cb4a46dcbbce690da7a22cdd7f88cb052
release-control commit:      4afb398aeb0dbb937c1a0fa38e38c370cc5b999b
release tag:                 abf-001-public-review-v1
publication gate:            PASS_PUBLIC_TECHNICAL_REVIEW
```

The complete package, source-package, and manifest hashes are recorded in
[`../../reports/publication-gates/ABF-001.json`](../../reports/publication-gates/ABF-001.json).

## Start here by audience

| Audience | Document |
|---|---|
| General reader | [`PLAIN_LANGUAGE.md`](PLAIN_LANGUAGE.md) |
| Mathematical reader | [`manuscript/ABF-001_MANUSCRIPT.md`](manuscript/ABF-001_MANUSCRIPT.md) |
| Claim auditor | [`CLAIMS.md`](CLAIMS.md) |
| Proof reviewer | [`PROOF_MAP.md`](PROOF_MAP.md) |
| Reproducer | [`REPRODUCE.md`](REPRODUCE.md) |
| Prior-art reviewer | [`PRIOR_ART.md`](PRIOR_ART.md) |
| External referee | [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md) |
| Machine reader | [`STATUS.json`](STATUS.json), [`SOURCE_MANIFEST.json`](SOURCE_MANIFEST.json) |

## Current evidence

| Dimension | Status |
|---|---|
| Consolidated manuscript | Complete candidate source |
| Human proof | Self-contained; outside audit pending |
| Fresh NumPy verifier | PASS |
| Separate integer/bitset verifier | PASS |
| Edge-atlas identity | `95d64917af27fa1b827bda0b82364dc6e69de6376ccb0ad81e12ab22b82742fa` |
| Historical C reconstruction | PASS; byte-identical edge atlas |
| Exhaustive small-universe controls | 5,505,024 checks; 0 mismatches |
| Formal verification | Not completed |
| External reproduction | Pending |
| Historical priority | Unestablished |
| Public technical review | Active |

## Safe public claim

> ABF-001 gives a self-contained moment-kernel certificate for affine restriction degree drops and a complete exact finite classification for a specified 16-to-8 vectorial Boolean map. The finite results are independently implemented inside the project. External correctness review, proof-assistant verification, and historical priority remain pending.

## Completed candidate controls

- expanded prior-art and equivalence-search protocol and query ledger;
- complete 5,505,024-comparison small-universe control;
- one-bit truth-table tamper rejection;
- final clean-copy execution receipt;
- release-candidate hostile review and same-day delta search recorded after source freeze;
- immutable tag, release assets, source manifest, and publication-gate PASS receipt.
