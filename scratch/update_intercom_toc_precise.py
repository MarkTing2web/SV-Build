import sys
sys.stdout.reconfigure(encoding='utf-8')

import re

filepath = r"C:\Projects\SV-Build\insights\choose-intercom-for-home.html"

with open(filepath, encoding='utf-8') as f:
    content = f.read()

replacements = [
    ("1. Starting With the Wrong Question", "1. Most People Start With the Wrong Question"),
    ("3. How Many Entrances?", "3. How Many Entrances Do You Actually Have?"),
    ("4. See or Just Hear?", "4. Do You Want to See or Just Hear?"),
    ("5. What When Nobody Is Home?", "5. What Happens When Nobody Is Home?"),
    ("6. How Do You Open the Gate?", "6. How Do You Want to Open the Gate?"),
    ("7. Renovating or Retrofitting?", "7. Are You Renovating or Retrofitting?"),
]

for old, new in replacements:
    content = content.replace(old, new)

with open(filepath, encoding='utf-8', mode='w') as f:
    f.write(content)

print("Done — verify TOC:")
toc = re.search(r'class=["\']toc-list["\'][^>]*>(.*?)</ul>', content, re.DOTALL)
if toc:
    for item in re.findall(r'<a[^>]*>([^<]+)</a>', toc.group(1)):
        print(f"  {item.strip()}")
