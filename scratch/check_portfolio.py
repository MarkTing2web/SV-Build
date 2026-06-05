import os
import re

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
js_path = os.path.join(repo_root, "portfolio-block.js")

with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

images = sorted(set(re.findall(r'image:\s*"([^"]+)"', js)))

print("Total unique images found:", len(images))
for img in images:
    full_path = os.path.join(repo_root, img.lstrip('/'))
    status = "FOUND" if os.path.exists(full_path) else "MISSING"
    print(f"{img} | {status}")
