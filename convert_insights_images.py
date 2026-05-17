"""
convert_insights_images.py
Securevision — Insights Image Conversion & Rename Script

What this does:
  1. Finds all JPG / PNG / JFIF images in \images\insights\
     that start with "insight-"
  2. Converts each to WebP at quality 82, resized to max 1200px wide
     (height scales proportionally — no forced crop)
  3. Renames by stripping the "insight-" prefix
     e.g. insight-how-to-choose-cctv-cover.jpg
       -> how-to-choose-cctv-cover.webp
  4. Scans all HTML files in \insights\ (and subfolders) and
     updates every src= and url() reference to the new filename
  5. Deletes the original files after successful conversion
  6. Skips any file that is already .webp
  7. Prints a full before/after size log at the end

Requirements:
  pip install Pillow

Usage:
  Run from VS Code terminal: python convert_insights_images.py
"""

from pathlib import Path
from PIL import Image

# ── CONFIG ────────────────────────────────────────────────────────────────────

REPO_ROOT    = Path(r"C:\Projects\SV-Build")
IMAGES_DIR   = REPO_ROOT / "images" / "insights"
HTML_DIR     = REPO_ROOT / "insights"
WEBP_QUALITY = 82
MAX_WIDTH    = 1200
STRIP_PREFIX = "insight-"
SOURCE_EXTS  = {".jpg", ".jpeg", ".png", ".jfif"}

# ── HELPERS ───────────────────────────────────────────────────────────────────

def new_stem(old_stem: str) -> str:
    if old_stem.lower().startswith(STRIP_PREFIX):
        return old_stem[len(STRIP_PREFIX):]
    return old_stem


def resize_if_needed(img):
    w, h = img.size
    if w <= MAX_WIDTH:
        return img
    new_h = int(h * MAX_WIDTH / w)
    return img.resize((MAX_WIDTH, new_h), Image.LANCZOS)


def convert_image(src_path):
    dest_path = src_path.parent / f"{new_stem(src_path.stem)}.webp"
    try:
        with Image.open(src_path) as img:
            if img.mode in ("P", "RGBA"):
                img = img.convert("RGBA")
            elif img.mode != "RGB":
                img = img.convert("RGB")
            img = resize_if_needed(img)
            img.save(dest_path, "WEBP", quality=WEBP_QUALITY, method=6)
        return dest_path, src_path.stat().st_size, dest_path.stat().st_size
    except Exception as e:
        print(f"  ERROR converting {src_path.name}: {e}")
        return None


def update_html_references(html_dir, rename_map):
    total = 0
    html_files = list(html_dir.rglob("*.html"))
    if not html_files:
        print(f"\n  WARNING: No HTML files found in {html_dir}")
        return 0
    for html_path in html_files:
        try:
            text = html_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = html_path.read_text(encoding="latin-1")
        file_count = 0
        for old, new in rename_map.items():
            n = text.count(old)
            if n:
                text = text.replace(old, new)
                file_count += n
        if file_count:
            html_path.write_text(text, encoding="utf-8")
            print(f"  Updated {html_path.relative_to(REPO_ROOT)} — {file_count} reference(s)")
            total += file_count
    return total

# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("Securevision — Insights Image Conversion & Rename")
    print("=" * 65)

    if not IMAGES_DIR.exists():
        print(f"\nERROR: Images directory not found:\n  {IMAGES_DIR}")
        return
    if not HTML_DIR.exists():
        print(f"\nERROR: HTML directory not found:\n  {HTML_DIR}")
        return

    candidates = [
        f for f in IMAGES_DIR.iterdir()
        if f.is_file()
        and f.suffix.lower() in SOURCE_EXTS
        and f.stem.lower().startswith(STRIP_PREFIX)
    ]

    if not candidates:
        print("\nNo matching files found. Nothing to do.")
        return

    print(f"\nFound {len(candidates)} file(s) to convert.\n")

    rename_map = {}
    results    = []
    failed     = []

    for src in sorted(candidates):
        print(f"  Converting: {src.name}")
        result = convert_image(src)
        if result:
            dest, old_b, new_b = result
            pct = round((1 - new_b / old_b) * 100, 1)
            print(f"    -> {dest.name}  ({old_b//1024}KB -> {new_b//1024}KB, -{pct}%)")
            rename_map[src.name] = dest.name
            results.append((src, dest, old_b, new_b))
        else:
            failed.append(src)

    print(f"\n{'─'*65}")
    print("Updating HTML references...")
    print(f"{'─'*65}")
    total_refs = update_html_references(HTML_DIR, rename_map)
    print(f"\n  Total references updated: {total_refs}")

    print(f"\n{'─'*65}")
    print("Deleting originals...")
    print(f"{'─'*65}")
    deleted = 0
    for src, dest, _, _ in results:
        try:
            src.unlink()
            print(f"  Deleted: {src.name}")
            deleted += 1
        except Exception as e:
            print(f"  ERROR deleting {src.name}: {e}")

    print(f"\n{'='*65}")
    print("SUMMARY")
    print(f"{'='*65}")
    total_old  = sum(r[2] for r in results)
    total_new  = sum(r[3] for r in results)
    total_saved = total_old - total_new
    overall_pct = round((1 - total_new / total_old) * 100, 1) if total_old else 0
    print(f"  Files converted:        {len(results)}")
    print(f"  Originals deleted:      {deleted}")
    print(f"  HTML files scanned:     {len(list(HTML_DIR.rglob('*.html')))}")
    print(f"  HTML references fixed:  {total_refs}")
    print(f"  Total size before:      {total_old//1024:,} KB")
    print(f"  Total size after:       {total_new//1024:,} KB")
    print(f"  Total saved:            {total_saved//1024:,} KB  (-{overall_pct}%)")
    if failed:
        print(f"\n  FAILED ({len(failed)}):")
        for f in failed:
            print(f"    {f.name}")
    print(f"\n{'='*65}")
    print("Done. Verify your site locally before committing to GitHub.")
    print(f"{'='*65}\n")

if __name__ == "__main__":
    main()
