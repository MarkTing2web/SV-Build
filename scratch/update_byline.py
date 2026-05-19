import os
import glob
import re

target_dir = r"c:\Projects\SV-Build\insights"
html_files = glob.glob(os.path.join(target_dir, "*.html"))

excluded = [
    'index.html', 
    'index-od1.html', 
    'index-od2.html',
    'how-technology-makes-your-guarding-team-more-competitive.html'
]

files_updated = []
files_not_found = []

for filepath in html_files:
    filename = os.path.basename(filepath)
    if filename in excluded:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    # We want to replace <span>Founder &amp; CEO ... </span> with <p class="hero-byline-role">Founder &amp; CEO ... </p>
    # The regex looks for exactly <span> followed by "Founder &amp; CEO" up to the next </span>
    
    new_content, count = re.subn(
        r'<span>\s*(Founder\s*&amp;\s*CEO.*?)\s*</span>', 
        r'<p class="hero-byline-role">\1</p>', 
        content,
        flags=re.DOTALL
    )
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        files_updated.append(filename)
    else:
        files_not_found.append(filename)

print("--- RESULTS ---")
for f in files_updated:
    print(f"UPDATED: {f}")
for f in files_not_found:
    print(f"NOT FOUND: {f}")
