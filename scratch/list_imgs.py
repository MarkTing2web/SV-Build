import os, re
root = r'c:\Projects\SV-Build\portfolio\condominiums'
imgs = set()
for f in os.listdir(root):
    if f.endswith('.html'):
        text = open(os.path.join(root, f), encoding='utf-8').read()
        for src in re.findall(r'<img[^>]*src=[\'"]([^\'"]+)[\'"]', text):
            imgs.add(src)
for i in sorted(imgs):
    print(i)
