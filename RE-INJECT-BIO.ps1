$files = @("cctv.html", "burglar-alarm.html", "door-access.html", "intercom-system-singapore.html", "auto-gate-singapore.html")

$bioBlockHtml = @"
    <div class="container">
      <div class="author-bio-strip">
        <img src="images/ler-wee-meng-bio.jpeg" alt="Wee Meng Ler" class="author-bio-photo">
        <div class="author-bio-text">
          <span class="author-bio-name">Wee Meng Ler</span>
          <span class="author-bio-credentials">Founder & CEO · Securevision · <span class="sv-years-experience">37</span>+ Years Experience</span>
        </div>
      </div>
    </div>
"@

foreach ($f in $files) {
    if (Test-Path $f) {
        $content = [System.IO.File]::ReadAllText((Get-Item $f).FullName)
        
        # 1. Ensure we don't have duplicates
        if ($content -notmatch 'author-bio-strip') {
             # Position after header and before breadcrumbs
             if ($content -match "</header>") {
                 $content = [regex]::Replace($content, "(?i)</header>", "</header>`r`n$bioBlockHtml")
                 [System.IO.File]::WriteAllText((Get-Item $f).FullName, $content)
                 Write-Host "Injected bio to $f" -ForegroundColor Green
             }
        }
    }
}
