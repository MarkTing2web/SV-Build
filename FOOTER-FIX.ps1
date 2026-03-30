# Finishing Touch: Footer Path & Year Fix
$files = Get-ChildItem *.html -Exclude "index_full.html"

foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw
    $original = $content

    # 1. Fix footer logo path (proprietary-assets -> images)
    $content = $content.Replace("proprietary-assets/securevision-dark-logo.png", "images/securevision-logo-white.png")
    $content = $content.Replace("proprietary-assets/securevision-logo-light.svg", "images/securevision-logo-white.png")
    
    # 2. Fix copyright year (2025 -> 2026)
    $content = $content.Replace("&copy; 2025", "&copy; 2026")
    $content = $content.Replace("© 2025", "© 2026")

    if ($content -ne $original) {
        Set-Content $f.FullName $content -NoNewline
        Write-Host "Updated Footer in $($f.Name)" -ForegroundColor Cyan
    }
}
