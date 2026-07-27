[CmdletBinding()]
param(
    [string]$Repository = "novakprotocol/N-Human-AI-Mathematics",
    [string]$ReleaseBranch = "release/public-review-v1",
    [int]$PullRequestNumber = 2,
    [string]$WorkDirectory = "C:\Git\N-Human-LLM-Mathematics-Private-Preflight",
    [switch]$KeepWorkDirectory
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$ExpectedHost = "github.com"
$ExpectedRepository = "novakprotocol/N-Human-AI-Mathematics"
$ExpectedLeaf = "N-Human-LLM-Mathematics-Private-Preflight"

if ($Repository -ne $ExpectedRepository) { throw "Unexpected repository: $Repository" }
if ($ReleaseBranch -ne "release/public-review-v1") { throw "Unexpected release branch: $ReleaseBranch" }
if ((Split-Path -Leaf $WorkDirectory) -ne $ExpectedLeaf) { throw "Unexpected work directory: $WorkDirectory" }
if ($Repository -match "(?i)ghe|va\.") { throw "GitHub Enterprise is off limits for this gate." }

$Downloads = Join-Path $env:USERPROFILE "Downloads"
$Stamp = [DateTime]::UtcNow.ToString("yyyyMMddTHHmmssZ")
$LogPath = Join-Path $Downloads "N-Human-LLM-Mathematics-Private-Preflight-$Stamp.log"
$ReceiptPath = Join-Path $Downloads "N-Human-LLM-Mathematics-Private-Preflight-$Stamp.json"
$ArchivePath = Join-Path $Downloads "N-Human-LLM-Mathematics-Private-Preflight-$Stamp.zip"
$ChecksumPath = Join-Path $Downloads "N-Human-LLM-Mathematics-Private-Preflight-$Stamp-SHA256SUMS.txt"

function Write-Log {
    param([string]$Message, [ConsoleColor]$Color = [ConsoleColor]::Gray)
    Write-Host $Message -ForegroundColor $Color
    Add-Content -LiteralPath $LogPath -Value $Message -Encoding UTF8
}

function Invoke-Native {
    param([string]$File, [string[]]$Arguments, [string]$WorkingDirectory, [string]$Label)
    if ($Label) { Write-Log ""; Write-Log "===== $Label =====" Cyan }
    $Old = Get-Location
    $OldPreference = $ErrorActionPreference
    try {
        if ($WorkingDirectory) { Set-Location -LiteralPath $WorkingDirectory }
        $ErrorActionPreference = "Continue"
        $Output = @(& $File @Arguments 2>&1)
        $Code = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $OldPreference
        Set-Location -LiteralPath $Old
    }
    foreach ($Line in $Output) { Write-Log $Line.ToString() }
    if ($Code -ne 0) { throw "Command failed ($Code): $File $($Arguments -join ' ')" }
    return [pscustomobject]@{ ExitCode = $Code; Output = [object[]]$Output }
}

function Get-GhJson {
    param([string[]]$Arguments)
    $Result = Invoke-Native -File "gh.exe" -Arguments $Arguments
    $Text = ($Result.Output | ForEach-Object { $_.ToString() }) -join "`n"
    if (-not $Text) { throw "Empty GitHub JSON response." }
    return $Text | ConvertFrom-Json
}

function Resolve-Python {
    $Python = Get-Command python.exe -ErrorAction SilentlyContinue
    if ($Python) { return [pscustomobject]@{ File = $Python.Source; Prefix = @() } }
    $Py = Get-Command py.exe -ErrorAction SilentlyContinue
    if ($Py) { return [pscustomobject]@{ File = $Py.Source; Prefix = @("-3") } }
    throw "Python 3 was not found."
}

function Write-Utf8NoBom {
    param([string]$Path, [string]$Content)
    [IO.File]::WriteAllText($Path, ($Content -replace "`r`n", "`n" -replace "`r", "`n"), [Text.UTF8Encoding]::new($false))
}

New-Item -ItemType Directory -Force -Path $Downloads | Out-Null
Write-Utf8NoBom -Path $LogPath -Content "N Human-LLM Mathematics private public-switch preflight`n"

foreach ($Command in @("git.exe", "gh.exe")) {
    if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) { throw "Missing command: $Command" }
}
$Python = Resolve-Python

