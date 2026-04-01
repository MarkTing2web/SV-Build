$files = Get-ChildItem -Filter *.html
foreach ($f in $files) {
    try {
        $content = [System.IO.File]::ReadAllText($f.FullName)
        if ($content -match '<meta name="description" content=".*?<span') {
             # Remove spans from meta description content
             $content = [regex]::Replace($content, '(<meta name="description" content=")(.*?)(")', {
                 param($m)
                 $prefix = $m.Groups[1].Value
                 $text = $m.Groups[2].Value
                 $suffix = $m.Groups[3].Value
                 # Strip any HTML tags from inside the content
                 $cleanText = [regex]::Replace($text, '<[^>]*>', '')
                 return "$prefix$cleanText$suffix"
             })
             [System.IO.File]::WriteAllText($f.FullName, $content)
             Write-Host "Fixed meta in $($f.Name)" -ForegroundColor Green
        }
    } catch {
         Write-Host "Failed $($f.Name): $($_.Exception.Message)"
    }
}
