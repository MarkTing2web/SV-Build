# SECUREVISION — TECHNICAL PILLAR GUIDE INSTRUCTION
## Page Type: Technical Guide (sv-guides)
## Applies to: cctv.html · burglar-alarm.html · door-access.html · auto-gate-singapore.html · intercom-system-singapore.html · and future pillar guides
## Version 2.0 — April 2026
## This file lives at: /_instructions/INSTRUCTION-technical-guide.md
## Changelog: v2.0 — Added Mode A / Mode B content framework. Migration rules strengthened.

---

## ⚠️ RULES SPECIFIC TO THIS PAGE TYPE

1. **No inline `<style>` blocks** except the single permitted `:root { --primary-access: #hex; }` accent override.
2. **All layout, typography, and component classes** come from `sv-guides.css` or `sv-shared.css`. Do not invent new class names.
3. **Do not number the final CTA section.** It is never listed in the TOC.
4. **Sidebar must include** both the TOC and the founder card — no exceptions.
5. **Section IDs must match TOC hrefs exactly** — e.g. `<section id="what-is-cctv">` links to `<a href="#what-is-cctv">`.
6. **The layout wrapper closes before the final CTA.** CTA is full-width outside the sidebar layout.
7. **Migration = restructure only. Never rewrite.** See Section 8B and Section 12 for full rules.

---

## 1. PAGE STRUCTURE

Every technical guide uses the same architectural wrapper — this is fixed and must not change:

```
[Head + CSS]
[Nav — frozen]
[Hero — hero-high-impact + page class]
[Author bio strip]
[Breadcrumb — sv-breadcrumb]
[Layout wrapper — layout-with-sidebar]
  [main — content column]
    [Content — Mode A or Mode B — see Section 8]
  [aside — sidebar column]
    Sticky TOC
    Founder card
[/Layout wrapper]
[Final CTA — full width, outside layout]
[Footer — frozen]
[WhatsApp float]
[Scripts]
```

### Content Mode Selection

The content inside `<main>` follows one of two modes depending on the page:

**MODE A — Framework Guide**
For new pages or short-form guides. Uses the strict 5-part structure defined in Section 8A.
TOC shows 5 entries. Section IDs use `section1` through `section5`.

**MODE B — Deep Technical Reference**
For existing content-rich pages with many sections. The 5-part framework becomes
grouping logic only — each part may contain multiple subsections with their own
section IDs and TOC entries. Section IDs use descriptive slugs matching the content
(e.g. `#what-is-cctv`, `#resolution-image-quality`).

| Page | Mode |
|---|---|
| cctv.html | Mode B |
| burglar-alarm.html | Mode B |
| door-access.html | Mode B |
| auto-gate-singapore.html | Mode B |
| intercom-system-singapore.html | Mode A (new build) |
| Future new pages | Mode A unless brief specifies otherwise |

In both modes: the wrapper, nav, footer, hero, author bio, breadcrumb, sidebar, and CTA
structure are identical and frozen.

---

## 2. HEAD TEMPLATE

```html
<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Page Title] | Securevision Singapore</title>
  <meta name="description" content="[140–160 chars]">
  <link rel="canonical" href="https://www.securevision.com.sg/[slug].html">
  <meta property="og:title" content="[Title]">
  <meta property="og:description" content="[Description]">
  <meta property="og:image" content="https://www.securevision.com.sg/images/og-default.jpg">
  <meta property="og:url" content="https://www.securevision.com.sg/[slug].html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Securevision">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="sv-shared.css">
  <script src="site-config.js"></script>
  <link rel="stylesheet" href="sv-guides.css">

  <!-- ONLY permitted inline style — page accent colour -->
  <style>
    :root { --primary-access: #0056b3; } /* Change hex per page — see accent table below */
  </style>
</head>
```

