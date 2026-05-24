"""
hero-solutions-organise.py
Securevision — Two tasks in one script:

TASK 1: Generate -mobile.webp variants (1080x1920)
for 8 pages that are missing mobile hero images.
Crops from their existing desktop hero (1920x1080).

TASK 2: Move 19 hero images that are still in
/images/solutions/ subfolders into /images/solutions/
hero-solutions/ and update HTML references sitewide.

Usage: python hero-solutions-organise.py
Run from: C:\\Projects\\SV-Build
"""

from pathlib import Path
from PIL import Image
import shutil
import re
import sys

REPO          = Path(r"C:\Projects\SV-Build")
HERO_DIR      = REPO / "images" / "solutions" / "hero-solutions"
SOLUTIONS_DIR = REPO / "images" / "solutions"
WEBP_QUALITY  = 82

# ── HELPERS ───────────────────────────────────────────────────────────────────

def centre_crop(img, tw, th):
    sw, sh = img.size
    sr, tr = sw / sh, tw / th
    if sr > tr:
        nw = int(sw * th / sh); nh = th
    else:
        nw = tw; nh = int(sh * tw / sw)
    img = img.resize((nw, nh), Image.LANCZOS)
    l = (nw - tw) // 2; t = (nh - th) // 2
    return img.crop((l, t, l + tw, t + th))

def to_rgb(img):
    if img.mode in ("RGBA", "P"):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        img2 = img.convert("RGBA") if img.mode == "P" else img
        bg.paste(img2, mask=img2.split()[3])
        return bg
    return img.convert("RGB") if img.mode != "RGB" else img

def save_webp(img, path, w, h):
    out = centre_crop(img, w, h)
    out = to_rgb(out)
    path.parent.mkdir(parents=True, exist_ok=True)
    out.save(path, "WEBP", quality=WEBP_QUALITY, method=6)
    return path.stat().st_size // 1024

def update_html_refs(old_path, new_path):
    """Update all HTML files in repo that reference old_path."""
    html_files = list(REPO.rglob("*.html"))
    old_str = old_path.replace("\\", "/")
    new_str = new_path.replace("\\", "/")
    updated = []
    for f in html_files:
        try:
            content = f.read_text(encoding="utf-8")
            if old_str in content:
                content = content.replace(old_str, new_str)
                f.write_text(content, encoding="utf-8")
                updated.append(f.relative_to(REPO))
        except Exception:
            pass
    return updated

# ── TASK 1: Generate missing mobile variants ──────────────────────────────────

MOBILE_TO_GENERATE = [
    # (source desktop hero in hero-solutions, mobile output name)
    ("automate-vehicle-access-hero.webp",
     "automate-vehicle-access-hero-mobile.webp"),
    ("solution-commercial-hotel-hero.webp",
     "solution-commercial-hotel-hero-mobile.webp"),
    ("solution-commercial-office-hero.webp",
     "solution-commercial-office-hero-mobile.webp"),
    ("solution-commercial-retail-hero.webp",
     "solution-commercial-retail-hero-mobile.webp"),
    ("solution-improve-cctv-visibility-hero.webp",
     "solution-improve-cctv-visibility-hero-mobile.webp"),
    ("improve-visitor-management-hero.webp",
     "improve-visitor-management-hero-mobile.webp"),
    ("reduce-manpower-with-technology.webp",
     "reduce-manpower-with-technology-mobile.webp"),
    ("intercom-upgrade-hero.webp",
     "intercom-upgrade-hero-mobile.webp"),
]

# ── TASK 2: Move 19 heroes to hero-solutions ──────────────────────────────────
# Format: (current path relative to SOLUTIONS_DIR, new filename in hero-solutions)

HEROES_TO_MOVE = [
    # solutions/ root
    ("solution-condominiums-managing-agents-hero.webp",
     "solution-condominiums-managing-agents-hero.webp"),
    ("solution-condominiums-mcst-hero.webp",
     "solution-condominiums-mcst-hero.webp"),
    ("solution-condominiums-security-contractors-hero.webp",
     "solution-condominiums-security-contractors-hero.webp"),
    ("solution-healthcare-daycare-hero.webp",
     "solution-healthcare-daycare-hero.webp"),
    ("solution-industrial-logistics-hero.webp",
     "solution-industrial-logistics-hero.webp"),
    ("solution-industrial-manufacturing-hero.webp",
     "solution-industrial-manufacturing-hero.webp"),
    ("solution-industrial-tech-park-hero.webp",
     "solution-industrial-tech-park-hero.webp"),
    ("solution-institutions-community-hero.webp",
     "solution-institutions-community-hero.webp"),
    ("solution-institutions-govt-office-hero.webp",
     "solution-institutions-govt-office-hero.webp"),
    ("solution-institutions-schools-hero.webp",
     "solution-institutions-schools-hero.webp"),
    ("solution-managed-living-co-living-hero.webp",
     "solution-managed-living-co-living-hero.webp"),
    # subfolders
    ("commercial/commercial-security-systems-hero.webp",
     "commercial-security-systems-hero.webp"),
    ("condominiums/condominium-security-systems-hero.webp",
     "condominium-security-systems-hero.webp"),
    ("data-centres/data-centre-security-systems-hero.webp",
     "data-centre-security-systems-hero.webp"),
    ("healthcare/healthcare-security-systems-hero.webp",
     "healthcare-security-systems-hero.webp"),
    ("industrial/industrial-security-systems-hero.webp",
     "industrial-security-systems-hero.webp"),
    ("institutions/institutions-security-systems-hero.webp",
     "institutions-security-systems-hero.webp"),
    ("managed-living/managed-living-security-systems-hero.webp",
     "managed-living-security-systems-hero.webp"),
    ("residential/partnering-architects-and-designers.webp",
     "partnering-architects-and-designers.webp"),
]

