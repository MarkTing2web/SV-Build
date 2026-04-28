SECUREVISION LANDED RESIDENTIAL PORTFOLIO TEMPLATE
Version: 3.0 — April 2026
Aligned with: _template-condominium-portfolio-case-v5.html

PAGE TYPE:
Portfolio / Case Study — Landed Residential
(Detached bungalow, semi-detached, terrace, cluster, developer bungalow)

════════════════════════════════════════════════════════
STANDARD PAGE FLOW
════════════════════════════════════════════════════════

1.  Head
2.  Nav — <nav id="sv-nav"></nav>
3.  Hero
4.  Trust Bar
5.  Breadcrumb
6.  Section 1 — Project Snapshot        (sv-section-grey)
7.  Section 2 — Project Overview        (sv-section-white)
8.  Section 3 — Design Intent           (sv-section-grey)
9.  Section 4 — Our Approach            (sv-section-white)
10. Section 5 — Security Layers         (sv-section-grey)
11. Section 6 — Outcome                 (sv-section-white)
12. Section 7 — Securevision Insight    (sv-section-grey + no-bottom-spacing)
13. Section 8 — Discovery Path          (sv-section-white)
14. Section 9 — Related Projects        (sv-section-grey)
15. Final CTA                           (Dark full-width)
16. Footer — <footer id="sv-footer"></footer>
17. DOMContentLoaded script (sv-* dynamic values)
18. <script src="/nav-footer.js"></script>

SECTION EYEBROW NAMES — MANDATORY:
Use exactly these labels. No variations permitted.
- Project Snapshot
- Technologies Implemented        (right col of Section 1)
- Project Overview
- Security Systems Implemented    (right col of Section 2)
- Design Intent
- Our Approach
- Security Layers
- Outcome
- Securevision Insight
- Discovery Path
- Next Steps in Discovery
- Planning a Landed Home?         (eyebrow-light in Final CTA)

BACKGROUND ALTERNATION — MANDATORY:
Section 1  Project Snapshot          sv-section-grey
Section 2  Project Overview          sv-section-white
Section 3  Design Intent             sv-section-grey
Section 4  Our Approach              sv-section-white
Section 5  Security Layers           sv-section-grey
Section 6  Outcome                   sv-section-white
Section 7  Securevision Insight      sv-section-grey  + no-bottom-spacing
Section 8  Discovery Path            sv-section-white
Section 9  Related Projects          sv-section-grey
Final CTA  Dark full-width image overlay

════════════════════════════════════════════════════════
HOW LANDED DIFFERS FROM CONDOMINIUM TEMPLATE
════════════════════════════════════════════════════════

1. TWO snapshot blocks instead of one:
   - Section 1 (Project Snapshot): stats + Technologies Implemented
     → links to /brands/ pages — same as condo
   - Section 2 (Project Overview): overview table + Security Systems Implemented
     → links to /systems/ pages — landed-specific

2. NO Transformation or Decision Point sections
   Landed homes are design-led, not problem-led.
   The narrative moves directly from Design Intent to Our Approach.

3. NO Results & Impact cards
   Outcomes for landed homes are qualitative (discreet presence,
   peace of mind, architectural harmony). Use prose + Securevision
   Insight pullquote instead of the 3-card grid used on condo pages.

4. ARCHITECT CREDIT in Design Intent (when applicable)
   Name the architect with a link to their website.
   Use rel="noopener" target="_blank".
   Firms we have worked with:
   - aKTa-rchitects — https://www.akta.com.sg/
   - HYLA Architects — https://www.hyla.com.sg/
   - Edmund Ng Architects — https://edmundngarchitects.com/
   - DI+ Architects — https://diplus.asia/
   Omit architect credit if no architect was involved.

5. DISCOVERY PATH links to landed-relevant systems:
   - Private Home Security  → /solutions/residential.html
   - Surveillance           → /systems/surveillance.html
   - People Access          → /systems/access-control.html
   - Vehicle Access & Gates → /systems/vehicle-access.html
   (Replace Platform Management with Vehicle Access for landed)

════════════════════════════════════════════════════════
SECTION SPECIFICATIONS
════════════════════════════════════════════════════════

HERO:
Same structure as condo hero.
- Dark overlay background image
- Left-aligned content
- Badge: RESIDENTIAL CASE STUDY
- Location line
- H1: project name or headline
- Subtitle: one sentence
- Exactly 4 stats relevant to the project
- portfolio-stat-grid / portfolio-stat / portfolio-stat-value / portfolio-stat-label

