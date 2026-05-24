import os

repo_root = r"c:\Projects\SV-Build"

targets = {
    "solutions/condominiums/managing-agents.html": [
        "solution-condominiums-managing-agents-hero.webp",
        "solution-condominiums-managing-agents-hero-mobile.webp"
    ],
    "solutions/condominiums/mcst.html": [
        "solution-condominiums-mcst-hero.webp",
        "solution-condominiums-mcst-hero-mobile.webp"
    ],
    "solutions/condominiums/security-contractors.html": [
        "solution-condominiums-security-contractors-hero.webp",
        "solution-condominiums-security-contractors-hero-mobile.webp"
    ],
    "solutions/healthcare/aged-care.html": [
        "solution-healthcare-aged-care-hero-mobile.webp"
    ],
    "solutions/healthcare/day-care.html": [
        "solution-healthcare-daycare-hero.webp",
        "solution-healthcare-daycare-hero-mobile.webp"
    ],
    "solutions/industrial/logistics.html": [
        "solution-industrial-logistics-hero.webp",
        "solution-industrial-logistics-hero-mobile.webp"
    ],
    "solutions/industrial/manufacturing.html": [
        "solution-industrial-manufacturing-hero.webp",
        "solution-industrial-manufacturing-hero-mobile.webp"
    ],
    "solutions/industrial/tech-park.html": [
        "solution-industrial-tech-park-hero.webp",
        "solution-industrial-tech-park-hero-mobile.webp"
    ],
    "solutions/institutions/community.html": [
        "solution-institutions-community-hero.webp",
        "solution-institutions-community-hero-mobile.webp"
    ],
    "solutions/institutions/govt-office.html": [
        "solution-institutions-govt-office-hero.webp",
        "solution-institutions-govt-office-hero-mobile.webp"
    ],
    "solutions/institutions/schools.html": [
        "solution-institutions-schools-hero.webp",
        "solution-institutions-schools-hero-mobile.webp"
    ],
    "solutions/managed-living/co-living.html": [
        "solution-managed-living-co-living-hero.webp",
        "solution-managed-living-co-living-hero-mobile.webp"
    ],
    "solutions/managed-living/dormitories.html": [
        "solution-managed-living-dormitories-hero-mobile.webp"
    ],
    "solutions/managed-living/hostels.html": [
        "solution-managed-living-hostels-hero-mobile.webp"
    ]
}

total_changed = 0

for rel_path, imgs in targets.items():
    filepath = os.path.join(repo_root, rel_path)
    if not os.path.exists(filepath):
        print(f"ERROR: File not found {rel_path}")
        continue

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    file_changed = 0
    flagged = []

    for img in imgs:
        target_path = f"/images/solutions/{img}"
        replacement_path = f"/images/solutions/hero-solutions/{img}"
        
        # Also check without leading slash just in case
        target_path_no_slash = f"images/solutions/{img}"
        replacement_path_no_slash = f"images/solutions/hero-solutions/{img}"

        # We need to make sure we don't accidentally replace something already in hero-solutions/
        # Check target_path
        changed_img = 0
        
        # If target_path is in content, replace it
        if target_path in content:
            count = content.count(target_path)
            content = content.replace(target_path, replacement_path)
            file_changed += count
            changed_img += count
            
        # If target_path_no_slash is in content and not preceded by / or another folder,
        # replace it. But replace_path_no_slash has 'hero-solutions' in it.
        # Simple solution: since we're matching f"images/solutions/{img}" and replacing with f"images/solutions/hero-solutions/{img}",
        # if the file had "/images/solutions/{img}", the replace of "images/solutions/{img}" would make it "/images/solutions/hero-solutions/{img}"!
        # So replacing "images/solutions/{img}" with "images/solutions/hero-solutions/{img}" is the most robust and covers both!
        # BUT wait! If it already had "/images/solutions/hero-solutions/{img}", then "images/solutions/hero-solutions/{img}" is in the file.
        # "images/solutions/{img}" is a substring of "images/solutions/hero-solutions/{img}".
        # Ah! That's a huge gotcha! "images/solutions/{img}" is indeed a substring of "images/solutions/hero-solutions/{img}"!
        # So we MUST NOT do a simple replacement of "images/solutions/{img}" because it would match "images/solutions/hero-solutions/{img}"
        # and turn it into "images/solutions/hero-solutions/hero-solutions/{img}"!
        # This is a very important warning!
        
        # To avoid this, we can search for the exact "/images/solutions/{img}" or do a regex replacement:
        # e.g., matching a prefix that is not followed by "hero-solutions/".
        # Let's do exact substring replacement of:
        # 1) `"/images/solutions/{img}"` -> `"/images/solutions/hero-solutions/{img}"`
        # 2) `'/images/solutions/{img}'` -> `'/images/solutions/hero-solutions/{img}'`
        # This is 100% safe.
        
        for q in ['"', "'"]:
            t1 = f"{q}/images/solutions/{img}{q}"
            r1 = f"{q}/images/solutions/hero-solutions/{img}{q}"
            if t1 in content:
                count = content.count(t1)
                content = content.replace(t1, r1)
                file_changed += count
                changed_img += count
                
            # Also handle cases inside url() or other formats where quotes might be different or optional
            t2 = f"url('/images/solutions/{img}')"
            r2 = f"url('/images/solutions/hero-solutions/{img}')"
            if t2 in content:
                count = content.count(t2)
                content = content.replace(t2, r2)
                file_changed += count
                changed_img += count
                
            t3 = f"url(\"/images/solutions/{img}\")"
            r3 = f"url(\"/images/solutions/hero-solutions/{img}\")"
            if t3 in content:
                count = content.count(t3)
                content = content.replace(t3, r3)
                file_changed += count
                changed_img += count
                
            # Also check for url(/images/solutions/{img}) without quotes
            t4 = f"url(/images/solutions/{img})"
            r4 = f"url(/images/solutions/hero-solutions/{img})"
            if t4 in content:
                count = content.count(t4)
                content = content.replace(t4, r4)
                file_changed += count
                changed_img += count

        # If it was still not found and no changes made, flag it
        if changed_img == 0:
            flagged.append(img)

    if file_changed > 0:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        total_changed += file_changed
        print(f"UPDATED: {rel_path} — {file_changed} references updated")
    else:
        print(f"NO CHANGES: {rel_path}")

    if flagged:
        for fimg in flagged:
            print(f"  FLAG: Reference to {fimg} not found or already updated in {rel_path}")

print(f"\nTotal references updated: {total_changed}")
