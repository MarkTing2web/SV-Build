import os
from PIL import Image

src = r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\797eb192-249a-4a9f-8875-9042f23c9a60\cctv_storage_square_1781832292088.png"
dst = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\solutions\root-solutions\solution-improve-cctv-visibility-cctv-storage-square.webp"

try:
    with Image.open(src) as img:
        img.save(dst, "WEBP", quality=85)
    print("Image successfully converted and saved.")
except Exception as e:
    print(f"Error: {e}")
