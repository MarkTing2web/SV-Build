$files = @("cctv.html", "burglar-alarm.html", "door-access.html", "intercom-system-singapore.html", "auto-gate-singapore.html")

foreach ($f in $files) {
    if (Test-Path $f) {
        $content = [System.IO.File]::ReadAllText((Get-Item $f).FullName)
        if ($content -match 'author-bio-name') {
            $content = $content.Replace('class="author-bio-name"', 'class="author-bio-name sv-author-name"')
            [System.IO.File]::WriteAllText((Get-Item $f).FullName, $content)
            Write-Host "Updated bio name in $f"
        }
    }
}
