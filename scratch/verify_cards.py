import os
import re

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"

files_to_check = [
    "/images/portfolio/commercial/altitudex-sentosa-card.webp",
    "/images/portfolio/commercial/catholic-centre-card.webp",
    "/images/portfolio/commercial/em-engineering-at-jalan-kilang-card.webp",
    "/images/portfolio/commercial/hilton-singapore-orchard-card.webp",
    "/images/portfolio/commercial/st-engineering-mobility-card.webp",
    "/images/portfolio/condominiums/high-oak-condominium-card.webp",
    "/images/portfolio/condominiums/hillview-park-condo-card.webp",
    "/images/portfolio/condominiums/rezi32-card.webp",
    "/images/portfolio/condominiums/suites-cairnhill-card.webp",
    "/images/portfolio/condominiums/the-clearwater-card.webp",
    "/images/portfolio/data-centres/fort-data-centre-card.webp",
    "/images/portfolio/industrial/cogent-1-logistics-hub-card.webp",
    "/images/portfolio/industrial/cyrus-tech-at-loyang-card.webp",
    "/images/portfolio/industrial/mitsubishi-elevator-singapore-card.webp",
    "/images/portfolio/industrial/multibase-construction-card.webp",
    "/images/portfolio/industrial/smartflex-at-tampines-card.webp",
    "/images/portfolio/industrial/st-microelectronics-loyang-card.webp",
    "/images/portfolio/industrial/sta-inspection-centre-sin-ming-card.webp",
    "/images/portfolio/institutions/changi-airside-card.webp",
    "/images/portfolio/institutions/cpf-maxwell-card.webp",
    "/images/portfolio/institutions/das-learning-centre-card.webp",
    "/images/portfolio/institutions/my-world-preschool-card.webp",
    "/images/portfolio/institutions/st-francis-xavier-retreat-centre-card.webp",
    "/images/portfolio/managed-living/nursing-hostel-at-jln-seh-chuan-card.webp",
    "/images/portfolio/residential/dyson-8-card.webp",
    "/images/portfolio/residential/shelford-card.webp",
    "/images/portfolio/residential/upper-east-coast-card.webp"
]

code_files = []
for root, _, files in os.walk(repo_root):
    if any(x in root for x in ['node_modules', '.git', 'scratch', '_ai']):
        continue
    for f in files:
        if f.endswith(('.html', '.css', '.js')):
            code_files.append(os.path.join(root, f))

print("| Filename | Check A (Referenced?) | Check B (Rel exists?) | Safe to Delete? |")
print("|---|---|---|---|")

html_comment_re = re.compile(r'<!--.*?-->', re.DOTALL)

for img_path in files_to_check:
    filename = os.path.basename(img_path)
    
    referenced = False
    ref_info = ""
    for cf in code_files:
        with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        if filename in content:
            if cf.endswith('.html'):
                active_content = html_comment_re.sub('', content)
            else:
                active_content = content
                
            if filename in active_content:
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if filename in line:
                        rel_cf = os.path.relpath(cf, repo_root).replace('\\', '/')
                        ref_info = f"{rel_cf}:{i+1}"
                        referenced = True
                        break
        if referenced:
            break
            
    check_a = f"REFERENCED (`{ref_info}`)" if referenced else "NOT REFERENCED"
    
    rel_path = img_path.replace('-card.webp', '-rel.webp')
    full_rel_path = os.path.join(repo_root, rel_path.lstrip('/'))
    rel_exists = os.path.exists(full_rel_path)
    check_b = "REL EXISTS" if rel_exists else "REL MISSING"
    
    safe = "YES" if (not referenced and rel_exists) else "NO"
    
    print(f"| `{filename}` | {check_a} | {check_b} | **{safe}** |")
