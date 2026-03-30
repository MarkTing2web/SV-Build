# STANDARDIZE-SITE.ps1
# Simple, robust site-wide navigation fix.

$navBlock = @"
<nav class="main-nav">
    <div class="nav-container">
        <a href="index.html" class="nav-logo-link" aria-label="Securevision Home">
            <img src="images/securevision-logo-white.png" alt="Securevision Logo" class="nav-logo-img">
            <span class="wordmark nav-wordmark">SECUREVISION</span>
        </a>
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
                </div>
            </li>
            <li class="nav-item"><a href="security-brands-singapore.html" class="nav-link has-dropdown">Brands</a>
                <div class="simple-dropdown wide-dropdown">
                    <a href="security-brands-singapore.html#surveillance"><strong>Surveillance</strong> &mdash; Hikvision &bull; Hanwha &bull; Uniview &bull; Milesight</a>
                    <a href="security-brands-singapore.html#access"><strong>Access Control</strong> &mdash; Suprema &bull; ZKTeco &bull; HID &bull; EntryPass</a>
                    <a href="security-brands-singapore.html#intercom"><strong>Intercoms</strong> &mdash; Akuvox &bull; Aiphone &bull; Kocom</a>
                    <a href="security-brands-singapore.html#alarms"><strong>Alarms</strong> &mdash; AJAX &bull; RISCO &bull; Paradox &bull; DSC</a>
                    <a href="security-brands-singapore.html#gates"><strong>Gates & Barriers</strong> &mdash; FAAC &bull; MAG &bull; Dormer</a>
                </div>
            </li>
            <li class="nav-item"><a href="portfolio.html" class="nav-link">Portfolio</a></li>
            <li class="nav-item"><a href="resources.html" class="nav-link">Resources</a></li>
            <li class="nav-item"><a href="security-articles-singapore.html" class="nav-link">Insights</a></li>
            <li class="nav-item"><a href="about.html" class="nav-link">About</a></li>
        </ul>
        <div class="nav-right">
            <button class="nav-search-btn" aria-label="Search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></button>
        </div>
        <button class="mobile-toggle" id="mobileToggle" onclick="toggleMobileMenu()" aria-label="Toggle Menu"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg></button>
    </div>
    <div class="mobile-menu" id="mobileMenu">
        <div class="mobile-menu-item" onclick="toggleSubmenu('solSub')">Solutions &#9662;<div class="mobile-submenu" id="solSub"><a href="security-solutions-singapore.html">View All Solutions</a><a href="residential-security-singapore.html">Private Homes</a><a href="condominiums.html">Condominiums</a><a href="commercial-security-singapore.html">Commercial &amp; Retail</a><a href="industrial-security-singapore.html">Industrial &amp; Logistics</a><a href="government-institution-security-singapore.html">Institutions &amp; Government</a><a href="healthcare-security-singapore.html">Healthcare &amp; Managed Living</a></div></div>
        <div class="mobile-menu-item" onclick="toggleSubmenu('sysSub')">Systems &#9662;<div class="mobile-submenu" id="sysSub"><a href="security-systems-singapore.html">View All Systems</a><a href="surveillance-detection.html">CCTV &amp; Surveillance</a><a href="people-access-control.html">Access Control Systems</a><a href="burglar-alarm.html">Alarm &amp; Intrusion</a><a href="intercom-system-singapore.html">Intercom &amp; Communication</a><a href="auto-gate-singapore.html">Autogate &amp; Barriers</a><a href="integrated-security-platform.html">Platform &amp; Integration</a></div></div>
        <div class="mobile-menu-item" onclick="toggleSubmenu('brandSub')">Brands &#9662;<div class="mobile-submenu" id="brandSub"><a href="security-brands-singapore.html">All Partners</a><a href="hikvision-singapore.html">Hikvision</a><a href="suprema-singapore.html">Suprema</a><a href="akuvox-singapore.html">Akuvox</a><a href="ajax-alarm-singapore.html">AJAX</a></div></div>
        <div class="mobile-menu-item" onclick="toggleSubmenu('portSub')">Portfolio &#9662;<div class="mobile-submenu" id="portSub"><a href="portfolio.html">All Projects</a><a href="residential-security-singapore.html">Private Homes</a><a href="condominiums.html">Condominiums</a></div></div>
        <a href="resources.html" class="mobile-menu-item">Resources</a>
        <a href="security-articles-singapore.html" class="mobile-menu-item">Insights</a>
        <a href="about.html" class="mobile-menu-item">About</a>
        <a href="contact.html" class="mobile-menu-item">Contact Us</a>
    </div>
</nav>
"@

$htmlFiles = Get-ChildItem "*.html"

foreach ($file in $htmlFiles) {
    Write-Host "Repairing $($file.Name)..."
    $c = [System.IO.File]::ReadAllText($file.FullName)
    
    # Remove existing nav and mobile menu
    $c = [regex]::Replace($c, "(?s)<nav.*?class=`"main-nav`".*?<\/nav>", "")
    $c = [regex]::Replace($c, "(?s)<div class=`"mobile-menu`".*?<\/div>", "")

    # Inject
    if ($c -match "<body[^>]*>") {
        $tag = $matches[0]
        $c = $c.Replace($tag, "$tag`n$navBlock")
    }

    # Fix gaps
    $c = $c.Replace("padding: 160px 0 120px;", "padding: 100px 0 80px;")
    $c = $c.Replace("padding: 160px 0 80px;", "padding: 100px 0 60px;")

    [System.IO.File]::WriteAllText($file.FullName, $c)
}
Write-Host "Done."
