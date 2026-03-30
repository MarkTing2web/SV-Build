# Site-Wide Navigation Repair & Standardization Script (Ver 5 - The Surgical Decimator)

$newNav = @"
    <nav class="main-nav">
        <div class="nav-container">
            <!-- Logo + Wordmark -->
            <a href="index.html" class="nav-logo-link" aria-label="Securevision Home">
                <img src="images/securevision-logo-white.png" alt="Securevision Logo" class="nav-logo-img">
                <span class="wordmark nav-wordmark">SECUREVISION</span>
            </a>

            <!-- Desktop nav links -->
            <ul class="nav-menu">
                <li class="nav-item"><a href="security-solutions-singapore.html" class="nav-link has-dropdown">Solutions</a>
                    <div class="simple-dropdown">
                        <a href="residential-security-singapore.html">Private Homes</a>
                        <a href="condominiums.html">Condominiums</a>
                        <a href="commercial-security-singapore.html">Commercial &amp; Retail</a>
                        <a href="industrial-security-singapore.html">Industrial &amp; Logistics</a>
                        <a href="government-institution-security-singapore.html">Institutions &amp; Government</a>
                        <a href="healthcare-security-singapore.html">Healthcare &amp; Managed Living</a>
                    </div>
                </li>
                <li class="nav-item"><a href="security-systems-singapore.html" class="nav-link has-dropdown">Systems</a>
                    <div class="simple-dropdown">
                        <a href="surveillance-detection.html">CCTV &amp; Surveillance</a>
                        <a href="people-access-control.html">Access Control Systems</a>
                        <a href="burglar-alarm.html">Alarm &amp; Intrusion</a>
                        <a href="intercom-system-singapore.html">Intercom &amp; Communication</a>
                        <a href="auto-gate-singapore.html">Autogate &amp; Barriers</a>
                        <a href="integrated-security-platform.html">Platform &amp; Integration</a>
                        <a href="security-systems-singapore.html"><strong>&rarr; View All Systems</strong></a>
                    </div>
                </li>
                <li class="nav-item"><a href="security-brands-singapore.html" class="nav-link has-dropdown">Brands</a>
                    <div class="simple-dropdown wide-dropdown">
                        <a href="security-brands-singapore.html#surveillance"><strong>Surveillance</strong> &mdash; Hikvision &bull; Hanwha &bull; Uniview &bull; Milesight</a>
                        <a href="security-brands-singapore.html#access"><strong>Access Control</strong> &mdash; Suprema &bull; ZKTeco &bull; HID &bull; EntryPass</a>
                        <a href="security-brands-singapore.html#intercom"><strong>Intercoms</strong> &mdash; Akuvox &bull; Aiphone &bull; Kocom</a>
                        <a href="security-brands-singapore.html#alarms"><strong>Alarms</strong> &mdash; AJAX &bull; RISCO &bull; Paradox &bull; DSC</a>
                        <a href="security-brands-singapore.html#gates"><strong>Gates & Barriers</strong> &mdash; FAAC &bull; MAG &bull; Dormer</a>
                        <hr>
                        <a href="security-brands-singapore.html"><strong>&rarr; View All Technology Partners</strong></a>
                    </div>
                </li>
                <li class="nav-item"><a href="portfolio.html" class="nav-link">Portfolio</a></li>
                <li class="nav-item"><a href="resources.html" class="nav-link has-dropdown">Resources</a>
                  <div class="simple-dropdown">
                    <a href="resources.html#guides">Technical Guides</a>
                    <a href="resources.html#tools">Planning Tools</a>
                    <a href="resources.html#library">Product Library</a>
                    <a href="resources.html#videos">Video Training</a>
                    <a href="resources.html#faq">FAQ</a>
                    <a href="resources.html#trade">For Professionals</a>
                    <a href="resources.html"><strong>&rarr; All Resources</strong></a>
                  </div>
                </li>
                <li class="nav-item"><a href="security-articles-singapore.html" class="nav-link">Insights</a></li>
                <li class="nav-item"><a href="about.html" class="nav-link has-dropdown">About</a>
                    <div class="simple-dropdown">
                        <a href="about.html">Our Story</a>
                        <a href="awards-certifications.html">Awards &amp; Certifications</a>
                        <a href="contact.html">Contact Us</a>
                    </div>
                </li>
            </ul>

            <div class="nav-right">
                <button class="nav-search-btn" aria-label="Search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></button>
            </div>

            <button class="mobile-toggle" onclick="toggleMobileMenu()"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg></button>
        </div>
    </nav>

    <div class="mobile-menu" id="mobileMenu">
      <div class="mobile-menu-item" onclick="toggleSubmenu('solSub')">Solutions &#9662;<div class="mobile-submenu" id="solSub"><a href="security-solutions-singapore.html"><strong>&rarr; View All Solutions</strong></a><a href="residential-security-singapore.html">Private Homes</a><a href="condominiums.html">Condominiums</a><a href="commercial-security-singapore.html">Commercial &amp; Retail</a><a href="industrial-security-singapore.html">Industrial &amp; Logistics</a><a href="government-institution-security-singapore.html">Institutions &amp; Government</a><a href="healthcare-security-singapore.html">Healthcare &amp; Managed Living</a></div></div>
      <div class="mobile-menu-item" onclick="toggleSubmenu('sysSub')">Systems &#9662;<div class="mobile-submenu" id="sysSub"><a href="security-systems-singapore.html"><strong>&rarr; View All Systems</strong></a><a href="surveillance-detection.html">CCTV &amp; Surveillance</a><a href="people-access-control.html">Access Control Systems</a><a href="burglar-alarm.html">Alarm &amp; Intrusion</a><a href="intercom-system-singapore.html">Intercom &amp; Communication</a><a href="auto-gate-singapore.html">Autogate &amp; Barriers</a><a href="integrated-security-platform.html">Platform &amp; Integration</a></div></div>
      <div class="mobile-menu-item" onclick="toggleSubmenu('brandSub')">Brands &#9662;<div class="mobile-submenu" id="brandSub">
          <a href="security-brands-singapore.html"><strong>&rarr; View All Partners</strong></a>
          <a href="security-brands-singapore.html#surveillance">Surveillance &mdash; Hik · Han · Uni · Mil</a>
          <a href="security-brands-singapore.html#access">Access &mdash; Sup · ZK · HID · EP</a>
          <a href="security-brands-singapore.html#intercom">Intercoms &mdash; Aku · Aip · Koc</a>
          <a href="security-brands-singapore.html#alarms">Alarms &mdash; AJAX · RIS · Par · DSC</a>
          <a href="security-brands-singapore.html#gates">Gates &mdash; FAAC · MAG · Dor</a>
        </div></div>
      <div class="mobile-menu-item" onclick="toggleSubmenu('portSub')">Portfolio &#9662;<div class="mobile-submenu" id="portSub"><a href="portfolio.html"><strong>&rarr; All Projects</strong></a><a href="portfolio.html">Private Homes</a><a href="portfolio.html">Condominiums</a><a href="commercial-security-singapore.html">Commercial &amp; Retail</a><a href="industrial-security-singapore.html">Industrial &amp; Logistics</a><a href="government-institution-security-singapore.html">Institutions &amp; Government</a><a href="healthcare-security-singapore.html">Healthcare &amp; Managed Living</a></div></div>
      <div class="mobile-menu-item" onclick="toggleSubmenu('resSub')">Resources &#9662;<div class="mobile-submenu" id="resSub"><a href="resources.html"><strong>&rarr; All Resources</strong></a><a href="resources.html#guides">Technical Guides</a><a href="resources.html#tools">Planning Tools</a><a href="resources.html#library">Product Library</a><a href="resources.html#videos">Video Training</a><a href="resources.html#faq">FAQ</a><a href="resources.html#trade">For Professionals</a></div></div>
      <a href="security-articles-singapore.html" class="mobile-menu-item">Insights</a>
      <div class="mobile-menu-item" onclick="toggleSubmenu('abtSub')">About &#9662;<div class="mobile-submenu" id="abtSub"><a href="about.html"><strong>&rarr; About Securevision</strong></a><a href="about.html#founder">Founder Story</a><a href="awards-certifications.html">Certifications</a><a href="contact.html">Contact Us</a></div></div>
    </div>
