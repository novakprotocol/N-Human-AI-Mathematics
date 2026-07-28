# HINC-001 — Hidden Infinitesimal Noncommutativity

## Full working title

**Hidden Infinitesimal Noncommutativity in Two Binary-Gerstenhaber Endomorphism Monoid Schemes**

```text
public-review version:       0.1.0-public-review
repository visibility:       public
public technical review:     active
public switch executed:      yes
peer reviewed:               no
journal submitted:           no
DOI:                         none
LLM disclosure:              human-led, LLM-assisted
specific model/provider:     not disclosed
```

## Controlling source

Read:

- [`manuscript/HINC-001_REVISED_MANUSCRIPT.md`](manuscript/HINC-001_REVISED_MANUSCRIPT.md)

The earlier four-part manuscript is preserved for provenance but is superseded for release purposes.

## One-paragraph description

Let `F` be a field of characteristic two and let `D=F[epsilon]/(epsilon^2)`. The revised manuscript studies two explicit binary-Gerstenhaber subalgebras of `HH*(D,D)=D[u]`:

```text
E = F + uD[u]
O = D + F epsilon u + u^2D[u].
```

It gives an arbitrary-base candidate classification of their unital, base-linear, degree-preserving endomorphisms preserving cup product and the binary Gerstenhaber bracket. Both representing affine monoid schemes contain the crossing

```text
C = Spec F[x,y]/(x(y-1)).
```

The even object adds a constrained skew square-zero direction; the odd object adds a separate clopen torus unit component.

## Why it is reviewable

The candidate package now contains one integrated human proof rather than a manuscript plus detached corrections. It includes:

- the characteristic-two normalized Hochschild calculation;
- the complete even and odd algebra presentations;
- the odd normal-form proof;
- the generator-to-global biderivation lemma;
- explicit representability;
- the coefficient classifications and composition laws;
- the common crossing comparison;
- the scheme-theoretic center with pointwise-center warning;
- the even unit-group commutator and fppf-derived argument;
- idempotent, geometric, finite-field, and finite-Artin consequences;
- exact formal, computational, and historical-priority boundaries.

## Start here by audience

| Audience | Document |
|---|---|
| General mathematical reader | [`manuscript/HINC-001_REVISED_MANUSCRIPT.md`](manuscript/HINC-001_REVISED_MANUSCRIPT.md) |
| Claim auditor | [`CLAIMS.md`](CLAIMS.md) |
| Proof-dependency reviewer | [`PROOF_MAP.md`](PROOF_MAP.md) |
| Formal methods reviewer | [`FORMAL_VERIFICATION.md`](FORMAL_VERIFICATION.md) |
| Reproducer | [`REPRODUCE.md`](REPRODUCE.md) |
| Prior-art reviewer | [`PRIOR_ART.md`](PRIOR_ART.md) |
| External referee | [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md) |
| LLM system | repository [`AGENTS.md`](../../AGENTS.md), then [`STATUS.json`](STATUS.json) |

## Current evidence state

| Dimension | Status |
|---|---|
| Consolidated revised manuscript | Complete candidate source |
| Human proof | Self-contained; outside audit pending |
| Standalone computational verifier | Passed internally and in a fresh copied workspace |
| Deterministic evidence identity | `20d883988da7818f73de0b4ccab68bc7adea5097a4af7a6ef5a72c23b4e1ea4b` |
| Base Lean kernel | Public hosted PASS under Lean 4.30.0 / Mathlib v4.30.0 |
| Principal coefficient classifications | Public hosted PASS under the same pinned environment |
| Full revised manuscript formalization | Not completed and not claimed |
| External specialist review | Pending; a target of public technical review |
| Independent external reproduction | Pending; a target of public technical review |
| Historical priority | Unestablished |
| Peer-review acceptance | Not established |
| Public technical review | Active; outside review remains pending |
| Specific model/provider disclosure | Withheld |

## Exact formal receipts

### Base Lean kernel

```text
N-MathLab PR:      #412
checker repo:      novakprotocol/novak-sdt
checker PR:        #57
run:               30119931881
artifact SHA-256:  63b2b160da40f722818820679da7c9d22eb7640694e48a5abc08fccf78f47133
```

### Principal coefficient classification

```text
N-MathLab PR:             #416
public checker:           novakprotocol/novak-sdt PR #58
immutable source:         d7751d1de76253407016ef4bf92738cffa800e82
workflow run:             30174213006
workflow job:             89720259114
artifact:                 8623775718
artifact SHA-256:         2dee88b9a248dee8719c27aa23a27ca3281e697cf67202bb50c1fe60a4809dc9
Classification SHA-256:   56267aba47fd67e94be5842057aaec5bd0718829e860af212eedcdb43efbb084
axiom-report SHA-256:     dcd0bbefb6d88e0c70a57dabc0e45c408fe7998ace6b33e330f6f6d44fb5b7ce
sorryAx:                  absent
```

The first classification checker attempt failed on recursive simplification in odd-data extensionality. The failure was preserved. Explicit field substitutions repaired the proof without changing the mathematical normal form, and the immutable rerun passed.

## Safe public claim

> HINC-001 supplies a self-contained candidate arbitrary-base classification of binary-Gerstenhaber endomorphism monoid schemes for two explicit subalgebras of the characteristic-two Hochschild cohomology of the dual numbers. The algebraic kernel and coefficient classifications have bounded public Lean verification; the full revised manuscript does not. External correctness review, independent reproduction, and historical priority remain pending and are objectives of the public technical-review release.

## Human–LLM disclosure

One or more large language models materially assisted the research under Matthew S. Novak’s direction. AI systems are not authors. Specific model and provider identities are not disclosed in this public-review version. Read [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md).

## Review request

The public candidate package will solicit:

- counterexamples;
- proof-gap reports;
- earlier equivalent theorems;
- independent reproductions;
- formalization contributions.

Use [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md) and the repository issue templates after the final visibility switch.

## Not claimed

This package does not claim:

- that the full paper is formally verified;
- that the result is globally unprecedented;
- that no general theorem contains it;
- that internal reproduction is external validation;
- that a GitHub release is peer review;
- that the MCRC family is required for the standalone theorem;
- that the result has a cryptographic consequence;
- that the public record establishes a specific model or provider identity.
