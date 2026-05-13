const fs = require('fs');
let css = fs.readFileSync('sv-shared.css', 'utf8');
const badStr = '/* ==========================================================================\\n   33. LONG-FORM CONTENT LAYOUT \u2014 MOVED TO resources.css\\n   Extracted: May 2026\\n   All guide-page typography, blog-row, blog-img-wrap, component-card,\\n   recommendation-box, stat-grid, author-bio-strip, trust-grid, and\\n   related responsive rules now live in /resources.css Section A.\\n   Do not re-add guide-specific classes to this file.\\n   ========================================================================== */';
const goodStr = \/* ==========================================================================
   33. LONG-FORM CONTENT LAYOUT — MOVED TO resources.css
   Extracted: May 2026
   All guide-page typography, blog-row, blog-img-wrap, component-card,
   recommendation-box, stat-grid, author-bio-strip, trust-grid, and
   related responsive rules now live in /resources.css Section A.
   Do not re-add guide-specific classes to this file.
   ========================================================================== */\;
css = css.replace(badStr, goodStr);
fs.writeFileSync('sv-shared.css', css);

