# INSTRUCTION — Building a New Securevision Insights Article
## Use this at the start of every new insights article session
## Version 1.0 — June 2026

---

## CONTEXT — What is already done for you

The following are fully defined in the CSS and JS files. You do not need to think about them. Do not redefine, override or recreate any of these.

| Element | Defined in |
|---|---|
| Two-row black nav (desktop + mobile) | `nav-footer.js` + `sv-shared.css` |
| Floating WhatsApp button | `nav-footer.js` |
| Footer | `nav-footer.js` |
| Related articles cards (auto-populated) | `nav-footer.js` + `site-config.js` |
| Active nav state | `nav-footer.js` |
| Dynamic values (years experience, licence, sites) | `site-config.js` |
| Hero — Night Watch Navy gradient, dot pattern | `sv-insights.css` |
| Category pill colours (6 categories) | `sv-insights.css` |
| Hero title, subtitle, byline layout | `sv-insights.css` |
| Article body layout, sidebar, TOC styling | `sv-insights.css` |
| Prose typography, headings, blue tick lists | `sv-insights.css` |
| Key takeaways block styling | `sv-insights.css` |
| Callout box, verdict box styling | `sv-insights.css` |
| Share strip styling | `sv-insights.css` |
| Author attribution styling | `sv-insights.css` |
| Float image with text wrap + 991px mobile reset | `sv-insights.css` |
| Related article card styling | `sv-insights.css` |
| Sidebar CTA styling | `sv-insights.css` |
| Breadcrumb styling | `sv-shared.css` |

---

## WHAT YOU MUST PROVIDE PER ARTICLE

### 1. File setup
- Filename: `/insights/[slug].html`
- `<body data-article="[slug]">` — slug must match `site-config.js` entry exactly
- CSS loads: `sv-shared.css` then `sv-insights.css` then `site-config.js` — in that order, no others unless needed
- No Google Fonts `<link>` tag — fonts load via `sv-shared.css`

### 2. Meta tags
Use `TEMPLATE-insights-meta.md` for the complete block. Fill in every `[SQUARE BRACKET]` field:
- `<title>` — article title + " | Securevision Insights" — under 60 characters
- `meta description` — plain English, under 155 characters
- `robots` — always `index, follow`
- `canonical` — full absolute URL
- All Open Graph tags including `og:image:width` (640) and `og:image:height` (360)
- `article:author`, `article:published_time`, `article:section`, 4× `article:tag`
- Twitter/X Card tags — also read by Slack, Telegram, Discord and AI crawlers
- OG image must point to the article feature image — never the generic `securevision-insights.webp`

### 3. JSON-LD structured data
Add this block in `<head>` after the meta tags. Fill in all fields:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[ARTICLE TITLE]",
  "description": "[META DESCRIPTION]",
  "image": "https://www.securevision.com.sg/images/insights/[SLUG]-feature.webp",
  "author": {
    "@type": "Person",
    "name": "Ler Wee Meng",
    "url": "https://www.linkedin.com/in/lerwm"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Securevision",
    "url": "https://www.securevision.com.sg"
  },
  "datePublished": "[YYYY-MM-DD]",
  "mainEntityOfPage": "https://www.securevision.com.sg/insights/[SLUG].html"
}
</script>
```

### 4. Hero header
```html
<header class="insights-header insights-cat-[CATEGORY]">
```
Category classes — use exactly one:
- `insights-cat-alarm` — Alarm & Intrusion (red pill)
- `insights-cat-cctv` — CCTV & Surveillance (blue pill)
- `insights-cat-access` — Access & Intercom (teal pill)
- `insights-cat-vehicle` — Vehicle & Gates (amber pill)
- `insights-cat-platform` — Platform & Integration (purple pill)
- `insights-cat-planning` — Security Planning (slate pill)

Hero must contain:
- `<span class="insights-cat-label">` — category display name
- `<h1 class="insights-header-title">` — article title (max 7 words, catchy)
- `<p class="insights-header-subtitle">` — subtitle (max 10 words)
- Hero byline with `<span class="sv-years-experience"></span>` — never hardcode the number
- SVG illustration — use the category SVG from the burglar alarm article as reference. Each category has its own SVG. Same SVG used across all articles in that category.

### 5. Breadcrumb
```html
<li><a href="/insights/?category=[CATEGORY-SLUG]">Category Name</a></li>
<li>[ARTICLE TITLE — must match H1 exactly]</li>
```
Category slugs:
- `alarm-intrusion` / `cctv-surveillance` / `access-intercom`
- `vehicle-gates` / `platform-integration` / `security-planning`

### 6. Article structure — fixed order
```
Key Takeaways block          (GEO/AEO optimised — 4 to 6 bullets)
Section 1 (id="section1")
Section 2 (id="section2")
...
Section N (id="sectionN")
<hr/>
Share strip HTML
Author attribution
Article tags
```

### 7. Key Takeaways block
```html
<div class="article-takeaways">
  <span class="article-takeaways-label">Key Takeaways</span>
  <ul>
    <li>...</li>
  </ul>
