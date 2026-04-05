# SECUREVISION — INSIGHTS ARTICLE INSTRUCTION
## Page Type: Insights / Blog Articles
## Applies to: All articles under insights-*.html
## Version 1.0 — April 2026
## This file lives at: /_instructions/INSTRUCTION-insights.md
## Primary standard: Securevision-Blog-Standards.md (v1.7, April 2026)
## This file supplements Blog Standards with Anti-Gravity-specific rules.

---

## ⚠️ RULES SPECIFIC TO THIS PAGE TYPE

1. **No inline `<style>` blocks.** Insights pages use `sv-shared.css` + `sv-guides.css`. All component classes are defined there.
2. **Tone is the founder's voice — first person, engineering-led, direct.** Write as Ler Wee Meng speaking from 37 years of experience. Never generic, never salesy.
3. **British English throughout.** Authorisation, optimisation, licence, programme, recognisable.
4. **All humans in images must be Asian, in recognisably Singaporean settings.** Securevision staff must wear white or black polo-T with visible Securevision branding. See Blog Standards Section 1.
5. **Callout boxes use `.callout-box` class** — do not use inline styles for key point panels. If `.callout-box` is missing from `sv-shared.css`, add it (see Section 9 below).
6. **Verdict boxes use `.verdict-box` class** — for "Securevision Verdict" or "Securevision View" sections.
7. **The author bio footer is mandatory** — 150–200 words, mentions NUS BEng, UoL LLB, 37+ years, VESTA platform, 2,000+ sites.
8. **Tags are mandatory** — positioned directly after the author bio, before article navigation.
9. **Related Insights shows 3 articles** — use `.related-grid` and `.nav-card`. Never fewer than 3.

---

## 1. ARTICLE CATEGORIES (fixed — use exactly these)

| Category | Slug | Typical topics |
|---|---|---|
| Security Planning | `security-planning` | How to choose systems, design decisions, site assessment advice |
| Technology | `technology` | AI analytics, IP architecture, system integrations, new tech |
| Case Studies | `case-studies` | Real project outcomes, before/after, client results |
| Singapore Industry | `singapore-industry` | Local regulations, PDPA, SCDF, MOM compliance, market trends |

---

## 2. IMAGE NAMING & DIMENSIONS (from Blog Standards Section 4)

| Type | Dimensions | Naming convention |
|---|---|---|
| Cover / Hero | 1200 × 480 px | `insight-[slug]-cover.jpg` |
| In-article | 800 × 500 px | `insight-[slug]-[desc].jpg` |
| CTA background | 1600 × 600 px | `insight-[slug]-cta.jpg` |

Image prompt style: "Professional photography, sharp architectural lines, cinematic lighting, modern security hardware, Singapore properties."

---

## 3. PAGE STRUCTURE

```
[Head]
[Nav — frozen]
[Article Header — category tag, H1, author byline]
[Breadcrumb — sv-breadcrumb]
[Layout with sidebar]
  [Article body — left column]
    Sections 1–N (numbered H2 headings)
    Callout boxes where appropriate
    Verdict box (end of article)
    Author bio footer (.author-bio-footer)
    Tags (.article-tags + .tag-pill)
    Article navigation (.prev-next-nav + .nav-card)
  [Sidebar — right column]
    Sticky TOC (.sticky-toc)
    Founder card (.founder-card)
[Related Insights — full width, outside layout]
[Final CTA — full width]
[Footer — frozen]
[WhatsApp float]
[Scripts incl. TOC scroll-spy]
```

---

## 4. HEAD TEMPLATE

```html
<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Article Title] | Securevision Insights</title>
  <meta name="description" content="[140–160 chars — written as a compelling reason to read the article, not a summary]">
  <link rel="canonical" href="https://www.securevision.com.sg/[slug].html">
  <meta property="og:title" content="[Article Title] | Securevision Insights">
  <meta property="og:description" content="[Same as meta description]">
  <meta property="og:image" content="https://www.securevision.com.sg/images/insight-[slug]-cover.jpg">
  <meta property="og:url" content="https://www.securevision.com.sg/[slug].html">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Securevision">
  <meta property="article:author" content="Ler Wee Meng">
  <meta property="article:published_time" content="[YYYY-MM-DD]">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="sv-shared.css">
  <script src="site-config.js"></script>
  <link rel="stylesheet" href="sv-guides.css">
</head>
```

---

## 5. ARTICLE HEADER (replaces hero for insights pages)

Insights articles do not use the full `.hero-high-impact` hero. They use a compact article header — dark background, category tag, H1, author byline. No background image.

