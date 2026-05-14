# SECUREVISION WEBSITE — GLOBAL DESIGN INSTRUCTION
## For use with Anti-Gravity AI Web Builder
## Version 3.2 — May 2026
## This file lives at: /_instructions/GLOBAL-INSTRUCTION.md

---

## ⚠️ CRITICAL RULES — READ BEFORE ANYTHING ELSE

1. **NEVER write inline `<style>` blocks in any HTML page.** All CSS is in external files. If a visual effect is needed that has no existing class, flag it in a comment — do NOT invent inline styles.
2. **NEVER create new CSS class names** without checking `sv-shared.css` and the relevant template CSS file first. Reuse existing classes.
3. **NEVER rewrite the NAV or FOOTER HTML.** These are frozen components. Copy them verbatim from the template file. Do not rephrase, restructure, or "improve" them.
4. **NEVER change URLs** in nav or footer links. All hrefs are canonical and must not be altered.
5. **ALWAYS use the page template file** from `/_templates/` as the starting skeleton. Fill in content — do not rebuild structure.
6. **NEVER use HTML entities** (`&amp;`, `&#9662;`, etc.) where plain Unicode characters work (e.g., `▾`, `→`, `·`, `&`). Mojibake comes from re-encoding entities — use the actual characters.
7. **Partial updates only:** When asked to update one section, touch only that section. Do not reformat, re-space, or "clean up" unrelated sections.
8. **ALL paths must be absolute** — every href, src, and url() must begin with `/`. Never use relative paths (`../` or bare filenames). This applies to CSS files, JS files, images, and all internal links.

---

## 1. PROJECT IDENTITY

