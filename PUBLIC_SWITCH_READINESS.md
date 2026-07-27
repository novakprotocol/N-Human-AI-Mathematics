# Public-switch readiness

## Decision

```text
repository:                  novakprotocol/N-Human-AI-Mathematics
visibility now:              private
proposed channel:            public technical review
candidate version:           0.1.0-public-review-candidate
controlling paper package:   HINC-001
public switch ready:         yes
visibility change executed:  no
Pages deployment executed:   no
peer reviewed:               no
journal submitted:           no
DOI assigned:                no
historical priority:         unestablished
specific model disclosed:    no
specific provider disclosed: no
```

The repository is prepared so that the final owner-controlled operation can change visibility and activate the public-review site without further mathematical rewriting.

## What “ready” means

Ready for public technical review means:

1. HINC-001 has one controlling, consolidated, self-contained revised manuscript.
2. The hostile-review corrections are integrated rather than left as detached errata.
3. The public claim is explicitly a **candidate classification**, not peer-reviewed or historically first mathematics.
4. The machine-readable claim matrix distinguishes human proof, computation, bounded Lean verification, external review, and historical priority.
5. External specialist review and independent reproduction are marked pending and are objectives of public release.
6. The repository contains no blanket license grant, personal workstation path, known credential pattern, private-key material, private chat transcript, or hidden chain-of-thought publication.
7. The public wording is category-level **Human-led, LLM-assisted**; no specific model or provider is disclosed.
8. The public website displays candidate, formal-verification, peer-review, and historical-priority limits above the fold.
9. The private and public workflows use current official GitHub action majors and preserve the hidden `.nojekyll` file in the Pages artifact.
10. The repository remains private until a separate final switch operation succeeds and is re-read from GitHub.

## HINC-001 evidence state

### Complete human proof in the controlling manuscript

The revised manuscript includes:

- the characteristic-two normalized Hochschild cochain calculation;
- the binary Gerstenhaber bracket formula;
- complete presentations of the even and odd algebras;
- the odd normal-form proof;
- the generator-to-global biderivation lemma;
- explicit natural representability arguments;
- the even and odd coefficient classifications;
- the common crossing and paired modifications;
- the scheme-theoretic center with pointwise-center warning;
- the unit-group commutator and fppf-derived subgroup argument;
- idempotent, geometric, finite-field, and finite-Artin consequences;
- the evidence and prior-art boundaries.

### Formally verified scope

Two bounded public Lean gates verify the algebraic kernel, coefficient equations, normalized composition laws, commutativity defect, sufficient center equations, and unit-group commutator.

The complete revised manuscript is not formally verified. The unformalized statements are listed in `papers/HINC-001/STATUS.json` and `papers/HINC-001/CLAIMS.md`.

### Internal computation

The package preserves Python, C, Gröbner, finite-Artin, and standalone common-core challenge routes. These are internal evidence. No outside reproduction is claimed.

## Governed local gate

Private hosted jobs currently fail before exposing an executed step. The repository records that infrastructure limitation without asserting its platform or billing cause.

The authoritative private gate is the downloadable guarded preflight:

```text
Invoke-PublicSwitchPreflight.ps1
SHA-256:
010abb2172ed97a179e1a2614392aae5f35c07881cd4128ca9b458dea49a3d8c
```

It uses ordinary `github.com` only, rejects GitHub Enterprise, validates the exact PR head, runs the validators and HINC tests, verifies workflow action majors, checks the site and whitespace, and produces a commit-anchored archive and receipt without changing repository state.

The rollback-capable activation gate is:

```text
FINALIZE-N-HUMAN-LLM-MATHEMATICS-PUBLIC-REVIEW-V1.ps1
SHA-256:
ebf24d2497741042b9899ae8ac694646aa018825fd20360adaf96bbb6e561de0
```

The complete governed switch kit is:

```text
N-Human-LLM-Mathematics-Final-Public-Switch-Complete-Kit.zip
SHA-256:
699d6fc60e86376037558bd54bb75fd973c9aada6b108b87575d8f498d4635f6
```

## Public-review purpose

The public repository will ask readers to:

- provide counterexamples;
- identify proof gaps;
- locate earlier equivalent work;
- reproduce the source independently;
- formalize currently unformalized nodes;
- propose corrections tied to exact source identities.

Public visibility is therefore the beginning of outside review, not a false assertion that outside review has already occurred.

## Publication order

1. `HINC-001` — active candidate public-review package.
2. `ABF-001` — next package; index entry only at first launch.
3. `FSG-001` — hold.
4. `ACM-001` — hold pending consolidation.

## Final switch operation

The eventual switch must perform, in order:

1. run the guarded private preflight against the exact current PR head;
2. verify its JSON receipt and checksum manifest;
3. mark the release PR ready and merge it into private `main`;
4. re-run validation on private `main`;
5. build and validate the public-state activation commit;
6. set repository visibility to public;
7. re-read GitHub metadata and require `PUBLIC`;
8. activate the validated GitHub Pages workflow;
9. verify the live site and all primary boundaries;
10. create the public-review tag, release, artifact attachment, structured review channels, and final receipts.

No partial success may be represented as a completed public release.
