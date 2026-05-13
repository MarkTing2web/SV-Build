const fs = require('fs');
let css = fs.readFileSync('sv-shared.css', 'utf8');
const replacement = '/* ==========================================================================\n   33. LONG-FORM CONTENT LAYOUT — MOVED TO resources.css\n   Extracted: May 2026\n   All guide-page typography, blog-row, blog-img-wrap, component-card,\n   recommendation-box, stat-grid, author-bio-strip, trust-grid, and\n   related responsive rules now live in /resources.css Section A.\n   Do not re-add guide-specific classes to this file.\n   ========================================================================== */';

// Use a regex to find the broken comment and replace it
const regex = /\/\* =+?\\n\s*33\. LONG-FORM CONTENT LAYOUT.*?=\+ \*\//s;
css = css.replace(/\/\* =+?\\n\s*33\. LONG-FORM CONTENT LAYOUT.*?=\* \*\//s, replacement);
css = css.replace(/\/\* ==========================================================================\\n   33\. LONG-FORM CONTENT LAYOUT.*?========================================================================== \*\//, replacement);
fs.writeFileSync('sv-shared.css', css);

