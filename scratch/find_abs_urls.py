import os, re
repo_root = r'd:\Ler Wee Meng\Project-Web\SV-Build'
abs_src = 0
abs_url = 0
for root, dirs, files in os.walk(repo_root):
    if 'node_modules' in root or '.git' in root or 'scratch' in root or '_ai' in root: continue
    for f in files:
        if f.endswith('.html') or f.endswith('.css'):
            with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                srcs = re.findall(r'src=[\"\']https://www\.securevision\.com\.sg/images/[^\"\']+[\"\']', content)
                urls = re.findall(r'url\([\"\']?https://www\.securevision\.com\.sg/images/[^\"\')]+[\"\']?\)', content)
                if srcs: abs_src += len(srcs)
                if urls: abs_url += len(urls)
                if srcs or urls:
                    print(f'Found in {f}: {srcs} {urls}')
print(f'Total abs src: {abs_src}, Total abs url: {abs_url}')
