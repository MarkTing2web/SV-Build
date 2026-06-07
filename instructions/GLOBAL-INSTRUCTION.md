# SECUREVISION WEBSITE — GLOBAL DESIGN INSTRUCTION
## For use with Anti-Gravity AI Web Builder
## Version 3.5 — June 2026
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
<link rel="stylesheet" href="/sv-shared.css">       <!-- Always required -->
<link rel="stylesheet" href="/sv-solutions.css">     <!-- /solutions/ pages only -->
<link rel="stylesheet" href="/sv-systems.css">       <!-- /systems/ pages only -->
<link rel="stylesheet" href="/sv-brands.css">        <!-- /brands/ pages only -->
<link rel="stylesheet" href="/sv-portfolio.css">     <!-- /portfolio/ pages only -->
<link rel="stylesheet" href="/sv-insights.css">      <!-- /insights/ pages only -->
<link rel="stylesheet" href="/sv-resources.css">     <!-- /resources/ pages only -->
<link rel="stylesheet" href="/sv-forms.css">         <!-- Pages with forms only -->
<script src="/site-config.js"></script>              <!-- Always required — dynamic values -->
```
Load only the files relevant to the page type. Every page loads sv-shared.css and site-config.js. Load only the section-specific CSS file that matches the page's folder.

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
ZERO style="" attributes are permitted in <body> with one exception:
  stat-bar-fill elements may use style="width:X%" — these are data-driven bar widths.

Background-image on hero sections goes in the <style> block in <head> — NOT as a style= attribute
on the <header> element itself.

The only permitted <style> block per page contains exactly 3 rules:
  :root { --page-accent: #0056b3; }
  .hero-[slug] { background-image: url('...desktop.webp'); }
  @media (max-width: 768px) { .hero-[slug] { background-image: url('...-mobile.webp'); } }

If a visual effect is needed that has no existing class, add <!-- NEEDS CSS: description --> and stop.
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

### Page accent colour — always #0056b3 sitewide
Every page uses the same accent colour. Do not change this per sector or per page type.
```html
<style>
  :root { --page-accent: #0056b3; }
  .hero-[slug] { background-image: url('/images/[path]/[slug].webp'); }
  @media (max-width: 768px) { .hero-[slug] { background-image: url('/images/[path]/[slug]-mobile.webp'); } }
</style>
```
The sector colour variables (--c-residential, --c-condos etc.) exist in sv-shared.css for reference
and potential future use. They are NOT applied as --page-accent on any current page.

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
Hero:        dark overlay via CSS ::before — no inline gradient in HTML
Trust bar:   white — immediately after hero
Breadcrumb:  white — immediately after trust bar
Section 1:   sv-section-grey (#EEF2F7) — first content section is ALWAYS grey
Section 2:   sv-section-white (#FAFBFC)
Section 3:   sv-section-grey (#EEF2F7)
Section 4:   sv-section-white (#FAFBFC)
...strictly alternating grey/white — never two consecutive same...
Final CTA:   cta-section cta-high-impact — outside <main>, not part of alternation
```
Use class names sv-section-grey and sv-section-white — never inline background styles.
Never use inline padding, inline background, or inline colour on section elements.

**The alternation rule is strict:**
- First content section after breadcrumb is always sv-section-grey
- Every subsequent section alternates: grey → white → grey → white
- Never two consecutive sections with the same background
- The final CTA section (cta-section cta-high-impact) is outside `<main>` and is not counted in the alternation

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
  Calculators       → /resources/calculators/
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

### Hero height classes — combine with hero-high-impact and page-specific class
```
hero-full      85vh desktop / 480px mobile — homepage only
hero-standard  65vh desktop / 380px mobile — sector hubs, systems pages, deep-dives, problem pages
hero-compact   44vh desktop / 280px mobile — persona sub-pages, portfolio, insights, resources
```

### Hero class combination — 3 classes always required
```html
<header class="hero-high-impact hero-standard hero-[slug]">
```
- `hero-high-impact` — always present, enables overlay and text layout
- `hero-standard` or `hero-compact` — sets viewport height (see table above)
- `hero-[slug]` — page-specific class that matches the slug in the `<style>` block

### Background image — in style block only, never inline on element
```html
<!-- In <head> style block — correct -->
<style>
  :root { --page-accent: #0056b3; }
  .hero-residential { background-image: url('/images/solutions/hero-solutions/residential.webp'); }
  @media (max-width: 768px) { .hero-residential { background-image: url('/images/solutions/hero-solutions/residential-mobile.webp'); } }
</style>

<!-- On the element — WRONG, never do this -->
<header class="hero-high-impact hero-standard hero-residential" style="background-image: url(...)">
```

### Hero inner structure (standard for technical guides)
```html
<header class="hero-high-impact hero-[PAGE]"
        style="background-image: url('/images/resources/guides/[topic]/hero-[page].webp');">
  <div class="container">
    <span class="eyebrow-light">Technical Pillar Guide</span>
    <h1 class="hero-title-main">[H1 text]</h1>
    <p class="hero-subtitle-main">[One sentence: what this guide covers]</p>
    <div class="rg-hero-author">
      <img src="/images/ler-wee-meng-bio.webp" alt="Ler Wee Meng" class="rg-hero-author-photo">
      <div>
        <span class="rg-hero-author-name sv-author-name">Ler Wee Meng</span>
        <span class="rg-hero-author-credentials">Founder & CEO, Securevision · <span class="sv-years-experience"></span>+ Years Experience</span>
      </div>
    </div>
  </div>
</header>
```

Note: Technical guide heroes do NOT include a btn-group. The author block replaces it.
The single final CTA section (Section 13) handles conversion — no hero CTA duplication.

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


---

## 11. TRUST BAR

Required on every page except the homepage. Place immediately after the closing `</header>` tag, before the breadcrumb.

```html
<div class="trust-bar">
  <div class="container">
    <div class="trust-bar-inner">
      <span>Police Licensed</span>
      <span class="trust-divider">|</span>
      <span class="sv-bizsafe"></span>
      <span class="trust-divider">|</span>
      <span><strong class="sv-sites"></strong> Sites Protected</span>
    </div>
  </div>
</div>
```

**Rules:**
- Outer class: `trust-bar` — not `sv-trust-bar`
- Inner class: `trust-bar-inner` — not `trust-flex-inline`
- Divider class: `trust-divider` — not `divider`, not `sep`
- Exactly 3 items: Police Licensed · bizSAFE Level 3 · Sites Protected
- **BCA Registered is never in the trust bar** — it belongs in the footer
- `sv-bizsafe` is a dynamic class populated by `nav-footer.js` — never write "bizSAFE Level 3" as plain text
- `sv-sites` must be inside `<strong>` — never a bare span and never a hardcoded number
- Zero inline `style=` on any element inside the trust bar

## 12. AUTHOR BIO STRIP (technical guides and insights)

```html
<div class="author-bio-strip">
  <img src="/images/ler-wee-meng-bio.webp" alt="Ler Wee Meng" class="author-bio-photo">
  <div class="author-bio-text">
    <span class="author-bio-name sv-author-name">Ler Wee Meng</span>
    <span class="author-bio-credentials">Founder & CEO · Securevision · 37+ Years Experience</span>
  </div>
</div>
```

---

## 13. FOUNDER CARD (sidebar — technical guides)

```html
<div class="founder-card">
  <div class="fc-head">
    <img src="/images/ler-wee-meng-bio.webp" alt="Ler Wee Meng">
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

## 14. CTA SECTION (final section — every page)

Place OUTSIDE the `.container` / `.rg-layout` wrapper so it stretches full width.
Do NOT add inline `style=""` attributes — padding and alignment are handled by `.cta-high-impact`.

### Canonical CTA button labels — 3 labels, used by destination

| Visible label | Button class | Destination | Used when |
|---|---|---|---|
| `Book a Site Assessment` | `btn btn-primary` | `/contact-gateway.html?intent=[page]-assessment` | Primary CTA — all guide and solution pages |
| `Request a Proposal` | `btn btn-primary` | `/contact-gateway.html?intent=proposal-request` | Primary CTA — evaluator/contractor pages |
| `💬 WhatsApp` | `btn btn-outline-light` | `https://wa.me/6593860466` | Secondary CTA — paired with primary on all pages |

**Retired labels — do not use on any button:**
- `Book Free Assessment` → use `Book a Site Assessment`
- `Book Site Assessment` → use `Book a Site Assessment` (missing "a")
- `WhatsApp Us` → use `💬 WhatsApp`
- `WhatsApp an Engineer` → **retained only** in `fc-wa-link` inside the sidebar founder card, and in `aria-label`/`title` attributes of the floating button. Nowhere else.

### CTA destination URLs
```
Primary assessment CTA:  /request-site-assessment-singapore.html?intent=[slug]-cta
Proposal CTA:            /request-site-assessment-singapore.html?intent=[slug]-proposal
```
Note: the old /contact-gateway.html destination is deprecated. Use /request-site-assessment-singapore.html.

### Standard final CTA — hub, systems, deep-dive, problem pages
```html
<section class="cta-section cta-high-impact">
  <div class="container">
    <h2>[CTA Heading]</h2>
    <p class="subtitle">[One supporting sentence]</p>
    <div class="btn-group">
      <a href="/request-site-assessment-singapore.html?intent=[slug]-cta" class="btn btn-primary">Book a Site Assessment</a>
    </div>
    <p class="cta-trust-note">Serving Singapore Since 2006</p>
  </div>
</section>
```

### Alternate final CTA — proposal intent (persona sub-pages, brands, portfolio, insights)
```html
<section class="cta-section cta-high-impact">
  <div class="container">
    <h2>[CTA Heading]</h2>
    <p class="subtitle">[One supporting sentence]</p>
    <div class="btn-group">
      <a href="/request-site-assessment-singapore.html?intent=[slug]-proposal" class="btn btn-primary">Request a Proposal</a>
    </div>
    <p class="cta-trust-note">Serving Singapore Since 2006</p>
  </div>
</section>
```
A second WhatsApp button inside the CTA btn-group is optional. Use it on guides and insights where
a conversational entry is natural. Omit it on solution and brand pages where the primary CTA is sufficient.
The page-type class (cta-property, cta-facilities etc.) is optional — omit if no matching background exists.

### CTA background classes (from sv-shared.css)
```
cta-property    ← Asset protection / property managers (guides, most solution pages)
cta-facilities  ← Operations / facilities / engineering
cta-compliance  ← Compliance / risk / governance
cta-care        ← Healthcare / senior care / social
cta-skyline     ← Generic fallback
```

Legacy per-page CTA classes (`cta-cctv`, `cta-alarm`, `cta-res`, etc.) are deprecated.
Use the persona-group classes above for all new and updated pages.

---

## 15. FOOTER — INJECTED COMPONENT

The footer is injected at runtime by `nav-footer.js`. Do not write any footer HTML.
The only permitted footer HTML on any page is the placeholder:
```html
<footer id="sv-footer"></footer>
```
`nav-footer.js` populates this at runtime with the full footer, JSON-LD LocalBusiness schema,
and all dynamic values. Never hardcode footer content, address, phone, or links.

---

## 16. FLOATING WHATSAPP BUTTON — INJECTED, NEVER HARDCODE

The WhatsApp floating button is injected at runtime by `nav-footer.js`.
**Never write `sv-wa-float` HTML in any page.** Never add a standalone WhatsApp anchor before `</body>`.

If you see `sv-wa-float` HTML in an existing page, remove it — it is a legacy artefact.
The button will still appear at runtime via `nav-footer.js`.

---

## 17. JAVASCRIPT CONVENTIONS

Vanilla JS only. No frameworks (no jQuery, no React, no Alpine).

### Mandatory scripts — loaded via external files, not inline
```html
<!-- Always load these two, in this order, last before </body> -->
<script src="/site-config.js"></script>    <!-- Dynamic values: year, licence, site count -->
<script src="/nav-footer.js"></script>     <!-- Nav, footer, WhatsApp float, JSON-LD schema -->

<!-- Load these only when the page uses the corresponding injection block -->
<script src="/systems-block.js"></script>    <!-- When sv-systems-block placeholder is present -->
<script src="/solutions-block.js"></script>  <!-- When sv-solutions-block placeholder is present -->
<script src="/portfolio-block.js"></script>  <!-- When sv-portfolio-block placeholder is present -->
```

**Do not write inline JS for:** nav toggle, mobile menu, dynamic year, dynamic site count,
dynamic licence number, WhatsApp float, JSON-LD schema. All of these are handled by the
external files above.

### Page-specific JS
If a page needs custom JS (e.g. a calculator, a filter, a toggle), write it in a dedicated
external file `/[section]/[page].js` and load it before `nav-footer.js`. Do not add inline
`<script>` blocks to HTML pages for general functionality.

---

## 18. SEO REQUIREMENTS

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[Topic] Singapore | Securevision</title>
<meta name="description" content="[120–160 chars, benefit-led, must include Singapore]">
<link rel="canonical" href="https://www.securevision.com.sg/[path]">
<meta property="og:title" content="[Same as title — copy exactly]">
<meta property="og:description" content="[Same as meta description — copy exactly]">
<meta property="og:image" content="https://www.securevision.com.sg/images/[section]/hero-[section]/[slug].webp">
<meta property="og:url" content="https://www.securevision.com.sg/[path]">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Securevision">
```

**Title format:** `[Topic] Singapore | Securevision` — Singapore comes before the pipe, not after.
**Title length:** 50–60 characters.
**Description length:** 120–160 characters.
**og:image:** Must be the actual hero image for this page — never `og-default.jpg`.
**og:title / og:description:** Must match title and description exactly — no variations.
**Canonical and og:url:** Must be the live absolute URL. Use new canonical paths, not old flat filenames.

One H1 per page only. H1 → H2 → H3 hierarchy must be logical. Never skip a heading level.

---

## 19. RESPONSIVE BREAKPOINTS

```css
/* Desktop default — no query */
@media (max-width: 1024px) { /* Laptop — reduce padding */ }
@media (max-width: 768px)  { /* Tablet — collapse nav, stack 2-col grids */ }
@media (max-width: 480px)  { /* Mobile — all grids 1-col, full-width buttons */ }
```

---

## 20. COMPANY CONSTANTS

Reference table for schema, meta, and non-HTML contexts. Never paraphrase these.

```
Company:          Securevision Pte Ltd
Established:      2006
Founder:          Ler Wee Meng
Founder quals:    BEng (NUS) · LLB (UOL)
Experience:       37+ years
Police Licence:   L/PS/001568/2026P
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

**In HTML body content, always use dynamic classes — never hardcode these values:**

| Value | Dynamic class | Usage |
|---|---|---|
| Police licence number | `sv-licence` | `<span class="sv-licence"></span>` |
| bizSAFE level | `sv-bizsafe` | `<span class="sv-bizsafe"></span>` |
| Sites protected count | `sv-sites` | `<strong class="sv-sites"></strong> Sites Protected` |
| Years in business | `sv-years-business` | `<span class="sv-years-business"></span> years` |
| Years experience (founder) | `sv-years-experience` | `<span class="sv-years-experience"></span>+ Years Experience` |
| Current year | `sv-current-year` | `<span class="sv-current-year"></span>` |

All of these are populated at runtime by `site-config.js` and `nav-footer.js`.
The constants table above is for reference only — do not copy these values directly into HTML body content.
"Since 2006" and "$2,000 to $6,000" (price ranges) and "2,000 residents" (capacity) as static text are acceptable.

---

## 21. TEMPLATE REFERENCE TABLE

| Page Type | Template File | CSS Files | Instruction File |
|---|---|---|---|
| Homepage | (unique — index.html) | sv-shared.css | GLOBAL-INSTRUCTION.md |
| Sector solution pages | _template-solution-standard.html | sv-shared.css + sv-solutions.css | INSTRUCTION-solution.md |
| Persona sub-pages | _template-solution-standard.html (hero-compact) | sv-shared.css + sv-solutions.css | INSTRUCTION-solution.md |
| Systems hub index | (unique — /systems/index.html) | sv-shared.css + systems.css | GLOBAL-INSTRUCTION.md |
| Systems detail pages | (unique per system) | sv-shared.css + systems.css | GLOBAL-INSTRUCTION.md |
| Technical pillar guides | _template-technical-guide.html | sv-shared.css + resources.css | INSTRUCTION-technical-guide.md |
| Brand pages | _template-brand.html | sv-shared.css + brands.css | INSTRUCTION-brand.md |
| Portfolio case studies | _template-portfolio.html | sv-shared.css + sv-portfolio.css | INSTRUCTION-portfolio.md |
| Insights articles | _template-insights.html | sv-shared.css + sv-insights.css | INSTRUCTION-insights.md |
| Utility (contact, about) | (unique per page) | sv-shared.css + sv-forms.css | GLOBAL-INSTRUCTION.md |
| Calculator / tool pages | (unique per tool) | sv-shared.css + sv-resources.css | GLOBAL-INSTRUCTION.md |

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

Is this a /resources/calculators/[tool].html calculator page?
  → unique page — no template; build against GLOBAL-INSTRUCTION.md
  → CSS: sv-shared.css + sv-resources.css (Section H and beyond for .calc- classes)
  → JS: external file at /resources/calculators/[tool].js
  → Hero: hero-high-impact hero-guide hero-compact (inline background-image optional;
    omit for a clean dark-navy header, or reuse a relevant existing hero image)
  → Page accent: #0056b3 (default; adjust only if tool belongs to a non-blue system)
  → Section structure: Hero → Calculator section (sv-section-white) → CTA
  → CTA: cta-section cta-high-impact cta-facilities (operations/sizing buyer persona)
```

---

## 22. URL REFERENCE MAP (old filename → new canonical path)

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
| *(new)* | /resources/calculators/ |
| *(new)* | /resources/calculators/cctv-storage-bandwidth-calculator.html |

---

## 23. SECTOR TAXONOMY — 8 SECTORS

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
  architects-and-designers.html

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
  day-care.html

/solutions/managed-living/
  dormitories.html
  hostels.html
  co-living.html

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

## 24. SYSTEMS TAXONOMY — 6 GROUPS

This is the canonical classification for all Systems pages, the systems hub index, and nav labels.
Every group has a detail page. The hub index at /systems/ presents all five.

| # | Nav label | System file | Page accent | What it covers |
|---|---|---|---|---|
| 1 | Premises Security | /systems/premises-security.html | #0056b3 | CCTV, AI analytics, burglar alarm, sensors, intrusion detection |
| 2 | Entry & Access Control | /systems/entry-access-control.html | #0056b3 | Door access, biometrics, intercom, visitor management |
| 3 | Vehicle & LPR Management | /systems/vehicle-lpr-management.html | #0056b3 | Auto-gates, barriers, LPR, car park management, UHF tags |
| 4 | IP Phone Communications | /systems/ip-phone-communications.html | #0056b3 | IP phones, IPPBX (Yeastar), handsets (Fanvil, Yealink) |
| 5 | Network Infrastructure | /systems/network-infrastructure.html | #0056b3 | Managed switches, structured cabling, WiFi access points |
| 6 | Security Management Platform | /systems/security-management-platform.html | #0056b3 | VESTA (condos), Milestone/HikCentral (complex sites), ZKTeco CVSecurity (offices) |

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

*Securevision Global Design Instruction v3.6 — June 2026*
*Changes from v3.5: Section 2 CSS stack updated — sv-portfolio.css and sv-insights.css added. Section 2 inline style rule clarified — background-image in style block only, stat-bar-fill the only permitted inline. Section 5 page-accent rule updated — always #0056b3 sitewide. Section 6 section alternation updated — sv-section-grey/white class names, EEF2F7/FAFBFC colours, alternation rule explicit. Section 8 hero updated — height class table added (hero-full/standard/compact), background-image moved from inline to style block. Section 11 Trust Bar added as new dedicated section. Section 11a Dynamic Values added. Sections renumbered accordingly. Section 14 Footer updated — injected by nav-footer.js, placeholder only. Section 15 WhatsApp Float updated — injected, never hardcode. Section 16 JS updated — nav-footer.js and site-config.js replace all inline JS. Section 17 SEO updated — title format corrected, og:image must be actual hero path. Section 20 Company Constants updated — dynamic class table added. Section 21 Template table updated — correct filenames, sv-portfolio.css and sv-insights.css added. Section 23 Sector Taxonomy updated — architects-and-designers.html path corrected, managed-living sub-pages corrected. Section 24 Systems Taxonomy updated — Network Infrastructure added as group 5, Platform moved to group 6, count corrected to 6.*
*Changes from v3.4: Section 7 nav updated — Calculators sub-item added under Resources. Section 20 template table updated — Calculator/tool page type added. Section 20 template selection guide updated — calculator page routing added. Section 21 URL map updated — /resources/calculators/ and /resources/calculators/cctv-storage-bandwidth-calculator.html added.*
*Changes from v3.3: Section 5 page-accent example corrected (--primary-access → --page-accent). Section 8 hero structure updated — guide heroes use rg-hero-author block, no btn-group. Section 13 overhauled — canonical CTA label table added (3 labels: Book a Site Assessment / Request a Proposal / 💬 WhatsApp), illegal inline styles removed from template, CTA background classes updated to persona-group system (cta-property / cta-facilities / cta-compliance / cta-care), legacy per-page classes deprecated. Section 13 now includes both standard and proposal-intent CTA variants. Section 19 licence number updated to L/PS/001568/2026P.*
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

*Securevision Global Design Instruction v3.6 — June 2026*
*Changes from v3.5 documented above.*
*Do not modify without updating version number and date*
