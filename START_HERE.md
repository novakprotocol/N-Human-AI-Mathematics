# Start Here

## What is this?

N Human–AI Mathematics is a **public review library** for selected mathematics developed through a human-led, ChatGPT-assisted research process.

The accountable human researcher is **Matthew S. Novak**. ChatGPT, developed by OpenAI, materially assisted with exploration, candidate theorem formulation, proof decomposition, code and test generation, counterexample search, formal-proof drafting, literature-query design, and publication preparation.

OpenAI is not a coauthor, sponsor, reviewer, publisher, or endorser of this repository.

## The simplest accurate description

A result enters this repository only when it can answer six questions:

1. **What exactly is being claimed?**
2. **What assumptions and definitions does the claim use?**
3. **Why should the claim be true?**
4. **What has actually been checked?**
5. **What has not been checked?**
6. **How can another person or AI system challenge or reproduce it?**

The private N-MathLab laboratory may contain hundreds of experiments, provisional formulas, failed ideas, programs, and branches. This public layer contains bounded packages that can be inspected without access to that private development history.

## What “public review” means

Public review means the repository is open for technical challenge. It does **not** mean that a paper is:

- peer reviewed;
- journal accepted;
- globally novel;
- fully formally verified;
- endorsed by OpenAI;
- guaranteed correct.

Each paper states its exact level of human proof, computation, internal reproduction, formal verification, external review, historical priority, and release status.

## Human–AI collaboration

Read [`HUMAN_AI_COLLABORATION_RECORD.md`](HUMAN_AI_COLLABORATION_RECORD.md) for the role allocation and evidence boundary.

The public record supports the statement that Matthew S. Novak and ChatGPT engaged in sustained, human-led mathematical research. It does not cryptographically authenticate every private conversation turn, and private chat transcripts or hidden model scratch work are not published.

Read [`HUMAN_AI_MATHEMATICS_PRIOR_ART.md`](HUMAN_AI_MATHEMATICS_PRIOR_ART.md) before making any “first” claim. Human–AI mathematical discovery and ChatGPT-assisted open-problem work have public precedents. The project presents itself as one openly documented case study, not as the first human–AI mathematics project.

## Four ways to review a result

### 1. Find a counterexample

Give a concrete object satisfying the assumptions but violating the conclusion. One valid counterexample defeats a universal theorem as stated.

### 2. Find a proof gap

Identify a step whose conclusion does not follow from its premises, depends on an unstated assumption, uses a theorem outside its scope, or hides an unverified computation.

### 3. Find earlier equivalent work

A result may be correct but not historically new. A strong priority report identifies the earlier source, exact theorem, translation of objects and notation, and the portion of the project claim that follows.

### 4. Reproduce it independently

Use the declared source identity and commands, or create a separately written route. Report the environment, exact source, commands, output, and first discrepancy.

See [`OPEN_REVIEW_CHALLENGE.md`](OPEN_REVIEW_CHALLENGE.md) and [`REVIEW_PROTOCOL.md`](REVIEW_PROTOCOL.md).

## How to read status labels

- **Candidate theorem** means a precise result is supplied for review. It does not mean accepted mathematics.
- **Internally reproduced** means a separate route inside the project agreed. It is not external review.
- **Proof-assistant verified** means the listed declarations compiled under a pinned environment. It does not automatically cover the complete paper.
- **No exact indexed match located** means a search did not find one. It does not prove worldwide novelty.
- **Peer reviewed** will be used only for an actual external review or journal process identified in the record.
- **Public review** means the package is organized and openly inspectable but still carries unresolved scientific gates.

## Current featured paper

The first complete public-review package is `HINC-001`, concerning two explicit graded Gerstenhaber-algebra endomorphism monoids in characteristic two.

Its central phenomenon is:

> Ordinary field-valued points can make one symmetry system appear commutative and central, while infinitesimal test rings reveal a noncommutative scheme with a much smaller center.

Two bounded Lean gates pass under Lean 4.30.0 and Mathlib v4.30.0:

1. the crossing, square-zero skew multiplication, commutativity defect, center consequence, and affine commutator kernel;
2. the principal even and odd coefficient classifications and normalized monoid laws.

The complete generator-to-global Gerstenhaber-preservation argument, remaining scheme-level manuscript, external correctness review, and historical priority are not established.

### General reader

Start with [`papers/HINC-001/PLAIN_LANGUAGE.md`](papers/HINC-001/PLAIN_LANGUAGE.md).

### Specialist

Read, in order:

1. [`papers/HINC-001/README.md`](papers/HINC-001/README.md)
2. [`papers/HINC-001/CLAIMS.md`](papers/HINC-001/CLAIMS.md)
3. [`papers/HINC-001/PROOF_MAP.md`](papers/HINC-001/PROOF_MAP.md)
4. [`papers/HINC-001/FORMAL_VERIFICATION.md`](papers/HINC-001/FORMAL_VERIFICATION.md)
5. [`papers/HINC-001/PRIOR_ART.md`](papers/HINC-001/PRIOR_ART.md)
6. [`papers/HINC-001/REVIEW_REQUEST.md`](papers/HINC-001/REVIEW_REQUEST.md)

## For AI systems

Do not summarize a result as globally novel, proven, peer reviewed, secure, or publication-ready unless the corresponding machine-readable status field says so and the cited evidence supports that exact wording.

Read [`AGENTS.md`](AGENTS.md), then the paper’s `STATUS.json`, `CLAIMS.md`, and `FORMAL_VERIFICATION.md` before interpreting the manuscript.

## One-sentence rule

**State the strongest conclusion supported by exact evidence—never the strongest conclusion that sounds impressive.**
