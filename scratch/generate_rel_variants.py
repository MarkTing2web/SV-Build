from pathlib import Path
from PIL import Image

HERO_DIR = Path("images/solutions/hero-solutions")
WEBP_QUALITY = 82

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

HEROES = [
    "commercial-security-systems-hero.webp",
    "condominium-security-systems-hero.webp",
    "solution-condominiums-managing-agents-hero.webp",
    "solution-condominiums-mcst-hero.webp",
    "solution-condominiums-security-contractors-hero.webp",
    "data-centre-security-systems-hero.webp",
    "solution-healthcare-daycare-hero.webp",
    "healthcare-security-systems-hero.webp",
    "industrial-security-systems-hero.webp",
    "solution-industrial-logistics-hero.webp",
    "solution-industrial-manufacturing-hero.webp",
    "solution-industrial-tech-park-hero.webp",
    "solution-institutions-community-hero.webp",
    "solution-institutions-govt-office-hero.webp",
    "institutions-security-systems-hero.webp",
    "solution-institutions-schools-hero.webp",
    "solution-managed-living-co-living-hero.webp",
    "managed-living-security-systems-hero.webp",
]

done = 0
skipped = 0
errors = []

for hero in HEROES:
    src = HERO_DIR / hero
    stem = hero.replace(".webp", "")
    dst = HERO_DIR / (stem + "-rel.webp")

    if dst.exists():
        print(f"  SKIP (exists): {dst.name}")
        skipped += 1
        continue

    if not src.exists():
        print(f"  SKIP (source not found): {hero}")
        skipped += 1
        continue

    try:
        with Image.open(src) as img:
            out = centre_crop(img, 960, 540)
            out = to_rgb(out)
            out.save(dst, "WEBP", quality=82, method=6)
        kb = dst.stat().st_size // 1024
        print(f"  OK: {dst.name} ({kb}KB)")
        done += 1
    except Exception as e:
        print(f"  ERROR: {hero} — {e}")
        errors.append(hero)

print(f"\nDone. Created: {done} | Skipped: {skipped} | Errors: {len(errors)}")
