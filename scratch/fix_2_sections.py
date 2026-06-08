import os
import re

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

edits = [
    ("portfolio/condominiums/village-pasir-panjang-condo.html", 357, '<section class="portfolio-insight-section sv-section-grey section-spacing no-bottom-spacing">', '<section class="portfolio-insight-section sv-section-white section-spacing no-bottom-spacing">'),
    ("portfolio/condominiums/the-verte-telok-kurau-condo.html", 305, '<section class="portfolio-section sv-section-grey section-spacing">', '<section class="portfolio-section sv-section-white section-spacing">')
]

for fpath, line_no, target, replacement in edits:
    full_path = os.path.join(base_dir, fpath)
    with open(full_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    if target in lines[line_no - 1]:
        lines[line_no - 1] = lines[line_no - 1].replace(target, replacement)
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

# Verification
files = [
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html"
]

with open("sections_output_final_2.txt", "w", encoding="utf-8") as out:
    for fpath in files:
        full_path = os.path.join(base_dir, fpath)
        out.write(f"FILE: {fpath}\n")
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        sections = []
        for match in re.finditer(r'<section([^>]*)>', content, re.IGNORECASE):
            attrs = match.group(1)
            class_match = re.search(r'class=["\']([^"\']*)["\']', attrs, re.IGNORECASE)
            if class_match:
                classes = class_match.group(1).split()
                bg_class = None
                if 'sv-section-grey' in classes:
                    bg_class = 'sv-section-grey'
                elif 'sv-section-white' in classes:
                    bg_class = 'sv-section-white'
                    
                if bg_class:
                    line_no = content[:match.start()].count('\n') + 1
                    sections.append((bg_class, line_no))
                    out.write(f"Line {line_no}: {bg_class}\n")
                    
        # check clashes
        clashes = 0
        for i in range(1, len(sections)):
            if sections[i][0] == sections[i-1][0]:
                out.write(f"CLASH: Line {sections[i-1][1]} and Line {sections[i][1]} both have {sections[i][0]}\n")
                clashes += 1
        
        if clashes == 0:
            out.write("No consecutive sections share the same class.\n")
        out.write("\n")
