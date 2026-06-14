const fs = require('fs');

let content = fs.readFileSync('C:\\Projects\\SV-Build\\site-config.js', 'utf8');

const toRemove = [
  "lpr-vs-rfid-vehicle-access-singapore",
  "pdpa-cctv-singapore",
  "video-analytics-retail-singapore"
];

let lines = content.split('\n');
let newLines = [];
let insideArray = false;

for (let i = 0; i < lines.length; i++) {
    let line = lines[i];
    if (line.includes('SECUREVISION.insights = [')) {
        insideArray = true;
        newLines.push(line);
        continue;
    }
    if (insideArray && line.trim() === '];') {
        insideArray = false;
    }
    
    if (insideArray) {
        let isOrphan = false;
        for (let orphan of toRemove) {
            if (line.includes(`slug: "${orphan}"`) || line.includes(`slug:"${orphan}"`)) {
                isOrphan = true;
                break;
            }
        }
        if (!isOrphan) {
            newLines.push(line);
        }
    } else {
        newLines.push(line);
    }
}

content = newLines.join('\n');

fs.writeFileSync('C:\\Projects\\SV-Build\\site-config.js', content);
console.log("Cleanup complete.");
