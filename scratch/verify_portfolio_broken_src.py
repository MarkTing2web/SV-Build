import os
import re

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
portfolio_dir = os.path.join(repo_root, "portfolio")
images_dir = os.path.join(repo_root, "images")

code_files = []
for root, _, files in os.walk(portfolio_dir):
    for f in files:
        if f.endswith('.html'):
            code_files.append(os.path.join(root, f))

html_comment_re = re.compile(r'<!--.*?-->', re.DOTALL)
img_src_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
img_exts = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg')

all_images = set()
broken_images = []

for cf in code_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    content = html_comment_re.sub('', content)
    
    srcs = img_src_re.findall(content)
    
    rel_cf = '/' + os.path.relpath(cf, repo_root).replace('\\', '/')
    
    for src in srcs:
        if not src.lower().endswith(img_exts):
            continue
        if src.startswith('http') or src.startswith('data:'):
            continue
            
        all_images.add(src)
        full_path = os.path.join(repo_root, src.lstrip('/'))
        
        if not os.path.exists(full_path):
            broken_images.append({'file': rel_cf, 'src': src})

all_repo_images = {}
for root, _, files in os.walk(images_dir):
    for file in files:
        if file.lower().endswith(img_exts):
            all_repo_images[file] = '/' + os.path.relpath(os.path.join(root, file), repo_root).replace('\\', '/')

total_checked = len(all_images)
total_broken = len(set(b['src'] for b in broken_images))
total_found = total_checked - total_broken

print("### Section A: Summary")
print(f"- Total unique image src paths checked: {total_checked}")
print(f"- Total FOUND: {total_found}")
print(f"- Total BROKEN: {total_broken}")
print()
print("### Section B: BROKEN references only")
print("| HTML File | Image src Path | File Exists Elsewhere? |")
print("|---|---|---|")

for b in sorted(broken_images, key=lambda x: x['file']):
    basename = os.path.basename(b['src'])
    elsewhere = f"YES (`{all_repo_images[basename]}`)" if basename in all_repo_images else "NO"
    print(f"| `{b['file']}` | `{b['src']}` | {elsewhere} |")

print()
print("### Section C: Confirmation")
if total_broken == 0:
    print("All image src references confirmed present on disk.")
else:
    print("All other image src references confirmed present on disk.")
