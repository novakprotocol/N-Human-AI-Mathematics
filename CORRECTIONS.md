# Corrections and Superseded Claims

A clean publication repository must remain honest about errors. This ledger records public corrections without importing the private laboratory's entire development history.

## Correction policy

For every material correction, record:

```text
correction ID
paper and theorem affected
original source commit and wording
problem discovered
how it was detected
scientific impact
replacement source commit
new evidence or proof route
review disposition
```

Do not rewrite an archived release. Publish a corrected release and link both identities.

## Severity

| Severity | Meaning |
|---|---|
| `editorial` | No mathematical meaning changed. |
| `clarification` | Ambiguity removed; theorem unchanged. |
| `local_proof_repair` | One proof step repaired without changing the statement. |
| `statement_narrowed` | Assumptions or conclusion changed materially. |
| `computation_replaced` | Evidence or implementation was defective and regenerated. |
| `claim_demoted` | Correct mathematics was identified as known or weaker than first described. |
| `retracted` | Claim false or unsupported. |

## Current public ledger

No standalone public repository release exists yet. The first release will import only corrections relevant to the promoted papers.

### HINC-CORR-001 — odd extensionality proof repair

```text
paper:                 HINC-001
severity:              local_proof_repair
failed source:         2e7423bb9d3461389ccc94ad59500395abc91385
failed run:            30173789803
failed job:            89719185539
failed artifact:       8623660266
repaired source:       d7751d1de76253407016ef4bf92738cffa800e82
passing run:           30174213006
passing job:           89720259114
passing artifact:      8623775718
artifact SHA-256:      2dee88b9a248dee8719c27aa23a27ca3281e697cf67202bb50c1fe60a4809dc9
```

The first principal-classification Lean build failed because the odd-data extensionality proof used recursive `simp_all` and exceeded Lean's recursion depth. The source reached genuine compilation; this was not an infrastructure failure.

The proof was replaced by explicit substitution of the four data-field equalities followed by reflexivity. The mathematical coefficient normal form, theorem statement, and composition law did not change.

The repaired immutable source passed `lake build`, the placeholder gate, and the classification axiom report with no `sorryAx`. The retained report lists only `propext` and `Quot.sound` for the displayed declarations.

Current disposition: `local_proof_repair — resolved and publicly verified`.

## Examples retained from the private laboratory

The private laboratory has previously withdrawn or demoted claims when:

- an oriented rewriting argument was incorrectly used as an equational-independence proof;
- a proposed new polynomial was shown to be a lossless re-encoding of established Hall/probabilistic-zeta data;
- a support formula was stronger in a linearized model than in the actual carry-enabled model;
- a test fixture contained incorrect expected coefficients;
- an execution environment created a job but ran zero steps.

These examples inform the public process but are not claims of the promoted papers unless explicitly imported.

## Rule

**A correction is evidence of quality control when it is specific, preserved, and propagated. Concealing or silently overwriting it is not.**
