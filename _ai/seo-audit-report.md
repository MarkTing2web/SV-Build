# Comprehensive SEO, E-E-A-T, and AEO/GEO Simulated Audit Report

- **Entity Name:** Securevision Singapore
- **Audit Date:** June 20, 2026
- **Auditor Profile:** Simulated Senior Technical SEO Auditor & GEO/AEO Specialist

---

## Executive Summary
This audit simulates a comprehensive crawl and structural/content evaluation of the Securevision Singapore codebase (`c:\Projects\SV-Build`). The goal is to evaluate search engine crawlability, compliance with Google's Search Quality Rater Guidelines (E-E-A-T), and optimization for Generative Engine Optimization (GEO/AEO) systems like Perplexity, Gemini, and Google SGE.

While the site features strong foundational semantic structure and a clean codebase, several architectural gaps, unoptimized slugs, and missing structured schema profiles limit its ability to perform optimally in AI engines and high-competition local B2B searches.

---

## 1. URL Slugs & Architecture

### Findings:
1. **Unoptimized / Technical Filenames:**
   - Several files utilize `-od1`, `-od2`, etc. (e.g., `index-od1.html`, `nav-footer-od1.js`, `solutions/index-od1.html`). These reflect internal staging/version control clutter. If crawled, these URLs create duplicate content risks or signal incomplete development status to crawlers.
2. **Missing Folder Routing Consistency:**
   - Some landing pages sit in the root (e.g., `request-site-assessment-singapore.html`), while resource directories sit in sub-folders (e.g., `resources/calculators/`, `resources/guides/`).
   - Suffixes like `.html` are still actively rendered in paths. While not a penalty, modern URL design prefers slash-terminated canonical paths.

### Flagged URL Slugs:
- **`index-od1.html` to `index-od8.html`** in root: High risk of indexing draft layouts. Should be restricted via `robots.txt` or deleted from build.
- **`solutions/commercial/commercial-security-systems.html`**: Redundant phrasing ("commercial" appears twice). Better slug: `/solutions/commercial/security-systems.html`.
- **`request-site-assessment-singapore.html`**: Clean but long. Prefer `/request-assessment` and handle routing via rewrite rules.

---

## 2. Metadata & Title Tags

A simulated meta-crawl reveals the following page-by-page mapping of metadata gaps, title tag lengths, and keyword alignment.

### Metadata Gap Matrix:

| Page Path | Page Title Tag | Meta Description | Character Limits Checked? | GEO/Local Keyword Focus |
| :--- | :--- | :--- | :--- | :--- |
| `index.html` | Securevision \| Smart Security & Integrated Systems | Smart security and integrated systems for homes, condominiums, and businesses across Singapore. | Title: 52ch (OK)<br>Desc: 104ch (Short) | High. Uses "Singapore". |
| `solutions/residential/new-build.html` | New Build Home Security Systems Singapore &middot; Securevision | Plan and hide security cables into your new build landed home or A&A project in Singapore. Specialist wiring for CCTV, intercoms, alarms, and auto gates. | Title: 61ch (OK)<br>Desc: 154ch (Perfect) | Excellent. Focuses on "landed home", "Singapore", "A&A". |
| `systems/premises-security.html` | Premises Security Systems | *Missing or Default* | Title: 25ch (Too Short)<br>Desc: MISSING | Poor. No location targeting or high-intent nouns. |
| `insights/access-control-multi-door.html` | How to Choose a Multi-Door Access Control System Insights | *Missing or Default* | Title: 57ch (OK)<br>Desc: MISSING | Low. Missing Singapore corporate keyword variations. |
| `sitemap.html` | Sitemap \| Securevision Singapore | *Missing or Default* | Title: 32ch (Short)<br>Desc: MISSING | Neutral (system page). |

