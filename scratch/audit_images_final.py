import os
import posixpath
import re
from collections import defaultdict

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
images_dir = os.path.join(repo_root, "images")
ai_dir = os.path.join(repo_root, "_ai")
os.makedirs(ai_dir, exist_ok=True)

image_extensions = {'.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg'}
code_extensions = {'.html', '.css', '.js'}
base_url = "https://www.securevision.com.sg"

disk_images = {}
for root, dirs, files in os.walk(images_dir):
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext in image_extensions:
            full_path = os.path.join(root, f)
            rel_path = '/' + os.path.relpath(full_path, repo_root).replace('\\', '/')
            disk_images[rel_path] = os.path.getsize(full_path)

references = defaultdict(list)
pattern = re.compile(r'(?:src=|content=|data-src=|href=)["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']|url\([\'"]?([^\'"\)]+\.(?:webp|jpg|jpeg|png|gif|svg))[\'"]?\)', re.IGNORECASE)

for root, dirs, files in os.walk(repo_root):
    if any(x in root for x in ['node_modules', '.git', 'scratch', '_ai']):
        continue
        
    for f in files:
        if any(f.endswith(ext) for ext in code_extensions):
            file_path = os.path.join(root, f)
            rel_file = '/' + os.path.relpath(file_path, repo_root).replace('\\', '/')
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
                
                for match in pattern.finditer(content):
                    img_path = match.group(1) or match.group(2)
                    if not img_path: continue
                    
                    if img_path.startswith(base_url):
                        img_path = img_path[len(base_url):]
                    elif img_path.startswith('http://') or img_path.startswith('https://') or img_path.startswith('data:'):
                        continue
                        
                    if not img_path.startswith('/'):
                        file_dir = posixpath.dirname(rel_file)
                        img_path = posixpath.normpath(posixpath.join(file_dir, img_path))
                        
                    img_path = img_path.split('?')[0].split('#')[0]
                    
                    references[img_path].append(rel_file)

used_images = {}
unused_images = {}
broken_images = defaultdict(list)

for img_path in disk_images:
    if img_path in references:
        used_images[img_path] = disk_images[img_path]
    else:
        if img_path != '/images/og-default.jpg':
            unused_images[img_path] = disk_images[img_path]

for img_path, files in references.items():
    if img_path not in disk_images and img_path.startswith('/images/'):
        for f in files:
            broken_images[img_path].append(f)

broken_list = []
for img, files in broken_images.items():
    for f in set(files):
        broken_list.append((f, img))
broken_list.sort(key=lambda x: (x[0], x[1]))

lines = []
lines.append("# Final Image Audit Report")

total_unused_size = sum(unused_images.values()) / (1024 * 1024)

lines.append("\n## Section A: Summary")
lines.append(f"- **Total images on disk**: {len(disk_images)}")
lines.append(f"- **Total USED**: {len(used_images)}")
lines.append(f"- **Total UNUSED**: {len(unused_images)} (Estimated {total_unused_size:.2f} MB)")
lines.append(f"- **Total BROKEN (urgent)**: {len(broken_list)}")

lines.append("\n## Section B: BROKEN images — urgent")
if broken_list:
    lines.append("| Page With Reference | Image Path Expected |")
    lines.append("|---|---|")
    for page, img in broken_list:
        lines.append(f"| {page} | {img} |")
else:
    lines.append("No broken image references found!")

lines.append("\n## Section C: UNUSED images — candidates for deletion")
if unused_images:
    lines.append("| File Path | File Size | Folder |")
    lines.append("|---|---|---|")
    
    unused_by_folder = defaultdict(list)
    for img, size in unused_images.items():
        folder = posixpath.dirname(img)
        unused_by_folder[folder].append((img, size))
        
    for folder in sorted(unused_by_folder.keys()):
        for img, size in sorted(unused_by_folder[folder]):
            kb_size = size / 1024
            lines.append(f"| {img} | {kb_size:.1f} KB | {folder} |")
else:
    lines.append("No unused images found!")

lines.append("\n## Section D: USED — confirmed keep")
if used_images:
    used_by_folder = defaultdict(list)
    for img in used_images:
        folder = posixpath.dirname(img)
        used_by_folder[folder].append(img)
        
    for folder in sorted(used_by_folder.keys()):
        lines.append(f"### {folder}")
        for img in sorted(used_by_folder[folder]):
            lines.append(f"- {img}")
else:
    lines.append("No used images found?")

report_path = os.path.join(ai_dir, "image-audit-final.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Report successfully saved to {report_path}")
