import os
from PIL import Image, ImageOps

artifact_dir = r"C:\Users\ler\.gemini\antigravity-ide\brain\403a2d5c-8453-466c-870d-11997a4d4efa"
output_dir = r"C:\Projects\SV-Build\images\insights"

images = [
    {"src": "compare_security_integrators_feature_1781358630846.png", "dst": "compare-security-integrators-feature.webp", "size": (640, 360)},
    {"src": "compare_security_integrators_scope_1781358643850.png", "dst": "compare-security-integrators-scope.webp", "size": (320, 240)},
    {"src": "compare_security_integrators_reference_1781358657312.png", "dst": "compare-security-integrators-reference.webp", "size": (320, 240)},
    {"src": "condo_security_upgrade_proposals_feature_1781358669925.png", "dst": "condo-security-upgrade-proposals-feature.webp", "size": (640, 360)},
    {"src": "condo_security_upgrade_proposals_gaps_1781358695646.png", "dst": "condo-security-upgrade-proposals-gaps.webp", "size": (320, 240)},
    {"src": "condo_security_upgrade_proposals_budget_1781358708405.png", "dst": "condo-security-upgrade-proposals-budget.webp", "size": (320, 240)},
    {"src": "architect_security_guide_feature_1781358721909.png", "dst": "architect-security-guide-feature.webp", "size": (640, 360)},
    {"src": "architect_security_guide_fire_1781358732597.png", "dst": "architect-security-guide-fire.webp", "size": (320, 240)},
    {"src": "architect_security_guide_drawing_1781358757399.png", "dst": "architect-security-guide-drawing.webp", "size": (320, 240)},
    {"src": "cctv_ai_upgrade_feature_1781358770309.png", "dst": "cctv-ai-upgrade-feature.webp", "size": (640, 360)},
    {"src": "cctv_ai_upgrade_nvr_1781358782226.png", "dst": "cctv-ai-upgrade-nvr.webp", "size": (320, 240)},
    {"src": "cctv_ai_upgrade_hardware_1781358793997.png", "dst": "cctv-ai-upgrade-hardware.webp", "size": (320, 240)}
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
