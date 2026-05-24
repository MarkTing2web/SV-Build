import os
import re
from bs4 import BeautifulSoup

repo_root = r"c:\Projects\SV-Build"
solutions_dir = os.path.join(repo_root, "solutions")
images_sol_dir = os.path.join(repo_root, "images", "solutions")

# Exclusions for Check 2
img_exclusions = [
    "/images/ler-wee-meng-bio.webp",
    "/images/og-default.jpg",
    "/images/portfolio/portfolio-light-cairnhill.webp",
    "/images/portfolio/portfolio-industrial.png"
]

url_in_style_re = re.compile(r'url\(\s*[\'"]?([^\'")\s]+)[\'"]?\s*\)', re.IGNORECASE)

def parse_srcset(srcset_val):
    if not srcset_val:
        return []
    urls = []
    parts = srcset_val.split(',')
    for part in parts:
        part = part.strip()
        if not part:
            continue
        url_part = part.split()[0]
        urls.append(url_part)
    return urls

# Helpers for Check 1 (Broken Links)
def resolve_local_path(path):
    path = path.split('?')[0].split('#')[0]
    path = path.strip()
    if not path:
        return None
        
    for domain in ["https://www.securevision.com.sg", "http://www.securevision.com.sg"]:
        if path.startswith(domain):
            path = path[len(domain):]
            
    if path.startswith(('http://', 'https://', 'mailto:', 'tel:', '//')):
        return None
        
    if not path.startswith('/'):
        # For this audit, since we only target solutions html files, if it doesn't start with /
        # it is relative. But let's handle relative path conversion inside the loop where we know the file's dir.
        return "RELATIVE"
        
    clean_path = path.lstrip('/')
    if not clean_path:
        return os.path.join(repo_root, "index.html")
        
    full_path = os.path.join(repo_root, clean_path)
    if os.path.isdir(full_path) or path.endswith('/'):
        return os.path.join(full_path, "index.html")
        
    return full_path

# Find all HTML files recursively in solutions/
solutions_html_files = []
for root, dirs, files in os.walk(solutions_dir):
    for f in files:
        if f.lower().endswith('.html'):
            solutions_html_files.append(os.path.join(root, f))
solutions_html_files.sort()

# Find all HTML and CSS files sitewide for search
all_html_files = []
all_css_files = []
for root, dirs, files in os.walk(repo_root):
    if any(p in root.split(os.sep) for p in [".git", "node_modules", ".vercel"]):
        continue
    for f in files:
        if f.lower().endswith('.html'):
            all_html_files.append(os.path.join(root, f))
        elif f.lower().endswith('.css'):
            all_css_files.append(os.path.join(root, f))

# Pre-load content of all HTML and CSS files to speed up search
html_contents = {}
for filepath in all_html_files:
    rel = os.path.relpath(filepath, repo_root).replace('\\', '/')
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            html_contents[rel] = f.read()
    except Exception as e:
        print(f"Error reading {rel}: {e}")

