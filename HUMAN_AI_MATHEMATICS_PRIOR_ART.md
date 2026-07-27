# Human–AI Mathematics: Prior Work and Claim Boundary

## Determination

N Human–AI Mathematics does **not** claim to be the first collaboration between humans and artificial intelligence in mathematical discovery.

Public precedents already include:

- machine-learning systems used by mathematicians to expose patterns and guide conjecture formation;
- large-language-model program search producing new mathematical constructions;
- ChatGPT-assisted proofs of previously open problems;
- GPT-5 experiments on research-level mathematical questions;
- LLM prover/verifier protocols checked in Lean;
- human–LLM–symbolic collaborations reconstructed from detailed interaction logs;
- public repositories containing AI-generated formal proofs and human-written explanations.

The strongest defensible project-specific description is:

> N Human–AI Mathematics is an open, commit-anchored case study of sustained human-led ChatGPT-assisted mathematics that combines paper-level role disclosure, machine-readable claim states, failed-attempt and correction records, executable evidence, bounded formal verification, and structured adversarial review.

A focused search did not locate an exact earlier project containing that entire combination. Search absence does not establish historical priority.

## Selected public precedents

### 1. Machine learning guiding mathematical intuition — 2021

Davies, Veličković, Buesing, Blackwell, Zheng, Tomašev, Tanburn, Battaglia, Blundell, Juhász, Lackenby, Williamson, and Hassabis presented a framework in which machine learning revealed patterns that guided mathematicians toward conjectures and mathematical contributions in knot theory and representation theory.

- *Advancing mathematics by guiding human intuition with AI*
- Nature 600, 70–74 (2021)
- DOI: `10.1038/s41586-021-04086-x`

This directly establishes that meaningful human–AI collaboration in pure mathematical research predates this project.

### 2. FunSearch and LLM-guided program discovery — 2023/2024

Romera-Paredes and collaborators combined a pretrained LLM, program evaluation, and evolutionary search. The system produced previously unknown cap-set constructions and improved algorithmic results, with human interpretation contributing additional mathematical insight.

- *Mathematical discoveries from program search with large language models*
- Nature 625, 468–475 (2024)
- DOI: `10.1038/s41586-023-06924-6`

This establishes prior LLM-enabled mathematical discovery with verifiable outputs.

### 3. ChatGPT-assisted resolution of an open optimization problem — 2025

Jang and Ryu reported a proof of point convergence for Nesterov’s accelerated gradient method and explicitly stated that proof discovery was heavily assisted by ChatGPT.

- *Point Convergence of Nesterov's Accelerated Gradient Method: An AI-Assisted Proof*
- arXiv: `2510.23513`

OpenAI also published an account describing GPT-5 as an unusual mathematical collaborator whose suggestions included flawed and useful directions, with the human mathematician checking, selecting, and writing the final proof.

This is a direct precedent for an acknowledged ChatGPT-assisted open-problem solution.

### 4. Controlled GPT-5 research experiment — 2025

Diez, da Maia, and Nourdin documented an experiment using GPT-5 on quantitative Malliavin–Stein questions.

- *Mathematical research with GPT-5: a Malliavin-Stein experiment*
- arXiv: `2509.03065`

This is a precedent for publicly documenting GPT-5 as a research instrument rather than only a classroom solver.

### 5. LLM provers, verifiers, and Lean checks — 2025

Le Duc and Liberti reported a protocol involving different GPT-5 instances acting as provers and verifiers, followed by Lean verification and human checking of premise/conclusion conformance.

- *Mathematics with large language models as provers and verifiers*
- arXiv: `2510.12829`

This predates the present repository’s use of bounded formal checks as one layer in an LLM-assisted mathematical workflow.

### 6. Detailed human–LLM–symbolic discovery logs — 2026

Xia, Gomes, Selman, and Szeider described a human-directed, LLM-powered, symbolically verified discovery in combinatorial design theory. They reconstructed the process from detailed multi-session interaction logs and formally verified the result in Lean 4.

- *Agentic Neurosymbolic Collaboration for Mathematical Discovery: A Case Study in Combinatorial Design*
- arXiv: `2603.08322`

This is a close precedent for an openly acknowledged human/LLM/symbolic mathematical discovery with detailed process analysis.

### 7. Human interaction with AI-guided mathematical discovery — 2026

