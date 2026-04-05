# SECUREVISION WEBSITE — GLOBAL DESIGN INSTRUCTION
## For use with Anti-Gravity AI Web Builder
## Version 2.0 — April 2026
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

### The CSS Stack (in load order — every page must load all three)
```html
<link rel="stylesheet" href="sv-shared.css">       <!-- Global: nav, footer, buttons, typography, hero, CTA -->
<link rel="stylesheet" href="sv-guides.css">        <!-- Technical guide pages only -->
<link rel="stylesheet" href="sv-forms.css">         <!-- Pages with forms only -->
<script src="site-config.js"></script>              <!-- Dynamic values: year, licence number, contact -->
```

### CSS Responsibility by File
| What | Where it lives |
|---|---|
| Nav, footer, breadcrumb | `sv-shared.css` |
| Buttons, typography, colours | `sv-shared.css` |
| Hero classes, CTA section classes | `sv-shared.css` |
| Founder card, author bio strip/footer | `sv-shared.css` |
| WhatsApp float button | `sv-shared.css` |
| Technical guide layout, TOC, blog-row, tables | `sv-guides.css` |
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

/* Sector accents */
--c-homes:        #38B000
--c-condos:       #4361EE
--c-commercial:   #FF6D00
--c-industrial:   #7209B7
--c-institutions: #0056b3
--c-healthcare:   #0056b3
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

### Canonical Nav URLs (use these exact hrefs — no variations)
```
Logo              → index.html
Solutions         → security-solutions-singapore.html
  Private Homes   → residential-security-singapore.html
  Condominiums    → condominiums.html
  Commercial      → commercial-security-singapore.html
  Industrial      → industrial-security-singapore.html
  Institutions    → government-institution-security-singapore.html
  Healthcare      → healthcare-security-singapore.html
Systems           → security-systems-singapore.html
  Surveillance    → surveillance-detection.html
  People Access   → people-access-control.html
  Vehicle Access  → vehicle-access-control.html
  Platform        → integrated-security-platform.html
Brands            → security-brands-singapore.html
Portfolio         → portfolio.html
Resources         → resources.html
Insights          → security-articles-singapore.html
About             → about.html
Contact           → contact.html
```

### Logo image path (always this — no other version)
```html
<img src="images/securevision-logo-white.png" alt="Securevision Logo" class="nav-logo-img">
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

<!-- Solution pages -->
<header class="hero-high-impact hero-res">          <!-- Residential -->
<header class="hero-high-impact hero-condo">        <!-- Condominiums -->
<header class="hero-high-impact hero-com">          <!-- Commercial -->
<header class="hero-high-impact hero-indus">        <!-- Industrial -->
<header class="hero-high-impact hero-gov">          <!-- Institutions -->
<header class="hero-high-impact hero-healthcare">   <!-- Healthcare -->
```

### Hero inner structure (standard for technical guides)
```html
<header class="hero-high-impact hero-[PAGE]">
  <div class="container">
    <span class="eyebrow-light">Technical Pillar Guide</span>
    <h1 class="hero-title-main">[H1 with <span style="color:#FFD700;">keyword span</span>]</h1>
    <p class="hero-subtitle-main">[One sentence: what this guide covers]</p>
    <div class="btn-group">
      <a href="request-site-assessment-singapore.html?intent=[page]-assessment" class="btn btn-primary">Book Site Assessment</a>
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

Required on all non-homepage pages. Use `.sv-breadcrumb`:
```html
<nav class="sv-breadcrumb" aria-label="Breadcrumb">
  <div class="container">
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="[parent].html">[Parent]</a></li>
      <li>[Current Page]</li>
    </ul>
  </div>
</nav>
```

---

## 11. AUTHOR BIO STRIP (technical guides and insights)

```html
<div class="author-bio-strip">
  <img src="images/ler-wee-meng-bio.jpeg" alt="Ler Wee Meng" class="author-bio-photo">
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
    <img src="images/ler-wee-meng-bio.jpeg" alt="Ler Wee Meng">
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
      <a href="request-site-assessment-singapore.html" class="btn btn-primary">Book Free Assessment</a>
      <a href="https://wa.me/6593860466" class="btn btn-outline-light">💬 WhatsApp Us</a>
    </div>
  </div>
</section>
```

CTA background classes (from sv-shared.css):
```
cta-cctv | cta-alarm | cta-access | cta-vehicle | cta-surveillance
cta-platform | cta-res | cta-condo | cta-com | cta-indus | cta-gov | cta-healthcare
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
<link rel="canonical" href="https://www.securevision.com.sg/[slug].html">
<meta property="og:title" content="[Same as title]">
<meta property="og:description" content="[Same as meta description]">
<meta property="og:image" content="https://www.securevision.com.sg/images/og-default.jpg">
<meta property="og:url" content="https://www.securevision.com.sg/[slug].html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Securevision">
```

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
| Solution pages | _template-solution.html | sv-shared.css | INSTRUCTION-solution.md |
| Systems hub/subsystem | _template-subsystem.html | sv-shared.css | INSTRUCTION-subsystem.md |
| Technical pillar guides | _template-technical-guide.html | sv-shared.css + sv-guides.css | INSTRUCTION-technical-guide.md |
| Brand pages | _template-brand.html | sv-shared.css | INSTRUCTION-brand.md |
| Portfolio case studies | _template-portfolio.html | sv-shared.css | INSTRUCTION-portfolio.md |
| Insights articles | _template-insights.html | sv-shared.css | INSTRUCTION-insights.md |
| Utility (contact, about) | (unique per page) | sv-shared.css + sv-forms.css | GLOBAL-INSTRUCTION.md |

---

## HOW TO USE THIS SYSTEM

### To build a NEW page:
```
1. Copy the correct template from /_templates/
2. Paste GLOBAL-INSTRUCTION.md into the Anti-Gravity prompt
3. Paste the relevant INSTRUCTION-[type].md below it
4. Add the page-specific brief at the bottom:

--- PAGE BRIEF ---
Template:  _templates/_template-technical-guide.html
File:      intercom-system-singapore.html
Page name: AV Intercom Systems Guide
Accent:    #319795 (teal — people access)
Hero:      hero-intercom (image to be added to sv-shared.css)
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
File:    cctv.html
Change:  Section 4 — update the resolution comparison table (new data below)
DO NOT TOUCH: nav, footer, hero, author bio strip, sidebar, CTA section, any other section
```

---

*Securevision Global Design Instruction v2.0 — April 2026*  
*Do not modify without updating version number and date*
