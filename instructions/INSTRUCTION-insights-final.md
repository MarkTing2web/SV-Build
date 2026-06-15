# SECUREVISION — INSIGHTS ARTICLE INSTRUCTION
## Page Type: Insights Articles
## Applies to: All articles under /insights/[slug].html
## Version 2.0 — June 2026
## Gold standard reference: standalone-door-access.html / burglar-alarm-design.html

---

## HOW TO USE THIS FILE

This is the complete guide for building a new Securevision Insights article.
Use alongside:
- `TEMPLATE-insights-meta.md` — copy-paste meta block for every article head
- `INSTRUCTION-insights-audit.md` — pre-publish checklist, run after building

---

## WHAT IS ALREADY DONE FOR YOU

Do not redefine, override or recreate any of these.

| Element | Defined in |
|---|---|
| Nav (desktop + mobile) | `nav-footer.js` + `sv-shared.css` |
| Floating WhatsApp button | `nav-footer.js` |
| Footer | `nav-footer.js` |
| Related articles (auto-populated from site-config.js) | `nav-footer.js` |
| Dynamic values (years experience, licence, sites) | `site-config.js` |
| Hero gradient and layout | `sv-insights.css` |
| Category pill colours | `sv-insights.css` |
| Article body, sidebar, TOC styling | `sv-insights.css` |
| Prose typography | `sv-insights.css` |
| Key Takeaways, callout box, verdict box | `sv-insights.css` |
| Share strip, author attribution | `sv-insights.css` |
| Float image class (`article-img-float-right`) | `sv-insights.css` |
| Sidebar CTA styling | `sv-insights.css` |
| Breadcrumb | `sv-shared.css` |

---

## THE 6 ARTICLE CATEGORIES

| Category | Header class | `article:section` value | Filter slug |
|---|---|---|---|
| Alarm & Intrusion | `insights-cat-alarm` | `Alarm &amp; Intrusion` | `alarm-intrusion` |
| CCTV & Surveillance | `insights-cat-cctv` | `CCTV &amp; Surveillance` | `cctv-surveillance` |
| Access & Intercom | `insights-cat-access` | `Access &amp; Intercom` | `access-intercom` |
| Vehicle & Gates | `insights-cat-vehicle` | `Vehicle &amp; Gates` | `vehicle-gates` |
| Platform & Integration | `insights-cat-platform` | `Platform &amp; Integration` | `platform-integration` |
| Security Planning | `insights-cat-planning` | `Security Planning` | `security-planning` |

---

## ARTICLE STRUCTURE — FIXED ORDER

```
<head>
  Meta block + JSON-LD (TEMPLATE-insights-meta.md)
  sv-shared.css → sv-insights.css → site-config.js

<body data-article="[slug]">
  <nav id="sv-nav">                        ← injected by nav-footer.js
  <header class="insights-header insights-cat-[class]">
    insights-header-inner
      insights-header-left
        insights-cat-label
        h1.insights-header-title
        p.insights-header-subtitle
        hero-byline (photo · name · Founder & Director · date · read time)
      insights-header-illus (SVG)
  <nav class="sv-breadcrumb">              ← Home → Insights → Category → Article
  <div class="article-body">
    <div class="layout-with-sidebar">
      <main class="prose">
        article-takeaways (Key Takeaways — 4 to 6 bullets)
        <section id="section1"> ... </section>
        <section id="section2"> ... </section>
        ...
        <section id="sectionN"> (last content section)
        <div class="verdict-box"> In Short </div>
        <hr/>
        article-share (share strip — 4 buttons)
        author-attribution
        article-tags (max 5 tags)
        <section id="sectionN+1"> FAQ — 10 to 12 questions </section>
      </main>
      <aside>
        sidebar-container
          sidebar-section (TOC + progress bar)
          sidebar-section--cta (contextual CTA)
      </aside>
  <section class="sv-section-grey"> Related Security Insights (auto) </section>
  <section class="cta-section cta-high-impact cta-property"> Final CTA </section>
  <footer id="sv-footer">                  ← injected by nav-footer.js
  <script> Share JS + TOC scroll-spy </script>
  <script src="/nav-footer.js">            ← always last
```

---

## FILE SETUP

