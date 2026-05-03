import os
import re
import collections
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# CONFIGURATION
ROOT_DIR = r"C:\Projects\SV-Build"
EXCLUDE_DIRS = ['templates', 'node_modules', '.git', '.gemini']
PAGE_TYPES = [
    "Homepage", "Landing Page", "Solution Hub", "Solution Sector", "Persona Sub-page",
    "System Hub", "System Page", "Brand Hub", "Brand Page", "Portfolio Hub",
    "Portfolio Case Study", "Insights Hub", "Insights Article", "Resources Hub",
    "Guide", "Contact", "About", "Other"
]

def get_page_type(rel_path):
    rel_path = rel_path.replace('\\', '/')
    if rel_path == 'index.html': return "Homepage"
    if rel_path in ['request-site-assessment-singapore.html', 'home-security-upgrade-singapore.html', 'security-solutions-singapore.html', 'new-build-security-singapore.html']: return "Landing Page"
    if rel_path.startswith('solutions/'):
        if rel_path == 'solutions/index.html': return "Solution Hub"
        if rel_path.count('/') == 1: return "Solution Sector"
        return "Persona Sub-page"
    if rel_path.startswith('systems/'):
        if rel_path == 'systems/index.html': return "System Hub"
        return "System Page"
    if rel_path.startswith('brands/'):
        if rel_path == 'brands/index.html': return "Brand Hub"
        return "Brand Page"
    if rel_path.startswith('portfolio/'):
        if rel_path == 'portfolio/index.html': return "Portfolio Hub"
        return "Portfolio Case Study"
    if rel_path.startswith('insights/'):
        if rel_path == 'insights/index.html': return "Insights Hub"
        return "Insights Article"
    if rel_path.startswith('resources/'):
        if rel_path == 'resources/index.html': return "Resources Hub"
        return "Guide"
    if rel_path == 'contact.html': return "Contact"
    if rel_path == 'about.html': return "About"
    return "Other"

def clean_label(text):
    text = re.sub(r'<[^>]+>', '', text) # Remove HTML tags
    return text.strip()

def run_audit():
    results = []
    labels_counter = collections.Counter()
    dest_counter = collections.Counter()
    anomalies = []
    skipped = []

    # Regex for a and button tags
    tag_pattern = re.compile(r'<(a|button)\s+([^>]+)>(.*?)</\1>', re.DOTALL | re.IGNORECASE)
    
    # Regex for attributes
    attr_pattern = re.compile(r'(\w+)\s*=\s*["\']([^"\']*)["\']')

    for root, dirs, files in os.walk(ROOT_DIR):
        # Filter excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if not file.endswith('.html'):
                continue
            
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, ROOT_DIR)
            page_type = get_page_type(rel_path)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                skipped.append(f"{rel_path} (Error reading: {e})")
                continue

            # Basic check: if it's minified or too big, skip for safety
            if len(content) > 1000000:
                skipped.append(f"{rel_path} (File too large)")
                continue

            # Remove header/nav/footer blocks from main content to avoid duplicates/exclusions
            # This is a bit rough but works for most templates
            main_content = re.sub(r'<(nav|footer).*?>.*?</\1>', '', content, flags=re.DOTALL | re.IGNORECASE)

            matches = tag_pattern.finditer(main_content)
            
            for match in matches:
                tag_name = match.group(1).lower()
                attrs_raw = match.group(2)
                tag_content = match.group(3)
                
                attrs = dict(attr_pattern.findall(attrs_raw))
                href = attrs.get('href', '')
                class_str = attrs.get('class', '')
                label = clean_label(tag_content)
                
                # CTA Logic
                is_cta = False
                
                # Styles/Classes that define a CTA
                cta_classes = ['btn', 'btn-primary', 'btn-outline-light', 'btn-whatsapp', 'fc-wa-link', 'cta-card-glass', 'cta-card-prominent']
                if any(c in class_str for c in cta_classes):
                    is_cta = True
                
                # Destinations that define a CTA
                cta_destinations = ['/contact.html', '/request-site-assessment-singapore.html', 'wa.me', 'tel:', 'mailto:']
                if any(d in href for d in cta_destinations):
                    is_cta = True
                
                if not is_cta:
                    continue

                # Exclusions
                if "Explore" in label and 'btn' not in class_str:
                    continue
                
                # Position Detection
                context_pre = main_content[max(0, match.start()-1000):match.start()].lower()
                
                section = "Inline body link"
                if 'class="hero' in context_pre or 'id="hero' in context_pre or '<header' in context_pre: # header sometimes used for hero
                    section = "Hero"
                    if 'btn-primary' in class_str: section += " (primary)"
                    elif 'btn-outline-light' in class_str: section += " (secondary)"
                elif 'cta-section' in context_pre or 'cta-high-impact' in context_pre:
                    section = "Final CTA"
                    if 'btn-primary' in class_str: section += " (primary)"
                    else: section += " (secondary)"
                elif 'cta-card' in context_pre:
                    section = "Mid-page card"
                elif 'fc-wa-link' in class_str:
                    section = "Founder card"
                elif 'whatsapp-btn' in class_str or 'floating' in class_str:
                    section = "Floating WA button"
                
                # UTM / Query Params
                query = ""
                if '?' in href:
                    query = href.split('?')[1]
                
                results.append({
                    "path": "/" + rel_path.replace('\\', '/'),
                    "type": page_type,
                    "section": section,
                    "label": label if label else "[icon only]",
                    "dest": href,
                    "class": class_str,
                    "utm": query if query else "—",
                    "type_rank": PAGE_TYPES.index(page_type) if page_type in PAGE_TYPES else 99
                })
                
                labels_counter[label] += 1
                dest_counter[href] += 1

    # Sorting
    results.sort(key=lambda x: (x['type_rank'], x['path']))

    # OUTPUT TABLE
    print("| Page Path | Page Type | Section/Position | CTA Label | Destination | Style/Class | UTM/Query Params |")
    print("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    for r in results:
        print(f"| {r['path']} | {r['type']} | {r['section']} | {r['label']} | {r['dest']} | {r['class']} | {r['utm']} |")

    # SUMMARY
    print("\n## Summary")
    
    print("\n### 1. CTA Label Frequency")
    for l, count in labels_counter.most_common():
        print(f"- {l} — {count} occurrences")

    print("\n### 2. Destination Frequency")
    for d, count in dest_counter.most_common():
        print(f"- {d} — {count} occurrences")

    print("\n### 3. Anomalies & Inconsistencies")
    # Check for same label pointing to different destinations
    label_to_dest = collections.defaultdict(set)
    for r in results:
        label_to_dest[r['label']].add(r['dest'])
    for l, dests in label_to_dest.items():
        if len(dests) > 1:
            anomalies.append(f"Label '{l}' points to multiple destinations: {', '.join(dests)}")

    # Check for missing UTMs on key pages
    for r in results:
        if r['section'].startswith("Hero") and r['dest'].startswith('/request') and 'intent=' not in r['utm']:
            anomalies.append(f"Hero CTA on {r['path']} missing 'intent' parameter in destination.")

    for a in anomalies:
        print(f"- {a}")

    print("\n### 4. Pages NOT scanned")
    for s in skipped:
        print(f"- {s}")

if __name__ == "__main__":
    run_audit()
