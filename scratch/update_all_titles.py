import os
import re

changes = {
    "portfolio/commercial/altitudex-sentosa-commercial.html": "AltitudeX Sentosa — Access Upgrade Singapore | Securevision",
    "portfolio/commercial/catholic-centre-security-partnership.html": "Catholic Centre Security Partnership Singapore | Securevision",
    "portfolio/commercial/em-services-call-centre-redhill.html": "EM Services Redhill — CCTV & Access | Securevision Singapore",
    "portfolio/commercial/hilton-singapore-orchard-fire-door.html": "Hilton Singapore Orchard — Fire Door Access | Securevision",
    "portfolio/commercial/scape-commercial.html": "SCAPE Singapore — AI Surveillance & Access | Securevision",
    "portfolio/commercial/scape-smart-booking-access.html": "SCAPE Singapore — Booking to Access | Securevision",
    "portfolio/commercial/st-engineering-mobility-cctv.html": "ST Engineering Mobility — CCTV Singapore | Securevision",
    "portfolio/condominiums/clearwater-access-salto-partnership.html": "The Clearwater — Access Control Singapore | Securevision",
    "portfolio/condominiums/clearwater-cctv-upgrade.html": "The Clearwater — CCTV Upgrade Singapore | Securevision",
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html": "Country Grandeur — Condo Security Singapore | Securevision",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html": "D'Elias — Condo Security Upgrade Singapore | Securevision",
    "portfolio/condominiums/high-oak-condominium-cctv.html": "High Oak Condominium — CCTV Singapore | Securevision",
    "portfolio/condominiums/hillview-park-cctv-upgrade.html": "Hillview Park — CCTV Upgrade Singapore | Securevision",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html": "Idyllic Suites — Condo Security Singapore | Securevision",
    "portfolio/condominiums/light-cairnhill-condo.html": "Light at Cairnhill — Security Singapore | Securevision",
    "portfolio/condominiums/mergui-mansions-novena-condo.html": "Mergui Mansions — Condo Security Singapore | Securevision",
    "portfolio/condominiums/newton21-newton-condo.html": "Newton 21 — Condo Security Singapore | Securevision",
    "portfolio/condominiums/rezi-3two-condo.html": "Rezi 3Two — Condo Security Singapore | Securevision",
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html": "Suites@Cairnhill — Intercom & LPR Singapore | Securevision",
    "portfolio/condominiums/the-bale-intercom-cctv.html": "The Bale — Intercom & CCTV Singapore | Securevision",
    "portfolio/condominiums/the-lviv-newton-condo.html": "L'viv Residences — Security Singapore | Securevision",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html": "The Verte — Condo Security Singapore | Securevision",
    "portfolio/condominiums/village-pasir-panjang-condo.html": "Village @ Pasir Panjang — Security Singapore | Securevision",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html": "FORT Data Centre — Access Upgrade Singapore | Securevision",
    "portfolio/data-centres/fort-st-engineering.html": "FORT Data Centre — CCTV Upgrade Singapore | Securevision",
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html": "Sunlove Wellness Centre — Security Singapore | Securevision",
    "portfolio/healthcare/surya-home.html": "Surya Home — Residence Security Singapore | Securevision",
    "portfolio/industrial/cogent-logistics-hub-cctv.html": "Cogent Logistics Hub — CCTV Singapore | Securevision",
    "portfolio/industrial/cyrus-tech-industrial.html": "Cyrus Tech — New Facility Security Singapore | Securevision",
    "portfolio/industrial/hoy-san-industrial.html": "Hoy San Group — Vehicle Access Singapore | Securevision",
    "portfolio/industrial/mitsubishi-elevator-face-access-bms.html": "Mitsubishi Elevator — Face Access Singapore | Securevision",
    "portfolio/industrial/multibase-construction-security-upgrade.html": "Multibase Construction — Security Singapore | Securevision",
    "portfolio/industrial/smartflex-tampines.html": "Smartflex Tampines — Security Singapore | Securevision",
    "portfolio/industrial/sta-compliance-imaging.html": "STA Compliance Imaging — Security Singapore | Securevision",
    "portfolio/industrial/sta-inspection-industrial.html": "STA Inspection — Security Singapore | Securevision",
    "portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html": "STMicroelectronics — Perimeter Singapore | Securevision",
    "portfolio/institutions/catholic-centre-waterloo.html": "Catholic Centre Waterloo — CCTV Singapore | Securevision",
    "portfolio/institutions/changi-airport-lpr-barriers.html": "Changi Airport — Airside LPR Singapore | Securevision",
    "portfolio/institutions/cpf-maxwell-institution.html": "CPF Maxwell — Accountability Singapore | Securevision",
    "portfolio/institutions/das-learning-centre-woodlands.html": "DAS Learning Centre — Security Singapore | Securevision",
    "portfolio/institutions/my-world-preschool-cctv.html": "MY World Preschool — CCTV Singapore | Securevision",
    "portfolio/institutions/sengkang-interim-bus-interchange.html": "Sengkang Bus Interchange — CCTV Singapore | Securevision",
    "portfolio/institutions/sfx-retreat-centre-punggol.html": "SFX Retreat Centre — Security Singapore | Securevision",
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html": "Nursing Hostel Seh Chuan — Security Singapore | Securevision",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html": "SCB Worker Dormitory — Access Singapore | Securevision",
    "portfolio/residential/dunbar-walk-landed-home.html": "Dunbar Walk — Landed Home Security Singapore | Securevision",
    "portfolio/residential/dyson-8-residences-landed-home.html": "Dyson 8 Residences — Security Singapore | Securevision",
    "portfolio/residential/lengkok-mariam-landed-home.html": "Lengkok Mariam — Landed Security Singapore | Securevision",
    "portfolio/residential/merryn-road-landed-home.html": "Merryn Road — Landed Home Security Singapore | Securevision",
    "portfolio/residential/shelford-landed-home.html": "Shelford Road — Landed Security Singapore | Securevision",
    "portfolio/residential/siglap-bank-landed-home.html": "Siglap Bank — Landed Home Security Singapore | Securevision",
    "portfolio/residential/upper-east-coast-road-landed-home.html": "Upper East Coast — Landed Security Singapore | Securevision"
}

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