- Filename: `/insights/[slug].html`
- `<html lang="en-GB">`
- `<body data-article="[slug]">` — slug must match `site-config.js` exactly
- CSS load order: `sv-shared.css` → `sv-insights.css` → `site-config.js`
- No Google Fonts `<link>` — fonts load via `sv-shared.css`
- No inline `<style>` blocks
- No inline `style=""` attributes

---

## META TAGS

Use `TEMPLATE-insights-meta.md` for the complete copy-paste block. Key rules:

- `<title>` — under 70 characters including " | Securevision"
- `meta description` — plain English, under 160 characters
- `canonical` — `https://www.securevision.com.sg/insights/[slug].html`
- `og:image` → `[slug]-feature-og.webp` (1200×630) — never the generic `securevision-insights.webp`
- `og:image:width` = 1200, `og:image:height` = 630
- `twitter:image` = same as `og:image`
- `article:published_time` — YYYY-MM-DD
- `article:section` — category display name exactly
- Minimum 4 × `article:tag` — always include "Singapore"

---

## JSON-LD

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[H1 TITLE]",
  "description": "[META DESCRIPTION]",
  "image": "https://www.securevision.com.sg/images/insights/[SLUG]-feature.webp",
  "datePublished": "[YYYY-MM-DD]",
  "author": {
    "@type": "Person",
    "name": "Ler Wee Meng",
    "url": "https://www.securevision.com.sg/about.html"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Securevision Pte Ltd",
    "url": "https://www.securevision.com.sg",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.securevision.com.sg/images/securevision-logo-blue.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.securevision.com.sg/insights/[SLUG].html"
  }
}
</script>
```

Note: JSON-LD `"image"` uses the regular feature image (960×540), not the OG version.

---

## HERO HEADER

```html
<header class="insights-header insights-cat-[CATEGORY-CLASS]">
  <div class="container">
    <div class="insights-header-inner">
      <div class="insights-header-left">
        <div class="insights-header-title-group">
          <span class="insights-cat-label">[Category Display Name]</span>
          <h1 class="insights-header-title">[Article Title]</h1>
          <p class="insights-header-subtitle">[One or two sentence subtitle]</p>
        </div>
        <div class="hero-byline">
          <img alt="Ler Wee Meng" class="hero-byline-img" src="/images/ler-wee-meng-bio.webp" />
          <div class="hero-byline-text">
            <strong>Ler Wee Meng</strong>
            <p class="hero-byline-role">Founder &amp; Director · Securevision · <span
                class="sv-years-experience"></span> Years Experience · [D Mmm YYYY] · [N] min read</p>
          </div>
        </div>
      </div>
      <div class="insights-header-illus">
        [SVG illustration — category-specific, viewBox="0 0 180 140", rgba() colours only]
      </div>
    </div>
  </div>
</header>
```

**Byline rules:**
- Date: `D Mmm YYYY` — e.g. `1 Apr 2026` (no leading zero on day)
- Reading time: word count ÷ 200, rounded to nearest whole number
- Always "Founder &amp; Director" — never "Founder &amp; CEO"
- `sv-years-experience` span — never hardcode the number

---

## BREADCRUMB

```html
<nav aria-label="Breadcrumb" class="sv-breadcrumb">
  <div class="container">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/insights/">Insights</a></li>
      <li><a href="/insights/?category=[CATEGORY-SLUG]">[Category Name]</a></li>
      <li>[Article Title — matches H1 exactly]</li>
    </ul>
  </div>
</nav>
```

---

## KEY TAKEAWAYS BLOCK

```html
<div class="article-takeaways">
  <span class="article-takeaways-label">Key Takeaways</span>
  <ul>
    <li>[Fact — complete standalone sentence, under 30 words]</li>
    <li>[Fact]</li>
    <li>[Fact]</li>
    <li>[Fact]</li>
    <li>[Fact]</li>
    <li>[Fact]</li>
  </ul>
</div>
```

- 4 to 6 bullets
- Each bullet is a complete standalone fact readable without context
- Written so an AI can extract it as a direct answer to a search query
- No marketing language — factual statements only

---

## SECTIONS

```html
<section id="section1">
  <h2>1. Section Heading</h2>
  <p>[Opening paragraph]</p>
  <img src="/images/insights/[slug]-feature.webp"
    alt="[Descriptive alt text — Singapore context, no brand names]"
    class="article-img-float-right" />
  <p>[Body paragraphs]</p>
  <div class="callout-box">
    <p class="callout-label">KEY POINT</p>
    <p>[Key point — 2 to 4 sentences]</p>
  </div>
