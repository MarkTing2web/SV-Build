import os
import re

base_dir = "C:/Projects/SV-Build"
brands_dir = os.path.join(base_dir, "brands")

data = {
    "aiphone-intercom.html": {
        "title": "Aiphone Intercom Installer Singapore | Securevision",
        "description": "Securevision installs Aiphone GT, JO, and IXG video intercom in Singapore. Japanese quality, long lifespan, condominium and residential specialists."
    },
    "ajax-alarms.html": {
        "description": "Securevision is an authorised AJAX partner in Singapore. We install and maintain AJAX wireless intrusion systems using Jeweller RF technology. Police-licensed."
    },
    "akuvox-access.html": {
        "title": "Akuvox Cloud Access Control Singapore | Securevision",
        "description": "Securevision installs Akuvox cloud-based access control for Singapore offices. Face recognition, card, PIN, and mobile app door release. Police-licensed."
    },
    "akuvox-intercom.html": {
        "title": "Akuvox SmartPlus Intercom Singapore | Securevision",
        "description": "Securevision installs Akuvox IP intercom across Singapore condominiums and offices. SmartPlus cloud platform, lift integration, remote monitoring."
    },
    "apollo-access.html": {
        "description": "Securevision installs Apollo Security access control in Singapore. NDAA-compliant, ASP-4 clustering controllers, APACS software, IDEMIA biometric integration."
    },
    "dahua-cctv.html": {
        "title": "Dahua IP Camera Installer Singapore | Securevision",
        "description": "Securevision installs and services Dahua IP camera systems in Singapore for existing clients and projects where Dahua is specified. Police-licensed integrator."
    },
    "dormer-autogate.html": {
        "title": "Dormer Recess Gate Motors Singapore | Securevision",
        "description": "Securevision installs Dormer recess swing gate motors in Singapore. Compact, cost-effective, suited to replacement of existing gate motor installations."
    },
    "dsc-alarms.html": {
        "description": "Securevision installs DSC PowerSeries Neo and Pro intrusion alarms in Singapore. Wireless PowerG technology, wired zones, professional monitoring."
    },
    "ebelco-locks.html": {
        "title": "Ebelco Electromagnetic Locks Singapore | Securevision",
        "description": "Securevision installs Ebelco electromagnetic locks, door holders, and access accessories in Singapore. Indoor and outdoor EM lock range. Police-licensed."
    },
    "entrypass-entry-access.html": {
        "description": "Securevision installs and services EntryPass access control in Singapore. N-series controllers, Suprema biometric integration, elevator and car park control."
    },
    "faac-autogate.html": {
        "title": "FAAC Gate Motor Installer Singapore | Securevision",
        "description": "Securevision installs FAAC Italian gate motors in Singapore. FAAC 746 sliding gate (600kg), FAAC 844 heavy duty (2,200kg), FAAC 415 swing arm. Police-licensed."
    },
    "fanvil-intercom.html": {
        "title": "Fanvil SIP Door Phone Installer Singapore | Securevision",
        "description": "Securevision installs Fanvil SIP video door phones in Singapore. i31S and i16SV stations work with Yeastar IPPBX so visitors ring IP desk phones directly."
    },
    "fanvil-ip-phone.html": {
        "title": "Fanvil VoIP Phone Installer Singapore | Securevision",
        "description": "Securevision installs Fanvil IP phones for Singapore offices. X-Series, V-Series, WiFi models, and 2-wire retrofit phones reusing existing keyphone wiring."
    },
    "gantrygo.html": {
        "description": "GantryGo is Securevision's LPR vehicle management platform for Singapore condominiums. Visitor pre-registration, licence plate recognition, parking alerts."
    },
    "ge-caddx-alarms.html": {
        "description": "Securevision installs and maintains GE-Caddx NetworX alarm systems in Singapore. NX-8V2 controllers, wired zone expanders, and monitoring support. Police-licensed."
    },
    "hanwha-cctv.html": {
        "title": "Hanwha Vision CCTV Installer Singapore | Securevision",
        "description": "Securevision installs Hanwha Vision (Wisenet) CCTV in Singapore. AI analytics, NDAA-compliant cameras, and Wave VMS. Police-licensed security integrator."
    },
    "hid-entry-access.html": {
        "title": "HID Global Access Credentials Singapore | Securevision",
        "description": "Securevision installs HID Global readers and credentials in Singapore. Signo readers, iCLASS SE, Seos, ProxCard — works with ZKTeco, Suprema, EntryPass."
    },
    "hikcentral.html": {
        "title": "HikCentral Professional Platform Singapore | Securevision",
        "description": "Securevision installs HikCentral Professional in Singapore — unified CCTV, access control, and ANPR on one platform. Modular perpetual licensing. Police-licensed."
    },
    "hikvision-access.html": {
        "title": "Hikvision Access Control Installer Singapore | Securevision",
        "description": "Securevision installs Hikvision MinMoe and HikCentral Access Control in Singapore. Face recognition terminals, up to 16 doors free, anti-passback, time zones."
    },
    "hikvision-cctv.html": {
        "title": "Hikvision CCTV Camera Installer Singapore | Securevision",
        "description": "Securevision is a Hikvision CCTV installer in Singapore. We specify ColorVu full-colour, AcuSense AI analytics, and DarkFighter technology. Police-licensed."
    },
    "hikvision-intercom.html": {
        "title": "Hikvision Video Door Intercom Singapore | Securevision",
        "description": "Securevision installs Hikvision IP, 2-wire, and 4-wire video intercom in Singapore. DS-KV door stations, indoor monitors, Hik-Connect app. Police-licensed."
    },
    "hrui-network.html": {
        "title": "HRUI PoE Network Switches Singapore | Securevision",
        "description": "Securevision deploys HRUI AI PoE switches for CCTV infrastructure in Singapore. Outdoor-rated, PoE watchdog auto-reboot, heavy-load power for cameras."
    },
    "kocom-intercom.html": {
        "title": "Kocom Video Intercom Service Singapore | Securevision"
    },
    "mag-autogate.html": {
        "title": "MAG Auto Gate and Barrier Singapore | Securevision",
        "description": "Securevision installs MAG car park barriers and swing gate motors in Singapore. Reliable, cost-effective Malaysian brand, well-supported from Johor Bahru."
    },
    "microengine-entry-access.html": {
        "description": "Securevision installs MicroEngine xPortal access control in Singapore. Plato readers, xPortalNet software, DesFire card encryption. Police-licensed."
    },
    "milesight-cctv.html": {
        "description": "Securevision installs Milesight AI surveillance and AIoT in Singapore. Next-generation optics, panoramic cameras, and intelligent LPR for commercial sites."
    },
    "omada-network.html": {
        "description": "Securevision deploys TP-Link Omada cloud-managed PoE switches and wireless APs for security networks in Singapore. Remote management and fibre uplinks."
    },
    "paradox-alarms.html": {
        "description": "Securevision installs Paradox EVO and MG series intrusion alarms in Singapore. High-security bus systems, wireless zone expansion, and professional monitoring."
    },
    "risco-alarms.html": {
        "description": "Securevision installs RISCO LightSYS and ProSYS alarms in Singapore. Cloud-integrated hybrid panels, wired zones, professional monitoring. Police-licensed."
    },
    "ruijie-reyee-network.html": {
        "description": "Securevision deploys Ruijie and Reyee cloud-managed PoE switches and wireless bridges for security networks in Singapore. Remote management and loop protection."
    },
    "suprema-entry-access.html": {
        "description": "Securevision installs Suprema biometric access control in Singapore. BioStation 3, FaceStation F2, BioEntry outdoor readers, and BioStar 2 management platform."
    },
    "uniview-cctv.html": {
        "title": "Uniview UNV CCTV Installer Singapore | Securevision",
        "description": "Securevision installs Uniview (UNV) CCTV in Singapore. Prime series, ColorHunter low-light cameras, and AI video analytics for commercial and industrial sites."
    },
    "vesta.html": {
        "title": "VESTA Smart Living Platform Singapore | Securevision",
        "description": "VESTA by Securevision unifies intercom, visitor management, facility booking, GantryGo LPR, and estate communications in one app for Singapore condominiums."
    },
    "viro-locks.html": {
        "description": "Securevision installs VIRO Italian electric strikes for Singapore gates and doors. Fail-secure — stays locked on power loss. Mechanical key override."
    },
    "yealink-ip-phone.html": {
        "title": "Yealink IP Phone Installer Singapore | Securevision",
        "description": "Securevision supplies and installs Yealink T-Series IP phones for Singapore offices. Reliable VoIP handsets compatible with Yeastar IPPBX. Police-licensed."
    },
    "yeastar-ippbx.html": {
        "title": "Yeastar IPPBX Phone System Singapore | Securevision",
        "description": "Securevision installs Yeastar P-Series and S-Series IPPBX in Singapore. Replace legacy keyphone systems with SIP trunks, DID numbers, and Linkus mobile app."
    },
    "zkteco-cvsecurity.html": {
        "title": "ZKBio CVSecurity Platform Singapore | Securevision",
        "description": "Securevision installs ZKBio CVSecurity for Singapore — unified access control, CCTV, LPR, intercom, and visitor management. On-premise, one-time licence."
    },
    "zkteco-entry-access.html": {
        "description": "Securevision installs ZKTeco biometric access control in Singapore. SpeedFace, ProID, InBio Pro panels, and ZKBio CVSecurity. Face, fingerprint, card, PIN."
    }
}

