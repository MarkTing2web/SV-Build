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
        img = img.convert('RGB')
        
        src_w, src_h = img.size
        target_w, target_h = int(width), int(height)
        src_ratio = src_w / src_h
        target_ratio = target_w / target_h
        
        if src_ratio > target_ratio:
            # Wider than target — crop sides
            new_w = int(src_h * target_ratio)
            left = (src_w - new_w) // 2
            img = img.crop((left, 0, left + new_w, src_h))
        else:
            # Taller than target — crop top/bottom
            new_h = int(src_w / target_ratio)
            top = (src_h - new_h) // 2
            img = img.crop((0, top, src_w, top + new_h))
            
        img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        img.save(dest_path, "WEBP", quality=85)
        print(f"Successfully saved to {dest_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 5:
        process_image(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: process_image.py <src_path> <dest_name> <width> <height>")