</section>
```

**Section rules:**
- `<section id="sectionN">` — sequential from 1
- `<h2>N. Section Heading</h2>` — numbered and scannable
- No H3 headings inside sections — prose only
- No bullet lists in article body prose
- At least one callout-box or verdict-box per section
- Feature image in section1 after first `<p>` — `article-img-float-right`, no wrapper, no caption
- Body images — `article-img-float-right`, no wrapper, no caption
- Never place `<img>` inside a `.callout-box` or `.verdict-box`

---

## CALLOUT BOX

```html
<div class="callout-box">
  <p class="callout-label">KEY POINT</p>
  <p>[2 to 4 sentences — key insight for this section]</p>
</div>
```

Labels (all caps): `KEY POINT` / `PLANNING POINT` / `DESIGN RULE` / `SINGAPORE CONTEXT`

---

## VERDICT BOX — SECUREVISION'S VIEW

```html
<div class="verdict-box">
  <p class="verdict-label">Securevision's View</p>
  <p>[3 to 5 sentences — "we" voice, specific professional opinion, committed position]</p>
</div>
```

Label is always exactly: `Securevision's View`
Never: "Securevision Verdict", "Securevision View", or any other variation.

---

## IN SHORT — MANDATORY END SUMMARY

Appears once after all content sections, before `<hr/>`:

```html
<div class="verdict-box">
  <p class="verdict-label">In Short</p>
  <p>[One paragraph — what the reader should take away from the entire article]</p>
</div>
```

---

## IMAGES

| Type | Size | Filename | Used in |
|---|---|---|---|
| Feature | 960×540px | `[slug]-feature.webp` | HTML body (section1), JSON-LD |
| OG | 1200×630px | `[slug]-feature-og.webp` | `og:image`, `twitter:image` only |
| Body | 800×500px | `[slug]-[descriptor].webp` | HTML body (sections 2+) |

- All stored in `/images/insights/`
- Class: `article-img-float-right` — no wrapper div, no caption, no inline styles
- Maximum 3 body images per article (feature counts as one)
- Alt text: descriptive, Singapore context, no brand names

**Anti-Gravity image rules:**
- Singapore setting, Asian faces on all people
- Securevision staff: white polo shirt, logo on left breast pocket, "SECUREVISION" on right sleeve
- Logo reference: `C:\Projects\SV-Build\images\securevision-logo-blue.png`
- No brand names on equipment
- WebP format, quality 85
- Never place images inside `.callout-box` or `.verdict-box`

---

## SHARE STRIP

```html
<div class="article-share">
  <span class="article-share-label">Share</span>
  <a class="share-btn share-btn-linkedin" id="shareLinkedIn" href="#" target="_blank" rel="noopener">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
    LinkedIn
  </a>
  <a class="share-btn share-btn-whatsapp" id="shareWhatsApp" href="#" target="_blank" rel="noopener">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
    WhatsApp
  </a>
  <button class="share-btn share-btn-copy" id="shareCopy" type="button">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    <span id="copyLabel">Copy Link</span>
  </button>
  <a class="share-btn share-btn-preferred"
    href="https://google.com/preferences/source?q=securevision.com.sg" target="_blank" rel="noopener">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
    Add to Google
  </a>
</div>
```

---

## AUTHOR ATTRIBUTION

```html
<div class="author-attribution">
  <img alt="Ler Wee Meng" class="author-attribution-img" src="/images/ler-wee-meng-bio.webp" />
  <div class="author-attribution-text">
    <strong>Ler Wee Meng</strong> — Founder &amp; Director, Securevision Pte Ltd.
    BEng (NUS) · LLB (University of London) · <span class="sv-years-experience"></span> years in security
    systems integration.
    <div class="author-attribution-links">
      <a href="https://www.linkedin.com/in/lerwm" rel="author" target="_blank">LinkedIn ↗</a>
      <a href="/about.html">About Securevision ↗</a>
    </div>
  </div>
</div>
```

Never use `author-bio-footer` — deprecated.

---

## ARTICLE TAGS

