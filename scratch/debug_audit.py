import os, re, urllib.parse
repo_root = r"c:\Projects\SV-Build"
filepath = r"c:\Projects\SV-Build\insights\10-tips-securing-your-premises.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

re_img_src = re.compile(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]')
for m in re_img_src.finditer(content):
    path = m.group(1)
    if path.startswith('/'):
        abs_disk_path = os.path.join(repo_root, path.lstrip('/'))
        abs_disk_path = abs_disk_path.split('?')[0].split('#')[0]
        abs_disk_path = urllib.parse.unquote(abs_disk_path)
        abs_disk_path = os.path.normpath(abs_disk_path)
        print(f"{path} -> {abs_disk_path} exists? {os.path.exists(abs_disk_path)}")