**Company:** Securevision Pte Ltd  
**Tagline:** Your partner in building smart, secure, and connected communities — powered by intelligent security systems since 2006.  
**Established:** 2006  
**Domain:** www.securevision.com.sg  
**Staging:** svbuild.vercel.app  
**Primary CTA:** WhatsApp +65 9386 0466 (https://wa.me/6593860466)

**Language & Spelling Standards:**
- British English (UK) throughout.
- Key spellings: `authorisation`, `optimisation`, `labour`, `centre`, `programme`, `defence`, `licence` (noun), `licensing` (verb), `modelling`.
- Singapore-specific terms: `estate`, `MCST`, `Managing Agent`, `GCB`, `bizSAFE`, `HDB`.

**Tone of voice:**
- Professional but not cold. Engineering-led — specific, precise, evidence-based.
- Never salesy or hyperbolic.
- Speaks to property managers, MCSTs, business owners, architects.
- Singapore context throughout.

**What this site is NOT:**
- Not an e-commerce store. Not a product catalogue.
- Always "systems" not "products". Always "integrator" not "installer".

---

## 2. CSS & FILE ARCHITECTURE

### The CSS Stack (in load order — every page must load in this order)
```html
<link rel="stylesheet" href="/sv-shared.css">       <!-- Global: nav, footer, buttons, typography, hero, CTA -->
<link rel="stylesheet" href="/sv-systems.css">         <!-- /systems/ pages only -->
<link rel="stylesheet" href="/sv-solutions.css">       <!-- /solutions/ pages only -->
<link rel="stylesheet" href="/sv-brands.css">          <!-- /brands/ pages only -->
<link rel="stylesheet" href="/sv-resources.css">       <!-- /resources/guides/ pages only -->
<link rel="stylesheet" href="/sv-forms.css">        <!-- Pages with forms only -->
<script src="/site-config.js"></script>             <!-- Dynamic values: year, licence number, contact -->
```
Load only the files relevant to the page type. Most pages only need sv-shared.css + site-config.js.

### CSS Responsibility by File
| What | Where it lives |
|---|---|
| Nav, footer, breadcrumb | `sv-shared.css` |
| Buttons, typography, colours | `sv-shared.css` |
| Hero classes, CTA section classes | `sv-shared.css` |
| Founder card, author bio strip/footer | `sv-shared.css` |
| WhatsApp float button | `sv-shared.css` |
| Systems page components (arch-grid, compare-wrap, scenario-grid etc.) | `systems.css` |
| Solutions page components (pillar-card, pricing-card, faq-grid, rel-card etc.) | `solutions.css` |
| Brand page components (hero layout, stat boxes, product cards, spec lists) | `brands.css` |
| Resource guide layout, TOC, blog-row, tables | `resources.css` |
| Form fields, checkboxes, booking slots | `sv-forms.css` |
| **Page-specific overrides** | **NONE — not permitted** |

### Inline Style Rule
```
ZERO inline <style> blocks are permitted in any HTML page.
ZERO style="" attributes are permitted except for background-image on hero sections.
If you believe a style is missing from the CSS files, add a comment <!-- NEEDS CSS: description --> and stop.
```

---

## 3. TECHNOLOGY STACK

- Plain HTML5, CSS3, vanilla JavaScript only
- No frameworks (no React, no Vue, no Bootstrap)
- No external CSS libraries
- Google Fonts via `<link>` in `<head>`
- All JS in a `<script>` block before `</body>`
- Mobile-first responsive design

---

## 4. FONTS

### Google Fonts Import (every page `<head>`)
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### Font Assignments
| Element | Font | Weight | Size (desktop) |
|---|---|---|---|
| H1 | Montserrat | 800 | clamp(36px, 5.5vw, 68px) |
| H2 | Montserrat | 700 | clamp(26px, 3.5vw, 40px) |
| H3 | Montserrat | 600 | 20px |
| H4 | Montserrat | 600 | 16px |
| Body text | Inter | 400 | 15–16px |
| Lead paragraph | Inter | 400 | 18px |
| Button labels | Montserrat | 600 | 13px uppercase |
| Eyebrow labels | Montserrat | 700 | 11–12px uppercase |
| Nav links | Inter | 500 | 14px |

---

## 5. COLOUR SYSTEM

### CSS Variables (already defined in sv-shared.css — do not redefine)
```
--primary-blue: #0056b3        /* Primary action colour */
--dark-blue:    #003d82        /* Hover / dark variant */
--text-dark:    #1B1F23
--text-gray:    #333333
--text-light:   #5F6368
--bg-light:     #F8F9FA
--white:        #ffffff
--border-light: #E8EAED
--accent-green: #25d366        /* WhatsApp */

/* Subsystem accents */
--c-surveillance: #2b6cb0
--c-people:       #319795
--c-vehicle:      #dd6b20
--c-platform:     #38a169

/* Sector accents — 8 sectors */
--c-residential:    #38B000    /* Residential — green */
--c-condos:         #4361EE    /* Condominiums — blue */
--c-commercial:     #FF6D00    /* Commercial — orange */
--c-industrial:     #7209B7    /* Industrial — purple */
--c-institutions:   #0056b3    /* Institutions — primary blue */
--c-healthcare:     #0EA5A0    /* Healthcare — teal */
--c-managed:        #C2410C    /* Managed Living — burnt orange */
--c-datacentres:    #1E3A5F    /* Data Centres — deep navy */

/* Legacy aliases — kept for backward compatibility */
--c-homes:          #38B000    /* = --c-residential */
```

### Page accent colour — set once per page via `:root` override
Each technical guide page sets its single accent in a minimal `:root` block:
```html
<style>
  :root { --primary-access: #0056b3; } /* CCTV blue — only permitted inline style block */
</style>
```
This is the ONLY permitted `<style>` block in any HTML file.

---

## 6. SPACING & LAYOUT

### Container
```css
.container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
```

### Section Padding (defined in sv-shared.css)
| Breakpoint | Section padding |
|---|---|
| Desktop 1200px+ | 80px top/bottom |
| Tablet 768px | 56px |
| Mobile 480px | 48px |

### Section Background Sequence (every multi-section page)
```
Hero:       dark gradient (#0E1A2B → #1a2942) with background image
Section 2:  white #FFFFFF
Section 3:  light #F8F9FA
Section 4:  white #FFFFFF
Section 5:  light #F8F9FA
...alternating...
Final CTA:  dark gradient with background image (cta-skyline or page-specific)
```

---

## 7. NAVIGATION — FROZEN COMPONENT

**Do not modify the nav HTML under any circumstances. Copy it verbatim from the template.**

### Canonical Nav URLs (use these exact hrefs — no variations, all absolute)
```
Logo                → /
Solutions           → /solutions/
  Residential       → /solutions/residential.html
  Condominiums      → /solutions/condominiums.html
  Commercial        → /solutions/commercial.html
  Industrial        → /solutions/industrial.html
  Institutions      → /solutions/institutions.html
  Healthcare        → /solutions/healthcare.html
  Managed Living    → /solutions/managed-living.html
  Data Centres      → /solutions/data-centres.html
  → View All        → /solutions/
Systems               → /systems/
  Premises Security   → /systems/premises-security.html
  Entry & Access      → /systems/entry-access-control.html
  Vehicle Management  → /systems/vehicle-lpr-management.html
  Communications      → /systems/ip-phone-communications.html
  Platform & Management → /systems/security-management-platform.html
Brands              → /brands/
  #surveillance     → /brands/#surveillance
  #access           → /brands/#access
  #intercom         → /brands/#intercom
  #alarms           → /brands/#alarms
  #gates            → /brands/#gates
Portfolio           → /portfolio/
  Residential       → /portfolio/?sector=residential
  Condominiums      → /portfolio/?sector=condominiums
  Commercial        → /portfolio/?sector=commercial
  Industrial        → /portfolio/?sector=industrial
  Institutions      → /portfolio/?sector=institutions
  Healthcare        → /portfolio/?sector=healthcare
  Managed Living    → /portfolio/?sector=managed-living
  Data Centres      → /portfolio/?sector=data-centres
  → View All        → /portfolio/
Resources           → /resources/
  Guides            → /resources/guides/
Insights            → /insights/
About               → /about.html
Contact             → /contact.html
```

### Logo image path (always this — absolute path, no other version)
```html
<img src="/images/securevision-logo-white.png" alt="Securevision Logo" class="nav-logo-img">
```

---

## 8. HERO SECTION

### Hero class combinations
```html
<!-- Technical guide pages -->
<header class="hero-high-impact hero-cctv">         <!-- CCTV guide -->
<header class="hero-high-impact hero-alarm">        <!-- Burglar alarm guide -->
<header class="hero-high-impact hero-access">       <!-- Door access guide -->
<header class="hero-high-impact hero-vehicle">      <!-- Auto gate guide -->

<!-- Solution pages — 8 sectors -->
<header class="hero-high-impact hero-res">          <!-- Residential -->
<header class="hero-high-impact hero-condo">        <!-- Condominiums -->
<header class="hero-high-impact hero-com">          <!-- Commercial -->
<header class="hero-high-impact hero-indus">        <!-- Industrial -->
<header class="hero-high-impact hero-gov">          <!-- Institutions -->
<header class="hero-high-impact hero-healthcare">   <!-- Healthcare -->
<header class="hero-high-impact hero-managed">      <!-- Managed Living — NEEDS CSS -->
<header class="hero-high-impact hero-dc">           <!-- Data Centres — NEEDS CSS -->

<!-- Systems pages — 5 groups -->
<header class="hero-high-impact hero-surveillance"> <!-- Premises Security -->
<header class="hero-high-impact hero-access">       <!-- Entry & Access -->
<header class="hero-high-impact hero-vehicle">      <!-- Vehicle Management -->
<header class="hero-high-impact hero-comms">        <!-- Communications — accent: #5a0892 -->
<header class="hero-high-impact hero-platform">     <!-- Platform & Management -->
```

### Hero inner structure (standard for technical guides)
```html
<header class="hero-high-impact hero-[PAGE]">
  <div class="container">
    <span class="eyebrow-light">Technical Pillar Guide</span>
    <h1 class="hero-title-main">[H1 with <span style="color:#FFD700;">keyword span</span>]</h1>
    <p class="hero-subtitle-main">[One sentence: what this guide covers]</p>
    <div class="btn-group">
      <a href="/request-site-assessment-singapore.html?intent=[page]-assessment" class="btn btn-primary">Book Site Assessment</a>
      <a href="https://wa.me/6593860466" class="btn btn-whatsapp-standard">WhatsApp an Engineer</a>
    </div>
  </div>
</header>
```

---

## 9. BUTTONS

All button classes are in `sv-shared.css`. Use only these:

| Class | Use |
|---|---|
| `.btn .btn-primary` | Primary action (blue) |
| `.btn .btn-secondary` | Secondary/outline |
| `.btn .btn-outline-light` | On dark backgrounds |
| `.btn .btn-whatsapp` | WhatsApp (green, icon) |
| `.btn .btn-whatsapp-standard` | WhatsApp with text label |
| `.btn .btn-sm` | Small variant |

Wrap multiple buttons in `<div class="btn-group">`.

---

## 10. BREADCRUMB

Required on all non-homepage pages. Use `.sv-breadcrumb`. All hrefs must be absolute:
```html
<nav class="sv-breadcrumb" aria-label="Breadcrumb">
  <div class="container">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/[parent]/">[Parent]</a></li>
      <li>[Current Page]</li>
    </ul>
  </div>
</nav>
```

---

## 11. AUTHOR BIO STRIP (technical guides and insights)

```html
<div class="author-bio-strip">
  <img src="/images/ler-wee-meng-bio.jpeg" alt="Ler Wee Meng" class="author-bio-photo">
  <div class="author-bio-text">
    <span class="author-bio-name sv-author-name">Ler Wee Meng</span>
    <span class="author-bio-credentials">Founder & CEO · Securevision · 37+ Years Experience</span>
  </div>
</div>
```

---

## 12. FOUNDER CARD (sidebar — technical guides)

```html
<div class="founder-card">
  <div class="fc-head">
    <img src="/images/ler-wee-meng-bio.jpeg" alt="Ler Wee Meng">
    <div>
      <strong>Ler Wee Meng</strong>
      <span>Founder & CEO · 37+ Years</span>
    </div>
  </div>
  <p>Need expert advice? Discuss your site requirements with our engineering team.</p>
  <a href="https://wa.me/6593860466" class="fc-wa-link">💬 WhatsApp an Engineer</a>
</div>
```

---

## 13. CTA SECTION (final section — every page)

Place OUTSIDE the `.container` / `.layout-with-sidebar` wrapper so it stretches full width.

```html
<!-- FINAL CTA — outside layout wrapper -->
<section class="cta-section cta-high-impact cta-[PAGE]" style="text-align:center; padding:120px 0;">
  <div class="container">
    <span class="eyebrow-light">Get Started</span>
    <h2 style="color:#fff; margin-bottom:20px;">[CTA Heading]</h2>
    <p class="subtitle">[One supporting sentence]</p>
    <div class="btn-group">
      <a href="/request-site-assessment-singapore.html" class="btn btn-primary">Book Free Assessment</a>
      <a href="https://wa.me/6593860466" class="btn btn-outline-light">💬 WhatsApp Us</a>
    </div>
  </div>
</section>
```

CTA background classes (from sv-shared.css):
```
cta-cctv | cta-alarm | cta-access | cta-vehicle | cta-surveillance
cta-platform | cta-comms
cta-res | cta-condo | cta-com | cta-indus | cta-gov | cta-healthcare
cta-managed | cta-dc                  ← NEEDS CSS: add to sv-shared.css
cta-skyline (generic fallback)
```

---

## 14. FOOTER — FROZEN COMPONENT

**Do not modify the footer HTML. Copy it verbatim from the template.**  
Footer uses `.site-footer` > `.footer-container` > `.footer-grid` structure as defined in `sv-shared.css`.

---

## 15. FLOATING WHATSAPP BUTTON

Place just before `</body>` on every page. Class `.sv-wa-float` is in `sv-shared.css`:
```html
<a href="https://wa.me/6593860466" class="sv-wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  <svg width="28" height="28" viewBox="0 0 24 24" fill="white">
    <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
  </svg>
</a>
```

---

## 16. JAVASCRIPT CONVENTIONS

Vanilla JS only. All scripts in one `<script>` block before `</body>`.

### Mandatory scripts (every page)
```javascript
// Dynamic year
document.querySelectorAll('.years-since').forEach(el => {
  el.textContent = new Date().getFullYear() - 2006;
});

// Mobile menu
function toggleMobileMenu() {
  document.getElementById('mobileMenu').classList.toggle('active');
}
function toggleSubmenu(id) {
  const sub = document.getElementById(id);
  const isOpen = sub.style.display === 'block';
  document.querySelectorAll('.mobile-submenu').forEach(s => s.style.display = 'none');
  if (!isOpen) sub.style.display = 'block';
}
```

### Technical guide pages also require
```javascript
// TOC scroll-spy
function toggleToc() {
  document.getElementById('tocList').classList.toggle('active');
  document.querySelector('.toc-title').classList.toggle('active');
}
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('section[id]');
  const tocLinks = document.querySelectorAll('.toc-list a');
  let current = '';
  sections.forEach(section => {
    if (window.scrollY >= section.offsetTop - 150) current = section.getAttribute('id');
  });
  tocLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === '#' + current) link.classList.add('active');
  });
});
```

---

## 17. SEO REQUIREMENTS

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[Page Title] | Securevision Singapore</title>
<meta name="description" content="[140–160 chars, unique per page]">
<link rel="canonical" href="https://www.securevision.com.sg/[new-path]">
<meta property="og:title" content="[Same as title]">
<meta property="og:description" content="[Same as meta description]">
<meta property="og:image" content="https://www.securevision.com.sg/images/og-default.jpg">
<meta property="og:url" content="https://www.securevision.com.sg/[new-path]">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Securevision">
```

Canonical and og:url must reflect the **new folder-based URL** (e.g. `/solutions/residential.html`, `/insights/maintenance-contract.html`), not the old flat-file names.

One H1 per page only. H1 → H2 → H3 hierarchy must be logical.

---

## 18. RESPONSIVE BREAKPOINTS

```css
/* Desktop default — no query */
@media (max-width: 1024px) { /* Laptop — reduce padding */ }
@media (max-width: 768px)  { /* Tablet — collapse nav, stack 2-col grids */ }
@media (max-width: 480px)  { /* Mobile — all grids 1-col, full-width buttons */ }
```

---

## 19. COMPANY CONSTANTS

Never paraphrase these. Copy exactly.

```
Company:          Securevision Pte Ltd
Established:      2006
Founder:          Ler Wee Meng
Founder quals:    BEng (NUS) · LLB (UOL)
Experience:       37+ years
Police Licence:   L/PS/000267/2023P
bizSAFE:          Level 3
BCA:              Registered Contractor
Sites protected:  2,000+
WhatsApp:         +65 9386 0466
WhatsApp URL:     https://wa.me/6593860466
Phone:            +65 6286 4796
Email:            enquiry@securevision.com.sg
Address:          Blk 1013 Geylang East Avenue 3 #02-142, Singapore 389728
Hours:            Mon–Fri 8:00am–5:00pm · Sat by appointment · Sun closed
Facebook:         https://www.facebook.com/securevision
LinkedIn:         https://www.linkedin.com/company/securevision-pte-ltd
YouTube:          http://www.youtube.com/@securevision
```

---

## 20. TEMPLATE REFERENCE TABLE

| Page Type | Template File | CSS Files | Instruction File |
|---|---|---|---|
| Homepage | (unique — index.html) | sv-shared.css | GLOBAL-INSTRUCTION.md |
| Sector solution pages | _template-sector-solution.html | sv-shared.css + solutions.css | INSTRUCTION-solution.md |
| Persona sub-pages | _template-persona-standardized.html | sv-shared.css + solutions.css | INSTRUCTION-persona.md (to create) |
| Systems hub index | (unique — /systems/index.html) | sv-shared.css + systems.css | GLOBAL-INSTRUCTION.md |
| Systems detail pages | (unique per system) | sv-shared.css + systems.css | GLOBAL-INSTRUCTION.md |
| Technical pillar guides | _template-technical-guide.html | sv-shared.css + resources.css | INSTRUCTION-technical-guide.md |
| Brand pages | _template-brand.html | sv-shared.css + brands.css | INSTRUCTION-brand.md |
| Portfolio case studies | _template-portfolio.html | sv-shared.css | INSTRUCTION-portfolio.md |
| Insights articles | _template-insights.html | sv-shared.css | INSTRUCTION-insights.md |
| Utility (contact, about) | (unique per page) | sv-shared.css + sv-forms.css | GLOBAL-INSTRUCTION.md |

### Template selection guide
```
Is this a top-level /solutions/[sector].html page?
  → _template-sector-solution.html

Is this a /solutions/[sector]/[persona].html page?
  → _template-persona-standardized.html
  → Layout A if the persona has operational problems + specific system solutions
    (office, retail, hotel, aged-care, dormitories, new-build, home-upgrade)
  → Layout B if the persona is a professional stakeholder / working relationship
    (mcst, managing-agents, security-contractors, architects)

Is this the /systems/ hub index?
  → unique page (systems/index.html) — no template, build from existing file

Is this a /systems/[page].html detail page?
  → unique page — refer to existing systems pages as reference
  → 8-section structure: Hero → Compare → Scenarios → Capabilities →
    Architecture → Integration → Deployment → CTA
  → Section 5 arch-grid always shows all 5 system groups with current page arch-active

Is this a /portfolio/[project].html case study?
  → _template-portfolio.html

Is this a /resources/guides/[guide].html technical guide?
  → _template-technical-guide.html

Is this a /brands/[brand].html brand page?
  → _template-brand.html

Is this a /insights/[slug].html article?
  → _template-insights.html
```

---

## 21. URL REFERENCE MAP (old filename → new canonical path)

| Old filename | New canonical URL |
|---|---|
| index.html | / |
| security-solutions-singapore.html | /solutions/ |
| residential-security-singapore.html | /solutions/residential.html |
| condominiums.html | /solutions/condominiums.html |
| commercial-security-singapore.html | /solutions/commercial.html |
| industrial-security-singapore.html | /solutions/industrial.html |
| government-institution-security-singapore.html | /solutions/institutions.html |
| healthcare-security-singapore.html | /solutions/healthcare.html |
| *(new)* | /solutions/managed-living.html |
| *(new)* | /solutions/data-centres.html |
| home-security-upgrade-singapore.html | /solutions/residential/home-upgrade.html |
| new-build-security-singapore.html | /solutions/residential/new-build.html |
| security-partner-architects-singapore.html | /solutions/residential/architects.html |
| condominiums-mcst.html | /solutions/condominiums/mcst.html |
| condominiums-security.html | /solutions/condominiums/security-contractors.html |
| commercial-office.html | /solutions/commercial/office.html |
| commercial-retail.html | /solutions/commercial/retail.html |
| commercial-hotel.html | /solutions/commercial/hotel.html |
| commercial-security-sta-building-singapore.html | /portfolio/sta-building-commercial.html |
| industrial-security-cyrus-tech-park-singapore.html | /portfolio/cyrus-tech-park-industrial.html |
| security-systems-singapore.html | /systems/ |
| surveillance-detection.html | /systems/premises-security.html |
| people-entry-access-control.html | /systems/entry-access-control.html |
| vehicle-entry-access-control.html | /systems/vehicle-lpr-management.html |
| integrated-security-security-management-platform.html | /systems/security-management-platform.html |
| *(new)* | /systems/ip-phone-communications.html |
| security-brands-singapore.html | /brands/ |
| [brand]-singapore.html | /brands/[brand].html |
| cctv.html | /resources/guides/cctv-guide.html |
| burglar-alarm.html | /resources/guides/burglar-alarm-guide.html |
| door-access.html | /resources/guides/door-access-guide.html |
| auto-gate-singapore.html | /resources/guides/auto-gate-guide.html |
| intercom-system-singapore.html | /resources/guides/intercom-guide.html |
| office-telephone-systems-singapore.html | /resources/guides/office-telephone-guide.html |
| resources.html | /resources/ |
| portfolio.html | /portfolio/ |
| security-articles-singapore.html | /insights/ |
| insights-[slug].html | /insights/[slug].html |

---

## 22. SECTOR TAXONOMY — 8 SECTORS

This is the canonical classification for all Solutions pages, Portfolio pages, and nav labels.
Every sector has a solution page, a nav entry, and a portfolio filter tab.
Portfolio filter tabs for Institutions and Healthcare are shown only when cases exist.

| # | Nav label | Solution file | Scope | Portfolio sub-type badges |
|---|---|---|---|---|
| 1 | Residential | /solutions/residential.html | Landed homes, bungalows, semi-D, terrace, GCB | Bungalow · Semi-detached · Terrace · GCB |
| 2 | Condominiums | /solutions/condominiums.html | Strata developments, condo estates | High-rise · Mid-rise · Landed Estate |
| 3 | Commercial | /solutions/commercial.html | Offices, hotels, retail, malls, F&B, community hubs | Office Building · Hotel · Retail · Shopping Mall · Community Hub |
| 4 | Industrial | /solutions/industrial.html | Factories, warehouses, logistics hubs, tech parks | Factory · Warehouse · Logistics Hub · Tech Park |
| 5 | Institutions | /solutions/institutions.html | Schools, childcare, churches, govt offices, army camps, bus interchanges | School · Childcare · Place of Worship · Government Office · Defence · Transport Hub |
| 6 | Healthcare | /solutions/healthcare.html | Nursing homes, senior day care, autism/CP centres, clinics | Nursing Home · Senior Day Care · Specialist Centre · Clinic |
| 7 | Managed Living | /solutions/managed-living.html | Worker dormitories, co-living apartments, student hostels | Worker Dormitory · Co-living · Student Hostel |
| 8 | Data Centres | /solutions/data-centres.html | Colocation, enterprise, hyperscale data centres | Data Centre |

### Sector colour variables (sv-shared.css) — retained for reference
These variables exist in sv-shared.css but are not applied to any page.
All pages use `--page-accent: #0056b3`. Do not use these to override page-accent.
```
--c-residential:  #38B000   Residential    (reference only)
--c-condos:       #4361EE   Condominiums   (reference only)
--c-commercial:   #FF6D00   Commercial     (reference only)
--c-industrial:   #7209B7   Industrial     (reference only)
--c-institutions: #0056b3   Institutions   (reference only)
--c-healthcare:   #0EA5A0   Healthcare     (reference only)
--c-managed:      #C2410C   Managed Living (reference only)
--c-datacentres:  #1E3A5F   Data Centres   (reference only)
```

### Sub-persona pages under each sector
```
/solutions/residential/
  new-build.html
  home-upgrade.html
  architects.html

/solutions/condominiums/
  mcst.html
  managing-agents.html
  security-contractors.html

/solutions/commercial/
  hotel.html
  office.html
  retail.html

/solutions/healthcare/
  aged-care.html
  hostels.html        ← review: confirm these are eldercare-adjacent
  dormitories.html    ← MOVE to /solutions/managed-living/ subfolder

/solutions/managed-living/
  dormitories.html    ← migrated from /solutions/healthcare/
  co-living.html      ← to create

/solutions/institutions/
  (to create — school, govt-office, defence sub-personas)

/solutions/data-centres/
  (thin page only for now — no sub-personas yet)
```

### Portfolio orphans — migrate when building those case studies
```
commercial-security-sta-building-singapore.html  → /portfolio/sta-building-commercial.html    (sector: Commercial)
industrial-security-cyrus-tech-park-singapore.html → /portfolio/cyrus-tech-park-industrial.html  (sector: Industrial)
```

---

## 23. SYSTEMS TAXONOMY — 5 GROUPS

This is the canonical classification for all Systems pages, the systems hub index, and nav labels.
Every group has a detail page. The hub index at /systems/ presents all five.

| # | Nav label | System file | Page accent | What it covers |
|---|---|---|---|---|
| 1 | Premises Security | /systems/premises-security.html | #0056b3 | CCTV, AI analytics, burglar alarm, sensors, intrusion detection |
| 2 | Entry & Access | /systems/entry-access-control.html | #0056b3 | Door access, biometrics, intercom, visitor management |
| 3 | Vehicle Management | /systems/vehicle-lpr-management.html | #0056b3 | Auto-gates, barriers, LPR, car park management, UHF tags |
| 4 | Communications | /systems/ip-phone-communications.html | #5a0892 | IP phones, IPPBX (Yeastar), handsets (Fanvil, Yealink) |
| 5 | Platform & Management | /systems/security-management-platform.html | #0056b3 | VESTA (condos), Milestone/HikCentral (complex sites), ZKTeco CVSecurity (offices) |

### Systems page structure (8 sections — consistent across all 5 pages)
```
Section 1: Hero
Section 2: Compare — before/after (sv-section-grey)
Section 3: Scenarios — 4 real-life use cases (sv-section-white)
Section 4: Capabilities — grid-3 or capabilities-grid (sv-section-grey) [id="capabilities"]
Section 5: Architecture — arch-grid showing all 5 system groups, current page arch-active (sv-section-white)
Section 6: Integration — integration-panel with image (sv-section-grey)
Section 7: Deployment — arch-grid or arch-grid-3 (sv-section-white)
Section 8: CTA — cta-section cta-high-impact cta-[page]
```

### Architecture pillar icons (canonical — use these SVGs consistently across all systems pages)
```
Premises Security:  camera SVG — path d="M15 10l4.553-2.069..."
Entry & Access:     padlock SVG — rect x="3" y="11" + path d="M7 11V7a5 5..."
Vehicle Management: car SVG — rect x="1" y="3" width="15" + path d="M16 8h4l3 5v3h-7V8z"
Communications:     phone SVG — path d="M22 16.92v3..."
Platform:           dashboard grid SVG — rect x="3" y="3" width="18" + path d="M3 9h18M9 21V9"
```

### Infrastructure positioning
Network switches (Omada, Ruijie) and structured cabling are NOT a systems category.
Position as a delivery capability statement on the systems hub index (Section 3 integration panel)
and on the Communications page (Section 4 network card). Never create a standalone systems page
for networking — it belongs in the capability narrative, not the navigation.

---

*Securevision Global Design Instruction v3.3 — May 2026*
*Changes from v3.2: Section 2 CSS stack updated — sv-guides.css retired, systems.css/solutions.css/brands.css/resources.css added. Template table updated with correct CSS file per page type.*
*Changes from v3.1: Section 7 Systems nav updated to 5-group client-centric taxonomy (Premises Security, Entry & Access, Vehicle Management, Communications, Platform & Management). Section 8 systems hero classes added. Section 13 cta-comms added. Section 20 template table updated — _template-subsystem.html removed (retired), systems pages are now unique builds. Template selection guide updated with systems page routing. Section 21 URL map: /systems/ip-phone-communications.html added. Section 23 added — Systems Taxonomy with 5-group reference table, page structure spec, canonical arch icons, and infrastructure positioning rule.*
*Do not modify without updating version number and date*

### To build a NEW page:
```
1. Copy the correct template from /_templates/
2. Paste GLOBAL-INSTRUCTION.md into the Anti-Gravity prompt
3. Paste the relevant INSTRUCTION-[type].md below it
4. Add the page-specific brief at the bottom:

--- PAGE BRIEF ---
Template:  _templates/_template-technical-guide.html
File:      /resources/guides/intercom-guide.html
Page name: Intercom Systems Guide
Accent:    #319795 (teal — people access)
Hero:      hero-intercom
CTA:       cta-access

[Content brief here]
```

### To UPDATE an existing page:
```
1. Paste GLOBAL-INSTRUCTION.md
2. State EXACTLY what section to change
3. State what must NOT be touched
4. Anti-Gravity updates only the specified section

--- UPDATE BRIEF ---
File:    /resources/guides/cctv-guide.html
Change:  Section 4 — update the resolution comparison table (new data below)
DO NOT TOUCH: nav, footer, hero, author bio strip, sidebar, CTA section, any other section
```

---

*Securevision Global Design Instruction v3.3 — May 2026*
*Changes from v3.1 documented in Section 23 above.*
*Do not modify without updating version number and date*
