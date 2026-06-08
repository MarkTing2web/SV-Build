import os
import re

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

group_ab = [
    "portfolio/commercial/altitudex-sentosa-commercial.html",
    "portfolio/commercial/catholic-centre-security-partnership.html",
    "portfolio/commercial/em-services-call-centre-redhill.html",
    "portfolio/commercial/hilton-singapore-orchard-fire-door.html",
    "portfolio/commercial/scape-commercial.html",
    "portfolio/commercial/scape-smart-booking-access.html",
    "portfolio/commercial/st-engineering-mobility-cctv.html",
    "portfolio/condominiums/clearwater-cctv-upgrade.html",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html",
    "portfolio/data-centres/fort-st-engineering.html",
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/industrial/cogent-logistics-hub-cctv.html",
    "portfolio/industrial/cyrus-tech-industrial.html",
    "portfolio/industrial/mitsubishi-elevator-face-access-bms.html",
    "portfolio/industrial/multibase-construction-security-upgrade.html",
    "portfolio/industrial/smartflex-tampines.html",
    "portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html",
    "portfolio/institutions/catholic-centre-waterloo.html",
    "portfolio/institutions/changi-airport-lpr-barriers.html",
    "portfolio/institutions/das-learning-centre-woodlands.html",
    "portfolio/institutions/my-world-preschool-cctv.html",
    "portfolio/institutions/sengkang-interim-bus-interchange.html",
    "portfolio/institutions/sfx-retreat-centre-punggol.html",
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

all_files = group_ab + [
    "portfolio/condominiums/the-bale-intercom-cctv.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html"
]

def check_clashes(content):
    sections = []
    for match in re.finditer(r'<section([^>]*)>', content, re.IGNORECASE):
        attrs = match.group(1)
        class_match = re.search(r'class=["\']([^"\']*)["\']', attrs, re.IGNORECASE)
        if class_match:
            classes = class_match.group(1).split()
            bg_class = None
            if 'sv-section-grey' in classes:
                bg_class = 'grey'
            elif 'sv-section-white' in classes:
                bg_class = 'white'
                
            if bg_class:
                line_no = content[:match.start()].count('\n') + 1
                sections.append((len(sections) + 1, bg_class, line_no))
                
    clashes = 0
    for i, (sec_idx, bg, line) in enumerate(sections):
        if i > 0:
            _, prev_bg, _ = sections[i-1]
            if bg == prev_bg:
                clashes += 1
    return clashes

with open("fix_sections_output.txt", "w", encoding="utf-8") as out:
    out.write("File | Clashes found | Clashes fixed | Remaining clashes\n")
    out.write("---|---|---|---\n")

    for fpath in all_files:
        full_path = os.path.join(base_dir, fpath)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        initial_clashes = check_clashes(content)
        
        # Apply fix
        if fpath in group_ab:
            # find <section> containing sv-systems-block
            # regex to match <section> ... </section> and ensure it contains class="sv-systems-block"
            # It's safer to just split into lines and find the block
            
            # Since the structure is standard, we can find the section start and end that wraps sv-systems-block
            idx = content.find('class="sv-systems-block"')
            if idx != -1:
                # find the preceding <section>
                sec_start = content.rfind('<section', 0, idx)
                if sec_start != -1:
                    sec_end = content.find('>', sec_start)
                    sec_tag = content[sec_start:sec_end+1]
                    if 'sv-section-grey' in sec_tag:
                        new_sec_tag = sec_tag.replace('sv-section-grey', 'sv-section-white')
                        content = content[:sec_start] + new_sec_tag + content[sec_end+1:]
        elif "the-bale-intercom-cctv.html" in fpath:
            # change the 5th section with sv-section-grey to white. Wait, we can find all sections.
            # Using finditer
            sec_starts = []
            for match in re.finditer(r'<section([^>]*)>', content, re.IGNORECASE):
                attrs = match.group(1)
                if 'sv-section-grey' in attrs or 'sv-section-white' in attrs:
                    sec_starts.append(match)
            if len(sec_starts) >= 5:
                match = sec_starts[4] # 0-indexed, so 5th section
                sec_tag = match.group(0)
                new_sec_tag = sec_tag.replace('sv-section-grey', 'sv-section-white')
                content = content[:match.start()] + new_sec_tag + content[match.end():]
        elif "village-pasir-panjang-condo.html" in fpath:
            sec_starts = []
            for match in re.finditer(r'<section([^>]*)>', content, re.IGNORECASE):
                attrs = match.group(1)
                if 'sv-section-grey' in attrs or 'sv-section-white' in attrs:
                    sec_starts.append(match)
            
            # Change section 6 (idx 5) and 9 (idx 8)
            # Need to apply replacements from back to front to avoid shifting indices
            for idx in [8, 5]:
                if len(sec_starts) > idx:
                    match = sec_starts[idx]
                    sec_tag = match.group(0)
                    new_sec_tag = sec_tag.replace('sv-section-grey', 'sv-section-white')
                    content = content[:match.start()] + new_sec_tag + content[match.end():]
        elif "the-verte-telok-kurau-condo.html" in fpath:
            sec_starts = []
            for match in re.finditer(r'<section([^>]*)>', content, re.IGNORECASE):
                attrs = match.group(1)
                if 'sv-section-grey' in attrs or 'sv-section-white' in attrs:
                    sec_starts.append(match)
            if len(sec_starts) >= 3:
                match = sec_starts[2] # 3rd section
                sec_tag = match.group(0)
                new_sec_tag = sec_tag.replace('sv-section-grey', 'sv-section-white')
                content = content[:match.start()] + new_sec_tag + content[match.end():]

        # check final clashes
        final_clashes = check_clashes(content)
        clashes_fixed = initial_clashes - final_clashes
        
        flag = " 🚩" if final_clashes != 0 else ""
        out.write(f"{fpath} | {initial_clashes} | {clashes_fixed} | {final_clashes}{flag}\n")

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