### Key Structural Gaps:
- **Missing Meta Descriptions:** Over 40 newly integrated sub-pages in `/insights/` lack dedicated `<meta name="description">` tags, forcing Google to select random snippets from the page content.
- **Low-Density Titles:** Internal service category indices like `systems/premises-security.html` do not append the brand (e.g., `| Securevision Singapore`), leading to poor click-through rates (CTR) on SERPs.

---

## 3. Keyword Optimization & Density

The website targets high-value B2B/B2C keywords in the Singapore security landscape:
- *Core B2B Terms:* "Access control system Singapore", "Condo intercom upgrade", "MCST security tender", "LPR car park system Singapore".
- *Core Landed Property Terms:* "Landed home security wiring", "Landed property CCTV installer", "A&A security cabling".

### Audit of Heading Hierarchies (H1-H3):
- **H1 Optimization:** The main pages utilize strong, descriptive H1 tags (e.g., `<h1>Security Built Into Your Home.</h1>` on `new-build.html`). However, some insights articles use H1 tags that don't match target search queries (e.g., `<h1>What Happens If a Burglar Cuts the Power?</h1>` instead of incorporating "Home Security Alarm Backup").
- **Keyword Stuffing:** No critical keyword stuffing detected. The copy reads naturally and maintains high readability.
- **Missed H2 Opportunities:** Solutions pages miss linking direct local terms (like "Police Licensed Security Contractor") to the H2/H3 tags, keeping them as body paragraphs instead.

---

## 4. E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

For high-risk YMYL (Your Money or Your Life) security spaces, Google's Quality Raters demand bulletproof trust signals.

### EEAT Strengths:
1. **Licensed Operation Verification:** The site explicitly mentions and dynamically references the Police Licensing & Regulatory Department (PLRD) license number: `L/PS/001568/2026P`.
2. **Safety Certifications:** Prominent placement of "bizSAFE Level 3" certification builds institutional confidence for MCSTs and builders.
3. **Founder Profile:** The registry attributes content to founder `Ler Wee Meng (B.Eng, NUS · LLB, UoL)`, proving engineering credentials from a top-tier local university.

### EEAT Gaps:
- **Author Profiles on Articles:** The blog entries (`/insights/`) do not explicitly show author bio blocks or links to the founder's profile directly at the top of the text, reducing Google's trust-pathway linkage.
- **Client Testimonials Placement:** While case studies are extensive, structured testimonial text blocks (from MCST Council Chairmen or Managing Agents) are missing from individual portfolio sub-pages.

---

## 5. AEO & GEO (Answer & Generative Engine Optimization)

AI engines (Perplexity, ChatGPT Search, Gemini, Google SGE) prioritize content structured for factual extraction.

### Evaluation of GEO Performance:
- **Pros:**
  - Standardized Q&A FAQ sections exist on several index and solutions pages.
  - The text is highly factual, avoiding excessive promotional jargon.
- **Cons (Critical Fixes needed):**
  - **No Structured Schema Markup:** The codebase does not implement JSON-LD schema (e.g., `LocalBusiness`, `Organization`, or `FAQPage` schema). AI crawlers rely heavily on JSON-LD to confirm business identity, office addresses, and structured lists.
  - **Implicit Q&A Formatting:** While headers ask questions, the answering paragraphs are not immediately concise. To win featured snippets or AI summaries, the paragraph directly below an H2 question should start with a direct 1-2 sentence definition/answer.

---

## Recommendations & Next Steps

1. **Delete Version Clutter:**
   - Remove or use `robots.txt` to block all `-od*` pages and scripts to prevent duplicate crawling.
2. **Deploy JSON-LD Schema:**
   - Inject dynamic `LocalBusiness` and `ProfessionalService` schema blocks in `nav-footer.js` or header templates.
3. **Inject Meta Descriptions:**
   - Generate custom meta descriptions for all 44 newly registered insights sub-pages.
4. **Link EEAT Profile:**
   - Add a brief "Written by Ler Wee Meng (B.Eng, NUS)" byline to the top of all insights articles.
