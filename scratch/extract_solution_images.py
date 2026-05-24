import os
import re
from bs4 import BeautifulSoup

solutions_dir = r"c:\Projects\SV-Build\solutions"
domain_to_strip = "https://www.securevision.com.sg"
excluded_image = "/images/ler-wee-meng-bio.webp"

# Regex for extracting URL from CSS background-image inline styles
url_in_style_re = re.compile(r'url\(\s*[\'"]?([^\'")\s]+)[\'"]?\s*\)', re.IGNORECASE)

all_unique_images = set()
results = []

def parse_srcset(srcset_val):
    if not srcset_val:
        return []
    urls = []
    # Split by comma
    parts = srcset_val.split(',')
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Split by whitespace, the first token is the URL
        url_part = part.split()[0]
        urls.append(url_part)
    return urls

# Recursively find all HTML files
html_files = []
for root, dirs, files in os.walk(solutions_dir):
    for f in files:
        if f.lower().endswith('.html'):
            html_files.append(os.path.join(root, f))

# Sort the HTML files so the output is consistent
html_files.sort()

for filepath in html_files:
    # Compute relative path from solutions_dir's parent
    rel_path = os.path.relpath(filepath, start=os.path.dirname(solutions_dir))
    # Replace backslashes with forward slashes for output consistency
    rel_path = rel_path.replace('\\', '/')
    
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
    # We will search style attribute on all tags
    for tag in soup.find_all(style=True):
        style_content = tag.get('style')
        # We look for url(...) inside style
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
                file_images.append(('og_image', content_val))
                
    # 5. data-src= attributes
    for tag in soup.find_all(attrs={"data-src": True}):
        data_src = tag.get('data-src')
        if data_src:
            file_images.append(('data_src', data_src))
            
    # Process the gathered images for this file
    cleaned_file_images = []
    for source_type, img_path in file_images:
        # If it's og:image, strip the domain https://www.securevision.com.sg
        if source_type == 'og_image':
            if img_path.startswith(domain_to_strip):
                img_path = img_path[len(domain_to_strip):]
        
        # Check exclusion criteria
        # Do NOT include:
        # - External URLs (http:// or https://)
        # - /images/ler-wee-meng-bio.webp
        if img_path.startswith('http://') or img_path.startswith('https://') or img_path.startswith('//'):
            continue
        if img_path == excluded_image:
            continue
            
        cleaned_file_images.append(img_path)
        all_unique_images.add(img_path)
        
    if cleaned_file_images:
        results.append((rel_path, cleaned_file_images))

# Now write to file
output_path = r"c:\Projects\SV-Build\scratch\extract_solution_images_output.txt"
with open(output_path, 'w', encoding='utf-8') as out_f:
    for rel_path, imgs in results:
        out_f.write(f"FILE: {rel_path}\n")
        for img in imgs:
            out_f.write(f"  {img}\n")
        out_f.write("\n")

    out_f.write("ALL UNIQUE IMAGE PATHS:\n")
    sorted_unique = sorted(list(all_unique_images))
    for img in sorted_unique:
        out_f.write(f"{img}\n")
    out_f.write("\n")
    out_f.write(f"Total count: {len(sorted_unique)}\n")

