import os
import re

def get_html_files(base_dir):
    html_files = []
    for root, _, files in os.walk(base_dir):
        if 'node_modules' in root or '.git' in root or '.vercel' in root or 'templates' in root or 'scratch' in root:
            continue
        for file in files:
            if file.endswith('.html') and file not in ['sitemap.html']:
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                html_files.append(rel_path.replace('\\', '/'))
    return html_files

def get_sitemap_xml_files(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    urls = re.findall(r'<loc>https://www.securevision.com.sg/([^<]+)</loc>', content)
    return urls

base_dir = r'c:\Projects\SV-Build'
sitemap_path = os.path.join(base_dir, 'sitemap.xml')

actual_files = set(get_html_files(base_dir))
sitemap_files = set(get_sitemap_xml_files(sitemap_path))

missing_from_sitemap = actual_files - sitemap_files

print("Files missing from sitemap.xml:")
for f in sorted(missing_from_sitemap):
    print(f)
