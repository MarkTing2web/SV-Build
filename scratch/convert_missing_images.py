import os
from PIL import Image, ImageOps

artifact_dir = r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa"
output_dir = r"C:\Projects\SV-Build\images\insights"

images = [
    {
        "src": "access_control_multi_door_integration_1781357305158.png",
        "dst": "access-control-multi-door-integration.webp",
        "size": (320, 240)
    },
    {
        "src": "cctv_system_components_feature_1781357317391.png",
        "dst": "cctv-system-components-feature.webp",
        "size": (640, 360)
    },
    {
        "src": "cctv_system_components_poe_1781357330637.png",
        "dst": "cctv-system-components-poe.webp",
        "size": (320, 240)
    },
    {
        "src": "cctv_system_components_nvr_1781357340626.png",
        "dst": "cctv-system-components-nvr.webp",
        "size": (320, 240)
    }
]

for img_data in images:
    src_path = os.path.join(artifact_dir, img_data["src"])
    dst_path = os.path.join(output_dir, img_data["dst"])
    if os.path.exists(src_path):
        with Image.open(src_path) as img:
            img_resized = ImageOps.fit(img, img_data["size"], Image.Resampling.LANCZOS)
            img_resized.save(dst_path, "WEBP", quality=85)
            print(f"Saved {dst_path}")
    else:
        print(f"File not found: {src_path}")