```html
<div class="article-tags">
  <a class="tag-pill" href="/insights/?category=[CATEGORY-SLUG]">[Category Name]</a>
  <a class="tag-pill" href="/insights/?tag=[tag1]">[Tag 1]</a>
  <a class="tag-pill" href="/insights/?tag=[tag2]">[Tag 2]</a>
  <a class="tag-pill" href="/insights/?tag=[tag3]">[Tag 3]</a>
  <a class="tag-pill" href="/insights/?tag=singapore">Singapore</a>
</div>
```

Maximum 5 tags. First = category link. Last = Singapore.
Tags must match `article:tag` meta values exactly.

---

## FAQ SECTION — MANDATORY

```html
<section id="section8">
  <h2>8. Frequently asked questions</h2>

  <p><strong>Question in natural conversational language?</strong></p>
  <p>Direct answer — first sentence answers the question, then expands.</p>

  <p><strong>Next question?</strong></p>
  <p>Answer.</p>

</section>
```

**FAQ rules:**
- 10 to 12 questions minimum
- Questions use natural conversational language — how a real person would type or speak
- Every answer opens with a direct response — never preamble before the answer
- Use `<p><strong>` for questions — never H3
- At least 2 Singapore-specific questions
- At least 1 definition question ("What is X?")
- FAQ is numbered sequentially after the last content section
- FAQ appears in HTML after share strip, author attribution, and tags

---

## SIDEBAR

```html
<aside>
  <div class="sidebar-container">
    <div class="sidebar-section">
      <span class="toc-title">In this article</span>
      <div class="toc-progress-wrap">
        <div class="toc-progress-track">
          <div class="toc-progress-fill" id="tocProgress"></div>
        </div>
      </div>
      <ul class="toc-list" id="tocList">
        <li><a href="#section1">1. Section heading</a></li>
        <li><a href="#section2">2. Section heading</a></li>
        ...
        <li><a href="#sectionN">N. FAQ</a></li>
      </ul>
    </div>
    <div class="sidebar-section sidebar-section--cta">
      <span class="sidebar-cta-label">[Category Name]</span>
      <p class="sidebar-cta-title">[Specific CTA title for this article]</p>
      <p class="sidebar-cta-desc">[One sentence — what we will do for them]</p>
      <a class="sidebar-cta-btn sidebar-cta-btn-primary"
         href="/request-proposal.html?intent=[specific-intent-slug]">Request a Proposal</a>
    </div>
  </div>
</aside>
```

Never use `sticky-toc` or `founder-card` — deprecated.

---

## RELATED INSIGHTS

```html
<section class="sv-section-grey section-spacing">
  <div class="container">
    <h2>Related Security Insights</h2>
    <div class="insights-related-grid" id="related-insights-grid"></div>
  </div>
</section>
```

Auto-populated by `nav-footer.js` from `site-config.js`. Never hardcode links here.

---

## FINAL CTA

```html
<section class="cta-section cta-high-impact cta-property">
  <div class="container">
    <h2>[Specific CTA headline for this article]</h2>
    <p class="subtitle">[One sentence — problem we solve, specific to this topic]</p>
    <div class="btn-group">
      <a class="btn btn-primary" href="/request-proposal.html">Request a Proposal</a>
      <a class="btn btn-outline-light" href="https://wa.me/6593860466">💬 WhatsApp</a>
    </div>
    <p class="cta-trust-note">Serving Singapore Since 2006 · Police Licensed · bizSAFE Level 3</p>
  </div>
</section>
```

CTA headline and subtitle must be specific to this article — never copied from another article.

---

## SCRIPTS

```html
<script>
  (function () {
    /* ── Share strip ── */
    (function () {
      var url = encodeURIComponent(window.location.href);
      var text = encodeURIComponent(document.title + ' — ' + window.location.href);
      var li = document.getElementById('shareLinkedIn');
      var wa = document.getElementById('shareWhatsApp');
      var cp = document.getElementById('shareCopy');
      if (li) li.href = 'https://www.linkedin.com/sharing/share-offsite/?url=' + url;
      if (wa) wa.href = 'https://wa.me/?text=' + text;
      if (cp) cp.addEventListener('click', function () {
        navigator.clipboard.writeText(window.location.href).then(function () {
          var label = document.getElementById('copyLabel');
          if (label) {
            label.textContent = 'Copied!';
            cp.classList.add('copied');
            setTimeout(function () {
              label.textContent = 'Copy Link';
              cp.classList.remove('copied');
            }, 2500);
          }
        });
      });
    })();

    /* ── TOC scroll-spy + progress bar ── */
    var tocLinks = document.querySelectorAll('.toc-list a');
    var progressFill = document.getElementById('tocProgress');
    var sections = [];
    tocLinks.forEach(function (link) {
      var id = link.getAttribute('href').replace('#', '');
      var el = document.getElementById(id);
      if (el) sections.push({ link: link, el: el });
    });
    function onScroll() {
      var scrollY = window.scrollY + 120;
      var active = null;
      sections.forEach(function (s) {
        if (s.el.offsetTop <= scrollY) active = s;
      });
      tocLinks.forEach(function (l) { l.classList.remove('active'); });
      if (active) active.link.classList.add('active');
      if (progressFill) {
        var docH = document.documentElement.scrollHeight - window.innerHeight;
        var pct = docH > 0 ? Math.min(100, Math.round((window.scrollY / docH) * 100)) : 0;
        progressFill.style.width = pct + '%';
      }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  })();
</script>
<script src="/nav-footer.js"></script>
```

