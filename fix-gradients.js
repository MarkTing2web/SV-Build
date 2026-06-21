const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(function(file) {
        file = path.join(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) {
            results = results.concat(walk(file));
        } else {
            if (file.endsWith('.html')) results.push(file);
        }
    });
    return results;
}

const dirsToSweep = ['portfolio', 'systems', 'solutions', 'brands'];
let modifiedFiles = 0;

dirsToSweep.forEach(dir => {
    const fullPath = path.join('c:/Projects/SV-Build', dir);
    if (!fs.existsSync(fullPath)) return;
    
    const files = walk(fullPath);
    files.forEach(file => {
        let content = fs.readFileSync(file, 'utf8');
        
        // Regex to match the broken gradient pattern
        // linear-gradient(to right, var(--text-primary) 0%, var(--text-secondary) 50%, var(--border-subtle) 100%)
        // Account for 50% or 55% or anything else
        const regex = /linear-gradient\([^)]*var\(--text-primary\)[^)]*var\(--text-secondary\)[^)]*var\(--border-subtle\)[^)]*\)/g;
        
        if (regex.test(content)) {
            const newContent = content.replace(regex, 'linear-gradient(to right, rgba(0,0,0,0.80) 0%, rgba(0,0,0,0.50) 50%, rgba(0,0,0,0.15) 100%)');
            fs.writeFileSync(file, newContent, 'utf8');
            modifiedFiles++;
            console.log('Fixed:', file);
        }
    });
});

console.log('Sweep complete. Total files fixed:', modifiedFiles);
