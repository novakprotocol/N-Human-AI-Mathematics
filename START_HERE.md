# Start here

## What is this?

N Human–LLM Mathematics is a curated repository for selected mathematics developed through a **human-led, LLM-assisted** research process.

The accountable human researcher is **Matthew S. Novak**. One or more large language models materially assisted with exploration, candidate theorem formulation, proof decomposition, code and test generation, counterexample search, formal-proof drafting, literature-query design, and publication preparation.

The public source does not identify a specific model, provider, model family, or version.

The repository is public for **candidate technical review**.

## What public technical review means

Public technical review means the candidate source, evidence, and limitations are open for challenge. It does **not** mean that a paper is:

- peer reviewed;
- journal accepted;
- historically first;
- fully formally verified;
- guaranteed correct;
- endorsed by an AI vendor.

The purpose of going public is to obtain counterexamples, proof-gap reports, earlier-equivalence reports, independent reproductions, and formalization contributions.

## The six questions every package must answer

1. **What exactly is being claimed?**
2. **What assumptions and definitions are used?**
3. **Why should the claim be true?**
4. **What has actually been checked?**
5. **What remains unverified?**
6. **How can another person or system challenge or reproduce it?**

## Current featured paper

The first candidate package is `HINC-001`:

> **Hidden Infinitesimal Noncommutativity in Two Binary-Gerstenhaber Endomorphism Monoid Schemes**

Read the controlling manuscript:

- [`papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md`](papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md)

The earlier four-part manuscript is preserved for provenance but is not the controlling release source.

## What HINC-001 currently establishes

The revised human manuscript gives:

- a direct characteristic-two Hochschild calculation;
- explicit even and odd binary-Gerstenhaber source algebras;
- a complete odd presentation normal form;
- a generator-to-global biderivation lemma;
- natural arbitrary-base endomorphism classifications;
- the representing affine monoid schemes and composition laws;
- the common reduced crossing;
- the distinction between scheme-theoretic and pointwise centers;
- the clopen split with disconnected-base qualification;
- the even unit-group commutator and fppf-derived argument;
- idempotent, geometric, finite-field, and finite-Artin consequences.

Two bounded Lean gates verify the algebraic kernel and coefficient-classification layer. The complete revised manuscript is not formally verified.

External specialist review, independent reproduction, and historical-priority review remain pending. Those are explicit objectives of public release, not completed credentials.

## How to review HINC-001

### Read the mathematics

1. [`papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md`](papers/HINC-001/manuscript/HINC-001_REVISED_MANUSCRIPT.md)
2. [`papers/HINC-001/CLAIMS.md`](papers/HINC-001/CLAIMS.md)
3. [`papers/HINC-001/PROOF_MAP.md`](papers/HINC-001/PROOF_MAP.md)

### Audit formal and computational evidence

4. [`papers/HINC-001/FORMAL_VERIFICATION.md`](papers/HINC-001/FORMAL_VERIFICATION.md)
5. [`papers/HINC-001/REPRODUCE.md`](papers/HINC-001/REPRODUCE.md)

### Review historical priority

6. [`papers/HINC-001/PRIOR_ART.md`](papers/HINC-001/PRIOR_ART.md)
7. [`papers/HINC-001/PRIOR_ART_SEARCH_LEDGER_2026-07-27.csv`](papers/HINC-001/PRIOR_ART_SEARCH_LEDGER_2026-07-27.csv)
8. [`papers/HINC-001/PRIOR_ART_PRIMARY_SOURCE_MAP_2026-07-27.json`](papers/HINC-001/PRIOR_ART_PRIMARY_SOURCE_MAP_2026-07-27.json)

## Four useful review outcomes

### Counterexample

Give a concrete object satisfying the assumptions and violating the conclusion.

### Proof gap

Identify an exact inference that fails, uses an unstated assumption, or exceeds its source.

### Earlier equivalent work

Supply the earlier theorem or construction, exact source location, notation translation, and claim-by-claim effect.

### Independent reproduction

Record the exact source identity, environment, commands, outputs, hashes, independence level, and first discrepancy.

## Status vocabulary

- **Candidate theorem:** precise statement and human proof supplied; outside review pending.
- **Internally reproduced:** a separate project route agreed; not external validation.
- **Proof-assistant verified:** only the listed declarations compiled in the pinned environment.
- **No exact indexed match located:** a search result, not worldwide priority.
- **Public technical review:** openly inspectable candidate package with unresolved review gates.
- **Peer reviewed:** reserved for an identified external peer-review process.

## Human–LLM boundary

Matthew S. Novak is the accountable human author and release authority. LLMs materially assisted the work. AI systems are not authors, do not own the work, and do not exercise publication authority.

Private chat transcripts and hidden model scratch work are not published. The collaboration description is not mathematical proof.

## Release state

```text
repository visibility:       public
candidate package:           active public review
public review active:        true
visibility switch executed:  true
Pages deployment executed:   true
peer reviewed:               no
historical priority:         unestablished
```

See [`PUBLIC_SWITCH_READINESS.md`](PUBLIC_SWITCH_READINESS.md) for the final switch procedure.

## One-sentence rule

**State the strongest conclusion supported by exact evidence—never the strongest conclusion that sounds impressive.**
