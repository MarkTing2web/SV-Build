$targetFiles = Get-ChildItem -Filter *.html -Exclude "index.html", "cctv.html" | Select-Object -First 3
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

foreach ($f in $targetFiles) {
    try {
        $content = [System.IO.File]::ReadAllText($f.FullName)
        
        # 1. Head
        if ($content -notmatch 'site-config\.js') {
            $content = $content.Replace('<link rel="stylesheet" href="sv-shared.css">', "<link rel=`"stylesheet`" href=`"sv-shared.css`">`r`n    <script src=`"site-config.js`"></script>")
        }

        # 2. General
        $content = [regex]::Replace($content, "35\+", '<span class="sv-years-experience">37</span>+')
        $content = $content.Replace("L/PS/000267/2023P", '<span class="sv-licence">L/PS/000267/2023P</span>')
        $content = $content.Replace("since 2006", 'since <span class="sv-founded-year">2006</span>')
        $content = $content.Replace("Since 2006", 'Since <span class="sv-founded-year">2006</span>')
        $content = $content.Replace("19+ Years of Experience", '<span class="sv-years-business">20</span>+ Years of Experience')

        # 3. Body
        if ($content -notmatch 'SECUREVISION') {
            $content = $content.Replace('</body>', "$hydrationScript`r`n</body>")
        }

        [System.IO.File]::WriteAllText($f.FullName, $content)
        Write-Host "Manually updated $($f.Name)" -ForegroundColor Cyan
    } catch {
        Write-Host "Failed $($f.Name): $($_.Exception.Message)" -ForegroundColor Red
    }
}
