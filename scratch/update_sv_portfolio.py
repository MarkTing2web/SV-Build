import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\sv-portfolio.css"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Change 1
old_hero = ".portfolio-hero {"
new_hero = """/* ── PORTFOLIO HERO — LEGACY CLASS ──────────────────────────
   This class is being retired across all 52 portfolio pages.
   Pages are migrating to: hero hero-compact hero-high-impact hero-[slug]
   governed by sv-shared.css hero height system.
   Once all 52 pages are confirmed migrated, remove this entire
   block including .portfolio-hero::before, .portfolio-hero .hero-image,
   .portfolio-hero .hero-overlay, and .portfolio-hero .container.
   Migration started: June 2026
─────────────────────────────────────────────────────────────── */
.portfolio-hero {"""

if old_hero in content:
    content = content.replace(old_hero, new_hero, 1)
else:
    print("Could not find .portfolio-hero {")

# Change 2
append_block = """

/* ── PORTFOLIO INDEX — CARD CONTENT CLAMP ───────────────────
   Prevents uneven card heights in the 4-column index grid.
   Applied to .project-card elements in portfolio/index.html.
   3 lines for description, 2 lines for key outcome.
─────────────────────────────────────────────────────────────── */
.project-card .desc {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.project-card .card-body > p:last-of-type {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}"""

if "PORTFOLIO INDEX — CARD CONTENT CLAMP" not in content:
    content = content.rstrip() + append_block

# Change 3
old_v12 = "   v1.2  May 2026    Added .grid-3 utility class"
new_v13_12 = """   v1.3  June 2026   hero-compact migration: legacy .portfolio-hero
                     class marked for retirement. Migration comment
                     added above block. Card content clamp rules
                     added for 4-column index grid.

   v1.2  May 2026    Added .grid-3 utility class"""

if old_v12 in content:
    content = content.replace(old_v12, new_v13_12, 1)
else:
    print("Could not find v1.2 block")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
