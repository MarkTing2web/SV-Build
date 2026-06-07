# SECUREVISION — SOLUTION PAGE INSTRUCTION
## Page Type: Solution Pages (Sector Hubs, Deep-Dives, Persona Sub-Pages)
## Version 2.0 — June 2026
## This file lives at: C:/Projects/SV-Build/_ai/INSTRUCTION-solution.md

---

## ⚠️ RULES — READ BEFORE WRITING ANY PAGE

These rules are non-negotiable. Every one was established through an audit of the live site. Do not deviate.

### 1. --page-accent is always #0056b3
There are no sector-specific accent colours. Every solution page uses `--page-accent: #0056b3`. Do not introduce any other value. Do not reference old colour tables from previous instruction versions.

### 2. CSS stack — exact load order
```html
<link rel="stylesheet" href="/sv-shared.css">
<link rel="stylesheet" href="/sv-solutions.css">
<script src="/site-config.js"></script>
```
Both CSS files are required. `site-config.js` is a script, not CSS — it comes after the CSS links. No other CSS files are permitted on solution pages.

### 3. Style block — exactly 3 rules, nothing else
```html
<style>
  :root { --page-accent: #0056b3; }
  .hero-[slug] { background-image: url('/images/solutions/hero-solutions/[slug].webp'); }
  @media (max-width: 768px) {
    .hero-[slug] { background-image: url('/images/solutions/hero-solutions/[slug]-mobile.webp'); }
  }
</style>
```
- No `linear-gradient` anywhere in the style block
- No `background:` shorthand — use `background-image:` only
- No other CSS rules beyond these three
- The `og:image` tag must use the same hero image path

### 4. Trust bar — canonical 3-item structure
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
- Outer class: `trust-bar` — not `sv-trust-bar`
- Inner class: `trust-bar-inner` — not `trust-flex-inline`
- Divider class: `trust-divider` — not `divider`, not `sep`
- Exactly 3 items — Police Licensed, bizSAFE Level 3, Sites Protected
- **BCA Registered is never in the trust bar** — it lives in the footer
- `sv-bizsafe` renders the dynamic text — never write "bizSAFE Level 3" in plain text
- `sv-sites` must be inside `<strong>` — never a plain number

### 5. WhatsApp float — never hardcode
The WhatsApp floating button is injected by `nav-footer.js` at runtime. Never write `sv-wa-float` HTML in any page. Never add a WhatsApp `<a>` to the hero. The only WhatsApp link permitted is inside the trust note if absolutely necessary — and even then, check whether it already appears via injection.

### 6. Dynamic values — never hardcode
| Value | Dynamic class | Example |
|---|---|---|
| Police licence number | `sv-licence` | `<span class="sv-licence"></span>` |
| bizSAFE level | `sv-bizsafe` | `<span class="sv-bizsafe"></span>` |
| Site count | `sv-sites` inside `<strong>` | `<strong class="sv-sites"></strong> Sites Protected` |
| Years in business | `sv-years-business` | `<span class="sv-years-business"></span> years` |
| Current year | `sv-current-year` | `<span class="sv-current-year"></span>` |

"Since 2006" as static text is acceptable. A capacity number like "can house 2,000 residents" is acceptable. A price like "$2,000 to $6,000" is acceptable. What is never acceptable is using a plain number where `sv-sites`, `sv-licence`, or `sv-bizsafe` should be.

### 7. Inline styles — zero
No `style=` attributes anywhere in `<body>`. Not for layout, not for typography, not for colour, not for spacing. Every layout requirement must be handled by a CSS class. The only permitted exception is `stat-bar-fill` elements with `style="width:X%"` — these are data-driven bar widths.

### 8. No inline typography
No `font-size`, `font-family`, `font-weight`, `color`, or `line-height` as inline styles. The typography system is defined in `sv-shared.css` and `sv-solutions.css`. Use classes only.

### 9. British English throughout
licence (not license as a noun), colour, centre, optimise, authorisation, programme. Exception: "License Plate Recognition" and "LPR" are technical terms — keep American spelling.

---

## PAGE TYPE REFERENCE