files_in_scope = [
    "aiphone-intercom.html", "ajax-alarms.html", "akuvox-access.html", "akuvox-intercom.html",
    "apollo-access.html", "dahua-cctv.html", "dormer-autogate.html", "dsc-alarms.html",
    "ebelco-locks.html", "entrypass-entry-access.html", "faac-autogate.html", "fanvil-intercom.html",
    "fanvil-ip-phone.html", "gantrygo.html", "ge-caddx-alarms.html", "hanwha-cctv.html",
    "hid-entry-access.html", "hikcentral.html", "hikvision-access.html", "hikvision-cctv.html",
    "hikvision-intercom.html", "hrui-network.html", "kocom-intercom.html", "mag-autogate.html",
    "microengine-entry-access.html", "milesight-cctv.html", "omada-network.html", "paradox-alarms.html",
    "risco-alarms.html", "ruijie-reyee-network.html", "suprema-entry-access.html", "uniview-cctv.html",
    "vesta.html", "viro-locks.html", "yealink-ip-phone.html", "yeastar-ippbx.html",
    "zkteco-cvsecurity.html", "zkteco-entry-access.html"
]

stats = {
    'modified': 0,
    'titles': 0,
    'descriptions': 0,
    'og': 0
}

# Apply fixes
for filename in files_in_scope:
    filepath = os.path.join(brands_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    orig_html = html
    
    # 1. Update Title if specified
    if filename in data and 'title' in data[filename]:
        new_title = data[filename]['title']
        html_new, n = re.subn(r'<title>(.*?)</title>', f'<title>{new_title}</title>', html, count=1)
        if html_new != html:
            stats['titles'] += 1
            html = html_new

    # 2. Update Description if specified
    if filename in data and 'description' in data[filename]:
        new_desc = data[filename]['description']
        html_new, n = re.subn(r'<meta name="description" content="([^"]*)">', f'<meta name="description" content="{new_desc}">', html, count=1)
        if html_new != html:
            stats['descriptions'] += 1
            html = html_new

    # Get the current title and description to sync with OG
    current_title_match = re.search(r'<title>(.*?)</title>', html)
    current_title = current_title_match.group(1) if current_title_match else ""
    
    current_desc_match = re.search(r'<meta name="description" content="([^"]*)">', html)
    current_desc = current_desc_match.group(1) if current_desc_match else ""
    
    canonical_url = f"https://www.securevision.com.sg/brands/{filename}"
    
    # 3. Sync og:title
    html_new, n = re.subn(r'<meta property="og:title" content="([^"]*)">', f'<meta property="og:title" content="{current_title}">', html, count=1)
    if html_new != html:
        stats['og'] += 1
        html = html_new
        
    # 4. Sync og:description
    html_new, n = re.subn(r'<meta property="og:description" content="([^"]*)">', f'<meta property="og:description" content="{current_desc}">', html, count=1)
    if html_new != html:
        stats['og'] += 1
        html = html_new
        
    # 5. Sync og:url
    html_new, n = re.subn(r'<meta property="og:url" content="([^"]*)">', f'<meta property="og:url" content="{canonical_url}">', html, count=1)
    if html_new != html:
        stats['og'] += 1
        html = html_new
        
    # 6. Ensure canonical is correct
    html_new, n = re.subn(r'<link rel="canonical" href="([^"]*)">', f'<link rel="canonical" href="{canonical_url}">', html, count=1)
    if html_new != html:
        html = html_new
        
    if html != orig_html:
        stats['modified'] += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

# Audit
audit = {
    'A': [], 'B': [], 'C': [], 'D': [], 'E': []
}

for filename in files_in_scope:
    filepath = os.path.join(brands_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    t_match = re.search(r'<title>(.*?)</title>', html)
    t = t_match.group(1).strip() if t_match else ""
    if not (50 <= len(t) <= 60):
        audit['A'].append(f"{filename} ({len(t)} chars)")
        
    d_match = re.search(r'<meta name="description" content="([^"]*)">', html)
    d = d_match.group(1).strip() if d_match else ""
    if not (120 <= len(d) <= 160):
        audit['B'].append(f"{filename} ({len(d)} chars)")
        
    og_t_match = re.search(r'<meta property="og:title" content="([^"]*)">', html)
    og_t = og_t_match.group(1).strip() if og_t_match else ""
    if og_t != t:
        audit['C'].append(filename)
        
    og_d_match = re.search(r'<meta property="og:description" content="([^"]*)">', html)
    og_d = og_d_match.group(1).strip() if og_d_match else ""
    if og_d != d:
        audit['D'].append(filename)
        
    expected_url = f"https://www.securevision.com.sg/brands/{filename}"
    og_u_match = re.search(r'<meta property="og:url" content="([^"]*)">', html)
    og_u = og_u_match.group(1).strip() if og_u_match else ""
    if og_u != expected_url:
        audit['E'].append(filename)
        
clean_pages = 38 - len(set([f.split(' ')[0] for f in audit['A'] + audit['B'] + audit['C'] + audit['D'] + audit['E']]))

out = []
out.append("BRANDS SECTION FIX — WAVE 5 COMPLETION REPORT")
out.append("Files processed: 38")
out.append(f"Files modified: {stats['modified']}\n")
out.append(f"Titles updated: {stats['titles']}")
out.append(f"Descriptions updated: {stats['descriptions']}")
out.append(f"OG tags synced: {stats['og']}\n")
out.append("AUDIT FINDINGS:")
out.append(f"A. Title length issues: {', '.join(audit['A']) if audit['A'] else 'None'}")
out.append(f"B. Description length issues: {', '.join(audit['B']) if audit['B'] else 'None'}")
out.append(f"C. og:title mismatches: {', '.join(audit['C']) if audit['C'] else 'None'}")
out.append(f"D. og:description mismatches: {', '.join(audit['D']) if audit['D'] else 'None'}")
out.append(f"E. og:url mismatches: {', '.join(audit['E']) if audit['E'] else 'None'}\n")
out.append(f"Pages fully clean: {clean_pages} / 38")

with open(os.path.join(base_dir, "_ai/audit-brands-wave5-completion.md"), 'w', encoding='utf-8') as f:
    f.write("\n".join(out))

print("Wave 5 completed.")
