[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$Repository = "novakprotocol/N-Human-AI-Mathematics",
    [string]$BootstrapRef = "agent/n-human-ai-mathematics-publication-bootstrap-v1",
    [string]$OutputDirectory = (Join-Path $env:TEMP "N-Human-AI-Mathematics-Bootstrap"),
    [string]$PrivateSourceRemotePattern = $env:NHAIM_PRIVATE_SOURCE_REMOTE_PATTERN,
    [switch]$SkipGitHubCreate,
    [switch]$KeepWorkDirectory
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Require-Command {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name
    )

    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command was not found: $Name"
    }
}

function Invoke-Native {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,

        [Parameter(Mandatory = $true)]
        [string[]]$Arguments,

        [string]$WorkingDirectory
    )

    $PreviousLocation = Get-Location
    $PreviousErrorActionPreference = $ErrorActionPreference
    $ExitCode = $null

    try {
        if ($WorkingDirectory) {
            Set-Location -LiteralPath $WorkingDirectory
        }

        # Native tools commonly write progress to stderr. Under Windows
        # PowerShell 5.1, ErrorActionPreference=Stop can incorrectly convert
        # that stream into a terminating NativeCommandError before the exit
        # code can be inspected. Continue locally, then fail on the real code.
        $ErrorActionPreference = "Continue"
        & $FilePath @Arguments
        $ExitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $PreviousErrorActionPreference
        Set-Location $PreviousLocation
    }

    if ($ExitCode -ne 0) {
        throw "Command failed ($ExitCode): $FilePath $($Arguments -join ' ')"
    }
}

function Invoke-NativeCapture {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,

        [Parameter(Mandatory = $true)]
        [string[]]$Arguments,

        [string]$WorkingDirectory
    )

    $PreviousLocation = Get-Location
    $PreviousErrorActionPreference = $ErrorActionPreference
    $ExitCode = $null
    $Captured = @()

    try {
        if ($WorkingDirectory) {
            Set-Location -LiteralPath $WorkingDirectory
        }

        $ErrorActionPreference = "Continue"
        $Captured = @(& $FilePath @Arguments 2>&1)
        $ExitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $PreviousErrorActionPreference
        Set-Location $PreviousLocation
    }

    return [pscustomobject]@{
        ExitCode = $ExitCode
        Output = [object[]]$Captured
    }
}

function Test-GitHubRepositoryExists {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepositoryName
    )

    $Probe = Invoke-NativeCapture `
        -FilePath "gh" `
        -Arguments @(
            "repo", "view", $RepositoryName,
            "--json", "nameWithOwner"
        )

    return ($Probe.ExitCode -eq 0)
}

function Resolve-GitCommit {
    param(
        [Parameter(Mandatory = $true)]
        [string]$GitRepository,

        [Parameter(Mandatory = $true)]
        [string]$Ref
    )

    $Candidates = @()
    if ($Ref -match '^[0-9a-fA-F]{40}$') {
        $Candidates += $Ref
    }
    else {
        $Candidates += "refs/heads/$Ref"
        $Candidates += "refs/remotes/origin/$Ref"
        $Candidates += $Ref
    }

    foreach ($Candidate in ($Candidates | Select-Object -Unique)) {
        $Resolution = Invoke-NativeCapture `
            -FilePath "git" `
            -Arguments @(
                "-C", $GitRepository,
                "rev-parse", "--verify",
                "$Candidate^{commit}"
            )

        if ($Resolution.ExitCode -eq 0) {
            $Commit = (($Resolution.Output | ForEach-Object { $_.ToString() }) -join "").Trim()
            if ($Commit -match '^[0-9a-f]{40}$') {
                return $Commit
            }
        }
    }

    throw @"
Unable to resolve bootstrap ref: $Ref

Tried:
  - local branch
  - origin remote-tracking branch
  - literal ref or commit

Run:
  git -C "$GitRepository" fetch origin --prune
and verify that the bootstrap branch or commit exists.
"@
}

function Resolve-PythonInvocation {
    if (Get-Command python -ErrorAction SilentlyContinue) {
        return [pscustomobject]@{
            Command = "python"
            Prefix = @()
        }
    }

    if (Get-Command py -ErrorAction SilentlyContinue) {
        return [pscustomobject]@{
            Command = "py"
            Prefix = @("-3")
        }
    }

    throw "Python 3 was not found. Install Python 3 and ensure either 'python' or 'py' is on PATH."
}

function Write-Utf8NoBom {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter(Mandatory = $true)]
        [string]$Text
    )

    $Parent = Split-Path -Parent $Path
    if ($Parent) {
        New-Item -ItemType Directory -Force -Path $Parent | Out-Null
    }

    $Encoding = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Text, $Encoding)
}

