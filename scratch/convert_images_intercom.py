import os
from PIL import Image

images = [
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\797eb192-249a-4a9f-8875-9042f23c9a60\qr_visitor_access_1781831806033.png", 
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\solutions\root-solutions\solution-upgrade-intercom-system-qr-visitor-access.webp"),
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\797eb192-249a-4a9f-8875-9042f23c9a60\cabling_reuse_1781831816451.png", 
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\solutions\root-solutions\solution-upgrade-intercom-system-cabling-reuse.webp")
]

for src, dst in images:
    try:
        with Image.open(src) as img:
            img.save(dst, "WEBP", quality=85)
        print(f"Converted and saved: {os.path.basename(dst)}")
    except Exception as e:
        print(f"Error on {os.path.basename(src)}: {e}")
