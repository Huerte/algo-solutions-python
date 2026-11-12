# Generate index.json for GitHub Pages site
# This script scans the solutions directory and creates a JSON index

$solutions = @()
$languages = @('python', 'javascript', 'cpp', 'java')
$solutionsDir = Join-Path (Split-Path $PSScriptRoot) "solutions"

Write-Host "Scanning solutions directory: $solutionsDir" -ForegroundColor Green

foreach ($lang in $languages) {
    $dir = Join-Path $solutionsDir $lang
    if (Test-Path $dir) {
        Write-Host "Processing $lang..." -ForegroundColor Cyan
        Get-ChildItem $dir -File | Where-Object { $_.Name -match "^practice\d+\." } | ForEach-Object {
            try {
                $content = Get-Content $_.FullName -Raw -ErrorAction SilentlyContinue
                $lines = $content -split "`n" | Select-Object -First 10

                $problemLine = $lines | Where-Object { $_ -match "^#\s+Problem:" -or $_ -match "^//\s+Problem:" }
                $sourceLine = $lines | Where-Object { $_ -match "^#\s+Source:" -or $_ -match "^//\s+Source:" }

                $problem = if ($problemLine) {
                    $problemLine -replace "^(#|//)\s+Problem:\s*", ""
                } else {
                    $_.BaseName
                }

                $source = if ($sourceLine) {
                    $sourceLine -replace "^(#|//)\s+Source:\s*", ""
                } else {
                    ""
                }

                $solutions += @{
                    name = $_.BaseName
                    language = $lang
                    filename = $_.Name
                    problem = $problem.Trim()
                    source = $source.Trim()
                    path = "solutions/$lang/$($_.Name)"
                }
            } catch {
                Write-Host "  Error processing $($_.Name): $_" -ForegroundColor Yellow
            }
        }
    }
}

# Generate JSON
$outputPath = Join-Path (Split-Path $PSScriptRoot) "docs\data.json"
$json = $solutions | ConvertTo-Json
if ($solutions.Count -eq 1) {
    $json = "[$json]"
}

$json | Set-Content -Path $outputPath -Encoding UTF8

Write-Host ""
Write-Host "✓ Index generated successfully!" -ForegroundColor Green
Write-Host "  Total solutions: $($solutions.Count)" -ForegroundColor Green
Write-Host "  Output file: $outputPath" -ForegroundColor Green

# Group by language for info
$byLanguage = $solutions | Group-Object language
Write-Host ""
Write-Host "Solutions by language:" -ForegroundColor Green
foreach ($group in $byLanguage) {
    Write-Host "  $($group.Name): $($group.Count)" -ForegroundColor Cyan
}
