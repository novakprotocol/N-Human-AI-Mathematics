## Purpose

Integrate the already tagged and released ABF-001 candidate technical-review package into the public repository index.

## Immutable release dependency

This PR must reference an existing successful release:

```text
tag:                         abf-001-public-review-v1
mathematical source commit:  45dbf87cb4a46dcbbce690da7a22cdd7f88cb052
release target:              candidate public technical review
```

The release workflow records the generated professional-package hash, frozen-Git-source hash, complete manifest hash, release attestation, and validation artifacts.

## Gate status

- complete human proof: PASS;
- exact finite classification: PASS;
- primary implementation: PASS;
- separate integer/bitset implementation: PASS;
- strict-C 5,505,024-comparison exhaustive control: PASS;
- one-bit tamper control: PASS;
- hostile review blockers: 0;
- prior-art search to declared scope: PASS;
- final same-day delta: PASS;
- package-specific owner authorization: PASS;
- historical priority: unestablished;
- external reproduction: pending;
- proof-assistant formalization: not completed;
- peer review: not completed.

## Repository changes

- add `papers/ABF-001/` with controlling manuscript, proof map, source, tests, evidence, rights, disclosure, review, and literature records;
- promote ABF-001 from HOLD/index-only to `active_review`;
- replace the ABF publication-gate HOLD receipt with a PASS receipt bound to the immutable release;
- update repository README, research index, and status records;
- leave HINC-001 source, tag, release, receipts, and claim status unchanged;
- make no `docs/` website change.

## Website boundary

The public website update is deliberately excluded. A rendered preview will be shown to Matthew S. Novak before any `docs/` commit.
