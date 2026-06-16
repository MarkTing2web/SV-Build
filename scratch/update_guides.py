import os

guides_dir = r"C:\Projects\SV-Build\resources\guides"
changed_files = []
skipped_files = []
no_match_files = []

replacements = [
    ("Founder & Director, Securevision Pte Ltd",  "Founder & CEO, Securevision Pte Ltd"),
    ("Founder & Director, Securevision",           "Founder & CEO, Securevision"),
    ("Founder & Director · Securevision",          "Founder & CEO · Securevision"),
    ("Founder & Director",                         "Founder & CEO"),

    ("Founder &amp; Director, Securevision Pte Ltd", "Founder &amp; CEO, Securevision Pte Ltd"),
    ("Founder &amp; Director, Securevision",          "Founder &amp; CEO, Securevision"),
    ("Founder &amp; Director · Securevision",         "Founder &amp; CEO · Securevision"),
    ("Founder &amp; Director",                        "Founder &amp; CEO"),
]

all_files = sorted(os.listdir(guides_dir))

for fname in all_files:
    if not fname.endswith(".html"):
        continue
    if fname == "index.html":
        skipped_files.append(fname)
        continue

    fpath = os.path.join(guides_dir, fname)

    try:
        with open(fpath, encoding="utf-8") as f:
            original = f.read()
    except Exception as e:
        skipped_files.append(f"{fname} (READ ERROR: {e})")
        continue

    updated = original

    for old, new in replacements:
        updated = updated.replace(old, new)

    if updated != original:
        try:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(updated)
            changed_files.append(fname)
        except Exception as e:
            skipped_files.append(f"{fname} (WRITE ERROR: {e})")
    else:
        no_match_files.append(fname)

print(f"\n============================================================\nGUIDES FOUNDER TITLE UPDATE — RESULTS\n============================================================\n")
print(f"Files updated ({len(changed_files)}):")
for f in changed_files:
    print(f"  [OK] {f}")

print(f"\nFiles with no match found ({len(no_match_files)}):")
for f in no_match_files:
    print(f"  [NO MATCH] {f}")

print(f"\nFiles skipped ({len(skipped_files)}):")
for f in skipped_files:
    print(f"  [SKIP] {f}")

print(f"\nSUMMARY: {len(changed_files)} updated, {len(no_match_files)} no match, {len(skipped_files)} skipped")
print(f"============================================================\n")
