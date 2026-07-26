# Evidence Standard

An evidence record must let a later reviewer reconstruct **what was checked, against which exact identity, by which method, in which environment, with what result, and under what limitations**.

## Required fields

| Field | Required content |
|---|---|
| Subject | Paper ID, theorem ID, repository, exact commit, source paths, and relevant artifact hashes. |
| Method | Exact command, proof route, solver, test population, and stopping rule. |
| Environment | Tool versions, operating system, runtime, compiler, proof assistant, and material hardware. |
| Result | Counts, outputs, failures, logs, generated artifacts, and timestamps. |
| Decision | Pass, fail, blocked, informational, superseded, or rejected. |
| Limitations | What was not checked and which stronger claims remain unsupported. |

## Identity rules

- A Git commit identifies a source tree.
- A SHA-256 value identifies file bytes.
- A semantic version communicates intended compatibility but does not uniquely identify bytes.
- A workflow run identifies an execution event but not necessarily the intended source unless checkout identity is verified.
- A proof-assistant version and dependency lock are part of proof identity.

## Evidence types

### Human proof

Record the exact manuscript commit and proof dependency map. State any externally imported lemmas and their assumptions.

### Exhaustive finite computation

Record the complete finite domain, enumeration method, candidate count, deduplication rules, expected invariants, and independent reconstruction where practical.

### Statistical experiment

Record population selection, sample size, seeds, metrics, multiple-testing treatment, holdouts, baselines, and uncertainty. Statistical evidence must not be restated as exact proof.

### Independent implementation

An independent implementation should avoid importing the primary result or its expected answer. The record must explain what structural independence was achieved and what assumptions remain shared.

### Proof-assistant build

Record:

```text
proof assistant and version
dependency revisions
exact source commit
build command
compiled declarations
placeholder policy
axiom report
workflow run and job
artifact identity
scope explicitly excluded
```

A successful build verifies only the formalized declarations.

## Failure preservation

A failed or blocked run is evidence. Preserve:

- the exact failed source;
- command and environment;
- logs and exit state;
- whether failure was mathematical, implementation, infrastructure, or inconclusive;
- the later correction as a separate event.

Never overwrite a failed receipt with a passing receipt under the same identity.

## Minimum machine-readable receipt

```json
{
  "schema_version": "n.human_ai_math.evidence_receipt.v1",
  "subject": {
    "paper_id": "HINC-001",
    "source_commit": "<40 hex>"
  },
  "method": {
    "command": "lake build",
    "environment": "Lean 4.30.0; Mathlib v4.30.0"
  },
  "result": "PASS",
  "observations": {},
  "limitations": [
    "full manuscript not formalized",
    "historical priority not established"
  ]
}
```

## Interpretation rule

**Evidence is always local to the declared source, method, environment, and scope.**