### Accent Colour Table
| Page | Accent Hex | CSS variable value |
|---|---|---|
| CCTV | `#0056b3` | Primary blue |
| Burglar Alarm | `#dc2626` | Alert red |
| Door Access | `#319795` | Teal (people) |
| Auto Gate | `#dd6b20` | Orange (vehicle) |
| Intercom | `#319795` | Teal (people) |
| Alarm Monitoring | `#7209B7` | Purple |

---

## 3. HERO SECTION

```html
<header class="hero-high-impact hero-[PAGE]">
  <div class="container">
    <span class="eyebrow-light">Technical Pillar Guide</span>
    <h1 class="hero-title-main">[Primary Keyword] &amp; <span style="color:#FFD700;">[Secondary Keyword]</span></h1>
    <p class="hero-subtitle-main">[One sentence: what this guide covers. Max 200 chars.]</p>
    <div class="btn-group">
      <a href="request-site-assessment-singapore.html?intent=[page]-assessment" class="btn btn-primary">Book Site Assessment</a>
      <a href="https://wa.me/6593860466" class="btn btn-whatsapp-standard">WhatsApp an Engineer</a>
    </div>
  </div>
</header>
```

### Hero image class per page
| Page | Hero class |
|---|---|
| cctv.html | `hero-cctv` |
| burglar-alarm.html | `hero-alarm` |
| door-access.html | `hero-access` |
| auto-gate-singapore.html | `hero-vehicle` |
| intercom-system-singapore.html | `hero-intercom` *(add to sv-shared.css)* |

---

## 4. AUTHOR BIO STRIP

Placed immediately after `</header>`, before breadcrumb:

```html
<div style="background:#fff; border-bottom:1px solid var(--border-light); padding: 0;">
  <div class="container">
    <div class="author-bio-strip">
      <img src="images/ler-wee-meng-bio.jpeg" alt="Ler Wee Meng" class="author-bio-photo">
      <div class="author-bio-text">
        <span class="author-bio-name sv-author-name">Ler Wee Meng</span>
        <span class="author-bio-credentials">Founder & CEO · Securevision · 37+ Years Experience</span>
      </div>
    </div>
  </div>
</div>
```

---

## 5. BREADCRUMB

```html
<nav class="sv-breadcrumb" aria-label="Breadcrumb">
  <div class="container">
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="security-systems-singapore.html">Systems</a></li>
      <li>[Current Page Name]</li>
    </ul>
  </div>
</nav>
```

---

## 6. LAYOUT WRAPPER

```html
<div class="container mt-64 mb-64" style="max-width:1280px;">
  <div class="layout-with-sidebar">

    <!-- MAIN CONTENT — left column -->
    <main>
      [Content — Mode A or Mode B — see Section 8]
    </main>

    <!-- SIDEBAR — right column -->
    <aside>
      <div class="sticky-toc">
        <h3 class="toc-title" onclick="toggleToc()">Guide Navigator</h3>
        <ul class="toc-list" id="tocList">
          <li><a href="#[section-id]">1. [Section Name]</a></li>
          <li><a href="#[section-id]">2. [Section Name]</a></li>
          <!-- one entry per section or subsection — no limit -->
          <!-- Do NOT list the final CTA here -->
        </ul>
        <!-- Founder card below TOC -->
        <div class="founder-card">
          <div class="fc-head">
            <img src="images/ler-wee-meng-bio.jpeg" alt="Ler Wee Meng">
            <div>
              <strong>Ler Wee Meng</strong>
              <span>Founder & CEO · <span class="sv-years-experience"></span>+ Years</span>
            </div>
          </div>
          <p>Need expert advice? Discuss your site requirements with our engineering team.</p>
          <a href="https://wa.me/6593860466" class="fc-wa-link">💬 WhatsApp an Engineer</a>
        </div>
      </div>
    </aside>

  </div><!-- end layout-with-sidebar -->
</div><!-- end container -->
```

---

## 7. CONTENT SECTION STRUCTURE

Each section uses `<section>` with an `id`. Sections alternate white and bg-light.

