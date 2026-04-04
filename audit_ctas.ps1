$htmlFiles = Get-ChildItem -Path . -Filter *.html -Recurse
$report = @()

foreach ($file in $htmlFiles) {
    if ($file.Name -match "sitemap|check_img|booking-success|contact-success") { continue }
    
    $content = Get-Content $file.FullName -Raw
    
    # regex 1: find <a ... class="...btn..." ... href="..." ...>Text</a>
    # regex 2: find <a ... href="..." ... class="...btn..." ...>Text</a>
    
    $match1 = [regex]::Matches($content, '<a\s+[^>]*class=["'']([^"'']*(?:btn|cta|link-arrow|rel-card-footer|btn-primary|btn-outline-light)[^"'']*)["''][^>]*href=["'']([^"'']*)["''][^>]*>(.*?)</a>', ([System.Text.RegularExpressions.RegexOptions]::Singleline -bor [System.Text.RegularExpressions.RegexOptions]::IgnoreCase))
    $match2 = [regex]::Matches($content, '<a\s+[^>]*href=["'']([^"'']*)["''][^>]*class=["'']([^"'']*(?:btn|cta|link-arrow|rel-card-footer|btn-primary|btn-outline-light)[^"'']*)["''][^>]*>(.*?)</a>', ([System.Text.RegularExpressions.RegexOptions]::Singleline -bor [System.Text.RegularExpressions.RegexOptions]::IgnoreCase))

    $allMatches = $match1 + $match2
    
    foreach ($m in $allMatches) {
        $classes = ""
        $href = ""
        $text = ""

        if ($m.Groups.Count -eq 4) {
            # Based on which regex it is
            if ($m.Value -match 'class=.*href=') {
                $classes = $m.Groups[1].Value
                $href = $m.Groups[2].Value
                $text = $m.Groups[3].Value
            } else {
                $href = $m.Groups[1].Value
                $classes = $m.Groups[2].Value
                $text = $m.Groups[3].Value
            }
        }
        
        $text = $text -replace '<[^>]+>', ''
        $text = $text.Trim()
        
        $startPos = $m.Index
        $contextStart = [Math]::Max(0, $startPos - 200)
        $len = [Math]::Min($content.Length - $contextStart, 400)
        $contextChunk = $content.Substring($contextStart, $len)
        
        $report += [PSCustomObject]@{
            Page = $file.Name
            CTA = $text
            Link = $href
            Classes = $classes.Trim()
            RawText = $m.Value.Substring(0, [Math]::Min($m.Value.Length, 150))
        }
    }
}

if ($report.Count -eq 0) {
    Write-Host "No matches found."
} else {
    $report | Export-Csv -Path "cta_audit.csv" -NoTypeInformation
    Write-Host "Audit completed. Found $($report.Count) CTAs."
}
