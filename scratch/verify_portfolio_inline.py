import os
import re

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
portfolio_dir = os.path.join(repo_root, "portfolio")

files_to_check = [
    "/images/portfolio/condominiums/country-grandeur-wide.webp",
    "/images/portfolio/condominiums/d-elias-front-facade.webp",
    "/images/portfolio/condominiums/d-elias-vcp.webp",
    "/images/portfolio/condominiums/hillview-park-condo.webp",
    "/images/portfolio/condominiums/idyllic-condo-main.webp",
    "/images/portfolio/condominiums/idyllic-suites-front-facade.webp",
    "/images/portfolio/condominiums/idyllic-suites-front.webp",
    "/images/portfolio/condominiums/light-condo-intercom.webp",
    "/images/portfolio/condominiums/light-lobby-akuvox-x915.webp",
    "/images/portfolio/condominiums/lviv-akuvox-vcp-upgrade.webp",
    "/images/portfolio/condominiums/lviv-angled-bracket-for-fingerprint.webp",
    "/images/portfolio/condominiums/lviv-condo-gate-hero.webp",
    "/images/portfolio/condominiums/lviv-condo-main.webp",
    "/images/portfolio/condominiums/lviv-front-entrance-gate-hero.webp",
    "/images/portfolio/condominiums/lviv-pool-side.webp",
    "/images/portfolio/condominiums/lviv-resident-face-palm-reader-installed.webp",
    "/images/portfolio/condominiums/mergui-condo-main.webp",
    "/images/portfolio/condominiums/mergui-mansion-building.webp",
    "/images/portfolio/condominiums/mergui-mansions-backgate-r28a.webp",
    "/images/portfolio/condominiums/mergui-mansions-facade.webp",
    "/images/portfolio/condominiums/newton-21-condo-facade.webp",
    "/images/portfolio/condominiums/newton-21-condo-main.webp",
    "/images/portfolio/condominiums/newton-21-condo-sign.webp",
    "/images/portfolio/condominiums/newton21-akuvox-intercom.webp",
    "/images/portfolio/condominiums/newton21-akuvox-r20a.webp",
    "/images/portfolio/condominiums/newton21-card.webp",
    "/images/portfolio/condominiums/newton21-front-facade.webp",
    "/images/portfolio/condominiums/newton21-lobby.webp",
    "/images/portfolio/condominiums/newton21-sign.webp",
    "/images/portfolio/condominiums/rezi32.webp",
    "/images/portfolio/condominiums/the-verte-condo-facade.webp",
    "/images/portfolio/condominiums/the-verte-condo-main.webp",
    "/images/portfolio/condominiums/the-verte-front-view.webp",
    "/images/portfolio/condominiums/the-village-at-pasir-panjang-card.webp",
    "/images/portfolio/condominiums/village-at-pasir-panjang-front-entrance.webp",
    "/images/portfolio/condominiums/village-at-pasir-panjang-front-facade.webp",
    "/images/portfolio/condominiums/village-at-pasir-panjang-lobby-r28a.webp",
    "/images/portfolio/condominiums/village-at-pasir-panjang-main.webp",
    "/images/portfolio/condominiums/village-at-pasir-panjang-poolside.webp",
    "/images/portfolio/condominiums/village-condo-facade.webp",
    "/images/portfolio/condominiums/village-condo-main.webp",
    "/images/portfolio/condominiums/village-lpr-camera.webp",
    "/images/portfolio/residential/22-dunbar-walk-residential.webp",
    "/images/portfolio/residential/22-dunbar-walk-wide.webp",
    "/images/portfolio/residential/26-lengkok-mariam.webp",
    "/images/portfolio/residential/29-siglap-bank-house.webp",
    "/images/portfolio/residential/29-siglap-bank.webp",
    "/images/portfolio/residential/merryn-road-house.webp",
    "/images/portfolio/residential/merryn-road-residential-wide.webp",
    "/images/portfolio/residential/upper-east-coast-card.webp",
    "/images/portfolio/residential/upper-east-coast-landed-upgrade-rel.webp",
    "/images/portfolio/institutions/catholic-centre-waterloo-rel.webp"
]

code_files = []
for root, _, files in os.walk(portfolio_dir):
    for f in files:
        if f.endswith('.html'):
            code_files.append(os.path.join(root, f))

html_comment_re = re.compile(r'<!--.*?-->', re.DOTALL)

print("| Filename | Status | Referenced In (if any) |")
print("|---|---|---|")

for img_path in files_to_check:
    basename = os.path.basename(img_path)
    
    referenced_list = []
    
    for cf in code_files:
        with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        if basename in content:
            active_content = html_comment_re.sub('', content)
            
            if basename in active_content:
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if basename in line:
                        if '<!--' in line and '-->' in line:
                            continue
                        rel_cf = os.path.relpath(cf, repo_root).replace('\\', '/')
                        referenced_list.append(f"`{rel_cf}:{i+1}`")
                            
    if referenced_list:
        referenced_list = list(dict.fromkeys(referenced_list))
        print(f"| `{img_path}` | REFERENCED | {', '.join(referenced_list)} |")
    else:
        print(f"| `{img_path}` | NOT REFERENCED | N/A |")
