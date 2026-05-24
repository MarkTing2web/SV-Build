import os
import re
from bs4 import BeautifulSoup

repo_root = r"c:\Projects\SV-Build"

files_list = [
    # ROOT
    "index.html",
    "contact.html",
    "contact-gateway.html",
    "booking-success.html",
    "contact-success.html",
    "thank-you-booking.html",
    "thank-you-proposal.html",
    "request-site-assessment-singapore.html",
    # ABOUT
    "about.html",
    "about/index.html",
    # SYSTEMS
    "systems/index.html",
    "systems/entry-access-control.html",
    "systems/ip-phone-communications.html",
    "systems/network-infrastructure.html",
    "systems/premises-security.html",
    "systems/security-management-platform.html",
    "systems/vehicle-lpr-management.html",
    # SOLUTIONS (all files)
    "solutions/index.html",
    "solutions/automate-vehicle-access.html",
    "solutions/commercial.html",
    "solutions/commercial/commercial-security-systems.html",
    "solutions/commercial/hotel.html",
    "solutions/commercial/office.html",
    "solutions/commercial/retail.html",
    "solutions/condominiums.html",
    "solutions/condominiums/condominium-security-systems.html",
    "solutions/condominiums/managing-agents.html",
    "solutions/condominiums/mcst.html",
    "solutions/condominiums/security-contractors.html",
    "solutions/data-centres.html",
    "solutions/data-centres/data-centre-security-systems.html",
    "solutions/healthcare.html",
    "solutions/healthcare/aged-care.html",
    "solutions/healthcare/day-care.html",
    "solutions/healthcare/healthcare-security-systems.html",
    "solutions/improve-cctv-visibility.html",
    "solutions/improve-visitor-management.html",
    "solutions/industrial.html",
    "solutions/industrial/industrial-security-systems.html",
    "solutions/industrial/logistics.html",
    "solutions/industrial/manufacturing.html",
    "solutions/industrial/tech-park.html",
    "solutions/institutions.html",
    "solutions/institutions/community.html",
    "solutions/institutions/govt-office.html",
    "solutions/institutions/institutions-security-systems.html",
    "solutions/institutions/schools.html",
    "solutions/managed-living.html",
    "solutions/managed-living/co-living.html",
    "solutions/managed-living/dormitories.html",
    "solutions/managed-living/hostels.html",
    "solutions/managed-living/managed-living-security-systems.html",
    "solutions/reduce-guard-manpower.html",
    "solutions/residential.html",
    "solutions/residential/architects-and-designers.html",
    "solutions/residential/home-upgrade.html",
    "solutions/residential/landed-home-security-systems.html",
    "solutions/residential/new-build.html",
    "solutions/upgrade-intercom-system.html"
]

url_pattern = re.compile(r'url\(\s*[\'"]?([^\'")\s]+)[\'"]?\s*\)', re.IGNORECASE)

fallback_img = "/images/hero-security-solutions-singapore.webp"

total_updated = 0
total_flagged = 0

print("=" * 65)
print("OG:IMAGE META TAG UPDATE AUDIT & EXECUTION")
print("=" * 65)

