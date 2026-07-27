# Open Review Challenge

## The invitation

This repository is public so that its mathematics and its human–AI research process can be challenged.

The request is not:

> Trust the model, the author, the code, or the repository.

The request is:

> Inspect a precise claim at an exact source identity and provide evidence that confirms, narrows, corrects, supersedes, or defeats it.

## Four principal review routes

### 1. Counterexample

Provide a complete object that satisfies the theorem’s assumptions and violates its conclusion.

A useful report includes:

- paper ID;
- exact source commit;
- theorem or lemma identifier;
- explicit object and parameter values;
- calculation showing that the assumptions hold;
- calculation showing that the conclusion fails;
- reproduction instructions.

Use the repository’s **Counterexample report** issue template.

### 2. Proof gap

Identify a step that does not follow from its premises, relies on an unstated assumption, invokes a theorem outside its scope, or hides an unverified computation.

A useful report distinguishes:

- editorial ambiguity;
- local repair;
- load-bearing gap;
- fatal defect in the current statement.

Use the **Proof-gap report** issue template.

### 3. Earlier equivalent result

Locate an earlier theorem, construction, code base, thesis, or non-indexed source that contains, implies, or is equivalent to a project claim.

A useful priority report gives:

- complete citation;
- exact theorem/page/source location;
- translation of notation and objects;
- implication or equivalence argument;
- the portion of the project claim that remains instance-specific.

A title similarity or search snippet is not enough. Use the **Prior-art or equivalence report** issue template.

### 4. Independent reproduction

Reproduce a theorem consequence, finite classification, formal declaration, or evidence identity.

State the independence level:

```text
exact rerun of primary source
fresh-environment rerun
separately written implementation
independent proof derivation
independent formalization
```

Report the exact source identity, environment, commands, outputs, hashes, and first discrepancy. Use the **Independent reproduction report** issue template.

## Additional process challenge

The repository also invites review of its human–AI collaboration record.

A process challenge may address:

- whether a public file overstates the contribution of ChatGPT or the human researcher;
- whether a model identity is stated more strongly than the session evidence supports;
- whether a correction was omitted or misclassified;
- whether internal reproduction is presented as external review;
- whether a reconstructed narrative could be mistaken for a contemporaneous record;
- whether a claimed public precedent is inaccurate or incomplete;
- whether the OpenAI institutional boundary is unclear.

Open an ordinary issue and cite exact files, commits, and evidence.

## Current featured challenge: HINC-001

The most useful reviews currently target:

1. the arbitrary-base even and odd coefficient eliminations;
2. generator-to-global preservation of all cup products and Gerstenhaber brackets;
3. representability of the complete endomorphism functors;
4. the odd clopen decomposition;
5. the complete scheme-theoretic center equality;
6. the fppf-derived subgroup and abelianization claims;
7. the common crossing-core equivalence;
8. earlier classifications or general theorems that imply the package.

Read:

- `papers/HINC-001/CLAIMS.md`
- `papers/HINC-001/PROOF_MAP.md`
- `papers/HINC-001/FORMAL_VERIFICATION.md`
- `papers/HINC-001/PRIOR_ART.md`
- `papers/HINC-001/REPRODUCE.md`
- `papers/HINC-001/REVIEW_REQUEST.md`

## Response policy

A substantive report will be classified and linked to the affected paper state.

Possible outcomes:

```text
confirmed for declared scope
clarified
locally corrected
claim narrowed
superseded
historical-priority status changed
rejected as stated
unresolved
```

Earlier source identities and failed statements remain preserved. Corrections do not silently rewrite history.

## Conduct

Be precise and direct. Criticism of claims, proofs, code, and evidence is welcome. Harassment, doxxing, credential attacks, and disclosure of secrets or private material are not.

The standard is evidence, not deference.
