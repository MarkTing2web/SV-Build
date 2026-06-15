import os
import re
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

insights_dir = r"C:\Projects\SV-Build\insights"
images_dir = r"C:\Projects\SV-Build\images\insights"
base_url = "https://www.securevision.com.sg/images/insights/"

html_files = glob.glob(os.path.join(insights_dir, "*.html"))
updated = []
skipped_no_og = []
skipped_index = []

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    slug = filename.replace('.html', '')

    # Skip index.html
    if slug == 'index':
        skipped_index.append(slug)
        continue

    # Check OG file exists and is non-zero
    og_filename = f"{slug}-feature-og.webp"
    og_path = os.path.join(images_dir, og_filename)
    if not os.path.exists(og_path) or os.path.getsize(og_path) == 0:
        skipped_no_og.append(slug)
        print(f"SKIP (no valid OG file): {slug}")
        continue

    # Read HTML
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Replace og:image content — handle both attribute orders
    og_image_url = f"{base_url}{og_filename}"
    feature_url = f"{base_url}{slug}-feature.webp"

    # Replace in og:image meta tag
    content = re.sub(
        r'(property=["\']og:image["\'][^>]*content=["\'])([^"\']+)(["\'])',
        lambda m: m.group(1) + og_image_url + m.group(3),
        content
    )
    content = re.sub(
        r'(content=["\'])([^"\']+)(["\'][^>]*property=["\']og:image["\'])',
        lambda m: m.group(1) + og_image_url + m.group(3),
        content
    )

    # Replace in twitter:image meta tag
    content = re.sub(
        r'(name=["\']twitter:image["\'][^>]*content=["\'])([^"\']+)(["\'])',
        lambda m: m.group(1) + og_image_url + m.group(3),
        content
    )
    content = re.sub(
        r'(content=["\'])([^"\']+)(["\'][^>]*name=["\']twitter:image["\'])',
        lambda m: m.group(1) + og_image_url + m.group(3),
        content
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated.append(slug)
        print(f"UPDATED: {slug}")
    else:
        print(f"NO CHANGE: {slug} (tags may already use OG or not found)")

print()
print(f"Updated:              {len(updated)}")
print(f"Skipped (no OG file): {len(skipped_no_og)}")
print(f"Skipped (index):      {len(skipped_index)}")
if skipped_no_og:
    print("Articles with no valid OG file:")
    for s in skipped_no_og:
        print(f"  {s}")
