import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\sv-portfolio.css"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Migration comment
has_migration = "PORTFOLIO HERO — LEGACY CLASS" in content and ".portfolio-hero {" in content.split("Migration started: June 2026\n─────────────────────────────────────────────────────────────── */\n")[1][:20]
print(f"1. Migration comment present before .portfolio-hero: {'Yes' if has_migration else 'No'}")

# 2. .desc clamp rule
has_desc_clamp = ".project-card .desc {\n    display: -webkit-box;\n    -webkit-line-clamp: 3;" in content
print(f"2. .project-card .desc clamp rule present: {'Yes' if has_desc_clamp else 'No'}")

# 3. p:last-of-type clamp rule
has_p_clamp = ".project-card .card-body > p:last-of-type {\n    display: -webkit-box;\n    -webkit-line-clamp: 2;" in content
print(f"3. .project-card .card-body > p:last-of-type clamp rule present: {'Yes' if has_p_clamp else 'No'}")

# 4. v1.3
has_v13 = "v1.3  June 2026   hero-compact migration:" in content
print(f"4. v1.3 entry present: {'Yes' if has_v13 else 'No'}")
