import os
from bs4 import BeautifulSoup

INSIGHTS_DIR = r"C:\Projects\SV-Build\insights"

trim_files = [
    "why-security-needs-managed-network.html",
    "managing-agents-guide-estate-security-systems.html",
    "how-ip-cctv-works.html",
    "how-burglar-alarm-works.html",
    "security-upgrade-condo-agm.html",
    "security-system-refresh.html",
    "analogue-to-ip-migration.html",
    "after-security-installation-support.html",
    "upgrade-condo-intercom.html",
    "standalone-door-access.html",
    "how-to-choose-auto-gate-motor.html",
    "how-technology-makes-your-guarding-team-more-competitive.html",
    "upgrade-existing-security-system.html",
    "wifi-remote-control-auto-gate.html",
    "managing-multiple-estates-with-vesta.html"
]

for filename in trim_files:
    fpath = os.path.join(INSIGHTS_DIR, filename)
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        desc = soup.find("meta", {"name": "description"})
        if not desc:
            desc = soup.find("meta", {"name": "Description"})
        if desc:
            content = desc.get("content", "")
            print(f"--- {filename} ({len(content)} chars) ---")
            print(content)
            print()
