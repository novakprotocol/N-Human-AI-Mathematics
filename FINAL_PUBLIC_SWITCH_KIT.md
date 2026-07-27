# Final public-switch kit identities

## Complete governed kit

```text
file:
N-Human-LLM-Mathematics-Final-Public-Switch-Complete-Kit.zip

SHA-256:
699d6fc60e86376037558bd54bb75fd973c9aada6b108b87575d8f498d4635f6
```

The complete kit contains:

- the guarded private preflight;
- the rollback-capable final activation gate;
- individual script checksums;
- the governed HINC-001 publication artifact ZIP;
- an operator README;
- a complete checksum manifest;
- a machine-readable kit receipt.

The kit is **prepared but not executed**. The repository remains private, PR #2 remains draft, and no merge, visibility change, Pages deployment, tag, or GitHub release has occurred.

## Private preflight

```text
file:
Invoke-PublicSwitchPreflight.ps1

SHA-256:
010abb2172ed97a179e1a2614392aae5f35c07881cd4128ca9b458dea49a3d8c

standalone kit:
N-Human-LLM-Mathematics-Private-Preflight-Kit.zip

standalone kit SHA-256:
5a020039081fdf78dd9b11b66d9f152596edb5de6449920ad150f1762d4b76ac
```

The preflight:

- uses ordinary `github.com` only;
- rejects GitHub Enterprise and VA enterprise resources;
- requires private visibility;
- requires PR #2 to remain open, draft, mergeable, and at the exact cloned head;
- runs both validators, HINC tests, and the common-core verifier;
- verifies the current official GitHub action majors and `.nojekyll` upload control;
- checks the private website boundaries and complete branch whitespace;
- creates a commit-anchored ZIP plus JSON, log, and checksum receipts;
- performs no merge, tag, release, Pages deployment, or visibility change.

## Final activation

```text
file:
FINALIZE-N-HUMAN-LLM-MATHEMATICS-PUBLIC-REVIEW-V1.ps1

SHA-256:
ebf24d2497741042b9899ae8ac694646aa018825fd20360adaf96bbb6e561de0

standalone kit:
N-Human-LLM-Mathematics-Final-Public-Switch-Kit.zip

standalone kit SHA-256:
351ae15312eb77159394319030d0fb359b6c68d70ecded3a35b1949a16265391
```

The activation gate:

- requires the governed private-preflight PASS receipt;
- requires the preflight commit to remain the exact PR head;
- verifies the HINC publication artifact hash;
- marks ready and merges only the validated PR into private `main`;
- reruns validators and HINC tests on private `main`;
- builds and locally validates a public-state activation commit;
- changes visibility and re-reads GitHub metadata;
- deploys Pages through the fail-closed public-state workflow;
- verifies the live site;
- attaches the governed publication package to the GitHub release;
- opens four structured review channels;
- records final local and repository receipts;
- attempts rollback to private visibility if any post-switch gate fails.

## HINC-001 publication artifact

```text
file:
HINC-001_Candidate_Technical_Review_Package_0.1.0.zip

SHA-256:
b357909077792a3e3b124359fa7348c21aea72c5d802c19562b46fa96350c123
```

Artifact QA:

```text
revised manuscript pages:       15
public review guide pages:       4
DOCX accessibility findings:    0
PDF preflight warnings:          0
visual page inspection:          complete
```

## Hard boundary

```text
allowed remote:
github.com/novakprotocol/N-Human-AI-Mathematics

off limits:
all GitHub Enterprise repositories
all VA or government enterprise resources
```

## Release language

HINC-001 may be released only as a **candidate technical-review package**. External specialist review, independent external reproduction, complete manuscript formalization, peer review, journal acceptance, and worldwide historical priority remain unestablished.
