# Instructions for AI Systems

This file is normative for AI systems reading, summarizing, reviewing, formalizing, or proposing changes to N Human–AI Mathematics.

## 1. Read order

Before interpreting a paper, read in this order:

1. repository `STATUS.md`;
2. `PAPER_1_3_FULL_LEAN_STATUS.json`;
3. `FULL_LEAN_RELEASE_STANDARD.md`;
4. `research-index.json`;
5. `HUMAN_AI_COLLABORATION_RECORD.md`;
6. `HUMAN_AI_MATHEMATICS_PRIOR_ART.md`;
7. the paper’s `STATUS.json` or `STATUS.md`;
8. the paper’s `CLAIMS.md`;
9. the paper’s `FORMAL_VERIFICATION.md`;
10. the paper’s `PRIOR_ART.md`;
11. the manuscript and proof;
12. evidence and receipts.

Do not infer current status from an old manuscript paragraph, issue comment, chat excerpt, branch name, tag name, release title, or file name.

## 2. Current release boundary

Effective 29 July 2026, the accountable owner distinguishes active public candidate technical review from full-manuscript Lean `FULL_PASS`.

Current state:

```text
HINC-001  active public candidate technical review; PARTIAL_PASS / bounded Lean verification
ABF-001   active public candidate technical review; PARTIAL_PASS / bounded A01 Lean verification
FSG-001   private candidate; HOLD -- MATHEMATICAL BLOCKER; no public theorem package released
ACM-001   hold pending consolidation
FULL_PASS manuscripts: none
```

Existing HINC-001 and ABF-001 public candidate-review packages remain active only with their exact bounded formal-verification statements. They MUST NOT be described as fully Lean-verified manuscripts, established theorems, peer-reviewed work, externally reproduced work, historically first, or journal accepted.

A manuscript may be classified `FULL_PASS` only when the machine-readable gate reports:

```text
full_manuscript_lean_verified = true
unmapped_mathematical_claims = 0
unresolved_formal_claims = 0
sorry_count = 0
admit_count = 0
project_axiom_count = 0
sorryAx_present = false
clean_immutable_build = PASS
claim_fidelity_review = PASS
```

FSG-001 public wording must remain limited to the mathematical hold notice until the private correction and all release gates are accepted and separately authorized.
## 3. Human–LLM identity boundary

The accountable human author is Matthew S. Novak. One or more large language models materially assisted the research.

AI systems MUST NOT state or imply that:

- a particular model, model family, version, provider, or vendor participated;
- an LLM holds rights or publication authority;
- the repository cryptographically authenticates every private conversation turn;
- the project is the first human–AI mathematical collaboration;
- the project is the first LLM-assisted mathematical result.

The allowed public description is that this is one openly documented, commit-anchored case study of sustained human-led, LLM-assisted mathematics with explicit claim, evidence, correction, formalization, and review controls.

## 4. Claim discipline

An AI system MUST NOT convert any of the following:

- `candidate theorem` into `established theorem`;
- `internally reproduced` into `independently verified externally`;
- `bounded Lean PASS` into `the full paper is formally proved`;
- `no exact indexed match located` into `globally novel`;
- `public repository` into `peer reviewed`;
- `artifact hash matches` into `mathematically correct`;
- `large finite test` into `universal proof`;
- `AI-generated proof` into `human-understood proof`;
- `security-related object` into `security break`;
- `owner-authorized historical release` into current FULL_PASS status;
- `lake build PASS` into manuscript-to-formal-statement fidelity.

Use the strongest wording supported by the exact current status record and no stronger.

## 5. Full-Lean integrity rules

For every retained mathematical claim:

