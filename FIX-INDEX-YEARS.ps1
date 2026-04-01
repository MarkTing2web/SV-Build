$f = "index.html"
$content = [System.IO.File]::ReadAllText($f)

# 1. Trust Bar
$content = [regex]::Replace($content, '<span>&bull; Police Licensed L/PS/000267/2023P</span>', '<span>&bull; Police Licensed <span class="sv-licence">L/PS/000267/2023P</span></span>')
$content = [regex]::Replace($content, '<span>&bull; <span id="years-val-2">19</span> Years in Operation</span>', '<span>&bull; <span class="sv-years-business">20</span> Years in Operation</span>')

# 2. Assurance Section
$content = [regex]::Replace($content, 'with <strong>37\+ years</strong> of hands-on industry experience', 'with <strong><span class="sv-years-experience">37</span>+ years</strong> of hands-on industry experience')
$content = [regex]::Replace($content, '<strong>Est. 2006</strong><small>19\+ Years</small>', '<strong>Est. <span class="sv-founded-year">2006</span></strong><small><span class="sv-years-business">20</span>+ Years</small>')

[System.IO.File]::WriteAllText($f, $content)
Write-Host "Updated index.html years and license to be dynamic." -ForegroundColor Green
