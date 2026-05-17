import os
import xml.etree.ElementTree as ET
from datetime import date

def get_html_files(root_dir):
    html_files = []
    exclude_dirs = {'.git', '.github', '.vercel', 'templates', 'scratch', 'image-folder', 'images', 'pdf', 'Final'}
    exclude_files = {'nav-footer-bak.js', 'nav-footer.js', 'site-config.js', 'systems-block.js', 'audit_ctas.py', 'audit_ctas.ps1', 'migrate-nav-footer.ps1'}
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith('.html') and not file.startswith('_') and file not in exclude_files:
                if ' - Copy' in file:
                    continue
                rel_path = os.path.relpath(os.path.join(root, file), root_dir)
                rel_path = rel_path.replace('\\', '/')
                if rel_path == 'index.html':
                    html_files.append('')
                else:
                    html_files.append(rel_path)
    return sorted(html_files)

def update_xml_sitemap(file_path, html_files):
    today = date.today().isoformat()
    base_url = "https://www.securevision.com.sg/"
    
    # We'll just rebuild it to be clean
    root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    for file in html_files:
        url_elem = ET.SubElement(root, "url")
        loc = ET.SubElement(url_elem, "loc")
        loc.text = base_url + file
        
        lastmod = ET.SubElement(url_elem, "lastmod")
        lastmod.text = today
        
        changefreq = ET.SubElement(url_elem, "changefreq")
        changefreq.text = "weekly"
        
        priority = ET.SubElement(url_elem, "priority")
        priority.text = "0.8"
        
    tree = ET.ElementTree(root)
    # Re-indenting manually because ET is basic
    from xml.dom import minidom
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
    # Remove first line (xml version) because we'll add it back or it's redundant
    lines = xmlstr.split('\n')
    if lines[0].startswith('<?xml'):
        xmlstr = '\n'.join(lines[1:])
    
    final_xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr.strip()
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_xml)

def extract_title(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            start = content.find('<title>')
            end = content.find('</title>')
            if start != -1 and end != -1:
                return content[start+7:end].strip()
    except:
        pass
    return os.path.basename(file_path)

def update_html_sitemap(file_path, html_files, root_dir):
    links = []
    for file in html_files:
        full_path = os.path.join(root_dir, file if file else 'index.html')
        title = extract_title(full_path)
        href = '/' + file
        links.append(f'      <li><a href="{href}">{title}</a></li>')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(lines):
        if '<ul>' in line:
            start_idx = i
        if '</ul>' in line:
            end_idx = i
            break
            
    if start_idx != -1 and end_idx != -1:
        new_content = lines[:start_idx+1] + [l + '\n' for l in links] + lines[end_idx:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_content)

def update_md_sitemap(file_path, html_files):
    base_url = "https://www.securevision.com.sg/"
    lines = ["# Securevision Site Structure\n", "\n"]
    for file in html_files:
        path = "/" + file
        url = base_url + file
        lines.append(f"- [{path}]({url})\n")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

if __name__ == "__main__":
    root = "c:/Projects/SV-Build"
    html_files = get_html_files(root)
    
    update_xml_sitemap(os.path.join(root, "sitemap.xml"), html_files)
    update_html_sitemap(os.path.join(root, "sitemap.html"), html_files, root)
    update_md_sitemap(os.path.join(root, "SITEMAP.md"), html_files)
    print(f"Updated sitemap with {len(html_files)} files.")
