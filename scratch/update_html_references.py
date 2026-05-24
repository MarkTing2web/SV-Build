import os
import re

repo_root = r"c:\Projects\SV-Build"

target_filenames = [
    "automate-vehicle-access-hero.webp",
    "healthcare-hero.webp",
    "improve-visitor-management-hero.webp",
    "intercom-upgrade-hero.webp",
    "reduce-manpower-with-technology-mobile.webp",
    "reduce-manpower-with-technology-rel.webp",
    "solution-commercial-office-hero.webp",
    "solution-commercial-retail-hero.webp",
    "solution-data-centres-hero.webp",
    "solution-healthcare-aged-care-hero.webp",
    "solution-improve-cctv-visibility-hero.webp",
    "solution-industrial-industrial-analysis.webp",
    "solution-managed-living-dormitories-hero.webp",
    "solution-managed-living-hero.webp",
    "solution-managed-living-hostels-hero.webp",
    "solutions-hub-singapore-mobile.webp",
    "solutions-hub-singapore-rel.webp",
    "solutions-hub-singapore.webp",
    "commercial-security-singapore-mobile.webp",
    "commercial-security-singapore-rel.webp",
    "commercial-security-singapore.webp",
    "solution-commercial-hotel-hero.webp",
    "condominium-estate-security-singapore-mobile.webp",
    "condominium-estate-security-singapore-rel.webp",
    "condominium-estate-security-singapore.webp",
    "data-centre-security-singapore-mobile.webp",
    "data-centre-security-singapore-rel.webp",
    "data-centre-security-singapore.webp",
    "healthcare-security-singapore-mobile.webp",
    "healthcare-security-singapore-rel.webp",
    "healthcare-security-singapore.webp",
    "industrial-security-singapore-mobile.webp",
    "industrial-security-singapore-rel.webp",
    "industrial-security-singapore.webp",
    "institutional-security-singapore-mobile.webp",
    "institutional-security-singapore-rel.webp",
    "institutional-security-singapore.webp",
    "dormitories-hero.webp",
    "hostels-hero.webp",
    "managed-living-hero.webp",
    "managed-living-security-singapore-rel.webp",
    "managed-living-security-singapore.webp",
    "managed-living-singapore-mobile.webp",
    "landed-home-security-singapore-mobile.webp",
    "landed-home-security-singapore-rel.webp",
    "landed-home-security-singapore.webp",
    "landed-home-security-warmlight-dusk-mobile.webp",
    "landed-home-security-warmlight-dusk.webp",
    "partnering-architects-and-designers-mobile.webp",
    "partnering-architects-and-designers-rel.webp",
    "planning-to-build-new-house-mobile.webp",
    "planning-to-build-new-house-rel.webp",
    "planning-to-build-new-house.webp",
    "upgrade-fix-residential-security-system-mobile.webp",
    "upgrade-fix-residential-security-system-rel.webp",
    "upgrade-fix-residential-security-system.webp"
]

def main():
    # Find all HTML files recursively
    html_files = []
    for root, dirs, files in os.walk(repo_root):
        if any(p in root.split(os.sep) for p in [".git", "node_modules", ".vercel"]):
            continue
        for f in files:
            if f.lower().endswith('.html'):
                html_files.append(os.path.join(root, f))

    updated_files_log = []
    total_replacements = 0

    for filepath in html_files:
        rel_path = os.path.relpath(filepath, repo_root).replace('\\', '/')
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        modified_content = content
        file_replacements = 0
        
        # We do a replacement for each filename
        for filename in target_filenames:
            pattern = rf'(https?://www\.securevision\.com\.sg)?(?:/|\.\./|)?images/solutions/(?:[\w\-]+/)*{re.escape(filename)}'
            
            def make_replacement(match):
                nonlocal file_replacements
                domain = match.group(1) or ""
                file_replacements += 1
                return domain + "/images/solutions/hero-solutions/" + filename
                
            modified_content = re.sub(pattern, make_replacement, modified_content)
            
        if file_replacements > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            print(f"Updated {rel_path}: {file_replacements} references changed.")
            updated_files_log.append((rel_path, file_replacements))
            total_replacements += file_replacements

    print("\n--- HTML UPDATE SUMMARY ---")
    print(f"Total HTML files updated: {len(updated_files_log)}")
    print(f"Total references updated: {total_replacements}")

    # Write to log file
    log_path = r"c:\Projects\SV-Build\scratch\update_html_references_output.txt"
    with open(log_path, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Total HTML files updated: {len(updated_files_log)}\n")
        log_f.write(f"Total references updated: {total_replacements}\n\n")
        for f, count in updated_files_log:
            log_f.write(f"FILE: {f} — {count} references changed\n")

if __name__ == "__main__":
    main()
