import os
import re
from collections import defaultdict

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
folders_to_check = [
    "images/temp1",
    "images/temp-port-image",
    "images/temp insights images that did some work"
]

code_extensions = {'.html', '.css', '.js'}
comment_pattern = re.compile(r'<!--.*?-->', re.DOTALL)
js_comment_pattern = re.compile(r'/\*.*?\*/', re.DOTALL)
js_line_comment = re.compile(r'//.*$', re.MULTILINE)
css_comment = re.compile(r'/\*.*?\*/', re.DOTALL)

folder_files = defaultdict(list)
for rel_folder in folders_to_check:
    full_folder = os.path.join(repo_root, rel_folder.replace('/', os.sep))
    if os.path.exists(full_folder):
        for f in os.listdir(full_folder):
            if os.path.isfile(os.path.join(full_folder, f)):
                folder_files[rel_folder].append(f)

all_filenames = set()
for files in folder_files.values():
    for f in files:
        all_filenames.add(f)

references = []

for root, dirs, files in os.walk(repo_root):
    if any(x in root for x in ['node_modules', '.git', 'scratch', '_ai']):
        continue
        
    for f in files:
        if any(f.endswith(ext) for ext in code_extensions):
            file_path = os.path.join(root, f)
            rel_file = '/' + os.path.relpath(file_path, repo_root).replace('\\', '/')
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
                
                if f.endswith('.html'):
                    content = comment_pattern.sub('', content)
                elif f.endswith('.js'):
                    content = js_comment_pattern.sub('', content)
                    content = js_line_comment.sub('', content)
                elif f.endswith('.css'):
                    content = css_comment.sub('', content)
                
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    for filename in all_filenames:
                        if filename in line:
                            references.append({
                                'filename': filename,
                                'file': rel_file,
                                'line': i + 1
                            })

print("--- VERIFICATION REPORT ---")
for rel_folder in folders_to_check:
    files_in_folder = folder_files[rel_folder]
    total_files = len(files_in_folder)
    print(f"\nFolder: /{rel_folder}/")
    print(f"Total files in folder: {total_files}")
    
    if total_files == 0:
        print("Final verdict: SAFE TO DELETE (Folder is empty or missing)")
        continue
        
    active_refs = [r for r in references if r['filename'] in files_in_folder]
    active_filenames = set(r['filename'] for r in active_refs)
    zero_ref_count = total_files - len(active_filenames)
    
    print(f"Total files with ZERO references: {zero_ref_count}")
    print(f"Total files with at least ONE active reference: {len(active_filenames)}")
    
    if active_filenames:
        print("Active references found:")
        print(f"| {'Filename'.ljust(40)} | {'Referenced In'.ljust(60)} | Line Number |")
        print("-" * 120)
        for r in active_refs:
            print(f"| {r['filename'].ljust(40)} | {r['file'].ljust(60)} | {r['line']} |")
        print("Final verdict: NOT SAFE")
    else:
        print("Final verdict: SAFE TO DELETE")
