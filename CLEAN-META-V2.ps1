$files = Get-ChildItem -Filter *.html
foreach ($f in $files) {
    try {
        $content = [System.IO.File]::ReadAllText($f.FullName)
        if ($content -match '<meta name="description"') {
             # Remove spans with their attributes and end tags
             # specifically looking for the sv-years-experience span inside quotes
             $content = $content.Replace('<span class="sv-years-experience">37</span>', '37')
             $content = $content.Replace('<span class="sv-years-experience">35</span>', '37') # catch any 35s
             [System.IO.File]::WriteAllText($f.FullName, $content)
             Write-Host "Re-cleaned meta in $($f.Name)" -ForegroundColor Yellow
        }
    } catch {
         Write-Host "Failed $($f.Name)"
    }
}