`nav-footer.js` is always the last script tag before `</body>`.

---

## SITE-CONFIG.JS ENTRY

```js
{
  slug: "[slug]",
  title: "[H1 title — matches article H1 exactly]",
  category: "[Category display name — e.g. Access & Intercom]",
  date: "[YYYY-MM-DD]",
  tags: ["[tag1]", "[tag2]", "[tag3]", "singapore"],
  excerpt: "[140 to 200 characters — what the article is about, plain English]",
  image: "[slug]-feature.webp"
},
```

All 7 fields required. `title` must match H1. `image` is filename only, no path.

---

## CONTENT STANDARDS

**Voice:**
- Wee Meng's voice — direct, engineering-led, no marketing language
- "We" voice only inside Securevision's View boxes
- Secondary school reading level — define all technical terms
- No contractions: it's, don't, can't, won't, isn't

**Language:**
- British English throughout
- Key spellings: authorisation, centre, colour, licence (noun), recognised, organised

**Length and structure:**
- Full article: 1,500 to 2,500 words body prose
- Each section: 150 to 350 words
- No paragraph longer than 4 sentences
- Bold sparingly — only for terms being defined or critical warnings

**Accuracy:**
- Statistics softened unless from a named source ("significantly more likely" not "3× more likely")
- Singapore context throughout — HDB, landed, condo, MCST referenced where relevant
- No Dahua or Tiandy brand names anywhere
- No "Hikvision AcuSense" by name

**SEO / GEO / AEO / E-E-A-T:**
- Primary keyword in title tag, H1, first paragraph, and at least two H2s
- Key Takeaways written as direct answers to search queries
- Each Securevision's View box written as a citable professional opinion
- FAQ questions in natural conversational language
- FAQ answers open with a direct response

---

## POST-BUILD CHECKLIST

Before handing off for review:

- [ ] Run `INSTRUCTION-insights-audit.md` against the completed article
- [ ] Feature image (960×540) generated and inserted
- [ ] OG image (1200×630) generated — saved as `[slug]-feature-og.webp`
- [ ] `og:image` and `twitter:image` point to the OG version
- [ ] `site-config.js` entry added with all 7 fields
- [ ] Date in byline matches `article:published_time`
- [ ] Reading time calculated and correct
- [ ] After deploy — LinkedIn Post Inspector run on article URL

---

## WHAT CHANGED FROM v1.0 (April 2026)

| Old | New |
|---|---|
| 4 categories | 6 categories |
| `sv-guides.css` | `sv-insights.css` |
| `badge badge-primary` | `insights-cat-label` |
| `insights-header-intro` | `insights-header-subtitle` |
| `sticky-toc` + `founder-card` | `sidebar-container` + `sidebar-section--cta` |
| `author-bio-footer` | `author-attribution` |
| `article-image-box` with caption | `article-img-float-right` (no caption) |
| Inline styles on header | No inline styles |
| `og:image` 640×360 | `og:image` 1200×630 (`-feature-og.webp`) |
| No OG image distinction | Feature (960×540) vs OG (1200×630) |
| No FAQ | FAQ mandatory — 10 to 12 questions |
| No "In Short" box | "In Short" verdict box mandatory |
| No share strip | Share strip mandatory (4 buttons) |
| No Key Takeaways | Key Takeaways mandatory (4 to 6 bullets) |
| "Securevision Verdict" | "Securevision's View" |
| "Founder & CEO" | "Founder & Director" |
| No `excerpt` in site-config | `excerpt` field required |
| Google Fonts in head | No Google Fonts |
| Hardcoded years | `sv-years-experience` span |
| Related articles hardcoded | Auto-populated via nav-footer.js |

