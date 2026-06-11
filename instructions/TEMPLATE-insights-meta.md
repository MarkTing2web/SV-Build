# Insights Article Meta Block Template
## Securevision — Copy into every new insights article `<head>`
## Replace ALL values in [SQUARE BRACKETS] before deploying

```html
<!-- ═══ SEO — UPDATE ALL FIELDS PER ARTICLE ═══ -->
<title>[ARTICLE TITLE] | Securevision Insights</title>
<meta content="[META DESCRIPTION — max 155 characters, plain English summary of the article]" name="description"/>
<meta name="robots" content="index, follow"/>
<link href="https://www.securevision.com.sg/insights/[SLUG].html" rel="canonical"/>

<!-- Open Graph -->
<meta content="article" property="og:type"/>
<meta content="Securevision" property="og:site_name"/>
<meta content="[ARTICLE TITLE] | Securevision Insights" property="og:title"/>
<meta content="[OG DESCRIPTION — max 200 characters, compelling summary for social share preview]" property="og:description"/>
<meta content="https://www.securevision.com.sg/insights/[SLUG].html" property="og:url"/>
<meta content="https://www.securevision.com.sg/images/insights/[SLUG]-feature.webp" property="og:image"/>
<meta content="640" property="og:image:width"/>
<meta content="360" property="og:image:height"/>

<!-- Article metadata -->
<meta content="Ler Wee Meng" property="article:author"/>
<meta content="[YYYY-MM-DD]" property="article:published_time"/>
<meta content="[CATEGORY — e.g. Alarm &amp; Intrusion]" property="article:section"/>
<meta content="[TAG 1]" property="article:tag"/>
<meta content="[TAG 2]" property="article:tag"/>
<meta content="[TAG 3]" property="article:tag"/>
<meta content="Singapore" property="article:tag"/>

<!-- Twitter/X Card — also used by Slack, Telegram, Discord and AI crawlers -->
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="[ARTICLE TITLE]"/>
<meta name="twitter:description" content="[META DESCRIPTION — same as above]"/>
<meta name="twitter:image" content="https://www.securevision.com.sg/images/insights/[SLUG]-feature.webp"/>
<!-- ════════════════════════════════════════════ -->
```

---

## Field Reference

| Field | What to put |
|---|---|
| `[ARTICLE TITLE]` | Short article title — no site name suffix in Twitter tag |
| `[SLUG]` | The filename without `.html` — e.g. `burglar-alarm-design` |
| `[META DESCRIPTION]` | Plain English, max 155 chars. Should describe what the reader will learn. |
| `[OG DESCRIPTION]` | Slightly longer, max 200 chars. Written to make someone want to click the link preview. |
| `[YYYY-MM-DD]` | Publication date — e.g. `2026-04-01` |
| `[CATEGORY]` | One of the 6 insight categories — see below |
| `[TAG 1–3]` | 3 topic tags — use terms people search for |

## Category values (article:section)

| Category | Value to use |
|---|---|
| Alarm & Intrusion | `Alarm &amp; Intrusion` |
| CCTV & Surveillance | `CCTV &amp; Surveillance` |
| Access & Intercom | `Access &amp; Intercom` |
| Vehicle & Gates | `Vehicle &amp; Gates` |
| Platform & Integration | `Platform &amp; Integration` |
| Security Planning | `Security Planning` |

## OG image rule

- Always 640×360px, saved as `.webp`
- Stored at `/images/insights/[SLUG]-feature.webp`
- Must exist before the article is published — do not leave pointing to `securevision-insights.webp`

## Checklist before publishing

- [ ] Title under 60 characters (check in browser tab — truncates at ~60)
- [ ] Meta description under 155 characters
- [ ] Canonical URL matches the actual page URL exactly
- [ ] OG image file exists at the stated path
- [ ] article:published_time is the actual publish date
- [ ] At least 3 article:tag values set
- [ ] Run through LinkedIn Post Inspector after deploy to force OG cache refresh
