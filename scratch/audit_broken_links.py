import os
import re
import posixpath
from collections import defaultdict

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
sitemap_path = os.path.join(repo_root, "SITEMAP.md")
ai_dir = os.path.join(repo_root, "_ai")
os.makedirs(ai_dir, exist_ok=True)

all_html_files = []
filename_to_paths = defaultdict(list)
for root, dirs, files in os.walk(repo_root):
    if any(x in root for x in ['node_modules', '.git', 'scratch', '_ai']):
        continue
    for f in files:
        if f.endswith('.html'):
            full_path = os.path.join(root, f)
            rel_path = '/' + os.path.relpath(full_path, repo_root).replace('\\', '/')
            all_html_files.append(rel_path)
            filename_to_paths[f].append(rel_path)

sitemap_files = set()
with open(sitemap_path, 'r', encoding='utf-8') as f:
    for line in f:
        match = re.search(r'- \[(.*?)\]', line)
        if match:
            url_path = match.group(1)
            if url_path == '/':
                sitemap_files.add('/index.html')
            elif url_path.endswith('/'):
                sitemap_files.add(url_path + 'index.html')
            else:
                sitemap_files.add(url_path)

comment_pattern = re.compile(r'<!--.*?-->', re.DOTALL)
a_tag_pattern = re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\']', re.IGNORECASE)

references = []

for s_file in sitemap_files:
    file_path = os.path.join(repo_root, s_file.lstrip('/'))
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        content = comment_pattern.sub('', content)
        
        for match in a_tag_pattern.finditer(content):
            href = match.group(1)
            
            if href.startswith(('http://', 'https://', 'mailto:', 'tel:', 'wa.me', 'whatsapp')):
                continue
            if href.startswith('#'):
                continue
                
            references.append({'file': s_file, 'href': href})

broken = []
found_count = 0
broken_count = 0

for ref in references:
    href = ref['href']
    src_file = ref['file']
    
    clean_href = href.split('#')[0].split('?')[0]
    if not clean_href:
        continue
        
    if clean_href.startswith('/'):
        target_path = clean_href
    else:
        target_path = posixpath.normpath(posixpath.join(posixpath.dirname(src_file), clean_href))
        
    if clean_href.endswith('/') or not os.path.basename(target_path).count('.'):
        if not target_path.endswith('/'):
            target_path += '/'
        target_path += 'index.html'

    disk_path = os.path.join(repo_root, target_path.lstrip('/'))
    
    if os.path.exists(disk_path) and os.path.isfile(disk_path):
        found_count += 1
    else:
        broken_count += 1
        basename = os.path.basename(target_path)
        if not basename:
            basename = 'index.html'
        elsewhere = filename_to_paths.get(basename, [])
        elsewhere_str = ", ".join(elsewhere) if elsewhere else "NO"
        broken.append({'file': src_file, 'href': href, 'expected': target_path, 'elsewhere': elsewhere_str})

lines = []
lines.append("# Internal Broken Links Report")
lines.append("\n## Section A: Summary")
lines.append(f"- **Total internal links checked**: {len(references)}")
lines.append(f"- **Total VALID (file exists)**: {found_count}")
lines.append(f"- **Total BROKEN**: {broken_count}")

lines.append("\n## Section B: BROKEN links only")
if broken:
    lines.append("| Source Page | Broken href | File Exists Elsewhere? |")
    lines.append("|---|---|---|")
    
    def get_section(f):
        parts = [p for p in f.split('/') if p]
        if not parts: return "Root"
        if parts[0] in ['insights', 'portfolio', 'solutions', 'systems', 'resources', 'brands']:
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
            lines.append(f"| {b['file']} | {b['href']} | {b['elsewhere']} |")
else:
    lines.append("No broken links found!")

lines.append("\n## Section C: Confirmation")
lines.append("All other internal href links are confirmed valid.")

report_path = os.path.join(ai_dir, "broken-links-report-v2.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Report successfully saved to {report_path}")
