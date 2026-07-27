# Final owner-controlled public switch

## Preconditions

The final switch must not begin until the guarded private preflight produces a receipt with:

```text
result:                    PASS
repository visibility:     PRIVATE
PR state:                  OPEN DRAFT
PR mergeability:           MERGEABLE
publication validation:    PASS
switch validation:         PASS
HINC tests:                PASS
common-core verifier:      PASS
source hygiene:            PASS
whitespace:                PASS
public switch ready:       true
```

The receipt commit must equal the current head of PR #2.

## Required artifact

```text
HINC-001_Candidate_Technical_Review_Package_0.1.0.zip
SHA-256:
4bd29a7fa58cf0e9f4f544c888c56c00e257b721aaaafbd860e62a07100a56a7
```

## Controlled sequence

1. Verify `github.com` authentication and reject every Enterprise endpoint.
2. Verify the private repository, default branch, PR state, and exact preflight commit.
3. Mark PR #2 ready and squash-merge it into private `main`.
4. Clone private `main` and rerun the private validators and HINC tests.
5. Build a public-state activation commit locally and run the post-switch source validator against it.
6. Change visibility to public.
7. Fast-forward `main` to the validated activation commit.
8. Re-read GitHub metadata and require public visibility and the expected main commit.
9. Enable GitHub Pages with workflow builds.
10. Dispatch `.github/workflows/pages.yml` with the exact confirmation phrase.
11. Require successful public-state validation, HINC tests, and Pages deployment.
12. Fetch the live site and verify its principal status language.
13. Commit the final live-site receipt, tag `public-review-v1`, and create the GitHub release.
14. Verify and attach the HINC artifact ZIP.
15. Open counterexample, proof-gap, prior-art, reproduction, and formalization review channels.
16. Write a local final receipt and checksum manifest.

## Rollback rule

If any gate fails after visibility changes, the release procedure must attempt to restore private visibility and preserve a failure receipt. No partial sequence may be described as a completed public release.

## Hard boundary

```text
allowed remote:
github.com/novakprotocol/N-Human-AI-Mathematics

off limits:
va.ghe.com
all GitHub Enterprise repositories
all VA or government enterprise resources
```
