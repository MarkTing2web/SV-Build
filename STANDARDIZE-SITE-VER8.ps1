# Site-Wide Navigation Repair & Standardization Script (Ver 8 - The Direct Portfolio)
# This script eliminates the Portfolio sub-menu and makes it a direct link.

$masterNav = @"
<nav class="main-nav">
<div class="nav-container">
  <!-- Logo + Wordmark — always left -->
  <a href="index.html" class="nav-logo-link" aria-label="Securevision Home">
    <img src="images/securevision-logo-white.png" alt="Securevision Logo" class="nav-logo-img">
    <span class="wordmark nav-wordmark">SECUREVISION</span>
  </a>
  <!-- Hamburger — centred absolutely on mobile (via CSS) -->
  <button class="mobile-toggle" id="mobileToggle" onclick="toggleMobileMenu()" aria-label="Toggle Menu"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg></button>
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
        <a href="security-solutions-singapore.html"><strong>&rarr; View All Solutions</strong></a>
      </div>
    </li>
    <li class="nav-item"><a href="security-systems-singapore.html" class="nav-link has-dropdown">Systems</a>
      <div class="simple-dropdown">
        <a href="surveillance-detection.html">Surveillance &amp; Detection</a>
        <a href="people-access-control.html">People Access Control</a>
        <a href="vehicle-access-control.html">Vehicle Access &amp; Barriers</a>
        <a href="integrated-security-platform.html">Platform Management</a>
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
        <a href="about.html#founder">Founder&rsquo;s Story</a>
        <a href="awards-certifications.html">Awards &amp; Certifications</a>
        <a href="contact.html">Contact Us</a>
      </div>
    </li>
  </ul>
  <!-- Desktop search icon -->
  <div class="nav-right">
    <button class="nav-search-btn" id="desktopSearchBtn" aria-label="Search" onclick="alert('Search coming soon')"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></button>
  </div>
  <!-- Mobile search icon — always right end on mobile -->
  <button class="mobile-search-btn" id="mobileSearchBtn" aria-label="Search" onclick="alert('Search coming soon')"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></button>
</div>
<div class="mobile-menu" id="mobileMenu">
  <div class="mobile-menu-item" onclick="toggleSubmenu('solSub')">Solutions &#9662;<div class="mobile-submenu" id="solSub"><a href="security-solutions-singapore.html"><strong>&rarr; View All Solutions</strong></a><a href="residential-security-singapore.html">Private Homes</a><a href="condominiums.html">Condominiums</a><a href="commercial-security-singapore.html">Commercial &amp; Retail</a><a href="industrial-security-singapore.html">Industrial &amp; Logistics</a><a href="government-institution-security-singapore.html">Institutions &amp; Government</a><a href="healthcare-security-singapore.html">Healthcare &amp; Managed Living</a></div></div>
  <div class="mobile-menu-item" onclick="toggleSubmenu('sysSub')">Systems &#9662;<div class="mobile-submenu" id="sysSub">
      <a href="surveillance-detection.html">Surveillance &amp; Detection</a>
      <a href="people-access-control.html">People Access Control</a>
      <a href="vehicle-access-control.html">Vehicle Access &amp; Barriers</a>
      <a href="integrated-security-platform.html">Platform Management</a>
    </div></div>
  <div class="mobile-menu-item" onclick="toggleSubmenu('brandSub')">Brands &#9662;<div class="mobile-submenu" id="brandSub">
      <a href="security-brands-singapore.html"><strong>&rarr; View All Partners</strong></a>
      <a href="security-brands-singapore.html#surveillance">Surveillance &mdash; Hik · Han · Uni · Mil</a>
      <a href="security-brands-singapore.html#access">Access &mdash; Sup · ZK · HID · EP</a>
      <a href="security-brands-singapore.html#intercom">Intercoms &mdash; Aku · Aip · Koc</a>
      <a href="security-brands-singapore.html#alarms">Alarms &mdash; AJAX · RIS · Par · DSC</a>
      <a href="security-brands-singapore.html#gates">Gates &mdash; FAAC · MAG · Dor</a>
    </div></div>
  <a href="portfolio.html" class="mobile-menu-item">Portfolio</a>
  <div class="mobile-menu-item" onclick="toggleSubmenu('resSub')">Resources &#9662;<div class="mobile-submenu" id="resSub"><a href="resources.html"><strong>&rarr; All Resources</strong></a><a href="resources.html#guides">Technical Guides</a><a href="resources.html#tools">Planning Tools</a><a href="resources.html#library">Product Library</a><a href="resources.html#videos">Video Training</a><a href="resources.html#faq">FAQ</a><a href="resources.html#trade">For Professionals</a></div></div>
  <a href="security-articles-singapore.html" class="mobile-menu-item">Insights</a>
  <div class="mobile-menu-item" onclick="toggleSubmenu('abtSub')">About &#9662;<div class="mobile-submenu" id="abtSub"><a href="about.html"><strong>&rarr; About Securevision</strong></a><a href="about.html#founder">Founder&rsquo;s Story</a><a href="awards-certifications.html">Awards</a><a href="contact.html">Contact Us</a></div></div>