with open("titles_update_output.txt", "w", encoding="utf-8") as out:
    out.write("File | New title | Chars | og:title matches title\n")
    out.write("---|---|---|---\n")

    for fpath, new_title in changes.items():
        full_path = os.path.join(base_dir, fpath)
        if not os.path.exists(full_path):
            continue
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update <title>
        content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.IGNORECASE | re.DOTALL)
        
        # Update og:title
        def replace_content(match):
            return match.group(1) + f'"{new_title}"'
            
        # Match <meta property="og:title" content="...">
        content = re.sub(r'(<meta[^>]*property=["\']og:title["\'][^>]*content=)["\'].*?["\']', replace_content, content, flags=re.IGNORECASE)
        # Match <meta content="..." property="og:title">
        content = re.sub(r'(<meta[^>]*content=)["\'].*?["\']([^>]*property=["\']og:title["\'])', lambda m: m.group(1) + f'"{new_title}"' + m.group(2), content, flags=re.IGNORECASE)
        
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        # Verification
        match_title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        final_title = match_title.group(1).strip() if match_title else "NOT FOUND"
        t_len = len(final_title)
        
        match_og = re.search(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
        if not match_og:
            match_og = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*property=["\']og:title["\']', content, re.IGNORECASE)
            
        # Since we just used double quotes around new_title, we can easily find it.
        # But wait, what if new_title has double quotes? It doesn't in our list, but if it did, we'd need to escape.
        # It only has single quotes (e.g. D'Elias). So using double quotes for HTML attribute works fine!
        match_og = re.search(r'<meta[^>]*property="og:title"[^>]*content="(.*?)"', content, re.IGNORECASE)
        if not match_og:
             match_og = re.search(r'<meta[^>]*content="(.*?)"[^>]*property="og:title"', content, re.IGNORECASE)
             
        final_og = match_og.group(1).strip() if match_og else "NOT FOUND"
        
        is_match = final_title == final_og
        
        flag_len = ""
        if t_len < 50 or t_len > 60:
            flag_len = " 🚩"
            
        flag_match = ""
        if not is_match:
            flag_match = " 🚩"
            
        match_str = "Yes" if is_match else "No"
        
        out.write(f"{fpath} | {final_title} | {t_len}{flag_len} | {match_str}{flag_match}\n")
