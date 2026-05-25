import os

files = [
    "portfolio/condominiums/clearwater-access-salto-partnership.html",
    "portfolio/condominiums/clearwater-cctv-upgrade.html",
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html",
    "portfolio/condominiums/high-oak-condominium-cctv.html",
    "portfolio/condominiums/hillview-park-cctv-upgrade.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/mergui-mansions-novena-condo.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/rezi-3two-condo.html",
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html"
]

attributes = """
         data-desc-premises="What you saw in this project — cameras covering every blind spot, colour at night, no dead zones — is what a properly specified CCTV system looks like. See how we design premises security for condominiums."
         data-desc-entry-access="Resident access that works without a queue at the guardhouse. Video intercom at the lobby, mobile app release from anywhere, and lift control that keeps common floors restricted — this is the access layer behind what you just read."
         data-desc-vehicle-lpr="Seamless vehicle entry without a barrier queue. LPR reads the plate, the barrier lifts, and the system logs the time — whether it is a resident returning home or a visitor checking in. See how we implement vehicle management for condominium estates."
         data-desc-network="Every system in this project runs on IP — and a poorly designed network is the most common reason security systems underperform. We plan the switching, cabling, and VLAN architecture so the infrastructure never becomes the weak point."
         data-desc-platform="When every system feeds into one platform, the management office sees the full picture — access logs, CCTV events, visitor records, and resident communications in one place. This is what unified estate management looks like in practice."
"""

base_dir = r"c:\Projects\SV-Build"
changed_count = 0

for file in files:
    filepath = os.path.join(base_dir, file.replace('/', '\\'))
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        target = 'data-intro="">'
        replacement = f'data-intro="">{attributes.rstrip()}'
        
        # Ensure we don't duplicate
        if target in content and 'data-desc-premises=' not in content:
            new_content = content.replace(target, f'data-intro="">\n{attributes.strip()}\n    >')
            # wait, target has closing >
            # let's be careful. `data-intro="">` closing the tag.
            # actually better to replace `data-intro="">` with `data-intro=""\n         data-desc... >`
            new_content = content.replace('data-intro="">', f'data-intro=""\n{attributes.strip()}>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            changed_count += 1
            print(f"Updated {file}")
        elif 'data-desc-premises=' in content:
            print(f"Skipped {file} - already has attributes")
        else:
            print(f"Skipped {file} - data-intro=\">\" not found")

print(f"\nTotal files updated: {changed_count}")
