import os
import re
from collections import defaultdict

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
sitemap_path = os.path.join(repo_root, "SITEMAP.md")

# 1. Parse SITEMAP.md for html files
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

live_html_files = []
# Match markdown links: [Text](/path/to/file.html)
# Wait, let's look for any .html paths in SITEMAP.md
for match in re.findall(r'-\s*\[([^\]]+)\]', sitemap_content):
    path = match.strip()
    if path == '/':
        live_html_files.append('index.html')
    elif path.endswith('/'):
        live_html_files.append(path + 'index.html')
    elif path.endswith('.html'):
        live_html_files.append(path)

# Make paths absolute to repo root
live_html_files = [os.path.join(repo_root, path.lstrip('/')) for path in live_html_files]
live_html_files = list(set(live_html_files)) # deduplicate

# Image extensions
img_exts = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg')

# Prepare regexes
html_comment_re = re.compile(r'<!--.*?-->', re.DOTALL)
og_image_re = re.compile(r'<meta[^>]*property=["\']og:image["\'][^>]*>', re.IGNORECASE)

img_src_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
inline_style_re = re.compile(r'style=["\'][^"\']*url\([\'"]?([^\'"\)]+)[\'"]?\)[^"\']*["\']', re.IGNORECASE)

all_images = set()
broken_images = [] # list of dicts: {'html_file': rel_html, 'img_path': img_path}

for html_file in live_html_files:
    if not os.path.exists(html_file):
        continue
        
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Remove HTML comments
    content = html_comment_re.sub('', content)
    # Remove og:image meta tags
    content = og_image_re.sub('', content)
    
    # Extract src from img tags
    srcs = img_src_re.findall(content)
    # Extract url from inline styles
    urls = inline_style_re.findall(content)
    
    found_in_file = srcs + urls
    
    rel_html = os.path.relpath(html_file, repo_root).replace('\\', '/')
    rel_html = '/' + rel_html
    
    for img_path in found_in_file:
        if not img_path.lower().endswith(img_exts):
            continue
        if img_path.startswith('http') or img_path.startswith('data:'):
            continue
            
        all_images.add(img_path)
        
        # Check if exists
        full_img_path = os.path.join(repo_root, img_path.lstrip('/'))
        if not os.path.exists(full_img_path):
            broken_images.append({'html_file': rel_html, 'img_path': img_path})

total_unique = len(all_images)
total_broken_unique = len(set(b['img_path'] for b in broken_images))
total_found_unique = total_unique - total_broken_unique

# Group broken images by section (folder of HTML file)
grouped_broken = defaultdict(list)
for b in broken_images:
    folder = os.path.dirname(b['html_file'])
    if folder == '/': folder = '/root/'
    grouped_broken[folder].append(b)

# Build a map of all images in repo to find if file exists elsewhere
all_repo_images = {}
images_dir = os.path.join(repo_root, 'images')
for root, _, files in os.walk(images_dir):
    for file in files:
        if file.lower().endswith(img_exts):
            all_repo_images[file] = os.path.relpath(os.path.join(root, file), repo_root).replace('\\', '/')

report = [
    "### Section A: Summary",
    f"- Total unique image src paths checked: {total_unique}",
    f"- Total FOUND: {total_found_unique}",
    f"- Total BROKEN: {total_broken_unique}",
    "",
    "### Section B: BROKEN references only",
    "| HTML File | Image src Path | File Exists Elsewhere? |",
    "|---|---|---|"
]

for folder in sorted(grouped_broken.keys()):
    for b in sorted(grouped_broken[folder], key=lambda x: x['html_file']):
        basename = os.path.basename(b['img_path'])
        if basename in all_repo_images:
            elsewhere = f"YES (`/{all_repo_images[basename]}`)"
        else:
            elsewhere = "NO"
            
        report.append(f"| `{b['html_file']}` | `{b['img_path']}` | {elsewhere} |")
        
report.append("")
report.append("### Section C: Confirmation")
if total_broken_unique == 0:
    report.append("All image src references confirmed present on disk.")
else:
    report.append("All other image src references confirmed present on disk.")

report_content = "\n".join(report)

report_path = os.path.join(repo_root, "_ai", "broken-images-final.md")
os.makedirs(os.path.dirname(report_path), exist_ok=True)
with open(report_path, "w", encoding="utf-8") as f:
    f.write(report_content)

print(f"Report saved to _ai/broken-images-final.md")
print(f"Total checked: {total_unique}")
print(f"Total found: {total_found_unique}")
print(f"Total broken: {total_broken_unique}")
