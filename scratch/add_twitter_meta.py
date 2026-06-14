import os
import re

insight_dir = r"C:\Projects\SV-Build\insights"
files_to_process = [
    "condo-security-upgrade-timeline.html",
    "hdb-landed-condo-security-differences.html",
    "home-security-system-cost-singapore.html",
    "how-card-access-works.html",
    "how-intercom-systems-work.html",
    "how-technology-makes-your-guarding-team-more-competitive.html",
    "how-to-choose-cctv.html",
    "is-my-security-system-still-working.html",
    "maintain-burglar-alarm.html",
    "maintenance-contract.html",
    "managing-agents-guide-estate-security-systems.html",
    "managing-multiple-estates-with-vesta.html",
    "mcst-legal-obligations-security.html",
    "rackmount-nvr.html",
    "reduce-false-alarms.html",
    "security-upgrade-condo-agm.html",
    "standalone-door-access.html"
]

def process_files():
    report = []
    
    for filename in files_to_process:
        filepath = os.path.join(insight_dir, filename)
        if not os.path.exists(filepath):
            report.append({"file": filename, "status": "FILE NOT FOUND"})
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if twitter:image is already present
        if re.search(r'<meta[^>]*?name="twitter:image"[^>]*?>', content):
            report.append({"file": filename, "status": "OK"})
            continue
            
        # Find og:image url
        og_img_match = re.search(r'<meta[^>]*?property="og:image"[^>]*?>|<meta[^>]*?property=[\'"]og:image[\'"][^>]*?>', content)
        if not og_img_match:
            report.append({"file": filename, "status": "OG IMAGE MISSING"})
            continue
            
        og_tag = og_img_match.group(0)
        content_match = re.search(r'content="([^"]*)"', og_tag)
        if not content_match:
            report.append({"file": filename, "status": "OG IMAGE URL MISSING"})
            continue
            
        og_url = content_match.group(1)
        
        # Find og:image:height to insert after
        height_match = re.search(r'<meta[^>]*?property="og:image:height"[^>]*?>', content)
        if not height_match:
            # If height is not found, just insert after og_img_match
            insert_pos = og_img_match.end()
        else:
            insert_pos = height_match.end()
            
        # Build the tags to insert
        tags_to_insert = f'\n  <meta name="twitter:card" content="summary_large_image" />\n  <meta name="twitter:image" content="{og_url}" />'
        
        # Insert
        content = content[:insert_pos] + tags_to_insert + content[insert_pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        report.append({"file": filename, "status": "ADDED"})

    # Output report
    print("| File | twitter:image added |")
    print("|------|-------------------|")
    for r in report:
        print(f"| {r['file']} | {r['status']} |")

if __name__ == "__main__":
    process_files()
