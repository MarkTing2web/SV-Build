import os
import re

files = [
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

attributes = """
           data-desc-premises="The cameras you saw in this project are part of a detection layer designed around how a landed home is actually approached — front gate, side access, driveway, and rear. See how we design CCTV and alarm systems for homes like yours."
           data-desc-entry-access="A video door phone at the gate, a motorised auto gate, and a mobile app that lets you open the gate from anywhere — this is what modern residential access control looks like. What you just read is a real example of how we install it."
           data-desc-vehicle-lpr="Auto gates, sliding gates, and remote entry — secure your driveway and control vehicle access to your home."
           data-desc-ip-telephony="Internal calling between floors and outbuildings without relying on mobile phones — useful in larger homes where the helper's quarters or upper level needs to stay connected to the main living area."
           data-desc-network="Security cameras, intercoms, and smart devices all run on IP — which means the network is the foundation everything else depends on. We design the cabling and WiFi layout alongside the security installation so nothing underperforms after handover."
"""

base_dir = r"c:\Projects\SV-Build"
changed_count = 0

for file in files:
    filepath = os.path.join(base_dir, file.replace('/', '\\'))
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'data-desc-ip-telephony' in content:
            print(f"Skipped {file} - already updated")
            continue
            
        old_lpr = 'data-desc-vehicle-lpr="Auto gates, sliding gates, and remote entry — secure your driveway and control vehicle access to your home.">'
        new_lpr = attributes.strip('\n') + ">"
        
        if old_lpr in content:
            new_content = content.replace(old_lpr, new_lpr)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            changed_count += 1
            print(f"Updated {file}")
        else:
            m = re.search(r'\s*data-desc-vehicle-lpr="[^"]*">', content)
            if m:
                new_content = content[:m.start()] + "\n" + attributes.strip('\n') + ">" + content[m.end():]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                changed_count += 1
                print(f"Updated {file} via regex")
            else:
                print(f"Failed to find target in {file}")
    else:
        print(f"Error: {file} not found")

print(f"\nTotal files updated: {changed_count}")
