$ErrorActionPreference = "Stop"

$repoRoot = Split-Path $PSScriptRoot -Parent
$generator = Join-Path $repoRoot ".github/scripts/generate-index.py"

if (-not (Test-Path $generator)) {
    throw "Index generator not found: $generator"
}

$candidates = @("py", "python", "python3")
$localPythons = Get-ChildItem -Path "$env:LOCALAPPDATA\Programs\Python\Python*\python.exe" -ErrorAction SilentlyContinue | ForEach-Object { $_.FullName }
if ($localPythons) {
    $candidates += $localPythons
}

$workingPython = $null
foreach ($cmd in $candidates) {
    try {
        $testOut = & $cmd --version 2>&1
        if ($LASTEXITCODE -eq 0 -and $testOut -match "Python 3\.") {
            $workingPython = $cmd
            break
        }
    } catch {
        continue
    }
}

if (-not $workingPython) {
    throw "Python 3 is required. Install Python 3 and ensure py, python, or python3 is on PATH."
}

& $workingPython $generator
if ($LASTEXITCODE -ne 0) {
    throw "The solutions index generator failed with exit code $LASTEXITCODE."
}