Write-Log "N Human-LLM Mathematics private public-switch preflight" Cyan
Write-Log "Allowed host: github.com"
Write-Log "GitHub Enterprise: OFF LIMITS"

Invoke-Native -File "gh.exe" -Arguments @("auth", "status", "--hostname", $ExpectedHost) -Label "github.com authentication" | Out-Null
$Repo = Get-GhJson @("repo", "view", $Repository, "--json", "nameWithOwner,visibility,defaultBranchRef,url")
if ($Repo.nameWithOwner -ne $Repository) { throw "Repository identity mismatch." }
if ($Repo.visibility -ne "PRIVATE") { throw "Repository must remain PRIVATE during preflight." }
if ($Repo.defaultBranchRef.name -ne "main") { throw "Default branch must be main." }
if ($Repo.url -notlike "https://github.com/*") { throw "Repository is not on github.com." }

$Pr = Get-GhJson @("pr", "view", $PullRequestNumber, "--repo", $Repository, "--json", "state,isDraft,mergeable,headRefName,headRefOid,baseRefName,url")
if ($Pr.state -ne "OPEN") { throw "PR is not open." }
if (-not $Pr.isDraft) { throw "PR must remain draft during preflight." }
if ($Pr.mergeable -ne "MERGEABLE") { throw "PR is not mergeable: $($Pr.mergeable)" }
if ($Pr.headRefName -ne $ReleaseBranch -or $Pr.baseRefName -ne "main") { throw "Unexpected PR branch relationship." }

if (Test-Path -LiteralPath $WorkDirectory) { Remove-Item -LiteralPath $WorkDirectory -Recurse -Force }
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $WorkDirectory) | Out-Null
Invoke-Native -File "git.exe" -Arguments @("clone", "--branch", $ReleaseBranch, "--single-branch", "https://github.com/$Repository.git", $WorkDirectory) -Label "clone release branch" | Out-Null
Invoke-Native -File "git.exe" -Arguments @("fetch", "--no-tags", "origin", "+refs/heads/main:refs/remotes/origin/main") -WorkingDirectory $WorkDirectory -Label "fetch private main" | Out-Null

$Head = ((Invoke-Native -File "git.exe" -Arguments @("rev-parse", "HEAD") -WorkingDirectory $WorkDirectory).Output -join "").Trim()
if ($Head -ne $Pr.headRefOid) { throw "Cloned head does not match PR head." }
$Remote = ((Invoke-Native -File "git.exe" -Arguments @("remote", "get-url", "origin") -WorkingDirectory $WorkDirectory).Output -join "").Trim()
if ($Remote -notmatch "^https://github\.com/novakprotocol/N-Human-AI-Mathematics(?:\.git)?$") { throw "Unexpected Git remote: $Remote" }
$Base = ((Invoke-Native -File "git.exe" -Arguments @("merge-base", "origin/main", "HEAD") -WorkingDirectory $WorkDirectory).Output -join "").Trim()
if ($Base -notmatch "^[0-9a-f]{40}$") { throw "Invalid merge base." }

$Venv = Join-Path $WorkDirectory ".venv"
$VenvPython = Join-Path $Venv "Scripts\python.exe"
$VenvArgs = @(); $VenvArgs += $Python.Prefix; $VenvArgs += @("-m", "venv", $Venv)
Invoke-Native -File $Python.File -Arguments $VenvArgs -WorkingDirectory $WorkDirectory -Label "create isolated Python environment" | Out-Null
Invoke-Native -File $VenvPython -Arguments @("-m", "pip", "install", "--disable-pip-version-check", "-r", "papers/HINC-001/requirements.txt") -WorkingDirectory $WorkDirectory -Label "install HINC requirements" | Out-Null
Invoke-Native -File $VenvPython -Arguments @("-m", "py_compile", "tools/validate_publication.py", "tools/validate_publication_v2.py", "tools/validate_public_release.py", "tools/validate_public_release_v2.py", "tools/validate_public_state.py", "papers/HINC-001/src/standalone_common_core_verifier.py", "papers/HINC-001/tests/test_hinc_standalone.py") -WorkingDirectory $WorkDirectory -Label "compile validators and HINC sources" | Out-Null

