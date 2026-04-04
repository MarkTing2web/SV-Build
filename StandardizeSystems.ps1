$pages = @(
    # Pillar/System Landing Pages
    @{ Path = "surveillance-detection.html"; Class = "surveillance"; Intent = "surveillance-assessment" },
    @{ Path = "people-access-control.html"; Class = "access"; Intent = "access-assessment" },
    @{ Path = "vehicle-access-control.html"; Class = "vehicle"; Intent = "vehicle-assessment" },
    @{ Path = "integrated-security-platform.html"; Class = "platform"; Intent = "platform-assessment" },
    
    # Solution Pillars
    @{ Path = "residential-security-singapore.html"; Class = "res"; Intent = "residential-assessment" },
    @{ Path = "commercial-security-singapore.html"; Class = "com"; Intent = "commercial-assessment" },
    @{ Path = "condominiums.html"; Class = "condo"; Intent = "condo-assessment" },
    @{ Path = "industrial-security-singapore.html"; Class = "indus"; Intent = "industrial-assessment" },
    @{ Path = "government-institution-security-singapore.html"; Class = "gov"; Intent = "gov-assessment" },
    @{ Path = "healthcare-security-singapore.html"; Class = "healthcare"; Intent = "healthcare-assessment" },

    # Specific Product Guides
    @{ Path = "cctv.html"; Class = "cctv"; Intent = "cctv-assessment" },
    @{ Path = "burglar-alarm.html"; Class = "alarm"; Intent = "alarm-assessment" },
    @{ Path = "thermal-imaging.html"; Class = "thermal"; Intent = "thermal-assessment" },
    @{ Path = "perimeter-security.html"; Class = "perimeter"; Intent = "perimeter-assessment" },
    @{ Path = "ai-analytics.html"; Class = "ai"; Intent = "ai-assessment" }
)

foreach ($page in $pages) {
    if (Test-Path $page.Path) {
        $content = Get-Content $page.Path -Raw
        $class = $page.Class
        $intent = $page.Intent

        # 1. STANDARDIZE HERO SECTION
        # Support <section> or <header> with any class that has 'hero'
        $heroRegex = '(?s)<(section|header)\b[^>]*class=[''"][^''"]*hero[^''"]*[''"][^>]*>.*?</\1>'
        $content = [regex]::Replace($content, $heroRegex, {
            param($m)
            $inner = $m.Value
            
            # Extract content carefully
            $eyebrow = if ($inner -match '<span class=[''"]eyebrow[^''"]*[''"][^>]*>(.*?)</span>') { $matches[1] } else { "" }
            $h1 = if ($inner -match '<h1[^>]*>(.*?)</h1>') { $matches[1] } else { "" }
            $p = if ($inner -match '<p\s+class=[''"]subtitle[''"][^>]*>(.*?)</p>') { $matches[1] } elseif ($inner -match '<p[^>]*subtitle[^>]*>(.*?)</p>') { $matches[1] } elseif ($inner -match '<p\s+class=[''"]hero-subtitle-main[''"][^>]*>(.*?)</p>') { $matches[1] } else { "" }
            
            if ($h1 -eq "") { return $m.Value } # Safety check

            # Build new Hero
            $newHero = "<header class=""hero-high-impact hero-$class"">`n"
            $newHero += "    <div class=""container"">`n"
            if ($eyebrow -ne "") { $newHero += "        <span class=""eyebrow-light"">$eyebrow</span>`n" }
            $newHero += "        <h1 class=""hero-title-main"">$h1</h1>`n"
            $newHero += "        <p class=""hero-subtitle-main"">$p</p>`n"
            $newHero += "        <div class=""btn-group equal-width"">`n"
            $newHero += "            <a href=""request-site-assessment-singapore.html?intent=$intent"" class=""btn btn-primary"">Book Site Assessment</a>`n"
            $newHero += "            <a href=""https://wa.me/6593860466"" class=""btn btn-whatsapp-standard"">WhatsApp an Engineer</a>`n"
            $newHero += "        </div>`n"
            $newHero += "    </div>`n"
            $newHero += "</header>"
            return $newHero
        })

        # 2. STANDARDIZE FINAL CTA SECTION
        # More aggressive regex for CTA (matches common IDs and classes)
        $ctaRegex = '(?s)<section\b[^>]*(id=[''"](cta|final-cta)[''"]|class=[''"](cta-section|final-cta|cta-high-impact|cta)[^''"]*[''"])[^>]*>.*?</section>'
        $content = [regex]::Replace($content, $ctaRegex, 
        {
            param($m)
            $inner = $m.Value
            $h2 = if ($inner -match '<h2[^>]*>(.*?)</h2>') { $matches[1] } else { "Ready to Secure Your Property?" }
            $p = if ($inner -match '<p[^>]*>(.*?)</p>') { $matches[1] } else { "Request a comprehensive site assessment today." }
            
            return "<section class=""cta-high-impact cta-$class"">`n    <div class=""container"">`n        <div style=""max-width: 850px; margin: 0 auto; text-align: center;"">`n            <h2>$h2</h2>`n            <p style=""font-size: 18px; opacity: 0.9; line-height: 1.8; margin-bottom: 48px;"">$p</p>`n            <div class=""btn-group equal-width"">`n                <a href=""https://wa.me/6593860466"" class=""btn btn-whatsapp-standard"">WhatsApp an Engineer</a>`n                <a href=""request-site-assessment-singapore.html?intent=$intent"" class=""btn btn-primary"">Book Site Assessment</a>`n            </div>`n        </div>`n    </div>`n</section>"
        })

        Set-Content $page.Path $content -NoNewline
        Write-Host "Processed $($page.Path)"
    }
}
