import os
import re

files = [
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

with open("sections_output_3.txt", "w", encoding="utf-8") as out:
    for fpath in files:
        full_path = os.path.join(base_dir, fpath)
        if not os.path.exists(full_path):
            continue
            
        out.write(f"FILE: {fpath}\n")
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            
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
                    out.write(f"Line {line_no}: {bg_class}\n")
        out.write("\n")
