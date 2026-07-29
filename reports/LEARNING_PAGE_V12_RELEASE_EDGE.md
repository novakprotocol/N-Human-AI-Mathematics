# Four-path learning page v12 — release-edge integration record

## Purpose

This change adds a public teaching layer for the four-paper portfolio without
changing any paper's publication state.

```text
HINC-001: active candidate public technical review
ABF-001:  active candidate public technical review
FSG-001:  private release edge; public release not authorized
ACM-001:  consolidation hold
```

The learning page is:

```text
docs/learn.html
```

The public landing page links to it and records FSG-001 as a private release
edge rather than a generic hold.

## Source and design decision

The page was distilled from the supplied long-form four-mystery learning design.
The public version retains its strongest teaching mechanisms:

- a hidden-recorder comparison for HINC-001;
- an interactive XOR/restriction toy for ABF-001;
- a resizable two-ring petal with structure and spanning-tree views for FSG-001;
- a 24-position XOR light wall for ACM-001;
- an evidence ladder separating story, example, proof, checks, and outside
  review.

A preliminary compressed-payload transport was rejected after an identity check
found a mismatch. It was not merged. The accepted implementation is one ordinary
line-reviewable HTML file with inline, syntax-checkable JavaScript and no runtime
network dependency.

## FSG-001 boundary

The page may state only the current private release-edge facts:

- the all-parameter human proof surface is internally complete;
- the renewed inside, outside, and hostile reviews passed after correction;
- nine overlapping internal challenge routes are recorded;
- at least 152,891 explicit checks are recorded before strict-C generated
  subchecks;
- zero internal blocking findings remain open;
- clean immutable-head execution, final package/manifest, release-day
  literature delta, and exact package authorization remain unresolved release
  engineering gates.

The page does not expose or link:

- the private `private research source` repository;
- the private FSG branch;
- private manuscript, source, evidence, or review paths;
- a tag, release, DOI, or public theorem package that does not exist.

## Validation

The change includes:

```text
tools/validate_learning_page.py
.github/workflows/validate-learning-page.yml
```

The validator fails closed on:

- missing or contradictory publication-state language;
- any private FSG repository, branch, or source reference;
- duplicate HTML IDs;
- missing four-path navigation;
- missing interactions;
- missing landing-page integration;
- unexpected page size;
- JavaScript syntax failure;
- served bytes differing from committed bytes.

The hosted workflow preserves its JSON receipt, extracted JavaScript, served
page copies, and server log as a 90-day artifact.

## Publication consequence

This is a website/teaching-layer release only. It does not:

- authorize FSG-001 public technical review;
- merge or publish FSG-001 mathematics;
- change repository visibility;
- claim peer review, outside reproduction, complete formal verification, or
  worldwide historical priority;
- alter HINC-001 or ABF-001 immutable release identities.
