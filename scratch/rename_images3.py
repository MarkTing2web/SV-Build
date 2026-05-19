import os
import re

repo_root = r"c:\Projects\SV-Build"
images_dir = os.path.join(repo_root, "images", "insights")
insights_dir = os.path.join(repo_root, "insights")

renames = {
    "security-system-refresh-upper-thomson-news-clipping.webp": "security-refresh-news-clipping.webp",
    "security-system-refresh-upper-thomson-backyard-camera.webp": "security-refresh-backyard-camera.webp",
    "security-upgrade-condo-agm-agm-preparation.webp": "condo-agm-preparation.webp",
    "security-upgrade-condo-agm-agm-discussion.webp": "condo-agm-discussion.webp",
    "how-to-choose-auto-gate-motor-auto-gate-concealed-motor.webp": "auto-gate-concealed-motor.webp",
    "how-to-choose-cctv-cctv-night-vision-comparison.webp": "cctv-choose-night-vision.webp",
    "how-to-choose-cctv-cctv-hd-analogue-toggle.webp": "cctv-choose-hd-analogue.webp",
    "how-to-choose-cctv-cctv-network-ip.webp": "cctv-choose-network-ip.webp",
    "how-to-choose-cctv-cover.webp": "cctv-choose-cover.webp",
    "how-to-choose-multi-door-access-multi-door-access-controller.webp": "multi-door-access-controller.webp",
    "managing-agents-guide-estate-security-systems-managing-agents-guide-maintenance.webp": "ma-guide-maintenance.webp",
    "managing-agents-guide-estate-security-systems-managing-agents-guide-sla.webp": "ma-guide-sla.webp",
    "managing-agents-guide-estate-security-systems-managing-agents-guide-night.webp": "ma-guide-night-response.webp",
    "managing-multiple-estates-with-vesta-vesta-guard-house-automation.webp": "vesta-guardhouse.webp",
    "managing-multiple-estates-with-vesta-vesta-three-views-split.webp": "vesta-three-views.webp",
    "managing-multiple-estates-with-vesta-vesta-training-session.webp": "vesta-training.webp",
    "mcst-legal-obligations-security-mcst-legal-pdpa.webp": "mcst-legal-pdpa.webp",
    "mcst-legal-obligations-security-mcst-legal-bmsma.webp": "mcst-legal-bmsma.webp",
    "mcst-legal-obligations-security-mcst-legal-fire.webp": "mcst-legal-fire-code.webp",
    "rackmount-nvr-nvr-on-desk-vs-rack.webp": "rackmount-nvr-comparison.webp",
    "is-my-security-system-still-working-nvr-playback-check.webp": "system-check-nvr-playback.webp",
    "alarm-walk-test-diagram.webp": "alarm-maintain-walk-test.webp",
    "reduce-false-alarms-false-alarm-pir-sunlight.webp": "false-alarm-sunlight-pir.webp",
    "compare-security-integrators-agm-document.webp": "DELETED",
    "compare-security-integrators-mcst-legal-meeting.webp": "DELETED",
    "managing-agents-guide-estate-security-systems-managing-agents-guide-vesta.webp": "DELETED",
    "managing-multiple-estates-with-vesta-vesta-portfolio-oversight.webp": "DELETED"
}

print("--- FILE RENAMES/DELETIONS ---")
for old_name, new_name in renames.items():
    old_path = os.path.join(images_dir, old_name)
    if os.path.exists(old_path):
        if new_name == "DELETED":
            os.remove(old_path)
            print(f"DELETED: {old_name}")
        else:
            new_path = os.path.join(images_dir, new_name)
            os.rename(old_path, new_path)
            print(f"RENAMED: {old_name} -> {new_name}")
    else:
        if new_name != "DELETED" and os.path.exists(os.path.join(images_dir, new_name)):
            print(f"ALREADY RENAMED: {old_name} -> {new_name}")
        else:
            print(f"NOT FOUND: {old_name}")

