# Claim Levels

Every public statement must use one of the following evidence levels or a more conservative description.

| Level | Label | Minimum requirement | Permitted wording |
|---:|---|---|---|
| 0 | Idea | Informal concept only | “We propose…” |
| 1 | Precise conjecture | Definitions, assumptions, exact statement | “We conjecture…” |
| 2 | Candidate proof | Complete written argument supplied | “We provide a candidate proof…” |
| 3 | Internally checked theorem | Written proof plus declared internal challenge routes | “The project’s proof and internal checks support…” |
| 4 | Exact finite classification | Exhaustive computation over a fully specified finite domain | “Exhaustively classified for the stated finite domain…” |
| 5 | Proof-assistant verified scope | Listed declarations compile under a pinned environment without unapproved placeholders | “The listed declarations are proof-assistant verified…” |
| 6 | Externally reproduced | Independent person or institution publishes a reproduction | “Independently reproduced by…” |
| 7 | Externally reviewed | Identified qualified reviewers have audited correctness/equivalence | “Externally reviewed, subject to the recorded scope…” |
| 8 | Peer reviewed | Accepted through an identified journal or conference process | “Peer reviewed and published in…” |
| 9 | Historical priority supported | Source-level review supports the precise novelty boundary | “The review supports priority for…” |

## Independent dimensions

Correctness, novelty, importance, formal verification, reproduction, peer review, and security relevance are different dimensions. A result may be high on one and low on another.

For example:

```text
proof_assistant_verified = true
historical_priority_established = false
peer_reviewed = false
```

is a coherent status.

## Prohibited upgrades

Do not infer:

```text
large test count -> proof
proof -> novelty
novelty -> importance
GitHub publication -> peer review
formal kernel -> full manuscript verification
no search match -> historical absence
AI confidence -> authority
```

## Security language

A paper may study a cryptographic component without establishing a vulnerability. Terms such as “break,” “attack,” “collision,” “preimage,” “security weakness,” or “record” require an exact threat model and evidence directly supporting that term.

## Status storage

Each paper must store these dimensions separately in a machine-readable status file. A single word such as `proved` is insufficient for a mixed human/computational/formal package.
