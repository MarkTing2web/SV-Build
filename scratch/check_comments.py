import os
import re
import glob

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"

checks = [
    ("solutions/commercial/commercial-security-systems.html", "commercial-security-systems-hero-mobile.webp"),
    ("solutions/condominiums/condominium-security-systems.html", "condominium-security-systems-hero-mobile.webp"),
    ("solutions/data-centres/data-centre-security-systems.html", "data-centre-security-systems-hero-mobile.webp"),
    ("solutions/healthcare/healthcare-security-systems.html", "healthcare-security-systems-hero-mobile.webp"),
    ("solutions/industrial/industrial-security-systems.html", "industrial-security-systems-hero-mobile.webp"),
    ("solutions/institutions/institutions-security-systems.html", "institutions-security-systems-hero-mobile.webp"),
    ("solutions/managed-living/managed-living-security-systems.html", "managed-living-security-systems-hero-mobile.webp")
]

def is_comment_or_active(filepath, search_str):
    if not os.path.exists(filepath):
        return "FILE NOT FOUND"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove HTML comments
    clean_content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    if search_str in clean_content:
        return "ACTIVE"
    elif search_str in content:
        return "COMMENT"
    else:
        return "NOT REFERENCED"

for rel_path, filename in checks:
    full_path = os.path.join(repo_root, rel_path.replace('/', os.sep))
    status = is_comment_or_active(full_path, filename)
    print(f"{filename} in {rel_path} : {status}")

print("\nChecking insights/*.html:")
insights_files = glob.glob(os.path.join(repo_root, "insights", "*.html"))
for f in insights_files:
    rel = os.path.relpath(f, repo_root).replace('\\', '/')
    for search_str in ["securevision-insights.webp", "securevision-insights-mobile.webp"]:
        status = is_comment_or_active(f, search_str)
        if status != "NOT REFERENCED":
            print(f"{search_str} in {rel} : {status}")
