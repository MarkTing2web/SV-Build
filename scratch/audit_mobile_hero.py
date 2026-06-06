import os
import glob
import re

workspace = r"c:\Projects\SV-Build"

solutions_files = [
    "solutions/residential.html",
    "solutions/condominiums.html",
    "solutions/commercial.html",
    "solutions/industrial.html",
    "solutions/institutions.html",
    "solutions/healthcare.html",
    "solutions/managed-living.html",
    "solutions/data-centres.html",
    "solutions/residential/landed-home-security-systems.html",
    "solutions/residential/architects-and-designers.html",
    "solutions/residential/home-upgrade.html",
    "solutions/residential/new-build.html",
    "solutions/condominiums/condominium-security-systems.html",
    "solutions/condominiums/mcst.html",
    "solutions/condominiums/managing-agents.html",
    "solutions/condominiums/security-contractors.html",
    "solutions/commercial/commercial-security-systems.html",
    "solutions/commercial/office.html",
    "solutions/commercial/retail.html",
    "solutions/commercial/hotel.html",
    "solutions/industrial/industrial-security-systems.html",
    "solutions/industrial/logistics.html",
    "solutions/industrial/manufacturing.html",
    "solutions/industrial/tech-park.html",
    "solutions/institutions/institutions-security-systems.html",
    "solutions/institutions/schools.html",
    "solutions/institutions/govt-office.html",
    "solutions/institutions/community.html",
    "solutions/healthcare/healthcare-security-systems.html",
    "solutions/healthcare/aged-care.html",
    "solutions/healthcare/day-care.html",
    "solutions/managed-living/managed-living-security-systems.html",
    "solutions/managed-living/dormitories.html",
    "solutions/managed-living/co-living.html",
    "solutions/managed-living/hostels.html",
    "solutions/data-centres/data-centre-security-systems.html",
]

systems_files = [
    "systems/premises-security.html",
    "systems/entry-access-control.html",
    "systems/vehicle-lpr-management.html",
    "systems/ip-phone-communications.html",
    "systems/network-infrastructure.html",
    "systems/security-management-platform.html",
]

brands_files = glob.glob(os.path.join(workspace, "brands", "*.html"))
brands_files = [os.path.relpath(f, workspace).replace('\\', '/') for f in brands_files]

resources_files = [
    "resources/index.html",
    "resources/guides.html",
    "resources/checklists.html",
    "resources/calculators.html",
    "resources/library.html",
    "resources/training-videos.html",
    "resources/faq.html",
]

all_files = {
    "Solutions": solutions_files,
    "Systems": systems_files,
    "Brands": brands_files,
    "Resources": resources_files
}

results = {
    "correct": 0,
    "same": 0,
    "missing": 0,
    "none": 0,
    "total": 0
}

output = []

for category, files in all_files.items():
    cat_output = []
    for rel_path in files:
        full_path = os.path.join(workspace, rel_path)
        if not os.path.exists(full_path):
            continue
            
        results["total"] += 1
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        head_m = re.search(r'<head>(.*?)</head>', content, re.DOTALL | re.IGNORECASE)
        head_content = head_m.group(1) if head_m else ""
        
        style_m = re.search(r'<style>(.*?)</style>', head_content, re.DOTALL | re.IGNORECASE)
        style_content = style_m.group(1) if style_m else ""
        
        # Check for desktop hero image
        bg_img_m = re.search(r'background-image:\s*url\([\'"]?([^\'"]+)[\'"]?\)', style_content)
        if not bg_img_m:
            results["none"] += 1
            continue
            
        desktop_img = bg_img_m.group(1)
        
        # Check for mobile override
        media_m = re.search(r'@media\s*\(\s*max-width:\s*768px\s*\)\s*\{([^}]+)\}', style_content, re.DOTALL | re.IGNORECASE)
        if media_m:
            media_content = media_m.group(1)
            mob_img_m = re.search(r'background-image:\s*url\([\'"]?([^\'"]+)[\'"]?\)', media_content)
            if mob_img_m:
                mob_img = mob_img_m.group(1)
                if mob_img == desktop_img:
                    results["same"] += 1
                    cat_output.append(f"⚠️ MOBILE SAME AS DESKTOP - {rel_path}")
                elif "-mobile" in mob_img:
                    results["correct"] += 1
                else:
                    # Treat as correct if different from desktop (user says separate -mobile.webp path, but let's be lenient if it's different)
                    # wait, user specifically said "with separate -mobile.webp path". 
                    if "-mobile.webp" in mob_img:
                        results["correct"] += 1
                    else:
                        results["same"] += 1 # it's not -mobile.webp, flag it maybe? Actually just check if it's different
                        cat_output.append(f"⚠️ DIFFERENT BUT NOT -MOBILE - {rel_path}")
            else:
                results["missing"] += 1
                cat_output.append(f"❌ NO MOBILE OVERRIDE - {rel_path}")
        else:
            results["missing"] += 1
            cat_output.append(f"❌ NO MOBILE OVERRIDE - {rel_path}")
            
    if cat_output:
        output.append(f"### {category}")
        output.extend(cat_output)
        output.append("")

print("\n".join(output))

print("--- SUMMARY ---")
print(f"Total pages checked: {results['total']}")
print(f"Pages with correct mobile override: {results['correct']}")
print(f"Pages missing mobile override: {results['missing']}")
print(f"Pages using same image for mobile: {results['same']}")
print(f"Pages with no hero image: {results['none']}")