$PublicationJson = Join-Path $WorkDirectory "reports\publication-validation-preflight.json"
$SwitchJson = Join-Path $WorkDirectory "reports\public-switch-validation-preflight.json"
Invoke-Native -File $VenvPython -Arguments @("tools/validate_publication_v2.py", "--root", ".", "--json-output", $PublicationJson) -WorkingDirectory $WorkDirectory -Label "publication validator" | Out-Null
Invoke-Native -File $VenvPython -Arguments @("tools/validate_public_release_v2.py", "--root", ".", "--json-output", $SwitchJson) -WorkingDirectory $WorkDirectory -Label "switch-readiness validator" | Out-Null
Invoke-Native -File $VenvPython -Arguments @("-m", "unittest", "discover", "-s", "papers/HINC-001/tests", "-p", "test_*.py", "-v") -WorkingDirectory $WorkDirectory -Label "HINC standalone tests" | Out-Null
Invoke-Native -File $VenvPython -Arguments @("papers/HINC-001/src/standalone_common_core_verifier.py", "--max-n", "4") -WorkingDirectory $WorkDirectory -Label "HINC common-core verifier" | Out-Null
Invoke-Native -File "git.exe" -Arguments @("diff", "--check", $Base, "HEAD", "--") -WorkingDirectory $WorkDirectory -Label "complete branch whitespace" | Out-Null

$Index = Get-Content -LiteralPath (Join-Path $WorkDirectory "research-index.json") -Raw | ConvertFrom-Json
$Hinc = Get-Content -LiteralPath (Join-Path $WorkDirectory "papers\HINC-001\STATUS.json") -Raw | ConvertFrom-Json
$Audit = Get-Content -LiteralPath (Join-Path $WorkDirectory "reports\public-release-audit-2026-07-27.json") -Raw | ConvertFrom-Json
$Ready = Get-Content -LiteralPath (Join-Path $WorkDirectory "reports\public-switch-readiness.json") -Raw | ConvertFrom-Json
if ($Index.public_release_authorized -ne $false -or $Index.public_switch_ready -ne $true -or $Index.release_channel -ne "private_staging") { throw "Research index state failed." }
if ($Hinc.release.public_authorized -ne $false -or $Hinc.release.public_switch_ready -ne $true -or $Hinc.release.channel -ne "private_staging") { throw "HINC release state failed." }
if ($Audit.result -ne "READY_PENDING_VISIBILITY_SWITCH" -or $Ready.result -ne "READY_PENDING_VISIBILITY_SWITCH") { throw "Readiness receipts failed." }

$Site = Get-Content -LiteralPath (Join-Path $WorkDirectory "docs\index.html") -Raw
foreach ($Phrase in @("Private public-switch preview", "Public switch ready", "Peer reviewed</span><strong>No", "Model/provider</dt><dd>Not disclosed", "noindex,nofollow,noarchive,nosnippet", "HINC-001_REVISED_MANUSCRIPT.md")) {
    if ($Site -notlike "*$Phrase*") { throw "Website boundary missing: $Phrase" }
}

