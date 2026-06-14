from PIL import Image, ImageOps
import os

images = [
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\condo_intercom_upgrade_feature_1781327421348.png",
     r"C:\Projects\SV-Build\images\insights\condo-intercom-upgrade-feature.webp", (640, 360)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\condo_intercom_upgrade_mobile_1781327432838.png",
     r"C:\Projects\SV-Build\images\insights\condo-intercom-upgrade-mobile.webp", (320, 240)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\condo_intercom_upgrade_modern_1781327444940.png",
     r"C:\Projects\SV-Build\images\insights\condo-intercom-upgrade-modern.webp", (320, 240))
]

for src, dst, size in images:
    if os.path.exists(src):
        img = Image.open(src)
        img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        img.save(dst, format="WEBP")
        print(f"Saved {dst}")
    else:
        print(f"Error: {src} not found")
