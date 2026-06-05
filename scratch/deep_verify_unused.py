import os
import re

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"

files_to_check = [
    "/images/cctv-guide-hero.webp",
    "/images/cta-singapore-skyline.png",
    "/images/cta-skyline-polo.webp",
    "/images/insights-hero-new.webp",
    "/images/intercom-guide-hero.webp",
    "/images/network-reader.png",
    "/images/platform-integration-hero.webp",
    "/images/prop-landed.webp",
    "/images/resources-knowledge-base-singapore-rel.webp",
    "/images/software-dash.png",
    "/images/standalone-reader.png",
    "/images/upgrade-compare.png",
    "/images/about/comp-integration-v3.png",
    "/images/about/people-access-hero.png",
    "/images/about/vehicle-access-hero.png",
    "/images/home/securevision-logo.svg",
    "/images/portfolio/commercial/catholic-centre.webp",
    "/images/portfolio/commercial/hilton-singapore-orchard.webp",
    "/images/portfolio/data-centres/fort-st-engineering-thumb.png",
    "/images/portfolio/healthcare/sunlove-card.webp",
    "/images/portfolio/industrial/gantrygo-at-work.webp",
    "/images/portfolio/industrial/hoy-san-main-gate.webp",
    "/images/portfolio/institutions/changi-airside.webp",
    "/images/solutions/root-solutions/solution-automate-vehicle-access-prop-industrial.webp",
    "/images/solutions/root-solutions/solution-commercial-hero.webp",
    "/images/solutions/root-solutions/solution-condominiums-project-condo-upgrade.webp",
    "/images/solutions/root-solutions/solution-condominiums-project-estate-integration.webp",
    "/images/solutions/root-solutions/solution-healthcare-healthcare-path-hostel.webp",
    "/images/solutions/root-solutions/solution-healthcare-healthcare-path-nursing.webp",
    "/images/solutions/root-solutions/solution-institutions-project-religious.webp",
    "/images/solutions/root-solutions/solution-institutions.webp",
    "/images/resources/resources-knowledge-base-singapore-mobile.webp",
    "/images/solutions/residential/landed-home-multiple-entry-points-singapore.webp",
    "/images/pillar_maintenance.webp",
    "/images/brands/vesta-security-logo.webp",
    "/images/about/founder-hero-ler-wee-meng-01.webp",
    "/images/wee-meng-akuvox-summit-2024.jpg"
]

code_files = []
for root, _, files in os.walk(repo_root):
    if 'node_modules' in root or '.git' in root or 'scratch' in root or '_ai' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.css', '.js')):
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
            if cf.endswith('.html'):
                active_content = html_comment_re.sub('', content)
            else:
                active_content = content
                
            if basename in active_content:
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if basename in line:
                        if cf.endswith('.html') and '<!--' in line and '-->' in line:
                            continue
                        rel_cf = os.path.relpath(cf, repo_root).replace('\\', '/')
                        referenced_list.append(f"`{rel_cf}:{i+1}`")
                            
    if referenced_list:
        referenced_list = list(dict.fromkeys(referenced_list))
        print(f"| `{img_path}` | REFERENCED | {', '.join(referenced_list)} |")
    else:
        print(f"| `{img_path}` | NOT REFERENCED | N/A |")
