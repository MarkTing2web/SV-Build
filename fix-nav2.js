const fs = require('fs');
let content = fs.readFileSync('c:/Projects/SV-Build/nav-footer.js', 'utf8');
let lines = content.split('\n');
lines[16] = lines[16].replace(/<\/nav>\\";.*$/, '</nav>";');
fs.writeFileSync('c:/Projects/SV-Build/nav-footer.js', lines.join('\n'), 'utf8');
console.log('Fixed quotes');
