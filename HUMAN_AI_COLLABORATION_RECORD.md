# Human–LLM Collaboration Record

## Purpose

This document records the operating relationship behind N Human–AI Mathematics.

The accountable human researcher and repository owner is:

```text
Matthew S. Novak
```

The public AI-assistance category is:

```text
one or more large language models (LLMs)
```

The project uses a **human-led, LLM-assisted** model. Matthew S. Novak selects research goals, supplies domain context and constraints, evaluates significance, runs or supervises release gates, decides which claims survive, and retains authorship and publication authority. LLMs materially assist with exploration, candidate theorem formulation, algebraic derivation, proof decomposition, program generation, test design, counterexample search, formal-proof drafting, literature-query design, documentation, and correction analysis.

The public release does not identify a specific model, model family, version, provider, or vendor. A more specific disclosure may be added only after separate human legal and publication-policy review.

## What the public record can establish

The repository supplies inspectable evidence that a sustained human–LLM research process occurred:

- dated Git commits and pull requests;
- source and artifact hashes;
- machine-readable paper and claim states;
- executable Python, C, symbolic, and Lean sources;
- preserved failed runs and explicit repairs;
- independent internal implementations where available;
- formal-verification receipts for bounded scopes;
- human-facing explanations and AI-facing interpretation rules;
- structured public channels for counterexamples, proof gaps, prior art, and reproduction.

These records establish chronology, source identity, declared role allocation, and the existence of a reproducible research workflow. They do not independently authenticate every private conversation turn or prove that every mathematical statement is correct.

## What is not being published

The public repository does not publish:

- private chat transcripts;
- hidden chain-of-thought or internal model scratch work;
- specific model or provider identities;
- personal workstation paths;
- credentials or private attachments;
- abandoned branches that do not contribute to a selected paper;
- reconstructed notes presented as if they were contemporaneous human notes.

When a research narrative is reconstructed from source, tests, receipts, and dated repository history, it must be labeled as a reconstruction.

## Role allocation

### Matthew S. Novak

The human role includes:

1. selecting the research direction and deciding when to persist, pivot, or stop;
2. supplying constraints, definitions, earlier project results, and application goals;
3. challenging shallow answers and demanding stronger proof or evidence;
4. deciding which candidate results are worth preserving;
5. executing or supervising local programs and publication scripts;
6. reviewing release boundaries, rights, attribution, and public visibility;
7. accepting responsibility for retained claims and future corrections.

### Large language models

The LLM role includes:

1. generating candidate mathematical objects, conjectures, reductions, and normal forms;
2. proposing proof plans and identifying load-bearing lemmas;
3. writing and revising source code, tests, formal source, and evidence processors;
4. constructing exhaustive finite checks and semantic negative controls;
5. searching for contradictions, edge cases, and overclaims;
6. designing literature and equivalence searches;
7. explaining technical results at human and machine-readable levels;
8. preserving failures, classifying their causes, and preparing bounded repairs;
9. organizing paper, reviewer, evidence, and release packages.

### Independent tools

Python, C compilers, symbolic algebra systems, Lean, Git, GitHub Actions, and checksum tools provide evidence routes. They do not become authors and do not convert a flawed statement into a theorem merely because a program ran.

## Identity boundary

The public disclosure intentionally stops at the category **LLM-assisted**. It does not claim cryptographic attestation of the model behind every historical message and does not identify any specific model or provider.

If a later journal, archive, legal review, or owner decision requires more specificity, that disclosure must be added as a separately reviewed change tied to an exact release.

## Correction discipline

The project follows a fail-closed rule:

```text
failure preserved
    ↓
cause classified
    ↓
source or statement repaired
    ↓
fresh immutable identity
    ↓
complete rerun
    ↓
PASS recorded separately
```

Operational failures are not mathematical counterexamples. Mathematical failures are not relabeled as tooling problems. External review is not simulated by assigning an AI a reviewer persona.

## Authorship and responsibility

AI systems are not listed as authors, do not own the work, and do not exercise publication authority. Matthew S. Novak is the accountable human author and accepts responsibility for deciding what is released, corrected, submitted, or withdrawn.

An LLM may materially influence discovery while the human researcher verifies, rewrites, selects, and accepts responsibility for the final manuscript.

## Public challenge

Readers are not asked to trust the collaboration narrative or the mathematics on authority. They are asked to inspect the exact record and do one or more of the following:

- reproduce a declared result;
- identify a counterexample;
- identify a proof gap;
- locate an earlier equivalent theorem;
- challenge the claimed role allocation with concrete repository evidence;
- propose a more accurate interpretation of what the evidence establishes.

A valid correction strengthens the record.
