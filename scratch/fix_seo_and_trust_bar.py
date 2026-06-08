import os
import re
from bs4 import BeautifulSoup

INSIGHTS_DIR = r"C:\Projects\SV-Build\insights"

TITLE_UPDATES = {
    "10-tips-securing-your-premises.html": "10 Tips for Securing Your Business Premises in Singapore",
    "after-security-installation-support.html": "Security System Support and Warranty in Singapore",
    "ai-analytics-hikvision.html": "AI Video Analytics with Hikvision: What It Does in Singapore",
    "analogue-to-ip-migration.html": "How to Migrate from Analogue to IP CCTV in Singapore",
    "architect-id-guide-security.html": "Security Guide for Architects and ID Firms in Singapore",
    "burglar-alarm-design.html": "Burglar Alarm System Design for Singapore Properties",
    "burglar-alarm-detectors-sensors.html": "Burglar Alarm Detectors and Sensors: A Guide for Singapore",
    "choose-intercom-for-home.html": "Choosing the Right Intercom System for Your Home in Singapore",
    "compare-security-integrators.html": "How to Compare Security System Integrators in Singapore",
    "condo-security-upgrade-proposal.html": "Condo Security Upgrade Proposals in Singapore Explained",
    "condo-security-upgrade-quotes.html": "Getting Condo Security Upgrade Quotes in Singapore",
    "condo-security-upgrade-timeline.html": "Condo Security Upgrade Timeline: What to Expect in Singapore",
    "hdb-landed-condo-security-differences.html": "HDB, Landed and Condo Security Differences in Singapore",
    "home-security-system-cost-singapore.html": "How Much Does a Home Security System Cost in Singapore?",
    "how-burglar-alarm-works.html": "How Burglar Alarm Systems Work: A Guide for Singapore Homes",
    "how-card-access-works.html": "How Card Access Control Works in Singapore Properties",
    "how-intercom-systems-work.html": "How Intercom Systems Work: A Guide for Singapore Properties",
    "how-ip-cctv-works.html": "How IP CCTV Works: A Practical Guide for Singapore Properties",
    "how-technology-makes-your-guarding-team-more-competitive.html": "How Security Technology Strengthens Guarding in Singapore",
    "how-to-choose-auto-gate-motor.html": "How to Choose an Auto Gate Motor for Singapore Homes",
    "how-to-choose-cctv.html": "Choosing a CCTV System for Your Singapore Property",
    "how-to-choose-multi-door-access.html": "How to Choose a Multi-Door Access Control System in Singapore",
    "is-my-security-system-still-working.html": "Is Your Security System Still Working? A Singapore Guide",
    "maintain-burglar-alarm.html": "How to Maintain Your Burglar Alarm System in Singapore",
    "maintenance-contract.html": "Security System Maintenance Contracts in Singapore Explained",
    "managing-agents-guide-estate-security-systems.html": "Managing Agents: Guide to Estate Security in Singapore",
    "managing-multiple-estates-with-vesta.html": "Multi-Estate Security Management in Singapore with Vesta",
    "mcst-legal-obligations-security.html": "MCST Legal Obligations for Estate Security in Singapore",
    "rackmount-nvr.html": "Rackmount NVR Systems for IP CCTV Installations in Singapore",
    "reduce-false-alarms.html": "How to Reduce False Burglar Alarm Activations in Singapore",
    "security-system-refresh.html": "When and How to Refresh Your Security System in Singapore",
    "security-upgrade-condo-agm.html": "Condo Security Upgrades: Getting AGM Approval in Singapore",
    "standalone-door-access.html": "Standalone Door Access Control: When to Use It in Singapore",
    "upgrade-condo-intercom.html": "How to Upgrade Your Condo Intercom System in Singapore",
    "upgrade-existing-security-system.html": "How to Upgrade an Existing Security System in Singapore",
    "upgrade-or-repair.html": "Security System: Should You Upgrade or Repair in Singapore?",
    "using-your-burglar-alarm.html": "Using Your Burglar Alarm System Correctly in Singapore",
    "why-mechanical-locks-not-enough.html": "Why Mechanical Locks Are Not Enough for Security in Singapore",
    "why-security-needs-managed-network.html": "Why Security Systems Need a Managed Network in Singapore",
    "wifi-remote-control-auto-gate.html": "Wi-Fi Remote Control for Auto Gates: A Singapore Guide"
}