**Mode A** — IDs are `section1`, `section2`, `section3`, `section4`, `section5`.
**Mode B** — IDs are descriptive slugs matching the existing page content exactly
(e.g. `what-is-cctv`, `how-it-works`, `camera-types`). Copy IDs verbatim from
the source file — do not rename them.

```html
<section id="[section-id]">
  <!-- white background — no class needed -->
  <span class="eyebrow">[Eyebrow label]</span>
  <h2>[Section Heading]</h2>
  <p class="lead">[Opening paragraph — use .lead on first paragraph of each section only]</p>

  <div class="blog-row">
    <div class="blog-text">
      <h3>[Subsection heading]</h3>
      <p>[Body copy]</p>
    </div>
    <div class="blog-img-wrap">
      <img src="images/[image].webp" alt="[Descriptive alt text]">
    </div>
  </div>

</section>

<section id="[section-id]" class="bg-light">
  <!-- bg-light background — alternate with white -->
</section>
```

### Content Component Library (all from sv-guides.css)

**Text + image row (65/35, non-wrapping):**
```html
<div class="blog-row">
  <div class="blog-text">[text]</div>
  <div class="blog-img-wrap"><img src="..." alt="..."></div>
</div>
```

**Text + image row (word-wrap float — for long descriptive text):**
```html
<div class="blog-row-wrap">
  <div class="blog-img-wrap">
    <img src="..." alt="...">
    <span class="blog-img-caption">[Caption text]</span>
  </div>
  <p>[Long body copy — wraps around image]</p>
  <p>[Continues...]</p>
</div>
```

**Square image (1:1 aspect ratio):**
```html
<div class="blog-img-wrap blog-img-square">
  <img src="..." alt="...">
</div>
```

**Full-width image (standalone — no text beside it):**
```html
<div class="blog-img-wrap" style="aspect-ratio:16/9; max-width:100%;">
  <img src="..." alt="...">
  <span class="blog-img-caption">[Caption]</span>
</div>
```

**Data table:**
```html
<div class="blog-table-wrap">
  <table class="blog-table">
    <thead>
      <tr><th>Column 1</th><th>Column 2</th><th>Column 3</th></tr>
    </thead>
    <tbody>
      <tr><td>Data</td><td>Data</td><td>Data</td></tr>
    </tbody>
  </table>
</div>
```

**Recommendation box:**
```html
<div class="recommendation-box">
  <h4>💡 Securevision Recommendation</h4>
  <p>[Recommendation text]</p>
</div>
```

**Component card (numbered — for anatomy sections):**
```html
<div class="component-card">
  <div class="component-header">
    <div class="component-number">1</div>
    <h3>[Component Name]</h3>
  </div>
  <div class="blog-row">
    <div class="blog-text"><p>[Description]</p></div>
    <div class="blog-img-wrap blog-img-square"><img src="..." alt="..."></div>
  </div>
</div>
```

**FAQ accordion:**
```html
<div class="faq-grid">
  <div class="faq-item">
    <h4>[Question]</h4>
    <p>[Answer]</p>
  </div>
</div>
```

**Subsection heading (with left border accent):**
```html
<div class="subsection">
  <h3>[Subsection heading]</h3>
  [content]
</div>
```

---

## 8A. MODE A — 5-PART CONTENT FRAMEWORK (new pages)

Use this for new page builds only (e.g. intercom-system-singapore.html).

