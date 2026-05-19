import os
import glob
import re

count = 0
for filepath in glob.glob('c:/Projects/SV-Build/insights/*.html'):
    if os.path.basename(filepath) in ['index.html', 'index-od1.html', 'index-od2.html']:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.finditer(r'<[a-zA-Z]+[^>]*class=[\'"]prev-next-nav[\'"][^>]*>.*?</[a-zA-Z]+>', content, re.DOTALL)
    for m in matches:
        print(f'Found block in {os.path.basename(filepath)}: {m.group(0)[:50]}')
        count += 1
        
    # Also just find the opening tag to see if there are unclosed blocks
    open_matches = re.finditer(r'<[a-zA-Z]+[^>]*class=[\'"]prev-next-nav[\'"][^>]*>', content)
    for m in open_matches:
        # print(f'Found opening tag in {os.path.basename(filepath)}: {m.group(0)}')
        pass

if count == 0:
    print('No full blocks found.')
