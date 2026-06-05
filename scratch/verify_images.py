import os

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
images_dir = os.path.join(repo_root, "images")

files_to_check = {
    "FILE 1: /resources/guides/cctv-guide.html": [
        "/images/resources/guides/cctv/cctv-legacy-analogue.webp",
        "/images/resources/guides/cctv/comp-integration-v3.webp",
        "/images/resources/guides/cctv/industrial-perimeter.webp",
        "/images/resources/guides/cctv/industrial-workforce.webp",
        "/images/resources/guides/cctv/project-factory.webp"
    ],
    "FILE 2: /resources/guides/auto-gate-guide.html": [
        "/images/resources/guides/autogate/homeowner-gate-app.webp",
        "/images/resources/guides/autogate/nice-barrier-condo.webp",
        "/images/resources/guides/autogate/photocell-safety-beam.webp",
        "/images/resources/guides/autogate/sliding-gate-track.webp",
        "/images/resources/guides/autogate/technician-greasing-rack.webp",
        "/images/resources/guides/autogate/technician-site-assessment.webp"
    ],
    "FILE 3: /solutions/healthcare.html": [
        "/images/solutions/solution-healthcare-cta.webp"
    ]
}

filename_map = {}
for root, dirs, files in os.walk(images_dir):
    for f in files:
        if f not in filename_map:
            filename_map[f] = []
        rel_path = '/' + os.path.relpath(os.path.join(root, f), repo_root).replace('\\', '/')
        filename_map[f].append(rel_path)

for file_section, images in files_to_check.items():
    print(file_section)
    for img_path in images:
        full_path = os.path.join(repo_root, img_path.lstrip('/\\').replace('/', os.sep))
        if os.path.exists(full_path):
            print(f"- {img_path} : FOUND")
        else:
            filename = os.path.basename(img_path)
            found_elsewhere = filename_map.get(filename, [])
            if found_elsewhere:
                print(f"- {img_path} : MISSING (Found instead at: {', '.join(found_elsewhere)})")
            else:
                print(f"- {img_path} : MISSING (File not found anywhere in /images/)")
    print()
