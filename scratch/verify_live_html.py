import os
import re
from collections import defaultdict

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
images_dir = os.path.join(repo_root, "images")
ai_dir = os.path.join(repo_root, "_ai")
os.makedirs(ai_dir, exist_ok=True)

filename_to_paths = defaultdict(list)
image_extensions = {'.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg'}

for root, dirs, files in os.walk(images_dir):
    for f in files:
        if os.path.splitext(f)[1].lower() in image_extensions:
            full_path = os.path.join(root, f)
            rel_path = '/' + os.path.relpath(full_path, repo_root).replace('\\', '/')
            filename_to_paths[f].append(rel_path)

comment_pattern = re.compile(r'<!--.*?-->', re.DOTALL)
img_src_pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
style_url_pattern = re.compile(r'style=["\'][^"\']*url\([\'"]?([^\'"\)]+)[\'"]?\)[^"\']*["\']', re.IGNORECASE)

references = []
unique_refs = set()

for root, dirs, files in os.walk(repo_root):
    if any(x in root for x in ['node_modules', '.git', 'scratch', '_ai', 'templates']):
        continue
        
    for f in files:
        if f.endswith('.html'):
            file_path = os.path.join(root, f)
            rel_file = '/' + os.path.relpath(file_path, repo_root).replace('\\', '/')
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
                content = comment_pattern.sub('', content)
                
                for match in img_src_pattern.finditer(content):
                    path = match.group(1)
                    references.append({'file': rel_file, 'path': path})
                    
                for match in style_url_pattern.finditer(content):
                    path = match.group(1)
                    references.append({'file': rel_file, 'path': path})

broken = []
found_count = 0
broken_count = 0

for ref in references:
    path = ref['path']
    src_file = ref['file']
    
    norm = re.sub(r'^https?://www\.securevision\.com\.sg', '', path).split('?')[0].split('#')[0]
    unique_refs.add(norm)
    
    if norm.startswith('/images/'):
        expected_path = norm
    else:
        if 'images' in norm.split('/'):
            parts = norm.split('/')
            expected_path = '/' + '/'.join(parts[parts.index('images'):])
        else:
            expected_path = norm
            
    disk_path = os.path.join(repo_root, expected_path.lstrip('/\\').replace('/', os.sep))
    if os.path.exists(disk_path) and os.path.isfile(disk_path):
        found_count += 1
    else:
        broken_count += 1
        filename = os.path.basename(expected_path)
        elsewhere = filename_to_paths.get(filename, [])
        elsewhere_str = ", ".join(elsewhere) if elsewhere else "NO"
        broken.append({'file': src_file, 'expected': expected_path, 'elsewhere': elsewhere_str})

lines = []
lines.append("# Live HTML Broken Image src Report")
lines.append("\n## Section A: Summary")
lines.append(f"- **Total unique image src paths checked**: {len(unique_refs)}")
lines.append(f"- **Total FOUND (file exists)**: {found_count}")
lines.append(f"- **Total BROKEN**: {broken_count}")

lines.append("\n## Section B: BROKEN image src references only")
if broken:
    lines.append("| HTML File | Image src Path | File Exists Elsewhere? |")
    lines.append("|---|---|---|")
    
    def get_section(f):
        parts = [p for p in f.split('/') if p]
        if not parts: return "Root"
        if parts[0] in ['insights', 'portfolio', 'solutions', 'systems', 'resources']:
            return f"/{parts[0]}/"
        if parts[0] == 'about.html':
            return "/about.html"
        return "Other Root Pages"
        
    grouped = defaultdict(list)
    for b in broken:
        sec = get_section(b['file'])
        grouped[sec].append(b)
        
    for sec in sorted(grouped.keys()):
        lines.append(f"### {sec}")
        for b in sorted(grouped[sec], key=lambda x: x['file']):
            lines.append(f"| {b['file']} | {b['expected']} | {b['elsewhere']} |")
else:
    lines.append("No broken references found!")

lines.append("\n## Section C: Confirmation")
lines.append("All other image src references are confirmed present on disk.")

report_path = os.path.join(ai_dir, "broken-image-src-report.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Report successfully saved to {report_path}")
