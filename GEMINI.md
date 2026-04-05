⚠️ CRITICAL RULES — apply to every session without exception

1. NEVER write inline <style> blocks. All CSS is in external files (sv-shared.css, sv-guides.css, sv-forms.css). The only permitted exception is a single :root { --primary-access: #hex; } accent override block.

2. NEVER create new CSS class names. Reuse existing classes from the CSS files only. If a style is missing, add a comment <!-- NEEDS CSS: description --> and stop. Do not solve it inline.

3. NEVER rewrite the NAV or FOOTER HTML. They are frozen components. Copy them verbatim from the template file in /_templates/. Do not rephrase, reorder, or improve them.

4. NEVER change any href URLs in the nav or footer. All URLs are canonical and must not be altered.

5. ALWAYS use the correct template file from /_templates/ as the starting skeleton. Fill in content only — do not rebuild structure from scratch.

6. NEVER use HTML entities (&amp; &#9662; &rarr; etc.) where plain Unicode characters work. Use → · ▾ & " directly. Re-encoding entities is the primary cause of mojibake on this site.

7. PARTIAL UPDATES ONLY — when asked to update one section, touch only that section. Do not reformat, re-space, or clean up anything else on the page. Spacing between cards, paragraph gaps, and section padding must never be altered unless explicitly instructed.

---

PROJECT IDENTITY

Company: Securevision Pte Ltd
Site: www.securevision.com.sg (staging: svbuild.vercel.app)
Language: British English — authorisation, optimisation, centre, programme, licence (noun)
Tone: Engineering-led, precise, never salesy. Speaks to MCSTs, property managers, architects.
Tone guardrails: Never use "affordable", "best", "cheapest", "leading", "world-class", or any superlative without a specific proof point (e.g. "2,000+ sites protected" not "Singapore's leading integrator").
Fonts: H1–H4 must use Montserrat. Body text and UI labels must use Inter. Never use system fonts or fallbacks as primary fonts.
Logo: images/securevision-logo-white.png — always this path, no other version
WhatsApp: https://wa.me/6593860466
Email: enquiry@securevision.com.sg
Phone: +65 6286 4796

CSS STACK (load order is mandatory):
  <link rel="stylesheet" href="sv-shared.css">
  <script src="site-config.js"></script>
  <link rel="stylesheet" href="sv-guides.css">   ← technical guide pages only
  <link rel="stylesheet" href="sv-forms.css">    ← pages with forms only

TEMPLATE FILES (always use these — never build from scratch):
  _templates/_template-technical-guide.html  ← cctv, burglar-alarm, door-access, auto-gate, intercom
  _templates/_template-brand.html            ← all 20 brand pages
  _templates/_template-solution.html         ← 6 solution sector pages
  _templates/_template-insights.html         ← all insights/blog articles
  _templates/_template-portfolio.html        ← case study pages

INSTRUCTION FILES (paste the relevant one per session):
  _instructions/GLOBAL-INSTRUCTION.md        ← full reference: colours, URLs, components, constants
  _instructions/INSTRUCTION-technical-guide.md
  _instructions/INSTRUCTION-brand.md
  _instructions/INSTRUCTION-solution.md
  _instructions/INSTRUCTION-insights.md
  _instructions/INSTRUCTION-portfolio.md

CANONICAL NAV URLS (never deviate from these):
  Solutions    → security-solutions-singapore.html
  Systems      → security-systems-singapore.html
  Brands       → security-brands-singapore.html
  Portfolio    → portfolio.html
  Resources    → resources.html
  Insights     → security-articles-singapore.html
  About        → about.html
  Contact      → contact.html

HOW TO USE THIS SYSTEM:
For every page build or update, the prompt must follow this format:

  [Paste GLOBAL-INSTRUCTION.md]
  [Paste INSTRUCTION-[page-type].md]
  --- PAGE BRIEF ---
  Template: _templates/_template-[type].html
  File: [filename.html]
  [specific instructions]

For partial updates:
 
  [Paste GLOBAL-INSTRUCTION.md]
  --- UPDATE BRIEF ---
  File: [filename.html]
  Change: [exactly what to change]
  DO NOT TOUCH: [list everything else]
