import os
import re
from pathlib import Path
from datetime import datetime

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
images_dir = os.path.join(repo_root, "images")
ai_dir = os.path.join(repo_root, "_ai")
os.makedirs(ai_dir, exist_ok=True)

# Regex patterns
patterns = [
    r'src\s*=\s*["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']',
    r'url\(\s*["\']?([^"\')]+\.(?:webp|jpg|jpeg|png|gif|svg))["\']?\s*\)',
    r'content\s*=\s*["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']',
    r'data-src\s*=\s*["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']',
]

code_extensions = {'.html', '.css', '.js'}
image_extensions = {'.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg'}

used_refs = []

def normalize_path(path):
    # Remove domain
    path = re.sub(r'^https?://[^/]+', '', path)
    # Remove query params
    path = path.split('?')[0].split('#')[0]
    
    # Handle absolute paths
    if path.startswith('/images/'):
        return path
    
    # Handle relative paths like ../images/ or images/
    parts = path.split('/')
    if 'images' in parts:
        idx = parts.index('images')
        return '/' + '/'.join(parts[idx:])
    
    return path # Just return whatever it is if we can't figure it out, could be just a filename

for root, dirs, files in os.walk(repo_root):
    if 'node_modules' in root or '.git' in root or 'scratch' in root or '_ai' in root:
        continue
    for file in files:
        if Path(file).suffix.lower() in code_extensions:
            file_path = os.path.join(root, file)
            is_template = '_template-' in file
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for pattern in patterns:
                        for match in re.finditer(pattern, content, re.IGNORECASE):
                            raw_ref = match.group(1)
                            norm_ref = normalize_path(raw_ref)
                            used_refs.append({
                                'raw': raw_ref,
                                'normalized': norm_ref,
                                'file': os.path.relpath(file_path, repo_root).replace('\\', '/'),
                                'is_template': is_template
                            })
            except Exception:
                pass

# Find all images on disk
disk_images = []
if os.path.exists(images_dir):
    for root, dirs, files in os.walk(images_dir):
        for file in files:
            if Path(file).suffix.lower() in image_extensions:
                full_path = os.path.join(root, file)
                rel_path = '/' + os.path.relpath(full_path, repo_root).replace('\\', '/')
                stat = os.stat(full_path)
                disk_images.append({
                    'full_path': full_path,
                    'rel_path': rel_path,
                    'size_bytes': stat.st_size,
                    'mtime': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                    'filename': file
                })

# Analyze
used_categories = []
unused_categories = []
uncertain_categories = []

used_norm_paths = {r['normalized'] for r in used_refs if r['normalized'].startswith('/images/')}
used_filenames = {os.path.basename(r['normalized']) for r in used_refs}

for disk_img in disk_images:
    if disk_img['rel_path'] == '/images/og-default.jpg' or disk_img['rel_path'] in used_norm_paths:
        disk_img['is_template_only'] = False
        # Check if ONLY referenced by template
        refs = [r for r in used_refs if r['normalized'] == disk_img['rel_path']]
        if refs and all(r['is_template'] for r in refs):
            disk_img['is_template_only'] = True
        used_categories.append(disk_img)
    else:
        # Check if filename is used anywhere
        if disk_img['filename'] in used_filenames:
            # UNCERTAIN
            refs = [r for r in used_refs if os.path.basename(r['normalized']) == disk_img['filename']]
            disk_img['uncertain_refs'] = refs
            uncertain_categories.append(disk_img)
        else:
            unused_categories.append(disk_img)

# Generate Markdown
report = ["# Image Audit & Cleanup Phase 1 Report\n"]

report.append("## Section A: Summary")
report.append(f"- Total images on disk: {len(disk_images)}")
report.append(f"- Total images referenced in code (USED): {len(used_categories)}")
report.append(f"- Total images not referenced (UNUSED): {len(unused_categories)}")
report.append(f"- Total flagged for manual review (UNCERTAIN): {len(uncertain_categories)}")

freed_bytes = sum(img['size_bytes'] for img in unused_categories)
report.append(f"- Total disk space that would be freed by deleting UNUSED images: {freed_bytes / (1024*1024):.2f} MB\n")

report.append("## Section B: UNUSED Images — Candidates for Deletion")
report.append("| File Path | File Size | Last Modified | Reason Flagged |")
report.append("|---|---|---|---|")
unused_categories.sort(key=lambda x: x['rel_path'])
for img in unused_categories:
    size_kb = img['size_bytes'] / 1024
    report.append(f"| `{img['rel_path']}` | {size_kb:.1f} KB | {img['mtime']} | Not referenced in any scanned code file |")

report.append("\n## Section C: UNCERTAIN Images — Manual Review Required")
report.append("| File Path | Referenced As | Issue |")
report.append("|---|---|---|")
for img in uncertain_categories:
    refs_str = "<br>".join(set([f"`{r['raw']}` in `{r['file']}`" for r in img['uncertain_refs']]))
    report.append(f"| `{img['rel_path']}` | {refs_str} | Filename matches a reference, but the path is ambiguous |")

report.append("\n## Section D: USED Images — Confirmed Keep")
used_categories.sort(key=lambda x: x['rel_path'])
current_dir = ""
for img in used_categories:
    dirname = os.path.dirname(img['rel_path'])
    if dirname != current_dir:
        report.append(f"\n### {dirname}")
        current_dir = dirname
    
    note = " *(referenced only in templates)*" if img.get('is_template_only') else ""
    report.append(f"- `{img['filename']}`{note}")

with open(os.path.join(ai_dir, 'image-audit-report.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(report))

print("Report generated successfully.")