### Part 1 — Conceptual Logic (The "Why")
- Section ID: `section1`
- Background: white
- Content: Define what this system IS and WHY it exists in a security architecture.
- Use `.lead` for opening paragraph.
- Include stat grid if applicable (3 key numbers from this system's performance).

### Part 2 — Anatomy of the Tech (The "How")
- Section ID: `section2`
- Background: `bg-light`
- Content: Deconstruct the hardware. Explain physics of sensors, mechanics of motors, optics of cameras.
- Use `.component-card` with numbered `.component-number` for each component.
- Use 1:1 square images (`blog-img-square`) for component diagrams.
- Use `.blog-table` for specification comparisons.

### Part 3 — Securevision Design Standard (The "Expertise")
- Section ID: `section3`
- Background: white
- Content: Singapore-specific engineering. SCDF compliance, IP67/IP66 tropicalisation, MAS TRM, BCA standards.
- Include the `.recommendation-box` with Securevision's specific position.

### Part 4 — System Integration (The "Unification")
- Section ID: `section4`
- Background: `bg-light`
- Content: How this system connects to others. If-This-Then-That logic. Cross-system triggers.

### Part 5 — Architect's Checklist (The "Action")
- Section ID: `section5`
- Background: white
- Content: 5–6 self-audit questions that help the reader assess their own property.
- Close with a `.recommendation-box` pointing to the site assessment.
- Do NOT list in TOC. Do NOT add a CTA banner inside this section.

---

## 8B. MODE B — DEEP TECHNICAL REFERENCE (existing pages)

Use this for cctv.html, burglar-alarm.html, door-access.html, auto-gate-singapore.html.

### Core Rule
This is a structural migration — not a rewrite. The source HTML contains the
final approved copy. The task is to move that copy into the correct template
wrapper and replace old CSS classes with the correct ones.

### What changes in a Mode B migration
- Old inline `<style>` blocks → removed entirely
- Old `style=""` attributes → removed (except hero background-image)
- Old div wrapper patterns → replaced with correct template components
  (e.g. old feature box → `.component-card`, old tip box → `.recommendation-box`)
- Old class names → replaced with correct sv-guides.css / sv-shared.css classes
- Nav and footer → replaced verbatim with frozen template versions
- Author bio strip → added if missing
- Breadcrumb → added if missing
- Sidebar with sticky TOC → added if missing
- Final CTA → replaced with correct template CTA

### What does NOT change in a Mode B migration
- Every word of body copy — preserved exactly
- Every heading — preserved exactly, word for word
- Every table and its data — preserved exactly
- Every image src and alt attribute — preserved exactly
- The order of sections — preserved exactly
- Section IDs — preserved exactly as they are in the source file
- TOC entries — updated to match the existing section IDs verbatim

### Class mapping guide (old → new)
When you encounter old class names, map them to these correct classes:

| If source has... | Replace with... |
|---|---|
| Any inline `<style>` block | Remove entirely |
| Any `style="..."` attribute (except hero bg) | Remove entirely |
| Old feature/tip/callout box | `.recommendation-box` |
| Old numbered component block | `.component-card` + `.component-header` + `.component-number` |
| Old text+image side-by-side | `.blog-row` + `.blog-text` + `.blog-img-wrap` |
| Old text+image wrap-around | `.blog-row-wrap` + `.blog-img-wrap` |
| Old comparison table | `.blog-table-wrap` + `.blog-table` |
| Old FAQ/accordion item | `.faq-grid` + `.faq-item` |
| Old subsection divider | `.subsection` |
| Old image with caption | `.blog-img-wrap` + `.blog-img-caption` |

---

## 9. FINAL CTA SECTION

Placed OUTSIDE and AFTER the `.container` layout wrapper:

```html
<!-- ═══ FINAL CTA — outside layout wrapper ═══ -->
<section class="cta-section cta-high-impact cta-[PAGE]" style="text-align:center; padding:120px 0;">
  <div class="container">
    <span class="eyebrow-light">Get Your Free Assessment</span>
    <h2 style="color:#fff; margin-bottom:20px;">Ready to Design Your [System] System?</h2>
    <p class="subtitle">Our engineers will assess your site, map coverage gaps, and design a system that fits your property and budget.</p>
    <div class="btn-group">
      <a href="request-site-assessment-singapore.html?intent=[page]-assessment" class="btn btn-primary">Book Free Site Assessment</a>
      <a href="https://wa.me/6593860466" class="btn btn-outline-light">💬 WhatsApp an Engineer</a>
    </div>
    <p style="color:rgba(255,255,255,0.45); font-size:13px; margin-top:32px;">
      Police Licence L/PS/000267/2023P · Serving Singapore Since 2006
    </p>
  </div>
</section>
```

CTA class per page:
| Page | CTA class |
|---|---|
| cctv.html | `cta-cctv` |
| burglar-alarm.html | `cta-alarm` |
| door-access.html | `cta-access` |
| auto-gate-singapore.html | `cta-vehicle` |
| intercom-system-singapore.html | `cta-access` |

---

## 10. SCRIPTS BLOCK

```html
<script>
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

// TOC toggle (mobile)
function toggleToc() {
  document.getElementById('tocList').classList.toggle('active');
  document.querySelector('.toc-title').classList.toggle('active');
}

// TOC scroll-spy
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('main section[id]');
  const tocLinks = document.querySelectorAll('.toc-list a');
  let current = '';
  sections.forEach(s => {
    if (window.scrollY >= s.offsetTop - 150) current = s.getAttribute('id');
  });
  tocLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === '#' + current) link.classList.add('active');
  });
});
</script>
```

---

## 11. CONTENT AUDIT (required before accepting any output)

After Anti-Gravity produces the migrated file, send this follow-up prompt:

```
Before I accept this output, run a content audit against the source file.

List every H2 and H3 from the SOURCE file.
Confirm each one is present in the OUTPUT, word for word.
Confirm no new sentences have been added.
Confirm no source sentences have been removed.

If any check fails, correct it and reissue the full file.
```

---

## 12. ANTI-GRAVITY PROMPT FORMAT

### For a MODE B MIGRATION (existing pages):

```
[Paste GLOBAL-INSTRUCTION.md in full]
[Paste INSTRUCTION-technical-guide.md in full]

--- PAGE BRIEF ---
Template:    _template-technical-guide.html
File:        [filename.html]
Mode:        B — Deep Technical Reference (migration)
Page name:   [Full page name]
Accent:      #[hex] ([colour name])
Hero class:  hero-[name]
CTA class:   cta-[name]
Intent:      [page]-assessment

THIS IS A MIGRATION — NOT A REWRITE.
The source file is attached. It contains the final approved copy.

YOUR ONLY TASKS ARE:
1. Add the correct template wrapper (nav, hero, author bio,
   breadcrumb, layout-with-sidebar, CTA, footer, scripts)
   copying each frozen component verbatim from the template.
2. Remove all inline <style> blocks and style="" attributes.
3. Replace old CSS class names with correct template classes
   using the mapping table in Section 8B.
4. Preserve every heading, paragraph, table, image, and
   section ID exactly as they appear in the source.
5. Update the TOC <li> entries to match the existing
   section IDs in the source file.

DO NOT rewrite, rephrase, condense, or expand any content.
DO NOT add new content to fill any section.
DO NOT rename any section IDs.
DO NOT reorder any content.
```

### For a MODE A NEW BUILD:

```
[Paste GLOBAL-INSTRUCTION.md in full]
[Paste INSTRUCTION-technical-guide.md in full]

--- PAGE BRIEF ---
Template:    _template-technical-guide.html
File:        [filename.html]
Mode:        A — Framework Guide (new build)
Page name:   [Full page name]
Accent:      #[hex] ([colour name])
Hero class:  hero-[name]
CTA class:   cta-[name]
Intent:      [page]-assessment

TOC items:
  1. [Section 1 name]
  2. [Section 2 name]
  3. [Section 3 name]
  4. [Section 4 name]
  (Part 5 — Architect's Checklist — not listed in TOC)

CONTENT BRIEF:
  Part 1 — [Summary of what to cover]
  Part 2 — [Summary]
  Part 3 — [Summary]
  Part 4 — [Summary]
  Part 5 — [Summary]
```

---

*Securevision · INSTRUCTION-technical-guide.md · v2.0 · April 2026*
*Do not modify without updating version number and date*
