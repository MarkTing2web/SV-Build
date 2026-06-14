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

# Expecting arguments: prefix1 out_name1 width1 height1 prefix2 out_name2 width2 height2 ...
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
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        img.save(out_path, "WEBP", quality=85)
        print(f"Saved {out_name}")
    else:
        print(f"Could not find artifact for {prefix}")
