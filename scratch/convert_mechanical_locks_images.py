from PIL import Image, ImageOps
import os

images = [
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\mechanical_locks_not_enough_feature_1781328193265.png",
     r"C:\Projects\SV-Build\images\insights\mechanical-locks-not-enough-feature.webp", (640, 360)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\mechanical_locks_not_enough_audit_1781328203491.png",
     r"C:\Projects\SV-Build\images\insights\mechanical-locks-not-enough-audit.webp", (320, 240)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\mechanical_locks_not_enough_digital_lock_1781328214051.png",
     r"C:\Projects\SV-Build\images\insights\mechanical-locks-not-enough-digital-lock.webp", (320, 240))
]

for src, dst, size in images:
    if os.path.exists(src):
        img = Image.open(src)
        img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        img.save(dst, format="WEBP")
        print(f"Saved {dst}")
    else:
        print(f"Error: {src} not found")
