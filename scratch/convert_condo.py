import os
import glob
import sys
from PIL import Image

ARTIFACTS_DIR = r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa"
TARGET_DIR = r"C:\Projects\SV-Build\images\insights"

def find_latest(prefix):
    files = glob.glob(os.path.join(ARTIFACTS_DIR, f"{prefix}_*.png"))
    if not files: return None
    return max(files, key=os.path.getmtime)

args = sys.argv[1:]
if len(args) % 4 != 0:
    print("Invalid number of arguments")
    sys.exit(1)

for i in range(0, len(args), 4):
    prefix = args[i]
    out_name = args[i+1]
    width = int(args[i+2])
    height = int(args[i+3])
    
    img_path = find_latest(prefix)
    if img_path:
        out_path = os.path.join(TARGET_DIR, out_name)
        img = Image.open(img_path)
        # Center crop and resize
        target_ratio = width / height
        img_ratio = img.width / img.height
        
        if img_ratio > target_ratio:
            new_width = int(img.height * target_ratio)
            left = (img.width - new_width) / 2
            img = img.crop((left, 0, left + new_width, img.height))
        elif img_ratio < target_ratio:
            new_height = int(img.width / target_ratio)
            top = (img.height - new_height) / 2
            img = img.crop((0, top, img.width, top + new_height))
            
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        img.save(out_path, "WEBP", quality=85)
        
        # Check size
        size_kb = os.path.getsize(out_path) / 1024
        print(f"Saved {out_name} ({size_kb:.1f} KB)")
    else:
        print(f"Could not find artifact for {prefix}")
