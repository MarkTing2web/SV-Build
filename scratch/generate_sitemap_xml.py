import os
import datetime

root_dir = r'c:\Projects\SV-Build'
base_url = 'https://www.securevision.com.sg'
lastmod = datetime.date.today().strftime('%Y-%m-%d')

# Exclude list
exclude_dirs = {'.git', '.vercel', 'scratch', 'node_modules', 'templates', 'images', 'artifacts'}
exclude_files = {'sitemap.xml', 'site-config.js', 'nav-footer.js'}

urls = []

for root, dirs, files in os.walk(root_dir):
    # Remove excluded dirs from search
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    
    for file in files:
        if file.endswith('.html') and file not in exclude_files:
            # Skip templates
            if '_template' in file:
                continue
            
            rel_path = os.path.relpath(os.path.join(root, file), root_dir).replace('\\', '/')
            
            # Special case for index.html
            if rel_path == 'index.html':
                url_path = '/'
            elif rel_path.endswith('/index.html'):
                url_path = '/' + rel_path[:-10] + '/'
            else:
                url_path = '/' + rel_path
            
            # Skip thank-you pages from sitemap.xml (they are noindex)
            if 'thank-you' in file or 'success' in file:
                continue
                
            urls.append(base_url + url_path)

urls = sorted(list(set(urls)))

xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for url in urls:
    xml_content += '  <url>\n'
    xml_content += f'    <loc>{url}</loc>\n'
    xml_content += f'    <lastmod>{lastmod}</lastmod>\n'
    xml_content += '    <changefreq>weekly</changefreq>\n'
    xml_content += '    <priority>0.8</priority>\n'
    xml_content += '  </url>\n'

xml_content += '</urlset>'

with open(os.path.join(root_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(xml_content)

print(f"Generated sitemap.xml with {len(urls)} URLs.")