Required structure:
<header class="portfolio-hero">
  <img src="/images/portfolio/[image].webp" alt="[Alt text]" class="hero-image">
  <div class="hero-overlay"></div>
  <div class="container pos-relative z-2">
    <div class="portfolio-kicker">
      <span class="badge badge-primary">Residential Case Study</span>
      <span class="portfolio-meta">📍 [Location], Singapore</span>
    </div>
    <h1 class="portfolio-hero-title">[Headline]</h1>
    <p class="portfolio-hero-subtitle">[One sentence description]</p>
    <div class="portfolio-taxonomy" aria-label="Project taxonomy">
      <span class="portfolio-chip">Property Type: [Type]</span>
      <span class="portfolio-chip">Architect: [Name or Omit]</span>
    </div>
    <div class="portfolio-stat-grid">
      <div class="portfolio-stat">
        <span class="portfolio-stat-value">[Value]</span>
        <span class="portfolio-stat-label">[Label]</span>
      </div>
      <!-- Repeat for 4 stats total -->
    </div>
  </div>
</header>

────────────────────────────────────────────────────────
SECTION 1 — PROJECT SNAPSHOT
────────────────────────────────────────────────────────
Two-column grid: left = snapshot stats, right = Technologies Implemented.
Technologies Implemented links to /brands/ pages only.
Same structure as condo Project Snapshot.

Required HTML classes:
- portfolio-snapshot
- portfolio-snapshot-grid
- snapshot-main
- snapshot-tech-col      (wrapper — eyebrow sits outside card)
- snapshot-tech-card     (white card box)
- portfolio-tech-stack
- portfolio-tech-item
- tech-brand-name
- tech-brand-desc

Required structure (right column):
<div class="snapshot-tech-col">
  <span class="eyebrow">Technologies Implemented</span>
  <div class="snapshot-tech-card">
    <div class="portfolio-tech-stack">
      <a href="/brands/[brand].html" class="portfolio-tech-item">
        <span class="tech-brand-name">[Brand Name]</span>
        <span class="tech-brand-desc">[One line — what was deployed]</span>
      </a>
      <!-- Repeat for each brand used -->
    </div>
  </div>
</div>

Common landed brands:
- Paradox  → /brands/paradox.html    — Alarm panel and zone control
- RISCO    → /brands/risco.html      — Alarm panel and zone control
- AJAX     → /brands/ajax.html       — Wireless alarm system
- Hikvision→ /brands/hikvision.html  — IP surveillance cameras and NVR
- Aiphone  → /brands/aiphone.html    — Video intercom and door station
- Akuvox   → /brands/akuvox.html     — SIP-based IP intercom
- FAAC     → /brands/faac.html       — Gate automation and barrier arms
- Dormer   → /brands/dormer.html     — Gate automation

────────────────────────────────────────────────────────
SECTION 2 — PROJECT OVERVIEW
────────────────────────────────────────────────────────
Two-column grid: left = overview table, right = Security Systems Implemented.
Security Systems Implemented links to /systems/ pages only.
This section is UNIQUE to landed pages — condos do not have this.

Left column — overview table:
Standard rows: Location, Sector, Property Type, Architect (if applicable), Scope

Required HTML classes:
- portfolio-overview-table (or standard HTML table with comparison-table class)

Right column — Security Systems Implemented:
Required HTML classes:
- snapshot-systems-col   (wrapper — eyebrow sits outside card)
- snapshot-systems-card  (white card box)
- portfolio-systems-stack
- portfolio-system-item
- system-name
- system-desc

Required structure (right column):
<div class="snapshot-systems-col">
  <span class="eyebrow">Security Systems Implemented</span>
  <div class="snapshot-systems-card">
    <div class="portfolio-systems-stack">
      <a href="/systems/[system].html" class="portfolio-system-item">
        <span class="system-name">[System Name]</span>
        <span class="system-desc">[One line — brand and key spec]</span>
      </a>
      <!-- Repeat for each system -->
    </div>
  </div>
</div>

Common landed systems:
- Burglar Alarm     → /systems/intrusion.html (add comment if page missing)
- Surveillance      → /systems/surveillance.html
- Intercom          → /systems/access-control.html
- Gate Automation   → /systems/vehicle-access.html

