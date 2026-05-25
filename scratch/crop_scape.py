from PIL import Image
import os

source_path = r'c:\Projects\SV-Build\images\portfolio\commercial\scape-hero.webp'
mobile_path = r'c:\Projects\SV-Build\images\portfolio\commercial\scape-mobile.webp'
rel_path = r'c:\Projects\SV-Build\images\portfolio\commercial\scape-rel.webp'

img = Image.open(source_path)

def center_crop(img, target_w, target_h):
    w, h = img.size
    target_aspect = target_w / target_h
    aspect = w / h
    
    if aspect > target_aspect:
        # Image is wider than target aspect
        new_w = int(h * target_aspect)
        left = (w - new_w) // 2
        right = left + new_w
        top = 0
        bottom = h
    else:
        # Image is taller than target aspect
        new_h = int(w / target_aspect)
        top = (h - new_h) // 2
        bottom = top + new_h
        left = 0
        right = w
        
    cropped = img.crop((left, top, right, bottom))
    return cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Generate scape-mobile.webp
mobile_img = center_crop(img, 1080, 1920)
mobile_img.save(mobile_path, 'WEBP', quality=82)
print(f"Saved {mobile_path}")

# Generate scape-rel.webp
rel_img = center_crop(img, 960, 540)
rel_img.save(rel_path, 'WEBP', quality=85)
print(f"Saved {rel_path}")
