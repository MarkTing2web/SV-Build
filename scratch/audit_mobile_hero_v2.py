import os
import glob
import re

workspace = r"c:\Projects\SV-Build"

solutions_files = [
    "solutions/residential.html", "solutions/condominiums.html", "solutions/commercial.html",
    "solutions/industrial.html", "solutions/institutions.html", "solutions/healthcare.html",
    "solutions/managed-living.html", "solutions/data-centres.html",
    "solutions/residential/landed-home-security-systems.html", "solutions/residential/architects-and-designers.html",
    "solutions/residential/home-upgrade.html", "solutions/residential/new-build.html",
    "solutions/condominiums/condominium-security-systems.html", "solutions/condominiums/mcst.html",
    "solutions/condominiums/managing-agents.html", "solutions/condominiums/security-contractors.html",
    "solutions/commercial/commercial-security-systems.html", "solutions/commercial/office.html",
    "solutions/commercial/retail.html", "solutions/commercial/hotel.html",
    "solutions/industrial/industrial-security-systems.html", "solutions/industrial/logistics.html",
    "solutions/industrial/manufacturing.html", "solutions/industrial/tech-park.html",
    "solutions/institutions/institutions-security-systems.html", "solutions/institutions/schools.html",
    "solutions/institutions/govt-office.html", "solutions/institutions/community.html",
    "solutions/healthcare/healthcare-security-systems.html", "solutions/healthcare/aged-care.html",
    "solutions/healthcare/day-care.html",
    "solutions/managed-living/managed-living-security-systems.html", "solutions/managed-living/dormitories.html",
    "solutions/managed-living/co-living.html", "solutions/managed-living/hostels.html",
    "solutions/data-centres/data-centre-security-systems.html",
]

systems_files = [
    "systems/premises-security.html", "systems/entry-access-control.html",
    "systems/vehicle-lpr-management.html", "systems/ip-phone-communications.html",
    "systems/network-infrastructure.html", "systems/security-management-platform.html",
]

brands_files = glob.glob(os.path.join(workspace, "brands", "*.html"))
brands_files = [os.path.relpath(f, workspace).replace('\\', '/') for f in brands_files]

resources_files = [
    "resources/index.html", "resources/guides.html", "resources/checklists.html",
    "resources/calculators.html", "resources/library.html", "resources/training-videos.html",
    "resources/faq.html",
]

all_files = {
    "Solutions": solutions_files,
    "Systems": systems_files,
    "Brands": brands_files,
    "Resources": resources_files
}

results = {
    "correct": 0, "same": 0, "missing": 0, "none": 0, "total": 0
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
        
        url_regex = r'url\([\'"]?([^\'"]+\.(?:webp|png|jpg|jpeg))[\'"]?\)'
        
        # Split style content by @media (max-width: 768px)
        # Note: there could be multiple media queries. We want the desktop one first.
        media_split = re.split(r'@media\s*\(\s*max-width:\s*768px\s*\)\s*\{', style_content, flags=re.IGNORECASE)
        
        desktop_css = media_split[0]
        
        desk_urls = re.findall(url_regex, desktop_css)
        if not desk_urls:
            results["none"] += 1
            continue
            
        # We assume the first URL in desktop CSS is the hero image
        desktop_img = desk_urls[0]
        
        mob_img = None
        has_media = len(media_split) > 1
        
        if has_media:
            # check the first @media block
            mobile_css = media_split[1].split('}')[0] # extract contents roughly
            
            # actually we should properly extract the block for mobile css. 
            # `media_split[1]` goes till the end of the style block.
            # let's just find any url inside the `@media (max-width: 768px)` block
            media_m = re.search(r'@media\s*\(\s*max-width:\s*768px\s*\)\s*\{([^}]+)\}', style_content, re.DOTALL | re.IGNORECASE)
            if media_m:
                mob_urls = re.findall(url_regex, media_m.group(1))
                if mob_urls:
                    mob_img = mob_urls[0]
        
        if not has_media or not mob_img:
            results["missing"] += 1
            cat_output.append(f"❌ NO MOBILE OVERRIDE - {rel_path}")
        else:
            if mob_img == desktop_img:
                results["same"] += 1
                cat_output.append(f"⚠️ MOBILE SAME AS DESKTOP - {rel_path}")
            else:
                results["correct"] += 1

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
