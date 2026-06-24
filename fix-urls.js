const fs = require('fs');
const path = require('path');

function getCleanUrl(url) {
    if (!url.includes('.html')) return url;
    // Don't modify external links if any
    if (url.startsWith('http') && !url.includes('securevision.com.sg')) return url;
    
    let clean = url.replace(/\/index\.html($|#|\?)/, '/$1');
    clean = clean.replace(/\.html($|#|\?)/, '$1');
    return clean;
}

// 1. Process sitemap.xml
let sitemapXml = fs.readFileSync('sitemap.xml', 'utf8');
sitemapXml = sitemapXml.replace(/<loc>(.*?)<\/loc>/g, (match, url) => {
    return `<loc>${getCleanUrl(url)}</loc>`;
});
fs.writeFileSync('sitemap.xml', sitemapXml, 'utf8');

// 2. Process SITEMAP.md
let sitemapMd = fs.readFileSync('SITEMAP.md', 'utf8');
sitemapMd = sitemapMd.replace(/\]\((.*?)\)/g, (match, url) => {
    return `](${getCleanUrl(url)})`;
});
fs.writeFileSync('SITEMAP.md', sitemapMd, 'utf8');

// 3. Process sitemap.html
let sitemapHtml = fs.readFileSync('sitemap.html', 'utf8');
sitemapHtml = sitemapHtml.replace(/href=["'](.*?)["']/g, (match, url) => {
    if (url.endsWith('.css') || url.endsWith('.js') || url.endsWith('.png') || url.endsWith('.webp') || url.endsWith('.jpg') || url.endsWith('.ico')) return match;
    return `href="${getCleanUrl(url)}"`;
});
fs.writeFileSync('sitemap.html', sitemapHtml, 'utf8');

// 4. Process all HTML files
function processDirectory(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        if (['node_modules', '.git', '.github', '.vercel', 'images'].includes(file)) continue;
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        
        if (stat.isDirectory()) {
            processDirectory(fullPath);
        } else if (file.endsWith('.html')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            let updated = false;
            
            // Fix canonical tags
            content = content.replace(/<link[^>]+rel=["']canonical["'][^>]*>/gi, (match) => {
                return match.replace(/href=["'](.*?)["']/, (m, url) => {
                    let clean = getCleanUrl(url);
                    if (clean !== url) updated = true;
                    return `href="${clean}"`;
                });
            });
            
            // Fix other internal absolute paths starting with /
            content = content.replace(/href=["'](\/[^"']*\.html[^"']*)["']/g, (match, url) => {
                let clean = getCleanUrl(url);
                if (clean !== url) updated = true;
                return `href="${clean}"`;
            });
            
            // Fix internal absolute paths starting with https://www.securevision.com.sg/
            content = content.replace(/href=["'](https:\/\/www\.securevision\.com\.sg\/[^"']*\.html[^"']*)["']/g, (match, url) => {
                let clean = getCleanUrl(url);
                if (clean !== url) updated = true;
                return `href="${clean}"`;
            });

            if (updated) {
                fs.writeFileSync(fullPath, content, 'utf8');
            }
        } else if (file.endsWith('.js') && !file.endsWith('.min.js') && file !== 'fix-urls.js') {
            let content = fs.readFileSync(fullPath, 'utf8');
            let updated = false;
            
            // Replace full .html paths
            content = content.replace(/(\/([a-zA-Z0-9_-]+\/)*[a-zA-Z0-9_-]+\.html)/g, (match, url) => {
                let clean = getCleanUrl(url);
                if (clean !== url) updated = true;
                return clean;
            });
            
            // specifically for build-search-index.js
            if (file === 'build-search-index.js') {
                content = content.replace(/'\/insights\/' \+ a\.slug \+ '\.html'/g, () => {
                    updated = true;
                    return "'/insights/' + a.slug";
                });
            }

            // specifically for sv-search.js, which has: window.location.href = item.url; (no change needed if json is updated)

            if (updated) {
                fs.writeFileSync(fullPath, content, 'utf8');
            }
        }
    }
}
processDirectory('.');
console.log('Done fixing URLs');
