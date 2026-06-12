from PIL import Image
import os

img_path = r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\dc6f1290-775d-4de8-9bce-fd9527c39650\internet_cut_feature_1781256029604.png"
out_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\alarm-internet-cut-feature.webp"

os.makedirs(os.path.dirname(out_path), exist_ok=True)
img = Image.open(img_path)
img = img.resize((640, 360), Image.Resampling.LANCZOS)
img.save(out_path, format="WEBP")
print("Saved internet cut feature image to", out_path)