---

## PRE-PUBLISH AUDIT CHECKLIST

Run this against the completed article HTML before publishing.
Upload the article file and check every item.

**FAIL** = must fix before publishing.
**FLAG** = worth reviewing — may be a content or judgement call.
**PASS** = confirmed correct.

## SECTION A — FILE AND SETUP

- [ ] **A1** Filename follows `/insights/[slug].html` pattern — lowercase, hyphens only
- [ ] **A2** `<html lang="en-GB">` present
- [ ] **A3** `<body data-article="[slug]">` — slug matches `site-config.js` entry exactly
- [ ] **A4** CSS load order correct: `sv-shared.css` → `sv-insights.css` → `site-config.js`
- [ ] **A5** No Google Fonts `<link>` tag — fonts load via `sv-shared.css`
- [ ] **A6** No inline `<style>` blocks anywhere
- [ ] **A7** No inline `style=""` attributes (exception: `style="width:X%"` on `.toc-progress-fill` only)
- [ ] **A8** `<nav id="sv-nav"></nav>` present as first element after `<body>`
- [ ] **A9** `<footer id="sv-footer"></footer>` present before scripts
- [ ] **A10** `<script src="/nav-footer.js"></script>` is the last script tag

---

## SECTION B — META TAGS

- [ ] **B1** `<title>` — under 70 characters including " | Securevision"
- [ ] **B2** `meta name="description"` — present, under 160 characters, plain English
- [ ] **B3** `meta name="robots" content="index, follow"` — present
- [ ] **B4** `<link rel="canonical">` — absolute URL to `https://www.securevision.com.sg/insights/[slug].html`
- [ ] **B5** `og:type` = "article"
- [ ] **B6** `og:site_name` = "Securevision"
- [ ] **B7** `og:title` — present
- [ ] **B8** `og:description` — present, under 200 characters
- [ ] **B9** `og:url` — absolute URL, matches canonical exactly
- [ ] **B10** `og:image` — points to `[slug]-feature-og.webp` — NOT generic `securevision-insights.webp`
- [ ] **B11** `og:image:width` = 1200
- [ ] **B12** `og:image:height` = 630
- [ ] **B13** `article:author` = "Ler Wee Meng"
- [ ] **B14** `article:published_time` — present, format YYYY-MM-DD
- [ ] **B15** `article:section` — matches the article category exactly
- [ ] **B16** Minimum 4 × `article:tag` — must include "Singapore"
- [ ] **B17** `twitter:card` = "summary_large_image"
- [ ] **B18** `twitter:title` — present
- [ ] **B19** `twitter:description` — present
- [ ] **B20** `twitter:image` — matches `og:image` exactly (points to `-feature-og.webp`)

---

## SECTION C — STRUCTURED DATA

- [ ] **C1** JSON-LD block present in `<head>`
- [ ] **C2** `@type` = "Article"
- [ ] **C3** `headline` matches H1 exactly
- [ ] **C4** `image` points to `[slug]-feature.webp` (the regular feature — not the OG version)
- [ ] **C5** `datePublished` matches `article:published_time`
- [ ] **C6** `author.name` = "Ler Wee Meng"
- [ ] **C7** `author.url` = "https://www.securevision.com.sg/about.html"
- [ ] **C8** `publisher.name` = "Securevision Pte Ltd"
- [ ] **C9** `publisher.logo.url` = "https://www.securevision.com.sg/images/securevision-logo-blue.png"
- [ ] **C10** `mainEntityOfPage.@id` matches canonical URL

---

## SECTION D — HERO HEADER

- [ ] **D1** `<header class="insights-header insights-cat-[category]">` — correct category class
- [ ] **D2** No inline styles on `<header>`
- [ ] **D3** `<div class="insights-header-inner">` present
- [ ] **D4** `<div class="insights-header-left">` present
- [ ] **D5** `<span class="insights-cat-label">` — category display name present
- [ ] **D6** `<h1 class="insights-header-title">` — present
- [ ] **D7** `<p class="insights-header-subtitle">` — present (not `insights-header-intro`)
- [ ] **D8** `<div class="hero-byline">` present with author photo and name
- [ ] **D9** Byline role: "Founder &amp; Director" — not "Founder &amp; CEO"
- [ ] **D10** `<span class="sv-years-experience"></span>` in byline — not hardcoded
- [ ] **D11** Byline date format: `D Mmm YYYY` — e.g. `1 Apr 2026` (no leading zero)
- [ ] **D12** Reading time present in byline — `[N] min read`
- [ ] **D13** `<div class="insights-header-illus">` present with SVG illustration
- [ ] **D14** SVG uses `rgba()` colours — no hardcoded hex values

