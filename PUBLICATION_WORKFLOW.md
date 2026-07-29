<!--
NHAIM_STATUS_BLOCK_V1
HINC-001:
  paper_id: HINC-001
  public_state: active_review
  formal_state: PARTIAL_PASS
  bounded_formal_scope: bounded_Lean
  claim_map_complete: false
  full_manuscript_lean_verified: false
  external_specialist_review: pending
  historical_priority: not_established
  peer_review: not_submitted
  journal_status: not_submitted
  public_release_authorized: true
ABF-001:
  paper_id: ABF-001
  public_state: active_review
  formal_state: PARTIAL_PASS
  bounded_formal_scope: bounded_A01_Lean
  compiled_lane: A01
  a02_a06_status: incomplete
  claim_map_complete: false
  full_manuscript_lean_verified: false
  external_specialist_review: pending
  historical_priority: not_established
  peer_review: not_submitted
  journal_status: not_submitted
  public_release_authorized: true
FSG-001:
  paper_id: FSG-001
  public_state: hold
  private_candidate: true
  mathematical_blocker: true
  public_theorem_released: false
  correction_status: private_correction_under_internal_review
  external_review: not_started
  formal_status: HOLD_MATHEMATICAL_BLOCKER
  public_release_authorized: false
ACM-001:
  paper_id: ACM-001
  public_state: hold
  manuscript_complete: false
  claim_map_complete: false
  full_manuscript_lean_verified: false
  public_theorem_released: false
  public_release_authorized: false
END_NHAIM_STATUS_BLOCK_V1
-->

# Publication Workflow

the private laboratory remains the private research laboratory. N Humanâ€“AI Mathematics receives only curated, self-contained exports.

## Two distinct release tracks

The project separates **public review** from **archival or journal publication**.

```text
private exploration
    â†“
candidate theorem freeze
    â†“
proof and evidence audit
    â†“
clean package export
    â†“
public-source and rights audit
    â†“
owner authorization
    â†“
PUBLIC REVIEW RELEASE
    â†“
outside review, correction, reproduction, priority analysis
    â†“
reviewed archival release / DOI
    â†“
journal submission and peer review
```

A public GitHub repository is not a journal publication. External review is not required merely to ask the public for review, but all unresolved scientific gates must remain visible.

## Gate 1 â€” Select one controlling result

The paper must have one principal object and one controlling theorem package. Related lemmas may be included; unrelated result stacks remain outside the public review package.

Required:

- paper identifier;
- working title;
- subject classification;
- one-paragraph contribution statement;
- exact source branch and commit;
- list of superseded internal branches.

## Gate 2 â€” Make the manuscript self-contained

A reviewer must not need private chat history or another draft branch to understand:

- definitions;
- assumptions;
- theorem statements;
- proof dependencies;
- computational role;
- limitations.

The main proof must be readable independently of test output. A computational classification must define its complete finite universe and enumeration method.

## Gate 3 â€” Freeze evidence

Every material program, truth table, data file, formal source, and generated report receives an immutable identity. The package records exact commands and environments.

Required evidence files:

```text
EVIDENCE_MAP.md
REPRODUCE.md
receipts/*.json
SHA256SUMS.txt
```

## Gate 4 â€” Run adversarial controls

At minimum:

- targeted negative tests;
- a known false mutation that the checker rejects;
- an independent implementation or proof route where practical;
- a prior-art equivalence audit;
- a correction-ledger review.

A failed load-bearing control blocks promotion. An operational failure is preserved and classified separately from a mathematical failure.

## Gate 5 â€” Formalization boundary

Formal proof is not mandatory for public review, but status must be explicit:

```text
not_started
source_written_uncompiled
compiled_for_listed_scope
independently_kernel_checked
full_main_theorem_formalized
```

The paper must name exactly which statements are formalized and which remain prose.

## Gate 6 â€” Public-source audit

Remove or quarantine:

