$htmlFiles = Get-ChildItem -Filter *.html *.css
$missingImages = @()

foreach ($f in $htmlFiles) {
    try {
        $content = [System.IO.File]::ReadAllText($f.FullName)
        # Match src="images/filename.ext" or url('images/filename.ext')
        $matches = [regex]::Matches($content, '(?i)(?:src=|url\()["'']?(images/[^"''\s\)]+)["''\s\)]?')
        foreach ($m in $matches) {
            $rawPath = $m.Groups[1].Value
            $imgPath = $rawPath.Replace('/', '\')
            # Resolve relative to root
            $fullPath = Join-Path (Get-Location) $imgPath
            if (-not (Test-Path $fullPath)) {
                $missingImages += [PSCustomObject]@{
                    SourceFile = $f.Name
                    MissingPath = $rawPath
                }
            }
        }
    } catch {
        Write-Host "Failed to process $($f.Name)" -ForegroundColor Red
    }
}

$uniqueMissing = $missingImages | Sort-Object MissingPath -Unique
if ($uniqueMissing.Count -eq 0) {
    Write-Host "No missing images found! 100% complete." -ForegroundColor Green
} else {
    Write-Host "Found $($uniqueMissing.Count) missing images:" -ForegroundColor Red
    $uniqueMissing | Format-Table -AutoSize
}
