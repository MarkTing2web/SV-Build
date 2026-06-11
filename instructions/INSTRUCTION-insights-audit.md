# INSTRUCTION — Insights Article Audit
## Run this against every completed insights article before it goes live
## Version 1.0 — June 2026

---

## HOW TO USE

Paste this instruction into a new chat. Upload the completed article HTML file. I will check every item on this list and return a report showing PASS, FAIL or FLAG for each item.

FAIL = must fix before publishing.
FLAG = worth reviewing — may be a content or judgement call.
PASS = confirmed correct.

---

## SECTION A — FILE AND SETUP

- [ ] **A1** Filename follows `/insights/[slug].html` pattern
- [ ] **A2** `<html lang="en-GB">` present
- [ ] **A3** `<body data-article="[slug]">` — slug matches the `site-config.js` entry exactly
- [ ] **A4** CSS load order correct: `sv-shared.css` → `sv-insights.css` → `site-config.js`
- [ ] **A5** No Google Fonts `<link>` tag in `<head>` — fonts load via `sv-shared.css`
- [ ] **A6** No inline `<style>` blocks anywhere in the file
- [ ] **A7** No inline `style=""` attributes except `background-image` on hero sections
- [ ] **A8** `<nav id="sv-nav"></nav>` present before hero
- [ ] **A9** `<footer id="sv-footer"></footer>` present before scripts
- [ ] **A10** `<script src="/nav-footer.js"></script>` is the last script tag

---

## SECTION B — META TAGS

- [ ] **B1** `<title>` — article title + " | Securevision Insights" — under 60 characters
- [ ] **B2** `meta name="description"` — present, under 155 characters, plain English
- [ ] **B3** `meta name="robots" content="index, follow"` — present
- [ ] **B4** `<link rel="canonical">` — absolute URL, matches page URL exactly
- [ ] **B5** `og:type` = "article"
- [ ] **B6** `og:site_name` = "Securevision"
- [ ] **B7** `og:title` — present, matches page title
- [ ] **B8** `og:description` — present, under 200 characters
- [ ] **B9** `og:url` — absolute URL, matches canonical
- [ ] **B10** `og:image` — points to article-specific feature image, NOT generic `securevision-insights.webp`
- [ ] **B11** `og:image:width` = 640
- [ ] **B12** `og:image:height` = 360
- [ ] **B13** `article:author` = "Ler Wee Meng"
- [ ] **B14** `article:published_time` — present, format YYYY-MM-DD
- [ ] **B15** `article:section` — matches the article category
- [ ] **B16** `article:tag` — minimum 4 tags including "Singapore"
- [ ] **B17** `twitter:card` = "summary_large_image"
- [ ] **B18** `twitter:title` — present
- [ ] **B19** `twitter:description` — present
- [ ] **B20** `twitter:image` — matches og:image

---

## SECTION C — STRUCTURED DATA

- [ ] **C1** JSON-LD `<script type="application/ld+json">` block present in `<head>`
- [ ] **C2** `@type` = "Article"
- [ ] **C3** `headline` matches H1 title
- [ ] **C4** `image` matches og:image path
- [ ] **C5** `author.name` = "Ler Wee Meng"
- [ ] **C6** `datePublished` present and matches `article:published_time`
- [ ] **C7** `mainEntityOfPage` matches canonical URL

---

## SECTION D — HERO

- [ ] **D1** `<header class="insights-header insights-cat-[category]">` — correct category class used
- [ ] **D2** `<span class="insights-cat-label">` — category display name present
- [ ] **D3** `<h1 class="insights-header-title">` — present, max 7 words
- [ ] **D4** `<p class="insights-header-subtitle">` — present, max 10 words
- [ ] **D5** Hero byline present with author photo, name, role
- [ ] **D6** `<span class="sv-years-experience"></span>` present in byline — not hardcoded
- [ ] **D7** Reading time in byline — present and accurate (word count ÷ 200)
- [ ] **D8** SVG illustration present — correct category SVG used

---

## SECTION E — BREADCRUMB

- [ ] **E1** `<nav aria-label="Breadcrumb" class="sv-breadcrumb">` present
- [ ] **E2** Breadcrumb path: Home → Insights → [Category] → [Article Title]
- [ ] **E3** Last breadcrumb item (current page) matches H1 title exactly
- [ ] **E4** Category link uses correct slug (`?category=alarm-intrusion` etc.)

---

## SECTION F — ARTICLE STRUCTURE

- [ ] **F1** `<div class="article-takeaways">` present immediately before section1
- [ ] **F2** Key Takeaways has 4 to 6 bullets
- [ ] **F3** Each takeaway is a standalone fact, under 25 words, no marketing language
- [ ] **F4** All sections use `<section id="sectionN">` with sequential numbering from 1
- [ ] **F5** Each section starts with `<h2>N. Section Title</h2>`
- [ ] **F6** Every section contains at least one `callout-box` or `verdict-box`
- [ ] **F7** At least one `verdict-box` with "Securevision Verdict" label present
- [ ] **F8** Final verdict box is the last content element before `<hr/>`
- [ ] **F9** TOC links in sidebar match actual section IDs and headings

