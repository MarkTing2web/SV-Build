# Site-Wide Legacy Navigation Gap Repair (Ver 9 - The Big Gap Fix)
# This script purges duplicated/orphaned mobile menu items that appeared between </nav> and the hero section.

$files = Get-ChildItem *.html -Exclude "index_full.html", "index-copy.html", "door-access-backup.html"

foreach ($f in $files) {
    $filePath = $f.FullName
    $content = Get-Content $filePath -Raw

    # Targeted removal of legacy block precisely between </nav> and the first <header>/<section class="hero">
    # Includes potential comments, extra </div> tags, and orphaned mobile-menu-item divs.
    
    # Matching pattern:
    # 1. Ends after </nav>
    # 2. Includes any spaces/newlines
    # 3. Matches various flavors of legacy comments
    # 4. Matches any number of orphaned divs with class "mobile-menu-item"
    # 5. Stops exactly before the first <header> or <section class="hero"> or <!-- HERO -->
    
    $legacyBlockPattern = '(?s)</nav>\s*(<!--.*?-->\s*|</div>\s*|<div class="mobile-menu-item".*?</div>\s*|<a href=.*?</a>\s*)*(?=\s*(?i)<(header|section|div)\s+(class|id)?=[^>]*?hero)'
    
    if ($content -match $legacyBlockPattern) {
        $content = [regex]::Replace($content, $legacyBlockPattern, "</nav>")
        Write-Host "Fixed Gap in $($f.Name)" -ForegroundColor Cyan
    }

    # Also fix secondary case where there's no clear hero but there are orphaned menu items
    # and they are OUTSIDE the div id="mobileMenu".
    # (Regex for finding divs with class "mobile-menu-item" not inside "mobile-menu" block)
    # Actually, the targeted block fix above handles the primary gap issue.

    Set-Content $filePath $content -NoNewline
}

Write-Host "Gap Repair Complete." -ForegroundColor Green
