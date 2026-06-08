import os
from bs4 import BeautifulSoup

RESOURCES_DIR = r"C:\Projects\SV-Build\resources"

SEO_DATA = {
    "calculators.html": {
        "title": "Security System Calculators Singapore | Securevision",
        "desc": "Free security planning calculators for Singapore — CCTV bandwidth and storage, camera coverage zones, system cost estimates for CCTV and access."
    },
    "checklists.html": {
        "title": "Security Planning Checklists Singapore | Securevision",
        "desc": "Interactive security planning checklists for Singapore properties — commercial offices, condominiums, care facilities, institutions, and dorms."
    },
    "faq.html": {
        "title": "Security System FAQs For Singapore | Securevision",
        "desc": "Answers to common questions about security systems in Singapore — CCTV cameras, burglar alarms, door access control, intercoms, and auto gates."
    },
    "guides.html": {
        "title": "Security System Technical Guides Singapore | Securevision",
        "desc": "Nine in-depth security system guides for Singapore — burglar alarms, CCTV, door access control, intercoms, auto gates, network, IP telephony."
    },
    "index.html": {
        "title": "Security Resources & Guides Singapore | Securevision",
        "desc": "Singapore's complete security knowledge base — technical guides, planning checklists, sizing calculators, and a full product library."
    },
    "library.html": {
        "title": "Security Product Library Singapore | Securevision",
        "desc": "Browse Securevision's product library — datasheets, specifications, manuals, and videos for every security brand we install in Singapore."
    },
    "training-videos.html": {
        "title": "Security System Training Videos Singapore | Securevision",
        "desc": "Training videos and how-to guides for security systems installed by Securevision in Singapore — Akuvox SmartPlus app tutorials, CCTV guides."
    },
    "auto-gate-guide.html": {
        "title": "Auto Gates & Vehicle Barriers Guide Singapore | Securevision",
        "desc": "From residential driveways to condominium barriers — understand gate motor selection, safety sensor standards, and LPR integration in Singapore."
    },
    "burglar-alarm-guide.html": {
        "title": "Burglar & Intrusion Alarm Guide Singapore | Securevision",
        "desc": "Technical guide for home and commercial burglar alarm systems in Singapore. Planning, sensor selection, wired vs wireless, monitoring tiers."
    },
    "cctv-guide.html": {
        "title": "CCTV Camera Systems Guide | Securevision Singapore",
        "desc": "The definitive technical guide to CCTV camera systems in Singapore. Planning, resolution standards, AI analytics, and legal PDPA compliance."
    },
    "door-access-guide.html": {
        "title": "Door Access Control Systems Guide Singapore | Securevision",
        "desc": "A comprehensive engineering-led guide to door access control in Singapore. Biometric terminals, cloud management, lock selection, fire safety."
    },
    "how-to-evaluate-security-contractor.html": {
        "title": "Evaluate A Security Contractor In Singapore | Securevision",
        "desc": "Licensing, quotation reading, site assessment standards, red flags, warranties, and handover — a practical guide to choosing a security contractor."
    },
    "intercom-guide.html": {
        "title": "Intercom & Video Entry Systems Guide Singapore | Securevision",
        "desc": "The definitive guide to intercom systems for Singapore properties — from residential landed homes to condominiums and commercial buildings."
    },
    "office-telephone-guide.html": {
        "title": "Office Telephone & IP Phone Guide Singapore | Securevision",
        "desc": "From PABX replacement to Yeastar IP deployment — understand SIP trunks, hosted telephony, Fanvil door phones, and communication infrastructure."
    },
    "security-renovation-guide.html": {
        "title": "Security Planning During Renovation Singapore | Securevision",
        "desc": "The only time to plan your security system without compromise is before the walls close. A complete guide for Singapore homeowners and MCSTs."
    },
    "wifi-network-guide.html": {
        "title": "Home Network & Wi-Fi Planning Guide Singapore | Securevision",
        "desc": "Wired vs wireless, Cat 6 cabling, PoE switches, static IPs, mesh systems, and why your router swap broke the cameras — a complete network guide."
    }
}

for root, dirs, files in os.walk(RESOURCES_DIR):
    for fname in files:
        if fname in SEO_DATA:
            path = os.path.join(root, fname)
            with open(path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            
            # Title
            if soup.title:
                soup.title.string = SEO_DATA[fname]['title']
            
            # og:title
            og_title = soup.find("meta", attrs={"property": "og:title"})
            if og_title:
                og_title["content"] = SEO_DATA[fname]['title']
                
            # description
            desc = soup.find("meta", attrs={"name": "description"})
            if desc:
                desc["content"] = SEO_DATA[fname]['desc']
                
            # og:description
            og_desc = soup.find("meta", attrs={"property": "og:description"})
            if og_desc:
                og_desc["content"] = SEO_DATA[fname]['desc']
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(str(soup))

print("Phase 4 SEO rewrites applied with BS4.")
