import sys
import os
from PIL import Image

def process_image(src_path, dest_name, width, height):
    base_dir = r"c:\Projects\SV-Build\images\insights"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    dest_path = os.path.join(base_dir, dest_name)
    
    try:
        img = Image.open(src_path)
        img = img.resize((int(width), int(height)), Image.Resampling.LANCZOS)
        img.save(dest_path, "WEBP", quality=85)
        print(f"Successfully saved to {dest_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 5:
        process_image(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: process_image.py <src_path> <dest_name> <width> <height>")