────────────────────────────────────────────────────────
SECTION 3 — DESIGN INTENT
────────────────────────────────────────────────────────
Tone: design-led, not problem-led.
Focus on:
- Architectural harmony and privacy
- The homeowner's brief and lifestyle
- Technology supporting the home without dominating it
- Discreet protection over visible deterrence

ARCHITECT CREDIT (include when architect was involved):
Add a one-line credit inside the section body:
<p>This project was designed in collaboration with
<a href="[architect URL]" target="_blank" rel="noopener">[Architect Name]</a>,
[one-line descriptor of their practice].</p>

Do NOT copy architect bios verbatim from their website.
Write a short original descriptor.

No card structure needed. Prose only.

────────────────────────────────────────────────────────
SECTION 4 — OUR APPROACH
────────────────────────────────────────────────────────
Explain Securevision's role as an integration partner.
Focus on:
- Coordinated planning across all systems
- Alignment with architectural and design intent
- Security built in, not added as an afterthought
- Early engagement with builder and M&E team

No card structure needed. Prose only.

────────────────────────────────────────────────────────
SECTION 5 — SECURITY LAYERS
────────────────────────────────────────────────────────
Use 3 or 4 portfolio-layer-card blocks in a grid-3 or grid-4.
Each card covers one functional security layer.

Standard layer labels for landed homes:
- Intrusion Protection  — alarm system, zones, perimeter detection
- Surveillance          — cameras, NVR, coverage map
- Visitor Communication — video intercom, door station, mobile access
- Entry Control         — auto gate, pedestrian door, remote control

Do NOT use inline styles. Use portfolio-layer-card class.

Required structure:
<div class="grid-3 mt-40">
  <div class="portfolio-layer-card">
    <span class="eyebrow">[Layer label]</span>
    <h3>[Layer heading]</h3>
    <p>[2–3 sentences. Non-technical. Outcome-focused.]</p>
  </div>
  <!-- Repeat for each layer -->
</div>

────────────────────────────────────────────────────────
SECTION 6 — OUTCOME
────────────────────────────────────────────────────────
Prose only. Do NOT use portfolio-result-card here.
Landed outcomes are qualitative — do not invent metrics.

Focus on:
- Discreet security presence
- Complete layered protection without visual clutter
- Intuitive daily usability for residents
- Clean integration into a premium home environment
- Architect and client satisfaction

One to two paragraphs. Keep it calm and confident.

────────────────────────────────────────────────────────
SECTION 7 — SECUREVISION INSIGHT
────────────────────────────────────────────────────────
Same pullquote treatment as condo pages.
Centred, no background, no border.
Controlled entirely by sv-shared.css .portfolio-insight.

Required structure:
<section class="portfolio-insight-section section-spacing no-bottom-spacing">
  <div class="container">
    <div class="portfolio-insight">
      <span class="eyebrow">Securevision Insight</span>
      <h2>[Sharp one-line insight]</h2>
      <p>[One concise paragraph. Engineering-led, not salesy.]</p>
    </div>
  </div>
</section>

Example insights for landed:
- Security in landed homes is most effective when it is designed as part of
  the architecture — not specified after the walls are built.
- The best home security system is the one residents use without thinking
  about it. Discreet integration is the goal, not visible deterrence.

────────────────────────────────────────────────────────
SECTION 8 — DISCOVERY PATH
────────────────────────────────────────────────────────
Fixed 4-card layout. Same HTML structure as condo Discovery Path.
Landed-specific links — replace Platform Management with Vehicle Access.

Required cards (do not change):
1. Private Home Security  → /solutions/residential.html
   Image: /images/prop-residential.webp
   Title: Private Home Security
   Desc: Integrated security design for landed homes and private residences.

2. Surveillance & Detection → /systems/surveillance.html
   Image: /images/pillar_surveillance.webp
   Title: Surveillance & Detection
   Desc: CCTV coverage, NVR recording, and perimeter monitoring.

3. People Access & Intercom → /systems/access-control.html
   Image: /images/pillar_people_access.webp
   Title: People Access & Intercom
   Desc: Video door stations, visitor verification, and access control.

4. Vehicle Access & Gates → /systems/vehicle-access.html
   Image: /images/pillar_vehicle_access.webp
   Title: Vehicle Access & Gates
   Desc: Auto gates, pedestrian doors, and remote entry management.

Required HTML classes (same as condo):
- portfolio-link-stack mt-40
- portfolio-link-card
- portfolio-link-card-body

