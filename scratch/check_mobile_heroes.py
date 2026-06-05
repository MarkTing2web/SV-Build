import os
import re
from collections import defaultdict

portfolio_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio"

mobile_patterns = [
    re.compile(r'url\([\'"]?([^\'"]+-mobile\.webp)[\'"]?\)', re.IGNORECASE),
    re.compile(r'<source\s+media="[^"]*max-width:\s*768px[^"]*"\s+srcset="([^"]+)"', re.IGNORECASE),
    re.compile(r'(?:src|srcset)=["\']([^"\']+-mobile\.webp)["\']', re.IGNORECASE)
]

results = defaultdict(list)

for root, dirs, files in os.walk(portfolio_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            rel_folder = os.path.relpath(root, portfolio_dir).replace('\\', '/')
            if rel_folder == '.': rel_folder = 'root'
            
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
                
            found_mobile = None
            for pattern in mobile_patterns:
                match = pattern.search(content)
                if match:
                    found_mobile = match.group(1).split('/')[-1]
                    break
                    
            if found_mobile:
                status = "MOBILE HERO PRESENT"
                filename = found_mobile
            else:
                status = "MOBILE HERO MISSING"
                filename = "N/A"
                
            results[rel_folder].append({'file': f, 'status': status, 'filename': filename})

for folder in sorted(results.keys()):
    if folder == 'root': continue
    print(f"\n### /portfolio/{folder}/")
    for item in sorted(results[folder], key=lambda x: x['file']):
        if item['status'] == 'MOBILE HERO PRESENT':
            print(f"- {item['file']}: **{item['status']}** (`{item['filename']}`)")
        else:
            print(f"- {item['file']}: **{item['status']}**")