| Page type | URL pattern | Hero class | CTA label |
|---|---|---|---|
| Sector hub index | `/solutions/index.html` | `hero-standard` | Book a Site Assessment |
| Sector hub | `/solutions/[sector].html` | `hero-standard` | Book a Site Assessment |
| Problem-based page | `/solutions/[problem].html` | `hero-standard` | Book a Site Assessment |
| Deep-dive systems | `/solutions/[sector]/[sector]-security-systems.html` | `hero-standard` | Book a Site Assessment |
| Persona sub-page | `/solutions/[sector]/[persona].html` | `hero-compact` | Request a Proposal |

Hero heights: `hero-standard` = 65vh desktop / 380px mobile. `hero-compact` = 44vh desktop / 280px mobile.

---

## PAGE STRUCTURE — MANDATORY SEQUENCE

```
<nav id="sv-nav">                   ← injected, placeholder only
<header class="hero-high-impact hero-standard hero-[slug]">
<div class="trust-bar">
<nav class="sv-breadcrumb">
<section class="sv-section-grey">  ← S1: first content section = always grey
<section class="sv-section-white"> ← S2: alternates
<section class="sv-section-grey">  ← S3: alternates
... strict grey/white alternation throughout ...
<section class="cta-section cta-high-impact">  ← final CTA, outside <main>
<footer id="sv-footer">            ← injected, placeholder only
<script src="/systems-block.js">   ← if sv-systems-block used on page
<script src="/nav-footer.js">      ← always last
```

Sections must alternate without exception. Never two grey or two white sections in a row. The CTA section does not count as a content section — it sits outside `<main>` and is not part of the alternation.

---

## SECTION GUIDE

### S1: PROBLEM STATEMENT (sv-section-grey)
Make the visitor feel understood before any product is mentioned. No system names, no product names, no brand names. Tone: "here is the reality of managing [sector]".

Structure: `eyebrow` + `h2` + `p.subtitle` + `div.grid-3` of 3 `.card` elements each with `h3` and `p`.

### S2: SUB-PERSONA ROUTER (sv-section-white)
Omit entirely if the sector has no sub-persona pages. When present: `h2` + `p.subtitle` + `div.grid-3` of `a.rel-card` links. Each card: `h3` + `p` + `div.rel-card-footer`.

### S3: SYSTEMS BLOCK (sv-section-grey)
Use the `sv-systems-block` injection placeholder. Do not write system cards manually.

```html
<div class="sv-systems-block" data-cols="3"
     data-eyebrow="What We Install"
     data-heading="What Goes Into a [Sector] Security System"
     data-intro="[One sentence]"
     data-systems="premises,entry-access,vehicle-lpr,ip-telephony,network,security-platform">
</div>
```

**`data-cols` rules:**
- 6 systems → `data-cols="3"` (3×2 grid)
- 5 systems → `data-cols="3"` (3+2 grid)
- 4 systems → `data-cols="2"` (2×2 grid)

**System keys** (use these exact strings in `data-systems`):
`premises` / `entry-access` / `vehicle-lpr` / `ip-telephony` / `network` / `security-platform`

**Residential sector note:** Always include `vehicle-lpr` but override the description to focus on auto-gates — no LPR, no barriers, no commercial car park language:
```html
data-desc-vehicle-lpr="Auto-gates and motorised gates are the vehicle access layer for landed homes. We install sliding and swing gate motors, connect them to the intercom system, and integrate smartphone control so residents open the gate remotely from the mobile app or indoor monitor."
```

**`systems-block.js` must be loaded** in the scripts section for the injection to work.

### S4: THE [SECTOR] PROTOCOL (sv-section-white)
Steps must be sector-specific. Use `div.step-row` containing `div.step-item` elements. Each step-item: `div.step-num` + `h3` + `p`. No inline styles.

### S5: PORTFOLIO PROOF (sv-section-grey)
Only link to real published portfolio pages. Use `div.grid-3` of `a.proof-card` links. Each card: `div.proof-image-wrap` + `img` (with descriptive alt, absolute src) + `div.proof-content` containing `p.proof-tag` + `h3` + `p`. Follow with `div.text-center.mt-48` view-all button.