"@

$newScript = @"
    <script>
        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            if (menu) menu.classList.toggle('active');
        }

        function toggleSubmenu(id) {
            const sub = document.getElementById(id);
            if (sub) sub.classList.toggle('active');
        }

        window.addEventListener('scroll', () => {
            const nav = document.querySelector('.main-nav');
            const logo = document.querySelector('.nav-logo-img');
            if (!nav) return;
            if (window.scrollY > 20) {
                nav.classList.add('scrolled');
                if (logo) logo.src = 'images/securevision-logo-blue.png';
            } else {
                nav.classList.remove('scrolled');
                if (logo) logo.src = 'images/securevision-logo-white.png';
            }
        });
        
        // Current Year
        const yearSpan = document.querySelector('.current-year');
        if (yearSpan) yearSpan.textContent = new Date().getFullYear();
    </script>
"@

# List of files to update
$files = Get-ChildItem *.html -Exclude "standardize-nav.ps1", "NAVIGATION-REPAIR.ps1"

foreach ($f in $files) {
    $file = $f.FullName
    $content = Get-Content $file -Raw
    
    # 1. Clear all main-nav blocks
    $content = [regex]::Replace($content, "(?s)<nav class=`"main-nav`".*?</nav>", "")
    
    # 2. Clear all mobile-menu blocks (the containers)
    $content = [regex]::Replace($content, "(?s)<div class=`"mobile-menu`".*?</div>", "")
    
    # 3. Clear orphaned contents (nested approach)
    # Delete submenus first to avoid premature </div> matching for parents
    $content = [regex]::Replace($content, "(?s)<div class=`"mobile-submenu`".*?</div>", "")
    # Now delete menu items
    $content = [regex]::Replace($content, "(?s)<div class=`"mobile-menu-item`".*?</div>", "")
    
    # 4. Clean up lingering broken closers and rogue artifacts
    $content = [regex]::Replace($content, "(?s)</nav>\s*(</div>)?\s*(iv>)?\s*(</div>)?\s*(</nav>)?", "")
    # Standardize whitespace and remove naked closing divs that might have been left behind
    $content = [regex]::Replace($content, "(?s)<\s*</div>", "")
    $content = [regex]::Replace($content, "(?s)> \s*</div>", "")
    $content = [regex]::Replace($content, "(?s)>\s*</div>", "")
    $content = [regex]::Replace($content, "(?s)< \s*</div>", "")

    # 5. INSERT NEW NAV AFTER <body>
    $bodyPattern = "(?i)<body.*?>"
    if ($content -match $bodyPattern) {
        $bodyTag = $matches[0]
        # Avoid double insert if repeating script
        if ($content -notmatch "<nav class=`"main-nav`"") {
            $content = $content.Replace($bodyTag, "$bodyTag`n$newNav")
            Write-Host "Repaired $file"
        }
    }

    # 6. STANDARDIZE SCRIPT
    $scriptRegex = "(?s)<script>\s*function toggleMobileMenu.*?/script>"
    if ($content -match "function toggleMobileMenu") {
        $content = [regex]::Replace($content, $scriptRegex, $newScript)
    } elseif ($content -match "</body>") {
        $content = $content.Replace("</body>", "$newScript`n</body>")
    }
    
    Set-Content $file $content -NoNewline
}
