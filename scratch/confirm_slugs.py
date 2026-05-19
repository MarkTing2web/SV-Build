import os
import glob
import re

target_dir = r"c:\Projects\SV-Build\insights"
html_files = glob.glob(os.path.join(target_dir, "*.html"))

excluded = ['index.html', 'index-od1.html', 'index-od2.html']

for filepath in html_files:
    filename = os.path.basename(filepath)
    if filename in excluded:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    m = re.search(r'<body[^>]*data-article=[\'\"]([^\'\"]+)[\'\"]', content)
    if m:
        print(f"Confirmed: {filename} -> slug: {m.group(1)}")
    else:
        print(f"Not found in: {filename}")
