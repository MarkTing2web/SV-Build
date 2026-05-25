import os

file_path = r"c:\Projects\SV-Build\portfolio\condominiums\the-bale-intercom-cctv.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = 'href="/brands/akuvox.html"'
replacement = 'href="/brands/akuvox-intercom.html"'

count = content.count(target)
if count > 0:
    new_content = content.replace(target, replacement)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Replaced {count} instances.")
