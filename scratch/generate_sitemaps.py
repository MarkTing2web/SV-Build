import os
from datetime import datetime

def generate_sitemaps(base_dir):
    html_files = []
    
    # Exclude directories
    exclude_dirs = ['node_modules', '.git', '.vercel', 'templates', 'scratch', 'instructions']
    
    for root, dirs, files in os.walk(base_dir):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith('.html') and file not in ['sitemap.html']:
                # Get path relative to base_dir
                rel_path = os.path.relpath(os.path.join(root, file), base_dir).replace('\\', '/')
                
                # Handle index.html -> /
                url_path = f"/{rel_path}"
                if url_path == '/index.html':
                    url_path = '/'
                elif url_path.endswith('/index.html'):
                    url_path = url_path[:-10] # e.g. /brands/index.html -> /brands/
                
                html_files.append((rel_path, url_path))
                
    # Sort files alphabetically by url_path
    html_files.sort(key=lambda x: x[1])
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 1. Generate sitemap.xml
    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>',
                   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    
    for rel_path, url_path in html_files:
        xml_content.append('  <url>')
        xml_content.append(f'    <loc>https://www.securevision.com.sg{url_path}</loc>')
        xml_content.append(f'    <lastmod>{today}</lastmod>')
        xml_content.append('    <changefreq>weekly</changefreq>')
        xml_content.append('    <priority>0.8</priority>')
        xml_content.append('  </url>')
    xml_content.append('</urlset>')
    
    with open(os.path.join(base_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_content))
        
    # 2. Update sitemap.html
    sitemap_html_path = os.path.join(base_dir, 'sitemap.html')
    with open(sitemap_html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    # Find the ul block and last updated
    import re
    
    # Replace Last updated date
    html_content = re.sub(r'<p>Last updated: .*?</p>', f'<p>Last updated: {today}</p>', html_content)
    
    ul_content = ['<ul>']
    for rel_path, url_path in html_files:
        display_text = "Home" if url_path == "/" else url_path.lstrip('/')
        ul_content.append(f'      <li><a href="{url_path}">{display_text}</a></li>')
    ul_content.append('    </ul>')
    
    # Replace the existing ul block
    html_content = re.sub(r'<ul>.*?</ul>', '\n'.join(ul_content), html_content, flags=re.DOTALL)
    
    with open(sitemap_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_sitemaps(r'c:\Projects\SV-Build')
    print("Sitemaps generated successfully.")
