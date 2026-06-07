import os

shared_css = "C:/Projects/SV-Build/sv-shared.css"
solutions_css = "C:/Projects/SV-Build/sv-solutions.css"

shared_classes = [
    ".trust-bar", ".trust-bar-inner", ".trust-divider", ".mt-24", 
    ".hero-standard", ".hero-compact"
]

sol_classes = [
    ".systems-deepdive-card", ".systems-deepdive-card__img", ".systems-deepdive-card__body",
    ".sol-grid-3", ".sol-grid-4", ".sol-grid-4-auto",
    ".sol-card-flush", ".sol-card-flush-img", ".sol-card-body", ".sol-card-link",
    ".sol-step-num-lg", ".sol-stat-display", ".sol-checklist-split",
    ".sol-badge-grid", ".sol-badge-item",
    ".sol-approach-card", ".sol-approach-num",
    ".sol-mistake-list", ".sol-tick-list"
]

missing = []

if not os.path.exists(shared_css):
    missing.append("sv-shared.css file not found")
else:
    with open(shared_css, 'r', encoding='utf-8') as f:
        content = f.read()
        for c in shared_classes:
            c_name = c.lstrip('.')
            if c_name not in content:
                missing.append(f"{c} missing from sv-shared.css")

if not os.path.exists(solutions_css):
    missing.append("sv-solutions.css file not found")
else:
    with open(solutions_css, 'r', encoding='utf-8') as f:
        content = f.read()
        for c in sol_classes:
            c_name = c.lstrip('.')
            if c_name not in content:
                missing.append(f"{c} missing from sv-solutions.css")

if missing:
    print("MISSING PREREQUISITES:")
    for m in missing:
        print("- " + m)
else:
    print("ALL PREREQUISITES FOUND")
