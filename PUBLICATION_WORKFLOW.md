# Publication Workflow

N-MathLab remains the private research laboratory. N Human–AI Mathematics receives only curated, self-contained exports.

## Lifecycle

```text
private exploration
    ↓
candidate theorem freeze
    ↓
proof and evidence audit
    ↓
clean-room package export
    ↓
private specialist review
    ↓
formal/reproduction updates
    ↓
owner authorization
    ↓
public repository release
    ↓
DOI/archive and journal submission
```

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

A failed control blocks promotion.

## Gate 5 — Formalization boundary

Formal proof is not mandatory for every paper, but status must be explicit:

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
- chat transcripts;
- reconstructed notes that could be mistaken for contemporaneous notes;
- unsupported reviewer identities;
- duplicate or superseded artifacts;
- license ambiguity;
- promotional claims exceeding status.

## Gate 7 — Private external review

Send one bounded package to the appropriate specialist. Ask specific questions. Do not send the entire N-MathLab history unless requested.

A review packet includes:

- manuscript;
- claim matrix;
- prior-art boundary;
- proof map;
- source/reproduction kit;
- formal status;
- review questionnaire.

## Gate 8 — Human authorization

Only the accountable owner may authorize:

- public visibility;
- named authorship;
- venue selection;
- AI-use disclosure;
- rights and licensing;
- release version;
- residual-risk acceptance.

Technical PASS does not grant release authority.

## Gate 9 — Release

The release should contain:

```text
source tag
source commit
PDF manuscript
source archive
reproducibility archive
checksums
status snapshot
citation metadata
release notes
```

Generated PDF, DOCX, PPTX, and ZIP files normally belong in GitHub Releases rather than repeated in Git history.

## Gate 10 — Archival citation

After public release:

1. archive the exact release through Zenodo or an equivalent repository;
2. record the DOI in `CITATION.cff` and paper metadata;
3. retain the Git commit, release tag, DOI, and artifact hashes together;
4. update later corrections without rewriting the archived release.

## Source-of-truth rule

Reviewable Markdown, LaTeX, formal source, structured status, and exact evidence control the publication. PDF and DOCX are derived reading artifacts, not the only source of truth.

## One paper at a time

The first public package is `HINC-001`. No second paper should be published until the first repository workflow has demonstrated:

- clean source import;
- validation;
- review issue handling;
- correction handling;
- release packaging;
- accurate citation and status updates.
