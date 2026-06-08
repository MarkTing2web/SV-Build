import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\sv-shared.css"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Edit 1: Update hero-compact
old_hero = """.hero-compact {
    min-height: 44vh;
    padding: 130px 0 80px;
}"""
new_hero = """.hero-compact {
    min-height: 52vh;
    padding: 130px 0 80px;
}"""
if old_hero in content:
    content = content.replace(old_hero, new_hero)
else:
    print("Could not find old_hero block.")

# Edit 2: Version Note
old_v28 = """   v2.8  May 2026       Form system extracted to sv-forms.css.
                         Section 29 (~286 lines) removed.
                         Section 33 dead stub (~9 lines) deleted.
                         sv-forms.css created fresh from Section 29
                         content — load on all pages with forms."""
                         
new_v28_29 = """   v2.8  May 2026       Form system extracted to sv-forms.css.
                         Section 29 (~286 lines) removed.
                         Section 33 dead stub (~9 lines) deleted.
                         sv-forms.css created fresh from Section 29
                         content — load on all pages with forms.

   v2.9  June 2026      hero-compact min-height increased from 44vh
                         to 52vh to accommodate portfolio stat grid
                         content without clipping."""

if old_v28 in content:
    content = content.replace(old_v28, new_v28_29)
else:
    print("Could not find v2.8 block.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done.")