---

## SECTION E — BREADCRUMB

- [ ] **E1** `<nav aria-label="Breadcrumb" class="sv-breadcrumb">` present
- [ ] **E2** 4 crumbs: Home → Insights → [Category] → [Article Title]
- [ ] **E3** Last crumb (current page) matches H1 or a clear abbreviation of it
- [ ] **E4** Category crumb links to `/insights/?category=[category-slug]`
- [ ] **E5** No `trust-bar` between breadcrumb and article body

---

## SECTION F — ARTICLE STRUCTURE

- [ ] **F1** `<div class="article-body">` wraps the entire body + sidebar
- [ ] **F2** `<main class="prose">` wraps article content
- [ ] **F3** `<div class="article-takeaways">` present before section1
- [ ] **F4** Key Takeaways has 4 to 6 bullets
- [ ] **F5** Each takeaway is a standalone fact — no marketing language
- [ ] **F6** All sections use `<section id="sectionN">` with sequential numbering from 1
- [ ] **F7** Each section starts with `<h2>N. Section Title</h2>` — numbered
- [ ] **F8** No H3 headings inside sections — use prose paragraphs only
- [ ] **F9** At least one `callout-box` or `verdict-box` per section
- [ ] **F10** "In Short" verdict box present after all content sections, before `<hr/>`
- [ ] **F11** Footer order correct: In Short → `<hr/>` → share strip → author attribution → tags → FAQ

---

## SECTION G — IMAGES

- [ ] **G1** Feature image in section1 after the first `<p>` tag
- [ ] **G2** Feature image filename: `[slug]-feature.webp`
- [ ] **G3** Feature image class: `article-img-float-right` — no wrapper div, no caption
- [ ] **G4** All body images use `class="article-img-float-right"` — no inline styles
- [ ] **G5** No `<img>` inside any `.callout-box` or `.verdict-box`
- [ ] **G6** All images stored at `/images/insights/[filename]`
- [ ] **G7** Alt text present on all images — descriptive, Singapore context, no brand names
- [ ] **G8** No duplicate image filenames across sections
- [ ] **G9** Maximum 3 body images per article

---

## SECTION H — CALLOUT AND VERDICT BOXES

- [ ] **H1** Callout box uses `<div class="callout-box">` and `<p class="callout-label">`
- [ ] **H2** Callout label is all-caps: `KEY POINT` / `PLANNING POINT` / `DESIGN RULE` / `SINGAPORE CONTEXT`
- [ ] **H3** Verdict box uses `<div class="verdict-box">` and `<p class="verdict-label">`
- [ ] **H4** Verdict label is: `Securevision's View` — not "Securevision Verdict" or "Securevision View"
- [ ] **H5** "In Short" verdict box label is: `In Short`
- [ ] **H6** Verdict box content uses "we" voice — first person plural
- [ ] **H7** No `<img>` inside any callout or verdict box

---

## SECTION I — SHARE STRIP

- [ ] **I1** `<div class="article-share">` present after `<hr/>`
- [ ] **I2** `<span class="article-share-label">Share</span>` present
- [ ] **I3** LinkedIn share button present (`share-btn-linkedin`, `id="shareLinkedIn"`)
- [ ] **I4** WhatsApp share button present (`share-btn-whatsapp`, `id="shareWhatsApp"`)
- [ ] **I5** Copy Link button present (`share-btn-copy`, `id="shareCopy"`, `id="copyLabel"`)
- [ ] **I6** Add to Google button present — links to `google.com/preferences/source?q=securevision.com.sg`

---

## SECTION J — AUTHOR ATTRIBUTION

