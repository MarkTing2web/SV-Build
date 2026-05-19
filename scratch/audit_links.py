import os
import re
import urllib.parse

repo_root = r"c:\Projects\SV-Build"
insights_dir = os.path.join(repo_root, "insights")

html_files = []
for root, dirs, files in os.walk(insights_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

ignored_images = {
    '/images/ler-wee-meng-bio.webp',
    '/images/insights/securevision-insights.webp',
    '/images/insights/securevision-insights-mobile.webp'
}

re_img_src = re.compile(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]')
re_bg_url = re.compile(r'background-image:\s*url\([\'"]?([^\'"\)]+)[\'"]?\)')
re_og_image = re.compile(r'<meta[^>]+property=[\'"]og:image[\'"][^>]+content=[\'"]([^\'"]+)[\'"]')
re_og_image2 = re.compile(r'<meta[^>]+content=[\'"]([^\'"]+)[\'"][^>]+property=[\'"]og:image[\'"]')

re_a_href = re.compile(r'<a[^>]+href=[\'"]([^\'"]+)[\'"]')
re_canonical = re.compile(r'<link[^>]+rel=[\'"]canonical[\'"][^>]+href=[\'"]([^\'"]+)[\'"]')
re_canonical2 = re.compile(r'<link[^>]+href=[\'"]([^\'"]+)[\'"][^>]+rel=[\'"]canonical[\'"]')
re_og_url = re.compile(r'<meta[^>]+property=[\'"]og:url[\'"][^>]+content=[\'"]([^\'"]+)[\'"]')
re_og_url2 = re.compile(r'<meta[^>]+content=[\'"]([^\'"]+)[\'"][^>]+property=[\'"]og:url[\'"]')

output_lines = []

all_missing_images = set()
all_broken_links = set()

files_with_missing_images = 0
files_with_broken_links = 0

def resolve_path(url, filepath):
    if url.startswith('http://') or url.startswith('https://'):
        if 'securevision.com.sg' in url:
            url = urllib.parse.urlparse(url).path
        else:
            return None
            
    if url.startswith('mailto:') or url.startswith('tel:') or url.startswith('#') or url.startswith('https://wa.me/'):
        return None
        
    url = url.split('?')[0].split('#')[0]
    
    if not url:
        return None
        
    url = urllib.parse.unquote(url)
    
    if url.startswith('/'):
        abs_disk_path = os.path.join(repo_root, url.lstrip('/'))
    else:
        abs_disk_path = os.path.join(os.path.dirname(filepath), url)
        
    abs_disk_path = os.path.normpath(abs_disk_path)
    return abs_disk_path

for filepath in sorted(html_files):
    rel_filepath = os.path.relpath(filepath, repo_root)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    found_images = set()
    for m in re_img_src.finditer(content): found_images.add(m.group(1))
    for m in re_bg_url.finditer(content): found_images.add(m.group(1))
    for m in re_og_image.finditer(content): found_images.add(m.group(1))
    for m in re_og_image2.finditer(content): found_images.add(m.group(1))
    
    found_links = set()
    for m in re_a_href.finditer(content):
        if m.group(1).startswith('/'):
            found_links.add(m.group(1))
    for m in re_canonical.finditer(content): found_links.add(m.group(1))
    for m in re_canonical2.finditer(content): found_links.add(m.group(1))
    for m in re_og_url.finditer(content): found_links.add(m.group(1))
    for m in re_og_url2.finditer(content): found_links.add(m.group(1))
    
    file_missing_images = []
    file_broken_links = []
    
    for img_url in found_images:
        if img_url in ignored_images:
            continue
            
        abs_disk_path = resolve_path(img_url, filepath)
        if abs_disk_path:
            if not os.path.exists(abs_disk_path):
                file_missing_images.append(img_url)
                all_missing_images.add(img_url)
                
    for link_url in found_links:
        abs_disk_path = resolve_path(link_url, filepath)
        if abs_disk_path:
            if not os.path.exists(abs_disk_path):
                file_broken_links.append(link_url)
                all_broken_links.add(link_url)
                
    if file_missing_images or file_broken_links:
        output_lines.append(f"{rel_filepath}")
        for mi in file_missing_images:
            output_lines.append(f"  MISSING IMAGE: {mi}")
        for bl in file_broken_links:
            output_lines.append(f"  BROKEN LINK: {bl}")
            
        if file_missing_images:
            files_with_missing_images += 1
        if file_broken_links:
            files_with_broken_links += 1
    else:
        output_lines.append(f"{rel_filepath} — OK")

print("\n".join(output_lines))
print("\n--- SUMMARY ---")
print(f"Total files scanned: {len(html_files)}")
print(f"Files with missing images: {files_with_missing_images}")
print(f"Files with broken links: {files_with_broken_links}")
print(f"Total missing images (deduplicated): {len(all_missing_images)}")
print(f"Total broken links (deduplicated): {len(all_broken_links)}")

print("\n--- MISSING IMAGES ---")
if not all_missing_images:
    print("None")
else:
    for m in sorted(list(all_missing_images)):
        print(f"  {m}")
        
print("\n--- BROKEN LINKS ---")
if not all_broken_links:
    print("None")
else:
    for m in sorted(list(all_broken_links)):
        print(f"  {m}")
