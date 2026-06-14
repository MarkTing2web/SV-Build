from PIL import Image, ImageOps
import os

images = [
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\access_control_multi_door_feature_1781328608511.png",
     r"C:\Projects\SV-Build\images\insights\access-control-multi-door-feature.webp", (640, 360)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\access_control_multi_door_credentials_1781328620634.png",
     r"C:\Projects\SV-Build\images\insights\access-control-multi-door-credentials.webp", (320, 240))
]

for src, dst, size in images:
    if os.path.exists(src):
        img = Image.open(src)
        img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        img.save(dst, format="WEBP")
        print(f"Saved {dst}")
    else:
        print(f"Error: {src} not found")
