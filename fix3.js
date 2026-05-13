const fs = require('fs');
let css = fs.readFileSync('sv-shared.css', 'utf8');
const target = '/* ==========================================================================\r\n   34. CHECKLIST UI COMPONENTS';
const target2 = '/* ==========================================================================\n   34. CHECKLIST UI COMPONENTS';

const replacement = '/* ==========================================================================\n   33. LONG-FORM CONTENT LAYOUT — MOVED TO resources.css\n   Extracted: May 2026\n   All guide-page typography, blog-row, blog-img-wrap, component-card,\n   recommendation-box, stat-grid, author-bio-strip, trust-grid, and\n   related responsive rules now live in /resources.css Section A.\n   Do not re-add guide-specific classes to this file.\n   ========================================================================== */\n\n';

let idx = css.indexOf(target);
if (idx === -1) idx = css.indexOf(target2);

if (idx !== -1) {
    css = css.substring(0, idx) + replacement + css.substring(idx);
    fs.writeFileSync('sv-shared.css', css);
    console.log('Inserted comment block');
} else {
    console.log('Could not find Section 34 header to insert before.');
}