```html
<header style="background: linear-gradient(135deg, #0E1A2B 0%, #1a2942 100%); padding: calc(68px + 48px) 0 48px; color:#fff;">
  <div class="container" style="max-width:900px;">
    <span class="badge badge-primary" style="margin-bottom:20px; display:inline-block;">[CATEGORY]</span>
    <h1 style="font-family:'Montserrat',sans-serif; font-size:clamp(26px,4vw,44px); font-weight:800; line-height:1.2; margin-bottom:24px; color:#fff;">
      [ARTICLE TITLE]
    </h1>
    <!-- Hero byline — exactly 2 lines per Blog Standards Section 2 -->
    <div class="hero-byline">
      <img src="images/ler-wee-meng-bio.jpeg" alt="Ler Wee Meng" class="hero-byline-img">
      <div class="hero-byline-text">
        <strong>Ler Wee Meng</strong>
        <span>Founder &amp; CEO · Securevision · 37+ Years Experience · [PUBLISH DATE]</span>
      </div>
    </div>
  </div>
</header>
```

---

## 6. BREADCRUMB

```html
<nav class="sv-breadcrumb" aria-label="Breadcrumb">
  <div class="container">
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="security-articles-singapore.html">Insights</a></li>
      <li><a href="security-articles-singapore.html?cat=[category-slug]">[Category Name]</a></li>
      <li>[Article short title — max 40 chars]</li>
    </ul>
  </div>
</nav>
```

---

## 7. LAYOUT WRAPPER

```html
<div class="container mt-64 mb-64" style="max-width:1280px;">
  <div class="layout-with-sidebar">

    <main class="article-body" style="padding: 80px 0;">

      <!-- Article sections go here — see Section 8 -->

      <!-- AUTHOR BIO FOOTER — mandatory, end of article prose -->
      <div class="author-bio-footer">
        <div class="abf-flex">
          <img src="images/ler-wee-meng-bio.jpeg" alt="Ler Wee Meng" class="abf-img">
          <div class="abf-content">
            <h3>About the Author</h3>
            <p>Ler Wee Meng is the Founder and CEO of Securevision Pte Ltd, Singapore's integrated security systems specialist. He holds a Bachelor of Engineering from the National University of Singapore and a Bachelor of Laws from the University of London, and brings 37 years of hands-on experience spanning R&D, engineering, project management, and systems integration.</p>
            <p>Securevision has protected over 2,000 sites across Singapore — from Good Class Bungalows and MCST-managed condominiums to government institutions and industrial facilities. Ler is also the architect of the VESTA™ platform, Securevision's unified security management and estate operations system.</p>
          </div>
        </div>
      </div>

      <!-- TAGS — mandatory, directly after author bio -->
      <div class="article-tags">
        <a href="security-articles-singapore.html?cat=[category-slug]" class="tag-pill">[Category]</a>
        <a href="security-articles-singapore.html?tag=[tag]" class="tag-pill">[Tag 1]</a>
        <a href="security-articles-singapore.html?tag=[tag]" class="tag-pill">[Tag 2]</a>
        <a href="security-articles-singapore.html?tag=[tag]" class="tag-pill">[Tag 3]</a>
      </div>

      <!-- ARTICLE NAVIGATION — prev/next -->
      <nav class="prev-next-nav" aria-label="Article navigation">
        <a href="[PREV-ARTICLE].html" class="nav-card">
          <span>← Previous</span>
          <strong>[Previous article title]</strong>
        </a>
        <a href="[NEXT-ARTICLE].html" class="nav-card" style="text-align:right;">
          <span>Next →</span>
          <strong>[Next article title]</strong>
        </a>
      </nav>

    </main>

    <!-- SIDEBAR -->
    <aside>
      <div class="sticky-toc">
        <h3 class="toc-title" onclick="toggleToc()">In This Article</h3>
        <ul class="toc-list" id="tocList">
          <li><a href="#section1">1. [Section heading]</a></li>
          <!-- one per H2 section — do NOT include author bio or tags -->
        </ul>
        <!-- Founder card -->
        <div class="founder-card">
          <div class="fc-head">
            <img src="images/ler-wee-meng-bio.jpeg" alt="Ler Wee Meng">
            <div>
              <strong>Ler Wee Meng</strong>
              <span>Founder &amp; CEO · 37+ Years</span>
            </div>
          </div>
          <p>Need expert advice? Discuss your site requirements with our engineering team.</p>
          <a href="https://wa.me/6593860466" class="fc-wa-link">💬 WhatsApp an Engineer</a>
        </div>
      </div>
    </aside>

  </div>
</div>
```

---

## 8. ARTICLE BODY — CONTENT COMPONENTS

All sections use `<section id="sectionN">` with H2 headings. Sections alternate white and bg-light.

### Section structure:
```html
<section id="section1">
  <h2>1. [Section heading — numbered]</h2>
  <p>[Body paragraph — Inter, 16px, 1.8 line height]</p>
</section>
```

### Callout box (Key Point / Planning Point):
```html
<div class="callout-box">
  <p class="callout-label">KEY POINT</p>
  <p>[The key takeaway — 1–3 sentences. Bold, clear, actionable.]</p>
</div>
```
*Note: `.callout-box` must exist in `sv-shared.css`. If missing, add it — see Section 9.*

### Verdict box (Securevision View / Securevision Verdict):
```html
<div class="verdict-box">
  <p class="verdict-label">Securevision Verdict</p>
  <p>[Ler Wee Meng's professional opinion on this topic — 2–4 sentences. Engineering-led, specific.]</p>
</div>
```
*Note: `.verdict-box` must exist in `sv-shared.css`. If missing, add it — see Section 9.*