function Export-GitTextFile {
    param(
        [Parameter(Mandatory = $true)]
        [string]$GitRepository,

        [Parameter(Mandatory = $true)]
        [string]$Commit,

        [Parameter(Mandatory = $true)]
        [string]$SourcePath,

        [Parameter(Mandatory = $true)]
        [string]$TargetPath
    )

    $Spec = "${Commit}:${SourcePath}"
    $Result = Invoke-NativeCapture `
        -FilePath "git" `
        -Arguments @(
            "-C", $GitRepository,
            "show", $Spec
        )

    if ($Result.ExitCode -ne 0) {
        $Details = ($Result.Output | ForEach-Object { $_.ToString() }) -join "`n"
        throw "Unable to read Git object: $Spec`n$Details"
    }

    $Text = ($Result.Output | ForEach-Object { $_.ToString() }) -join "`n"
    if (-not $Text.EndsWith("`n")) {
        $Text += "`n"
    }

    Write-Utf8NoBom -Path $TargetPath -Text $Text
}

Require-Command -Name "git"
$Python = Resolve-PythonInvocation

if (-not $SkipGitHubCreate) {
    Require-Command -Name "gh"
    Invoke-Native `
        -FilePath "gh" `
        -Arguments @(
            "auth", "status",
            "--hostname", "github.com"
        )
}

# tools/ -> N-Human-AI-Mathematics/ -> exports/ -> private research source root
$LabRepo = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
if (-not (Test-Path -LiteralPath (Join-Path $LabRepo ".git"))) {
    throw @"
The script must run from the private research source export tree.

Expected a Git repository at:
  $LabRepo

Do not run this script from N-LMS. Check out the private research source first.
"@
}

$RemoteProbe = Invoke-NativeCapture `
    -FilePath "git" `
    -Arguments @(
        "-C", $LabRepo,
        "remote", "get-url", "origin"
    )

if ($RemoteProbe.ExitCode -ne 0) {
    throw "Unable to read the private research source origin remote."
}

$RemoteUrl = (($RemoteProbe.Output | ForEach-Object { $_.ToString() }) -join "").Trim()
if ($PrivateSourceRemotePattern -and $RemoteUrl -notmatch $PrivateSourceRemotePattern) {
    throw "The detected private source repository does not match the caller-supplied remote policy."
}

Invoke-Native `
    -FilePath "git" `
    -Arguments @(
        "-C", $LabRepo,
        "fetch", "origin", "--prune"
    )

$BootstrapCommit = Resolve-GitCommit `
    -GitRepository $LabRepo `
    -Ref $BootstrapRef

