# Publication Workflow

N-MathLab remains the private research laboratory. N Human–AI Mathematics receives only curated, self-contained exports.

## Two distinct release tracks

The project separates **public review** from **archival or journal publication**.

```text
private exploration
    ↓
candidate theorem freeze
    ↓
proof and evidence audit
    ↓
clean package export
    ↓
public-source and rights audit
    ↓
owner authorization
    ↓
PUBLIC REVIEW RELEASE
    ↓
outside review, correction, reproduction, priority analysis
    ↓
reviewed archival release / DOI
    ↓
journal submission and peer review
```

A public GitHub repository is not a journal publication. External review is not required merely to ask the public for review, but all unresolved scientific gates must remain visible.

## Gate 1 — Select one controlling result

The paper must have one principal object and one controlling theorem package. Related lemmas may be included; unrelated result stacks remain in N-MathLab.

Required:

- paper identifier;
- working title;
- subject classification;
- one-paragraph contribution statement;
- exact source branch and commit;
- list of superseded internal branches.

## Gate 2 — Make the manuscript self-contained

A reviewer must not need private chat history or another draft branch to understand:

- definitions;
- assumptions;
- theorem statements;
- proof dependencies;
- computational role;
- limitations.

The main proof must be readable independently of test output. A computational classification must define its complete finite universe and enumeration method.

## Gate 3 — Freeze evidence

Every material program, truth table, data file, formal source, and generated report receives an immutable identity. The package records exact commands and environments.

Required evidence files:

```text
EVIDENCE_MAP.md
REPRODUCE.md
receipts/*.json
SHA256SUMS.txt
```

## Gate 4 — Run adversarial controls

At minimum:

- targeted negative tests;
- a known false mutation that the checker rejects;
- an independent implementation or proof route where practical;
- a prior-art equivalence audit;
- a correction-ledger review.

A failed load-bearing control blocks promotion. An operational failure is preserved and classified separately from a mathematical failure.

## Gate 5 — Formalization boundary

Formal proof is not mandatory for public review, but status must be explicit:

```text
not_started
source_written_uncompiled
compiled_for_listed_scope
independently_kernel_checked
full_main_theorem_formalized
```

The paper must name exactly which statements are formalized and which remain prose.

## Gate 6 — Public-source audit

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

## Gate 7 — Human–LLM disclosure

Every released paper must state:

- the accountable human author;
- that one or more LLMs materially assisted, where accurate;
- the material LLM contributions;
- the human decisions and responsibilities;
- the evidence and identity limits;
- whether a specific model or provider is publicly disclosed.

The default public release uses category-level **LLM-assisted** wording. A specific model, model family, version, provider, or vendor may be named only after separate human legal and editorial review and an explicit owner-approved release change.

## Gate 8 — Owner authorization

Only the accountable owner may authorize:

- public visibility;
- named authorship;
- release channel;
- AI-use disclosure level;
- rights and licensing;
- release version;
- residual-risk acceptance.

Technical PASS does not grant release authority.

## Gate 9 — Public review release

A public-review release should contain:

```text
source commit
public-review version
self-contained manuscript source
claim and limitation snapshot
formal-verification boundary
reproduction source
checksums and receipts
human–LLM disclosure
prior-art boundary
rights and third-party notices
open review request
release audit
citation metadata
```

Generated PDF, DOCX, PPTX, and ZIP files normally belong in GitHub Releases rather than repeated in Git history. A source-complete Markdown release may precede polished derived reading artifacts when the status says so explicitly.

## Gate 10 — Public review handling

After public visibility:

1. triage counterexample, proof-gap, prior-art, and reproduction reports;
2. link every substantive report to the affected paper and exact source identity;
3. preserve the original release;
4. publish corrections, narrowed claims, supersessions, or rejections explicitly;
5. never convert silence into external validation.

## Gate 11 — Private or public specialist review

Send one bounded package to the appropriate specialist. Ask specific questions. Do not send the entire N-MathLab history unless requested.

A specialist packet includes:

- manuscript;
- claim matrix;
- prior-art boundary;
- proof map;
- source/reproduction kit;
- formal status;
- review questionnaire.

A reviewer’s identity and conclusion may be published only with an appropriate basis and accurate scope.

## Gate 12 — Archival citation

When the public-review package has reached a suitable checkpoint:

1. freeze an exact release tag;
2. archive it through Zenodo or an equivalent repository;
3. record the DOI in `CITATION.cff` and paper metadata;
4. retain the Git commit, release tag, DOI, and artifact hashes together;
5. update later corrections without rewriting the archived release.

## Gate 13 — Journal submission

Before claiming journal submission:

- verify the selected venue’s AI, authorship, data, code, and preprint policies;
- determine whether a more specific LLM disclosure is legally and editorially appropriate;
- complete the owner’s proof and reference review;
- freeze the exact submitted manuscript and supplements;
- record the venue and submission date only after submission occurs.

Peer-review or acceptance status may be recorded only after the identified external process produces it.

## Source-of-truth rule

Reviewable Markdown, LaTeX, formal source, structured status, and exact evidence control the publication. PDF and DOCX are derived reading artifacts, not the only source of truth.

## One paper at a time

The active public candidate-review packages are `HINC-001` and `ABF-001`. `FSG-001` remains private on HOLD -- MATHEMATICAL BLOCKER with no public theorem package released and no public release authorization. `ACM-001` remains on hold pending consolidation.

The public workflow must demonstrate:

- clean source import;
- validation;
- review issue handling;
- correction handling;
- release packaging;
- accurate citation and status updates.
