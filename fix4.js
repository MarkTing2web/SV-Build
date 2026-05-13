const fs = require('fs');
let css = fs.readFileSync('sv-shared.css', 'utf8');
css = css.replace(/33\. LONG-FORM CONTENT LAYOUT.*?MOVED TO resources\.css/, '33. LONG-FORM CONTENT LAYOUT \u2014 MOVED TO resources.css');
fs.writeFileSync('sv-shared.css', css, 'utf8');

