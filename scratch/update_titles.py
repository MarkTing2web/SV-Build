import os
import re

target_dir = r"c:\Projects\SV-Build\insights"

updates = {
    "10-tips-securing-your-premises.html": "10 Tips for Securing Your Home or Office in Singapore",
    "analogue-to-ip-migration.html": "How Do I Migrate from Analogue to IP CCTV Without Full Replacement?",
    "architect-id-guide-security.html": "The Architect and ID's Guide to Security Systems in Singapore",
    "burglar-alarm-detectors-sensors.html": "Know Your Burglar Alarm Detectors and Sensors",
    "choose-intercom-for-home.html": "How to Choose an Intercom for Your Home",
    "compare-security-integrators.html": "How to Compare Two Security Integrators Fairly",
    "condo-security-upgrade-proposal.html": "What Does a Security Upgrade Proposal to Residents Look Like?",
    "condo-security-upgrade-quotes.html": "How Do I Get Quotes for an AGM-Approved Security Upgrade?",
    "condo-security-upgrade-timeline.html": "Realistic Timeline and Disruption Plan for Condo Security Upgrade",
    "hdb-landed-condo-security-differences.html": "HDB, Landed, or Condo — How Security Requirements Differ",
    "how-burglar-alarm-works.html": "How Your Burglar Alarm Actually Works",
    "how-card-access-works.html": "How Card Access Control Actually Works",
    "how-intercom-systems-work.html": "How Intercom Systems Work",
    "how-ip-cctv-works.html": "How an IP CCTV Network Actually Works",
    "how-to-choose-auto-gate-motor.html": "How to Choose an Auto Gate Motor for Your Home",
    "using-your-burglar-alarm.html": "How to Use Your Burglar Alarm Correctly"
}

results = []

for filename, new_title in updates.items():
    filepath = os.path.join(target_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = re.sub(
            r'<h1 class="insights-header-title">.*?</h1>',
            f'<h1 class="insights-header-title">{new_title}</h1>',
            content,
            flags=re.DOTALL
        )
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            results.append(f"Updated: {filename} -> {new_title}")
        else:
            if f'<h1 class="insights-header-title">{new_title}</h1>' in content:
                results.append(f"Already set: {filename} -> {new_title}")
            else:
                results.append(f"FAILED to update: {filename}")
    else:
        results.append(f"File not found: {filename}")

for r in results:
    print(r)
