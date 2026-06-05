import os
from collections import defaultdict

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
images_dir = os.path.join(repo_root, "images")
img_exts = ('.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg')

all_images = []

for root, _, files in os.walk(images_dir):
    for f in files:
        if f.lower().endswith(img_exts):
            full_path = os.path.join(root, f)
            rel_path = '/' + os.path.relpath(full_path, repo_root).replace('\\', '/')
            size = os.path.getsize(full_path)
            all_images.append({'path': rel_path, 'size': size})

total_scanned = len(all_images)
oversized = [img for img in all_images if img['size'] > 200 * 1024]
acceptable = total_scanned - len(oversized)

top_10 = sorted(all_images, key=lambda x: x['size'], reverse=True)[:10]

report = [
    "### Section A: Summary",
    f"- Total images scanned: {total_scanned}",
    f"- Total under 200KB (acceptable): {acceptable}",
    f"- Total over 200KB (needs attention): {len(oversized)}",
    "",
    "**Largest 10 files by size:**"
]

for img in top_10:
    report.append(f"- `{img['path']}` - {img['size']/1024:.1f} KB")

report.append("")
report.append("### Section B: Oversized images — over 200KB")

if not oversized:
    report.append("None found.")
else:
    grouped = defaultdict(list)
    for img in oversized:
        folder = os.path.dirname(img['path']) + '/'
        grouped[folder].append(img)
        
    for folder in sorted(grouped.keys()):
        report.append(f"\n#### {folder}")
        report.append("| File Path | File Size | Image Type | Priority |")
        report.append("|---|---|---|---|")
        
        folder_imgs = sorted(grouped[folder], key=lambda x: x['size'], reverse=True)
        
        for img in folder_imgs:
            ext = os.path.splitext(img['path'])[1].upper()
            size_kb = img['size'] / 1024
            
            if size_kb > 500:
                priority = "🔴 CRITICAL"
            else:
                priority = "🟡 LARGE"
                
            report.append(f"| `{os.path.basename(img['path'])}` | {size_kb:.1f} KB | {ext} | {priority} |")

report.append("")
report.append("### Section C: Confirmation")
if acceptable == total_scanned:
    report.append("All images are under 200KB.")
else:
    report.append("All other images are under 200KB.")

report_path = os.path.join(repo_root, "_ai", "image-size-audit.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print(f"Report saved to _ai/image-size-audit.md")
print(f"Total: {total_scanned}, Oversized: {len(oversized)}")
