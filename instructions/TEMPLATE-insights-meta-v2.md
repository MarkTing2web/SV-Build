# Insights Article Meta Block Template
## Securevision — Copy into every new insights article `<head>`
## Version 2.0 — June 2026
## Replace ALL values in [SQUARE BRACKETS] before deploying

```html
  <!-- ═══ SEO — UPDATE ALL FIELDS PER ARTICLE ═══ -->
  <title>[ARTICLE TITLE] | Securevision</title>
  <meta
    content="[META DESCRIPTION — max 160 characters, plain English, what the reader will learn]"
    name="description" />
  <meta name="robots" content="index, follow" />
  <link href="https://www.securevision.com.sg/insights/[SLUG].html" rel="canonical" />

  <!-- Open Graph -->
  <meta content="article" property="og:type" />
  <meta content="Securevision" property="og:site_name" />
  <meta content="[ARTICLE TITLE]" property="og:title" />
  <meta
    content="[OG DESCRIPTION — max 200 characters, written to make someone want to click]"
    property="og:description" />
  <meta content="https://www.securevision.com.sg/insights/[SLUG].html" property="og:url" />
  <meta content="https://www.securevision.com.sg/images/insights/[SLUG]-feature-og.webp"
    property="og:image" />
  <meta content="1200" property="og:image:width" />
  <meta content="630" property="og:image:height" />

  <!-- Article metadata -->
  <meta content="Ler Wee Meng" property="article:author" />
  <meta content="[YYYY-MM-DD]" property="article:published_time" />
  <meta content="[CATEGORY — e.g. Alarm &amp; Intrusion]" property="article:section" />
  <meta content="[TAG 1]" property="article:tag" />
  <meta content="[TAG 2]" property="article:tag" />
  <meta content="[TAG 3]" property="article:tag" />
  <meta content="Singapore" property="article:tag" />

  <!-- Twitter/X Card — also used by Slack, Telegram, Discord and AI crawlers -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="[ARTICLE TITLE]" />
  <meta name="twitter:description"
    content="[META DESCRIPTION — same as above]" />
  <meta name="twitter:image"
    content="https://www.securevision.com.sg/images/insights/[SLUG]-feature-og.webp" />

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "[H1 TITLE — matches article H1 exactly]",
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
  <!-- ════════════════════════════════════════════ -->
  <link href="/sv-shared.css" rel="stylesheet" />
  <link href="/sv-insights.css" rel="stylesheet" />
  <script src="/site-config.js"></script>
```

---

## Field Reference

| Field | What to put |
|---|---|
| `[ARTICLE TITLE]` | The title as it appears in the browser tab — under 70 chars including " \| Securevision" |
| `[SLUG]` | Filename without `.html` — e.g. `standalone-door-access` |
| `[META DESCRIPTION]` | Plain English, max 160 chars. What the reader will learn. |
| `[OG DESCRIPTION]` | Max 200 chars. Written to make someone click the share card preview. Can differ from meta description. |
| `[H1 TITLE]` | The article H1 — can differ from the title tag. What the reader sees on the page. |
| `[YYYY-MM-DD]` | Publication date — e.g. `2026-04-01` |
| `[CATEGORY]` | One of the 6 insight categories — see below |
| `[TAG 1–3]` | 3 topic tags — use terms people search for. Always include Singapore as the 4th. |

---

## Category values (article:section)

| Category | Value to use in meta tag |
|---|---|
| Alarm & Intrusion | `Alarm &amp; Intrusion` |
| CCTV & Surveillance | `CCTV &amp; Surveillance` |
| Access & Intercom | `Access &amp; Intercom` |
| Vehicle & Gates | `Vehicle &amp; Gates` |
| Platform & Integration | `Platform &amp; Integration` |
| Security Planning | `Security Planning` |

---

## Image rules

| Image | Size | Filename | Used in |
|---|---|---|---|
| Feature image | 960×540px | `[slug]-feature.webp` | HTML body (`article-img-float-right`), JSON-LD |
| OG image | 1200×630px | `[slug]-feature-og.webp` | `og:image`, `twitter:image` |

- Both stored in `/images/insights/`
- OG image is a centre-cropped version of the feature image
- `og:image` and `twitter:image` always point to the `-feature-og.webp` version
- JSON-LD `"image"` points to the regular `-feature.webp`
- Neither image is the generic `securevision-insights.webp` — that is for the index page only

---

## Checklist before publishing

- [ ] Title under 70 characters total including " | Securevision"
- [ ] Meta description under 160 characters
- [ ] Canonical URL matches the actual page URL exactly
- [ ] `og:image` points to `[slug]-feature-og.webp` — not the generic image, not the regular feature
- [ ] `og:image:width` = 1200, `og:image:height` = 630
- [ ] `twitter:image` matches `og:image` exactly
- [ ] JSON-LD `"image"` points to `[slug]-feature.webp` (not the OG version)
- [ ] `article:published_time` is the actual publish date in YYYY-MM-DD
- [ ] `article:section` matches the category in site-config.js
- [ ] Minimum 4 `article:tag` values — always include Singapore
- [ ] JSON-LD `headline` matches the article H1 exactly
- [ ] JSON-LD `datePublished` matches `article:published_time`
- [ ] Run LinkedIn Post Inspector after deploy to confirm OG preview