</div>
```
- 4 to 6 bullets
- Each bullet is a complete, standalone fact — readable without context
- Written so an AI can extract it as a direct answer to a search query
- No marketing language — factual statements only

### 8. Sections
- Each section has `<section id="sectionN">` where N is sequential from 1
- Each section starts with `<h2>N. Section Title</h2>`
- Each section ends with either a `callout-box` or `verdict-box`
- Callout box labels: KEY POINT / PLANNING POINT / DESIGN RULE / SINGAPORE CONTEXT
- Verdict box label: Securevision Verdict — always "we" voice, Securevision's professional opinion
- Minimum 1 callout or verdict per section

### 9. Inline summary blocks
Three layers — all three must be present across the article:

**Layer 1 — Key Takeaways** (top of article): GEO/AEO snippet for AI systems

**Layer 2 — Callout boxes** (mid-section): reinforce the main argument for skimmers
```html
<div class="callout-box">
<p class="callout-label">KEY POINT</p>
<p>...</p>
</div>
```

**Layer 3 — Verdict boxes** (end of sections): Securevision's professional opinion
```html
<div class="verdict-box">
<p class="verdict-label">Securevision Verdict</p>
<p>...</p>
</div>
```

### 10. Images
- Every article needs a feature image: `[slug]-feature.webp` at 640×360px
- Feature image goes in `section1` immediately after the opening paragraph
- Body images: 320×240px, `article-img-float-right` class, float right with text wrapping
- All images stored in `/images/insights/`
- Naming convention: `[slug]-[descriptor].webp` — e.g. `burglar-alarm-pir-detector.webp`
- All Securevision staff wear white polo shirt with logo from `/images/securevision-logo-blue.png` on breast pocket and SECUREVISION on sleeve
- Generate via Anti-Gravity using `AG-[slug]-images.md` instruction brief
- STOP for review after each image before inserting

### 11. Share strip HTML
Copy this block verbatim into every article between `<hr/>` and author attribution:
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
  <a class="share-btn share-btn-preferred" href="https://google.com/preferences/source?q=securevision.com.sg" target="_blank" rel="noopener">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
    Add to Google
  </a>
</div>
```

### 12. Share JS
Copy this block verbatim into the `<script>` block, before the TOC scroll-spy code:
```js
/* ── Share strip ── */
(function () {
  var url   = encodeURIComponent(window.location.href);
  var text  = encodeURIComponent(document.title + ' — ' + window.location.href);
  var li    = document.getElementById('shareLinkedIn');
  var wa    = document.getElementById('shareWhatsApp');
  var cp    = document.getElementById('shareCopy');
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
```

### 13. TOC scroll-spy JS
Copy verbatim from `burglar-alarm-design.html` — the block starting with `/* ── TOC scroll-spy + progress bar ── */`.

### 14. Author attribution
Copy verbatim — `sv-years-experience` spans must be present, never hardcoded:
```html
<div class="author-attribution">
<img alt="Ler Wee Meng" class="author-attribution-img" src="/images/ler-wee-meng-bio.webp"/>
<div class="author-attribution-text">
<strong>Ler Wee Meng</strong> — Founder &amp; Director, Securevision Pte Ltd.
BEng (NUS) · LLB (University of London) · <span class="sv-years-experience"></span> years in security systems integration.
<div class="author-attribution-links">
<a href="https://www.linkedin.com/in/lerwm" rel="author" target="_blank">LinkedIn ↗</a>
<a href="/about.html">About Securevision ↗</a>
</div>
</div>
</div>
```

### 15. Article tags
Match exactly the `article:tag` meta values. Use category link and 3 topic links:
```html
<div class="article-tags">
<a class="tag-pill" href="/insights/?category=[CATEGORY-SLUG]">[Category Name]</a>
<a class="tag-pill" href="/insights/?tag=[tag1]">[Tag 1]</a>
<a class="tag-pill" href="/insights/?tag=[tag2]">[Tag 2]</a>
<a class="tag-pill" href="/insights/?tag=singapore">Singapore</a>
</div>
```

