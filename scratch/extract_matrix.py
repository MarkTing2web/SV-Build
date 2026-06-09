import os
import re

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
out_file = os.path.join(root_dir, '_ai', 'extracted-site-matrix.txt')

def extract_meta(html_path):
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            title = title_match.group(1).strip() if title_match else "No title found"
            
            desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', content, re.IGNORECASE | re.DOTALL)
            desc = desc_match.group(1).strip() if desc_match else "No meta description found"
            
            return title, desc
    except Exception as e:
        return f"Error: {e}", ""

sections = {
    "SOLUTIONS PROPERTY TYPES": [
        {"href": "/solutions/residential.html", "name": "Landed & Residential", "fallback": "Bungalows, semi-detached, and terrace homes — integrated alarm and CCTV for perimeter and interior protection."},
        {"href": "/solutions/condominiums.html", "name": "Condominiums & MCSTs", "fallback": "MCSTs, managing agents, and strata estates — estate-wide systems managed from a central operations layer."},
        {"href": "/solutions/commercial.html", "name": "Offices & Commercial", "fallback": "Offices, hotels, retail shops, and commercial buildings — layered security across tenancies and common areas."},
        {"href": "/solutions/industrial.html", "name": "Industrial & Logistics", "fallback": "Factories, warehouses, logistics hubs, and tech parks — large-scale perimeter and operational security."},
        {"href": "/solutions/institutions.html", "name": "Institutions & Government", "fallback": "Schools, government offices, churches, and civic facilities — compliance-grade systems for public environments."},
        {"href": "/solutions/healthcare.html", "name": "Healthcare", "fallback": "Nursing homes, day care centres, and specialist care facilities — patient safety and duty-of-care systems."},
        {"href": "/solutions/managed-living.html", "name": "Managed Living", "fallback": "Worker dormitories, co-living apartments, and managed hostels — access control and monitoring for high-occupancy sites."},
        {"href": "/solutions/data-centres.html", "name": "Data Centres", "fallback": "Colocation, enterprise, and hyperscale facilities — physical access audit trails and compliance-grade surveillance."},
        {"href": "/solutions/", "name": "View All Solutions", "fallback": ""}
    ],
    "SYSTEMS TECHNOLOGY TYPES": [
        {"href": "/systems/premises-security.html", "name": "Premises Security", "fallback": "CCTV, AI analytics, burglar alarms, and sensors — monitor your property and detect what matters."},
        {"href": "/systems/entry-access-control.html", "name": "Entry Access", "fallback": "Door access, biometrics, intercom, and visitor management — control who enters and track movement."},
        {"href": "/systems/vehicle-lpr-management.html", "name": "Vehicle & LPR Management", "fallback": "Auto-gates, barriers, LPR, and car park systems — automate vehicle flow and reduce guard dependency."},
        {"href": "/systems/ip-phone-communications.html", "name": "IP Telephony", "fallback": "IP phones and IPPBX systems — replace legacy keyphones with modern, app-enabled communications."},
        {"href": "/systems/network-infrastructure.html", "name": "Network Infrastructure", "fallback": "Managed PoE switches, WiFi access points, and structured cabling — the IP foundation every system runs on."},
        {"href": "/systems/security-management-platform.html", "name": "Management Platforms", "fallback": "VESTA, Milestone, HikCentral — connect every system into one operational view across your property."},
        {"href": "/systems/", "name": "View All Systems", "fallback": ""}
    ],
    "BRANDS": [
        {"href": "/brands/", "name": "View All Brands", "fallback": ""}
    ],
    "PORTFOLIO": [
        {"href": "/portfolio/", "name": "All Projects", "fallback": ""}
    ],
    "RESOURCES": [
        {"href": "/resources/guides.html", "name": "Technical Guides", "fallback": ""},
        {"href": "/resources/checklists.html", "name": "Planning Checklists", "fallback": ""},
        {"href": "/resources/calculators.html", "name": "Planning Calculators", "fallback": ""},
        {"href": "/resources/library.html", "name": "Product Library", "fallback": ""},
        {"href": "/resources/training-videos.html", "name": "Training Videos", "fallback": ""},
        {"href": "/resources/faq.html", "name": "FAQ", "fallback": ""},
        {"href": "/resources/", "name": "All Resources", "fallback": ""}
    ],
    "INSIGHTS": [
        {"href": "/insights/", "name": "Insights", "fallback": ""}
    ],
    "ABOUT": [
        {"href": "/about.html", "name": "Our Story", "fallback": ""},
        {"href": "/contact.html", "name": "Contact Us", "fallback": ""}
    ]
}

os.makedirs(os.path.dirname(out_file), exist_ok=True)

with open(out_file, 'w', encoding='utf-8') as f:
    for section_name, items in sections.items():
        f.write(f"=== {section_name} ===\n\n")
        for item in items:
            href_clean = item['href']
            if href_clean.endswith('/'):
                href_clean += 'index.html'
            
            full_path = os.path.join(root_dir, href_clean.lstrip('/'))
            title, desc = extract_meta(full_path)
            
            f.write(f"URL Slug: {item['href']}\n")
            f.write(f"Filename: {os.path.basename(href_clean)}\n")
            f.write(f"Menu Name: {item['name']}\n")
            f.write(f"Current <title>: {title}\n")
            if item['fallback']:
                f.write(f"Block Data Fallback: {item['fallback']}\n")
            f.write(f"Current Meta Description: {desc}\n")
            f.write("-" * 40 + "\n\n")

print(f"Extended data extracted and written to {out_file}")
