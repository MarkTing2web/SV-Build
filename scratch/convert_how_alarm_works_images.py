from PIL import Image, ImageOps
import os

images = [
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\how_alarm_works_feature_1781284154856.png",
     r"C:\Projects\SV-Build\images\insights\how-alarm-works-feature.webp", (640, 360)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\how_alarm_works_panel_1781284322462.png",
     r"C:\Projects\SV-Build\images\insights\how-alarm-works-panel.webp", (320, 240)),
    (r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa\how_alarm_works_keypad_1781284385762.png",
     r"C:\Projects\SV-Build\images\insights\how-alarm-works-keypad.webp", (320, 240))
]

for src, dst, size in images:
    if os.path.exists(src):
        img = Image.open(src)
        img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        img.save(dst, format="WEBP")
        print(f"Saved {dst}")
    else:
        print(f"Error: {src} not found")
