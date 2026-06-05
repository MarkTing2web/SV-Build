import os
import re

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"

pages = [
    "/portfolio/commercial/altitudex-sentosa-commercial.html",
    "/portfolio/commercial/catholic-centre-security-partnership.html",
    "/portfolio/commercial/em-services-call-centre-redhill.html",
    "/portfolio/commercial/hilton-singapore-orchard-fire-door.html",
    "/portfolio/commercial/scape-commercial.html",
    "/portfolio/commercial/scape-smart-booking-access.html",
    "/portfolio/commercial/st-engineering-mobility-cctv.html",
    "/portfolio/data-centres/fort-st-engineering.html",
    "/portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html",
    "/portfolio/healthcare/surya-home.html",
    "/portfolio/industrial/sta-compliance-imaging.html",
    "/portfolio/institutions/sengkang-interim-bus-interchange.html",
    "/portfolio/managed-living/scb-worker-dormitory-jalan-papan.html"
]

print("| Page | Desktop Hero Image | Mobile Image Exists? |")
print("|---|---|---|")

bg_pattern = re.compile(r'url\([\'"]?([^\'"]+\.webp)[\'"]?\)', re.IGNORECASE)

for page in pages:
    file_path = os.path.join(repo_root, page.lstrip('/'))
    
    if not os.path.exists(file_path):
        print(f"| {page} | HTML FILE NOT FOUND | N/A |")
        continue
        
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Find background images. Usually the hero image is the first one in a <style> block 
    # or inline in <header> that points to an image.
    matches = bg_pattern.findall(content)
    
    desktop_img = None
    for match in matches:
        if '-mobile' not in match and ('/images/portfolio/' in match or '/images/' in match):
            desktop_img = match
            break
            
    if not desktop_img:
        print(f"| {page} | NO HERO IMAGE FOUND IN CODE | N/A |")
        continue
        
    # Construct mobile image path
    # Rule: usually -hero.webp -> -mobile.webp, or just append -mobile
    if desktop_img.endswith('-hero.webp'):
        mobile_img = desktop_img.replace('-hero.webp', '-mobile.webp')
    elif desktop_img.endswith('.webp'):
        mobile_img = desktop_img.replace('.webp', '-mobile.webp')
    elif desktop_img.endswith('.png'):
        mobile_img = desktop_img.replace('.png', '-mobile.webp')
    elif desktop_img.endswith('.jpg'):
        mobile_img = desktop_img.replace('.jpg', '-mobile.webp')
    else:
        mobile_img = desktop_img + "-mobile.webp"
        
    full_mobile_path = os.path.join(repo_root, mobile_img.lstrip('/'))
    
    # Also check variations if the first one doesn't exist
    if not os.path.exists(full_mobile_path):
        if desktop_img.endswith('.webp') and not desktop_img.endswith('-hero.webp'):
            # try finding -mobile without removing anything else
            # e.g., scape-building-profile.webp -> scape-building-profile-mobile.webp
            pass
        elif desktop_img.endswith('-hero.webp'):
            # try just adding -mobile to the hero?
            mobile_img_var = desktop_img.replace('.webp', '-mobile.webp')
            full_var_path = os.path.join(repo_root, mobile_img_var.lstrip('/'))
            if os.path.exists(full_var_path):
                mobile_img = mobile_img_var
                full_mobile_path = full_var_path
            else:
                # check replacing -hero with -mobile
                pass
                
    exists = "YES" if os.path.exists(full_mobile_path) else "NO"
    
    print(f"| {page} | `{desktop_img}` | **{exists}** (`{mobile_img}`) |")
