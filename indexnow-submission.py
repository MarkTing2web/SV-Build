"""
IndexNow Submission Script — Securevision
Submits all key pages to Bing/IndexNow in one call.
Run from anywhere: python3 indexnow-submission.py
"""

import urllib.request
import json

KEY = "88e8565336c4438985c75bd76ef85b5b"
HOST = "securevision.com.sg"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

# All key pages to submit
URLS = [
    # Homepage
    "https://securevision.com.sg/",
    "https://securevision.com.sg/index.html",

    # Solutions — Condominiums
    "https://securevision.com.sg/solutions/condominiums/condominium-security-systems.html",
    "https://securevision.com.sg/solutions/condominiums/managing-agents.html",
    "https://securevision.com.sg/solutions/condominiums/mcst.html",

    # Solutions — Residential
    "https://securevision.com.sg/solutions/residential/landed-home-security-systems.html",
    "https://securevision.com.sg/solutions/residential/home-upgrade.html",

    # Solutions — Commercial
    "https://securevision.com.sg/solutions/commercial/office.html",
    "https://securevision.com.sg/solutions/commercial/hotel.html",

    # Solutions — Industrial / Institutional
    "https://securevision.com.sg/solutions/industrial/industrial-security-systems.html",
    "https://securevision.com.sg/solutions/institutions/institutions-security-systems.html",
    "https://securevision.com.sg/solutions/healthcare/healthcare-security-systems.html",
    "https://securevision.com.sg/solutions/managed-living/managed-living-security-systems.html",
    "https://securevision.com.sg/solutions/managed-living/dormitories.html",
    "https://securevision.com.sg/solutions/reduce-guard-manpower.html",
    "https://securevision.com.sg/solutions/automate-vehicle-access.html",
    "https://securevision.com.sg/solutions/upgrade-intercom-system.html",
    "https://securevision.com.sg/solutions/improve-cctv-visibility.html",

    # Contact & core pages
    "https://securevision.com.sg/contact.html",
    "https://securevision.com.sg/about.html",

    # Insights — all 44 articles
    "https://securevision.com.sg/insights/managing-agents-guide-estate-security-systems.html",
    "https://securevision.com.sg/insights/mcst-legal-obligations-security.html",
    "https://securevision.com.sg/insights/condo-security-upgrade-proposals.html",
    "https://securevision.com.sg/insights/condo-security-upgrade-timeline.html",
    "https://securevision.com.sg/insights/lpr-vs-rfid-condo.html",
    "https://securevision.com.sg/insights/condo-intercom-upgrade.html",
    "https://securevision.com.sg/insights/mcst-security-tender.html",
    "https://securevision.com.sg/insights/compare-security-integrators.html",
    "https://securevision.com.sg/insights/managing-multiple-estates-with-vesta.html",
    "https://securevision.com.sg/insights/guarding-technology-singapore.html",
    "https://securevision.com.sg/insights/cctv-pdpa-compliance.html",
    "https://securevision.com.sg/insights/architect-security-guide.html",
    "https://securevision.com.sg/insights/intercom-system-evolution-singapore.html",
    "https://securevision.com.sg/insights/access-control-multi-door.html",
    "https://securevision.com.sg/insights/access-control-upgrade-drivers-singapore.html",
    "https://securevision.com.sg/insights/is-my-security-system-still-working.html",
    "https://securevision.com.sg/insights/installer-leaves.html",
    "https://securevision.com.sg/insights/maintenance-contract.html",
    "https://securevision.com.sg/insights/alarm-upgrade-or-replace.html",
    "https://securevision.com.sg/insights/home-security-system-cost-singapore.html",
    "https://securevision.com.sg/insights/hdb-landed-condo-security-differences.html",
    "https://securevision.com.sg/insights/break-in-nearby-security-review.html",
    "https://securevision.com.sg/insights/10-things-security-assessment.html",
    "https://securevision.com.sg/insights/installer-licensed-singapore.html",
    "https://securevision.com.sg/insights/agm-security-upgrade-approval.html",
    "https://securevision.com.sg/insights/mechanical-locks-not-enough.html",
    "https://securevision.com.sg/insights/choose-intercom-for-home.html",
    "https://securevision.com.sg/insights/cctv-system-components.html",
    "https://securevision.com.sg/insights/how-to-choose-cctv.html",
    "https://securevision.com.sg/insights/cctv-ai-upgrade.html",
    "https://securevision.com.sg/insights/cctv-cable-upgrade.html",
    "https://securevision.com.sg/insights/rack-mount-vs-desktop-nvr.html",
    "https://securevision.com.sg/insights/cctv-retail-analytics.html",
    "https://securevision.com.sg/insights/cctv-vs-alarm.html",
    "https://securevision.com.sg/insights/how-alarm-works.html",
    "https://securevision.com.sg/insights/false-alarm-causes.html",
    "https://securevision.com.sg/insights/false-alarms.html",
    "https://securevision.com.sg/insights/burglar-alarm-detectors-sensors.html",
    "https://securevision.com.sg/insights/modern-detectors.html",
    "https://securevision.com.sg/insights/maintain-burglar-alarm.html",
    "https://securevision.com.sg/insights/alarm-self-monitor-vs-cms.html",
    "https://securevision.com.sg/insights/auto-gate-motor.html",
    "https://securevision.com.sg/insights/gate-remote-smartphone.html",
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": URLS
}

data = json.dumps(payload).encode("utf-8")

req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=data,
    headers={
        "Content-Type": "application/json; charset=utf-8"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as response:
        print(f"✅ Submitted {len(URLS)} URLs")
        print(f"   Status: {response.status}")
except urllib.error.HTTPError as e:
    print(f"❌ HTTP Error: {e.code} — {e.reason}")
except Exception as e:
    print(f"❌ Error: {e}")