$Excluded = @("tools\validate_publication.py", "tools\validate_publication_v2.py", "tools\validate_public_release.py", "tools\validate_public_release_v2.py", "tools\Invoke-PublicSwitchPreflight.ps1")
$Withheld = @(("Chat" + "GPT"), ("Open" + "AI"), ("GPT" + "-5"), ("GPT" + "-4"))
$Findings = @()
foreach ($File in Get-ChildItem -LiteralPath $WorkDirectory -File -Recurse) {
    if ($File.FullName -match "\\.git(\\|$)|\\.venv(\\|$)|__pycache__|\.pyc$") { continue }
    if (@(".md", ".txt", ".json", ".yml", ".yaml", ".cff", ".py", ".ps1", ".lean", ".tex", ".bib", ".toml", ".html", ".css", ".js", ".xml", ".cmd") -notcontains $File.Extension.ToLowerInvariant()) { continue }
    $Relative = $File.FullName.Substring($WorkDirectory.Length).TrimStart("\")
    if ($Excluded -contains $Relative) { continue }
    $Text = Get-Content -LiteralPath $File.FullName -Raw -Encoding UTF8
    if ($Text -match "[A-Za-z]:\\Users\\[^\\\s]+") { $Findings += "Personal path: $Relative" }
    if ($Text -match "(?:gh[oprsu]_|github_pat_)[A-Za-z0-9_]{20,}") { $Findings += "Credential: $Relative" }
    if ($Text -match "-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----") { $Findings += "Private key: $Relative" }
    if ($Text -match "Permission is hereby granted, free of charge, to any person obtaining a copy") { $Findings += "Blanket MIT grant: $Relative" }
    foreach ($Name in $Withheld) { if ($Text.IndexOf($Name, [StringComparison]::OrdinalIgnoreCase) -ge 0) { $Findings += "Withheld identity: $Relative" } }
}
if ($Findings.Count -ne 0) { throw "Public-source scan failed:`n$($Findings -join "`n")" }

$Publication = Get-Content -LiteralPath $PublicationJson -Raw | ConvertFrom-Json
$Switch = Get-Content -LiteralPath $SwitchJson -Raw | ConvertFrom-Json
if ($Publication.result -ne "PASS" -or $Publication.error_count -ne 0) { throw "Publication receipt failed." }
if ($Switch.result -ne "PASS" -or $Switch.error_count -ne 0) { throw "Switch receipt failed." }

if (Test-Path -LiteralPath $ArchivePath) { Remove-Item -LiteralPath $ArchivePath -Force }
Invoke-Native -File "git.exe" -Arguments @("archive", "--format=zip", "--output=$ArchivePath", "HEAD") -WorkingDirectory $WorkDirectory -Label "create commit-anchored archive" | Out-Null
$ArchiveHash = (Get-FileHash -LiteralPath $ArchivePath -Algorithm SHA256).Hash.ToLowerInvariant()
$LogHash = (Get-FileHash -LiteralPath $LogPath -Algorithm SHA256).Hash.ToLowerInvariant()

$Receipt = [ordered]@{
    schema_version = "n.human_ai_mathematics.private_public_switch_preflight.v1"
    result = "PASS"
    repository = $Repository
    host = $ExpectedHost
    github_enterprise_used = $false
    repository_visibility = $Repo.visibility
    pull_request_url = $Pr.url
    pull_request_draft = $Pr.isDraft
    pull_request_mergeable = $Pr.mergeable
    release_branch = $ReleaseBranch
    release_commit = $Head
    merge_base = $Base
    candidate_version = "0.1.0-public-review-candidate"
    public_switch_ready = $true
    merge_executed = $false
    visibility_change_executed = $false
    pages_deployment_executed = $false
    publication_validation = $Publication.result
    switch_validation = $Switch.result
    hinc_tests = "PASS"
    common_core_verifier = "PASS"
    whitespace = "PASS"
    source_hygiene = "PASS"
    archive_path = $ArchivePath
    archive_sha256 = $ArchiveHash
    log_path = $LogPath
    log_sha256 = $LogHash
    peer_reviewed = $false
    historical_priority_established = $false
    next_gate = "private merge and final owner-controlled public switch"
    created_utc = [DateTime]::UtcNow.ToString("o")
}
Write-Utf8NoBom -Path $ReceiptPath -Content (($Receipt | ConvertTo-Json -Depth 20) + "`n")
$ReceiptHash = (Get-FileHash -LiteralPath $ReceiptPath -Algorithm SHA256).Hash.ToLowerInvariant()
Write-Utf8NoBom -Path $ChecksumPath -Content ("$ArchiveHash  $([IO.Path]::GetFileName($ArchivePath))`n$LogHash  $([IO.Path]::GetFileName($LogPath))`n$ReceiptHash  $([IO.Path]::GetFileName($ReceiptPath))`n")

Write-Log ""
Write-Log "PASS - private public-switch preflight completed." Green
Write-Log "Release commit: $Head"
Write-Log "Candidate archive: $ArchivePath"
Write-Log "Archive SHA-256: $ArchiveHash"
Write-Log "Receipt: $ReceiptPath"
Write-Log "Receipt SHA-256: $ReceiptHash"
Write-Log "No merge, tag, release, Pages deployment, visibility change, or GitHub Enterprise access occurred." Yellow

if (-not $KeepWorkDirectory) {
    Remove-Item -LiteralPath $WorkDirectory -Recurse -Force
    Write-Log "Temporary preflight checkout removed."
}
