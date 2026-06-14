from PIL import Image, ImageOps
import os

images = [
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\break_in_review_feature_1781282973932.png",
     r"C:\Projects\SV-Build\images\insights\break-in-nearby-security-review-feature.webp", (640, 360)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\break_in_review_backyard_1781283139039.png",
     r"C:\Projects\SV-Build\images\insights\break-in-nearby-security-review-backyard.webp", (320, 240)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\break_in_review_camera_1781283191396.png",
     r"C:\Projects\SV-Build\images\insights\break-in-nearby-security-review-ai-camera.webp", (320, 240))
]

for src, dst, size in images:
    if os.path.exists(src):
        img = Image.open(src)
        img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        img.save(dst, format="WEBP")
        print(f"Saved {dst}")
    else:
        print(f"Error: {src} not found")
