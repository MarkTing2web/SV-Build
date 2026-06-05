import os
import re
from collections import defaultdict

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
images_dir = os.path.join(repo_root, "images")
ai_dir = os.path.join(repo_root, "_ai")
os.makedirs(ai_dir, exist_ok=True)

code_extensions = {'.html', '.css', '.js'}
image_extensions = {'.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg'}

patterns = [
    r'src\s*=\s*["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']',
    r'url\(\s*["\']?([^"\')]+\.(?:webp|jpg|jpeg|png|gif|svg))["\']?\s*\)',
    r'content\s*=\s*["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']',
    r'data-src\s*=\s*["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']',
]

def normalize_path(path):
    path = re.sub(r'^https?://www\.securevision\.com\.sg', '', path)
    path = path.split('?')[0].split('#')[0]
    return path

# 1. Collect all images on disk
images_on_disk = {}
filename_to_paths = defaultdict(list)
for root, dirs, files in os.walk(images_dir):
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext in image_extensions:
            full_path = os.path.join(root, f)
            rel_path = '/' + os.path.relpath(full_path, repo_root).replace('\\', '/')
            images_on_disk[rel_path] = os.path.getsize(full_path)
            filename_to_paths[f].append(rel_path)

# 2. Collect all references
references = []
for root, dirs, files in os.walk(repo_root):
    if any(x in root for x in ['node_modules', '.git', 'scratch', '_ai']):
        continue
    for f in files:
        if any(f.endswith(ext) for ext in code_extensions):
            file_path = os.path.join(root, f)
            rel_file = '/' + os.path.relpath(file_path, repo_root).replace('\\', '/')
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file_obj:
                    content = file_obj.read()
                    for pattern in patterns:
                        for match in re.finditer(pattern, content, re.IGNORECASE):
                            raw = match.group(1)
                            norm = normalize_path(raw)
                            references.append({'file': rel_file, 'raw_ref': raw, 'norm_ref': norm})
            except Exception:
                pass

# 3. Classify
used = set()
broken = []
uncertain = []

for ref in references:
    norm = ref['norm_ref']
    src_file = ref['file']
    filename = os.path.basename(norm)
    
    if norm.startswith('/images/'):
        resolved_path = norm
    else:
        parts = norm.split('/')
        if 'images' in parts:
            resolved_path = '/' + '/'.join(parts[parts.index('images'):])
        else:
            resolved_path = norm
            
    if resolved_path in images_on_disk:
        used.add(resolved_path)
    else:
        found_elsewhere = filename_to_paths.get(filename, [])
        if found_elsewhere:
            uncertain.append({
                'file': src_file,
                'ref': norm,
                'issue': f"File not at {resolved_path}, but found at: {', '.join(found_elsewhere)}"
            })
            for p in found_elsewhere:
                used.add(p)
        else:
            broken.append({
                'file': src_file,
                'expected': resolved_path,
                'elsewhere': "NO"
            })

unused = {p: s for p, s in images_on_disk.items() if p not in used}

# Prepare report
lines = []
lines.append("# Full Image Audit Report (v2)")
lines.append("\n## Section A: Summary")
lines.append(f"- **Total images on disk**: {len(images_on_disk)}")
lines.append(f"- **Total references found in code**: {len(references)}")
lines.append(f"- **Total BROKEN REFERENCES**: {len(broken)}")
lines.append(f"- **Total UNUSED images**: {len(unused)}")
lines.append(f"- **Total UNCERTAIN references**: {len(uncertain)}")
recoverable_mb = sum(unused.values()) / (1024 * 1024) if unused else 0
lines.append(f"- **Estimated disk space recoverable**: {recoverable_mb:.2f} MB")

lines.append("\n## Section B: BROKEN REFERENCES — urgent")
if broken:
    lines.append("| File With Broken Reference | Image Path Expected | Does File Exist Elsewhere? |")
    lines.append("|---|---|---|")
    broken.sort(key=lambda x: x['file'])
    for b in broken:
        lines.append(f"| {b['file']} | {b['expected']} | {b['elsewhere']} |")
else:
    lines.append("No broken references found!")

lines.append("\n## Section C: UNUSED images — candidates for deletion")
if unused:
    lines.append("| File Path | File Size (KB) | Folder |")
    lines.append("|---|---|---|")
    
    folders = defaultdict(list)
    for p, s in unused.items():
        folder = os.path.dirname(p)
        folders[folder].append((p, s))
        
    for folder in sorted(folders.keys()):
        flag = " 🚩" if "temp" in folder.lower() else ""
        lines.append(f"### {folder}{flag}")
        for p, s in sorted(folders[folder]):
            lines.append(f"| {p} | {s/1024:.1f} | {folder} |")
else:
    lines.append("No unused images found!")

lines.append("\n## Section D: UNCERTAIN — manual review needed")
if uncertain:
    lines.append("| File Path | Referenced As | Issue |")
    lines.append("|---|---|---|")
    for u in uncertain:
        lines.append(f"| {u['file']} | {u['ref']} | {u['issue']} |")
else:
    lines.append("No uncertain references found!")

lines.append("\n## Section E: USED — confirmed keep")
if used:
    used_folders = defaultdict(list)
    for p in used:
        folder = os.path.dirname(p)
        used_folders[folder].append(p)
        
    for folder in sorted(used_folders.keys()):
        lines.append(f"### {folder}")
        for p in sorted(used_folders[folder]):
            lines.append(f"- {p}")
else:
    lines.append("No used images found?")

report_path = os.path.join(ai_dir, "image-audit-report-v2.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Report successfully saved to {report_path}")
