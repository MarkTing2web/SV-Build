# Site-Wide File Renaming & Link Updating Script
# This script renames 4 core system pages and updates all internal references to them.

$mappings = @{
    "cctv-surveillance-singapore.html" = "surveillance-detection.html"
    "access-control-singapore.html" = "people-access-control.html"
    "vehicle-access-control-singapore.html" = "vehicle-access-control.html"
    "integrated-security-system-singapore.html" = "integrated-security-platform.html"
}

# 1. RENAME PHYSICAL FILES
foreach ($old in $mappings.Keys) {
    $new = $mappings[$old]
    if (Test-Path $old) {
        Rename-Item -Path $old -NewName $new -Force
        Write-Host "Renamed: $old -> $new" -ForegroundColor Green
    } else {
        Write-Host "Warning: $old not found." -ForegroundColor Yellow
    }
}

# 2. UPDATE ALL REFERENCES SITE-WIDE (ALL HTML & PS1)
$targets = Get-ChildItem -Include *.html, *.md, *.ps1 -Recurse

foreach ($f in $targets) {
    if ($f.Name -eq "RENAME-FILES.ps1") { continue } # Skip self
    
    $content = Get-Content $f.FullName -Raw
    $original = $content

    foreach ($old in $mappings.Keys) {
        $new = $mappings[$old]
        # Replace occurrences of the old filename
        $content = $content.Replace($old, $new)
    }

    if ($content -ne $original) {
        Set-Content $f.FullName $content -NoNewline
        Write-Host "Updated links in: $($f.Name)" -ForegroundColor Cyan
    }
}

Write-Host "File Renaming and Link Update Complete." -ForegroundColor Green
