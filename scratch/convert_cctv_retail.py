import os
import glob
from PIL import Image

ARTIFACTS_DIR = r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa"
TARGET_DIR = r"C:\Projects\SV-Build\images\insights"

def find_latest(prefix):
    files = glob.glob(os.path.join(ARTIFACTS_DIR, f"{prefix}_*.png"))
    if not files: return None
    return max(files, key=os.path.getmtime)

tasks = [
    ("cctv_retail_analytics_feature", "cctv-retail-analytics-feature.webp", (640, 360)),
    ("cctv_retail_analytics_heatmap", "cctv-retail-analytics-heatmap.webp", (320, 240)),
    ("cctv_retail_analytics_dashboard", "cctv-retail-analytics-dashboard.webp", (320, 240)),
]

for prefix, out_name, size in tasks:
    img_path = find_latest(prefix)
    if img_path:
        out_path = os.path.join(TARGET_DIR, out_name)
        img = Image.open(img_path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        img.save(out_path, "WEBP", quality=85)
        print(f"Saved {out_name}")
    else:
        print(f"Could not find artifact for {prefix}")