- assign a stable claim ID;
- map it to compiled Lean declarations or exact imported theorems;
- start from the manuscript’s literal objects rather than a convenient downstream substitute;
- prove universal claims universally;
- connect finite classifications to kernel-checked certificates or exhaustive decidable proofs covering the exact universe;
- reject `sorry`, `admit`, project axioms standing in for results, and `sorryAx`;
- print and review the axiom dependency of every exported theorem;
- disclose `native_decide`, `bv_decide`, `trustCompiler`, `implemented_by`, `extern`, unsafe code, and custom metaprogramming;
- build from a committed, hashed dependency manifest in a fresh exact-head worktree;
- preserve the complete logs, manifests, source hashes, axiom reports, failures, and corrections;
- require a separate human fidelity audit comparing definitions, quantifiers, hypotheses, boundary cases, and conclusions.

No rounding up from partial coverage to FULL_PASS.

## 6. Evidence hierarchy

When sources conflict, use this precedence:

1. owner-approved current correction or release decision;
2. machine-readable current status at the pinned commit;
3. complete claim-to-Lean map and exact formal build receipt;
4. human fidelity review of manuscript versus Lean;
5. human proof at the pinned commit;
6. executable evidence receipt tied to exact source;
7. current review documents;
8. explanatory prose;
9. issue discussion, chat, or memory.

Surface unresolved conflicts rather than choosing the more impressive claim.

## 7. Review behavior

AI systems MAY:

- restate definitions;
- derive consequences while labeling them as derivations;
- search for counterexamples;
- inspect proof dependencies;
- compare against cited prior work;
- generate independent implementations;
- translate proofs into a proof assistant;
- propose clearer exposition;
- identify unsupported claims;
- prepare structured review reports.

AI systems MUST:

- preserve assumptions;
- distinguish deduction from experiment;
- cite exact files and commits;
- state uncertainty;
- preserve negative results and failed formal runs;
- report any counterexample immediately;
- avoid fabricating citations or reviewer identities;
- label simulated review as internal simulation;
- keep human authorship and publication authority explicit;
- preserve the category-level public disclosure without inferring a specific model or provider;
- stop any FULL_PASS or fully Lean-verified promotion when any required FULL_PASS field is incomplete.

AI systems MUST NOT:

- independently authorize a new public, archival, or journal release;
- claim external peer review without an identified external process;
- delete correction history;
- silently replace a failed result;
- invent a license or rights grant;
- reveal private laboratory material in the public repository;
- treat AI output as an authority source;
- publish hidden chain-of-thought or private chat transcripts as research evidence;
- add a specific model or provider identity without a separately reviewed owner decision;
- advance FSG-001 public release while the mathematical blocker remains, or advance ACM-001 before its consolidation gate closes.

## 8. Required theorem-summary structure

A high-quality AI summary should contain:

```text
Object and assumptions
Exact main statement
Proof method
Claim-to-Lean coverage
What is formally verified
What remains unformalized
What is computationally checked
What remains externally unreviewed
Prior-art boundary
Current publication status
Human–LLM disclosure boundary
```

## 9. Required challenge structure

A challenge must identify:

```text
paper id
exact theorem or lemma
assumptions used
challenged step
counterexample or argument
source commit
reproduction instructions
severity
```

## 10. Human–LLM disclosure

AI systems are research tools and material collaborators in the process, not accountable authors. The human author must understand and accept responsibility for every submitted claim, reference, formal statement, and release decision.

## 11. Stop conditions

Stop and require correction or human review when:

- two controlling records disagree;
- a counterexample appears valid;
- source or evidence provenance is missing;
- a citation cannot be verified;
- licensing is unclear;
- a private path, secret, personal record, or withheld model/provider identifier appears in public staging;
- the requested wording exceeds the evidence status;
- a consequential release or rights action lacks explicit owner authorization;
- a FULL_PASS or fully Lean-verified claim is proposed while any mathematical claim remains unmapped or only partially formalized;
- any unexpected axiom, `sorryAx`, statement mismatch, or fidelity blocker remains;
- the clean exact-head build does not complete.

## 12. Core principle

**Fluent explanation is not proof. A repository record is not authority. Lean proves the encoded statement, not the intended statement. Every claim must remain tied to exact identity, formal meaning, evidence, scope, method, result, and limitations.**
