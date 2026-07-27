# Final public-switch kit identities

## Complete governed kit

```text
file:
N-Human-LLM-Mathematics-Final-Public-Switch-Complete-Kit.zip

SHA-256:
f17e486df202fdbe053c3acee6ffbed67ae4471209d84ebae61ec5514c4451fb
```

The complete kit contains:

- guarded private preflight;
- rollback-capable final activation gate;
- individual script checksums;
- the governed HINC-001 publication artifact ZIP;
- instructions and a complete checksum manifest.

## Private preflight

```text
file:
Invoke-PublicSwitchPreflight.ps1

SHA-256:
563f1b171a130a781887549ceda8c6e0912c3f576e0fe1eaf4c9271be6ad9041
```

The preflight:

- uses ordinary `github.com` only;
- rejects GitHub Enterprise;
- requires private visibility;
- requires PR #2 to remain open, draft, mergeable, and at the exact cloned head;
- runs both validators, HINC tests, and the common-core verifier;
- scans paths, credentials, private keys, blanket-license text, and withheld identities;
- checks branch whitespace;
- creates a commit-anchored ZIP and signed JSON/checksum receipt;
- performs no merge, tag, release, Pages deployment, or visibility change.

## Final activation

```text
file:
FINALIZE-N-HUMAN-LLM-MATHEMATICS-PUBLIC-REVIEW-V1.ps1

SHA-256:
1478b3112fcdaf6fc9acf6a75b30d2a8775ce3b4583c22f3d78c5008b128c859
```

The activation gate:

- requires the governed private-preflight PASS receipt;
- requires the preflight commit to remain the exact PR head;
- verifies the HINC publication artifact hash;
- merges only the validated PR;
- reruns validators and HINC tests on private `main`;
- builds and locally validates a public-state activation commit;
- changes visibility and verifies GitHub metadata;
- deploys Pages through the fail-closed public-state workflow;
- verifies the live site;
- attaches the governed publication package to the GitHub release;
- opens structured review channels;
- records final receipts;
- attempts rollback to private visibility if any post-switch gate fails.

## HINC-001 publication artifact

```text
file:
HINC-001_Candidate_Technical_Review_Package_0.1.0.zip

SHA-256:
4bd29a7fa58cf0e9f4f544c888c56c00e257b721aaaafbd860e62a07100a56a7
```

## Hard boundary

```text
allowed remote:
github.com/novakprotocol/N-Human-AI-Mathematics

off limits:
va.ghe.com
all GitHub Enterprise repositories
all VA or government enterprise resources
```

## Release language

HINC-001 may be released only as a **candidate technical-review package**. External specialist review, independent external reproduction, complete manuscript formalization, peer review, journal acceptance, and worldwide historical priority remain unestablished.
