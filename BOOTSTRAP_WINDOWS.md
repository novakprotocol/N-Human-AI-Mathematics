# Windows bootstrap: N Human–AI Mathematics

This guide creates the standalone private repository:

```text
novakprotocol/N-Human-AI-Mathematics
```

from the curated export stored in the private `novakprotocol/N-MathLab` repository.

## Critical repository boundary

Run the bootstrap from **N-MathLab**, not from `N-LMS` or another N repository.

The correct local source directory is normally:

```text
C:\Git\N-MathLab
```

The bootstrap script verifies the `origin` remote and refuses to proceed when the detected repository is not `N-MathLab`.

## Supported shell

Windows PowerShell 5.1 is supported.

You do **not** need PowerShell 7, and the command `pwsh` is not required. Use:

```text
powershell.exe
```

## Prerequisites

The following commands must be available:

```powershell
git --version
python --version
gh --version
gh auth status
```

The active `github.com` account must have permission to create repositories under `novakprotocol`.

## Exact clean-run commands

Open Windows PowerShell and run this block:

```powershell
$ErrorActionPreference = "Stop"

$Lab = "C:\Git\N-MathLab"
$Branch = "agent/n-human-ai-mathematics-publication-bootstrap-v1"

if (-not (Test-Path -LiteralPath "$Lab\.git" -PathType Container)) {
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Lab) | Out-Null
    git clone https://github.com/novakprotocol/N-MathLab.git $Lab
}

Set-Location -LiteralPath $Lab

git fetch origin --prune
git switch --force-create $Branch --track "origin/$Branch"

powershell.exe `
    -NoLogo `
    -NoProfile `
    -ExecutionPolicy Bypass `
    -File ".\exports\N-Human-AI-Mathematics\tools\Initialize-N-Human-AI-Mathematics.ps1"
```

The initialization script also resolves the remote-tracking branch directly after `git fetch`, so the source identity remains stable even when the local tracking branch did not previously exist.

## One-click launcher

After switching to the bootstrap branch, this launcher runs the same process and keeps the window open so that failures remain visible:

```powershell
& ".\exports\N-Human-AI-Mathematics\RUN-INITIALIZE-N-HUMAN-AI-MATHEMATICS.cmd"
```

## Safe local-only validation

To materialize and validate the complete repository without creating anything on GitHub:

```powershell
powershell.exe `
    -NoLogo `
    -NoProfile `
    -ExecutionPolicy Bypass `
    -File ".\exports\N-Human-AI-Mathematics\tools\Initialize-N-Human-AI-Mathematics.ps1" `
    -SkipGitHubCreate `
    -KeepWorkDirectory
```

The staged repository is written beneath:

```text
%TEMP%\N-Human-AI-Mathematics-Bootstrap\repository
```

## Expected final state

A successful full run produces:

```text
GitHub repository:  novakprotocol/N-Human-AI-Mathematics
Visibility:         private
Default branch:     main
Public release:     unauthorized
Blanket MIT license:no
Initial paper:      HINC-001
Validation receipt: reports/publication-validation.json
Bootstrap receipt:  BOOTSTRAP_RECEIPT.json
```

The script refuses to overwrite an existing GitHub repository with the same name.

## Verification commands

After a successful run:

```powershell
gh repo view novakprotocol/N-Human-AI-Mathematics `
    --json nameWithOwner,visibility,defaultBranchRef,url

git -C "$env:TEMP\N-Human-AI-Mathematics-Bootstrap\repository" status --short
git -C "$env:TEMP\N-Human-AI-Mathematics-Bootstrap\repository" log -1 --oneline
```

The local status should be clean.

## Common failures

### `fatal: invalid reference`

Cause: the branch was requested from the wrong repository or the remote refs were not fetched.

Repair:

```powershell
Set-Location C:\Git\N-MathLab
git fetch origin --prune
git branch -r --list "origin/agent/n-human-ai-mathematics-publication-bootstrap-v1"
```

### `pwsh is not recognized`

Cause: PowerShell 7 is not installed.

Repair: use `powershell.exe`, which is included with Windows PowerShell 5.1.

### Script path not found

Cause: the bootstrap branch is not checked out, or the current directory is not `N-MathLab`.

Repair:

```powershell
Set-Location C:\Git\N-MathLab
git fetch origin --prune
git switch --force-create agent/n-human-ai-mathematics-publication-bootstrap-v1 `
    --track origin/agent/n-human-ai-mathematics-publication-bootstrap-v1
```

### Target repository already exists

The bootstrap stops deliberately. Inspect the existing repository before deciding whether to retain, rename, archive, or delete it:

```powershell
gh repo view novakprotocol/N-Human-AI-Mathematics
```

Do not rerun with destructive workarounds.
