import json
import os

def generate_report():
    with open('d:\\Ler Wee Meng\\Project-Web\\SV-Build\\scratch\\geo_audit_results.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Filter out templates
    files = [d for d in data if 'templates' not in d['rel_path'] and '_template' not in d['rel_path']]

    total_files = len(files)
    
    # Calculate scores
    scores = {
        'Main Service': sum(1 for d in files if d['has_h1']),
        'Sub-services/Locality': sum(1 for d in files if d['has_nav'] or d['has_submenus']),
        'Cost Transparency': sum(1 for d in files if d['has_cost']),
        'Competitive Alternatives': sum(1 for d in files if d['has_comp']),
        'Locality/Geography': sum(1 for d in files if d['has_geo']),
        'Mentions/Validation': sum(1 for d in files if d['has_val']),
        'Step-by-Step Process': sum(1 for d in files if d['has_steps']),
        'Audience Profiling': sum(1 for d in files if d['has_audience']),
        'Risk Reversal': sum(1 for d in files if d['has_risk']),
        'Nuance/Myths': sum(1 for d in files if d['has_myth']),
        'Prerequisites': sum(1 for d in files if d['has_pre']),
        'JSON-LD': sum(1 for d in files if d['has_json_ld']),
        'Semantic HTML': sum(1 for d in files if d['has_semantic']['section'] or d['has_semantic']['article'])
    }

    # Group by directory (templates/sub-menus)
    dirs = {}
    for d in files:
        dirname = os.path.dirname(d['rel_path'])
        if not dirname:
            dirname = "root"
        if dirname not in dirs:
            dirs[dirname] = []
        dirs[dirname].append(d)

    report = []
    report.append("# Generative Engine Optimization (GEO) & Technical SEO Audit Report")
    report.append("\n## Executive Summary")
    
    total_checks = total_files * 11
    passed_checks = sum(scores.values()) - scores['JSON-LD'] - scores['Semantic HTML']
    readiness_score = (passed_checks / total_checks) * 100 if total_checks else 0
    
    report.append(f"**Overall AI Readiness Score: {readiness_score:.1f}%**")
    report.append(f"Total HTML Pages Scanned (excluding templates): {total_files}")
    report.append("\n*The AI Readiness Score reflects the percentage of our core pages that contain the 11 critical informational blocks AI search engines look for.*")
    
    report.append("\n### High-Level Compliance by Category:")
    for k, v in scores.items():
        pct = (v / total_files) * 100 if total_files else 0
        report.append(f"- **{k}:** {pct:.1f}% ({v}/{total_files} pages)")

    report.append("\n## Checklist Map by Section")
    for dirname, dir_files in dirs.items():
        report.append(f"\n### Section: `{dirname}` ({len(dir_files)} pages)")
        
        # Calculate section stats
        sec_scores = {
            'Cost': sum(1 for d in dir_files if d['has_cost']),
            'Comp': sum(1 for d in dir_files if d['has_comp']),
            'Geo': sum(1 for d in dir_files if d['has_geo']),
            'Val': sum(1 for d in dir_files if d['has_val']),
            'Steps': sum(1 for d in dir_files if d['has_steps']),
            'Aud': sum(1 for d in dir_files if d['has_audience']),
            'Risk': sum(1 for d in dir_files if d['has_risk']),
            'Myth': sum(1 for d in dir_files if d['has_myth']),
            'Pre': sum(1 for d in dir_files if d['has_pre']),
            'JSON-LD': sum(1 for d in dir_files if d['has_json_ld']),
            'Semantic': sum(1 for d in dir_files if d['has_semantic']['section'] or d['has_semantic']['article'])
        }
        
        report.append("| Metric | Pass Rate |")
        report.append("|---|---|")
        for k, v in sec_scores.items():
            pct = (v / len(dir_files)) * 100
            status = "✅" if pct > 70 else ("⚠️" if pct > 30 else "❌")
            report.append(f"| {k} | {status} {pct:.0f}% |")

    report.append("\n## Critical Missing Information Blocks")
    report.append("The following key files have significant informational gaps (missing >7 of the 11 key GEO criteria):")
    
    for d in files:
        passed = sum([d['has_h1'], d['has_nav'] or d['has_submenus'], d['has_cost'], d['has_comp'], 
                      d['has_geo'], d['has_val'], d['has_steps'], d['has_audience'], 
                      d['has_risk'], d['has_myth'], d['has_pre']])
        if passed < 4:
            report.append(f"- `{d['rel_path']}` (Passed only {passed}/11 points)")

    report.append("\n## Phase 3: Technical Parsing Verification")
    report.append(f"- **JSON-LD Schema Markup:** Present on {scores['JSON-LD']}/{total_files} pages. (Most pages are missing structured data like `FAQPage`, `LocalBusiness`, or `Product`).")
    report.append(f"- **Semantic HTML5:** Present on {scores['Semantic HTML']}/{total_files} pages. (Good usage of `<section>`, `<article>`, `<nav>` across most templates).")

    report.append("\n## Implementation Plan")
    report.append("### Step 1: Inject JSON-LD Global Schema")
    report.append("- Create a standard `LocalBusiness` JSON-LD snippet targeting Singapore and inject it into the global header or footer include.")
    report.append("- Add `FAQPage` schema dynamically to pages with Q&A sections.")
    
    report.append("### Step 2: Standardize Missing Content Blocks")
    report.append("- **Audience Profiling:** Add a \"Who This is For / Not For\" component block to `solutions/*` and `portfolio/*` templates.")
    report.append("- **Competitive Alternatives:** Add \"Why Choose Us over Alternatives\" section in core service pages.")
    report.append("- **Nuance/Myths & Prerequisites:** Create reusable `<section>` blocks for common objections and preparation checklists and inject into the `templates/_template-solution-standard.html` and `templates/_template-portfolio-*.html`.")
    
    report.append("### Step 3: Enhance Risk Reversal & Cost Transparency")
    report.append("- Explicitly mention SLAs, support response times, and general pricing tiers/estimates on solution and systems pages to improve AI extraction.")

    with open('d:\\Ler Wee Meng\\Project-Web\\SV-Build\\scratch\\geo_audit_report.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

if __name__ == "__main__":
    generate_report()