### In-article image:
```html
<div class="article-image-box">
  <img src="images/insight-[slug]-[desc].jpg" alt="[Descriptive alt text]">
  <p class="image-caption">[Caption — italic, 12px, centred]</p>
</div>
```
*Note: `.article-image-box` must exist in `sv-shared.css`. If missing, add it — see Section 9.*

### Comparison table:
```html
<div class="blog-table-wrap">
  <table class="blog-table">
    <thead><tr><th>[Col 1]</th><th>[Col 2]</th><th>[Col 3]</th></tr></thead>
    <tbody>
      <tr><td>[Data]</td><td>[Data]</td><td>[Data]</td></tr>
    </tbody>
  </table>
</div>
```

---

## 9. MISSING CSS — ADD TO sv-shared.css IF NOT PRESENT

The Blog Standards references these classes. Check `sv-shared.css` before building. If missing, add these blocks:

```css
/* Callout box — Key Points / Planning Points */
.callout-box {
  background: #f0f7ff;
  border-left: 4px solid var(--primary-blue);
  border-radius: 0 8px 8px 0;
  padding: 24px 28px;
  margin: 32px 0;
}
.callout-box .callout-label {
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: var(--primary-blue);
  margin-bottom: 10px;
}

/* Verdict box — Securevision Verdict / View */
.verdict-box {
  background: #0E1A2B;
  border-radius: 12px;
  padding: 32px 36px;
  margin: 40px 0;
  color: #fff;
}
.verdict-box .verdict-label {
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: rgba(255,255,255,0.5);
  margin-bottom: 12px;
}
.verdict-box p { color: rgba(255,255,255,0.85); line-height: 1.7; margin: 0; }

/* Article image box */
.article-image-box {
  margin: 32px 0;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--border-light);
}
.article-image-box img { width: 100%; display: block; }
.image-caption {
  font-size: 12px;
  color: var(--text-light);
  font-style: italic;
  text-align: center;
  padding: 10px 16px;
  background: var(--bg-light);
}
```

---

## 10. RELATED INSIGHTS (outside layout wrapper)

```html
<!-- RELATED INSIGHTS — outside layout wrapper, full width -->
<section style="padding:80px 0; background:var(--bg-light);">
  <div class="container">
    <h2 style="text-align:center; margin-bottom:40px;">Related Security Insights</h2>
    <div class="related-grid">
      <a href="[ARTICLE-1].html" class="nav-card">
        <span>[Category]</span>
        <strong>[Article 1 title]</strong>
      </a>
      <a href="[ARTICLE-2].html" class="nav-card">
        <span>[Category]</span>
        <strong>[Article 2 title]</strong>
      </a>
      <a href="[ARTICLE-3].html" class="nav-card">
        <span>[Category]</span>
        <strong>[Article 3 title]</strong>
      </a>
    </div>
  </div>
</section>
```

---

## 11. FINAL CTA

```html
<section class="cta-section cta-high-impact cta-skyline" style="text-align:center; padding:120px 0;">
  <div class="container">
    <span class="eyebrow-light">Talk to an Engineer</span>
    <h2 style="color:#fff; margin-bottom:20px;">Have a Question About Your Security System?</h2>
    <p class="subtitle">Our engineering team is available to assess your site, answer technical questions, and design a system that fits your property and budget.</p>
    <div class="btn-group">
      <a href="request-site-assessment-singapore.html" class="btn btn-primary">Book Free Site Assessment</a>
      <a href="https://wa.me/6593860466" class="btn btn-outline-light">💬 WhatsApp an Engineer</a>
    </div>
  </div>
</section>
```

---

## 12. ANTI-GRAVITY PROMPT FORMAT

```
[Paste GLOBAL-INSTRUCTION.md]
[Paste INSTRUCTION-insights.md]

--- ARTICLE BRIEF ---
Template:   _templates/_template-insights.html
File:       insights-[slug].html
Title:      [Full article title]
Category:   [Security Planning / Technology / Case Studies / Singapore Industry]
Published:  [YYYY-MM-DD]
Cover image: images/insight-[slug]-cover.jpg

SECTIONS (numbered H2 headings):
  1. [Section heading] — [2–3 sentence summary of content]
  2. [Section heading] — [summary]
  3. [Section heading] — [summary]
  ...

CALLOUT BOXES: [Note which sections should have KEY POINT callouts]
VERDICT BOX: [The Securevision Verdict — what is Ler Wee Meng's professional position?]

TAGS: [4–5 relevant tags]

RELATED ARTICLES (3):
  1. [Title] — [filename].html
  2. [Title] — [filename].html
  3. [Title] — [filename].html

PREV/NEXT NAVIGATION:
  Prev: [Title] — [filename].html
  Next: [Title] — [filename].html
```

---

*Securevision · INSTRUCTION-insights.md · v1.0 · April 2026*
*Primary standard: Securevision-Blog-Standards.md v1.7*
