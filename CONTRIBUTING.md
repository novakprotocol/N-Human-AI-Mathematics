# Contributing

Contributions are welcome when they improve correctness, reproducibility, clarity, equivalence review, or formal coverage.

## Best contributions

- explicit counterexamples;
- precise proof-gap reports;
- source-level prior-art equivalence analyses;
- independently written reproductions;
- proof-assistant translations;
- corrected references;
- simpler proofs;
- accessibility and teaching improvements that preserve exact meaning.

## Before opening a pull request

1. Identify the paper and exact theorem affected.
2. Read its current status and claim boundaries.
3. Open or link the relevant review issue.
4. Keep mathematical changes separate from editorial changes.
5. Add or update tests and evidence where computation is material.
6. Preserve corrections rather than deleting history.
7. Do not add generated binary artifacts directly unless the repository workflow requires them.

## Pull-request requirements

A mathematical PR should state:

```text
paper ID
source theorem or lemma
change type: proof / computation / formalization / prior art / exposition
exact claim affected
reason for the change
validation performed
new limitations or unresolved questions
```

## Code

Code must be deterministic where the theorem depends on exact output. Declare dependencies and versions. Avoid personal paths, hidden network calls, telemetry, and undeclared data downloads.

Independent implementations should explain which primary modules and expected answers they intentionally avoid.

## Formal proofs

Formalization PRs must include:

- pinned proof-assistant version;
- pinned dependencies;
- placeholder policy;
- build command;
- listed declarations;
- axiom report or equivalent;
- explicit scope not formalized.

## References

Citations must be checked against the original source. AI-generated bibliography entries are not acceptable without human verification. Include theorem numbers, pages, or precise passages for equivalence claims.

## Authorship

Contributing code, comments, or review does not automatically establish paper authorship. Authorship follows the target venue's standards and requires substantial intellectual contribution, accountability, and owner-approved disclosure.

AI systems are not authors and cannot accept contributor terms or publication responsibility.

## Conduct

Critique claims, proofs, and evidence directly. Do not attack people, speculate about motives, or use credentials as a substitute for an argument.

## Rights

By contributing, a human contributor must state that they have the right to provide the submitted material and identify any licensing restrictions. No contribution receives a blanket MIT license merely by entering the repository.
