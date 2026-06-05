import os
import re

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
target_domain = "https://www.securevision.com.sg/images/"

files_with_abs = {}

for root, dirs, files in os.walk(repo_root):
    if 'node_modules' in root or '.git' in root or 'scratch' in root or '_ai' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            rel_file = '/' + os.path.relpath(file_path, repo_root).replace('\\', '/')
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                    abs_refs = re.findall(r'(https://www\.securevision\.com\.sg/images/[^"\'\s\)]+)', content)
                    
                    if abs_refs:
                        abs_refs = list(set(abs_refs))
                        files_with_abs[rel_file] = []
                        
                        for abs_url in abs_refs:
                            img_path = abs_url.replace("https://www.securevision.com.sg", "")
                            img_filename = os.path.basename(img_path)
                            
                            content_without_abs = content.replace(abs_url, "")
                            if img_filename in content_without_abs:
                                status = "DUPLICATE"
                            else:
                                status = "SOLE"
                                
                            files_with_abs[rel_file].append({
                                'url': abs_url,
                                'status': status
                            })
            except Exception as e:
                pass

print(f"Total files containing absolute URL image references: {len(files_with_abs)}\n")

sorted_files = sorted(files_with_abs.keys())
for f in sorted_files:
    print(f"**{f}**")
    for r in sorted(files_with_abs[f], key=lambda x: x['url']):
        print(f"- {r['url']} : **{r['status']}**")
    print()
