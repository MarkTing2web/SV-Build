import os
import datetime

root_dir = r'c:\Projects\SV-Build'
base_url = 'https://www.securevision.com.sg'
lastmod = datetime.date.today().strftime('%Y-%m-%d')

exclude_dirs = {'.git', '.vercel', 'scratch', 'node_modules', 'templates', 'images', 'artifacts'}
exclude_files = {'sitemap.xml', 'site-config.js', 'nav-footer.js'}

urls = []

for root, dirs, files in os.walk(root_dir):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html') and file not in exclude_files:
            if '_template' in file:
                continue
            rel_path = os.path.relpath(os.path.join(root, file), root_dir).replace('\\', '/')
            if rel_path == 'index.html':
                url_path = '/'
            elif rel_path.endswith('/index.html'):
                url_path = '/' + rel_path[:-10] + '/'
            else:
                url_path = '/' + rel_path
            
            # Skip thank-you/success from XML but keep in HTML/MD? 
            # Actually, standard is to exclude them from public sitemaps if noindex.
            if 'thank-you' in file or 'success' in file:
                continue
            urls.append(url_path)

urls = sorted(list(set(urls)))

# --- 1. GENERATE sitemap.xml ---
xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for path in urls:
    full_url = base_url + path
    xml_content += '  <url>\n'
    xml_content += f'    <loc>{full_url}</loc>\n'
    xml_content += f'    <lastmod>{lastmod}</lastmod>\n'
    xml_content += '    <changefreq>weekly</changefreq>\n'
    xml_content += '    <priority>0.8</priority>\n'
    xml_content += '  </url>\n'
xml_content += '</urlset>'

with open(os.path.join(root_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(xml_content)

# --- 2. GENERATE sitemap.html ---
# We keep the nav-footer injection and container styling
html_content = f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <title>Sitemap | Securevision Singapore</title>
  <link rel="stylesheet" href="/sv-shared.css">
</head>
<body>
  <nav id="sv-nav"></nav>
  <div class="container" style="padding: 100px 0;">
    <h1>Sitemap</h1>
    <p>Last updated: {lastmod}</p>
    <ul>
'''
for path in urls:
    # Make anchor text prettier
    anchor = path.lstrip('/')
    if not anchor: anchor = "Home"
    html_content += f'      <li><a href="{path}">{anchor}</a></li>\n'

html_content += '''    </ul>
  </div>
  <footer id="sv-footer"></footer>
  <script src="/nav-footer.js"></script>
</body>
</html>'''

with open(os.path.join(root_dir, 'sitemap.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

# --- 3. GENERATE SITEMAP.md ---
md_content = f'# Securevision Site Structure\n\n'
md_content += f'Last updated: {lastmod}\n\n'
for path in urls:
    full_url = base_url + path
    md_content += f'- [{path}]({full_url})\n'

with open(os.path.join(root_dir, 'SITEMAP.md'), 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Synchronized sitemap.xml, sitemap.html, and SITEMAP.md with {len(urls)} URLs.")
