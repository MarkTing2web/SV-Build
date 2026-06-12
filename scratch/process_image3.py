from PIL import Image
import os

img_path = r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\dc6f1290-775d-4de8-9bce-fd9527c39650\comm_paths_dual_path_1781255558941.png"
out_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\alarm-communication-paths-dual-path.webp"

os.makedirs(os.path.dirname(out_path), exist_ok=True)
img = Image.open(img_path)
img = img.resize((320, 240), Image.Resampling.LANCZOS)
img.save(out_path, format="WEBP")
print("Saved dual path image to", out_path)