- [ ] **J1** `<div class="author-attribution">` present — NOT `author-bio-footer`
- [ ] **J2** Author photo present: `class="author-attribution-img"`
- [ ] **J3** Credentials: BEng (NUS) · LLB (University of London) · `sv-years-experience` span
- [ ] **J4** `sv-years-experience` span present — never hardcoded number
- [ ] **J5** LinkedIn link with `rel="author"` present
- [ ] **J6** About Securevision link to `/about.html` present

---

## SECTION K — ARTICLE TAGS

- [ ] **K1** `<div class="article-tags">` present after author attribution
- [ ] **K2** Maximum 5 tags
- [ ] **K3** First tag links to category (`/insights/?category=[slug]`)
- [ ] **K4** Singapore tag always present (`/insights/?tag=singapore`)
- [ ] **K5** Tags match `article:tag` meta values

---

## SECTION L — FAQ

- [ ] **L1** FAQ section present — `<section id="sectionN">` numbered sequentially after content sections
- [ ] **L2** FAQ H2 heading: `N. Frequently asked questions`
- [ ] **L3** Minimum 10 questions
- [ ] **L4** Questions use `<p><strong>[Question?]</strong></p>` — not H3
- [ ] **L5** Every answer opens with a direct response — no preamble
- [ ] **L6** At least 2 Singapore-specific questions
- [ ] **L7** At least 1 definition question ("What is X?")
- [ ] **L8** FAQ appears after share strip and author attribution in HTML source

---

## SECTION M — SIDEBAR

- [ ] **M1** `<div class="sidebar-container">` present — NOT `sticky-toc` or `founder-card`
- [ ] **M2** `<div class="sidebar-section">` for TOC block
- [ ] **M3** TOC progress bar present: `.toc-progress-wrap` → `.toc-progress-track` → `.toc-progress-fill`
- [ ] **M4** TOC entries numbered to match H2 section numbers
- [ ] **M5** TOC includes FAQ as final entry
- [ ] **M6** `<div class="sidebar-section sidebar-section--cta">` present
- [ ] **M7** Sidebar CTA title and description specific to this article topic
- [ ] **M8** Sidebar CTA links to `/request-proposal.html?intent=[specific-slug]`

---

## SECTION N — RELATED INSIGHTS AND FINAL CTA

- [ ] **N1** Related insights section uses `<div class="insights-related-grid" id="related-insights-grid">` — auto-populated
- [ ] **N2** No hardcoded article links in the related grid
- [ ] **N3** Final CTA headline specific to this article — not copied from another article
- [ ] **N4** CTA trust note: "Serving Singapore Since 2006 · Police Licensed · bizSAFE Level 3"

---

## SECTION O — SCRIPTS

- [ ] **O1** Share strip JS present and wires all 4 buttons from `window.location.href`
- [ ] **O2** TOC scroll-spy + progress bar JS present
- [ ] **O3** `<script src="/nav-footer.js"></script>` is the last tag before `</body>`
- [ ] **O4** No other custom JS blocks

---

## SECTION P — CONTENT QUALITY

- [ ] **P1** Voice — direct, engineering-led, no marketing language
- [ ] **P2** Reading level — secondary school. No unexplained jargon
- [ ] **P3** British English — authorisation, centre, colour, licence (noun), recognised
- [ ] **P4** No Dahua or Tiandy brand names
- [ ] **P5** No "Hikvision AcuSense" by name
- [ ] **P6** Word count 1,500 to 2,500 words
- [ ] **P7** No paragraph longer than 4 sentences
- [ ] **P8** Singapore context present — HDB/landed/condo/MCST referenced where relevant
- [ ] **P9** No contractions (it's, don't, can't, isn't)
- [ ] **P10** No bullet lists inside article body prose — prose only

---

## SECTION Q — SITE-CONFIG AND DEPLOYMENT

- [ ] **Q1** Article entry exists in `site-config.js`
- [ ] **Q2** `title` field matches H1 exactly
- [ ] **Q3** `category` field matches `article:section` exactly
- [ ] **Q4** `date` field matches `article:published_time`
- [ ] **Q5** `excerpt` field present — 140 to 200 characters
- [ ] **Q6** `image` field present — `[slug]-feature.webp` filename only (no path)
- [ ] **Q7** After deploy — LinkedIn Post Inspector run to confirm OG preview

---

## REPORT FORMAT

**FAILS (must fix before publishing):**
- [Item code] [Description of issue]

**FLAGS (review before publishing):**
- [Item code] [Description of issue]

**PASS:** All other items confirmed correct.
