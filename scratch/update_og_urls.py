import os
import re

files_and_urls = {
    "portfolio/commercial/catholic-centre-security-partnership.html": "https://www.securevision.com.sg/portfolio/commercial/catholic-centre-security-partnership.html",
    "portfolio/commercial/scape-smart-booking-access.html": "https://www.securevision.com.sg/portfolio/commercial/scape-smart-booking-access.html",
    "portfolio/commercial/st-engineering-mobility-cctv.html": "https://www.securevision.com.sg/portfolio/commercial/st-engineering-mobility-cctv.html",
    "portfolio/condominiums/clearwater-access-salto-partnership.html": "https://www.securevision.com.sg/portfolio/condominiums/clearwater-access-salto-partnership.html",
    "portfolio/condominiums/clearwater-cctv-upgrade.html": "https://www.securevision.com.sg/portfolio/condominiums/clearwater-cctv-upgrade.html",
    "portfolio/condominiums/high-oak-condominium-cctv.html": "https://www.securevision.com.sg/portfolio/condominiums/high-oak-condominium-cctv.html",
    "portfolio/condominiums/rezi-3two-condo.html": "https://www.securevision.com.sg/portfolio/condominiums/rezi-3two-condo.html",
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html": "https://www.securevision.com.sg/portfolio/condominiums/suites-cairnhill-intercom-lpr.html",
    "portfolio/healthcare/surya-home.html": "https://www.securevision.com.sg/portfolio/healthcare/surya-home.html",
    "portfolio/industrial/cogent-logistics-hub-cctv.html": "https://www.securevision.com.sg/portfolio/industrial/cogent-logistics-hub-cctv.html",
    "portfolio/industrial/mitsubishi-elevator-face-access-bms.html": "https://www.securevision.com.sg/portfolio/industrial/mitsubishi-elevator-face-access-bms.html",
    "portfolio/industrial/sta-compliance-imaging.html": "https://www.securevision.com.sg/portfolio/industrial/sta-compliance-imaging.html",
    "portfolio/industrial/smartflex-tampines.html": "https://www.securevision.com.sg/portfolio/industrial/smartflex-tampines.html",
    "portfolio/institutions/catholic-centre-waterloo.html": "https://www.securevision.com.sg/portfolio/institutions/catholic-centre-waterloo.html",
    "portfolio/institutions/changi-airport-lpr-barriers.html": "https://www.securevision.com.sg/portfolio/institutions/changi-airport-lpr-barriers.html",
    "portfolio/institutions/cpf-maxwell-institution.html": "https://www.securevision.com.sg/portfolio/institutions/cpf-maxwell-institution.html",
    "portfolio/institutions/sengkang-interim-bus-interchange.html": "https://www.securevision.com.sg/portfolio/institutions/sengkang-interim-bus-interchange.html",
    "portfolio/institutions/sfx-retreat-centre-punggol.html": "https://www.securevision.com.sg/portfolio/institutions/sfx-retreat-centre-punggol.html",
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html": "https://www.securevision.com.sg/portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html": "https://www.securevision.com.sg/portfolio/managed-living/scb-worker-dormitory-jalan-papan.html"
}

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

print("File | canonical href | og:url content | Match")
print("---|---|---|---")

for fpath, new_url in files_and_urls.items():
    full_path = os.path.join(base_dir, fpath)
    if not os.path.exists(full_path):
        continue
        
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update og:url
    new_content = re.sub(
        r'(<meta[^>]*property=["\']og:url["\'][^>]*content=["\'])([^"\']+)(["\'])',
        r'\g<1>' + new_url + r'\g<3>',
        content,
        flags=re.IGNORECASE
    )
    if new_content == content:
        # try the reverse order: content then property
        new_content = re.sub(
            r'(<meta[^>]*content=["\'])([^"\']+)(["\'][^>]*property=["\']og:url["\'])',
            r'\g<1>' + new_url + r'\g<3>',
            content,
            flags=re.IGNORECASE
        )

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    # Verification
    canonical_match = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', new_content, re.IGNORECASE)
    if not canonical_match:
        canonical_match = re.search(r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']', new_content, re.IGNORECASE)
        
    ogurl_match = re.search(r'<meta[^>]*property=["\']og:url["\'][^>]*content=["\']([^"\']+)["\']', new_content, re.IGNORECASE)
    if not ogurl_match:
        ogurl_match = re.search(r'<meta[^>]*content=["\']([^"\']+)["\'][^>]*property=["\']og:url["\']', new_content, re.IGNORECASE)
        
    canonical_val = canonical_match.group(1) if canonical_match else "NOT FOUND"
    ogurl_val = ogurl_match.group(1) if ogurl_match else "NOT FOUND"
    
    match_val = "Yes" if canonical_val == ogurl_val and canonical_val != "NOT FOUND" else "No 🚩"
    print(f"{fpath} | {canonical_val} | {ogurl_val} | {match_val}")
