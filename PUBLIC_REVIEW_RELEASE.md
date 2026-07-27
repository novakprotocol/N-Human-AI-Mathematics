# Public Review Release

## Release identity

```text
release channel:            public review
version:                    0.1.0-public-review
release date:               2026-07-27
repository:                 novakprotocol/N-Human-AI-Mathematics
accountable owner:          Matthew S. Novak
public visibility:          authorized by owner
AI assistance:              one or more large language models
specific model disclosed:   no
specific provider disclosed:no
blanket license:            none
DOI:                        not assigned
journal submission:         not initiated
peer-review status:         not peer reviewed
historical priority:        unestablished
```

## Purpose

This release opens a bounded mathematical research record for public inspection, reproduction, correction, and prior-art review.

It documents a sustained human-led, LLM-assisted workflow and releases the first complete paper package, `HINC-001`. It does not present every result from the private N-MathLab laboratory.

## Released paper package

### HINC-001

**Title:** *Hidden Infinitesimal Noncommutativity in Endomorphism Monoids of Two Graded Gerstenhaber Algebras*

**Release status:** public candidate theorem package.

Included:

- self-contained manuscript source;
- plain-language explanation;
- claim and proof maps;
- formal-verification scope;
- Python verifier and tests;
- deterministic evidence and receipts;
- prior-art boundary;
- review request;
- human–LLM disclosure;
- rights and third-party notices.

Established internal evidence includes two bounded public Lean build scopes: the base algebraic kernel and the principal coefficient classifications. The complete manuscript is not formally verified, and qualified external mathematical review remains pending.

## Indexed but not released as complete packages

The following lines remain visible only as research-index entries:

- `ABF-001` — standalone public package pending;
- `FSG-001` — standalone public package pending;
- `ACM-001` — consolidation and standalone public package pending.

Their index entries are not substitutes for complete manuscripts or releases.

## Public-source audit

Before this release, the repository is checked for:

- personal workstation paths;
- credential and private-key patterns;
- accidental blanket-license language;
- private chat transcripts;
- hidden chain-of-thought representations;
- specific model and provider identifiers;
- unsupported global-novelty or peer-review claims;
- required paper status, rights, evidence, and disclosure files;
- bibliographic consistency for the materialized HINC reference list;
- third-party figures or copied extended prose.

The release gate fails if a withheld model or provider name appears anywhere in the public tree. This is a bounded audit, not a guarantee that no issue can ever be discovered.

The machine-readable audit is stored in:

```text
reports/public-release-audit-2026-07-27.json
```

## Human–LLM claim boundary

The release establishes a public case study of collaboration between Matthew S. Novak and one or more large language models. It does not claim the first human–AI mathematical collaboration. Earlier acknowledged examples are recorded in `HUMAN_AI_MATHEMATICS_PRIOR_ART.md`.

The project-specific process claim is narrower:

> The repository combines sustained human direction and material LLM assistance with commit-anchored sources, machine-readable claim limits, executable evidence, preserved failures and corrections, bounded formal checks, and public adversarial-review channels.

Historical priority for that exact combination remains unestablished.

## Identity and legal-review boundary

The public repository identifies the assistance only at the category level: **LLM-assisted**.

It does not identify a particular model, model family, version, provider, or vendor. A more specific disclosure may be added later only after separate human legal and editorial review and an explicit owner-approved release change.

## Rights

Public visibility permits reading and review. It does not create a blanket open-source or open-content license.

Unless a file-specific notice states otherwise:

```text
Copyright © 2026 Matthew S. Novak. All rights reserved.
```

See `RIGHTS_AND_LICENSING.md` and each paper’s terms files.

## Known unresolved gates

- external algebra/monoid specialist review;
- source-level historical-equivalence review of HINC-001;
- generator-to-global formalization;
- remaining scheme-level formalization;
- outside reproduction;
- DOI/archive release;
- journal submission.

These gates remain visible after public release; public visibility is intended to help satisfy them.

## Owner decision

Matthew S. Novak explicitly authorized this public-review release on 27 July 2026 using **Human + LLM** category wording. The authorization covers public repository visibility and the release language above. It does not convert pending scientific gates into completed ones and does not authorize a specific model/provider disclosure.

## Correction policy

Any substantive defect will be linked to the affected source identity and classified. The repository will preserve the earlier state and publish a correction, narrowing, supersession, or rejection rather than silently rewriting the historical record.
