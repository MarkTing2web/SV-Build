import os
import re

files = [
    "portfolio/commercial/catholic-centre-security-partnership.html",
    "portfolio/commercial/scape-smart-booking-access.html",
    "portfolio/commercial/st-engineering-mobility-cctv.html",
    "portfolio/condominiums/clearwater-access-salto-partnership.html",
    "portfolio/condominiums/clearwater-cctv-upgrade.html",
    "portfolio/condominiums/high-oak-condominium-cctv.html",
    "portfolio/condominiums/rezi-3two-condo.html",
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/industrial/cogent-logistics-hub-cctv.html",
    "portfolio/industrial/mitsubishi-elevator-face-access-bms.html",
    "portfolio/industrial/sta-compliance-imaging.html",
    "portfolio/industrial/smartflex-tampines.html",
    "portfolio/institutions/catholic-centre-waterloo.html",
    "portfolio/institutions/changi-airport-lpr-barriers.html",
    "portfolio/institutions/cpf-maxwell-institution.html",
    "portfolio/institutions/sengkang-interim-bus-interchange.html",
    "portfolio/institutions/sfx-retreat-centre-punggol.html",
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

for fpath in files:
    full_path = os.path.join(base_dir, fpath)
    if not os.path.exists(full_path):
        print(f"### {fpath}")
        print("FILE NOT FOUND")
        print()
        continue
        
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    canonical_match = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', content, re.IGNORECASE)
    if not canonical_match:
        # try reverse order
        canonical_match = re.search(r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']', content, re.IGNORECASE)
        
    ogurl_match = re.search(r'<meta[^>]*property=["\']og:url["\'][^>]*content=["\']([^"\']+)["\']', content, re.IGNORECASE)
    if not ogurl_match:
        # try reverse order
        ogurl_match = re.search(r'<meta[^>]*content=["\']([^"\']+)["\'][^>]*property=["\']og:url["\']', content, re.IGNORECASE)
        
    canonical_val = canonical_match.group(1) if canonical_match else "NOT FOUND"
    ogurl_val = ogurl_match.group(1) if ogurl_match else "NOT FOUND"
    
    print(f"### {fpath}")
    print(f"Canonical : {canonical_val}")
    print(f"og:url    : {ogurl_val}")
    print()
