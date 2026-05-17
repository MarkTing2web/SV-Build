"""
fix_image_paths_v2.py
Securevision — Direct Image Path Fix (v2)

Simple and targeted. Does exactly two things:
  1. Replaces /images/insight-  with  /images/insights/insight-
  2. Replaces /images/cctv-     with  /images/insights/cctv-
  3. Replaces /images/intercom- with  /images/insights/intercom-
  4. Replaces /images/alarm-    with  /images/insights/alarm-
  5. Replaces /images/digital-  with  /images/insights/digital-
  6. Replaces /images/og-default with /images/og-default (leave alone)

Scans all HTML files in /insights/ and subfolders.
No dependency checks — just does the string replacement directly.

Usage:
  python fix_image_paths_v2.py
"""

from pathlib import Path

# ── CONFIG ────────────────────────────────────────────────────────────────────

REPO_ROOT = Path(r"C:\Projects\SV-Build")
HTML_DIR  = REPO_ROOT / "insights"

# Each tuple: (find this exact string, replace with this exact string)
REPLACEMENTS = [
    ("/images/insight-",   "/images/insights/insight-"),
    ("/images/cctv-",      "/images/insights/cctv-"),
    ("/images/intercom-",  "/images/insights/intercom-"),
    ("/images/alarm-",     "/images/insights/alarm-"),
    ("/images/digital-",   "/images/insights/digital-"),
    # Fix the spaces filename too
    ("/images/Securevision sales discussing",
     "/images/insights/Securevision sales discussing"),
]

# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("Securevision — Direct Image Path Fix v2")
    print("=" * 65)

    if not HTML_DIR.exists():
        print(f"\nERROR: HTML directory not found:\n  {HTML_DIR}")
        return

    html_files = list(HTML_DIR.rglob("*.html"))
    print(f"\nHTML files found: {len(html_files)}\n")

    total_fixes  = 0
    files_changed = 0

    for html_path in sorted(html_files):
        # Read file
        try:
            text = html_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = html_path.read_text(encoding="latin-1")

        original = text
        file_fixes = 0

        # Apply each replacement
        for find_str, replace_str in REPLACEMENTS:
            count = text.count(find_str)
            if count:
                text = text.replace(find_str, replace_str)
                file_fixes += count

        # Write back only if changed
        if text != original:
            html_path.write_text(text, encoding="utf-8")
            rel = html_path.relative_to(REPO_ROOT)
            print(f"  FIXED  {rel}  ({file_fixes} replacement(s))")
            total_fixes  += file_fixes
            files_changed += 1
        else:
            rel = html_path.relative_to(REPO_ROOT)
            print(f"  OK     {rel}")

    print(f"\n{'='*65}")
    print("SUMMARY")
    print(f"{'='*65}")
    print(f"  HTML files scanned:  {len(html_files)}")
    print(f"  HTML files changed:  {files_changed}")
    print(f"  Total replacements:  {total_fixes}")
    print(f"\nDone. Run the audit again to confirm.")
    print(f"{'='*65}\n")


if __name__ == "__main__":
    main()