- private repository URLs not meant for disclosure;
- personal workstation paths;
- secrets, tokens, or private attachments;
- raw private chat transcripts;
- hidden chain-of-thought representations;
- reconstructed notes that could be mistaken for contemporaneous notes;
- unsupported reviewer identities;
- duplicate or superseded artifacts;
- license ambiguity;
- promotional claims exceeding status.

Also review:

- bibliography metadata;
- third-party notices;
- figures and copied prose;
- AI-assistance wording;
- machine-readable release flags;
- withheld model and provider identifiers.

## Gate 7 â€” Humanâ€“LLM disclosure

Every released paper must state:

- the accountable human author;
- that one or more LLMs materially assisted, where accurate;
- the material LLM contributions;
- the human decisions and responsibilities;
- the evidence and identity limits;
- whether a specific model or provider is publicly disclosed.

The default public release uses category-level **LLM-assisted** wording. A specific model, model family, version, provider, or vendor may be named only after separate human legal and editorial review and an explicit owner-approved release change.

## Gate 8 â€” Owner authorization

Only the accountable owner may authorize:

- public visibility;
- named authorship;
- release channel;
- AI-use disclosure level;
- rights and licensing;
- release version;
- residual-risk acceptance.

Technical PASS does not grant release authority.

## Gate 9 â€” Public review release

A public-review release should contain:

```text
source commit
public-review version
self-contained manuscript source
claim and limitation snapshot
formal-verification boundary
reproduction source
checksums and receipts
humanâ€“LLM disclosure
prior-art boundary
rights and third-party notices
open review request
release audit
citation metadata
```

Generated PDF, DOCX, PPTX, and ZIP files normally belong in GitHub Releases rather than repeated in Git history. A source-complete Markdown release may precede polished derived reading artifacts when the status says so explicitly.

## Gate 10 â€” Public review handling

After public visibility:

1. triage counterexample, proof-gap, prior-art, and reproduction reports;
2. link every substantive report to the affected paper and exact source identity;
3. preserve the original release;
4. publish corrections, narrowed claims, supersessions, or rejections explicitly;
5. never convert silence into external validation.

## Gate 11 â€” Private or public specialist review

Send one bounded package to the appropriate specialist. Ask specific questions. Do not send the entire the private laboratory history unless requested.

A specialist packet includes:

- manuscript;
- claim matrix;
- prior-art boundary;
- proof map;
- source/reproduction kit;
- formal status;
- review questionnaire.

A reviewerâ€™s identity and conclusion may be published only with an appropriate basis and accurate scope.

## Gate 12 â€” Archival citation

When the public-review package has reached a suitable checkpoint:

1. freeze an exact release tag;
2. archive it through Zenodo or an equivalent repository;
3. record the DOI in `CITATION.cff` and paper metadata;
4. retain the Git commit, release tag, DOI, and artifact hashes together;
5. update later corrections without rewriting the archived release.

## Gate 13 â€” Journal submission

Before claiming journal submission:

- verify the selected venueâ€™s AI, authorship, data, code, and preprint policies;
- determine whether a more specific LLM disclosure is legally and editorially appropriate;
- complete the ownerâ€™s proof and reference review;
- freeze the exact submitted manuscript and supplements;
- record the venue and submission date only after submission occurs.

Peer-review or acceptance status may be recorded only after the identified external process produces it.

## Source-of-truth rule

Reviewable Markdown, LaTeX, formal source, structured status, and exact evidence control the publication. PDF and DOCX are derived reading artifacts, not the only source of truth.

## One paper at a time

Current portfolio state:

```text
HINC-001  active public candidate technical review; PARTIAL_PASS / bounded Lean verification; full manuscript incomplete
ABF-001   active public candidate technical review; PARTIAL_PASS / bounded A01 Lean verification; full manuscript incomplete
FSG-001   private candidate; HOLD -- MATHEMATICAL BLOCKER; no public theorem package released; no public release authorization
ACM-001   hold pending consolidation; controlling manuscript incomplete; no public release authorization
```

The public workflow must demonstrate:

- clean source import;
- validation;
- review issue handling;
- correction handling;
- release packaging;
- accurate citation and status updates.
