from PIL import Image, ImageOps
import os

images = [
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\assessment_10_things_feature_1781283580072.png",
     r"C:\Projects\SV-Build\images\insights\security-assessment-10-things-feature.webp", (640, 360)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\assessment_10_things_blind_spot_1781283714681.png",
     r"C:\Projects\SV-Build\images\insights\security-assessment-10-things-blind-spot.webp", (320, 240)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\assessment_10_things_sliding_door_1781283815234.png",
     r"C:\Projects\SV-Build\images\insights\security-assessment-10-things-sliding-door.webp", (320, 240))
]

for src, dst, size in images:
    if os.path.exists(src):
        img = Image.open(src)
        img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        img.save(dst, format="WEBP")
        print(f"Saved {dst}")
    else:
        print(f"Error: {src} not found")
