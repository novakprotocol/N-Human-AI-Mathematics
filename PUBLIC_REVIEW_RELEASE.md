# Public Review Release Record

## Current Controlling Status -- 29 July 2026

The 27-28 July 2026 HINC-001 and ABF-001 candidate-review packages remain public
and active for technical review. PR #57 is preserved in history, but the owner
has clarified that its full-Lean-hold interpretation does not convert those
releases into inactive or withdrawn artifacts.

The current distinction is:

```text
HINC-001  active public candidate technical review; PARTIAL_PASS bounded Lean
ABF-001   active public candidate technical review; PARTIAL_PASS bounded A01 Lean
FSG-001   private candidate; HOLD -- MATHEMATICAL BLOCKER
ACM-001   hold pending consolidation
FULL_PASS none
```

Full-manuscript Lean verification remains a gold-standard improvement program.
It must not be claimed until every retained manuscript claim is mapped to
compiled Lean declarations or exact imported theorems, the unresolved formal
scope is zero, and the manuscript-to-formal-statement fidelity gate passes.

## Public Candidate Releases

### HINC-001

HINC-001 remains an active candidate public technical-review package. Its
bounded Lean scopes are genuine:

```text
formal status:                PARTIAL_PASS
bounded Lean verification:    PASS
full manuscript formalized:   no
external review:              pending
historical priority:          unestablished
```

The bounded Lean PASS covers the algebraic kernel and coefficient
classifications. The complete revised manuscript remains unformalized,
including major Hochschild, source-algebra, global-preservation,
representability, center, clopen, derived-subgroup, and downstream consequence
claims.

### ABF-001

ABF-001 remains an active candidate public technical-review package. Its bounded
A01 Lean lane is genuine:

```text
formal status:                PARTIAL_PASS
bounded A01 Lean verification: PASS
full manuscript formalized:   no
external review:              pending
historical priority:          unestablished
```

A02-A06 and the complete proof-connected finite atlas remain unformalized.

### FSG-001

FSG-001 is private and paused. A universal arithmetic criterion in the private
candidate manuscript was disproved before public release. The private statement,
proof, tests, formal map, and status records are being corrected and
independently re-audited. No FSG theorem package has been publicly released.

```text
public state:       private candidate
mathematical state: HOLD -- MATHEMATICAL BLOCKER
public release:     not authorized
```

### ACM-001

ACM-001 remains on hold pending consolidation.

## Historical Release Identity

```text
release channel:             public review
version:                     0.1.0-public-review
initial release date:        2026-07-27
repository:                  novakprotocol/N-Human-AI-Mathematics
accountable owner:           Matthew S. Novak
AI assistance:               one or more large language models
specific model disclosed:    no
specific provider disclosed: no
blanket license:             none
DOI:                         not assigned
journal submission:          not initiated
peer-review status:          not peer reviewed
historical priority:         unestablished
```

## Scientific-Status Boundaries

Do not describe HINC-001 or ABF-001 as fully Lean verified, peer reviewed,
externally reproduced, historically first, journal accepted, or formally proved
as complete manuscripts.

Do not describe FSG-001 as released, corrected, review-passed, or authorized for
public theorem release.

Lean verification does not establish external specialist correctness review,
independent outside reproduction, historical priority, novelty, significance,
peer review, journal acceptance, DOI status, or archival publication status.

## Rights

Public visibility permits reading and review. It does not create a blanket
open-source or open-content license. Unless a file-specific notice states
otherwise:

```text
Copyright (c) 2026 Matthew S. Novak. All rights reserved.
```

See `RIGHTS_AND_LICENSING.md` and each paper's terms files.

## Correction Policy

Historical releases and correction records are preserved. Any material
correction, narrowing, supersession, formal completion, or withdrawal must
identify the affected source, claim, evidence, impact, repaired source, and
disposition.