# Site-Wide Navigation Standardization Script (Ver 11)
# Corrects "Video Training" to "Training Videos" site-wide.

$files = Get-ChildItem *.html -Exclude "index_full.html", "index-copy.html", "door-access-backup.html"

foreach ($f in $files) {
    $filePath = $f.FullName
    $content = Get-Content $filePath -Raw

    # Targeted replacement for Resources sub-menu (desktop and mobile)
    $pattern = '<a href="resources.html#videos">Video Training</a>'
    $replacement = '<a href="resources.html#videos">Training Videos</a>'
    
    if ($content -like "*$pattern*") {
        $content = $content.Replace($pattern, $replacement)
        Set-Content $filePath $content -NoNewline
        Write-Host "Updated Resources menu in $($f.Name)" -ForegroundColor Cyan
    }
}

Write-Host "Site-Wide Navigation Update Complete." -ForegroundColor Green
