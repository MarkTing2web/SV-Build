import os
import re

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
hero_dir = os.path.join(repo_root, "images", "solutions", "hero-solutions")

mobile_images = [
    "commercial-security-systems-hero-mobile.webp",
    "condominium-security-systems-hero-mobile.webp",
    "data-centre-security-systems-hero-mobile.webp",
    "healthcare-security-systems-hero-mobile.webp",
    "industrial-security-systems-hero-mobile.webp",
    "institutions-security-systems-hero-mobile.webp",
    "managed-living-security-systems-hero-mobile.webp"
]

desktop_images = [img.replace("-mobile", "") for img in mobile_images]
rel_images = [img.replace("-hero-mobile", "-rel") for img in mobile_images] + [img.replace("-hero-mobile", "-hero-rel") for img in mobile_images]

# 1. Catalog all files in /images/
all_images = {}
for root, dirs, files in os.walk(os.path.join(repo_root, "images")):
    for f in files:
        if f.endswith('.webp') or f.endswith('.jpg') or f.endswith('.png'):
            rel_path = '/' + os.path.relpath(os.path.join(root, f), repo_root).replace('\\', '/')
            if f not in all_images:
                all_images[f] = []
            all_images[f].append(rel_path)

# 2. Parse all code files
code_extensions = {'.html', '.css', '.js'}
patterns = [
    r'src\s*=\s*["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']',
    r'url\(\s*["\']?([^"\')]+\.(?:webp|jpg|jpeg|png|gif|svg))["\']?\s*\)',
    r'content\s*=\s*["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']',
    r'data-src\s*=\s*["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif|svg))["\']',
]

references = {}

def normalize_path(path):
    path = re.sub(r'^https?://[^/]+', '', path)
    path = path.split('?')[0].split('#')[0]
    return path

for root, dirs, files in os.walk(repo_root):
    if 'node_modules' in root or '.git' in root or 'scratch' in root or '_ai' in root:
        continue
    for file in files:
        if any(file.endswith(ext) for ext in code_extensions):
            file_path = os.path.join(root, file)
            rel_file = '/' + os.path.relpath(file_path, repo_root).replace('\\', '/')
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for pattern in patterns:
                        for match in re.finditer(pattern, content, re.IGNORECASE):
                            raw_ref = match.group(1)
                            norm_ref = normalize_path(raw_ref)
                            filename = os.path.basename(norm_ref)
                            if filename not in references:
                                references[filename] = []
                            references[filename].append({
                                'file': rel_file,
                                'raw_ref': raw_ref,
                                'norm_ref': norm_ref
                            })
            except Exception:
                pass

report = []
report.append("# Image Audit Report\n")

report.append("## STEP 1: All images in /images/solutions/hero-solutions/")
hero_files = os.listdir(hero_dir) if os.path.exists(hero_dir) else []
report.append("| Image Filename | Stored At | Referenced As | In File | Status |")
report.append("|---|---|---|---|---|")
for f in hero_files:
    if not f.endswith('.webp'): continue
    stored_at = f"/images/solutions/hero-solutions/{f}"
    refs = references.get(f, [])
    if not refs:
        report.append(f"| {f} | {stored_at} | (Not referenced) | - | - |")
    for r in refs:
        if r['norm_ref'].startswith('/images/'):
            resolved_path = r['norm_ref']
        else:
            parts = r['norm_ref'].split('/')
            if 'images' in parts:
                resolved_path = '/' + '/'.join(parts[parts.index('images'):])
            else:
                resolved_path = r['norm_ref']
        
        full_resolved = os.path.join(repo_root, resolved_path.lstrip('/').replace('/', os.sep))
        status = "CORRECT" if os.path.exists(full_resolved) and resolved_path == stored_at else "WRONG PATH" if not os.path.exists(full_resolved) else "EXISTS BUT DIFFERENT LOCATION"
        report.append(f"| {f} | {stored_at} | {r['raw_ref']} | {r['file']} | {status} |")

report.append("\n## STEP 2: Mobile Hero Images")
report.append("| Image Filename | Stored At | Referenced As | In File | Status |")
report.append("|---|---|---|---|---|")
for f in mobile_images:
    stored_locations = all_images.get(f, ["(Not on disk)"])
    stored_str = "<br>".join(stored_locations)
    refs = references.get(f, [])
    if not refs:
        report.append(f"| {f} | {stored_str} | (Not referenced) | - | - |")
    for r in refs:
        resolved_path = r['norm_ref']
        if not resolved_path.startswith('/images/'):
            parts = resolved_path.split('/')
            if 'images' in parts:
                resolved_path = '/' + '/'.join(parts[parts.index('images'):])
        
        full_resolved = os.path.join(repo_root, resolved_path.lstrip('/').replace('/', os.sep))
        status = "CORRECT" if os.path.exists(full_resolved) else "WRONG PATH (Not Found)"
        report.append(f"| {f} | {stored_str} | {r['raw_ref']} | {r['file']} | {status} |")

report.append("\n## STEP 3: Desktop Hero Images")
report.append("| Image Filename | Stored At | Referenced As | In File | Status |")
report.append("|---|---|---|---|---|")
for f in desktop_images:
    stored_locations = all_images.get(f, ["(Not on disk)"])
    stored_str = "<br>".join(stored_locations)
    refs = references.get(f, [])
    if not refs:
        report.append(f"| {f} | {stored_str} | (Not referenced) | - | - |")
    for r in refs:
        resolved_path = r['norm_ref']
        if not resolved_path.startswith('/images/'):
            parts = resolved_path.split('/')
            if 'images' in parts:
                resolved_path = '/' + '/'.join(parts[parts.index('images'):])
        
        full_resolved = os.path.join(repo_root, resolved_path.lstrip('/').replace('/', os.sep))
        status = "CORRECT" if os.path.exists(full_resolved) else "WRONG PATH (Not Found)"
        report.append(f"| {f} | {stored_str} | {r['raw_ref']} | {r['file']} | {status} |")

report.append("\n## STEP 4: -rel Variants")
report.append("| Image Filename | Stored At | Referenced As | In File | Status |")
report.append("|---|---|---|---|---|")
all_rel_variants = set()
for m in mobile_images:
    base = m.replace("-hero-mobile.webp", "")
    for filename in all_images:
        if base in filename and "rel" in filename:
            all_rel_variants.add(filename)
    for filename in references:
        if base in filename and "rel" in filename:
            all_rel_variants.add(filename)

for f in sorted(list(all_rel_variants)):
    stored_locations = all_images.get(f, ["(Not on disk)"])
    stored_str = "<br>".join(stored_locations)
    refs = references.get(f, [])
    if not refs:
        report.append(f"| {f} | {stored_str} | (Not referenced) | - | - |")
    for r in refs:
        resolved_path = r['norm_ref']
        if not resolved_path.startswith('/images/'):
            parts = resolved_path.split('/')
            if 'images' in parts:
                resolved_path = '/' + '/'.join(parts[parts.index('images'):])
        
        full_resolved = os.path.join(repo_root, resolved_path.lstrip('/').replace('/', os.sep))
        status = "CORRECT" if os.path.exists(full_resolved) else "WRONG PATH (Not Found)"
        report.append(f"| {f} | {stored_str} | {r['raw_ref']} | {r['file']} | {status} |")

with open(os.path.join(repo_root, 'scratch', 'hero_audit_report.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(report))

print("Report saved to scratch/hero_audit_report.md")
