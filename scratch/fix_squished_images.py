from PIL import Image, ImageOps
import os

images = [
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\installer_leaves_feature_1781282443257.png",
     r"C:\Projects\SV-Build\images\insights\installer-leaves-feature.webp", (640, 360)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\installer_leaves_keypad_1781282509374.png",
     r"C:\Projects\SV-Build\images\insights\installer-leaves-keypad-fault.webp", (320, 240)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\installer_leaves_documentation_1781282574961.png",
     r"C:\Projects\SV-Build\images\insights\installer-leaves-documentation.webp", (320, 240)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\network_systems_feature_1781281936771.png",
     r"C:\Projects\SV-Build\images\insights\network-security-systems-feature.webp", (640, 360)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\network_systems_switch_1781281969293.png",
     r"C:\Projects\SV-Build\images\insights\network-security-systems-switch.webp", (320, 240)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\network_systems_remote_1781282000012.png",
     r"C:\Projects\SV-Build\images\insights\network-security-systems-remote.webp", (320, 240))
]

for src, dst, size in images:
    if os.path.exists(src):
        img = Image.open(src)
        img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        img.save(dst, format="WEBP")
        print(f"Saved {dst}")
    else:
        print(f"Error: {src} not found")
