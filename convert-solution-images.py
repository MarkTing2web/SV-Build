from pathlib import Path
from PIL import Image

# ── CONFIG ────────────────────────────────────────────────────────────────────

REPO_ROOT    = Path(r"C:\Projects\SV-Build")
IMAGES_DIR   = REPO_ROOT / "images" / "solutions"
HTML_DIR     = REPO_ROOT
WEBP_QUALITY = 82
MAX_WIDTH    = 1200
SOURCE_EXTS  = {".jpg", ".jpeg", ".png", ".jfif"}

# ── HELPERS ───────────────────────────────────────────────────────────────────

def resize_if_needed(img):
    w, h = img.size
    if w <= MAX_WIDTH:
        return img
    new_h = int(h * MAX_WIDTH / w)
    return img.resize((MAX_WIDTH, new_h), Image.LANCZOS)


def convert_image(src_path):
    dest_path = src_path.parent / f"{src_path.stem}.webp"
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
    # Find all html files excluding node_modules, .git, .vercel
    html_files = []
    for p in html_dir.rglob("*.html"):
        parts = p.parts
        if any(part in parts for part in (".git", "node_modules", ".vercel")):
            continue
        html_files.append(p)
        
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
            print(f"  Updated {html_path.relative_to(REPO_ROOT)} - {file_count} reference(s)")
            total += file_count
    return total

# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("Securevision - Solutions Image Conversion & Resize")
    print("=" * 65)

    if not IMAGES_DIR.exists():
        print(f"\nERROR: Images directory not found:\n  {IMAGES_DIR}")
        return

    # Find all source images recursively in images/solutions
    candidates = sorted(list(
        f for f in IMAGES_DIR.rglob("*")
        if f.is_file()
        and f.suffix.lower() in SOURCE_EXTS
    ))

    # Also list webp files that will be skipped
    webp_files = sorted(list(
        f for f in IMAGES_DIR.rglob("*")
        if f.is_file()
        and f.suffix.lower() == ".webp"
    ))

    if webp_files:
        print("\nSkipped (already WebP):")
        for f in webp_files:
            rel_path = f.relative_to(IMAGES_DIR).as_posix()
            print(f"  - {rel_path}")

    if not candidates:
        print("\nNo matching files to convert (.png, .jpg, .jpeg, .jfif). Nothing to do.")
        return

    print(f"\nFound {len(candidates)} file(s) to convert.\n")

    rename_map = {}
    results    = []
    failed     = []

    for src in candidates:
        rel_path = src.relative_to(IMAGES_DIR).as_posix()
        print(f"  Converting: {rel_path}")
        result = convert_image(src)
        if result:
            dest, old_b, new_b = result
            pct = round((1 - new_b / old_b) * 100, 1)
            print(f"    -> {dest.name}  ({old_b//1024}KB -> {new_b//1024}KB, -{pct}%)")
            rename_map[src.name] = dest.name
            results.append((src, dest, old_b, new_b))
        else:
            failed.append(src)

    print(f"\n{'-'*65}")
    print("Updating HTML references...")
    print(f"{'-'*65}")
    total_refs = update_html_references(HTML_DIR, rename_map)
    print(f"\n  Total references updated: {total_refs}")

    print(f"\n{'-'*65}")
    print("Deleting originals...")
    print(f"{'-'*65}")
    deleted = 0
    for src, dest, _, _ in results:
        try:
            src.unlink()
            print(f"  Deleted original: {src.name}")
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
    print(f"  HTML references fixed:  {total_refs}")
    print(f"  Total size before:      {total_old//1024:,} KB")
    print(f"  Total size after:       {total_new//1024:,} KB")
    print(f"  Total saved:            {total_saved//1024:,} KB  (-{overall_pct}%)")
    if failed:
        print(f"\n  FAILED ({len(failed)}):")
        for f in failed:
            print(f"    {f.name}")
    print(f"\n{'='*65}")
    print("Done.")
    print(f"{'='*65}\n")

if __name__ == "__main__":
    main()