### 16. Sidebar
```html
<div class="sidebar-section sidebar-section--cta">
  <span class="sidebar-cta-label">[Category Name]</span>
  <p class="sidebar-cta-title">[Specific CTA title for this article]</p>
  <p class="sidebar-cta-desc">[One sentence — what we will do for them]</p>
  <a class="sidebar-cta-btn sidebar-cta-btn-primary"
     href="/request-proposal.html?intent=[INTENT-SLUG]">Request a Proposal</a>
</div>
```
Intent slug must be specific to the article topic — e.g. `alarm-design-review`, `cctv-selection`, `access-audit`.

### 17. Final CTA section
Tailor H2 and subtitle to the article topic. Never copy the burglar alarm version verbatim:
```html
<section class="cta-section cta-high-impact cta-property">
<div class="container">
<h2>[Specific CTA headline for this article]</h2>
<p class="subtitle">[One sentence — the problem we solve, specific to article topic]</p>
<div class="btn-group">
<a class="btn btn-primary" href="/request-site-assessment-singapore.html">Book a Site Assessment</a>
<a class="btn btn-outline-light" href="/request-proposal.html">Request a Proposal</a>
<a class="btn btn-outline-light" href="https://wa.me/6593860466">💬 WhatsApp</a>
</div>
<p class="cta-trust-note">Serving Singapore Since 2006 · Police Licensed · bizSAFE Level 3</p>
</div>
</section>
```

### 18. site-config.js update
Add `image` field to the article entry:
```js
{ slug: "[slug]", title: "...", category: "...", tags: [...], image: "[slug]-feature.webp" },
```
Without this the related article cards on other pages will not show the feature image.

### 19. Reading time
Calculate: word count ÷ 200 = minutes (round to nearest whole number).
Update in hero byline: `· [N] min read`

---

## CONTENT STANDARDS — apply to every article

### Voice
- Wee Meng's voice — direct, no-nonsense, engineering-led
- "We" voice only inside Verdict boxes — neutral informational tone everywhere else
- No marketing language, no superlatives, no generic AI filler
- Secondary school reading level — if a 15-year-old in Singapore can't understand it, rewrite it
- Replace jargon with plain English. If a technical term is unavoidable, explain it in one sentence

### Structure
- Title: max 7 words, catchy, captures the article's core argument
- Subtitle: max 10 words, tells the reader what they will learn
- Each section starts with an H2 heading — numbered, clear, scannable
- Each paragraph covers one idea only
- No paragraph longer than 4 sentences
- Bold is used sparingly — only for terms being defined or critical warnings

### Word limits
- Each section: 150 to 300 words
- Full article: 1,500 to 2,500 words
- Key Takeaways: 4 to 6 bullets, each under 25 words
- Callout box: 2 to 4 sentences
- Verdict box: 3 to 5 sentences

### Accuracy
- All statistics must be softened unless from a named source — "significantly more likely" not "3× more likely"
- Singapore context throughout — reference HDB, landed, condo, MCST where relevant
- No brand names in editorial content except AJAX (approved)
- No Dahua or Tiandy brand names anywhere
- All factual claims must be verifiable from professional practice

### SEO and GEO
- Primary keyword in H1, first paragraph and at least two H2 headings
- Secondary keywords in H3 headings and naturally in body text
- Key Takeaways written as direct answers to search queries — AI systems extract these
- Each Verdict box written as a citable professional opinion
- No keyword stuffing — if it reads unnaturally, remove it

### British English
Always. Key spellings: authorisation, optimisation, labour, centre, programme, defence, licence (noun), licensing (verb), modelling, recognised, organised.

---

## POST-BUILD CHECKLIST

Before handing off for review:
- [ ] `INSTRUCTION-insights-audit.md` run against the completed article
- [ ] Feature image generated, reviewed and inserted
- [ ] OG image path points to article feature image (not generic)
- [ ] `site-config.js` entry updated with `image` field
- [ ] LinkedIn Post Inspector run after deploy

---

*Save this file as `/_instructions/INSTRUCTION-insights-build.md` in the repo.*
*Use alongside `GLOBAL-INSTRUCTION.md` and `TEMPLATE-insights-meta.md`.*
