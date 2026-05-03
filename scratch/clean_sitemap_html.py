import os
import re

file_path = r'c:\Projects\SV-Build\sitemap.html'
with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Fix the specific industrial entries that have long ugly anchor texts
replacements = {
    '<li><a href="/portfolio/industrial/sta-inspection-industrial.html">commercial-security-sta-building-singapore.html</a></li>': 
    '<li><a href="/portfolio/industrial/sta-inspection-industrial.html">STA Building (Industrial)</a></li>',
    '<li><a href="/portfolio/industrial/cyrus-tech-industrial.html">industrial-security-cyrus-tech-park-singapore.html</a></li>':
    '<li><a href="/portfolio/industrial/cyrus-tech-industrial.html">Cyrus Tech Park (Industrial)</a></li>'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Cleaned up sitemap.html anchor texts.")
