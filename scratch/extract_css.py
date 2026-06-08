import os
import re

RESOURCES_DIR = r"C:\Projects\SV-Build\resources"
RESOURCES_CSS = r"C:\Projects\SV-Build\sv-resources.css"

files_with_css = [
    "calculators.html",
    "checklists.html",
    "faq.html",
    "guides.html",
    "index.html",
    "library.html",
    "training-videos.html"
]

all_css = ""

for fname in files_with_css:
    path = os.path.join(RESOURCES_DIR, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract <style> ... </style> block that is not :root
    # Actually, let's just find the first <style> block
    match = re.search(r'<style>(.*?)</style>', content, flags=re.DOTALL)
    if match:
        css = match.group(1).strip()
        all_css += f"\n/* ── Extracted from {fname} ── */\n{css}\n"
        
        # Remove it from html
        content = content.replace(match.group(0), "")
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

# Append to sv-resources.css
if all_css:
    with open(RESOURCES_CSS, 'a', encoding='utf-8') as f:
        f.write(all_css)

print("CSS extracted.")