# Also move their -mobile variants if they exist alongside
MOBILE_VARIANTS_TO_MOVE = [
    ("solution-condominiums-managing-agents-hero-mobile.webp",
     "solution-condominiums-managing-agents-hero-mobile.webp"),
    ("solution-condominiums-mcst-hero-mobile.webp",
     "solution-condominiums-mcst-hero-mobile.webp"),
    ("solution-condominiums-security-contractors-hero-mobile.webp",
     "solution-condominiums-security-contractors-hero-mobile.webp"),
    ("solution-healthcare-daycare-hero-mobile.webp",
     "solution-healthcare-daycare-hero-mobile.webp"),
    ("solution-industrial-logistics-hero-mobile.webp",
     "solution-industrial-logistics-hero-mobile.webp"),
    ("solution-industrial-manufacturing-hero-mobile.webp",
     "solution-industrial-manufacturing-hero-mobile.webp"),
    ("solution-industrial-tech-park-hero-mobile.webp",
     "solution-industrial-tech-park-hero-mobile.webp"),
    ("solution-institutions-community-hero-mobile.webp",
     "solution-institutions-community-hero-mobile.webp"),
    ("solution-institutions-govt-office-hero-mobile.webp",
     "solution-institutions-govt-office-hero-mobile.webp"),
    ("solution-institutions-schools-hero-mobile.webp",
     "solution-institutions-schools-hero-mobile.webp"),
    ("solution-managed-living-co-living-hero-mobile.webp",
     "solution-managed-living-co-living-hero-mobile.webp"),
    ("commercial/commercial-security-systems-hero-mobile.webp",
     "commercial-security-systems-hero-mobile.webp"),
    ("condominiums/condominium-security-systems-hero-mobile.webp",
     "condominium-security-systems-hero-mobile.webp"),
    ("data-centres/data-centre-security-systems-hero-mobile.webp",
     "data-centre-security-systems-hero-mobile.webp"),
    ("healthcare/healthcare-security-systems-hero-mobile.webp",
     "healthcare-security-systems-hero-mobile.webp"),
    ("industrial/industrial-security-systems-hero-mobile.webp",
     "industrial-security-systems-hero-mobile.webp"),
    ("institutions/institutions-security-systems-hero-mobile.webp",
     "institutions-security-systems-hero-mobile.webp"),
    ("managed-living/managed-living-security-systems-hero-mobile.webp",
     "managed-living-security-systems-hero-mobile.webp"),
]

# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    try:
        from PIL import Image
    except ImportError:
        print("ERROR: pip install Pillow")
        sys.exit(1)

    HERO_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 65)
    print("TASK 1 — Generate 8 missing mobile hero variants")
    print("=" * 65)

    t1_done = 0
    for desktop_name, mobile_name in MOBILE_TO_GENERATE:
        src = HERO_DIR / desktop_name
        dst = HERO_DIR / mobile_name

        if dst.exists():
            print(f"  SKIP (exists): {mobile_name}")
            continue
        if not src.exists():
            print(f"  SKIP (source not found): {desktop_name}")
            continue

        with Image.open(src) as img:
            kb = save_webp(img, dst, 1080, 1920)
        print(f"  \u2705 Created: {mobile_name} ({kb}KB)")
        t1_done += 1

    print(f"\n  Generated: {t1_done} mobile variants")

    print()
    print("=" * 65)
    print("TASK 2 — Move 19 hero images to hero-solutions/")
    print("=" * 65)

    t2_done = 0
    t2_skip = 0
    all_moves = HEROES_TO_MOVE + MOBILE_VARIANTS_TO_MOVE

    for rel_src, new_name in all_moves:
        src = SOLUTIONS_DIR / rel_src
        dst = HERO_DIR / new_name

        if not src.exists():
            print(f"  SKIP (not found): {rel_src}")
            t2_skip += 1
            continue

        if dst.exists():
            print(f"  SKIP (already in hero-solutions): {new_name}")
            t2_skip += 1
            continue

        shutil.move(str(src), str(dst))
        print(f"  \u2705 Moved: {rel_src}")
        print(f"       \u2192 hero-solutions/{new_name}")

        # Update HTML references sitewide
        old_ref = "/images/solutions/" + rel_src.replace("\\", "/")
        new_ref = "/images/solutions/hero-solutions/" + new_name
        updated = update_html_refs(old_ref, new_ref)
        if updated:
            for f in updated:
                print(f"       HTML updated: {f}")

        t2_done += 1

    print(f"\n  Moved: {t2_done} files")
    print(f"  Skipped: {t2_skip} files")

    print()
    print("=" * 65)
    print("DONE")
    print("=" * 65)
    print(f"  Mobile variants generated: {t1_done}")
    print(f"  Heroes moved to hero-solutions: {t2_done}")
    print()

if __name__ == "__main__":
    main()
