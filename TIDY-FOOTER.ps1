# Site-Wide Footer "Systems" Cleanup Script
# This script standardizes the Systems column in the footer to exactly 4 items.

$newSystemsFooter = @"
            <div class="footer-links">
                <h4>Systems</h4>
                <ul>
                    <li><a href="surveillance-detection.html">Surveillance &amp; Detection</a></li>
                    <li><a href="people-access-control.html">People Access Control</a></li>
                    <li><a href="vehicle-access-control.html">Vehicle Access &amp; Barriers</a></li>
                    <li><a href="integrated-security-platform.html">Platform Management</a></li>
                </ul>
            </div>
"@

$files = Get-ChildItem *.html -Exclude "index_full.html", "index-copy.html", "door-access-backup.html"

foreach ($f in $files) {
    $filePath = $f.FullName
    $content = Get-Content $filePath -Raw

    # Targeted replacement of the Systems footer column
    $pattern = '(?s)<div class="footer-links">\s*<h4>Systems</h4>.*?</ul>\s*</div>'
    
    if ($content -match $pattern) {
        $content = [regex]::Replace($content, $pattern, $newSystemsFooter)
        Set-Content $filePath $content -NoNewline
        Write-Host "Updated Footer in $($f.Name)" -ForegroundColor Cyan
    }
}

Write-Host "Footer Systems Cleanup Complete." -ForegroundColor Green
