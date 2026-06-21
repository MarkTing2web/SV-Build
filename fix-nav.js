const fs = require('fs');
let content = fs.readFileSync('c:/Projects/SV-Build/nav-footer.js', 'utf8');
let lines = content.split('\n');
let navLine = lines[15];

// Fix the start of the line
navLine = navLine.replace('"use stric  var NAV_HTML = ', '"use strict";\n  var NAV_HTML = ');

// Fix the end of the line
navLine = navLine.replace(/<\/nav>\\";.*$/, '</nav>\\";');

lines[15] = navLine;
fs.writeFileSync('c:/Projects/SV-Build/nav-footer.js', lines.join('\n'), 'utf8');
console.log('Fixed nav-footer.js');