### S6: MID-PAGE NUDGE (sv-section-white) — optional
Only include on long pages (8+ sections). Keep copy distinct from the final CTA. Container with `text-center` class, `h2`, `p.subtitle`, `div.btn-group`.

### S7: WHY SECUREVISION (sv-section-grey)
3 differentiators, each addressing a real objection. Never generic. No sales language ("best value", "affordable", "cheapest"). Use outcome language: "reduced operational liability", "lower total cost of ownership", "minimised guard dependency". Use `div.grid-3` of `.card` with `h3` + `p`.

### S8: FAQ (sv-section-white)
4–6 questions, sector-specific. Use `div.faq-grid` of `div.faq-item`. Each item: `h3.faq-question` + `p.faq-answer`. Questions are H3 — never H2 or H4.

### S9: CROSS-SELL (sv-section-grey)
Show 2–3 adjacent sectors only. Adjacency guide:

| Sector | Adjacent to |
|---|---|
| Residential | Condominiums, Commercial |
| Condominiums | Residential, Managed Living |
| Commercial | Industrial, Institutions |
| Industrial | Commercial, Managed Living |
| Institutions | Healthcare, Commercial |
| Healthcare | Managed Living, Institutions |
| Managed Living | Industrial, Healthcare |
| Data Centres | Industrial, Commercial |

Use `div.grid-3` of `a.rel-card` links with `h3` + `p` + `div.rel-card-footer`.

---

## HEADING HIERARCHY RULES

- Exactly one `h1` per page — inside the hero
- Section headings are `h2`
- Card titles inside sections are `h3`
- Sub-headings inside cards (where needed) are `h4` — only after an `h3`
- **Never skip a level** — no h2 → h4 without an h3 in between
- `arch-grid` headings are always `h3`, never `h4`
- `faq-question` is always `h3`
- `step-item` headings are always `h3`

---

## CARD CONTRAST RULES

Cards must contrast with their section background:
- Cards in `sv-section-grey` → white background (default `.card` is white)
- Cards in `sv-section-white` → grey background (`var(--bg-light)`, `#EEF2F7`)
- `arch-card` is always white regardless of section
- `callout-box` is always white regardless of section
- Never set card background via inline style — card contrast is handled by CSS classes

---

## FINAL CTA — MANDATORY STRUCTURE

```html
<section class="cta-section cta-high-impact">
  <div class="container">
    <h2>Ready to Secure Your Property?</h2>
    <p class="subtitle">Tell us about your site. We'll assess it and design a system that works as one.</p>
    <div class="btn-group">
      <a href="/request-site-assessment-singapore.html?intent=[slug]-cta" class="btn btn-primary">Book a Site Assessment</a>
    </div>
    <p class="cta-trust-note">Serving Singapore Since 2006</p>
  </div>
</section>
```

- Both classes `cta-section` and `cta-high-impact` are required
- Must contain an `h2`
- Subtitle must use `.subtitle` class — not inline
- CTA label: `Book a Site Assessment` for hub/deep-dive/problem pages, `Request a Proposal` for persona sub-pages
- No inline styles anywhere in this section
- Sits outside `</main>`, before `<footer>`

---

## SEO REQUIREMENTS

| Field | Rule |
|---|---|
| `<title>` | 50–60 characters. Must include "Singapore". Format: `[Topic] Singapore \| Securevision` |
| `<meta name="description">` | 120–160 characters. Benefit-led. Must include Singapore. |
| `<link rel="canonical">` | Absolute URL: `https://www.securevision.com.sg/[path]` |
| `og:title` | Matches `<title>` exactly |
| `og:description` | Matches `<meta name="description">` exactly |
| `og:image` | Absolute URL to the actual hero image: `https://www.securevision.com.sg/images/solutions/hero-solutions/[slug].webp` — not `og-default.jpg` |
| `og:url` | Matches canonical exactly |
| No entities | No `&amp;` or `&#039;` in title or description |

---

## ANTIGRAVITY PROMPT FORMAT

When creating a new solution page, give Antigravity this brief:

```
[Paste INSTRUCTION-solution.md]

--- PAGE BRIEF ---
Template:    _templates/_template-solution-standard.html
File:        solutions/[sector].html
Page type:   [sector hub / persona / deep-dive / problem-based]
Hero class:  hero-[slug]
Audience:    [Primary decision-maker for this sector]

SEO:
  Title: [50–60 chars, includes Singapore]
  Description: [120–160 chars, benefit-led]
  Hero image: /images/solutions/hero-solutions/[slug].webp

HERO:
  Eyebrow: [Category label]
  H1: [Outcome-focused headline]
  Subtitle: [One sentence, max 200 chars]

SYSTEMS BLOCK:
  Systems: [comma-separated list of system keys]
  data-cols: [2 or 3]
  Heading: [What goes into a [sector] system]
  Intro: [One sentence]
  Description overrides (if needed): [key: text]

S1 PROBLEM (3 cards):
  Card 1: [Heading] / [2–3 sentences]
  Card 2: [Heading] / [2–3 sentences]
  Card 3: [Heading] / [2–3 sentences]

S2 ROUTER (if sub-pages exist):
  [Sub-type name] / [2 sentences] / [href]
  [Sub-type name] / [2 sentences] / [href]
  [Sub-type name] / [2 sentences] / [href]

S4 PROTOCOL (4 steps):
  Step 1: [Name] / [2–3 sentences]
  Step 2: [Name] / [2–3 sentences]
  Step 3: [Name] / [2–3 sentences]
  Step 4: [Name] / [2–3 sentences]

S5 PROOF (portfolio references):
  Project 1: [name] / [slug] / [image] / [tag] / [2 sentences]
  Project 2: [name] / [slug] / [image] / [tag] / [2 sentences]
  Project 3 (if available): [name] / [slug] / [image] / [tag] / [2 sentences]

S7 WHY SECUREVISION (3 differentiators):
  1. [Heading] / [3–4 sentences]
  2. [Heading] / [3–4 sentences]
  3. [Heading] / [3–4 sentences]

S8 FAQ (4 questions):
  Q1: [Question] / [3–4 sentence answer]
  Q2: [Question] / [3–4 sentence answer]
  Q3: [Question] / [3–4 sentence answer]
  Q4: [Question] / [3–4 sentence answer]

S9 CROSS-SELL:
  [Adjacent sector 1] / [href] / [1–2 sentences]
  [Adjacent sector 2] / [href] / [1–2 sentences]
  [Adjacent sector 3 if needed] / [href] / [1–2 sentences]

FINAL CTA:
  H2: [Heading]
  Subtitle: [One sentence]
  Intent param: [slug]-cta
```

---

## QUALITY CHECKLIST — RUN BEFORE SAVING

Before considering any solution page complete, verify:

- [ ] `lang="en-GB"` on `<html>`
- [ ] Title 50–60 chars, includes "Singapore"
- [ ] Description 120–160 chars
- [ ] Canonical absolute URL
- [ ] All 4 OG tags present, `og:image` is actual hero path
- [ ] Style block: exactly 3 rules, `#0056b3`, `background-image` only, no gradient
- [ ] Hero: correct height class (`hero-standard` or `hero-compact`), `hero-high-impact`, page-specific class
- [ ] Trust bar: 3 items, correct classes, `sv-bizsafe`, `sv-sites` inside `<strong>`, no BCA
- [ ] Breadcrumb: linked Home, unlinked last item, correct depth
- [ ] Sections start grey, alternate strictly
- [ ] Zero inline `style=` attributes in `<body>` (except `stat-bar-fill width:X%`)
- [ ] Zero hardcoded dynamic values (licence, sites, bizsafe)
- [ ] CTA label correct for page type
- [ ] `cta-section cta-high-impact` classes on final CTA
- [ ] No `sv-wa-float` in HTML
- [ ] `nav-footer.js` loaded last
- [ ] `systems-block.js` loaded if `sv-systems-block` used
- [ ] All image `alt` attributes descriptive, all `src` and `href` absolute paths
- [ ] No heading levels skipped
- [ ] British English (except "License Plate Recognition")

---

*Securevision · INSTRUCTION-solution.md · v2.0 · June 2026*