---

## SECTION G — IMAGES

- [ ] **G1** Feature image present in section1 after opening paragraph
- [ ] **G2** Feature image filename: `[slug]-feature.webp`
- [ ] **G3** Feature image uses `class="article-img-float-right"` — no inline styles
- [ ] **G4** All body images use `class="article-img-float-right"` — no inline styles
- [ ] **G5** All images stored at `/images/insights/[filename].webp`
- [ ] **G6** All image filenames follow `[slug]-[descriptor].webp` pattern
- [ ] **G7** No image is duplicated across two different sections
- [ ] **G8** Alt text present on all images — descriptive, not keyword-stuffed

---

## SECTION H — SHARE STRIP

- [ ] **H1** `<div class="article-share">` present between `<hr/>` and author attribution
- [ ] **H2** LinkedIn share button present (`share-btn-linkedin`)
- [ ] **H3** WhatsApp share button present (`share-btn-whatsapp`)
- [ ] **H4** Copy Link button present (`share-btn-copy`)
- [ ] **H5** Add to Google button present (`share-btn-preferred`) linking to `google.com/preferences/source?q=securevision.com.sg`
- [ ] **H6** Share JS present in `<script>` block — wires all 4 buttons dynamically from `window.location.href`

---

## SECTION I — ARTICLE FOOTER ELEMENTS

- [ ] **I1** Author attribution present with photo, name, credentials
- [ ] **I2** `<span class="sv-years-experience"></span>` in author attribution — not hardcoded
- [ ] **I3** LinkedIn `rel="author"` link present in author attribution
- [ ] **I4** Article tags present — minimum 4 including category and Singapore
- [ ] **I5** Tag URLs use correct filter format (`?category=` or `?tag=`)
- [ ] **I6** Tags match `article:tag` meta values

---

## SECTION J — SIDEBAR

- [ ] **J1** TOC present with progress bar
- [ ] **J2** Sidebar CTA title and description are specific to this article's topic — not copied from burglar alarm
- [ ] **J3** Sidebar CTA links to `request-proposal.html?intent=[specific-intent]`
- [ ] **J4** Intent slug is specific to the article topic

---

## SECTION K — FINAL CTA

- [ ] **K1** CTA section present at bottom
- [ ] **K2** CTA headline specific to this article — not copied from burglar alarm
- [ ] **K3** CTA subtitle specific to this article
- [ ] **K4** Three buttons present: Book Assessment, Request Proposal, WhatsApp
- [ ] **K5** Trust note present: "Serving Singapore Since 2006 · Police Licensed · bizSAFE Level 3"

---

## SECTION L — SCRIPTS

- [ ] **L1** Share strip JS present and complete
- [ ] **L2** TOC scroll-spy JS present and complete
- [ ] **L3** No other custom JS beyond these two blocks

---

## SECTION M — CONTENT QUALITY

- [ ] **M1** Voice — direct, engineering-led, no marketing language or superlatives
- [ ] **M2** Reading level — secondary school. No jargon without explanation
- [ ] **M3** Flow — sections are in logical order, each builds on the previous
- [ ] **M4** Accuracy — statistics softened ("significantly more likely" not specific multipliers unless sourced)
- [ ] **M5** No Dahua or Tiandy brand names anywhere
- [ ] **M6** British English throughout — check: authorisation, centre, colour, licence, recognised
- [ ] **M7** Word count 1,500 to 2,500 words
- [ ] **M8** No paragraph longer than 4 sentences
- [ ] **M9** Singapore context present — HDB/landed/condo/MCST referenced where relevant
- [ ] **M10** Primary keyword in H1 and first paragraph
- [ ] **M11** Section headings are scannable and descriptive — not generic

---

## SECTION N — SITE-CONFIG AND DEPLOYMENT

- [ ] **N1** Article entry exists in `site-config.js`
- [ ] **N2** `image` field added to `site-config.js` entry pointing to feature image filename
- [ ] **N3** Category in `site-config.js` matches `article:section` meta tag
- [ ] **N4** Tags in `site-config.js` are consistent with `article:tag` meta values
- [ ] **N5** After deploy — LinkedIn Post Inspector run to force OG cache refresh before sharing

---

## REPORT FORMAT

Return results as:

**FAILS (must fix):**
- [item code] [description of issue]

**FLAGS (review):**
- [item code] [description of issue]

**PASS:** All other items confirmed correct.

---

*Save this file as `/_instructions/INSTRUCTION-insights-audit.md` in the repo.*
*Use after completing an article and before deploying.*
