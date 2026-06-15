from PIL import Image
import os
import glob

insights_dir = r"C:\Projects\SV-Build\images\insights"

# Get all article slugs from HTML files
html_files = glob.glob(r"C:\Projects\SV-Build\insights\*.html")
slugs = []
for f in html_files:
    basename = os.path.basename(f).replace('.html', '')
    if basename != 'index':
        slugs.append(basename)

og_size = (1200, 630)
created = []
skipped = []
missing_feature = []

for slug in sorted(slugs):
    og_path = os.path.join(insights_dir, f"{slug}-feature-og.webp")
    feature_path = os.path.join(insights_dir, f"{slug}-feature.webp")

    # Skip if OG already exists and is non-zero
    if os.path.exists(og_path) and os.path.getsize(og_path) > 0:
        skipped.append(slug)
        continue

    # Check feature image exists and is non-zero
    if not os.path.exists(feature_path) or os.path.getsize(feature_path) == 0:
        missing_feature.append(slug)
        continue

    # Create OG image from feature — centre crop to 1200x630
    with Image.open(feature_path) as img:
        img = img.convert('RGB')
        # Calculate crop box for centre crop
        src_w, src_h = img.size
        target_w, target_h = og_size
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
        img = img.resize(og_size, Image.LANCZOS)
        img.save(og_path, 'WEBP', quality=85)
        created.append(slug)

print(f"OG images already existed (skipped): {len(skipped)}")
print(f"OG images created from feature:      {len(created)}")
print(f"Feature image missing (cannot create OG): {len(missing_feature)}")
print()
if created:
    print("CREATED:")
    for s in created:
        print(f"  {s}-feature-og.webp")
if missing_feature:
    print("CANNOT CREATE — feature image missing or 0 bytes:")
    for s in missing_feature:
        print(f"  {s}-feature.webp")
