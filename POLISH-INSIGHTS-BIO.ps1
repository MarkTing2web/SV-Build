$files = Get-ChildItem -Filter *.html
foreach ($f in $files) {
    try {
        $content = [System.IO.File]::ReadAllText($f.FullName)
        $modified = $false
        
        # 1. Years of experience (35 years, 35+ years)
        $newContent = [regex]::Replace($content, "35\syears", '<span class="sv-years-experience">37</span> years')
        if ($newContent -ne $content) { $content = $newContent; $modified = $true }
        
        # 2. Founded Year Variations
        $newContent = [regex]::Replace($content, "in 2006", 'in <span class="sv-founded-year">2006</span>')
        if ($newContent -ne $content) { $content = $newContent; $modified = $true }

        # 3. Sites Count Variations
        $newContent = [regex]::Replace($content, "1,000 sites", '<span class="sv-sites">1,000+ Sites</span>')
        if ($newContent -ne $content) { $content = $newContent; $modified = $true }
        
        $newContent = [regex]::Replace($content, "more than 1,000 sites", '<span class="sv-sites">1,000+ Sites</span>')
        if ($newContent -ne $content) { $content = $newContent; $modified = $true }

        if ($modified) {
            [System.IO.File]::WriteAllText($f.FullName, $content)
            Write-Host "Polished bio in $($f.Name)" -ForegroundColor Cyan
        }
    } catch {
        Write-Host "Failed $($f.Name): $($_.Exception.Message)"
    }
}
