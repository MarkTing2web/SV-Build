import os, re, urllib.parse
repo_root = r"c:\Projects\SV-Build"
path = r"c:\Projects\SV-Build\insights\10-tips-securing-your-premises.html"
with open(path, 'r', encoding='utf-8') as f: content = f.read()
re_img_src = re.compile(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]')
found_paths = set(m.group(1) for m in re_img_src.finditer(content))
for raw_path in found_paths:
    print('RAW_PATH:', raw_path)
