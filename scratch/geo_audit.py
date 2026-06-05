import os
import re
import json

def analyze_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lower_content = content.lower()
    except Exception as e:
        return {"error": str(e)}

    # Phase 2: 11-Point GEO
    # 1. Main Service: <h1> exists
    has_h1 = bool(re.search(r'<h1[^>]*>.*?</h1\s*>', content, re.IGNORECASE | re.DOTALL))
    
    # 2. Sub-services/Locality: `<nav>` with sub-links
    has_nav = bool(re.search(r'<nav[^>]*>.*?</nav\s*>', content, re.IGNORECASE | re.DOTALL))
    has_submenus = bool(re.search(r'class="[^"]*dropdown[^"]*"', lower_content))
    
    # 3. Cost Transparency
    has_cost = bool(re.search(r'\b(price|pricing|cost|costs|quote|quotes|tier|tiers|estimate)\b|\$', lower_content))
    
    # 4. Competitive Alternatives
    has_comp = bool(re.search(r'\b(vs\.|versus|compared to|alternative|alternatives|competitor|competitors)\b', lower_content))
    
    # 5. Locality/Geography
    has_geo = bool(re.search(r'\b(singapore|address|location|map)\b', lower_content))
    
    # 6. Mentions/Validation
    has_val = bool(re.search(r'\b(testimonial|testimonials|review|reviews|case study|case studies|client|clients)\b', lower_content))
    
    # 7. Step-by-Step Process
    has_steps = bool(re.search(r'\b(how it works|step 1|step one)\b|<ol[^>]*>', lower_content))
    
    # 8. Audience Profiling
    has_audience = bool(re.search(r'\b(who this is for|ideal for|not for|who shouldn\'t|target audience)\b', lower_content))
    
    # 9. Risk Reversal
    has_risk = bool(re.search(r'\b(guarantee|guaranteed|warranty|cancellation|support|sla|refund|response time)\b', lower_content))
    
    # 10. Nuance/Myths
    has_myth = bool(re.search(r'\b(myth|myths|misconception|misconceptions|truth|fact|common belief)\b', lower_content))
    
    # 11. Prerequisites
    has_pre = bool(re.search(r'\b(prerequisite|prerequisites|preparation|checklist|what you need to prepare)\b', lower_content))
    
    # Phase 3: Technical Parsing Verification
    has_json_ld = bool(re.search(r'<script type="application/ld\+json">', lower_content))
    
    has_semantic = {
        'section': bool(re.search(r'<section[^>]*>', lower_content)),
        'article': bool(re.search(r'<article[^>]*>', lower_content)),
        'nav': has_nav
    }

    return {
        'filepath': filepath,
        'has_h1': has_h1,
        'has_nav': has_nav,
        'has_submenus': has_submenus,
        'has_cost': has_cost,
        'has_comp': has_comp,
        'has_geo': has_geo,
        'has_val': has_val,
        'has_steps': has_steps,
        'has_audience': has_audience,
        'has_risk': has_risk,
        'has_myth': has_myth,
        'has_pre': has_pre,
        'has_json_ld': has_json_ld,
        'has_semantic': has_semantic
    }

def main():
    root_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"
    results = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'node_modules' in dirpath or '.git' in dirpath:
            continue
        for file in filenames:
            if file.endswith('.html'):
                full_path = os.path.join(dirpath, file)
                rel_path = os.path.relpath(full_path, root_dir)
                res = analyze_file(full_path)
                res['rel_path'] = rel_path
                results.append(res)
    
    with open(os.path.join(root_dir, 'scratch', 'geo_audit_results.json'), 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
