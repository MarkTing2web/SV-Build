import sys
sys.stdout.reconfigure(encoding='utf-8')

from PIL import Image
import os
import glob

insights_dir = r"C:\Projects\SV-Build\images\insights"
html_dir = r"C:\Projects\SV-Build\insights"

# Get all article slugs from HTML files
slugs = []
for f in glob.glob(os.path.join(html_dir, "*.html")):
    basename = os.path.basename(f).replace('.html', '')
    if basename != 'index':
        slugs.append(basename)

created = []
skipped_exists = []
skipped_no_feature = []

for slug in sorted(slugs):
    og_path      = os.path.join(insights_dir, f"{slug}-feature-og.webp")
    feature_path = os.path.join(insights_dir, f"{slug}-feature.webp")

    # Skip if OG already exists AND is non-zero
    if os.path.exists(og_path) and os.path.getsize(og_path) > 0:
        skipped_exists.append(slug)
        continue

    # Skip if feature image does not exist or is 0 bytes
    if not os.path.exists(feature_path) or os.path.getsize(feature_path) == 0:
        skipped_no_feature.append(slug)
        print(f"SKIP (no valid feature): {slug}")
        continue

    # Generate OG from feature — centre crop to 1200x630
    try:
        with Image.open(feature_path) as img:
            img = img.convert('RGB')
            src_w, src_h = img.size
            target_w, target_h = 1200, 630
            src_ratio = src_w / src_h
            target_ratio = target_w / target_h
            if src_ratio > target_ratio:
                new_w = int(src_h * target_ratio)
                left = (src_w - new_w) // 2
                img = img.crop((left, 0, left + new_w, src_h))
            else:
                new_h = int(src_w / target_ratio)
                top = (src_h - new_h) // 2
                img = img.crop((0, top, src_w, top + new_h))
            img = img.resize((1200, 630), Image.LANCZOS)
            img.save(og_path, 'WEBP', quality=85)
            size = os.path.getsize(og_path)
            created.append((slug, size))
            print(f"CREATED: {slug}-feature-og.webp ({size:,} bytes)")
    except Exception as e:
        print(f"ERROR: {slug} — {e}")

print()
print(f"OG already existed (skipped):      {len(skipped_exists)}")
print(f"OG created from feature:           {len(created)}")
print(f"Skipped — no valid feature image:  {len(skipped_no_feature)}")
if skipped_no_feature:
    print("Slugs with no valid feature image:")
    for s in skipped_no_feature:
        print(f"  {s}")