DESC_UPDATES = {
    "why-security-needs-managed-network.html": "Most security system failures are not camera or alarm faults — they are network faults. Wee Meng explains VLANs, managed switches, remote management,",
    "managing-agents-guide-estate-security-systems.html": "Engineering safety and efficiency for managing multiple Singaporean estates. A comprehensive guide for Managing Agents on unified platforms, maintenance",
    "security-upgrade-condo-agm.html": "A comprehensive guide for MCST Committee Members on how to present a security upgrade at an AGM. Learn how to document failures, handle cost objections,",
    "analogue-to-ip-migration.html": "A practical engineering guide to transitioning your Singapore property from analogue CCTV to IP without tearing out your cable infrastructure",
    "after-security-installation-support.html": "What follows a home security installation? Understand walk-tests, warranties, maintenance plans, and how to contact support.",
    "standalone-door-access.html": "A single door access system looks like a simple purchase. It is not. Learn how to choose a standalone reader that is easy to administer",
    "how-technology-makes-your-guarding-team-more-competitive.html": "PWM wage floors are rising and recruitment is harder. The guarding companies winning Singapore estate contracts are not adding headcount",
    "upgrade-existing-security-system.html": "Can you reuse existing cameras or alarm panels? Learn about ONVIF compatibility, channel limits, and when it makes sense to upgrade parts",
    "managing-multiple-estates-with-vesta.html": "Learn how the VESTA operational platform connects residents, management, and security infrastructure to streamline estate operations"
}

FLAGGED_FILES = [
    "how-ip-cctv-works.html",
    "how-burglar-alarm-works.html",
    "security-system-refresh.html",
    "upgrade-condo-intercom.html",
    "how-to-choose-auto-gate-motor.html",
    "wifi-remote-control-auto-gate.html"
]

def apply_updates():
    # Title updates
    for filename, new_title in TITLE_UPDATES.items():
        fpath = os.path.join(INSIGHTS_DIR, filename)
        if not os.path.exists(fpath):
            print(f"Skipping {filename}, file not found.")
            continue
            
        with open(fpath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            
        title_tag = soup.find("title")
        if title_tag:
            title_tag.string = new_title
        og_title = soup.find("meta", {"property": "og:title"})
        if og_title:
            og_title["content"] = new_title
            
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
    # Description updates
    for filename, new_desc in DESC_UPDATES.items():
        fpath = os.path.join(INSIGHTS_DIR, filename)
        if not os.path.exists(fpath):
            continue
            
        with open(fpath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            
        desc_tag = soup.find("meta", {"name": "description"})
        if not desc_tag:
            desc_tag = soup.find("meta", {"name": "Description"})
        if desc_tag:
            desc_tag["content"] = new_desc
            
        og_desc = soup.find("meta", {"property": "og:description"})
        if og_desc:
            og_desc["content"] = new_desc
            
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
    print(f"Applied titles to 40 files, trimmed descriptions for 9 files. Flagged {len(FLAGGED_FILES)} files.")

def fix_index_trust_bar():
    fpath = os.path.join(INSIGHTS_DIR, "index.html")
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    trust_bar = soup.find("div", class_="trust-bar-inner")
    if trust_bar:
        # Re-build carefully.
        # Find the text "2000+ Sites Protected" or similar.
        for el in trust_bar.contents:
            if isinstance(el, str) and "Sites Protected" in el:
                # The user says "replace it with <strong class='sv-sites'></strong> Sites Protected"
                el.replace_with(BeautifulSoup('<strong class="sv-sites"></strong> Sites Protected', "html.parser"))
                break
                
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Fixed index.html trust bar.")

if __name__ == "__main__":
    apply_updates()
    fix_index_trust_bar()
