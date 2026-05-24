import os

repo_root = r"c:\Projects\SV-Build"

# List of replacements per file
# We omit those where the destination -rel file is missing
replacements = {
    "solutions/industrial.html": [
        (
            "/images/solutions/hero-solutions/solution-industrial-industrial-analysis.webp",
            "/images/solutions/hero-solutions/solution-industrial-logistics-hero-rel.webp"
        ),
        (
            "/images/solutions/root-solutions/solution-commercial-pillar_surveillance.webp",
            "/images/solutions/hero-solutions/solution-industrial-manufacturing-hero-rel.webp"
        ),
        (
            "/images/solutions/hero-solutions/solution-commercial-office-hero.webp",
            "/images/solutions/hero-solutions/solution-industrial-tech-park-hero-rel.webp"
        )
    ],
    "solutions/institutions.html": [
        (
            "/images/solutions/root-solutions/solution-institutions.webp",
            "/images/solutions/hero-solutions/solution-institutions-schools-hero-rel.webp"
        ),
        (
            "/images/solutions/root-solutions/solution-institutions-project-religious.webp",
            "/images/solutions/hero-solutions/solution-institutions-govt-office-hero-rel.webp"
        )
    ],
    "solutions/managed-living.html": [
        (
            "/images/portfolio/portfolio-industrial.png",
            "/images/solutions/hero-solutions/industrial-security-singapore-rel.webp"
        ),
        (
            "/images/solutions/hero-solutions/healthcare-hero.webp",
            "/images/solutions/hero-solutions/healthcare-security-singapore-rel.webp"
        ),
        (
            "/images/solutions/hero-solutions/managed-living-hero.webp",
            "/images/solutions/hero-solutions/condominium-estate-security-singapore-rel.webp"
        )
    ],
    "solutions/data-centres.html": [
        (
            "/images/portfolio/portfolio-industrial.png",
            "/images/solutions/hero-solutions/industrial-security-singapore-rel.webp"
        ),
        (
            "/images/solutions/root-solutions/solution-commercial-hero.webp",
            "/images/solutions/hero-solutions/commercial-security-singapore-rel.webp"
        )
    ],
    "solutions/automate-vehicle-access.html": [
        (
            "/images/solutions/root-solutions/solution-automate-vehicle-access-prop-condo.webp",
            "/images/solutions/hero-solutions/condominium-estate-security-singapore-rel.webp"
        ),
        (
            "/images/solutions/root-solutions/solution-automate-vehicle-access-prop-commercial.webp",
            "/images/solutions/hero-solutions/commercial-security-singapore-rel.webp"
        ),
        (
            "/images/solutions/root-solutions/solution-automate-vehicle-access-prop-industrial.webp",
            "/images/solutions/hero-solutions/industrial-security-singapore-rel.webp"
        )
    ],
    "solutions/improve-cctv-visibility.html": [
        (
            "/images/solutions/root-solutions/solution-automate-vehicle-access-prop-condo.webp",
            "/images/solutions/hero-solutions/condominium-estate-security-singapore-rel.webp"
        ),
        (
            "/images/solutions/root-solutions/solution-automate-vehicle-access-prop-commercial.webp",
            "/images/solutions/hero-solutions/commercial-security-singapore-rel.webp"
        ),
        (
            "/images/solutions/root-solutions/solution-automate-vehicle-access-prop-industrial.webp",
            "/images/solutions/hero-solutions/industrial-security-singapore-rel.webp"
        )
    ]
}

total_updates = 0
updated_files = {}

for rel_path, pairs in replacements.items():
    filepath = os.path.join(repo_root, rel_path)
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {rel_path}")
        continue

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    file_updates = 0
    for from_src, to_src in pairs:
        # Also check without leading slash or relative just in case,
        # but the prompt specifically lists "/images/...".
        # Let's check both options:
        # 1) "/images/..." -> "/images/..."
        # 2) "images/..." -> "images/..."
        # Let's do a strict replacement of the exact string from_src
        if from_src in content:
            count = content.count(from_src)
            content = content.replace(from_src, to_src)
            file_updates += count
        else:
            # Check without leading slash
            from_src_no_slash = from_src.lstrip('/')
            to_src_no_slash = to_src.lstrip('/')
            if from_src_no_slash in content:
                count = content.count(from_src_no_slash)
                content = content.replace(from_src_no_slash, to_src_no_slash)
                file_updates += count
            else:
                print(f"WARNING: Source string '{from_src}' not found in {rel_path}")

    if file_updates > 0:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        updated_files[rel_path] = file_updates
        total_updates += file_updates
        print(f"UPDATED: {rel_path} — {file_updates} replacements made")
    else:
        print(f"NO UPDATES MADE: {rel_path}")

print("\n" + "="*50)
print(f"Total replacements made: {total_updates}")
print(f"Total files changed: {len(updated_files)}")
