from PIL import Image
import os

images_dir = r"C:\Projects\SV-Build\images\insights"

files = [
    "modern-detectors-feature.webp",
    "alarm-upgrade-or-replace-feature.webp",
    "lpr-vs-rfid-condo-feature.webp",
    "cctv-retail-analytics-feature.webp"
]

for filename in files:
    path = os.path.join(images_dir, filename)
    if not os.path.exists(path):
        print(f"File not found: {filename}")
        continue
        
    try:
        with Image.open(path) as img:
            # Get current width and height
            w, h = img.size
            print(f"Processing {filename}: original size = {w}x{h}")
            
            # 1. Stretch back to square (restoring the 1:1 aspect ratio of the original subject)
            square_img = img.resize((w, w), Image.Resampling.LANCZOS)
            
            # 2. Center crop to 16:9 (which matches the target 1.777 ratio)
            target_h = int(w * 9 / 16)
            top = (w - target_h) // 2
            cropped_img = square_img.crop((0, top, w, top + target_h))
            
            # 3. Resize to 640x360 (or keep the width)
            final_img = cropped_img.resize((640, 360), Image.Resampling.LANCZOS)
            
            # Save it back
            final_img.save(path, "WEBP", quality=85)
            print(f"  Successfully un-squished and saved: {filename}")
    except Exception as e:
        print(f"  Error processing {filename}: {e}")
