import os, re

root = r'c:\Projects\SV-Build\portfolio\condominiums'
files = [f for f in os.listdir(root) if f.endswith('.html')]

images = set()
for f in files:
    with open(os.path.join(root, f), 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.findall(r'<img[^>]*src=[\'"]([^\'"]+)[\'"]', content)
        for m in matches:
            images.add(m)

print("Found image references:")
for img in sorted(list(images)):
    if 'rel.webp' not in img and 'thumb' not in img and 'hero' not in img:
        print(img)
