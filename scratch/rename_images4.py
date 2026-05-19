import os

repo_root = r"c:\Projects\SV-Build"
images_dir = os.path.join(repo_root, "images", "insights")
insights_dir = os.path.join(repo_root, "insights")

renames = {
    "insight-wifi-remote-control-auto-gate-YET-Tuya-mobile-app-receiver-for-auto-gate.webp": "wifi-gate-tuya-receiver.webp",
    "upgrade-condo-intercom-condo-intercom-akuvox-r29.webp": "condo-intercom-akuvox-r29.webp",
    "upgrade-existing-security-system-nvr-channel-assessment.webp": "upgrade-existing-nvr-assessment.webp",
    "upgrade-or-repair-timeline.webp": "upgrade-repair-timeline.webp",
    "upgrade-or-repair-hybrid.webp": "upgrade-repair-hybrid.webp",
    "why-mechanical-locks-not-enough-lock-bumping-diagram.webp": "mechanical-lock-bumping.webp",
    "digital-door-lock-singapore.webp": "digital-lock-singapore.webp"
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
    "wifi-remote-control-auto-gate.html": [
        ("insight-wifi-remote-control-auto-gate-YET-Tuya-mobile-app-receiver-for-auto-gate.webp", "wifi-gate-tuya-receiver.webp")
    ],
    "upgrade-condo-intercom.html": [
        ("upgrade-condo-intercom-condo-intercom-akuvox-r29.webp", "condo-intercom-akuvox-r29.webp")
    ],
    "upgrade-existing-security-system.html": [
        ("upgrade-existing-security-system-nvr-channel-assessment.webp", "upgrade-existing-nvr-assessment.webp")
    ],
    "upgrade-or-repair.html": [
        ("upgrade-or-repair-timeline.webp", "upgrade-repair-timeline.webp"),
        ("upgrade-or-repair-hybrid.webp", "upgrade-repair-hybrid.webp")
    ],
    "why-mechanical-locks-not-enough.html": [
        ("why-mechanical-locks-not-enough-lock-bumping-diagram.webp", "mechanical-lock-bumping.webp"),
        ("digital-door-lock-singapore.webp", "digital-lock-singapore.webp")
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
