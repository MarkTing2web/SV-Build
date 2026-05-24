import os
import re
from bs4 import BeautifulSoup

repo_root = r"c:\Projects\SV-Build"
solutions_dir = os.path.join(repo_root, "solutions")

# Scan every .html file in /solutions/ and all its subfolders recursively
solutions_html_files = []
for root, dirs, files in os.walk(solutions_dir):
    for f in files:
        if f.lower().endswith('.html'):
            solutions_html_files.append(os.path.join(root, f))
solutions_html_files.sort()

url_pattern = re.compile(r'url\(\s*[\'"]?([^\'")\s]+)[\'"]?\s*\)', re.IGNORECASE)

results = []

for filepath in solutions_html_files:
    rel_path = os.path.relpath(filepath, repo_root).replace('\\', '/')
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # 1. Find the DESKTOP hero
    # Let's extract all image URLs in style blocks, header inline styles
    style_urls = []
    for style in soup.find_all('style'):
        style_urls.extend(url_pattern.findall(style.string or ''))
    for header in soup.find_all('header'):
        header_style = header.get('style') or ''
        style_urls.extend(url_pattern.findall(header_style))
        
    # The desktop hero is typically the first url in style/header that ends with .webp, .png, etc.
    # but not ending in -mobile.webp, -mobile.png, -rel.webp, etc.
    desktop_hero = None
    for url in style_urls:
        url_clean = url.strip().split('?')[0].split('#')[0]
        if not url_clean:
            continue
        if '-mobile' not in url_clean.lower() and '-rel' not in url_clean.lower():
            desktop_hero = url_clean
            break
            
    if not desktop_hero:
        # fallback: check og:image
        for meta in soup.find_all('meta', property='og:image'):
            val = meta.get('content') or ''
            if val and '-rel' not in val.lower() and '-mobile' not in val.lower():
                # strip domain if absolute
                for domain in ["https://www.securevision.com.sg", "http://www.securevision.com.sg"]:
                    if val.startswith(domain):
                        val = val[len(domain):]
                desktop_hero = val
                break
                
    # 2. Check for MOBILE hero
    mobile_hero_val = "MISSING"
    if desktop_hero:
        base_name_ext = os.path.basename(desktop_hero)
        base_name, ext = os.path.splitext(base_name_ext)
        
        # Determine core name (strip -hero if present)
        core_name = base_name[:-5] if base_name.endswith("-hero") else base_name
        
        # Possible mobile filenames
        possible_mobiles = [
            f"{base_name}-mobile.webp",
            f"{core_name}-mobile.webp",
            f"{core_name}-hero-mobile.webp"
        ]
        # Remove duplicates while preserving order
        possible_mobiles = list(dict.fromkeys(possible_mobiles))
        
        for pm in possible_mobiles:
            if pm in content:
                # Find the full path/url
                pattern = r'[\w\-./]*' + re.escape(pm)
                match = re.search(pattern, content)
                mobile_hero_val = match.group(0) if match else pm
                break
                
    # 3. Check for REL thumbnail
    rel_thumbnail_val = "MISSING"
    if desktop_hero:
        base_name_ext = os.path.basename(desktop_hero)
        base_name, ext = os.path.splitext(base_name_ext)
        
        # Determine core name (strip -hero if present)
        core_name = base_name[:-5] if base_name.endswith("-hero") else base_name
        
        # Possible rel filenames
        possible_rels = [
            f"{base_name}-rel.webp",
            f"{core_name}-rel.webp",
            f"{core_name}-hero-rel.webp"
        ]
        # Remove duplicates while preserving order
        possible_rels = list(dict.fromkeys(possible_rels))
        
        for pr in possible_rels:
            if pr in content:
                # Find the full path/url
                pattern = r'[\w\-./]*' + re.escape(pr)
                match = re.search(pattern, content)
                rel_thumbnail_val = match.group(0) if match else pr
                break

    results.append({
        "file": rel_path,
        "desktop": desktop_hero or "MISSING",
        "mobile": mobile_hero_val,
        "rel": rel_thumbnail_val
    })
# Output format
out_path = r"c:\Projects\SV-Build\scratch\audit_heros_output.txt"
with open(out_path, 'w', encoding='utf-8') as out_f:
    for r in results:
        out_f.write(f"FILE: {r['file']}\n")
        out_f.write(f"  Desktop hero:  {'DEFINED: ' + r['desktop'] if r['desktop'] != 'MISSING' else 'MISSING'}\n")
        out_f.write(f"  Mobile hero:   {'DEFINED: ' + r['mobile'] if r['mobile'] != 'MISSING' else 'MISSING'}\n")
        out_f.write(f"  Rel thumbnail: {'DEFINED: ' + r['rel'] if r['rel'] != 'MISSING' else 'MISSING'}\n")
        out_f.write("\n")

    out_f.write("Summary Table:\n")
    out_f.write("| Page | Desktop | Mobile | Rel |\n")
    out_f.write("| --- | --- | --- | --- |\n")
    flagged_pages = []
    for r in results:
        d_status = "✅" if r['desktop'] != "MISSING" else "❌"
        m_status = "✅" if r['mobile'] != "MISSING" else "❌"
        r_status = "✅" if r['rel'] != "MISSING" else "❌"
        out_f.write(f"| {r['file']} | {d_status} | {m_status} | {r_status} |\n")
        if r['mobile'] == "MISSING" or r['rel'] == "MISSING":
            flagged_pages.append(r['file'])
            
    if flagged_pages:
        out_f.write("\nFlagged pages (Mobile or Rel is MISSING):\n")
        for fp in flagged_pages:
             out_f.write(f"- {fp}\n")

