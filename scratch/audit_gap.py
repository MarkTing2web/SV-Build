import os
import re

insights_dir = r"C:\Projects\SV-Build\insights"
output_dir = r"C:\Projects\SV-Build\_ai"
os.makedirs(output_dir, exist_ok=True)

slugs = [
    "access-control-upgrade-drivers-singapore",
    "guarding-technology-singapore",
    "hdb-landed-condo-security-differences",
    "home-security-system-cost-singapore",
    "how-card-access-works",
    "how-to-choose-cctv",
    "intercom-system-evolution-singapore",
    "cctv-pdpa-compliance",
    "condo-intercom-upgrade",
    "condo-security-upgrade-timeline",
    "false-alarms",
    "gate-remote-smartphone",
    "alarm-communication-paths",
    "alarm-internet-cut",
    "alarm-panel",
    "alarm-power-cut",
    "alarm-response",
    "alarm-siren",
    "alarm-system-lifespan",
    "alarm-upgrade-or-replace",
    "alarm-wiring-reuse",
    "auto-gate-motor",
    "burglar-alarm-design",
    "burglar-alarm-detectors-sensors",
    "cctv-ai-upgrade",
    "cctv-retail-analytics",
    "false-alarm-causes",
    "how-alarm-works",
    "mechanical-locks-not-enough",
    "monitoring-station",
    "pstn-to-ip",
    "access-control-multi-door",
    "alarm-monitoring-history",
    "alarm-panel-polling",
    "alarm-usage-habits",
    "architect-security-guide",
    "break-in-nearby-security-review",
    "cctv-cable-upgrade",
    "cctv-system-components",
    "cctv-vs-alarm",
    "choose-intercom-for-home",
    "compare-security-integrators",
    "condo-security-upgrade-proposals",
    "installer-leaves",
    "lpr-vs-rfid-condo",
    "mcst-security-tender",
    "modern-detectors",
    "network-security-systems",
    "security-assessment-10-things",
    "self-monitoring-vs-cms",
    "singapore-licensing",
    "system-repair-or-replace",
    "video-verification",
]

results = []

for slug in slugs:
    filepath = os.path.join(insights_dir, f"{slug}.html")
    if not os.path.exists(filepath):
        results.append((slug, "FILE MISSING", "FILE MISSING", "FILE MISSING"))
        continue

    with open(filepath, encoding='utf-8', errors='ignore') as f:
        content = f.read()

    has_takeaways = "article-takeaways" in content
    has_in_short  = "In Short" in content
    has_faq       = bool(re.search(r'[Ff]requently asked', content))

    results.append((slug, has_takeaways, has_in_short, has_faq))

# Write report
lines = []
lines.append("# Insights Gap Audit — 53 Older Articles")
lines.append("## Checking: Key Takeaways · In Short · FAQ")
lines.append("")

missing_takeaways = [r[0] for r in results if not r[1]]
missing_in_short  = [r[0] for r in results if not r[2]]
missing_faq       = [r[0] for r in results if not r[3]]

lines.append("## Summary")
lines.append("")
lines.append(f"| Element | Missing | Present |")
lines.append(f"|---|---|---|")
lines.append(f"| Key Takeaways | {len(missing_takeaways)} | {53 - len(missing_takeaways)} |")
lines.append(f"| In Short | {len(missing_in_short)} | {53 - len(missing_in_short)} |")
lines.append(f"| FAQ | {len(missing_faq)} | {53 - len(missing_faq)} |")
lines.append("")

lines.append("## Full Article Status")
lines.append("")
lines.append("| Slug | Key Takeaways | In Short | FAQ |")
lines.append("|---|---|---|---|")
for slug, kt, ins, faq in results:
    kt_str  = "✅" if kt  is True  else ("❌" if kt  is False else kt)
    ins_str = "✅" if ins is True  else ("❌" if ins is False else ins)
    faq_str = "✅" if faq is True  else ("❌" if faq is False else faq)
    lines.append(f"| {slug} | {kt_str} | {ins_str} | {faq_str} |")

lines.append("")
lines.append("## Missing Key Takeaways")
for s in missing_takeaways:
    lines.append(f"- {s}")

lines.append("")
lines.append("## Missing In Short")
for s in missing_in_short:
    lines.append(f"- {s}")

lines.append("")
lines.append("## Missing FAQ")
for s in missing_faq:
    lines.append(f"- {s}")

with open(os.path.join(output_dir, "insights-gap-audit.md"), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Articles scanned: {len(results)}")
print(f"Missing Key Takeaways: {len(missing_takeaways)}")
print(f"Missing In Short:      {len(missing_in_short)}")
print(f"Missing FAQ:           {len(missing_faq)}")
