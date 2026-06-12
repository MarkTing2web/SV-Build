from PIL import Image, ImageOps
import os

def crop_and_resize(src, dest, w, h):
    img = Image.open(src)
    img = ImageOps.fit(img, (w, h), Image.Resampling.LANCZOS, bleed=0.0, centering=(0.5, 0.5))
    img.save(dest, format="WEBP", quality=95)
    print(f"Fixed {dest}")

base_dir = r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\dc6f1290-775d-4de8-9bce-fd9527c39650"
target_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights"

images = [
    ("comm_paths_feature_1781255264815.png", "alarm-communication-paths-feature.webp", 640, 360),
    ("comm_paths_bank_1781255497625.png", "alarm-communication-paths-bank.webp", 320, 240),
    ("comm_paths_dual_path_1781255558941.png", "alarm-communication-paths-dual-path.webp", 320, 240),
    ("internet_cut_feature_1781256029604.png", "alarm-internet-cut-feature.webp", 640, 360),
    ("internet_cut_siren_1781256156577.png", "alarm-internet-cut-siren.webp", 320, 240),
    ("internet_cut_cellular_1781256235128.png", "alarm-internet-cut-cellular.webp", 320, 240)
]

for src_name, dest_name, w, h in images:
    src_path = os.path.join(base_dir, src_name)
    dest_path = os.path.join(target_dir, dest_name)
    if os.path.exists(src_path):
        crop_and_resize(src_path, dest_path, w, h)
    else:
        print(f"Could not find {src_path}")
