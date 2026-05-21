import os
from pathlib import Path

base_dir = Path(r"d:\Ler Wee Meng\Project-Web\SV-Build")
cctv_dir = base_dir / "images" / "resources" / "guides" / "cctv"
guides_dir = base_dir / "images" / "resources" / "guides"
resources_root = base_dir / "images" / "resources"
html_path = base_dir / "resources" / "guides" / "cctv-guide.html"

new_files = [
    "ai-analytics-demo.webp", "analogue-vs-ip.webp", "analytics-perimeter.webp",
    "burglar-alarm-high-end-boutique.webp", "burglar-alarm-project-bukit-timah.webp",
    "camera-anatomy.webp", "case-study-sunlove.webp", "cctv-legacy-analogue.webp",
    "cctv-resolution-comparison.webp", "comp-integration-v3.webp", "cost-distribution.webp",
    "dual-lens-thermal.webp", "edge-analytics.webp", "face-recognition-lobby.webp",
    "hd-analogue.webp", "hdd-surveillance.webp", "hybrid-upgrade.webp",
    "industrial-perimeter.webp", "industrial-workforce.webp", "ip-camera-tech.webp",
    "maintenance-audit.webp", "mobile-app-mockup.webp", "mobile-app.webp",
    "modern-ai.webp", "monitor-display.webp", "nvr-analytics.webp", "nvr-front.webp",
    "overview-main.webp", "planning-layout.webp", "poe-switch.webp", "project-factory.webp",
    "ptz-camera.webp", "resolution-ladder.webp", "retail-heat-map.webp", "server-vms.webp",
    "specialized-lowlight.webp", "starlight-comparison.webp", "system-flow.webp",
    "type-bullet.webp", "type-dome.webp", "type-turret.webp", "ups-unit.webp",
    "wireless-wifi.webp"
]

old_files = [
    "cctv-legacy-analogue.webp", "cctv-resolution-comparison.webp", "comp-integration-v3.webp",
    "resource-guide-burglar-alarm-high-end-boutique.webp", "resource-guide-burglar-alarm-project-bukit-timah.webp",
    "resource-guide-cctv-ai-analytics-demo.webp", "resource-guide-cctv-analogue-vs-ip.webp",
    "resource-guide-cctv-analytics-perimeter.webp", "resource-guide-cctv-camera-anatomy.webp",
    "resource-guide-cctv-case-study-sunlove.webp", "resource-guide-cctv-cost-distribution.webp",
    "resource-guide-cctv-dual-lens-thermal.webp", "resource-guide-cctv-edge-analytics.webp",
    "resource-guide-cctv-face-recognition-lobby.webp", "resource-guide-cctv-hd-analogue.webp",
    "resource-guide-cctv-hdd-surveillance.webp", "resource-guide-cctv-hybrid-upgrade.webp",
    "resource-guide-cctv-industrial-perimeter.webp", "resource-guide-cctv-industrial-workforce.webp",
    "resource-guide-cctv-ip-camera-tech.webp", "resource-guide-cctv-maintenance-audit.webp",
    "resource-guide-cctv-mobile-app-mockup.webp", "resource-guide-cctv-mobile-app.webp",
    "resource-guide-cctv-modern-ai.webp", "resource-guide-cctv-monitor-display.webp",
    "resource-guide-cctv-nvr-analytics.webp", "resource-guide-cctv-nvr-front.webp",
    "resource-guide-cctv-overview-main.webp", "resource-guide-cctv-planning-layout.webp",
    "resource-guide-cctv-poe-switch.webp", "resource-guide-cctv-project-factory.webp",
    "resource-guide-cctv-ptz-camera.webp", "resource-guide-cctv-resolution-ladder.webp",
    "resource-guide-cctv-retail-heat-map.webp", "resource-guide-cctv-server-vms.webp",
    "resource-guide-cctv-specialized-lowlight.webp", "resource-guide-cctv-starlight-comparison.webp",
    "resource-guide-cctv-system-flow.webp", "resource-guide-cctv-type-bullet.webp",
    "resource-guide-cctv-type-dome.webp", "resource-guide-cctv-type-turret.webp",
    "resource-guide-cctv-ups-unit.webp", "resource-guide-cctv-wireless-wifi.webp"
]

# CHECK 1
check1_exists = 0
check1_missing = []
for f in new_files:
    if (cctv_dir / f).exists():
        check1_exists += 1
    else:
        check1_missing.append(f)

# CHECK 2
check2_gone = 0
check2_still_exists = []
for f in old_files:
    if not (guides_dir / f).exists():
        check2_gone += 1
    else:
        check2_still_exists.append(f)

# CHECK 3
html_content = html_path.read_text(encoding='utf-8') if html_path.exists() else ""
check3_issues = []
for f in old_files:
    old_ref = f"/images/resources/guides/{f}"
    if old_ref in html_content:
        check3_issues.append(old_ref)

check3_status = "CLEAN" if not check3_issues else "ISSUES FOUND"

# CHECK 4
check4_files = []
for item in resources_root.iterdir():
    if item.is_file():
        check4_files.append(item.name)

# OUTPUT
print(f"CHECK 1: {check1_exists} of 43 files exist in cctv/ subfolder")
for m in check1_missing:
    print(f"  MISSING: {m}")

print(f"\nCHECK 2: {check2_gone} of 43 old files gone from guides root")
for s in check2_still_exists:
    print(f"  STILL EXISTS: {s}")

print(f"\nCHECK 3: cctv-guide.html references — {check3_status}")
for i in check3_issues:
    print(f"  Found old reference: {i}")

print(f"\nCHECK 4: Resources root files — list all found")
for f in sorted(check4_files):
    if f in ["resources-knowledge-base-singapore.webp", "resources-knowledge-base-singapore-mobile.webp"]:
        print(f"  {f}")
    else:
        print(f"  {f} (UNEXPECTED)")

# OVERALL
overall = "PASS"
needs_fixing = []
if check1_missing:
    needs_fixing.append("Missing files in cctv/")
if check2_still_exists:
    needs_fixing.append("Old files still exist in guides/")
if check3_issues:
    needs_fixing.append("Old references found in HTML")
if [f for f in check4_files if f not in ["resources-knowledge-base-singapore.webp", "resources-knowledge-base-singapore-mobile.webp"]]:
    needs_fixing.append("Unexpected files in resources root")

if needs_fixing:
    overall = "FAIL (" + ", ".join(needs_fixing) + ")"

print(f"\nOVERALL: {overall}")
