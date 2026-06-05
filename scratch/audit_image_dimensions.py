import os
import math

try:
    from PIL import Image
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
    from PIL import Image

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"

files_to_check = [
    "/images/resources/guides/network/structured-cabling-patch-panel.webp",
    "/images/resources/guides/network/guest-wifi-network-setup.webp",
    "/images/resources/guides/network/cable-tester-wiremap.webp",
    "/images/resources/guides/network/wifi-security-lock-signal.webp",
    "/images/resources/guides/network/ruijie-omada-access-points.webp",
    "/images/resources/guides/network/network-monitoring-dashboard.webp",
    "/images/solutions/hero-solutions/dormitories-hero.webp",
    "/images/hero-security-solutions-singapore.webp",
    "/images/solutions/root-solutions/solution-condominiums-condo-resident-experience.webp",
    "/images/portfolio-hero.png",
    "/images/brands/security-brands-hero.png",
    "/images/solutions/root-solutions/solution-condominiums-condo-estate-operations.webp",
    "/images/portfolio/commercial/scape-hero.webp",
    "/images/solutions/condominiums/fragmented-systems.webp",
    "/images/solutions/root-solutions/solution-commercial-retail-video-analytics-of-a-retail-shop.webp",
    "/images/solutions/hero-solutions/solution-commercial-office-hero.webp",
    "/images/solutions/hero-solutions/solution-commercial-retail-hero.webp"
]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

results = []

for rel_path in files_to_check:
    full_path = os.path.join(repo_root, rel_path.lstrip('/'))
    
    if not os.path.exists(full_path):
        continue
        
    size_kb = os.path.getsize(full_path) / 1024
    
    try:
        with Image.open(full_path) as img:
            w, h = img.size
    except Exception:
        w, h = 0, 0
        
    if w == 0 or h == 0:
        continue
        
    divisor = gcd(w, h)
    aspect_w, aspect_h = w // divisor, h // divisor
    ratio_val = w / h
    if abs(ratio_val - 16/9) < 0.05: aspect = "16:9"
    elif abs(ratio_val - 3/4) < 0.05: aspect = "3:4"
    elif abs(ratio_val - 4/3) < 0.05: aspect = "4:3"
    elif abs(ratio_val - 1) < 0.05: aspect = "1:1"
    else: aspect = f"{aspect_w}:{aspect_h}"

    expected = ""
    target_w, target_h = 0, 0
    action = "COMPRESS ONLY"
    
    basename = os.path.basename(rel_path).lower()
    
    # Classify based on filename and directory
    if "hero" in basename or "-hero" in basename:
        expected = "1920x1080px (16:9)"
        target_w, target_h = 1920, 1080
    elif "diagram" in basename or "dashboard" in basename or "wiremap" in basename:
        expected = "Keep original ratio"
        action = "COMPRESS ONLY"
    else:
        # Inline article/solution images
        expected = "1200x675px max (16:9)"
        target_w, target_h = 1200, 675
        
    if action != "COMPRESS ONLY":
        pass # already set
    elif target_w and target_h:
        if "max" in expected:
            if w > target_w * 1.1 or h > target_h * 1.1:
                action = "RESIZE + COMPRESS"
        else:
            w_diff = abs(w - target_w) / target_w
            h_diff = abs(h - target_h) / target_h
            if w_diff > 0.1 or h_diff > 0.1:
                action = "RESIZE + COMPRESS"
                
    results.append({
        'file': rel_path,
        'size': size_kb,
        'dim': f"{w}x{h}",
        'aspect': aspect,
        'expected': expected,
        'action': action
    })

# Sort by Action
results.sort(key=lambda x: (0 if x['action'] == "RESIZE + COMPRESS" else 1, -x['size']))

print("| File | Current Size | Current Dimensions | Aspect Ratio | Expected Dimensions | Action |")
print("|---|---|---|---|---|---|")
for r in results:
    print(f"| `{r['file']}` | {r['size']:.1f} KB | {r['dim']} | {r['aspect']} | {r['expected']} | **{r['action']}** |")
