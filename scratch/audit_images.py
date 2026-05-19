import os
import glob
import re
import urllib.parse

repo_root = r"c:\Projects\SV-Build"
insights_dir = os.path.join(repo_root, "insights")

html_files = []
for root, dirs, files in os.walk(insights_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

image_exts = {'.jpg', '.jpeg', '.png', '.webp', '.jfif', '.gif', '.svg'}

total_html_scanned = len(html_files)
total_images_found = 0
total_missing_images = 0
all_missing_images = set()

re_img_src = re.compile(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]')
re_source_srcset = re.compile(r'<source[^>]+srcset=[\'"]([^\'"]+)[\'"]')
re_bg_url = re.compile(r'background-image:\s*url\([\'"]?([^\'"\)]+)[\'"]?\)')
re_og_image = re.compile(r'<meta[^>]+property=[\'"]og:image[\'"][^>]+content=[\'"]([^\'"]+)[\'"]')
re_og_image2 = re.compile(r'<meta[^>]+content=[\'"]([^\'"]+)[\'"][^>]+property=[\'"]og:image[\'"]')

output_lines = []

for filepath in sorted(html_files):
    rel_filepath = os.path.relpath(filepath, repo_root)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    found_paths = set()
    
    for m in re_img_src.finditer(content):
        found_paths.add(m.group(1))
        
    for m in re_source_srcset.finditer(content):
        srcset = m.group(1)
        for part in srcset.split(','):
            path = part.strip().split(' ')[0]
            if path:
                found_paths.add(path)
                
    for m in re_bg_url.finditer(content):
        found_paths.add(m.group(1))
        
    for m in re_og_image.finditer(content):
        found_paths.add(m.group(1))
    for m in re_og_image2.finditer(content):
        found_paths.add(m.group(1))
        
    file_images_total = 0
    file_missing_list = []
    
    for raw_path in found_paths:
        path = raw_path
        if path.startswith('http://') or path.startswith('https://'):
            if 'securevision.com.sg' in path:
                parsed = urllib.parse.urlparse(path)
                path = parsed.path
            else:
                continue 
                
        parsed_path = urllib.parse.urlparse(path).path
        ext = os.path.splitext(parsed_path)[1].lower()
        if ext not in image_exts:
            continue
            
        file_images_total += 1
        
        if path.startswith('/'):
            abs_disk_path = os.path.join(repo_root, path.lstrip('/'))
        else:
            abs_disk_path = os.path.join(os.path.dirname(filepath), path)
            
        abs_disk_path = abs_disk_path.split('?')[0].split('#')[0]
        abs_disk_path = urllib.parse.unquote(abs_disk_path)
        abs_disk_path = os.path.normpath(abs_disk_path)
        
        if not os.path.exists(abs_disk_path):
            file_missing_list.append(raw_path)
            all_missing_images.add(raw_path)
            
    total_images_found += file_images_total
    total_missing_images += len(file_missing_list)
    
    if len(file_missing_list) == 0:
        output_lines.append(f"{rel_filepath} — OK")
    else:
        output_lines.append(f"{rel_filepath} — MISSING {len(file_missing_list)} of {file_images_total}")
        for mp in file_missing_list:
            output_lines.append(f"  - {mp}")

print("\n".join(output_lines))

print("\n--- SUMMARY ---")
print(f"Total HTML files scanned: {total_html_scanned}")
print(f"Total image references found: {total_images_found}")
print(f"Total missing images: {total_missing_images}")

print("\nAll missing images (deduplicated):")
if not all_missing_images:
    print("  (None)")
else:
    for m in sorted(list(all_missing_images)):
        print(f"  - {m}")
