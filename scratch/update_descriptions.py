import os
import re

updates = {
    "portfolio/commercial/hilton-singapore-orchard-fire-door.html": "Securevision secured 50+ fire emergency doors across Hilton Singapore Orchard with EM locks, ZKTeco CV management, and fire alarm integration.",
    "portfolio/commercial/scape-commercial.html": "Securevision deployed 209 AI cameras and face recognition access at SCAPE Orchard Road — with Salesforce integration — cutting incident response time by 87%.",
    "portfolio/commercial/scape-smart-booking-access.html": "Securevision connected SCAPE Singapore's Salesforce bookings to ZKTeco access control — eliminating manual check-ins with automated QR code entry.",
    "portfolio/condominiums/hillview-park-cctv-upgrade.html": "Securevision upgraded Hillview Park condominium with 48 IP cameras across 3 towers and common facilities, with cloud-ready NVR management.",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html": "Securevision transformed Idyllic Suites from weak access control to a fully logged condominium environment with integrated intercom and CCTV.",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html": "Securevision upgraded FORT Data Centre from end-of-life ZKTeco v3.5 to ZK CV Security — replacing 5 access doors and over 40 cameras.",
    "portfolio/healthcare/surya-home.html": "Securevision delivered CCTV, MicroEngine door access, lift control, and UPS for the rebuilt Surya Home — a care facility for adults with intellectual disability.",
    "portfolio/industrial/hoy-san-industrial.html": "Securevision automated vehicle access at Hoy San Group's Penjuru logistics facility using GantryGo LPR, MAG barriers, and LiDAR safety systems.",
    "portfolio/industrial/multibase-construction-security-upgrade.html": "Securevision upgraded Multibase Construction's Tuas South facility with 16 AI cameras, ZKTeco biometric entry, and barrier automation.",
    "portfolio/industrial/smartflex-tampines.html": "Securevision managed Smartflex's security relocation from Ubi to Tampines — IP CCTV upgrade, expanded MicroEngine card access, and DSC alarm reinstallation.",
    "portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html": "Securevision upgraded STMicroelectronics' Loyang perimeter — 1.2km fence line protected by RISCO alarm integration and high-definition surveillance.",
    "portfolio/institutions/das-learning-centre-woodlands.html": "Securevision installed child-safety security for the Dyslexia Association of Singapore at Causeway Point — 14 cameras and biometric entry.",
    "portfolio/institutions/my-world-preschool-cctv.html": "Securevision provides integrated surveillance for MY World Preschool centres — high-definition cameras, secure recording, and child-safety protocols.",
    "portfolio/institutions/sengkang-interim-bus-interchange.html": "Securevision delivered the design-and-build CCTV system for LTA's Sengkang Interim Bus Interchange — 53 cameras, 5 NVRs, and 28-day retention.",
    "portfolio/residential/lengkok-mariam-landed-home.html": "Securevision delivered integrated security for a landed home at Lengkok Mariam — RISCO alarm, Hikvision CCTV, Aiphone intercom, and FAAC gate control.",
    "portfolio/residential/shelford-landed-home.html": "Securevision delivered integrated security for detached bungalows at Shelford Road — Paradox alarms, Hikvision CCTV, and Aiphone intercoms.",
    "portfolio/residential/siglap-bank-landed-home.html": "Securevision delivered integrated security for a landed home at Siglap Bank — RISCO alarm, Hikvision CCTV, Aiphone intercom, and Dormer gate control.",
    "portfolio/residential/upper-east-coast-road-landed-home.html": "A decade-long security partnership at Upper East Coast Road — covering IP CCTV, keyphone, and two generations of motorised gate automation."
}

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

with open("meta_update_results.txt", "w", encoding="utf-8") as out:
    out.write("File | Description length | og:description matches | Within 120-160\n")
    out.write("---|---|---|---\n")

    for fpath, new_desc in updates.items():
        full = os.path.join(base_dir, fpath)
        if not os.path.exists(full):
            continue
            
        with open(full, "r", encoding="utf-8") as f:
            content = f.read()
            
        # replace meta description
        # Using lambda to avoid messing up with re.escape and groups
        content = re.sub(r'(<meta[^>]*name="description"[^>]*content=")(.*?)(")', lambda m: m.group(1) + new_desc + m.group(3), content, flags=re.IGNORECASE)
        
        # replace og:description
        content = re.sub(r'(<meta[^>]*property="og:description"[^>]*content=")(.*?)(")', lambda m: m.group(1) + new_desc + m.group(3), content, flags=re.IGNORECASE)
        
        with open(full, "w", encoding="utf-8") as f:
            f.write(content)
            
        # Verify
        dmatch = re.search(r'<meta[^>]*name="description"[^>]*content="(.*?)"', content, re.IGNORECASE)
        ogmatch = re.search(r'<meta[^>]*property="og:description"[^>]*content="(.*?)"', content, re.IGNORECASE)
        
        desc = dmatch.group(1) if dmatch else ""
        og_desc = ogmatch.group(1) if ogmatch else ""
        
        length = len(desc)
        matches = "Yes" if desc == og_desc and desc == new_desc else "No"
        within = "Yes" if 120 <= length <= 160 else f"No ({length})"
        
        flag = " 🚩" if "No" in within else ""
        
        out.write(f"{fpath} | {length} | {matches} | {within}{flag}\n")
