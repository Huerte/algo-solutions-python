$ErrorActionPreference = "Stop"

$repoRoot = $PSScriptRoot
$generator = Join-Path $repoRoot ".github/scripts/generate-index.py"

if (-not (Test-Path $generator)) {
    throw "Index generator not found: $generator"
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command python3 -ErrorAction SilentlyContinue
}
if (-not $python) {
    throw "Python 3 is required. Install Python 3 and ensure python or python3 is on PATH."
}

& $python.Source $generator
if ($LASTEXITCODE -ne 0) {
    throw "The solutions index generator failed with exit code $LASTEXITCODE."
}
