const fs = require('fs');
let css = fs.readFileSync('sv-shared.css', 'utf8');
const replacement = '/* ==========================================================================\n   33. LONG-FORM CONTENT LAYOUT — MOVED TO resources.css\n   Extracted: May 2026\n   All guide-page typography, blog-row, blog-img-wrap, component-card,\n   recommendation-box, stat-grid, author-bio-strip, trust-grid, and\n   related responsive rules now live in /resources.css Section A.\n   Do not re-add guide-specific classes to this file.\n   ========================================================================== */\n\n';

if (css.indexOf('33. LONG-FORM CONTENT LAYOUT — MOVED TO resources.css') === -1) {
    const target = '/* ==========================================================================\n   34. CHECKLIST UI COMPONENTS';
    const target2 = '/* ==========================================================================\r\n   34. CHECKLIST UI COMPONENTS';
    let idx = css.indexOf(target);
    if (idx === -1) idx = css.indexOf(target2);
    if (idx !== -1) {
        css = css.substring(0, idx) + replacement + css.substring(idx);
        fs.writeFileSync('sv-shared.css', css);
    }
}