for rel_path in files_list:
    filepath = os.path.join(repo_root, rel_path)
    if not os.path.exists(filepath):
        # SKIP if file does not exist (like about/index.html which is optional)
        if "about/index.html" in rel_path:
            continue
        print(f"{rel_path} — NOT FOUND")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    
    # 1. Determine the desktop hero image
    desktop_hero = None
    
    # Get header class names
    header = soup.find('header')
    header_classes = []
    if header:
        header_classes = header.get('class') or []
        # check if it has inline style
        header_style = header.get('style') or ''
        matches = url_pattern.findall(header_style)
        if matches:
            desktop_hero = matches[0]
            
    if not desktop_hero:
        # Check style tags for classes matching header
        style_content = ""
        for style in soup.find_all('style'):
            style_content += (style.string or "") + "\n"
            
        # Try to find class definitions
        for hc in header_classes:
            pattern = rf'\.{hc}\s*\{{[^}}]*\}}'
            match = re.search(pattern, style_content, re.IGNORECASE | re.DOTALL)
            if match:
                urls = url_pattern.findall(match.group(0))
                # filter out -mobile and -rel
                for u in urls:
                    if '-mobile' not in u.lower() and '-rel' not in u.lower():
                        desktop_hero = u
                        break
            if desktop_hero:
                break
                
    if not desktop_hero:
        # fallback: find first webp/png/jpg in style that is not -mobile or -rel
        urls = url_pattern.findall(style_content)
        for u in urls:
            if '-mobile' not in u.lower() and '-rel' not in u.lower():
                desktop_hero = u
                break
                
    # Normalize path to root-relative /images/...
    hero_path = None
    flagged = False
    
    if desktop_hero:
        desktop_hero = desktop_hero.strip().replace('"', '').replace("'", "")
        # Remove queries/hashes
        desktop_hero = desktop_hero.split('?')[0].split('#')[0]
        
        # If relative (contains images/...)
        idx = desktop_hero.find('images/')
        if idx != -1:
            hero_path = "/" + desktop_hero[idx:]
        else:
            # Fallback to the exact path
            hero_path = desktop_hero
            if not hero_path.startswith('/'):
                hero_path = "/" + hero_path
    else:
        # Fallback for pages with no clear hero image
        hero_path = fallback_img
        # Flag if a hero was expected but not found, excluding typical fallback pages
        non_hero_pages = ["contact-success.html", "thank-you-booking.html", "thank-you-proposal.html", "booking-success.html", "contact.html", "contact-gateway.html"]
        if not any(nh in rel_path for nh in non_hero_pages):
            flagged = True

    # Prepend domain
    og_img_val = f"https://www.securevision.com.sg{hero_path}"
    
    # 2. Update or Insert the og:image meta tag
    # Find existing og:image
    meta_og_image = soup.find('meta', property='og:image')
    if not meta_og_image:
        meta_og_image = soup.find('meta', attrs={"name": "og:image"})
        
    if meta_og_image:
        # Replace value
        # We need to replace it in the original content string to preserve formatting,
        # or rewrite the file using soup. But BeautifulSoup changes format.
        # Let's do exact regex replacement on content for safety.
        # Find the tag in raw html
        raw_tag = str(meta_og_image)
        # Construct new tag
        new_tag = f'<meta property="og:image" content="{og_img_val}">'
        # Let's find any meta tag with og:image in content
        # property="og:image" or name="og:image"
        pattern = re.compile(r'<meta\s+[^>]*?(?:property|name)=["\']og:image["\'][^>]*?>', re.IGNORECASE)
        match = pattern.search(content)
        if match:
            content = content[:match.start()] + new_tag + content[match.end():]
        else:
            # Fallback replacement if regex failed
            content = content.replace(raw_tag, new_tag)
    else:
        # Find og:description tag to insert after
        meta_og_desc = soup.find('meta', property='og:description')
        if not meta_og_desc:
            meta_og_desc = soup.find('meta', attrs={"name": "og:description"})
            
        new_tag = f'<meta property="og:image" content="{og_img_val}">'
        
        if meta_og_desc:
            raw_desc = str(meta_og_desc)
            # Find in raw content
            idx = content.find(raw_desc)
            if idx != -1:
                # Add newline and same indentation
                # Find indentation of description tag
                start_line = content.rfind('\n', 0, idx)
                indent = ""
                if start_line != -1:
                    indent = content[start_line+1 : idx]
                content = content[:idx + len(raw_desc)] + f"\n{indent}{new_tag}" + content[idx + len(raw_desc):]
            else:
                # fallback: append before </head>
                content = content.replace('</head>', f'  {new_tag}\n</head>')
        else:
            # Append before </head>
            content = content.replace('</head>', f'  {new_tag}\n</head>')

    # Write back
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
        
    status_str = "flagged" if flagged else "set"
    print(f"{rel_path} — og:image set to: {og_img_val}" + (" [FLAGGED]" if flagged else ""))
    
    if flagged:
        total_flagged += 1
    else:
        total_updated += 1

print("\nSummary:")
print(f"  Total files updated: {total_updated}")
print(f"  Total files flagged: {total_flagged}")
