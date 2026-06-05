import os

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"

required_files = [
    "/images/securevision-logo-blue.png",
    "/images/ler-wee-meng-bio.webp",
    "/images/og-default.jpg"
]

files_to_delete = [
    # GROUP 1
    "/images/portfolio/condominiums/lviv-condo-facade.webp",
    "/images/portfolio/condominiums/lviv-condo-front-facade-intercom-access-control.png",
    "/images/portfolio/condominiums/lviv-front-gate.png",
    "/images/portfolio/condominiums/light-at-cairnhill-front-facade-full.webp",
    "/images/portfolio/condominiums/light-at-cairnhill-entrance.webp",
    "/images/portfolio/condominiums/light-at-cairnhill-front-facade-hero.webp",
    "/images/portfolio/condominiums/light-condo-gate.webp",
    "/images/portfolio/condominiums/light-condo-main-hero.webp",
    # GROUP 2
    "/images/wee-meng-profile.jpg",
    "/images/ler-wee-meng-bio.jpeg",
    "/images/auto-gate-motor-cover.jpg",
    "/images/rackmount-nvr-cover.jpg",
    "/images/home-security-cost-cover.jpg",
    "/images/how-ip-cctv-works-cover.jpg",
    "/images/standalone-door-access-cover.jpg",
    "/images/contact-hero-v2.png",
    "/images/intercom-assessment-cta.png",
    "/images/portfolio-cta.png",
    "/images/resources-cta.png",
    "/images/securevision-team-cta.png",
    "/images/home/cta-technician-walkthrough-singapore.png",
    # GROUP 3
    "/images/portfolio/commercial/altitudex-sentosa-card.webp",
    "/images/portfolio/commercial/catholic-centre-card.webp",
    "/images/portfolio/commercial/em-engineering-at-jalan-kilang-card.webp",
    "/images/portfolio/commercial/hilton-singapore-orchard-card.webp",
    "/images/portfolio/commercial/st-engineering-mobility-card.webp",
    "/images/portfolio/condominiums/high-oak-condominium-card.webp",
    "/images/portfolio/condominiums/hillview-park-condo-card.webp",
    "/images/portfolio/condominiums/rezi32-card.webp",
    "/images/portfolio/condominiums/suites-cairnhill-card.webp",
    "/images/portfolio/condominiums/the-clearwater-card.webp",
    "/images/portfolio/data-centres/fort-data-centre-card.webp",
    "/images/portfolio/industrial/cogent-1-logistics-hub-card.webp",
    "/images/portfolio/industrial/cyrus-tech-at-loyang-card.webp",
    "/images/portfolio/industrial/mitsubishi-elevator-singapore-card.webp",
    "/images/portfolio/industrial/multibase-construction-card.webp",
    "/images/portfolio/industrial/smartflex-at-tampines-card.webp",
    "/images/portfolio/industrial/st-microelectronics-loyang-card.webp",
    "/images/portfolio/industrial/sta-inspection-centre-sin-ming-card.webp",
    "/images/portfolio/institutions/changi-airside-card.webp",
    "/images/portfolio/institutions/cpf-maxwell-card.webp",
    "/images/portfolio/institutions/das-learning-centre-card.webp",
    "/images/portfolio/institutions/my-world-preschool-card.webp",
    "/images/portfolio/institutions/st-francis-xavier-retreat-centre-card.webp",
    "/images/portfolio/managed-living/nursing-hostel-at-jln-seh-chuan-card.webp",
    "/images/portfolio/residential/dyson-8-card.webp",
    "/images/portfolio/residential/shelford-card.webp",
    # GROUP 4
    "/images/solutions/hero-solutions/commercial-security-systems-hero-rel.webp",
    "/images/solutions/hero-solutions/condominium-security-systems-hero-rel.webp",
    "/images/solutions/hero-solutions/data-centre-security-systems-hero-rel.webp",
    "/images/solutions/hero-solutions/industrial-security-systems-hero-rel.webp",
    "/images/solutions/hero-solutions/institutions-security-systems-hero-rel.webp",
    "/images/solutions/hero-solutions/reduce-manpower-with-technology-rel.webp",
    "/images/solutions/hero-solutions/solution-condominiums-managing-agents-hero-rel.webp",
    "/images/solutions/hero-solutions/solution-condominiums-mcst-hero-rel.webp",
    "/images/solutions/hero-solutions/solution-healthcare-daycare-hero-rel.webp",
    "/images/solutions/hero-solutions/solution-institutions-community-hero-rel.webp",
    "/images/solutions/hero-solutions/solution-managed-living-co-living-hero-rel.webp",
    "/images/solutions/hero-solutions/solutions-hub-singapore-rel.webp"
]

# CHECK REQUIRED FILES
all_exist = True
for f in required_files:
    path = os.path.join(repo_root, f.lstrip('/'))
    if not os.path.exists(path):
        print(f"ABORTING: Required file missing: {f}")
        all_exist = False

if not all_exist:
    exit(1)

print("Pre-deletion check passed. All 3 required files confirmed present.")

# DELETE FILES
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
    else:
        print(f"Skipped (not found): {f}")

freed_mb = freed_bytes / (1024 * 1024)

print("\n--- SUMMARY ---")
print(f"Total files deleted: {deleted_count}")
print(f"Total disk space freed: {freed_mb:.2f} MB")

# VERIFY LOGO REMAINS
logo_path = os.path.join(repo_root, "/images/securevision-logo-blue.png".lstrip('/'))
if os.path.exists(logo_path):
    print("Post-deletion confirmation: /images/securevision-logo-blue.png STILL EXISTS.")
else:
    print("ERROR: /images/securevision-logo-blue.png is MISSING after deletion!")
