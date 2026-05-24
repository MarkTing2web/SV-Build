import os
import re
from bs4 import BeautifulSoup

repo_root = r"c:\Projects\SV-Build"
solutions_dir = os.path.join(repo_root, "solutions")
domain_to_strip = "https://www.securevision.com.sg"

# Exclusions
exclusions = [
    "/images/ler-wee-meng-bio.webp",
    "/images/og-default.jpg"
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

def is_excluded(ref):
    if ref in exclusions:
        return True
    if ref.startswith('http://') or ref.startswith('https://') or ref.startswith('//'):
        return True
    return False

# Recursively find all HTML files under solutions/
html_files = []
for root, dirs, files in os.walk(solutions_dir):
    for f in files:
        if f.lower().endswith('.html'):
            html_files.append(os.path.join(root, f))

html_files.sort()

all_missing_images = set()
files_with_missing = 0
results = []

for filepath in html_files:
    rel_path_from_solutions = os.path.relpath(filepath, solutions_dir).replace('\\', '/')
    # For file-specific output, let's get the filename (or relative path starting with solutions/)
    # Wait, the prompt says:
    # "For each file:
    #   filename — MISSING IMAGE: /path
    #   filename — OK"
    # Wait, does 'filename' mean the filename (like condominiums.html) or the path (like solutions/condominiums.html)?
    # Let's check the examples in Task 1 output format:
    # "FILE: solutions/[path]/[filename].html"
    # Here the prompt says "filename — MISSING IMAGE: /path".
    # Let's compute the relative path starting with solutions/ for clarity, e.g. solutions/condominiums.html,
    # or the basename. Let's output "solutions/path/filename.html" as the filename, which is clearer and avoids duplicate names.
    # Wait! Let's check if the prompt says "For each file: filename — MISSING IMAGE: /path".
    # Let's use the relative path starting with solutions/, e.g., "solutions/condominiums.html",
    # or let's use the basename? Let's check: "All .html files in /solutions/ and all its subfolders recursively."
    # If we have solutions/commercial/office.html, solutions/commercial/hotel.html,solutions/managed-living/dormitories.html,
    # using solutions/[path] makes sure it is distinct. Let's output `solutions/[path]/[filename].html`.
    rel_path = os.path.relpath(filepath, repo_root).replace('\\', '/')
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    file_images = []
    
    # 1. <img src="...">
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            file_images.append(('img_src', src))
            
    # 2. <source srcset="...">
    for source in soup.find_all('source'):
        srcset = source.get('srcset')
        if srcset:
            for url in parse_srcset(srcset):
                file_images.append(('source_srcset', url))
                
    # 3. CSS background-image: url('...') inline styles
    for tag in soup.find_all(style=True):
        style_content = tag.get('style')
        matches = url_in_style_re.findall(style_content)
        for match in matches:
            file_images.append(('css_bg', match))
            
    # 4. og:image meta content attributes
    for meta in soup.find_all('meta'):
        is_og_image = False
        if meta.get('property') == 'og:image' or meta.get('name') == 'og:image':
            is_og_image = True
        if is_og_image:
            content_val = meta.get('content')
            if content_val:
                if content_val.startswith(domain_to_strip):
                    content_val = content_val[len(domain_to_strip):]
                file_images.append(('og_image', content_val))
                
    # 5. data-src= attributes
    for tag in soup.find_all(attrs={"data-src": True}):
        data_src = tag.get('data-src')
        if data_src:
            file_images.append(('data_src', data_src))
            
    # Validate each image
    missing_in_file = []
    for source_type, img_path in file_images:
        # Clean paths (strip whitespaces, quotes, etc)
        img_path = img_path.strip().replace('"', '').replace("'", "")
        if is_excluded(img_path):
            continue
            
        # Determine existence
        if img_path.startswith('/'):
            full_img_path = os.path.join(repo_root, img_path.lstrip('/'))
        else:
            full_img_path = os.path.join(os.path.dirname(filepath), img_path)
            
        full_img_path = os.path.abspath(full_img_path)
        if not os.path.exists(full_img_path):
            missing_in_file.append(img_path)
            all_missing_images.add(img_path)
            
    if missing_in_file:
        files_with_missing += 1
        for m in missing_in_file:
            results.append((rel_path, f"{rel_path} — MISSING IMAGE: {m}"))
    else:
        results.append((rel_path, f"{rel_path} — OK"))

output_file = r"c:\Projects\SV-Build\scratch\audit_solution_images_output.txt"
with open(output_file, 'w', encoding='utf-8') as out_f:
    # Print reports
    for rel_path, line in results:
        out_f.write(f"{line}\n")
    out_f.write("\n")
    # Print summary
    out_f.write(f"Total files scanned: {len(html_files)}\n")
    out_f.write(f"Files with missing images: {files_with_missing}\n")
    out_f.write(f"Total missing images (deduplicated): {len(all_missing_images)}\n")
    out_f.write("\nFull list of all missing images:\n")
    for img in sorted(list(all_missing_images)):
        out_f.write(f"  {img}\n")
