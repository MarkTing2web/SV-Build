import os
import base64
import anthropic

folder = r"C:\Projects\SV-Build\images\resources\guides\alarm"
output_file = r"C:\Projects\SV-Build\_ai\alarm-image-descriptions.md"

client = anthropic.Anthropic()

# Only describe content images — skip hero and rel thumbnails
skip = {
    "burglar-alarm-guide-singapore.webp",
    "burglar-alarm-guide-singapore-rel.webp",
}

files = sorted([
    f for f in os.listdir(folder)
    if f.endswith(".webp") and f not in skip
])

lines = []
lines.append("# Alarm Guide Image Descriptions")
lines.append(f"## {len(files)} images described")
lines.append("")
lines.append("| Filename | Description |")
lines.append("|---|---|")

for fname in files:
    fpath = os.path.join(folder, fname)
    with open(fpath, "rb") as f:
        img_data = base64.standard_b64encode(f.read()).decode("utf-8")

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=150,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/webp",
                        "data": img_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Describe what is physically visible in this image in one plain sentence. Be specific about objects, colours, and setting. No interpretation — just what you can see."
                }
            ],
        }]
    )

    description = response.content[0].text.strip()
    lines.append(f"| {fname} | {description} |")
    print(f"✅ {fname}")
    print(f"   {description}")
    print()

os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\nDone. Output saved to: {output_file}")
