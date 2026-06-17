import os
import base64
import anthropic

folder = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\resources\guides\cctv"
output_file = r"d:\Ler Wee Meng\Project-Web\SV-Build\_ai\cctv-image-descriptions.md"

client = anthropic.Anthropic()

if not os.path.exists(folder):
    print(f"FOLDER NOT FOUND: {folder}")
    # Check what guide folders exist
    parent = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\resources\guides"
    if os.path.exists(parent):
        print(f"\nAvailable folders in {parent}:")
        for item in sorted(os.listdir(parent)):
            print(f"  {item}")
    exit()

files = sorted([
    f for f in os.listdir(folder)
    if f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png'))
])

print(f"Folder: {folder}")
print(f"Total images: {len(files)}")
print()

lines = []
lines.append("# CCTV Guide Image Descriptions")
lines.append(f"## {len(files)} images described")
lines.append(f"## Folder: {folder}")
lines.append("")
lines.append("| Filename | Size (bytes) | Description |")
lines.append("|---|---|---|")

for fname in files:
    fpath = os.path.join(folder, fname)
    fsize = os.path.getsize(fpath)

    with open(fpath, "rb") as f:
        img_data = base64.standard_b64encode(f.read()).decode("utf-8")

    # Detect media type
    ext = fname.lower().split('.')[-1]
    media_map = {'webp': 'image/webp', 'jpg': 'image/jpeg',
                 'jpeg': 'image/jpeg', 'png': 'image/png'}
    media_type = media_map.get(ext, 'image/jpeg')

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=150,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": media_type,
                        "data": img_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Describe what is physically visible in this image in one plain sentence. Be specific about objects, colours, setting and any text visible. No interpretation — just what you can see."
                }
            ],
        }]
    )

    description = response.content[0].text.strip()
    lines.append(f"| {fname} | {fsize:,} | {description} |")
    print(f"✅ {fname}")
    print(f"   {description}")
    print()

os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\nDone. Saved to: {output_file}")