print("\n--- HTML UPDATES ---")
html_updates = {
    "security-system-refresh.html": [
        ("security-system-refresh-upper-thomson-news-clipping.webp", "security-refresh-news-clipping.webp"),
        ("security-system-refresh-upper-thomson-backyard-camera.webp", "security-refresh-backyard-camera.webp")
    ],
    "security-upgrade-condo-agm.html": [
        ("compare-security-integrators-agm-document.webp", "condo-agm-proposal-document.webp"),
        ("security-upgrade-condo-agm-agm-preparation.webp", "condo-agm-preparation.webp"),
        ("security-upgrade-condo-agm-agm-discussion.webp", "condo-agm-discussion.webp")
    ],
    "how-to-choose-auto-gate-motor.html": [
        ("how-to-choose-auto-gate-motor-auto-gate-concealed-motor.webp", "auto-gate-concealed-motor.webp")
    ],
    "how-to-choose-cctv.html": [
        ("how-to-choose-cctv-cctv-night-vision-comparison.webp", "cctv-choose-night-vision.webp"),
        ("how-to-choose-cctv-cctv-hd-analogue-toggle.webp", "cctv-choose-hd-analogue.webp"),
        ("how-to-choose-cctv-cctv-network-ip.webp", "cctv-choose-network-ip.webp"),
        ("how-to-choose-cctv-cover.webp", "REMOVE_BLOCK")
    ],
    "how-to-choose-multi-door-access.html": [
        ("how-to-choose-multi-door-access-multi-door-access-controller.webp", "multi-door-access-controller.webp")
    ],
    "managing-agents-guide-estate-security-systems.html": [
        ("managing-agents-guide-estate-security-systems-managing-agents-guide-maintenance.webp", "ma-guide-maintenance.webp"),
        ("managing-agents-guide-estate-security-systems-managing-agents-guide-sla.webp", "ma-guide-sla.webp"),
        ("managing-agents-guide-estate-security-systems-managing-agents-guide-night.webp", "ma-guide-night-response.webp"),
        ("managing-agents-guide-vesta.webp", "REMOVE_BLOCK")
    ],
    "managing-multiple-estates-with-vesta.html": [
        ("managing-multiple-estates-with-vesta-vesta-guard-house-automation.webp", "vesta-guardhouse.webp"),
        ("managing-multiple-estates-with-vesta-vesta-three-views-split.webp", "vesta-three-views.webp"),
        ("managing-multiple-estates-with-vesta-vesta-training-session.webp", "vesta-training.webp"),
        ("vesta-portfolio-oversight.webp", "REMOVE_BLOCK")
    ],
    "mcst-legal-obligations-security.html": [
        ("compare-security-integrators-mcst-legal-meeting.webp", "mcst-legal-committee-meeting.webp"),
        ("mcst-legal-obligations-security-mcst-legal-pdpa.webp", "mcst-legal-pdpa.webp"),
        ("mcst-legal-obligations-security-mcst-legal-bmsma.webp", "mcst-legal-bmsma.webp"),
        ("mcst-legal-obligations-security-mcst-legal-fire.webp", "mcst-legal-fire-code.webp")
    ],
    "rackmount-nvr.html": [
        ("rackmount-nvr-nvr-on-desk-vs-rack.webp", "rackmount-nvr-comparison.webp")
    ],
    "is-my-security-system-still-working.html": [
        ("is-my-security-system-still-working-nvr-playback-check.webp", "system-check-nvr-playback.webp")
    ],
    "maintain-burglar-alarm.html": [
        ("alarm-walk-test-diagram.webp", "alarm-maintain-walk-test.webp")
    ],
    "reduce-false-alarms.html": [
        ("reduce-false-alarms-false-alarm-pir-sunlight.webp", "false-alarm-sunlight-pir.webp")
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
        if new_img == "REMOVE_BLOCK":
            pattern_div = r'[ \t]*<div[^>]*class="[^"]*article-image-box[^"]*"[^>]*>\s*<img[^>]*'+re.escape(old_img)+r'[^>]*>(?:\s*<p[^>]*>.*?</p>)?\s*</div>[ \t]*\n?'
            new_content = re.sub(pattern_div, '', content, flags=re.DOTALL)
            if new_content == content:
                pattern_img = r'[ \t]*<img[^>]*'+re.escape(old_img)+r'[^>]*>[ \t]*\n?'
                new_content = re.sub(pattern_img, '', content, flags=re.DOTALL)
            content = new_content
        else:
            content = content.replace(old_img, new_img)
            
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"HTML UPDATED: {html_file}")
    else:
        print(f"HTML NO CHANGES: {html_file}")
