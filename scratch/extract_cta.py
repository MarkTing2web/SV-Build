import os
import re

files = [
    "portfolio/commercial/catholic-centre-security-partnership.html",
    "portfolio/condominiums/the-bale-intercom-cctv.html",
    "portfolio/industrial/cogent-logistics-hub-cctv.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

with open(os.path.join(base_dir, "scratch/output.txt"), "w", encoding="utf-8") as out:
    for fpath in files:
        full_path = os.path.join(base_dir, fpath)
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            match = re.search(r'<section class="cta-section[^>]*>.*?</section>', content, re.DOTALL)
            out.write(f"### {fpath}\n")
            if match:
                out.write(match.group(0) + "\n")
            else:
                out.write("NOT FOUND\n")
            out.write("\n" + "-"*40 + "\n\n")
