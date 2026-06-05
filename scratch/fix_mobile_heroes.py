import os

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"

replacements = [
    (
        "solutions/commercial/commercial-security-systems.html",
        "/images/solutions/commercial/commercial-security-systems-hero-mobile.webp",
        "/images/solutions/hero-solutions/commercial-security-systems-hero-mobile.webp"
    ),
    (
        "solutions/condominiums/condominium-security-systems.html",
        "/images/solutions/condominiums/condominium-security-systems-hero-mobile.webp",
        "/images/solutions/hero-solutions/condominium-security-systems-hero-mobile.webp"
    ),
    (
        "solutions/data-centres/data-centre-security-systems.html",
        "/images/solutions/data-centres/data-centre-security-systems-hero-mobile.webp",
        "/images/solutions/hero-solutions/data-centre-security-systems-hero-mobile.webp"
    ),
    (
        "solutions/healthcare/healthcare-security-systems.html",
        "/images/solutions/healthcare/healthcare-security-systems-hero-mobile.webp",
        "/images/solutions/hero-solutions/healthcare-security-systems-hero-mobile.webp"
    ),
    (
        "solutions/industrial/industrial-security-systems.html",
        "/images/solutions/industrial/industrial-security-systems-hero-mobile.webp",
        "/images/solutions/hero-solutions/industrial-security-systems-hero-mobile.webp"
    ),
    (
        "solutions/institutions/institutions-security-systems.html",
        "/images/solutions/institutions/institutions-security-systems-hero-mobile.webp",
        "/images/solutions/hero-solutions/institutions-security-systems-hero-mobile.webp"
    ),
    (
        "solutions/managed-living/managed-living-security-systems.html",
        "/images/solutions/managed-living/managed-living-security-systems-hero-mobile.webp",
        "/images/solutions/hero-solutions/managed-living-security-systems-hero-mobile.webp"
    )
]

for file_rel, find_str, rep_str in replacements:
    path = os.path.join(repo_root, file_rel.replace("/", os.sep))
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if find_str in content:
        content = content.replace(find_str, rep_str)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"FIXED: {file_rel}")
    else:
        print(f"FAILED: {file_rel} (Pattern not found)")
        
print("\n--- VERIFICATION PASS ---")
for file_rel, find_str, rep_str in replacements:
    path = os.path.join(repo_root, file_rel.replace("/", os.sep))
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if find_str in content:
        print(f"ERROR: Wrong path still exists in {file_rel}")
    elif rep_str in content:
        print(f"CONFIRMED: Correct path verified in {file_rel}")
    else:
        print(f"ERROR: Neither path found in {file_rel}")
