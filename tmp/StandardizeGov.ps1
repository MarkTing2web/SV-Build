$file = "c:\Users\ler\OneDrive - Securevision Pte Ltd\1 SV Build\government-institution-security-singapore.html"
$content = Get-Content $file -Raw

# 1. Hero Standardisation
# Replace hero section opening tag
$content = $content -replace '<section class="hero-institutions hero" style="[^"]+">', "<section class='hero-institutions hero hero-gov'>"
# Clean up h1 and p subtitle styles in hero
$content = $content -replace '<h1 style="color:#fff;">', "<h1>"
$content = $content -replace '<p class="subtitle" style="color:rgba\(255,255,255,0\.95\);">', '<p class="subtitle">'

# 2. Hero Buttons
$content = $content -replace 'Request an Institutional Audit &rarr;', 'Book Site Assessment'

# 3. Final CTA Block
$content = $content -replace '<section id="final-cta" class="cta-section" style="[^"]+">', '<section id="final-cta" class="cta-high-impact cta-gov">'
$content = $content -replace '<div class="text-center" style="max-width:850px; margin: 0 auto 64px;">', '<div class="text-center mb-64">'
# Standardize h2 and p in final cta
$content = $content -replace '<h2 style="color: #ffffff;">', '<h2>'
$content = $content -replace '<p class="subtitle" style="color: rgba\(255,255,255,0\.9\) !important; max-width: 800px; margin: 0 auto;">', '<p class="subtitle">'

# 4. CTA Cards Icons and Buttons
$content = $content -replace '<div style="font-size:32px; margin-bottom:20px;">', '<div class="cta-icon-lg">'
$content = $content -replace 'WhatsApp Us &rarr;', 'WhatsApp an Engineer'
$content = $content -replace 'Book Audit &rarr;', 'Book Site Assessment'
$content = $content -replace 'Call Now &rarr;', 'Call Office Now'
$content = $content -replace 'class="btn btn-outline-light" style="border-color:#fff;"', 'class="btn btn-outline-light"'

# Wrap buttons in mt-48
$content = $content -replace '<a href="https://wa\.me/6593860466" class="btn btn-whatsapp" target="_blank">WhatsApp an Engineer</a>', '<div class="mt-48"><a href="https://wa.me/6593860466" class="btn btn-whatsapp" target="_blank">WhatsApp an Engineer</a></div>'
$content = $content -replace '<a href="request-site-assessment-singapore\.html" class="btn btn-primary">Book Site Assessment</a>', '<div class="mt-48"><a href="request-site-assessment-singapore.html?intent=institutional-assessment" class="btn btn-primary">Book Site Assessment</a></div>'
$content = $content -replace '<a href="tel:\+6562864796" class="btn btn-outline-light">Call Office Now</a>', '<div class="mt-48"><a href="tel:+6562864796" class="btn btn-outline-light">Call Office Now</a></div>'

Set-Content $file $content -NoNewline
