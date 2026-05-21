import os
import re
import urllib.parse

repo_root = r"c:\Projects\SV-Build"
filepath = os.path.join(repo_root, "resources", "guides", "cctv-guide.html")

re_img_src = re.compile(r'<img\s+[^>]*src\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
re_bg_url = re.compile(r'background-image\s*:\s*url\(\s*[\'"]?([^\'"\)]+)[\'"]?\s*\)', re.IGNORECASE)
re_og_image = re.compile(r'<meta\s+[^>]*(?:property|name)\s*=\s*["\']og:image["\']\s+[^>]*content\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
re_a_href = re.compile(r'<a\s+[^>]*href\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
re_canonical = re.compile(r'<link\s+[^>]*rel\s*=\s*["\']canonical["\']\s+[^>]*href\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print("--- IMAGES ---")
for m in re_img_src.finditer(content):
    url = m.group(1)
    # resolve path
    path = urllib.parse.urlparse(url).path
    abs_path = os.path.normpath(os.path.join(repo_root, path.lstrip('/')))
    exists = os.path.exists(abs_path)
    print(f"img src: {url} -> {abs_path} (exists: {exists})")

for m in re_bg_url.finditer(content):
    url = m.group(1)
    path = urllib.parse.urlparse(url).path
    abs_path = os.path.normpath(os.path.join(repo_root, path.lstrip('/')))
    exists = os.path.exists(abs_path)
    print(f"bg url: {url} -> {abs_path} (exists: {exists})")

for m in re_og_image.finditer(content):
    url = m.group(1)
    if 'securevision.com.sg' in url:
        path = urllib.parse.urlparse(url).path
    else:
        path = url
    abs_path = os.path.normpath(os.path.join(repo_root, path.lstrip('/')))
    exists = os.path.exists(abs_path)
    print(f"og:image: {url} -> {abs_path} (exists: {exists})")

print("\n--- LINKS ---")
for m in re_a_href.finditer(content):
    url = m.group(1)
    if url.startswith('/'):
        abs_path = os.path.normpath(os.path.join(repo_root, url.lstrip('/')))
        exists = os.path.exists(abs_path)
        print(f"a href: {url} -> {abs_path} (exists: {exists})")
for m in re_canonical.finditer(content):
    url = m.group(1)
    parsed = urllib.parse.urlparse(url)
    path = parsed.path
    abs_path = os.path.normpath(os.path.join(repo_root, path.lstrip('/')))
    exists = os.path.exists(abs_path)
    print(f"canonical: {url} -> {abs_path} (exists: {exists})")
