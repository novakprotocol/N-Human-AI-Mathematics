# Final public-switch kit identities

## Complete governed kit

```text
file:
N-Human-LLM-Mathematics-Final-Public-Switch-Complete-Kit.zip

SHA-256:
b013212cd8022c84ef95b5cafd33de917d6d043c85c1a434bd22cac7ea887fef
```

The complete kit contains:

- a hash-verified private-preflight launcher;
- the guarded private preflight;
- a hash-verified publication launcher with an exact confirmation phrase;
- the rollback-capable final activation gate;
- individual script checksums;
- the governed HINC-001 publication artifact ZIP;
- an operator README;
- a complete checksum manifest;
- a machine-readable kit receipt.

The kit is **prepared but not executed**. The repository remains private, PR #2 remains draft, and no merge, visibility change, Pages deployment, tag, or GitHub release has occurred.

## Private preflight launcher

```text
file:
RUN-N-HUMAN-LLM-PRIVATE-PREFLIGHT.ps1

SHA-256:
f86b7c6965c7eb84cfa5a7801e8ac68c3c82a29754288a6c1a34eb4760f201ea
```

The launcher discovers the governed preflight in `Downloads`, verifies its SHA-256, runs the Windows PowerShell parser, and invokes it only after both gates pass.

## Private preflight

```text
file:
Invoke-PublicSwitchPreflight.ps1

SHA-256:
c5b8d1efa9e9650d10bf42ed184602bc2c631b635ac3cd390a6073d4bc587b1e

standalone kit:
N-Human-LLM-Mathematics-Private-Preflight-Kit.zip

standalone kit SHA-256:
7277673b5a138cba23faa749ea074e3d9732afe728c6ea62d81e6615a251c087
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

## Frozen workflow controls

```text
actions/checkout@v7
actions/setup-python@v7
actions/upload-artifact@v7
actions/configure-pages@v6
actions/upload-pages-artifact@v5
actions/deploy-pages@v5
include-hidden-files: true
```

## Final publication launcher

```text
file:
RUN-N-HUMAN-LLM-FINAL-PUBLIC-SWITCH.ps1

SHA-256:
593e849d9e50b9dc63f11c7b3e4527e4767de3e6b7c606b35ddfa6a3caa07023
```

The launcher discovers the governed activation script in `Downloads`, verifies its SHA-256, runs the Windows PowerShell parser, and requires the exact case-sensitive phrase:

```text
PUBLISH-HINC-001
```

before any public-switch operation can start.

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