</div>
</nav>
"@

$masterScript = @'
<script>
function toggleMobileMenu() {
  const menu = document.getElementById('mobileMenu');
  if (menu) menu.classList.toggle('active');
}

function toggleSubmenu(id) {
  const sub = document.getElementById(id);
  if (sub) {
    const isActive = sub.classList.contains('active');
    document.querySelectorAll('.mobile-submenu').forEach(s => s.classList.remove('active'));
    if (!isActive) sub.classList.add('active');
  }
}

document.addEventListener('click', function (e) {
  const nav = document.querySelector('.main-nav');
  const menu = document.getElementById('mobileMenu');
  if (nav && !nav.contains(e.target) && menu && menu.classList.contains('active')) {
    menu.classList.remove('active');
  }
});

// Header scroll effect
window.addEventListener('scroll', () => {
  const nav = document.querySelector('.main-nav');
  const logo = document.querySelector('.nav-logo-img');
  if (nav && logo) {
    if (window.scrollY > 20) {
      nav.classList.add('scrolled');
      logo.src = 'images/securevision-logo-blue.png';
    } else {
      nav.classList.remove('scrolled');
      logo.src = 'images/securevision-logo-white.png';
    }
  }
});

// Auto-highlight active nav link
document.querySelectorAll('.nav-link').forEach(link => {
  if (link.href === window.location.href || link.href.split('/').pop() === window.location.pathname.split('/').pop()) {
    link.classList.add('active');
  }
});

// Current Year
const yearSpan = document.querySelector('.current-year');
if (yearSpan) yearSpan.textContent = new Date().getFullYear();
</script>
'@

# Files to process
$files = Get-ChildItem *.html -Exclude "index_full.html", "index-copy.html", "door-access-backup.html"

foreach ($f in $files) {
    $filePath = $f.FullName
    $content = Get-Content $filePath -Raw

    # 1. REMOVE ALL EXISTING NAV BLOCKS (Aggressive Purge)
    $content = [regex]::Replace($content, "(?s)<nav class=`"main-nav`".*?</nav>", "")
    $content = [regex]::Replace($content, "(?s)<div class=`"mobile-menu`".*?</div>", "")
    
    # 2. REMOVE ALL EXISTING SCRIPTS with toggleMobileMenu (Legacy Purge)
    $content = [regex]::Replace($content, "(?s)<script>.*?function toggleMobileMenu.*?/script>", "")

    # 3. INSERT MASTER NAV AFTER <body>
    $bodyPattern = "(?i)<body.*?>"
    if ($content -match $bodyPattern) {
        $bodyTag = $matches[0]
        # Only insert if not already present (failsafe)
        if ($content -notmatch "class=`"main-nav`"") {
            $content = $content.Replace($bodyTag, "$bodyTag`n$masterNav")
            Write-Host "Injected Nav into $($f.Name)"
        }
    }

    # 4. INSERT MASTER SCRIPT BEFORE </body>
    if ($content -match "</body>") {
        # Avoid double script
        if ($content -notmatch "function toggleMobileMenu") {
            $content = $content.Replace("</body>", "$masterScript`n</body>")
            Write-Host "Injected Script into $($f.Name)"
        }
    }

    Set-Content $filePath $content -NoNewline
}

Write-Host "Portfolio Menu Simplification Complete." -ForegroundColor Green
