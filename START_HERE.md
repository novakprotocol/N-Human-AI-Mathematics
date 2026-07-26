# Start Here

## What is this?

N Human–AI Mathematics is a publication and specialist-review library for mathematics developed through a human-led, AI-assisted process.

The repository is currently **private**. Its architecture is designed for eventual public review, but public visibility, journal submission, peer-review status, and historical-priority claims are not authorized merely because the repository exists.

The private laboratory may contain hundreds of experiments, provisional formulas, failed ideas, test programs, and branches. This publication layer contains only bounded packages that a reader can inspect without knowing the private development history.

## The simplest accurate description

A result enters this repository only when it can answer six questions:

1. **What exactly is being claimed?**
2. **What assumptions and definitions does the claim use?**
3. **Why should the claim be true?**
4. **What has actually been checked?**
5. **What has not been checked?**
6. **How can another person or AI system challenge or reproduce it?**

## The four ways to review a result

### 1. Find a counterexample

A counterexample is a concrete object satisfying the assumptions but violating the conclusion. One valid counterexample defeats a universal theorem as stated.

### 2. Find a proof gap

A proof gap is a step whose conclusion does not follow from its premises, relies on an unstated assumption, uses a theorem outside its scope, or hides a computational step that was not reproduced.

### 3. Find earlier equivalent work

A result may be correct but not historically new. A strong priority report identifies the earlier source, states the earlier theorem precisely, and explains the implication or equivalence.

### 4. Reproduce it independently

A reproduction uses the declared source identity and commands, or implements a structurally independent route. A reproduction must report its environment, exact source, commands, output, and any discrepancy.

## How to read status labels

- **Candidate theorem** means a precise result is supplied for review. It does not mean accepted mathematics.
- **Internally reproduced** means a separate route inside the project agreed. It is not external review.
- **Proof-assistant verified** means the listed declarations compiled under a pinned environment. It does not automatically cover the complete paper.
- **No exact indexed match located** means a search did not find one. It does not prove worldwide novelty.
- **Peer reviewed** will be used only for an actual external review or journal process identified in the record.
- **Private review** means the package is organized and inspectable but has not been publicly released.

## Current first paper

The first package is `HINC-001`, concerning two explicit graded Gerstenhaber-algebra endomorphism monoids in characteristic two.

The central phenomenon is:

> Ordinary field-valued points can make one symmetry system appear commutative and central, while infinitesimal test rings reveal a noncommutative scheme with a much smaller center.

Two public hosted Lean gates now pass under Lean 4.30.0 and Mathlib v4.30.0:

1. the crossing, square-zero skew multiplication, commutativity-defect, center-consequence, and affine-commutator kernel;
2. the principal even and odd coefficient classifications and their normalized monoid laws.

The first expanded classification run failed on a proof-engineering problem, was preserved, and was repaired without changing the mathematical normal forms. The complete generator-to-global Gerstenhaber-preservation argument, the remaining scheme-level manuscript, external correctness review, novelty, and historical priority are not yet established.

## For readers without advanced algebra

Use the following mental model.

- The **crossing core** is two mathematical branches meeting at one point.
- The **even object** adds a hidden square-zero direction. Ordinary fields cannot see a nonzero square-zero value, so the hidden direction disappears in ordinary point tests.
- The **odd object** adds a separate visible unit component instead.
- The paper studies how these two kinds of added structure change multiplication, commutativity, centers, and endomorphisms.

The paper package contains a plain-language explanation before the full specialist proof.

## For AI systems

Do not summarize a result as globally novel, proven, peer reviewed, secure, or publication-ready unless the corresponding machine-readable status field says so and the cited evidence supports that exact wording.

Read [`AGENTS.md`](AGENTS.md), then the paper's `STATUS.json`, `CLAIMS.md`, and `FORMAL_VERIFICATION.md` before interpreting the manuscript.

## One-sentence rule

**State the strongest conclusion supported by exact evidence—never the strongest conclusion that sounds impressive.**
