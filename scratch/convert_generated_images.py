from PIL import Image
import os

images = [
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\repair_replace_feature_1781281359475.png",
     r"C:\Projects\SV-Build\images\insights\system-repair-or-replace-feature.webp", (640, 360)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\repair_replace_selective_1781281397283.png",
     r"C:\Projects\SV-Build\images\insights\system-repair-or-replace-selective.webp", (320, 240)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\repair_replace_comparison_1781281455236.png",
     r"C:\Projects\SV-Build\images\insights\system-repair-or-replace-comparison.webp", (320, 240))
]

for src, dst, size in images:
    if os.path.exists(src):
        img = Image.open(src)
        img = img.resize(size)
        img.save(dst, format="WEBP")
        print(f"Saved {dst}")
    else:
        print(f"Error: {src} not found")
