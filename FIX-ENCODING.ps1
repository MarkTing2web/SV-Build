$files = @("cctv.html", "burglar-alarm.html", "door-access.html", "intercom-system-singapore.html", "auto-gate-singapore.html")

foreach ($f in $files) {
    if (Test-Path $f) {
        $content = [System.IO.File]::ReadAllText((Get-Item $f).FullName)
        if ($content -match 'Â·') {
            $content = $content.Replace('Â·', '&middot;')
            [System.IO.File]::WriteAllText((Get-Item $f).FullName, $content)
            Write-Host "Fixed encoding in $f" -ForegroundColor Yellow
        }
    }
}
