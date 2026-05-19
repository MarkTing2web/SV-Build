import os, urllib.parse
repo_root = r"c:\Projects\SV-Build"
raw_path = "/images/insights/10-tips-perimeter-audit.webp"
path = raw_path
abs_disk_path = os.path.join(repo_root, path.lstrip('/'))
abs_disk_path = abs_disk_path.split('?')[0].split('#')[0]
abs_disk_path = urllib.parse.unquote(abs_disk_path)
abs_disk_path = os.path.normpath(abs_disk_path)
print("abs_disk_path:", abs_disk_path)
print("exists:", os.path.exists(abs_disk_path))
