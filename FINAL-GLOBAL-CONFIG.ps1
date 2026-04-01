$files = Get-ChildItem -Filter *.html | Where-Object { $_.Name -notin @("index.html", "cctv.html") }
$hydrationScript = @"
<script>
document.addEventListener('DOMContentLoaded', () => {
    if (typeof SECUREVISION !== 'undefined') {
        const SV = SECUREVISION;
        document.querySelectorAll('.sv-licence').forEach(el => el.textContent = SV.licenceNumber);
        document.querySelectorAll('.sv-years-business').forEach(el => el.textContent = SV.yearsInBusiness);
        document.querySelectorAll('.sv-years-experience').forEach(el => el.textContent = SV.yearsExperience);
        document.querySelectorAll('.sv-sites').forEach(el => el.textContent = SV.siteDisplay);
        document.querySelectorAll('.sv-founded-year').forEach(el => el.textContent = SV.foundedYear);
        document.querySelectorAll('.sv-current-year').forEach(el => el.textContent = new Date().getFullYear());
        document.querySelectorAll('a[href^="tel:"]').forEach(link => link.href = "tel:" + SV.phone.replace(/[^0-9]/g, ""));
        document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
            link.href = "mailto:" + SV.email;
            if (link.textContent.includes('@')) link.textContent = SV.email;
        });
        document.querySelectorAll('a[href^="https://wa.me/"]').forEach(link => link.href = "https://wa.me/" + SV.whatsapp);
    }
});
</script>
"@

foreach ($f in $files) {
    try {
        $content = [System.IO.File]::ReadAllText($f.FullName)
        $modified = $false
        
        # 1. Update <head>
        if ($content -notmatch 'site-config\.js') {
            $newContent = [regex]::Replace($content, "(?i)(<link[^>]*sv-shared\.css[^>]*>)", "`$1`r`n    <script src=`"site-config.js`"></script>")
            if ($newContent -ne $content) {
                $content = $newContent
                $modified = $true
            }
        }

        # 2. General Data Replacements
        $replacements = @(
            @("35\+", '<span class="sv-years-experience">37</span>+'),
            @("L/PS/000267/2023P", '<span class="sv-licence">L/PS/000267/2023P</span>'),
            @("since 2006", 'since <span class="sv-founded-year">2006</span>'),
            @("Since 2006", 'Since <span class="sv-founded-year">2006</span>'),
            @("19\+ Years of Experience", '<span class="sv-years-business">20</span>+ Years of Experience'),
            @("thousands of additional projects", '<span class="sv-sites">1,000+ Sites</span>'),
            @("Thousands of additional projects", '<span class="sv-sites">1,000+ Sites</span>')
        )

        foreach ($r in $replacements) {
            $newContent = [regex]::Replace($content, $r[0], $r[1])
            if ($newContent -ne $content) {
                $content = $newContent
                $modified = $true
            }
        }

        # 3. Add Hydration Script before </body>
        if ($content -notmatch 'SECUREVISION') {
            $newContent = [regex]::Replace($content, "(?i)</body>", "$hydrationScript`r`n</body>")
            if ($newContent -ne $content) {
                $content = $newContent
                $modified = $true
            }
        }

        if ($modified) {
            [System.IO.File]::WriteAllText($f.FullName, $content)
            Write-Host "Updated $($f.Name)" -ForegroundColor Green
        }
    } catch {
        Write-Host "Failed $($f.Name): $($_.Exception.Message)" -ForegroundColor Red
    }
}