────────────────────────────────────────────────────────
SECTION 9 — RELATED PROJECTS
────────────────────────────────────────────────────────
Show 3 related landed residential portfolio case studies.
Do not include the current project.
Do not link to condo pages — audience is different.

Required HTML classes (same as condo):
- grid-3 mt-48
- card card-clickable related-project-card
- related-project-body
- related-project-badge   (use "Landed Residential" not "Condominium")
- related-project-title
- related-project-text
- related-project-link

Section header must be:
<div class="section-header text-center">
  <span class="eyebrow">Next Steps in Discovery</span>
  <h2>Related Case Studies</h2>
  <p class="text-left mt-16">Explore how we have approached security integration for other landed homes and private residences in Singapore.</p>
</div>

────────────────────────────────────────────────────────
FINAL CTA
────────────────────────────────────────────────────────
Same structure as condo Final CTA.
Background: project hero image with dark overlay.
Heading: Planning a Landed Home or Major Upgrade?
Body: Engage Securevision early to design security that works
as one complete system — integrated with your home, not added after.

Required structure:
<section id="final-cta" class="final-cta cta-high-impact" style="background-image: linear-gradient(rgba(15, 23, 42, 0.78), rgba(15, 23, 42, 0.78)), url('/images/portfolio/[project-image].webp');">
  <div class="container text-center">
    <span class="eyebrow-light">Planning a Landed Home?</span>
    <h2>Planning a Landed Home or Major Upgrade?</h2>
    <p class="cta-subtext">Engage Securevision early to design security that works as one complete system — integrated with your home, not added after.</p>
    <div class="btn-group center">
      <a href="/request-site-assessment-singapore.html" class="btn btn-primary">Book Site Assessment</a>
      <a href="https://wa.me/6593860466" class="btn btn-outline-light">Discuss Your Project</a>
    </div>
  </div>
</section>

════════════════════════════════════════════════════════
SCRIPTS — MANDATORY
════════════════════════════════════════════════════════

Add before </body> in this order:

<script>
  document.addEventListener('DOMContentLoaded', function () {
    if (typeof SECUREVISION !== 'undefined') {
      var SV = SECUREVISION;
      document.querySelectorAll('.sv-licence').forEach(function(el) { el.textContent = SV.licenceNumber || ''; });
      document.querySelectorAll('.sv-sites').forEach(function(el) { el.textContent = SV.siteDisplay || ''; });
      document.querySelectorAll('.sv-bizsafe').forEach(function(el) { el.textContent = SV.bizsafeLevel || 'bizSAFE Level 3'; });
    }
  });
</script>
<script src="/nav-footer.js"></script>

════════════════════════════════════════════════════════
INLINE STYLE RULES
════════════════════════════════════════════════════════

DO NOT use inline style= attributes except:
- background-image on hero and final CTA (permitted)
- background-image on any section that requires a project-specific image

ALL other styling must use sv-shared.css classes.
If a class is missing, add an HTML comment:
<!-- NEEDS CSS: description of class required -->
Do NOT add a style= workaround.

════════════════════════════════════════════════════════
COPY TONE
════════════════════════════════════════════════════════
- British English
- Premium but not flowery
- Design-led and engineering-informed
- Calm and confident
- No sales hype
- No condo / MCST language
- No exaggerated claims or invented metrics

════════════════════════════════════════════════════════
ANTI-GRAVITY RULE
════════════════════════════════════════════════════════
"Use this landed residential portfolio template. Do not invent a new
layout. Do not use inline styles except for background-image. Fill
the approved blocks with project content only.

Nav uses <nav id='sv-nav'></nav> injected by nav-footer.js.
Footer uses <footer id='sv-footer'></footer>.
Add DOMContentLoaded script and <script src='/nav-footer.js'></script>
before </body>.

Section 1 Technologies Implemented links to /brands/ pages only.
Section 2 Security Systems Implemented links to /systems/ pages only.
Discovery Path uses the 4 fixed landed cards — do not change the links.
Related Projects badge must say 'Landed Residential' not 'Condominium'.

Do not add a Project Priorities section — merge any priorities content
into Design Intent. Do not add a Transformation or Decision Point section.
These are condo-specific and have no place in a landed portfolio page."

════════════════════════════════════════════════════════
REFERENCE PAGES
════════════════════════════════════════════════════════
Use these as reference once migrated:
- dyson-8-residences-landed-home.html — most complete existing page
- siglap-bank-landed-home.html — good Design Intent example
- dunbar-walk-landed-home.html — good architect credit example
