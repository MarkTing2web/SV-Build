const fs = require('fs');
let css = fs.readFileSync('sv-shared.css', 'utf8');

// 1. Extract canonical block
const canonicalStart = '/* 6. SIDEBAR & NAVIGATION */';
const responsiveStart = '/* 7. RESPONSIVE COMPLIANCE (991px Mobile Rule) */';

let canIdx = css.indexOf(canonicalStart);
let resIdx = css.indexOf(responsiveStart);
let endIdx = css.indexOf('/* Author bio strip', resIdx); // End of responsive block

let canonicalBlock = css.substring(canIdx, endIdx);

// Fix scoping in canonical block
canonicalBlock = canonicalBlock.replace('aside { grid-area: sidebar; }', '.layout-with-sidebar aside { grid-area: sidebar; }');
canonicalBlock = canonicalBlock.replace('main { grid-area: content; }', '.layout-with-sidebar main { grid-area: content; }');

// 2. Remove early duplicate
const earlyStart = '/* -- TECHNICAL GUIDE TEMPLATE (Side-Nav Format) -- */';
const earlyEnd = '    .layout-with-sidebar main section.bg-light {\r\n        margin-left: -16px;\r\n        margin-right: -16px;\r\n        padding: 48px 16px;\r\n    }\r\n}';
const earlyEndAlt = '    .layout-with-sidebar main section.bg-light {\n        margin-left: -16px;\n        margin-right: -16px;\n        padding: 48px 16px;\n    }\n}';

let eIdx1 = css.indexOf(earlyStart);
if (eIdx1 !== -1) {
    let eIdx2 = css.indexOf(earlyEnd, eIdx1);
    let len = earlyEnd.length;
    if (eIdx2 === -1) {
        eIdx2 = css.indexOf(earlyEndAlt, eIdx1);
        len = earlyEndAlt.length;
    }
    // Replace early block with canonical block!
    if (eIdx2 !== -1) {
        css = css.substring(0, eIdx1) + canonicalBlock + css.substring(eIdx2 + len);
    }
}

// 3. Remove Section 33 and add comment
const sec33Start = '/* ==========================================================================\r\n   33. LONG-FORM CONTENT LAYOUT';
const sec33StartAlt = '/* ==========================================================================\n   33. LONG-FORM CONTENT LAYOUT';

const sec33End = '  .trust-grid {\r\n    grid-template-columns: 1fr;\r\n    gap: 20px;\r\n  }\r\n}';
const sec33EndAlt = '  .trust-grid {\n    grid-template-columns: 1fr;\n    gap: 20px;\n  }\n}';

let sIdx1 = css.indexOf(sec33Start);
if (sIdx1 === -1) sIdx1 = css.indexOf(sec33StartAlt);

if (sIdx1 !== -1) {
    let sIdx2 = css.indexOf(sec33End, sIdx1);
    let slen = sec33End.length;
    if (sIdx2 === -1) {
        sIdx2 = css.indexOf(sec33EndAlt, sIdx1);
        slen = sec33EndAlt.length;
    }
    if (sIdx2 !== -1) {
        const replacement = '/* ==========================================================================\\n   33. LONG-FORM CONTENT LAYOUT \u2014 MOVED TO resources.css\\n   Extracted: May 2026\\n   All guide-page typography, blog-row, blog-img-wrap, component-card,\\n   recommendation-box, stat-grid, author-bio-strip, trust-grid, and\\n   related responsive rules now live in /resources.css Section A.\\n   Do not re-add guide-specific classes to this file.\\n   ========================================================================== */';
        let replStr = replacement;
        if (css.indexOf('\\r\\n') !== -1) {
            replStr = replStr.replace(/\\n/g, '\\r\\n');
        }
        css = css.substring(0, sIdx1) + replStr + css.substring(sIdx2 + slen);
    }
}

fs.writeFileSync('sv-shared.css', css);