$WorkRoot = [System.IO.Path]::GetFullPath($OutputDirectory)
if (Test-Path -LiteralPath $WorkRoot) {
    Remove-Item -LiteralPath $WorkRoot -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $WorkRoot | Out-Null

$Archive = Join-Path $WorkRoot "bootstrap.zip"
$Extracted = Join-Path $WorkRoot "extracted"
$Stage = Join-Path $WorkRoot "repository"
New-Item -ItemType Directory -Force -Path $Extracted, $Stage | Out-Null

Invoke-Native `
    -FilePath "git" `
    -Arguments @(
        "-C", $LabRepo,
        "archive",
        "--format=zip",
        "--output", $Archive,
        $BootstrapCommit,
        "exports/N-Human-AI-Mathematics"
    )

Expand-Archive -LiteralPath $Archive -DestinationPath $Extracted -Force

$ExportRoot = Join-Path $Extracted "exports\N-Human-AI-Mathematics"
if (-not (Test-Path -LiteralPath $ExportRoot)) {
    throw "Bootstrap archive did not contain the expected export root: $ExportRoot"
}
Copy-Item -Path (Join-Path $ExportRoot "*") -Destination $Stage -Recurse -Force

$ManifestPath = Join-Path $Stage "papers\HINC-001\SOURCE_MANIFEST.json"
$Manifest = Get-Content -LiteralPath $ManifestPath -Raw | ConvertFrom-Json

$PublicClone = Join-Path $WorkRoot "novak-sdt"
$PublicCloneReady = $false

foreach ($Source in $Manifest.sources) {
    foreach ($File in $Source.files) {
        $Target = Join-Path $Stage ($File.target -replace '/', '\')

        if ($Source.private_source_identifier_withheld -eq $true) {
            if (-not (Test-Path -LiteralPath $Target -PathType Leaf)) {
                throw "Expected staged private-source export target is missing: $Target"
            }
            continue
        }

        switch ($Source.repository) {
            "novakprotocol/novak-sdt" {
                if (-not $PublicCloneReady) {
                    Invoke-Native `
                        -FilePath "git" `
                        -Arguments @(
                            "clone",
                            "--filter=blob:none",
                            "--no-checkout",
                            "https://github.com/novakprotocol/novak-sdt.git",
                            $PublicClone
                        )

                    Invoke-Native `
                        -FilePath "git" `
                        -Arguments @(
                            "-C", $PublicClone,
                            "checkout", "--detach",
                            $Source.commit
                        )

                    $PublicCloneReady = $true
                }

                $SourceFile = Join-Path $PublicClone ($File.source -replace '/', '\')
                if (-not (Test-Path -LiteralPath $SourceFile -PathType Leaf)) {
                    throw "Public formal source is missing: $SourceFile"
                }

                $TargetParent = Split-Path -Parent $Target
                New-Item -ItemType Directory -Force -Path $TargetParent | Out-Null
                Copy-Item -LiteralPath $SourceFile -Destination $Target -Force
            }

            default {
                throw "Unsupported source repository in SOURCE_MANIFEST.json: $($Source.repository)"
            }
        }
    }
}

$ValidationReceipt = Join-Path $Stage "reports\publication-validation.json"
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $ValidationReceipt) | Out-Null

$PythonArguments = @()
$PythonArguments += $Python.Prefix
$PythonArguments += @(
    (Join-Path $Stage "tools\validate_publication.py"),
    "--root", $Stage,
    "--json-output", $ValidationReceipt
)
Invoke-Native -FilePath $Python.Command -Arguments $PythonArguments

$Receipt = [ordered]@{
    schema_version = "n.human_ai_mathematics.bootstrap_receipt.v1"
    result = "PASS"
    repository = $Repository
    created_utc = [DateTime]::UtcNow.ToString("o")
    bootstrap_ref = $BootstrapRef
    bootstrap_commit = $BootstrapCommit
    manuscript_source_repository = "derived from a private research source"
    manuscript_source_commit = $null
    formal_source_repository = "novakprotocol/novak-sdt"
    formal_source_commit = "d7751d1de76253407016ef4bf92738cffa800e82"
    public_visibility_authorized = $false
    license_applied = $false
    validation_receipt = "reports/publication-validation.json"
    private_source_identifier_withheld = $true
}

Write-Utf8NoBom `
    -Path (Join-Path $Stage "BOOTSTRAP_RECEIPT.json") `
    -Text (($Receipt | ConvertTo-Json -Depth 10) + "`n")

Invoke-Native -FilePath "git" -Arguments @("init") -WorkingDirectory $Stage
Invoke-Native -FilePath "git" -Arguments @("checkout", "-b", "main") -WorkingDirectory $Stage
Invoke-Native -FilePath "git" -Arguments @("add", ".") -WorkingDirectory $Stage
Invoke-Native `
    -FilePath "git" `
    -Arguments @(
        "commit", "-m",
        "Initial curated human-AI mathematics publication repository"
    ) `
    -WorkingDirectory $Stage

if (-not $SkipGitHubCreate) {
    if (Test-GitHubRepositoryExists -RepositoryName $Repository) {
        throw "GitHub repository already exists: $Repository. Refusing to overwrite it."
    }

    if ($PSCmdlet.ShouldProcess($Repository, "Create private GitHub repository and push initial main branch")) {
        Invoke-Native `
            -FilePath "gh" `
            -Arguments @(
                "repo", "create", $Repository,
                "--private",
                "--source", $Stage,
                "--remote", "origin",
                "--push",
                "--description",
                "Human-led, AI-assisted mathematical research: proofs, formal verification, reproducible evidence, corrections, and open specialist review."
            )

        Invoke-Native `
            -FilePath "gh" `
            -Arguments @(
                "repo", "edit", $Repository,
                "--add-topic", "mathematics",
                "--add-topic", "formal-verification",
                "--add-topic", "reproducible-research",
                "--add-topic", "human-ai-collaboration"
            )
    }
}

Write-Host ""
Write-Host "N Human-AI Mathematics bootstrap completed."
Write-Host "Local repository: $Stage"
Write-Host "Bootstrap commit: $BootstrapCommit"
Write-Host "Visibility: private (public release remains unauthorized)"
Write-Host ""
Write-Host "Next gate: inspect the private repository, review HINC-001, then explicitly authorize public visibility."

if (-not $KeepWorkDirectory -and -not $SkipGitHubCreate) {
    Write-Host "The work directory was retained for inspection: $WorkRoot"
}
