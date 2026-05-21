import os
import shutil
from pathlib import Path

base_dir = Path(r"d:\Ler Wee Meng\Project-Web\SV-Build")
img_guides_dir = base_dir / "images" / "resources" / "guides"
cctv_dir = img_guides_dir / "cctv"

cctv_dir.mkdir(parents=True, exist_ok=True)

renames = {
    "resource-guide-cctv-ai-analytics-demo.webp": "ai-analytics-demo.webp",
    "resource-guide-cctv-analogue-vs-ip.webp": "analogue-vs-ip.webp",
    "resource-guide-cctv-analytics-perimeter.webp": "analytics-perimeter.webp",
    "resource-guide-cctv-camera-anatomy.webp": "camera-anatomy.webp",
    "resource-guide-cctv-case-study-sunlove.webp": "case-study-sunlove.webp",
    "resource-guide-cctv-cost-distribution.webp": "cost-distribution.webp",
    "resource-guide-cctv-dual-lens-thermal.webp": "dual-lens-thermal.webp",
    "resource-guide-cctv-edge-analytics.webp": "edge-analytics.webp",
    "resource-guide-cctv-face-recognition-lobby.webp": "face-recognition-lobby.webp",
    "resource-guide-cctv-hd-analogue.webp": "hd-analogue.webp",
    "resource-guide-cctv-hdd-surveillance.webp": "hdd-surveillance.webp",
    "resource-guide-cctv-hybrid-upgrade.webp": "hybrid-upgrade.webp",
    "resource-guide-cctv-industrial-perimeter.webp": "industrial-perimeter.webp",
    "resource-guide-cctv-industrial-workforce.webp": "industrial-workforce.webp",
    "resource-guide-cctv-ip-camera-tech.webp": "ip-camera-tech.webp",
    "resource-guide-cctv-maintenance-audit.webp": "maintenance-audit.webp",
    "resource-guide-cctv-mobile-app-mockup.webp": "mobile-app-mockup.webp",
    "resource-guide-cctv-mobile-app.webp": "mobile-app.webp",
    "resource-guide-cctv-modern-ai.webp": "modern-ai.webp",
    "resource-guide-cctv-monitor-display.webp": "monitor-display.webp",
    "resource-guide-cctv-nvr-analytics.webp": "nvr-analytics.webp",
    "resource-guide-cctv-nvr-front.webp": "nvr-front.webp",
    "resource-guide-cctv-overview-main.webp": "overview-main.webp",
    "resource-guide-cctv-planning-layout.webp": "planning-layout.webp",
    "resource-guide-cctv-poe-switch.webp": "poe-switch.webp",
    "resource-guide-cctv-project-factory.webp": "project-factory.webp",
    "resource-guide-cctv-ptz-camera.webp": "ptz-camera.webp",
    "resource-guide-cctv-resolution-ladder.webp": "resolution-ladder.webp",
    "resource-guide-cctv-retail-heat-map.webp": "retail-heat-map.webp",
    "resource-guide-cctv-server-vms.webp": "server-vms.webp",
    "resource-guide-cctv-specialized-lowlight.webp": "specialized-lowlight.webp",
    "resource-guide-cctv-starlight-comparison.webp": "starlight-comparison.webp",
    "resource-guide-cctv-system-flow.webp": "system-flow.webp",
    "resource-guide-cctv-type-bullet.webp": "type-bullet.webp",
    "resource-guide-cctv-type-dome.webp": "type-dome.webp",
    "resource-guide-cctv-type-turret.webp": "type-turret.webp",
    "resource-guide-cctv-ups-unit.webp": "ups-unit.webp",
    "resource-guide-cctv-wireless-wifi.webp": "wireless-wifi.webp",
    "resource-guide-burglar-alarm-high-end-boutique.webp": "burglar-alarm-high-end-boutique.webp",
    "resource-guide-burglar-alarm-project-bukit-timah.webp": "burglar-alarm-project-bukit-timah.webp",
    "cctv-legacy-analogue.webp": "cctv-legacy-analogue.webp",
    "cctv-resolution-comparison.webp": "cctv-resolution-comparison.webp",
    "comp-integration-v3.webp": "comp-integration-v3.webp"
}

# PART 1: Move and rename files
moved = 0
for old_name, new_name in renames.items():
    src_file = img_guides_dir / old_name
    dst_file = cctv_dir / new_name
    if src_file.exists():
        shutil.move(str(src_file), str(dst_file))
        print(f"Moved {old_name} -> cctv/{new_name}")
        moved += 1
    else:
        print(f"File not found, skipped: {old_name}")

print(f"\nTotal files moved: {moved}")

# PART 2: Update HTML references
html_path = base_dir / "resources" / "guides" / "cctv-guide.html"
if html_path.exists():
    content = html_path.read_text(encoding='utf-8')
    replacements = 0
    for old_name, new_name in renames.items():
        old_ref = f"/images/resources/guides/{old_name}"
        new_ref = f"/images/resources/guides/cctv/{new_name}"
        if old_ref in content:
            content = content.replace(old_ref, new_ref)
            replacements += 1
    
    html_path.write_text(content, encoding='utf-8')
    print(f"Updated HTML file: {html_path.name} with {replacements} replacements.")

# ALSO DELETE
delete_file = base_dir / "images" / "resources" / "resources-knowledge-base-singapore-rel.webp"
if delete_file.exists():
    delete_file.unlink()
    print(f"Deleted {delete_file.name}")
else:
    print(f"File to delete not found: {delete_file.name}")
