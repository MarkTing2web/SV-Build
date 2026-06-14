const fs = require('fs');

let content = fs.readFileSync('C:\\Projects\\SV-Build\\site-config.js', 'utf8');

let match = content.match(/SECUREVISION\.insights\s*=\s*\[([\s\S]*?)\];/);
if(match) {
    let slugs = [];
    let regex = /slug:\s*"([^"]+)"/g;
    let m;
    while ((m = regex.exec(match[1])) !== null) {
        slugs.push(m[1]);
    }
    
    let files = fs.readdirSync('C:\\Projects\\SV-Build\\insights');
    let htmlFiles = files.filter(f => f.endsWith('.html') && f !== 'index.html').map(f => f.replace('.html', ''));
    
    let invalid = slugs.filter(s => !htmlFiles.includes(s));
    console.log('Slugs in site-config.js WITHOUT an HTML file:', invalid);
    
    let missing = htmlFiles.filter(f => !slugs.includes(f));
    console.log('HTML files WITHOUT a slug in site-config.js:', missing);
}
