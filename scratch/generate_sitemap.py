import os
import datetime

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
base_url = "https://www.securevision.com.sg"
today = datetime.datetime.now().strftime("%Y-%m-%d")

exclude_dirs = {'.git', '.vercel', '.github', 'node_modules', '_ai', 'scratch', 'templates'}

html_files = []

for root, dirs, files in os.walk(repo_root):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    
    for f in files:
        if f.endswith('.html'):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, repo_root).replace('\\', '/')
            
            if rel_path == 'index.html':
                url_path = '/'
            elif rel_path.endswith('/index.html'):
                url_path = '/' + rel_path[:-10]
            else:
                url_path = '/' + rel_path
                
            html_files.append(url_path)

html_files.sort()

# Generate SITEMAP.md
md_lines = [
    "# Securevision Site Structure",
    "",
    f"Last updated: {today}",
    ""
]

for url_path in html_files:
    md_lines.append(f"- [{url_path}]({base_url}{url_path})")

with open(os.path.join(repo_root, "SITEMAP.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")

# Generate sitemap.xml
xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for url_path in html_files:
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{base_url}{url_path}</loc>')
    xml_lines.append(f'    <lastmod>{today}</lastmod>')
    xml_lines.append('    <changefreq>weekly</changefreq>')
    xml_lines.append('    <priority>0.8</priority>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')

with open(os.path.join(repo_root, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(xml_lines) + "\n")

# Generate sitemap.html
html_lines = [
    '<!DOCTYPE html>',
    '<html lang="en-GB">',
    '<head>',
    '  <meta charset="UTF-8">',
    '  <title>Sitemap | Securevision Singapore</title>',
    '  <link rel="stylesheet" href="/sv-shared.css">',
    '</head>',
    '<body>',
    '  <nav id="sv-nav"></nav>',
    '  <div class="container" style="padding: 100px 0;">',
    '    <h1>Sitemap</h1>',
    f'    <p>Last updated: {today}</p>',
    '    <ul>'
]

for url_path in html_files:
    if url_path == '/':
        display_text = 'Home'
    else:
        display_text = url_path.lstrip('/')
    html_lines.append(f'      <li><a href="{url_path}">{display_text}</a></li>')

html_lines.extend([
    '    </ul>',
    '  </div>',
    '  <footer id="sv-footer"></footer>',
    '  <script src="/nav-footer.js"></script>',
    '</body>',
    '</html>'
])

with open(os.path.join(repo_root, "sitemap.html"), "w", encoding="utf-8") as f:
    f.write("\n".join(html_lines) + "\n")

print(f"Successfully generated sitemap.html, sitemap.xml, and SITEMAP.md with {len(html_files)} entries.")
