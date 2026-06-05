import os

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"

files_to_delete = [
    "/images/cctv-guide-hero.webp",
    "/images/cta-singapore-skyline.png",
    "/images/cta-skyline-polo.webp",
    "/images/insights-hero-new.webp",
    "/images/intercom-guide-hero.webp",
    "/images/network-reader.png",
    "/images/platform-integration-hero.webp",
    "/images/prop-landed.webp",
    "/images/resources-knowledge-base-singapore-rel.webp",
    "/images/software-dash.png",
    "/images/standalone-reader.png",
    "/images/upgrade-compare.png",
    "/images/pillar_maintenance.webp",
    "/images/about/comp-integration-v3.png",
    "/images/about/people-access-hero.png",
    "/images/about/vehicle-access-hero.png",
    "/images/about/founder-hero-ler-wee-meng-01.webp",
    "/images/home/securevision-logo.svg",
    "/images/brands/vesta-security-logo.webp",
    "/images/portfolio/commercial/catholic-centre.webp",
    "/images/portfolio/commercial/hilton-singapore-orchard.webp",
    "/images/portfolio/data-centres/fort-st-engineering-thumb.png",
    "/images/portfolio/healthcare/sunlove-card.webp",
    "/images/portfolio/industrial/gantrygo-at-work.webp",
    "/images/portfolio/industrial/hoy-san-main-gate.webp",
    "/images/portfolio/institutions/changi-airside.webp",
    "/images/solutions/root-solutions/solution-automate-vehicle-access-prop-industrial.webp",
    "/images/solutions/root-solutions/solution-commercial-hero.webp",
    "/images/solutions/root-solutions/solution-condominiums-project-condo-upgrade.webp",
    "/images/solutions/root-solutions/solution-condominiums-project-estate-integration.webp",
    "/images/solutions/root-solutions/solution-healthcare-healthcare-path-hostel.webp",
    "/images/solutions/root-solutions/solution-healthcare-healthcare-path-nursing.webp",
    "/images/solutions/root-solutions/solution-institutions-project-religious.webp",
    "/images/solutions/root-solutions/solution-institutions.webp",
    "/images/resources/resources-knowledge-base-singapore-mobile.webp",
    "/images/solutions/residential/landed-home-multiple-entry-points-singapore.webp",
    "/images/wee-meng-akuvox-summit-2024.jpg"
]

logo_path = os.path.join(repo_root, "images/securevision-logo-blue.png")

if not os.path.exists(logo_path):
    print("ABORTING: /images/securevision-logo-blue.png NOT FOUND.")
    exit(1)

print("Pre-deletion check passed. /images/securevision-logo-blue.png is present.")

freed_bytes = 0
deleted_count = 0

for f in files_to_delete:
    path = os.path.join(repo_root, f.lstrip('/'))
    if os.path.exists(path):
        size = os.path.getsize(path)
        try:
            os.remove(path)
            freed_bytes += size
            deleted_count += 1
            print(f"Deleted: {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")

freed_mb = freed_bytes / (1024 * 1024)

print("\n--- SUMMARY ---")
print(f"Total files deleted: {deleted_count}")
print(f"Total disk space freed: {freed_mb:.2f} MB")

if os.path.exists(logo_path):
    print("Post-deletion confirmation: /images/securevision-logo-blue.png STILL EXISTS.")
else:
    print("ERROR: /images/securevision-logo-blue.png is MISSING after deletion!")
