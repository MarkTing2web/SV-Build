import os
import re

files_changes = {
    "portfolio/condominiums/clearwater-access-salto-partnership.html": {"exact_find": '<section class="final-cta cta-high-impact section-spacing">', "exact_repl": '<section class="cta-section cta-high-impact cta-property">'},
    "portfolio/condominiums/clearwater-cctv-upgrade.html": {"exact_find": '<section class="final-cta cta-high-impact section-spacing">', "exact_repl": '<section class="cta-section cta-high-impact cta-property">'},
    "portfolio/condominiums/high-oak-condominium-cctv.html": {"exact_find": '<section class="final-cta cta-high-impact section-spacing">', "exact_repl": '<section class="cta-section cta-high-impact cta-property">'},
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html": {"exact_find": '<section class="final-cta cta-high-impact section-spacing">', "exact_repl": '<section class="cta-section cta-high-impact cta-property">'},
    "portfolio/industrial/cogent-logistics-hub-cctv.html": {"exact_find": '<section class="final-cta cta-high-impact cta-indus section-spacing">', "exact_repl": '<section class="cta-section cta-high-impact cta-facilities">'},
    "portfolio/industrial/mitsubishi-elevator-face-access-bms.html": {"exact_find": '<section class="final-cta cta-high-impact cta-indus section-spacing">', "exact_repl": '<section class="cta-section cta-high-impact cta-facilities">'},
    "portfolio/commercial/catholic-centre-security-partnership.html": {"add_class": "cta-facilities", "remove_spacing": True},
    "portfolio/commercial/em-services-call-centre-redhill.html": {"add_class": "cta-facilities", "remove_spacing": True},
    "portfolio/commercial/scape-smart-booking-access.html": {"add_class": "cta-facilities", "remove_spacing": True},
    "portfolio/commercial/st-engineering-mobility-cctv.html": {"add_class": "cta-facilities", "remove_spacing": True},
    "portfolio/condominiums/hillview-park-cctv-upgrade.html": {"add_class": "cta-property", "remove_spacing": True},
    "portfolio/institutions/das-learning-centre-woodlands.html": {"add_class": "cta-facilities", "remove_spacing": True},
    "portfolio/institutions/my-world-preschool-cctv.html": {"add_class": "cta-facilities", "remove_spacing": True},
    "portfolio/industrial/multibase-construction-security-upgrade.html": {"add_class": "cta-facilities", "remove_spacing": True},
    "portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html": {"add_class": "cta-facilities", "remove_spacing": True},
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html": {"add_class": "cta-care", "remove_spacing": True},
    "portfolio/data-centres/fort-data-centre-access-upgrade.html": {"add_class": "cta-compliance", "remove_spacing": True}
}

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

print("File | Final CTA opening tag after fix | Flags")
print("---|---|---")

for fpath, instructions in files_changes.items():
    full_path = os.path.join(base_dir, fpath)
    if not os.path.exists(full_path):
        print(f"{fpath} | NOT FOUND | 🚩 File missing")
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    final_tag = ""

    if "exact_find" in instructions:
        # Do exact replacement
        if instructions["exact_find"] in new_content:
            new_content = new_content.replace(instructions["exact_find"], instructions["exact_repl"])
            final_tag = instructions["exact_repl"]
        else:
            # Just in case we missed it because of spacing, use regex fallback
            pattern3 = re.compile(r'<section[^>]*class="[^"]*cta-high-impact[^"]*"[^>]*>')
            match3 = pattern3.search(new_content)
            if match3:
                tag = match3.group(0)
                final_tag = instructions["exact_repl"]
                new_content = new_content.replace(tag, final_tag)
            else:
                final_tag = "TAG NOT FOUND"
    else:
        # Find the CTA section
        pattern = re.compile(r'<section([^>]*)class="([^"]*cta-section[^"]*cta-high-impact[^"]*|[^"]*cta-high-impact[^"]*cta-section[^"]*)"([^>]*)>')
        match = pattern.search(new_content)
        if match:
            attrs_before = match.group(1)
            classes = match.group(2).split()
            attrs_after = match.group(3)
            
            if "section-spacing" in classes:
                classes.remove("section-spacing")
            if "final-cta" in classes:
                classes.remove("final-cta")
            if "cta-indus" in classes:
                classes.remove("cta-indus")
                
            cls_to_add = instructions["add_class"]
            if cls_to_add not in classes:
                classes.append(cls_to_add)
                
            new_classes = " ".join(classes)
            final_tag = f'<section{attrs_before}class="{new_classes}"{attrs_after}>'
            new_content = new_content[:match.start()] + final_tag + new_content[match.end():]
        else:
            pattern2 = re.compile(r'<section[^>]*class="[^"]*cta-high-impact[^"]*"[^>]*>')
            match2 = pattern2.search(new_content)
            if match2:
                tag = match2.group(0)
                class_match = re.search(r'class="([^"]*)"', tag)
                if class_match:
                    classes = class_match.group(1).split()
                    if "section-spacing" in classes:
                        classes.remove("section-spacing")
                    if "final-cta" in classes:
                        classes.remove("final-cta")
                    if "cta-indus" in classes:
                        classes.remove("cta-indus")
                    
                    if "cta-section" not in classes:
                        classes.append("cta-section")
                        
                    cls_to_add = instructions["add_class"]
                    if cls_to_add not in classes:
                        classes.append(cls_to_add)
                        
                    new_classes = " ".join(classes)
                    final_tag = re.sub(r'class="[^"]*"', f'class="{new_classes}"', tag)
                    new_content = new_content.replace(tag, final_tag)
            else:
                final_tag = "TAG NOT FOUND"

    # Write back
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    # Verification
    flags = []
    if final_tag and final_tag != "TAG NOT FOUND":
        cls_match = re.search(r'class="([^"]*)"', final_tag)
        if cls_match:
            cls_list = cls_match.group(1).split()
            if "cta-section" not in cls_list:
                flags.append("Missing cta-section")
            if "final-cta" in cls_list:
                flags.append("Contains final-cta")
            if "cta-high-impact" not in cls_list:
                flags.append("Missing cta-high-impact")
                
            valid_themes = ["cta-property", "cta-facilities", "cta-care", "cta-compliance"]
            if not any(t in cls_list for t in valid_themes):
                flags.append("Missing theme class")
                
            if "section-spacing" in cls_list:
                flags.append("Contains section-spacing")
            if "cta-indus" in cls_list:
                flags.append("Contains cta-indus")
        else:
            flags.append("No class attribute")
    else:
        flags.append("Tag not found")

    flag_str = " ".join([f"🚩 {msg}" for msg in flags]) if flags else "Passed"
    
    safe_tag = final_tag.replace("<", "&lt;").replace(">", "&gt;")
    
    print(f"{fpath} | `{safe_tag}` | {flag_str}")
