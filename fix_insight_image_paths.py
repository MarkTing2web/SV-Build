"""
fix_insight_image_paths.py
Securevision — Insights Image Path Fix Script

What this does:
  1. Scans all HTML files in /insights/ and subfolders
  2. Fixes image paths that point to the wrong folder:
       /images/insight-*   ->  /images/insights/insight-*
       /images/cctv-*      ->  /images/insights/cctv-*
       /images/how-to-*    ->  /images/insights/how-to-*
       /images/intercom-*  ->  /images/insights/intercom-*
       /images/alarm-*     ->  /images/insights/alarm-*
       /images/digital-*   ->  /images/insights/digital-*
  3. Only fixes the path if the file actually EXISTS in
     /images/insights/ — never creates a broken link
  4. Reports exactly what was changed and what is still missing
  5. Does NOT touch paths that are already correct

Requirements: none (standard library only)

Usage:
  python fix_insight_image_paths.py
"""

import re
from pathlib import Path

# ── CONFIG ────────────────────────────────────────────────────────────────────

REPO_ROOT  = Path(r"C:\Projects\SV-Build")
IMAGES_DIR = REPO_ROOT / "images" / "insights"
HTML_DIR   = REPO_ROOT / "insights"

# Filename prefixes that belong in /images/insights/ but may be
# referenced as /images/ in the HTML
MISROUTED_PREFIXES = [
    "insight-",
    "cctv-",
    "how-to-",
    "intercom-",
    "alarm-",
    "digital-",
    "securevision-",
]

# ── HELPERS ───────────────────────────────────────────────────────────────────

def get_insights_filenames() -> set:
    """Return set of all filenames currently in /images/insights/."""
    if not IMAGES_DIR.exists():
        return set()
    return {f.name for f in IMAGES_DIR.iterdir() if f.is_file()}


def should_fix(filename: str, insights_files: set) -> bool:
    """
    Return True if this filename:
    - starts with one of our misrouted prefixes
    - actually exists in /images/insights/
    """
    name_lower = filename.lower()
    for prefix in MISROUTED_PREFIXES:
        if name_lower.startswith(prefix):
            # Check if it exists in insights folder
            if filename in insights_files:
                return True
            # Also check with .webp extension swap
            stem = Path(filename).stem
            if f"{stem}.webp" in insights_files:
                return True
    return False


def fix_extension_if_converted(filename: str, insights_files: set) -> str:
    """
    If the original .jpg/.png was converted to .webp by the
    conversion script, return the .webp filename instead.
    """
    if filename in insights_files:
        return filename
    stem = Path(filename).stem
    webp_name = f"{stem}.webp"
    if webp_name in insights_files:
        return webp_name
    return filename


# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("Securevision — Insights Image Path Fix")
    print("=" * 65)

    if not HTML_DIR.exists():
        print(f"\nERROR: HTML directory not found:\n  {HTML_DIR}")
        return

    if not IMAGES_DIR.exists():
        print(f"\nERROR: Images directory not found:\n  {IMAGES_DIR}")
        return

    insights_files = get_insights_filenames()
    print(f"\nFiles in /images/insights/: {len(insights_files)}")

    html_files = list(HTML_DIR.rglob("*.html"))
    print(f"HTML files to scan:         {len(html_files)}\n")

    # Pattern matches any image reference in src=, srcset=, content=, url()
    # that points to /images/[filename] (NOT /images/insights/[filename])
    # Captures: the path prefix and the filename separately
    pattern = re.compile(
        r'(/images/)([^/"\')\s]+\.(?:jpg|jpeg|png|webp|gif|svg|jfif))',
        re.IGNORECASE
    )

    total_fixes   = 0
    still_missing = set()
    files_changed = []

    for html_path in sorted(html_files):
        try:
            text = html_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = html_path.read_text(encoding="latin-1")

        original  = text
        file_fixes = 0
        file_missing = []

        def replace_path(match):
            nonlocal file_fixes
            prefix   = match.group(1)   # /images/
            filename = match.group(2)   # insight-xxx.jpg

            # Already correctly pathed to insights subfolder — skip
            # (this pattern only matches /images/filename, not /images/insights/filename)

            if should_fix(filename, insights_files):
                correct_filename = fix_extension_if_converted(filename, insights_files)
                file_fixes += 1
                return f"/images/insights/{correct_filename}"

            # Not in insights folder — flag as still missing
            # but only flag image-looking paths, not external
            name_lower = filename.lower()
            for prefix_str in MISROUTED_PREFIXES:
                if name_lower.startswith(prefix_str):
                    file_missing.append(f"/images/{filename}")
                    break

            return match.group(0)  # unchanged

        text = pattern.sub(replace_path, text)

        # Also fix any /images/insights/insight-xxx.jpg that should now
        # point to /images/insights/xxx.webp (extension update)
        def fix_webp_extension(match):
            full_path = match.group(0)   # /images/insights/insight-xxx.jpg
            filename  = match.group(1)   # insight-xxx.jpg
            correct   = fix_extension_if_converted(filename, insights_files)
            if correct != filename:
                return f"/images/insights/{correct}"
            return full_path

        webp_pattern = re.compile(
            r'/images/insights/([^/"\')\s]+\.(?:jpg|jpeg|png|jfif))',
            re.IGNORECASE
        )
        text = webp_pattern.sub(fix_webp_extension, text)

        # Count webp fixes too
        if text != original:
            html_path.write_text(text, encoding="utf-8")
            rel = html_path.relative_to(REPO_ROOT)
            print(f"  FIXED  {rel} — {file_fixes} path(s) corrected")
            total_fixes += file_fixes
            files_changed.append(str(rel))

        if file_missing:
            for m in file_missing:
                still_missing.add(m)

    # Also scan for /images/insights/ references to files that don't exist
    for html_path in sorted(html_files):
        try:
            text = html_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = html_path.read_text(encoding="latin-1")

        for match in re.finditer(
            r'/images/insights/([^/"\')\s]+)',
            text, re.IGNORECASE
        ):
            fname = match.group(1)
            if fname not in insights_files:
                still_missing.add(f"/images/insights/{fname}")

    # ── SUMMARY ───────────────────────────────────────────────────
    print(f"\n{'='*65}")
    print("SUMMARY")
    print(f"{'='*65}")
    print(f"  HTML files scanned:    {len(html_files)}")
    print(f"  HTML files updated:    {len(files_changed)}")
    print(f"  Path fixes applied:    {total_fixes}")
    print(f"  Still missing:         {len(still_missing)}")

    if still_missing:
        print(f"\n{'─'*65}")
        print("STILL MISSING — these files need to be created or")
        print("their references removed from the HTML:")
        print(f"{'─'*65}")
        for m in sorted(still_missing):
            print(f"  {m}")

    print(f"\n{'='*65}")
    print("Done. Run the image audit again to verify.")
    print(f"{'='*65}\n")


if __name__ == "__main__":
    main()
