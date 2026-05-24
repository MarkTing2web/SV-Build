import os
import re

repo_root = r"c:\Projects\SV-Build"

replacements = [
    {
        "file": "solutions/commercial/commercial-security-systems.html",
        "from": "/images/solutions/commercial/commercial-security-systems-hero.webp",
        "to": "/images/solutions/hero-solutions/commercial-security-systems-hero.webp"
    },
    {
        "file": "solutions/condominiums/condominium-security-systems.html",
        "from": "/images/solutions/condominiums/condominium-security-systems-hero.webp",
        "to": "/images/solutions/hero-solutions/condominium-security-systems-hero.webp"
    },
    {
        "file": "solutions/condominiums/managing-agents.html",
        "from": "/images/solutions/solution-condominiums-managing-agents-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-condominiums-managing-agents-hero.webp"
    },
    {
        "file": "solutions/condominiums/mcst.html",
        "from": "/images/solutions/solution-condominiums-mcst-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-condominiums-mcst-hero.webp"
    },
    {
        "file": "solutions/condominiums/security-contractors.html",
        "from": "/images/solutions/solution-condominiums-security-contractors-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-condominiums-security-contractors-hero.webp"
    },
    {
        "file": "solutions/data-centres/data-centre-security-systems.html",
        "from": "/images/solutions/data-centres/data-centre-security-systems-hero.webp",
        "to": "/images/solutions/hero-solutions/data-centre-security-systems-hero.webp"
    },
    {
        "file": "solutions/healthcare/day-care.html",
        "from": "/images/solutions/solution-healthcare-daycare-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-healthcare-daycare-hero.webp"
    },
    {
        "file": "solutions/healthcare/healthcare-security-systems.html",
        "from": "/images/solutions/healthcare/healthcare-security-systems-hero.webp",
        "to": "/images/solutions/hero-solutions/healthcare-security-systems-hero.webp"
    },
    {
        "file": "solutions/industrial/industrial-security-systems.html",
        "from": "/images/solutions/industrial/industrial-security-systems-hero.webp",
        "to": "/images/solutions/hero-solutions/industrial-security-systems-hero.webp"
    },
    {
        "file": "solutions/industrial/logistics.html",
        "from": "/images/solutions/solution-industrial-logistics-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-industrial-logistics-hero.webp"
    },
    {
        "file": "solutions/industrial/manufacturing.html",
        "from": "/images/solutions/solution-industrial-manufacturing-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-industrial-manufacturing-hero.webp"
    },
    {
        "file": "solutions/industrial/tech-park.html",
        "from": "/images/solutions/solution-industrial-tech-park-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-industrial-tech-park-hero.webp"
    },
    {
        "file": "solutions/institutions/community.html",
        "from": "/images/solutions/solution-institutions-community-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-institutions-community-hero.webp"
    },
    {
        "file": "solutions/institutions/govt-office.html",
        "from": "/images/solutions/solution-institutions-govt-office-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-institutions-govt-office-hero.webp"
    },
    {
        "file": "solutions/institutions/institutions-security-systems.html",
        "from": "/images/solutions/institutions/institutions-security-systems-hero.webp",
        "to": "/images/solutions/hero-solutions/institutions-security-systems-hero.webp"
    },
    {
        "file": "solutions/institutions/schools.html",
        "from": "/images/solutions/solution-institutions-schools-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-institutions-schools-hero.webp"
    },
    {
        "file": "solutions/managed-living/co-living.html",
        "from": "/images/solutions/solution-managed-living-co-living-hero.webp",
        "to": "/images/solutions/hero-solutions/solution-managed-living-co-living-hero.webp"
    },
    {
        "file": "solutions/managed-living/managed-living-security-systems.html",
        "from": "/images/solutions/managed-living/managed-living-security-systems-hero.webp",
        "to": "/images/solutions/hero-solutions/managed-living-security-systems-hero.webp"
    }
]

# Regex pattern for og:image tag
og_image_pattern = re.compile(
    r'(<meta\s+[^>]*?property=["\']og:image["\'][^>]*?content=["\'])([^"\']*)(["\'][^>]*?>)'
    r'|'
    r'(<meta\s+[^>]*?content=["\'])([^"\']*)(["\'][^>]*?property=["\']og:image["\'][^>]*?>)',
    re.IGNORECASE
)

updated_count = 0

for item in replacements:
    filepath = os.path.join(repo_root, item["file"])
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {item['file']}")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define replacement handler
    replaced_urls = []
    
    def replacer(match):
        if match.group(1) is not None:
            prefix = match.group(1)
            url = match.group(2)
            suffix = match.group(3)
        else:
            prefix = match.group(4)
            url = match.group(5)
            suffix = match.group(6)
            
        if item["from"] in url:
            new_url = url.replace(item["from"], item["to"])
            replaced_urls.append((url, new_url))
            return f"{prefix}{new_url}{suffix}"
        return match.group(0)

    new_content, count = og_image_pattern.subn(replacer, content)

    if count > 0 and replaced_urls:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(new_content)
        print(f"UPDATED: {item['file']}")
        for old_u, new_u in replaced_urls:
            print(f"  From: {old_u}")
            print(f"  To:   {new_u}")
        updated_count += 1
    else:
        print(f"WARNING: No matching og:image tag found/updated in {item['file']}")

print(f"\nTotal files updated: {updated_count}")
