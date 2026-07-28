# Mandatory publication gates

No new theorem package, benchmark, dataset, public branch containing unreleased mathematics, Pages activation, visibility change, tag, release, DOI deposit, or journal submission may proceed unless the exact candidate package passes every gate below.

The process is fail-closed. A missing receipt, interrupted command, unavailable search source, unresolved hostile-review finding, unproved universal claim, incomplete exhaustive run, or ambiguous source identity leaves the package on **HOLD**.

## 1. Claim boundary

Every public statement must be classified as one of:

- a theorem with a complete human proof;
- a finite classification established by a complete declared enumeration;
- a bounded computational check with an exact scope;
- a formally verified declaration with an exact proof-assistant receipt;
- a conjecture, observation, definition, or open question.

The package must state assumptions, object identity, quantified scope, known gaps, and nonclaims. Tests and examples never substitute for a universal proof. A finite computation never establishes a larger or full-width claim.

## 2. Proof closure

Before public technical review:

1. every universal mathematical claim has a complete human proof and dependency map;
2. every finite census has either a mathematical counting proof or a completed exhaustive enumeration over the entire declared universe;
3. every executable claim is tied to source, environment, inputs, output, and SHA-256 identities;
4. proof-assistant status is stated exactly, including unformalized portions;
5. no `sorry`, `admit`, placeholder proof, omitted case, or unresolved proof obligation is represented as complete.

Proof-assistant formalization is strongly preferred but is not falsely required for a candidate technical-review release when a complete human proof exists. A formal PASS applies only to the declarations compiled in the recorded environment.

## 3. Hostile review

A separate review lane must assume the result is wrong and actively attempt to break it. At minimum it must test:

- hidden assumptions and quantifier changes;
- counterexamples and boundary cases;
- duplicate counting, orbit/subspace confusion, and off-by-one errors;
- dependence between supposedly independent implementations;
- stale hashes, wrong source identities, and generated-file contamination;
- overclaiming of novelty, proof, external review, security, or generality;
- overlap with earlier project manuscripts.

Every finding must be corrected, rejected with a written reason, or left as a release blocker. Public release requires zero unresolved blocking findings.

## 4. Prior-art and equivalence search

The search must be systematic and complete **to a declared scope and date**. It cannot honestly guarantee that no equivalent work exists anywhere.

The ledger must cover, when relevant:

- exact title, phrases, equations, presentations, identifiers, and numerical signatures;
- synonyms, translated terminology, coordinate changes, dual/opposite conventions, and broader general theorems;
- arXiv, journal/publisher metadata, Crossref/DOI surfaces, IACR ePrint, HAL, Zenodo, theses, books, public repositories, and public zbMATH/MathSciNet surfaces;
- backward and forward citation tracing from the closest sources;
- a final delta search immediately before release.

A no-match result authorizes only: **“No exact indexed match was located in the recorded search.”** It does not establish worldwide priority, first discovery, or peer review.

## 5. Independent challenge route

At least one structurally independent route must challenge the controlling result. For computational work this normally means a separate implementation that does not import the primary implementation and that agrees on canonical outputs. For proof-heavy work it may be an independent derivation, proof assistant, or specialist reconstruction.

The package must include negative or tamper controls where meaningful. Internal independence is not external reproduction and must not be described as such.

## 6. Clean execution to completion

The complete gate must run from a fresh checkout or clean copied workspace in an isolated environment. It must:

- install pinned dependencies;
- compile all declared source;
- run every test, verifier, native route, proof build, and checksum check;
- finish without timeout, interruption, skipped required work, or accepted partial output;
- produce deterministic receipts and a complete SHA-256 manifest;
- preserve failed attempts separately from the accepted PASS receipt.

A command that started but did not finish is **NOT RUN TO COMPLETION**, not PASS.

## 7. Provenance and priority record

Before release, the exact source and artifacts must be locked by:

- an exact repository commit;
- a complete SHA-256 manifest;
- a versioned tag and release record;
- release assets attached before publication;
- an immutable GitHub release and release attestation when available;
- an archival DOI or equivalent long-term deposit when the owner elects to use one.

The source record supports provenance and citation. It does not itself establish mathematical correctness or historical priority. Potentially patentable applications must be held for owner/legal review before public disclosure.

## 8. Owner authorization

The final receipt must record explicit owner authorization for the exact package identity and release target. General repository authority is not a substitute for package-specific authorization.

## 9. Allowed release state

Passing these gates permits a **candidate public technical-review release**. It does not permit claims of:

- peer review or journal acceptance;
- external reproduction unless an identified outside party completed it;
- worldwide historical priority;
- complete formal verification beyond the recorded declarations;
- security consequences beyond the exact proved scope.

## Machine enforcement

The repository workflow runs `tools/validate_publication_gate.py`. Every paper in `active_review` or `published` state must have a PASS receipt at:

```text
reports/publication-gates/<PAPER-ID>.json
```

A new paper cannot be promoted to a public state without adding a complete gate receipt in the same reviewed change.
