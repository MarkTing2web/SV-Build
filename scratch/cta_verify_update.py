import os
import re

mapping_rules = [
    (r'portfolio/condominiums/', 'cta-property'),
    (r'portfolio/residential/', 'cta-property'),
    (r'portfolio/commercial/', 'cta-facilities'),
    (r'portfolio/industrial/', 'cta-facilities'),
    (r'portfolio/data-centres/', 'cta-facilities'),
    (r'portfolio/institutions/', 'cta-compliance'),
    (r'portfolio/managed-living/', 'cta-compliance'),
    (r'portfolio/healthcare/', 'cta-care'),
    (r'solutions/healthcare/', 'cta-care'),
    (r'solutions/residential/', 'cta-property'),
    (r'solutions/condominiums/', 'cta-property'),
    (r'solutions/commercial/', 'cta-facilities'),
    (r'solutions/industrial/', 'cta-facilities'),
    (r'solutions/institutions/', 'cta-compliance'),
    (r'solutions/managed-living/', 'cta-compliance'),
    (r'brands/', 'cta-facilities'),
    (r'insights/', 'cta-property'),
    (r'systems/', 'cta-facilities'),
    (r'resources/', 'cta-property'),
    (r'index\.html$', 'cta-property'),
    (r'managing-agent\.html$', 'cta-property'),
    (r'mcst-committee-member\.html$', 'cta-property'),
    (r'new-build-security-singapore\.html$', 'cta-property'),
    (r'people-access-control\.html$', 'cta-facilities'),
    (r'surveillance-detection\.html$', 'cta-facilities'),
    (r'vehicle-access-control\.html$', 'cta-facilities'),
    (r'contact\.html$', 'cta-facilities'),
    (r'contact-gateway\.html$', 'cta-facilities'),
    (r'request-site-assessment-singapore\.html$', 'cta-facilities'),
    (r'portfolio/index\.html$', 'cta-facilities'),
    (r'solutions/index\.html$', 'cta-facilities'),
    (r'about/index\.html$', 'cta-facilities'),
    (r'about/architect-partners\.html$', 'cta-facilities'),
]

skip_pages = [
    "booking-success.html",
    "contact-success.html",
    "privacy.html",
    "terms.html",
    "sitemap.html",
    "thank-you-booking.html",
    "thank-you-proposal.html",
]

legacy_cta_classes = [
    "cta-res", "cta-com", "cta-condo", "cta-home", "cta-indus", "cta-gov", "cta-healthcare",
    "cta-surveillance", "cta-access", "cta-vehicle", "cta-platform", "cta-cctv", "cta-day-care",
    "cta-schools", "cta-govt-office", "cta-logistics", "cta-manufacturing", "cta-community",
    "cta-tech-park", "cta-alarm", "cta-intercom", "cta-office-phones", "cta-thermal", "cta-perimeter",
    "cta-ai", "cta-vehicle-access", "cta-managed", "cta-dc", "cta-skyline", "cta-resources",
    "cta-sec-final", "cta-section-final", "cta-industrial"
]

def get_group(rel_path):
    rel_path_alt = rel_path.replace('\\', '/')
    for pattern, group in mapping_rules:
        if re.search(pattern, rel_path_alt):
            return group
    # Fallbacks
    if 'portfolio' in rel_path_alt: return 'cta-facilities'
    if 'solutions' in rel_path_alt: return 'cta-facilities'
    if 'about' in rel_path_alt: return 'cta-facilities'
    return None

def update_file(full_path, rel_path):
    if rel_path in skip_pages:
        return "SKIPPED"

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    group_class = get_group(rel_path)
    if not group_class:
        return "NO_GROUP_MAPPED"

    # 1. Replace section classes and remove inline backgrounds
    legacy_pattern = "|".join(legacy_cta_classes)
    tag_pattern = rf'(<section[^>]+class="([^"]*(cta-section|cta-high-impact|{legacy_pattern})[^"]*)"[^>]*>)'
    
    def replace_section(match):
        full_tag = match.group(1)
        classes_str = match.group(2)
        classes = classes_str.split()
        
        new_classes = [c for c in classes if c not in legacy_cta_classes]
        if "cta-section" not in new_classes:
            new_classes.insert(0, "cta-section")
        if "cta-high-impact" not in new_classes:
            new_classes.append("cta-high-impact")
            
        group_classes = ['cta-property', 'cta-facilities', 'cta-compliance', 'cta-care']
        new_classes = [c for c in new_classes if c not in group_classes]
        
        ordered_classes = ["cta-section", "cta-high-impact", group_class]
        for c in new_classes:
            if c not in ordered_classes:
                ordered_classes.append(c)
        
        new_classes_str = " ".join(ordered_classes)
        new_tag = full_tag.replace(f'class="{classes_str}"', f'class="{new_classes_str}"')
        new_tag = re.sub(r'\s*style="[^"]*background[^"]*"', '', new_tag)
        return new_tag

    new_content = re.sub(tag_pattern, replace_section, content)
    
    # 2. Remove legacy style blocks from <head>
    for legacy_cls in legacy_cta_classes:
        # Match .classname { ... } including potential newlines
        style_pattern = rf'\.{legacy_cls}\s*\{{[^}}]*\}}'
        new_content = re.sub(style_pattern, '', new_content, flags=re.DOTALL)

    # 3. Final cleanup of multiple FINAL CTA comments (optional but nice)
    new_content = re.sub(r'(<!-- ── FINAL CTA ── -->\s*){2,}', r'<!-- FINAL CTA -->\n', new_content)
    
    has_cta = 'cta-high-impact' in new_content
    
    if new_content != content:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return "UPDATED"
    
    return "OK" if has_cta else "MISSING_CTA"

base_dir = "c:/Projects/SV-Build"
results = {}

for root, dirs, files in os.walk(base_dir):
    if '.git' in root or 'node_modules' in root or 'scratch' in root or 'templates' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, base_dir)
            status = update_file(full_path, rel_path)
            results[rel_path] = status

print("FINAL CTA VERIFICATION REPORT")
print("=============================")
for rel_path, status in sorted(results.items()):
    if status != "OK" and status != "SKIPPED":
        print(f"{status}: {rel_path}")

missing = [p for p, s in results.items() if s == "MISSING_CTA"]
print(f"\nTotal Missing CTA: {len(missing)}")
for p in missing:
    print(f"  - {p}")