css_contents = {}
for filepath in all_css_files:
    rel = os.path.relpath(filepath, repo_root).replace('\\', '/')
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            css_contents[rel] = f.read()
    except Exception as e:
        print(f"Error reading {rel}: {e}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RUN CHECK 1 & 2
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
check1_results = [] # list of (file, list of broken links)
check2_results = [] # list of (file, list of missing images)

for filepath in solutions_html_files:
    file_dir = os.path.dirname(filepath)
    rel_file = os.path.relpath(filepath, repo_root).replace('\\', '/')
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # Check 1: Links
    broken_links = []
    # - <a href="..."> starting with / (or relative)
    # - <link rel="canonical" href="...">
    # - og:url meta content
    
    # 1a. <a href="...">
    for a in soup.find_all('a'):
        href = a.get('href')
        if href:
            href_clean = href.split('?')[0].split('#')[0].strip()
            if not href_clean or href_clean.startswith(('http://', 'https://', 'mailto:', 'tel:', '//', '#')):
                continue
            # Resolve
            resolved = resolve_local_path(href)
            if resolved == "RELATIVE":
                resolved = os.path.abspath(os.path.join(file_dir, href_clean))
            if resolved and not os.path.exists(resolved):
                broken_links.append(href)
                
    # 1b. <link rel="canonical" href="...">
    for link in soup.find_all('link', rel='canonical'):
        href = link.get('href')
        if href:
            resolved = resolve_local_path(href)
            if resolved == "RELATIVE":
                resolved = os.path.abspath(os.path.join(file_dir, href.split('?')[0].split('#')[0].strip()))
            if resolved and not os.path.exists(resolved):
                broken_links.append(href)
                
    # 1c. og:url meta content
    for meta in soup.find_all('meta'):
        if meta.get('property') == 'og:url' or meta.get('name') == 'og:url':
            content_val = meta.get('content')
            if content_val:
                resolved = resolve_local_path(content_val)
                if resolved == "RELATIVE":
                    resolved = os.path.abspath(os.path.join(file_dir, content_val.split('?')[0].split('#')[0].strip()))
                if resolved and not os.path.exists(resolved):
                    broken_links.append(content_val)
                    
    if broken_links:
        check1_results.append((rel_file, sorted(list(set(broken_links)))))
    else:
        check1_results.append((rel_file, []))
        
    # Check 2: Missing Images
    missing_imgs = []
    file_images = []
    
    # img src
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            file_images.append(src)
            
    # source srcset
    for source in soup.find_all('source'):
        srcset = source.get('srcset')
        if srcset:
            file_images.extend(parse_srcset(srcset))
            
    # style url(...)
    for tag in soup.find_all(style=True):
        style_content = tag.get('style')
        matches = url_in_style_re.findall(style_content)
        file_images.extend(matches)
        
    # og:image
    for meta in soup.find_all('meta'):
        if meta.get('property') == 'og:image' or meta.get('name') == 'og:image':
            content_val = meta.get('content')
            if content_val:
                if content_val.startswith("https://www.securevision.com.sg"):
                    content_val = content_val[len("https://www.securevision.com.sg"):]
                file_images.append(content_val)
                
    # data-src
    for tag in soup.find_all(attrs={"data-src": True}):
        data_src = tag.get('data-src')
        if data_src:
            file_images.append(data_src)
            
    # Validate existences
    for img_path in file_images:
        img_path = img_path.strip().replace('"', '').replace("'", "")
        if not img_path:
            continue
        if img_path in img_exclusions:
            continue
        if img_path.startswith(('http://', 'https://', '//')):
            continue
            
        if img_path.startswith('/'):
            full_img_path = os.path.join(repo_root, img_path.lstrip('/'))
        else:
            full_img_path = os.path.join(file_dir, img_path)
            
        full_img_path = os.path.abspath(full_img_path)
        if not os.path.exists(full_img_path):
            missing_imgs.append(img_path)
            
    if missing_imgs:
        check2_results.append((rel_file, sorted(list(set(missing_imgs)))))
    else:
        check2_results.append((rel_file, []))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RUN CHECK 3
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# List every file in /images/solutions/ and all its subfolders recursively
images_solutions_files = []
for root, dirs, files in os.walk(images_sol_dir):
    for f in files:
        images_solutions_files.append(os.path.join(root, f))
images_solutions_files.sort()

check3_unused = []
check3_used_log = []

for filepath in images_solutions_files:
    rel_path = "/" + os.path.relpath(filepath, repo_root).replace('\\', '/')
    filename = os.path.basename(filepath)
    
    # Check if filename is in ANY html file sitewide
    is_used = False
    ref_files = []
    
    # Search HTML files
    for html_rel, html_content in html_contents.items():
        if filename in html_content:
            is_used = True
            ref_files.append(html_rel)
            
    # If in hero-solutions subfolder, check CSS files sitewide
    is_in_hero_solutions = "hero-solutions" in filepath.split(os.sep)
    if is_in_hero_solutions:
        for css_rel, css_content in css_contents.items():
            if filename in css_content:
                is_used = True
                ref_files.append(css_rel)
                
    if is_used:
        check3_used_log.append((rel_path, sorted(ref_files)))
    else:
        check3_unused.append(rel_path)

# Write output file
output_path = r"c:\Projects\SV-Build\scratch\audit_full_solutions_output.txt"
with open(output_path, 'w', encoding='utf-8') as out_f:
    # Check 1 formatting
    out_f.write("CHECK 1 — BROKEN LINKS:\n")
    broken_files_count = 0
    for file_rel, broken in check1_results:
        if broken:
            broken_files_count += 1
            for b in broken:
                out_f.write(f"  {file_rel} — BROKEN LINK: {b}\n")
        else:
            out_f.write(f"  {file_rel} — OK\n")
    out_f.write(f"  Summary: {broken_files_count} files with broken links\n\n")
    
    # Check 2 formatting
    out_f.write("CHECK 2 — MISSING IMAGES:\n")
    missing_files_count = 0
    for file_rel, missing in check2_results:
        if missing:
            missing_files_count += 1
            for m in missing:
                out_f.write(f"  {file_rel} — MISSING IMAGE: {m}\n")
        else:
            out_f.write(f"  {file_rel} — OK\n")
    out_f.write(f"  Summary: {missing_files_count} files with missing images\n\n")
    
    # Check 3 formatting
    out_f.write("CHECK 3 — UNUSED FILES:\n")
    for unused in check3_unused:
        out_f.write(f"  {unused}\n")
    out_f.write(f"  Summary: {len(check3_unused)} unused files found\n\n")
    
    # Flag reduce-guard-manpower.html
    stray_html_path = "/images/solutions/reduce-guard-manpower.html"
    stray_exists = os.path.exists(os.path.join(repo_root, stray_html_path.lstrip('/')))
    out_f.write("STRAY FILE FLAG:\n")
    if stray_exists:
        out_f.write(f"  STRAY HTML FILE DETECTED: {stray_html_path} (This file should be deleted)\n")
    else:
        out_f.write("  No stray HTML files detected in the images folder.\n")
