import os
import glob
import re

target_dir = r"c:\Projects\SV-Build\insights"
html_files = glob.glob(os.path.join(target_dir, "*.html"))

excluded = ['index.html', 'index-od1.html', 'index-od2.html']

ok_files = []
placeholder_files = []
empty_files = []
missing_files = []

def is_placeholder(text):
    text = text.strip()
    lower_text = text.lower()
    placeholders = [
        '[article title]',
        '[title]',
        'article title',
        '[insert title]',
        'title goes here'
    ]
    if lower_text in placeholders:
        return True
    
    # check for any text inside square brackets (entire text or partial?)
    # "content matches any of these patterns: ... or any text inside square brackets"
    # Wait, the prompt says "content matches any of these patterns ... or any text inside square brackets"
    # Usually this means if it's strictly `[something]` or contains `[something]`? Let's check if it starts with [ and ends with ]
    if text.startswith('[') and text.endswith(']'):
        return True
    # or if it contains square brackets
    if re.search(r'\[.*?\]', text):
        return True
        
    return False

for filepath in html_files:
    filename = os.path.basename(filepath)
    if filename in excluded:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    m = re.search(r'<h1[^>]*class="insights-header-title"[^>]*>(.*?)</h1>', content, re.DOTALL)
    
    if not m:
        missing_files.append((filename, "missing"))
    else:
        title = m.group(1).strip()
        if not title:
            empty_files.append((filename, "empty"))
        elif is_placeholder(title):
            placeholder_files.append((filename, title))
        else:
            ok_files.append((filename, title))

# SORT THEM (optional but good for consistent output)
placeholder_files.sort()
empty_files.sort()
missing_files.sort()
ok_files.sort()

# Output format
print("--- ISSUES ---")
for f, v in missing_files:
    print(f"MISSING: {f} -> {v}")
for f, v in empty_files:
    print(f"EMPTY: {f} -> {v}")
for f, v in placeholder_files:
    print(f"PLACEHOLDER: {f} -> '{v}'")
    
if not (missing_files or empty_files or placeholder_files):
    print("None")

print("\n--- OK FILES ---")
for f, v in ok_files:
    trunc_v = v if len(v) <= 80 else v[:77] + "..."
    print(f"OK: {f} -> {trunc_v}")

print("\n--- SUMMARY ---")
print(f"OK:           {len(ok_files)} files")
print(f"PLACEHOLDER:  {len(placeholder_files)} files")
print(f"EMPTY:        {len(empty_files)} files")
print(f"MISSING:      {len(missing_files)} files")
print(f"TOTAL:        {len(ok_files) + len(placeholder_files) + len(empty_files) + len(missing_files)} files")
