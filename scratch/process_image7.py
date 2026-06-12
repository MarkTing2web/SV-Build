from PIL import Image, ImageOps
import os

def crop_and_resize(src, dest, w, h):
    img = Image.open(src)
    img = ImageOps.fit(img, (w, h), Image.Resampling.LANCZOS, bleed=0.0, centering=(0.5, 0.5))
    img.save(dest, format="WEBP", quality=95)
    print(f"Fixed {dest}")

src_path = r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\dc6f1290-775d-4de8-9bce-fd9527c39650\internet_cut_cellular_v2_1781256963586.png"
dest_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\alarm-internet-cut-cellular.webp"

os.makedirs(os.path.dirname(dest_path), exist_ok=True)
crop_and_resize(src_path, dest_path, 320, 240)
