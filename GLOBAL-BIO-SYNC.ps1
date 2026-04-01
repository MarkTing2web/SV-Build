$files = Get-ChildItem -Filter *.html
$hydrationScript = @"
<script>
document.addEventListener('DOMContentLoaded', () => {
    if (typeof SECUREVISION !== 'undefined') {
        const SV = SECUREVISION;
        // Basic Facts
        document.querySelectorAll('.sv-licence').forEach(el => el.textContent = SV.licenceNumber);
        document.querySelectorAll('.sv-years-business').forEach(el => el.textContent = SV.yearsInBusiness);
        document.querySelectorAll('.sv-years-experience').forEach(el => el.textContent = SV.yearsExperience);
        document.querySelectorAll('.sv-sites').forEach(el => el.textContent = SV.siteDisplay);
        document.querySelectorAll('.sv-founded-year').forEach(el => el.textContent = SV.foundedYear);
        document.querySelectorAll('.sv-current-year').forEach(el => el.textContent = new Date().getFullYear());
        
        // Author Bio (New)
        document.querySelectorAll('.sv-author-name').forEach(el => el.textContent = SV.authorName);
        document.querySelectorAll('.sv-author-title').forEach(el => el.textContent = SV.authorTitle);
        document.querySelectorAll('.sv-author-description').forEach(el => el.textContent = SV.authorDescription);
        document.querySelectorAll('.sv-author-story').forEach(el => el.textContent = SV.authorStory);
        document.querySelectorAll('.sv-author-expertise').forEach(el => el.textContent = SV.authorExpertise);
        document.querySelectorAll('.sv-author-client-focus').forEach(el => el.textContent = SV.authorClientFocus);

        // Contact Links
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
    $content = [System.IO.File]::ReadAllText($f.FullName)
    
    # 1. Update the hydration script block
    if ($content -match '<script>\s*document\.addEventListener\(''DOMContentLoaded'',\s*\(\)\s*=>\s*{\s*if\s*\(typeof\s*SECUREVISION') {
        $content = [regex]::Replace($content, "(?s)<script>.*?SECUREVISION.*?</script>", $hydrationScript)
    }

    # 2. Inject classes into the author bio section (Insight-style)
    # Target: <h4 ...>Ler Wee Meng</h4>
    $content = [regex]::Replace($content, "(?i)<h4[^>]*>Ler Wee Meng</h4>", '<h4 class="sv-author-name">Ler Wee Meng</h4>')
    # Target: <p ...>Founder & CEO, Securevision Pte Ltd</p>
    $content = [regex]::Replace($content, "(?i)Founder & CEO, Securevision Pte Ltd", '<span class="sv-author-title">Founder & CEO, Securevision Pte Ltd</span>')
    
    # Target paragraphs specifically in the bio content div
    # Paragraph 1
    $content = [regex]::Replace($content, "(?i)<p[^>]*>Wee Meng has over.*?National University of Singapore.*?</p>", '<p class="sv-author-description">Wee Meng has over 37 years of experience in security systems engineering and integration. He holds a BEng in Electrical and Electronic Engineering from the National University of Singapore and a law degree from the University of London.</p>')
    # Paragraph 2
    $content = [regex]::Replace($content, "(?i)<p[^>]*>He founded Securevision in.*?spanning residential properties.*?</p>", '<p class="sv-author-story">He founded Securevision in 2006 and has since led security system deployments across more than 1,000+ Sites in Singapore — spanning residential properties, condominiums, commercial buildings, industrial facilities, and institutions.</p>')
    # Paragraph 3
    $content = [regex]::Replace($content, "(?i)<p[^>]*>His technical focus spans CCTV and AI video analytics.*?</p>", '<p class="sv-author-expertise">His technical focus spans CCTV and AI video analytics, IP intercom systems, access control, licence plate recognition, and integrated platform design. He is the architect behind VESTA, Securevision''s unified security platform built specifically for condominium management in Singapore.</p>')
    # Paragraph 4
    $content = [regex]::Replace($content, "(?i)<p[^>]*>Wee Meng works directly with managing agents.*?sold off a catalogue.*?</p>", '<p class="sv-author-client-focus">Wee Meng works directly with managing agents, MCSTs, property developers, architects, and security companies to design systems that are engineered for the site, not sold off a catalogue.</p>')

    [System.IO.File]::WriteAllText($f.FullName, $content)
}
