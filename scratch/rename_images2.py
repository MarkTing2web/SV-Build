import os

repo_root = r"c:\Projects\SV-Build"
images_dir = os.path.join(repo_root, "images", "insights")
insights_dir = os.path.join(repo_root, "insights")

renames = {
    "how-ip-cctv-works-poe-switch-installation.webp": "ip-cctv-poe-switch.webp",
    "how-ip-cctv-works-surveillance-hard-disk.webp": "ip-cctv-hard-disk.webp",
    "securevision-sales-guarding-technology.webp": "guarding-tech-consultation.webp",
    "condo-security-upgrade-quotes-condo-tender-specification.webp": "condo-quotes-spec-document.webp",
    "condo-security-upgrade-timeline-condo-installation-phases.webp": "condo-timeline-phases.webp",
    "condo-security-upgrade-timeline-condo-resident-notice.webp": "condo-timeline-resident-notice.webp",
    "hdb-landed-condo-security-differences-landed-home-security-layout.webp": "property-types-landed-layout.webp",
    "home-security-system-cost-singapore-alarm-system-components-layout.webp": "home-cost-alarm-components.webp",
    "home-security-system-cost-singapore-home-security-budget-breakdown.webp": "home-cost-budget-breakdown.webp",
    "how-burglar-alarm-works-alarm-controller-panel.webp": "alarm-works-controller.webp",
    "how-card-access-works-card-access-controller-panel.webp": "card-access-controller.webp",
}

print("--- FILE RENAMES ---")
for old_name, new_name in renames.items():
    old_path = os.path.join(images_dir, old_name)
    if os.path.exists(old_path):
        new_path = os.path.join(images_dir, new_name)
        os.rename(old_path, new_path)
        print(f"RENAMED: {old_name} -> {new_name}")
    else:
        if os.path.exists(os.path.join(images_dir, new_name)):
            print(f"ALREADY RENAMED: {old_name} -> {new_name}")
        else:
            print(f"NOT FOUND: {old_name}")

print("\n--- HTML UPDATES ---")
html_updates = {
    "how-ip-cctv-works.html": [
        ("how-ip-cctv-works-poe-switch-installation.webp", "ip-cctv-poe-switch.webp"),
        ("how-ip-cctv-works-surveillance-hard-disk.webp", "ip-cctv-hard-disk.webp")
    ],
    "how-technology-makes-your-guarding-team-more-competitive.html": [
        ("securevision-sales-guarding-technology.webp", "guarding-tech-consultation.webp")
    ],
    "condo-security-upgrade-quotes.html": [
        ("condo-security-upgrade-quotes-condo-tender-specification.webp", "condo-quotes-spec-document.webp")
    ],
    "condo-security-upgrade-timeline.html": [
        ("condo-security-upgrade-timeline-condo-installation-phases.webp", "condo-timeline-phases.webp"),
        ("condo-security-upgrade-timeline-condo-resident-notice.webp", "condo-timeline-resident-notice.webp")
    ],
    "hdb-landed-condo-security-differences.html": [
        ("hdb-landed-condo-security-differences-landed-home-security-layout.webp", "property-types-landed-layout.webp")
    ],
    "home-security-system-cost-singapore.html": [
        ("home-security-system-cost-singapore-alarm-system-components-layout.webp", "home-cost-alarm-components.webp"),
        ("home-security-system-cost-singapore-home-security-budget-breakdown.webp", "home-cost-budget-breakdown.webp")
    ],
    "how-burglar-alarm-works.html": [
        ("how-burglar-alarm-works-alarm-controller-panel.webp", "alarm-works-controller.webp")
    ],
    "how-card-access-works.html": [
        ("how-card-access-works-card-access-controller-panel.webp", "card-access-controller.webp")
    ]
}

for html_file, changes in html_updates.items():
    filepath = os.path.join(insights_dir, html_file)
    if not os.path.exists(filepath):
        print(f"HTML NOT FOUND: {html_file}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    for old_img, new_img in changes:
        content = content.replace(old_img, new_img)
            
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"HTML UPDATED: {html_file}")
    else:
        print(f"HTML NO CHANGES: {html_file}")
