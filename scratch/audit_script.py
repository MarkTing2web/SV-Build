import os
import re
import html
import sys

# Force UTF-8 output for Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def extract_text(tag_pattern, content):
    match = re.search(tag_pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        text = match.group(1)
        # Remove tags inside
        text = re.sub(r'<[^>]+>', '', text)
        # Remove multiple whitespaces/newlines
        text = re.sub(r'\s+', ' ', text)
        text = html.unescape(text).strip()
        return text if text else "empty"
    return "empty"

def truncate_subtitle(text):
    if text == "empty" or text == "no hero found": return text
    # Truncate to first sentence
    sentences = re.split(r'(?<=[.!?])\s+', text)
    if not sentences: return text
    first_sentence = sentences[0]
    words = first_sentence.split()
    if len(words) > 20:
        return " ".join(words[:20]) + "..."
    return first_sentence

def audit_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return None, None

    # Extract Hero Section
    # Look for header or section with hero-high-impact
    hero_match = re.search(r'<(?:header|section)[^>]+class="[^"]*hero-high-impact[^"]*"[^>]*>(.*?)</(?:header|section)>', content, re.DOTALL | re.IGNORECASE)
    hero_data = {
        'eyebrow': 'no hero found',
        'h1': 'no hero found',
        'subtitle': 'no hero found'
    }
    if hero_match:
        hero_content = hero_match.group(1)
        hero_data['eyebrow'] = extract_text(r'<(?:span|div|p)[^>]+class="[^"]*(?:eyebrow-light|eyebrow)[^"]*"[^>]*>(.*?)</(?:span|div|p)>', hero_content)
        hero_data['h1'] = extract_text(r'<h1[^>]*>(.*?)</h1>', hero_content)
        hero_data['subtitle'] = extract_text(r'<(?:p|div)[^>]+class="[^"]*(?:hero-subtitle-main|subtitle)[^"]*"[^>]*>(.*?)</(?:p|div)>', hero_content)
        if hero_data['subtitle'] == "empty":
            # Find the first <p> that isn't the eyebrow or part of btn group
            p_matches = re.findall(r'<p[^>]*>(.*?)</p>', hero_content, re.DOTALL | re.IGNORECASE)
            for p_text in p_matches:
                clean_p = re.sub(r'<[^>]+>', '', p_text).strip()
                if clean_p:
                    hero_data['subtitle'] = clean_p
                    break
        hero_data['subtitle'] = truncate_subtitle(hero_data['subtitle'])

    # Extract CTA Section
    # Look for section carrying BOTH .cta-section and .cta-high-impact
    cta_match = re.search(r'<section[^>]+class="[^"]*cta-section[^"]*cta-high-impact[^"]*"[^>]*>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
    if not cta_match:
        cta_match = re.search(r'<section[^>]+class="[^"]*cta-high-impact[^"]*cta-section[^"]*"[^>]*>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
    
    cta_data = {
        'h2': 'no CTA found',
        'subtitle': 'no CTA found',
        'trust_note': 'no CTA found',
        'button': 'no CTA found'
    }
    if cta_match:
        cta_content = cta_match.group(1)
        cta_data['h2'] = extract_text(r'<h2[^>]*>(.*?)</h2>', cta_content)
        cta_data['subtitle'] = extract_text(r'<(?:p|div)[^>]+class="[^"]*subtitle[^"]*"[^>]*>(.*?)</(?:p|div)>', cta_content)
        if cta_data['subtitle'] == "empty":
            # first <p>
            cta_data['subtitle'] = extract_text(r'<p[^>]*>(.*?)</p>', cta_content)
        
        cta_data['trust_note'] = extract_text(r'<(?:p|span)[^>]+class="[^"]*cta-trust-note[^"]*"[^>]*>(.*?)</(?:p|span)>', cta_content)
        if cta_data['trust_note'] == "empty":
             cta_data['trust_note'] = "none"
             
        cta_data['button'] = extract_text(r'<a[^>]+class="[^"]*btn[^"]*"[^>]*>(.*?)</a>', cta_content)

    return hero_data, cta_data

def main():
    root_dir = r"c:\Projects\SV-Build"
    
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        if "templates" in root: continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    results = []
    for filepath in html_files:
        rel_path = os.path.relpath(filepath, root_dir)
        hero, cta = audit_file(filepath)
        if hero:
            results.append({
                'path': rel_path,
                'hero': hero,
                'cta': cta
            })

    # Sorting
    def sort_key(item):
        path = item['path'].replace("\\", "/")
        order = ["solutions/", "systems/", "resources/", "insights/", "portfolio/", "brands/", ""]
        for i, prefix in enumerate(order):
            if path.startswith(prefix) and (prefix != "" or "/" not in path):
                return (i, path)
        return (len(order), path)

    results.sort(key=sort_key)

    output_path = os.path.join(root_dir, "scratch", "audit_results.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        # Print table
        f.write("| Page file path | Hero eyebrow | Hero h1 | Hero subtitle (p) | CTA h2 | CTA subtitle (p) | CTA trust note | CTA button label |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
        for r in results:
            hp = r['hero']
            cp = r['cta']
            # Escape pipe symbols for markdown
            row = [
                r['path'].replace("\\", "/"),
                hp['eyebrow'].replace("|", "\\|"),
                hp['h1'].replace("|", "\\|"),
                hp['subtitle'].replace("|", "\\|"),
                cp['h2'].replace("|", "\\|"),
                cp['subtitle'].replace("|", "\\|"),
                cp['trust_note'].replace("|", "\\|"),
                cp['button'].replace("|", "\\|")
            ]
            f.write("| " + " | ".join(row) + " |\n")
    print(f"Audit complete. Results written to {output_path}")

if __name__ == "__main__":
    main()
