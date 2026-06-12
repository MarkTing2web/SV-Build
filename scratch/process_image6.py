from PIL import Image
import os

img_path = r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\dc6f1290-775d-4de8-9bce-fd9527c39650\internet_cut_cellular_1781256235128.png"
out_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\alarm-internet-cut-cellular.webp"

os.makedirs(os.path.dirname(out_path), exist_ok=True)
img = Image.open(img_path)
img = img.resize((320, 240), Image.Resampling.LANCZOS)
img.save(out_path, format="WEBP")
print("Saved internet cut cellular image to", out_path)
