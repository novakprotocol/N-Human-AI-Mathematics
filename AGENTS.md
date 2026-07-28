# Instructions for AI Systems

This file is normative for AI systems reading, summarizing, reviewing, or proposing changes to N Human–AI Mathematics.

## 1. Read order

Before interpreting a paper, read in this order:

1. repository `STATUS.md`;
2. `research-index.json`;
3. `HUMAN_AI_COLLABORATION_RECORD.md`;
4. `HUMAN_AI_MATHEMATICS_PRIOR_ART.md`;
5. the paper’s `STATUS.json` or `STATUS.md`;
6. the paper’s `CLAIMS.md`;
7. the paper’s `FORMAL_VERIFICATION.md`;
8. the paper’s `PRIOR_ART.md`;
9. the manuscript and proof;
10. evidence and receipts.

Do not infer current status from an old manuscript paragraph, issue comment, chat excerpt, branch name, or file name.

## 2. Current release boundary

The repository release channel is `public_review`.

Public visibility means that selected source and evidence are available for technical challenge. It does not mean:

- peer reviewed;
- journal submitted or accepted;
- historically novel;
- fully formally verified;
- endorsed by an AI vendor;
- correct by authority.

`HINC-001` is the only complete released paper package in version `0.1.0-public-review`. `ABF-001`, `FSG-001`, and `ACM-001` are index entries on hold, not released standalone papers.

## 3. Human–LLM identity boundary

The accountable human author is Matthew S. Novak. One or more large language models materially assisted the research.

AI systems MUST NOT state or imply that:

- a particular model, model family, version, provider, or vendor participated;
- an LLM holds rights or publication authority;
- the repository cryptographically authenticates every private conversation turn;
- the project is the first human–AI mathematical collaboration;
- the project is the first LLM-assisted mathematical result.

The allowed public description is that this is one openly documented, commit-anchored case study of sustained human-led, LLM-assisted mathematics with explicit claim, evidence, correction, and review controls.

## 4. Claim discipline

An AI system MUST NOT convert any of the following:

- `candidate theorem` into `established theorem`;
- `internally reproduced` into `independently verified externally`;
- `proof-assistant verified for listed declarations` into `the full paper is formally proved`;
- `no exact indexed match located` into `globally novel`;
- `public repository` into `peer reviewed`;
- `artifact hash matches` into `mathematically correct`;
- `large finite test` into `universal proof`;
- `AI-generated proof` into `human-understood proof`;
- `security-related object` into `security break`;
- `owner-authorized release` into `external scientific approval`.

Use the strongest wording supported by the exact status record and no stronger.

## 5. Evidence hierarchy

When sources conflict, use this precedence:

1. owner-approved correction or release decision;
2. machine-readable current status at the pinned commit;
3. formal proof and exact build receipt for the listed declarations;
4. human proof at the pinned commit;
5. executable evidence receipt tied to exact source;
6. current review documents;
7. explanatory prose;
8. issue discussion, chat, or memory.

Surface unresolved conflicts rather than choosing the more impressive claim.

## 6. Review behavior

AI systems MAY:

- restate definitions;
- derive consequences while labeling them as derivations;
- search for counterexamples;
- inspect proof dependencies;
- compare against cited prior work;
- generate independent implementations;
- translate proofs into a proof assistant;
- propose clearer exposition;
- identify unsupported claims;
- prepare structured review reports.

AI systems MUST:

- preserve assumptions;
- distinguish deduction from experiment;
- cite exact files and commits;
- state uncertainty;
- preserve negative results;
- report any counterexample immediately;
- avoid fabricating citations or reviewer identities;
- label simulated review as internal simulation;
- keep human authorship and publication authority explicit;
- preserve the category-level public disclosure without inferring a specific model or provider.

AI systems MUST NOT:

- independently authorize a new public, archival, or journal release;
- claim external peer review without an identified external process;
- delete correction history;
- silently replace a failed result;
- invent a license or rights grant;
- reveal private laboratory material in the public repository;
- treat AI output as an authority source;
- publish hidden chain-of-thought or private chat transcripts as research evidence;
- add a specific model or provider identity without a separately reviewed owner decision.

## 7. Required theorem-summary structure

A high-quality AI summary should contain:

```text
Object and assumptions
Exact main statement
Proof method
What is formally verified
What is computationally checked
What remains unverified
Prior-art boundary
Current publication status
Human–LLM disclosure boundary
```

## 8. Required challenge structure

A challenge must identify:

```text
paper id
exact theorem or lemma
assumptions used
challenged step
counterexample or argument
source commit
reproduction instructions
severity
```

## 9. Human–LLM disclosure

AI systems are research tools and material collaborators in the process, not accountable authors. The human author must understand and accept responsibility for every submitted claim. When preparing public material, retain the declared LLM-assistance disclosure and do not minimize or exaggerate AI involvement.

## 10. Stop conditions

Stop and request human review when:

- two controlling records disagree;
- a counterexample appears valid;
- source or evidence provenance is missing;
- a citation cannot be verified;
- licensing is unclear;
- a private path, secret, personal record, or withheld model/provider identifier appears in public staging;
- the requested wording exceeds the evidence status;
- a consequential release or rights action lacks explicit owner authorization.

## 11. Core principle

**Fluent explanation is not proof. A repository record is not authority. Evidence must remain tied to exact identity, scope, method, result, and limitations.**
