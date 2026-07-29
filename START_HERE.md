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

# Start Here

## What Is This?

N Human-LLM Mathematics is a curated repository for selected mathematics developed through a **human-led, LLM-assisted** research process.

The accountable human researcher is **Matthew S. Novak**. One or more large language models materially assisted with exploration, candidate theorem formulation, proof decomposition, code and test generation, counterexample search, formal-proof drafting, literature-query design, and publication preparation.

The public source does not identify a specific model, provider, model family, or version.

The repository is public for **candidate technical review**.

## What Public Technical Review Means

Public technical review means the candidate source, evidence, and limitations are open for challenge. It does **not** mean that a paper is:

- peer reviewed;
- journal accepted;
- historically first;
- fully formally verified;
- guaranteed correct;
- endorsed by an AI vendor.

The purpose of going public is to obtain counterexamples, proof-gap reports, earlier-equivalence reports, independent reproductions, and formalization contributions.

## Current Review Targets

`HINC-001` and `ABF-001` are active public candidate technical-review packages.

`HINC-001` has `PARTIAL_PASS` / bounded Lean verification. The full revised manuscript is not fully formalized.

`ABF-001` has `PARTIAL_PASS` / bounded A01 Lean verification. The full manuscript is not fully formalized.

External specialist review, independent reproduction, and historical-priority review remain pending for both. Those are objectives of public release, not completed credentials.

`FSG-001` is private and paused on HOLD -- MATHEMATICAL BLOCKER. No public FSG theorem package has been released, and no public FSG release is authorized.

`ACM-001` is on hold pending consolidation.

## How To Review

1. Read the current status: [`STATUS.md`](STATUS.md).
2. Inspect the paper index: [`RESEARCH_INDEX.md`](RESEARCH_INDEX.md) and [`research-index.json`](research-index.json).
3. For HINC-001, read [`papers/HINC-001/README.md`](papers/HINC-001/README.md), the controlling manuscript, claims, proof map, and formal-verification boundary.
4. For ABF-001, read [`papers/ABF-001/README.md`](papers/ABF-001/README.md), the controlling manuscript, claims, proof map, and formal-verification boundary.
5. For FSG-001, read the public teaching hold: [`FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md`](FSG_001_PUBLIC_TEACHING_HOLD_2026-07-29.md).

## Four Useful Review Outcomes

### Counterexample

Give a concrete object satisfying the assumptions and violating the conclusion.

### Proof Gap

Identify an exact inference that fails, uses an unstated assumption, or exceeds its source.

### Earlier Equivalent Work

Supply the earlier theorem or construction, exact source location, notation translation, and claim-by-claim effect.

### Independent Reproduction

Record the exact source identity, environment, commands, outputs, hashes, independence level, and first discrepancy.

## Status Vocabulary

- **Candidate theorem:** precise statement and human proof supplied; outside review pending.
- **Internally reproduced:** a separate project route agreed; not external validation.
- **Proof-assistant verified:** only the listed declarations compiled in the pinned environment.
- **FULL_PASS:** every retained manuscript claim is covered by compiled Lean and fidelity review. Not currently claimed.
- **No exact indexed match located:** a search result, not worldwide priority.
- **Peer reviewed:** reserved for an identified external peer-review process.

## Release State

```text
repository visibility:              public
active public candidate review:     HINC-001, ABF-001
FSG public theorem package:         not released
FSG public release authorized:      no
ACM state:                          hold pending consolidation
peer reviewed:                      no
historical priority:                unestablished
FULL_PASS manuscripts:              none
```

## One-Sentence Rule

**State the strongest conclusion supported by exact evidence -- never the strongest conclusion that sounds impressive.**