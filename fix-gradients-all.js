const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(function(file) {
        file = path.join(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) {
            // Exclude directories we don't want to sweep
            if (!file.includes('node_modules') && !file.includes('.git')) {
                results = results.concat(walk(file));
            }
        } else {
            if (file.endsWith('.html')) results.push(file);
        }
    });
    return results;
}

const rootDir = 'c:/Projects/SV-Build';
const files = walk(rootDir);
let modifiedFiles = [];

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // Regex to match the broken gradient pattern
    const regex = /linear-gradient\([^)]*var\(--text-primary\)[^)]*var\(--text-secondary\)[^)]*var\(--border-subtle\)[^)]*\)/g;
    
    if (regex.test(content)) {
        const newContent = content.replace(regex, 'linear-gradient(to right, rgba(0,0,0,0.80) 0%, rgba(0,0,0,0.50) 50%, rgba(0,0,0,0.15) 100%)');
        fs.writeFileSync(file, newContent, 'utf8');
        modifiedFiles.push(file);
        console.log('Fixed:', file);
    }
});

console.log('Sweep complete. Total files fixed:', modifiedFiles.length);
