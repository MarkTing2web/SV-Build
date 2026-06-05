import os
import re
from collections import defaultdict

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
images_dir = os.path.join(repo_root, "images")

# Excluded directories for code scanning
exclude_dirs = ['templates', 'node_modules', '.git', 'scratch', '_ai']
img_exts = ('.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg')

# 1. Collect all image references from code
code_files = []
for root, _, files in os.walk(repo_root):
    # Check if root contains any excluded dir
    rel_root = os.path.relpath(root, repo_root).replace('\\', '/')
    if any(ex in rel_root.split('/') for ex in exclude_dirs):
        continue
    for f in files:
        if f.endswith(('.html', '.css', '.js')):
            code_files.append(os.path.join(root, f))

# Regex to catch various reference forms
img_patterns = [
    re.compile(r'src=["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']', re.IGNORECASE),
    re.compile(r'url\([\'"]?([^\'"\)]+\.(?:webp|jpg|jpeg|png|gif|svg))[\'"]?\)', re.IGNORECASE),
    re.compile(r'content=["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']', re.IGNORECASE),
    re.compile(r'data-src=["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']', re.IGNORECASE)
]

referenced_images = set()

for cf in code_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    for pattern in img_patterns:
        matches = pattern.findall(content)
        for match in matches:
            # Normalize to /images/...
            match_lower = match.lower()
            if '/images/' in match_lower:
                idx = match_lower.find('/images/')
                rel_path = match[idx:]
                referenced_images.add(rel_path)
            elif 'images/' in match_lower:
                idx = match_lower.find('images/')
                rel_path = '/' + match[idx:]
                referenced_images.add(rel_path)
            elif match.startswith('http'):
                # Extract if it's pointing to the site itself
                if 'securevision.com.sg/images/' in match_lower:
                    idx = match_lower.find('/images/')
                    referenced_images.add(match[idx:])

# 2. Collect all images on disk
images_on_disk = {}
for root, _, files in os.walk(images_dir):
    for f in files:
        if f.lower().endswith(img_exts):
            full_path = os.path.join(root, f)
            rel_path = '/' + os.path.relpath(full_path, repo_root).replace('\\', '/')
            images_on_disk[rel_path] = os.path.getsize(full_path)

# 3. Classify
used = set()
unused = [] # list of tuples (rel_path, size)

for img_path, size in images_on_disk.items():
    if img_path in referenced_images:
        used.add(img_path)
    else:
        # Exclude og-default.jpg
        if img_path != '/images/og-default.jpg':
            unused.append((img_path, size))

# Group UNUSED
grouped_unused = defaultdict(list)
total_unused_size = 0

for img_path, size in unused:
    total_unused_size += size
    folder = os.path.dirname(img_path)
    grouped_unused[folder].append({'path': img_path, 'size': size})

total_on_disk = len(images_on_disk)
total_used = len([img for img in images_on_disk.keys() if img in referenced_images or img == '/images/og-default.jpg'])
total_unused = len(unused)
unused_mb = total_unused_size / (1024 * 1024)

# 4. Output
report = [
    "### Section A: Summary",
    f"- Total images on disk: {total_on_disk}",
    f"- Total USED: {total_used} (including intentional defaults)",
    f"- Total UNUSED: {total_unused} (Estimated disk space: {unused_mb:.2f} MB)",
    "",
    "### Section B: UNUSED images only"
]

for folder in sorted(grouped_unused.keys()):
    report.append(f"\n#### {folder}/")
    report.append("| File Path | File Size |")
    report.append("|---|---|")
    for item in sorted(grouped_unused[folder], key=lambda x: x['path']):
        size_kb = item['size'] / 1024
        report.append(f"| `{os.path.basename(item['path'])}` | {size_kb:.1f} KB |")

report.append("\n### Section C: Confirmation")
report.append("All other images are confirmed referenced.")

report_content = "\n".join(report)

report_path = os.path.join(repo_root, "_ai", "unused-images-final.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write(report_content)

print(f"Report saved to _ai/unused-images-final.md")
print(f"Total on disk: {total_on_disk}")
print(f"Total used: {total_used}")
print(f"Total unused: {total_unused}")
