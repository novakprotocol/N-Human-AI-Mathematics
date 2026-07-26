# Adversarial Review Protocol

The repository invites four kinds of technical challenge. A review succeeds when it improves the record, whether it confirms, repairs, demotes, or rejects a claim.

## 1. Counterexample report

Use when a universal statement fails on a concrete object.

Required content:

```text
paper ID and exact source commit
theorem/lemma identifier
all assumptions claimed to hold
explicit counterexample object
calculation showing the conclusion fails
independent reproduction instructions
software and environment, if any
```

A counterexample receives highest triage priority. The affected claim must be marked `challenged` until resolved.

## 2. Proof-gap report

Use when a proof step is unsupported, circular, scope-invalid, or depends on an unstated assumption.

Required content:

```text
paper ID and theorem/lemma
exact proof location
the disputed inference
why the cited premise is insufficient
whether the issue appears fatal or repairable
suggested repair, when known
```

A stylistic preference is not a proof gap. A proof gap must concern logical support.

## 3. Prior-art or equivalence report

Use when an earlier result may contain, imply, or be equivalent to a project claim.

Required content:

```text
complete bibliographic source
stable link, DOI, MR/Zbl identifier, or archived copy
exact earlier theorem/proposition/page
translation between definitions and notation
implication or equivalence argument
which current novelty statement must change
```

A search-result title or keyword overlap is insufficient. The report should compare theorem statements and hypotheses.

## 4. Reproduction report

Use when rerunning or independently rebuilding a proof or computation.

Required content:

```text
paper ID and exact source commit
commands executed
operating system and tool versions
hardware where material
whether expected outputs were hidden
outputs, logs, and artifact hashes
discrepancies and their severity
whether primary source code was reused
```

## Review dispositions

| Disposition | Meaning |
|---|---|
| `confirmed_for_scope` | Review found no error within its declared scope. |
| `clarification_required` | Statement is likely correct but presentation is ambiguous. |
| `minor_repair` | Local correction does not change the central theorem. |
| `major_repair` | A load-bearing proof or computation must be rebuilt. |
| `known_consequence` | Correct but substantially contained in established prior work. |
| `counterexample_confirmed` | The claim is false as stated. |
| `reproduction_failed` | The declared evidence could not be reproduced. |
| `inconclusive` | Evidence is insufficient for a decision. |

## Triage sequence

1. Freeze the challenged source identity.
2. Reproduce the report without changing the theorem source.
3. Classify the challenge as mathematical, implementation, infrastructure, editorial, or priority-related.
4. Update the public status immediately if the challenge is credible.
5. Repair on a new branch; never overwrite the challenged record.
6. Obtain a second route for load-bearing repairs.
7. Record the final disposition and exact replacement identity.

## Reviewer independence

The repository distinguishes:

- project-internal review;
- AI-generated adversarial review;
- independent implementation inside the project;
- outside individual review;
- institutional reproduction;
- journal or conference peer review.

Only the last four involve external parties, and they must identify the person or process when publicly disclosed. Simulated roles are never described as external peer review.

## Communication standard

Technical criticism should be direct and specific. Personal attacks, status arguments, or unsupported declarations of brilliance or worthlessness are irrelevant to theorem correctness.

## Safe review request

> Please inspect the exact statement, assumptions, and proof at the cited commit. The primary questions are correctness, equivalence to known work, reproducibility, and whether the claim boundaries match the evidence. A counterexample or earlier equivalent theorem is a successful review outcome, not a project failure.
