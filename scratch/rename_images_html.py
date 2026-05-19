import os
import re

repo_root = r"c:\Projects\SV-Build"
images_dir = os.path.join(repo_root, "images", "insights")
insights_dir = os.path.join(repo_root, "insights")

renames = {
    "10-tips-securing-your-premises-10-tips-security-perimeter-audit.webp": "10-tips-perimeter-audit.webp",
    "ai-analytics-hikvision-camera.webp": "ai-hikvision-acusense-camera.webp",
    "ai-analytics-hikvision-edgebox.webp": "ai-hikvision-edgebox.webp",
    "analogue-to-ip-migration-hdcvi.webp": "analogue-ip-hdcvi-connector.webp",
    "analogue-to-ip-migration-hybrid.webp": "analogue-ip-hybrid-nvr.webp",
    "analogue-to-ip-migration-phase.webp": "analogue-ip-site-plan.webp",
    "architect-id-guide-security-architect-id-engineer-discussion.webp": "architect-guide-engineer-discussion.webp",
    "architect-id-guide-security-architect-id-conduit-check.webp": "architect-guide-conduit-check.webp",
    "architect-id-guide-security-architect-id-coordination-meeting.webp": "architect-guide-coordination.webp",
    "architect-id-guide-security-architect-id-regulatory-compliance.webp": "DELETED",
    "architect-id-guide-security-architect-id-tender-review.webp": "DELETED",
    "burglar-alarm-design-burglar-alarm-pir-detector.webp": "burglar-alarm-design-pir.webp",
    "burglar-alarm-design-burglar-alarm-ajax-panel.webp": "burglar-alarm-design-ajax-panel.webp",
    "burglar-alarm-detectors-sensors-door-window-contact-sensor.webp": "alarm-detectors-door-contact.webp",
    "burglar-alarm-detectors-sensors-glass-break-sensor.webp": "alarm-detectors-glass-break.webp",
    "intercom-door-station.webp": "intercom-home-door-station.webp",
    "compare-security-integrators-agm-document.webp": "compare-integrators-licence-check.webp",
    "compare-security-integrators-mcst-legal-meeting.webp": "compare-integrators-site-meeting.webp",
    "condo-security-upgrade-proposal-condo-upgrade-timeline-chart.webp": "condo-proposal-timeline-chart.webp",
    "condo-security-upgrade-proposal-cover.webp": "condo-proposal-council-meeting.webp",
}

print("--- FILE RENAMES ---")
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
        # Check if already renamed/deleted
        if new_name != "DELETED" and os.path.exists(os.path.join(images_dir, new_name)):
            print(f"ALREADY RENAMED: {old_name} -> {new_name}")
        elif new_name == "DELETED":
            print(f"NOT FOUND (prob already deleted): {old_name}")
        else:
            print(f"NOT FOUND: {old_name}")

print("\n--- HTML UPDATES ---")

html_updates = {
    "10-tips-securing-your-premises.html": {
        "10-tips-securing-your-premises-10-tips-security-perimeter-audit.webp": "10-tips-perimeter-audit.webp"
    },
    "ai-analytics-hikvision.html": {
        "ai-analytics-hikvision-camera.webp": "ai-hikvision-acusense-camera.webp",
        "ai-analytics-hikvision-edgebox.webp": "ai-hikvision-edgebox.webp"
    },
    "analogue-to-ip-migration.html": {
        "analogue-to-ip-migration-hdcvi.webp": "analogue-ip-hdcvi-connector.webp",
        "analogue-to-ip-migration-hybrid.webp": "analogue-ip-hybrid-nvr.webp",
        "analogue-to-ip-migration-phase.webp": "analogue-ip-site-plan.webp"
    },
    "architect-id-guide-security.html": {
        "architect-id-guide-security-architect-id-engineer-discussion.webp": "architect-guide-engineer-discussion.webp",
        "architect-id-guide-security-architect-id-conduit-check.webp": "architect-guide-conduit-check.webp",
        "architect-id-guide-security-architect-id-coordination-meeting.webp": "architect-guide-coordination.webp",
        "architect-id-guide-security-architect-id-regulatory-compliance.webp": "REMOVE_BLOCK",
        "architect-id-guide-security-architect-id-tender-review.webp": "REMOVE_BLOCK"
    },
    "burglar-alarm-design.html": {
        "burglar-alarm-design-burglar-alarm-pir-detector.webp": "burglar-alarm-design-pir.webp",
        "burglar-alarm-design-burglar-alarm-ajax-panel.webp": "burglar-alarm-design-ajax-panel.webp"
    },
    "burglar-alarm-detectors-sensors.html": {
        "burglar-alarm-detectors-sensors-door-window-contact-sensor.webp": "alarm-detectors-door-contact.webp",
        "burglar-alarm-detectors-sensors-glass-break-sensor.webp": "alarm-detectors-glass-break.webp"
    },
    "choose-intercom-for-home.html": {
        "intercom-door-station.webp": "intercom-home-door-station.webp"
    },
    "compare-security-integrators.html": {
        "compare-security-integrators-agm-document.webp": "compare-integrators-licence-check.webp",
        "compare-security-integrators-mcst-legal-meeting.webp": "compare-integrators-site-meeting.webp"
    },
    "condo-security-upgrade-proposal.html": {
        "condo-security-upgrade-proposal-condo-upgrade-timeline-chart.webp": "condo-proposal-timeline-chart.webp",
        "condo-security-upgrade-proposal-cover.webp": "condo-proposal-council-meeting.webp"
    }
}

for html_file, changes in html_updates.items():
    filepath = os.path.join(insights_dir, html_file)
    if not os.path.exists(filepath):
        print(f"HTML NOT FOUND: {html_file}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    for old_img, new_img in changes.items():
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
