$files = Get-ChildItem -Filter *.html -Exclude "index.html"
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
    $content = Get-Content $f.FullName -Raw
    
    # 1. Inject site-config.js in head
    if ($content -notmatch 'script src="site-config.js"') {
        $content = $content -replace '(<link rel="stylesheet" href="sv-shared.css">)', "`$1`r`n    <script src=`"site-config.js`"></script>"
    }

    # 2. Global Replacements
    $content = $content -replace "35\+", '<span class="sv-years-experience">37</span>+'
    $content = $content -replace "L/PS/000267/2023P", '<span class="sv-licence">L/PS/000267/2023P</span>'
    $content = $content -replace "since 2006", 'since <span class="sv-founded-year">2006</span>'
    $content = $content -replace "Since 2006", 'Since <span class="sv-founded-year">2006</span>'
    $content = $content -replace "19\+ Years of Experience", '<span class="sv-years-business">20</span>+ Years of Experience'
    $content = $content -replace "Thousands of additional projects", '<span class="sv-sites">1,000+ Sites</span>'
    $content = $content -replace "Join thousands of Singaporean homes", "Join <span class='sv-sites'>1,000+ Sites</span>"
    $content = $content -replace "&copy; 2026", '&copy; <span class="sv-current-year">2026</span>'

    # 3. Inject Hydration Script before </body>
    if ($content -notmatch 'sv-years-experience') {
         # This check is slightly loose, but should work if we've already done replacements above
         # Better check:
    }
    
    if ($content -notmatch 'SECUREVISION') {
        $content = $content -replace '(</body>)', "$hydrationScript`r`n`$1"
    }

    Set-Content $f.FullName $content -NoNewline
    Write-Host "Processed $($f.Name)" -ForegroundColor Green
}
