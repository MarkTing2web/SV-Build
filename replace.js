const fs = require('fs');
let css = fs.readFileSync('sv-shared.css', 'utf8');

// Replace 1: remove early .layout-with-sidebar block
const r1_start = '/* -- TECHNICAL GUIDE TEMPLATE (Side-Nav Format) -- */';
const r1_end = '    .layout-with-sidebar main section.bg-light {\r\n        margin-left: -16px;\r\n        margin-right: -16px;\r\n        padding: 48px 16px;\r\n    }\r\n}';
const r1_end_alt = '    .layout-with-sidebar main section.bg-light {\n        margin-left: -16px;\n        margin-right: -16px;\n        padding: 48px 16px;\n    }\n}';

let idx1 = css.indexOf(r1_start);
if (idx1 !== -1) {
    let endIdx = css.indexOf(r1_end, idx1);
    let len = r1_end.length;
    if (endIdx === -1) {
        endIdx = css.indexOf(r1_end_alt, idx1);
        len = r1_end_alt.length;
    }
    if (endIdx !== -1) {
        css = css.substring(0, idx1) + css.substring(endIdx + len);
        console.log('Replaced block 1 successfully.');
    } else {
        console.log('End of block 1 not found.');
    }
} else {
    console.log('Start of block 1 not found.');
}

// Replace 2: Section 33 removal
const r2_start = '/* ==========================================================================\r\n   33. LONG-FORM CONTENT LAYOUT (formerly sv-guides.css)';
const r2_start_alt = '/* ==========================================================================\n   33. LONG-FORM CONTENT LAYOUT (formerly sv-guides.css)';

const r2_end = '  .trust-grid {\r\n    grid-template-columns: 1fr;\r\n    gap: 20px;\r\n  }\r\n}';
const r2_end_alt = '  .trust-grid {\n    grid-template-columns: 1fr;\n    gap: 20px;\n  }\n}';

let idx2 = css.indexOf(r2_start);
if (idx2 === -1) idx2 = css.indexOf(r2_start_alt);

if (idx2 !== -1) {
    let endIdx2 = css.indexOf(r2_end, idx2);
    let len2 = r2_end.length;
    if (endIdx2 === -1) {
        endIdx2 = css.indexOf(r2_end_alt, idx2);
        len2 = r2_end_alt.length;
    }
    if (endIdx2 !== -1) {
        const replacement = '/* ==========================================================================\\n   33. LONG-FORM CONTENT LAYOUT — MOVED TO resources.css\\n   Extracted: May 2026\\n   All guide-page typography, blog-row, blog-img-wrap, component-card,\\n   recommendation-box, stat-grid, author-bio-strip, trust-grid, and\\n   related responsive rules now live in /resources.css Section A.\\n   Do not re-add guide-specific classes to this file.\\n   ========================================================================== */';
        
        let replStr = replacement;
        if (css.indexOf('\\r\\n') !== -1) {
            replStr = replStr.replace(/\\n/g, '\\r\\n');
        }
        
        css = css.substring(0, idx2) + replStr + css.substring(endIdx2 + len2);
        console.log('Replaced block 2 successfully.');
    } else {
        console.log('End of block 2 not found.');
    }
} else {
    console.log('Start of block 2 not found.');
}

fs.writeFileSync('sv-shared.css', css);

