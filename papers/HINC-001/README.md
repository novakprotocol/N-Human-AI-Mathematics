# HINC-001 — Hidden Infinitesimal Noncommutativity

## Full working title

**Hidden Infinitesimal Noncommutativity in Endomorphism Monoids of Two Graded Gerstenhaber Algebras**

```text
release channel: public review
version:         0.1.0-public-review
peer reviewed:   no
DOI:             none
AI disclosure:   human-led, LLM-assisted
model/provider:  not publicly identified
```

## One-paragraph description

Let `F` be a field of characteristic two and let `D = F[ε]/(ε²)`. Inside the Hochschild Gerstenhaber algebra `HH*(D) ≅ D[u]`, the paper defines two explicit graded Gerstenhaber subalgebras, called `E` and `O`, and classifies their strict graded Gerstenhaber endomorphism monoid schemes over arbitrary commutative `F`-algebras. Both classifications contain the same reduced crossing

```text
C = Spec F[x,y]/(x(y-1)),
```

but they enlarge it in fundamentally different ways. The even object is a connected square-zero skew thickening whose universal multiplication is noncommutative; the odd object is a reduced commutative clopen unit doubling. Ordinary field-valued points cannot see the square-zero direction, so the even symmetry can look commutative and central at every ordinary point while failing universally.

## Why the result is interesting

The paper gives an explicit example of a general warning in scheme-valued symmetry:

> Pointwise behavior over reduced fields can miss infinitesimal noncommutativity and can give the wrong answer to a universal center question.

The result may be useful as:

- a concrete candidate classification of two Gerstenhaber endomorphism monoids;
- an example separating reduced-point behavior from scheme-valued behavior;
- a characteristic-two parity phenomenon;
- a formal-verification case study for algebraic monoid calculations;
- a human-led, LLM-assisted mathematical research case study.

## Start here by audience

| Audience | Document |
|---|---|
| New to the mathematics | [`PLAIN_LANGUAGE.md`](PLAIN_LANGUAGE.md) |
| Specialist reader | [`manuscript/MANUSCRIPT_INDEX.md`](manuscript/MANUSCRIPT_INDEX.md) |
| Proof auditor | [`PROOF_MAP.md`](PROOF_MAP.md) and [`CLAIMS.md`](CLAIMS.md) |
| Formal methods reviewer | [`FORMAL_VERIFICATION.md`](FORMAL_VERIFICATION.md) |
| Reproducer | [`REPRODUCE.md`](REPRODUCE.md) |
| Prior-art reviewer | [`PRIOR_ART.md`](PRIOR_ART.md) |
| External referee | [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md) |
| AI system | repository `AGENTS.md`, then [`STATUS.json`](STATUS.json) |
| Human–LLM process reviewer | repository `HUMAN_AI_COLLABORATION_RECORD.md` |

## Current status

| Dimension | Status |
|---|---|
| Self-contained manuscript | Complete candidate source, publicly released for review |
| Human proof | Complete candidate proof; external correctness review pending |
| Standalone computational verifier | Passed internally and in a fresh copied workspace |
| Deterministic evidence identity | `20d883988da7818f73de0b4ccab68bc7adea5097a4af7a6ef5a72c23b4e1ea4b` |
| Base Lean kernel | Public hosted PASS under Lean 4.30.0 / Mathlib v4.30.0 |
| Principal coefficient classifications | Public hosted Lean PASS under the same pinned environment |
| Generator-to-global Gerstenhaber preservation | Not yet formalized |
| Full manuscript formalization | Incomplete |
| External specialist review | Pending |
| Historical-equivalence review | Pending |
| Worldwide novelty | Unestablished |
| Peer-review acceptance | Not established |
| Public review authorization | **True — version 0.1.0-public-review** |
| Specific model/provider disclosure | Withheld pending separate human review |

## Exact source provenance

### Standalone manuscript and verifier

```text
repository:  novakprotocol/N-MathLab
PR:          #406
branch:      agent/mcrc-hidden-infinitesimal-noncommutativity-submission-v1
commit:      e6adac212150177d4afa56e643d37533a208693c
```

### Publicly compiled base Lean kernel

```text
N-MathLab PR:      #412
source branch:     agent/hinc-lean-kernel-v1
source head:       4b46df5e901fc322af5402c957df788be8a416ca
compiled source:   8ccf90b05a0ab4fb45774e9dd8ba7b3c9a59cd8c
checker repo:      novakprotocol/novak-sdt
checker PR:        #57
run:               30119931881
job:               89569737408
artifact:          8606983225
artifact SHA-256:  63b2b160da40f722818820679da7c9d22eb7640694e48a5abc08fccf78f47133
```

### Publicly compiled principal classification

```text
N-MathLab PR:             #416
N-MathLab head:           53f2ccbeb13b64864c5db6ab9ee66d2dc672d112
public checker:           novakprotocol/novak-sdt PR #58
immutable source:         d7751d1de76253407016ef4bf92738cffa800e82
workflow run:             30174213006
workflow job:             89720259114
artifact:                 8623775718
artifact SHA-256:         2dee88b9a248dee8719c27aa23a27ca3281e697cf67202bb50c1fe60a4809dc9
Classification SHA-256:   56267aba47fd67e94be5842057aaec5bd0718829e860af212eedcdb43efbb084
axiom-report SHA-256:     dcd0bbefb6d88e0c70a57dabc0e45c408fe7998ace6b33e330f6f6d44fb5b7ce
```

The first classification checker attempt failed on recursive simplification in odd-data extensionality. The failure is preserved. Explicit field substitutions repaired the proof without changing the mathematical normal form, and the immutable rerun passed with no `sorryAx`.

## Public claim

The safe current statement is:

> We provide a self-contained candidate classification of the graded strict Gerstenhaber endomorphism monoid schemes of two explicit subalgebras of the Hochschild cohomology of the dual numbers in characteristic two. The common crossing/skew kernel and the principal even and odd coefficient classifications are publicly proof-assistant verified under a pinned Lean environment. The complete generator-to-global preservation, scheme representability, clopen decomposition, center, and derived-subgroup portions of the manuscript are not yet fully formalized. External correctness, equivalence, historical priority, and peer review remain pending.

## Human–LLM disclosure

One or more large language models materially assisted the research under Matthew S. Novak’s direction. AI systems are not authors. Specific model and provider identities are not disclosed in this public-review version. Read [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md).

## Review request

The package is public specifically to solicit:

- counterexamples;
- proof-gap reports;
- earlier equivalent theorems;
- independent reproductions;
- formalization contributions.

Use [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md) and the repository issue templates.

## Not claimed

This package does not claim:

- that the full paper is already formally verified;
- that the result is globally unprecedented;
- that no general theorem contains it;
- that an internal simulated referee is external peer review;
- that compilation proves importance;
- that the MCRC family is required for the standalone theorem;
- that the result has a cryptographic consequence;
- that the public record establishes a specific model or provider identity.
