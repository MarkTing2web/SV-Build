# Securevision Full Site Audit — Executive Summary
**Date:** June 07, 2026
**Audited by:** Gemini Antigravity
**Total pages audited:** 227
**Total issues found:** 3650 — Critical: 202 | High: 2950 | Medium: 486 | Low: 12

---

## Top Systemic Issues
- **RULE 9 - CTA label is "Book a Site Assessment" — should be "Request a Proposal" (or is non-canonical)** (Found on 160 pages)
- **RULE 4 - No recognised hero height class present** (Found on 153 pages)
- **RULE 5 - Hardcoded licence in trust bar or missing .sv-licence** (Found on 151 pages)
- **RULE 5 - Trust bar text deviating from canonical format** (Found on 151 pages)
- **RULE 12 - <title> missing 'Singapore'** (Found on 106 pages)
- **RULE 2 - Inline style found on <svg>: width: 14px; height: 14px; display: inline-block; vertical-align: middle; margin-right: 4px;** (Found on 101 pages)
- **RULE 2 - Inline style found on <p>: font-size: 0.8rem; color: #3182ce; font-weight: 700; margin-top: 12px;** (Found on 86 pages)
- **RULE 3 - Missing @media mobile hero override in <style> block** (Found on 76 pages)
- **RULE 3 - Missing :root { --page-accent } in style block** (Found on 75 pages)
- **RULE 16 - Hardcoded '2026' found instead of dynamic class .sv-current-year** (Found on 58 pages)

---

## Issues by Section

| Section | Pages | Critical | High | Medium | Low | Total |
|---|---|---|---|---|---|---|
| Root | 8 | 14 | 77 | 14 | 1 | 106 |
| Solutions | 42 | 43 | 591 | 62 | 2 | 698 |
| Systems | 7 | 7 | 78 | 18 | 0 | 103 |
| Brands | 39 | 42 | 496 | 99 | 1 | 638 |
| Portfolio | 53 | 54 | 921 | 105 | 2 | 1082 |
| Insights | 44 | 4 | 415 | 97 | 1 | 517 |
| Resources | 34 | 38 | 372 | 91 | 5 | 506 |
| **TOTAL** | 227 | 202 | 2950 | 486 | 12 | 3650 |

---

## Recommended Fix Order
1. Fix CRITICAL layout script dependencies (missing/hardcoded nav/footer placeholders).
2. Fix CRITICAL SEO issues (missing titles, canonicals).
3. Standardise RULE 2 Inline Styles across Brands pages.
4. Normalise CSS Load Order (RULE 1) across all sections.
5. Standardise CTA labels across section hubs and portfolio pages.
