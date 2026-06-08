import os
from bs4 import BeautifulSoup

INSIGHTS_DIR = r"C:\Projects\SV-Build\insights"

REPLACEMENTS = {
    "how-burglar-alarm-works.html": "A burglar alarm has five core components working together. Knowing each one helps you choose the right system and manage it confidently in your Singapore home.",
    "how-ip-cctv-works.html": "Six components work between the camera and your footage. Knowing each one helps you spot a poorly specified IP CCTV system before it is installed in Singapore.",
    "security-system-refresh.html": "Is your security system still adequate for your current site? Learn when a full refresh is warranted and what a proper site survey covers in Singapore.",
    "upgrade-condo-intercom.html": "Ageing intercoms are the most deferred maintenance issue in Singapore condos. Learn when deferral stops being practical and what a modern upgrade involves.",
    "how-to-choose-auto-gate-motor.html": "The wrong motor for your gate type and usage pattern means a breakdown within five years. Learn how to select the right auto gate motor for your Singapore home.",
    "wifi-remote-control-auto-gate.html": "Most Singapore auto gate motors can be upgraded to WiFi control without replacing the motor. Learn how the Tuya module works and what the upgrade involves."
}

def update_descriptions():
    for filename, new_desc in REPLACEMENTS.items():
        fpath = os.path.join(INSIGHTS_DIR, filename)
        if not os.path.exists(fpath):
            print(f"Skipping {filename}, file not found.")
            continue
            
        with open(fpath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            
        desc_tag = soup.find("meta", {"name": "description"})
        if not desc_tag:
            desc_tag = soup.find("meta", {"name": "Description"})
        if desc_tag:
            desc_tag["content"] = new_desc
            
        og_desc = soup.find("meta", {"property": "og:description"})
        if og_desc:
            og_desc["content"] = new_desc
            
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
    print(f"Updated meta descriptions for {len(REPLACEMENTS)} flagged files.")

if __name__ == "__main__":
    update_descriptions()