Bäuerle and collaborators studied eleven expert mathematicians using AlphaEvolve and characterized iterative human steering, goal formation, and interpretation.

- *Intentmaking and Sensemaking: Human Interaction with AI-Guided Mathematical Discovery*
- arXiv: `2605.05921`

This establishes a broader research literature on human agency inside AI-guided mathematical workflows.

### 8. Human-in-the-loop mathematical workbenches — 2026

MathCoPilot describes an interactive human–AI system in which mathematicians steer a living proof blueprint while agents perform detailed proof and formalization work under continued human guidance.

- *MathCoPilot: An Interactive System for Human-AI Symbiotic Paradigm of Mathematical Research*
- arXiv: `2607.14582`

This is a recent precedent for explicitly designing public human–AI mathematical research infrastructure.

### 9. Public AI-generated formal proof repositories

Other public examples include:

- `google-deepmind/alphaproof-nexus-results`, containing Lean proofs generated by AlphaProof Nexus and accompanying natural-language proofs;
- `math-inc/strongpnt`, containing an AI-generated Lean formalization of the strong prime number theorem completed with targeted human scaffolding and review;
- public formal-mathematics benchmarks and conjecture libraries used to evaluate and guide automated provers.

These projects differ in purpose and governance, but they rule out any broad claim that public, human-guided AI mathematics or AI-generated formal proof records are unprecedented.

## What may distinguish this repository

The present project emphasizes a combined evidence-and-governance structure:

1. one accountable human owner;
2. explicit naming of ChatGPT and the OpenAI institutional boundary;
3. paper-level AI role disclosure;
4. public claim and limitation ledgers;
5. immutable source identities and checksums;
6. executable Python, C, symbolic, and Lean evidence;
7. preserved failures and repairs;
8. separation of internal reproduction from external review;
9. structured counterexample, proof-gap, prior-art, and reproduction channels;
10. controlled promotion from a private research laboratory into bounded public packages.

The focused search found projects containing several of these features, but no exact indexed match to the entire combination. This observation is a **candidate process contribution**, not a first-in-history claim.

## Claims allowed

Allowed:

> Matthew S. Novak and ChatGPT conducted sustained, human-led, AI-assisted mathematical research. This repository publishes selected outcomes, source identities, evidence, formal-verification boundaries, failures, corrections, and open review requests.

> The project is one openly documented case study in the emerging practice of human–AI mathematical research.

> A focused search did not locate an exact prior repository with the same complete evidence-and-governance structure; historical priority for that structure remains unestablished.

Not allowed:

> This is the first human–AI mathematical collaboration.

> ChatGPT had never before helped solve an open mathematical problem.

> OpenAI coauthored or endorsed these results.

> The repository proves that every candidate theorem is correct or globally novel.

## Search limitations

The review covered indexed scholarly sources, arXiv, publisher pages, official AI-laboratory accounts, and public source repositories through July 2026. It cannot exclude:

- unpublished work;
- private repositories;
- differently named but equivalent workflows;
- non-English sources not surfaced by the search;
- older computer-assisted mathematical collaborations that would qualify under a broader definition;
- future corrections to the cited projects’ status.

Historical-priority claims should therefore remain conservative and revisable.

## References

- Davies et al., *Advancing mathematics by guiding human intuition with AI*, Nature 600 (2021), DOI `10.1038/s41586-021-04086-x`.
- Romera-Paredes et al., *Mathematical discoveries from program search with large language models*, Nature 625 (2024), DOI `10.1038/s41586-023-06924-6`.
- Jang and Ryu, *Point Convergence of Nesterov's Accelerated Gradient Method: An AI-Assisted Proof*, arXiv `2510.23513`.
- Diez, da Maia, and Nourdin, *Mathematical research with GPT-5: a Malliavin-Stein experiment*, arXiv `2509.03065`.
- Le Duc and Liberti, *Mathematics with large language models as provers and verifiers*, arXiv `2510.12829`.
- Xia, Gomes, Selman, and Szeider, *Agentic Neurosymbolic Collaboration for Mathematical Discovery*, arXiv `2603.08322`.
- Bäuerle et al., *Intentmaking and Sensemaking*, arXiv `2605.05921`.
- Zhang et al., *MathCoPilot*, arXiv `2607.14582`.
- OpenAI, *How GPT-5 helped mathematician Ernest Ryu solve a 40-year-old open problem*, 24 November 2025.
