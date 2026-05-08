import os
import re

pages = [
    "solutions/residential.html",
    "solutions/condominiums.html",
    "solutions/commercial.html",
    "solutions/healthcare.html",
    "solutions/industrial.html",
    "solutions/institutions.html",
    "solutions/managed-living.html",
    "solutions/data-centres.html",
    "solutions/index.html"
]

root_dir = "d:/Ler Wee Meng/Project-Web/SV-Build"

def check_file(path):
    if path.startswith("/"):
        full_path = os.path.join(root_dir, path.lstrip("/"))
    else:
        return True
    
    return os.path.exists(full_path)

broken_links = {}

for page in pages:
    page_path = os.path.join(root_dir, page)
    if not os.path.exists(page_path):
        continue
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = re.findall(r'src=["\'](.*?)["\']', content)
    links += re.findall(r'url\(["\']?(.*?)["\']?\)', content)
    links += re.findall(r'srcset=["\'](.*?)["\']', content)
    
    img_links = [l for l in links if any(l.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp', '.svg', '.mp4'])]
    
    broken = []
    for link in img_links:
        sub_links = [s.strip().split(' ')[0] for s in link.split(',')]
        for sl in sub_links:
            if sl.startswith("http") or sl.startswith("https"):
                continue
            if not check_file(sl):
                broken.append(sl)
    
    if broken:
        broken_links[page] = list(set(broken))

if not broken_links:
    print("No broken links found!")
else:
    for page, links in broken_links.items():
        print(f"Broken links in {page}:")
        for link in links:
            print(f"  - {link}")
