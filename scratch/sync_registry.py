import re
import json

orphans = [
    "10-tips-securing-your-premises",
    "after-security-installation-support",
    "ai-analytics-hikvision",
    "analogue-to-ip-migration",
    "architect-id-guide-security",
    "condo-security-upgrade-proposal",
    "condo-security-upgrade-quotes",
    "how-burglar-alarm-works",
    "how-ip-cctv-works",
    "how-to-choose-auto-gate-motor",
    "how-to-choose-multi-door-access",
    "security-system-refresh",
    "upgrade-condo-intercom",
    "upgrade-existing-security-system",
    "upgrade-or-repair",
    "using-your-burglar-alarm",
    "why-mechanical-locks-not-enough",
    "wifi-remote-control-auto-gate"
]

new_41 = """
  { slug: "monitoring-station",             title: "What Happens at a Security Monitoring Centre When Your Alarm Goes Off?",         category: "Alarm & Intrusion",  date: "2026-02-10", tags: ["burglar-alarm","alarm-monitoring","monitoring-centre","singapore"],    excerpt: "Most homeowners have never seen inside a security monitoring centre. Learn how operators receive alarm signals, verify events, contact keyholders and coordinate police response in Singapore.",                                                                                             image: "monitoring-station-feature.webp" },
  { slug: "alarm-response",                 title: "What Really Happens When Your Alarm Goes Off?",                                  category: "Alarm & Intrusion",  date: "2026-02-13", tags: ["burglar-alarm","alarm-response","keyholders","singapore"],            excerpt: "What really happens after your burglar alarm goes off? Learn how monitoring centres verify alarms, activate police response, work with keyholders and manage real-world alarm incidents behind the scenes.",                                                                               image: "alarm-response-feature.webp" },
  { slug: "video-verification",             title: "Video Verification — Seeing the Alarm Before Responding",                       category: "Alarm & Intrusion",  date: "2026-02-16", tags: ["burglar-alarm","video-verification","alarm-monitoring","singapore"],  excerpt: "Video verification allows monitoring centres to see what triggered an alarm before dispatching police. Learn how it works, when it matters, and why it reduces unnecessary call-outs.",                                                                                                   image: "video-verification-feature.webp" },
  { slug: "false-alarms",                   title: "Why False Alarms Matter More Than You Think",                                    category: "Alarm & Intrusion",  date: "2026-02-19", tags: ["burglar-alarm","false-alarms","alarm-monitoring","singapore"],        excerpt: "False alarms are more than just an annoyance. Learn how they affect homeowners, monitoring centres and police resources, why alarm verification matters and how proper system design helps reduce unnecessary alarm activations.",                                                          image: "false-alarms-feature.webp" },
  { slug: "alarm-siren",                    title: "Why Burglar Alarm Sirens Don't Ring Forever",                                   category: "Alarm & Intrusion",  date: "2026-02-22", tags: ["burglar-alarm","alarm-siren","alarm-design","singapore"],             excerpt: "Why do burglar alarm sirens stop after a few minutes? Learn how modern alarm systems use sirens, strobe lights, mobile apps and monitoring centres to protect your property without creating unnecessary disturbance.",                                                                     image: "alarm-siren-feature.webp" },
  { slug: "false-alarm-causes",             title: "The Most Common Causes of False Alarms — and How to Prevent Them",              category: "Alarm & Intrusion",  date: "2026-02-25", tags: ["burglar-alarm","false-alarms","alarm-detectors","singapore"],         excerpt: "Why do burglar alarms go off when nobody is breaking in? Learn the most common causes of false alarms — from user mistakes and sunlight to pets, air-conditioning and poor detector placement.",                                                                                         image: "false-alarm-causes-feature.webp" },
  { slug: "modern-detectors",               title: "Why Modern Motion Detectors Are Better Than Ever",                               category: "Alarm & Intrusion",  date: "2026-02-28", tags: ["burglar-alarm","motion-detectors","pir-sensors","singapore"],         excerpt: "Motion detectors have evolved from simple ultrasonic sensors to intelligent devices capable of analysing movement patterns and reducing false alarms. Learn how modern detector technology improves security.",                                                                             image: "modern-detectors-feature.webp" },
  { slug: "singapore-licensing",            title: "Why Security System Installers Must Be Licensed in Singapore",                   category: "Alarm & Intrusion",  date: "2026-03-03", tags: ["burglar-alarm","singapore-licensing","psia","singapore"],             excerpt: "Why do security system installers need a licence in Singapore? Learn how false alarms and evolving technology led to the professionalisation of the security industry and why licensing matters to property owners.",                                                                       image: "singapore-licensing-feature.webp" },
  { slug: "alarm-monitoring-history",       title: "How Alarm Monitoring Evolved in Singapore",                                     category: "Alarm & Intrusion",  date: "2026-03-06", tags: ["burglar-alarm","alarm-monitoring","history","singapore"],             excerpt: "From telephone dial-up to always-on IP monitoring — how the alarm monitoring industry in Singapore evolved over four decades and what it means for property owners today.",                                                                                                               image: "alarm-monitoring-history-feature.webp" },
  { slug: "alarm-panel-polling",            title: "What Is Alarm Panel Polling and Why Does It Matter?",                           category: "Alarm & Intrusion",  date: "2026-03-09", tags: ["burglar-alarm","alarm-panel","polling","alarm-monitoring"],           excerpt: "Polling is how a monitoring centre knows your alarm panel is still online. Learn how it works, what happens when polling fails, and why it matters for the reliability of your alarm monitoring service.",                                                                                 image: "alarm-panel-polling-feature.webp" },
  { slug: "alarm-communication-paths",      title: "How Your Alarm Communicates With the Monitoring Centre",                        category: "Alarm & Intrusion",  date: "2026-03-12", tags: ["burglar-alarm","alarm-monitoring","ip-monitoring","singapore"],       excerpt: "Your alarm panel uses one or more communication paths to report to the monitoring centre. Learn the difference between IP, cellular, and dual-path communication and which provides the most reliable protection.",                                                                        image: "alarm-communication-paths-feature.webp" },
  { slug: "pstn-to-ip",                     title: "From PSTN to IP Monitoring — Why the Phone Line Is No Longer Enough",           category: "Alarm & Intrusion",  date: "2026-03-15", tags: ["burglar-alarm","alarm-monitoring","ip-monitoring","singapore"],       excerpt: "How did alarm monitoring evolve from telephone lines to always-on IP connectivity? Learn why PSTN networks are being retired and what modern IP monitoring means for alarm reliability in Singapore.",                                                                                     image: "pstn-to-ip-feature.webp" },
  { slug: "self-monitoring-vs-cms",         title: "Should You Monitor Your Alarm Yourself or Use a Monitoring Centre?",            category: "Alarm & Intrusion",  date: "2026-03-18", tags: ["burglar-alarm","alarm-monitoring","self-monitoring","singapore"],     excerpt: "Self-monitoring or professional alarm monitoring? Learn the advantages, limitations and real-world considerations behind both approaches before deciding which is right for your home or business.",                                                                                       image: "self-monitoring-vs-cms-feature.webp" },
  { slug: "alarm-wiring-reuse",             title: "Can I Reuse My Existing Alarm Wiring When Upgrading?",                         category: "Alarm & Intrusion",  date: "2026-03-21", tags: ["burglar-alarm","alarm-upgrade","alarm-wiring","singapore"],          excerpt: "Can you reuse existing alarm wiring when upgrading a burglar alarm system? Learn when cables and detectors can be retained, what usually needs replacing and how homeowners can reduce costs during an alarm upgrade.",                                                                     image: "alarm-wiring-reuse-feature.webp" },
  { slug: "alarm-upgrade-or-replace",       title: "Should I Upgrade or Replace My Burglar Alarm System?",                         category: "Alarm & Intrusion",  date: "2026-03-24", tags: ["burglar-alarm","alarm-upgrade","alarm-replacement","singapore"],     excerpt: "Should you upgrade or replace your burglar alarm system? Learn how to assess ageing alarm panels, detectors, communications and wiring so you can make the most cost-effective decision.",                                                                                               image: "alarm-upgrade-or-replace-feature.webp" },
  { slug: "alarm-system-lifespan",          title: "How Long Should a Burglar Alarm System Last?",                                 category: "Alarm & Intrusion",  date: "2026-03-27", tags: ["burglar-alarm","alarm-maintenance","alarm-lifespan","singapore"],    excerpt: "How long should a burglar alarm system last? Learn the expected lifespan of alarm panels, detectors, batteries and wiring, and discover when upgrading makes more sense than replacing the entire system.",                                                                               image: "alarm-system-lifespan-feature.webp" },
  { slug: "cctv-vs-alarm",                  title: "CCTV vs Burglar Alarm — Do You Need Both?",                                    category: "Alarm & Intrusion",  date: "2026-03-30", tags: ["burglar-alarm","cctv","security-planning","singapore"],              excerpt: "CCTV and burglar alarms serve different security functions. Learn when each system is most effective, how they work together, and how to decide which is the right starting point for your property.",                                                                                    image: "cctv-vs-alarm-feature.webp" },
  { slug: "alarm-internet-cut",             title: "What Happens to My Alarm If the Internet Is Cut?",                             category: "Alarm & Intrusion",  date: "2026-04-02", tags: ["burglar-alarm","alarm-monitoring","ip-monitoring","singapore"],       excerpt: "What happens to your burglar alarm system when the internet goes down? Learn how modern alarm systems use dual-path communication to maintain monitoring even when the primary connection fails.",                                                                                         image: "alarm-internet-cut-feature.webp" },
  { slug: "alarm-power-cut",                title: "What Happens to My Alarm During a Power Cut?",                                 category: "Alarm & Intrusion",  date: "2026-04-05", tags: ["burglar-alarm","alarm-panel","backup-power","singapore"],             excerpt: "What happens to your burglar alarm during a power cut? Learn how backup batteries work, how long they last, and what steps to take to ensure your alarm continues protecting your property during an outage.",                                                                            image: "alarm-power-cut-feature.webp" },
  { slug: "how-alarm-works",                title: "How a Burglar Alarm System Actually Works — From Trigger to Response",          category: "Alarm & Intrusion",  date: "2026-04-08", tags: ["burglar-alarm","how-it-works","alarm-monitoring","singapore"],       excerpt: "From the moment a detector triggers to the moment police are dispatched — a clear explanation of how a modern burglar alarm system works from end to end.",                                                                                                                               image: "how-alarm-works-feature.webp" },
  { slug: "alarm-panel",                    title: "What Does an Alarm Panel Actually Do?",                                        category: "Alarm & Intrusion",  date: "2026-04-08", tags: ["burglar-alarm","alarm-panel","controller","singapore"],               excerpt: "The alarm panel is the brain of the entire system. Learn how it manages zones, communicates with monitoring centres, and why the panel specification matters as much as the detectors connected to it.",                                                                                  image: "alarm-panel-feature.webp" },
  { slug: "alarm-usage-habits",             title: "Bad Alarm Habits That Undermine Your Security",                                category: "Security Planning",  date: "2026-04-23", tags: ["burglar-alarm","security-planning","homeowner","singapore"],         excerpt: "The most sophisticated alarm system is only as effective as the habits of the people using it. Learn the most common usage mistakes that leave properties vulnerable — and the simple fixes for each.",                                                                                    image: "alarm-usage-habits-feature.webp" },
  { slug: "system-repair-or-replace",       title: "Repair or Replace? How to Decide What to Do With an Ageing Security System",  category: "Security Planning",  date: "2026-04-26", tags: ["security-planning","upgrade","maintenance","singapore"],             excerpt: "When a security system starts failing, the repair-or-replace decision involves more than just the cost of the next service call. Learn the framework for making the right decision for your property.",                                                                                   image: "system-repair-or-replace-feature.webp" },
  { slug: "security-assessment-10-things",  title: "10 Things a Security Assessment Should Tell You",                              category: "Security Planning",  date: "2026-04-11", tags: ["security-planning","security-assessment","homeowner","singapore"],   excerpt: "A security assessment is only valuable if it tells you something actionable. Learn the ten questions every property security assessment should answer — and what to do when it does not.",                                                                                                 image: "security-assessment-10-things-feature.webp" },
  { slug: "break-in-nearby-security-review",title: "There Has Been a Break-In Nearby. What Should You Do?",                       category: "Security Planning",  date: "2026-04-14", tags: ["security-planning","break-in","homeowner","singapore"],              excerpt: "A break-in in your neighbourhood is a clear signal to review your own security. Learn what to assess, what to improve, and how to respond without overreacting.",                                                                                                                        image: "break-in-nearby-feature.webp" },
  { slug: "installer-leaves",               title: "What to Do When Your Security Installer Leaves the Job",                       category: "Security Planning",  date: "2026-04-17", tags: ["security-planning","after-sales","maintenance","singapore"],         excerpt: "What should you do in the first week after your security system is installed? Learn the steps that ensure your system is working correctly, your team is trained, and you are not left without support.",                                                                                 image: "installer-leaves-feature.webp" },
  { slug: "network-security-systems",       title: "Why Your Security System Is Only as Good as Your Network",                     category: "Security Planning",  date: "2026-04-20", tags: ["security-planning","network","ip-systems","singapore"],              excerpt: "IP cameras, intercoms, access control panels and alarm systems all depend on the network. Learn the most common network problems that cause security systems to fail — and how to prevent them.",                                                                                          image: "network-security-systems-feature.webp" },
  { slug: "cctv-system-components",         title: "The Four Components That Make Up a CCTV System",                              category: "Security Planning",  date: "2026-05-02", tags: ["cctv","security-planning","nvr","singapore"],                        excerpt: "Understanding the four main components of a CCTV system — cameras, recorder, storage, and network — is the starting point for specifying, installing, and maintaining any surveillance installation.",                                                                                   image: "cctv-system-components-feature.webp" },
  { slug: "access-control-multi-door",      title: "How to Choose a Multi-Door Access Control System",                             category: "Security Planning",  date: "2026-05-05", tags: ["access-control","multi-door","security-planning","singapore"],       excerpt: "A single-door access reader is straightforward. A multi-door system serving multiple areas, user groups, and schedules requires a different approach. Learn how to specify and design access control that scales.",                                                                        image: "access-control-multi-door-feature.webp" },
  { slug: "mechanical-locks-not-enough",    title: "Why Mechanical Locks Are No Longer Enough",                                    category: "Security Planning",  date: "2026-05-08", tags: ["access-control","locks","security-planning","singapore"],             excerpt: "A mechanical lock on every door is the starting point for physical security — not the end point. Learn why mechanical locks alone leave significant gaps and what electronic access control adds.",                                                                                        image: "mechanical-locks-not-enough-feature.webp" },
  { slug: "auto-gate-motor",                title: "Choosing the Right Auto Gate Motor for Your Property",                         category: "Security Planning",  date: "2026-05-11", tags: ["auto-gate","gate-motor","security-planning","singapore"],            excerpt: "The gate comes first, the motor comes second. Learn how to match a gate motor to your gate's weight, usage frequency, and property type — and what happens when the specification is wrong.",                                                                                           image: "auto-gate-motor-feature.webp" },
  { slug: "condo-intercom-upgrade",         title: "Upgrading Your Condominium Intercom System — What Councils Need to Know",      category: "Security Planning",  date: "2026-05-14", tags: ["intercom","condominium-security","mcst","singapore"],                excerpt: "A condominium intercom upgrade is one of the most impactful and most complex security projects an MCST can undertake. Learn what to plan for, what to expect, and what questions to ask before committing.",                                                                              image: "condo-intercom-upgrade-feature.webp" },
  { slug: "gate-remote-smartphone",         title: "Controlling Your Gate With a Smartphone — What You Need to Know",              category: "Security Planning",  date: "2026-05-17", tags: ["auto-gate","smart-home","security-planning","singapore"],            excerpt: "Smartphone control for auto gates is one of the most requested features from Singapore homeowners. Learn how it works, what it requires, and what happens when the internet or power goes down.",                                                                                         image: "gate-remote-smartphone-feature.webp" },
  { slug: "lpr-vs-rfid-condo",              title: "LPR vs RFID: Which Vehicle Access System Is Better for Your Condominium?",    category: "Security Planning",  date: "2026-05-20", tags: ["condominium-security","vehicle-access","mcst","singapore"],          excerpt: "Should your condominium choose RFID or Licence Plate Recognition for vehicle access? Learn the operational differences, how they affect resident experience and administration, and why many Singapore estates are moving towards LPR.",                                                   image: "lpr-vs-rfid-condo-feature.webp" },
  { slug: "cctv-pdpa-compliance",           title: "CCTV and PDPA — What Singapore Property Owners Need to Know",                 category: "CCTV",               date: "2026-05-23", tags: ["cctv","pdpa","compliance","singapore"],                              excerpt: "Installing CCTV in Singapore comes with data protection obligations under the Personal Data Protection Act. Learn what the law requires, what the common compliance gaps are, and how to address them.",                                                                                  image: "cctv-pdpa-compliance-feature.webp" },
  { slug: "cctv-retail-analytics",          title: "Can Your CCTV System Help You Sell More?",                                    category: "CCTV",               date: "2026-05-26", tags: ["cctv","retail-analytics","video-analytics","singapore"],             excerpt: "Modern video analytics can provide footfall counts, heatmaps, occupancy data and customer flow insights that help retailers improve layouts, staffing and marketing decisions across multiple outlets.",                                                                                   image: "cctv-retail-analytics-feature.webp" },
  { slug: "cctv-ai-upgrade",                title: "Do I Need to Replace My Cameras to Get AI?",                                  category: "CCTV",               date: "2026-05-29", tags: ["cctv","ai-analytics","video-analytics","singapore"],                 excerpt: "Can AI analytics be added to an existing CCTV system? Learn when AI can be added through cameras, recorders or servers, what features can be retrofitted, and when camera replacement is unavoidable.",                                                                                  image: "cctv-ai-upgrade-feature.webp" },
  { slug: "cctv-cable-upgrade",             title: "Do I Need to Replace All My CCTV Cables to Upgrade My System?",              category: "CCTV",               date: "2026-06-01", tags: ["cctv","cctv-upgrade","security-planning","singapore"],               excerpt: "Do you need to replace all your CCTV cables to upgrade from analogue to IP? In many cases, no. Learn how HD-over-coax, hybrid recorders and phased upgrades can modernise your system without costly rewiring.",                                                                         image: "cctv-cable-upgrade-feature.webp" },
  { slug: "architect-security-guide",       title: "The Architect's Guide to Getting Security Systems Right",                     category: "Security Planning",  date: "2026-06-04", tags: ["for-professionals","construction","security-planning","singapore"],  excerpt: "A practical guide for architects, interior designers and consultants involved in Singapore building projects. Learn how to coordinate CCTV, access control, intercom and vehicle management systems while avoiding common design and construction mistakes.",                              image: "architect-security-guide-feature.webp" },
  { slug: "condo-security-upgrade-proposals",title: "Why Some Condo Security Upgrade Proposals Get Approved — And Others Fail",  category: "Security Planning",  date: "2026-06-10", tags: ["mcst","condominium-security","for-professionals","singapore"],       excerpt: "Why do some condominium security upgrade proposals get approved while others fail? Learn how successful MCST proposals explain the problem, answer the repair-versus-replace question and build resident confidence.",                                                                      image: "condo-security-upgrade-proposals-feature.webp" },
  { slug: "mcst-security-tender",           title: "We Got AGM Approval. Now How Do We Get Meaningful Security Quotes?",         category: "Security Planning",  date: "2026-06-13", tags: ["mcst","procurement","for-professionals","singapore"],                excerpt: "How do you obtain meaningful quotations after an AGM approves a condominium security upgrade? Learn why specifications matter, how to compare contractor submissions fairly, and the tender mistakes that lead to confusion and cost overruns.",                                            image: "mcst-security-tender-feature.webp" }
"""

new_slugs = []
for line in new_41.strip().split('\\n'):
    m = re.search(r'slug:\s*"([^"]+)"', line)
    if m:
        new_slugs.append(m.group(1))

print("Total new slugs:", len(new_slugs))

with open(r'c:\Projects\SV-Build\site-config.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CEO -> Director
content = content.replace("authorTitle: 'Founder & CEO, Securevision Pte Ltd',", "authorTitle: 'Founder & Director, Securevision Pte Ltd',")

# Fix missing array open if needed
content = content.replace('// article page. Add one entry per published article.  { slug: "analogue-to-ip-migration"', '// article page. Add one entry per published article.\\n\\nSECUREVISION.insights = [\\n  { slug: "analogue-to-ip-migration"')

# Now we need to parse the file into three parts:
# 1. Before SECUREVISION.insights = [
# 2. Inside the array
# 3. After the array (];)

start_marker = "SECUREVISION.insights = ["
end_marker = "];"
start_idx = content.find(start_marker)
if start_idx == -1:
    print("Could not find start marker")
    exit(1)

end_idx = content.find(end_marker, start_idx)
if end_idx == -1:
    print("Could not find end marker")
    exit(1)

before_array = content[:start_idx + len(start_marker)]
array_content = content[start_idx + len(start_marker):end_idx]
after_array = content[end_idx:]

# Process array_content to find valid existing entries
existing_entries = []
# split by newline
lines = array_content.split('\\n')
for line in lines:
    if '{ slug:' in line or '{slug:' in line:
        m = re.search(r'slug:\s*"([^"]+)"', line)
        if m:
            slug = m.group(1)
            # Drop if orphan
            if slug in orphans:
                continue
            # Drop if in new_41 (it will be added at the end)
            if slug in new_slugs:
                continue
            # Otherwise, keep it
            existing_entries.append(line.rstrip(','))

print("Valid existing entries kept:", len(existing_entries))

# Format the existing entries nicely
existing_lines = []
for entry in existing_entries:
    existing_lines.append(entry.strip())

# The new entries are already a string
new_lines = [line for line in new_41.strip().split('\\n') if line.strip()]

# Combine them:
# Each existing entry needs a comma
all_combined = []
for entry in existing_lines:
    all_combined.append("  " + entry + ",")

# For new lines, all except the last one need a comma
# Actually, the new_41 string already has commas at the end of each line EXCEPT the last one!
for line in new_lines:
    all_combined.append(line)

final_array_content = "\\n" + "\\n".join(all_combined) + "\\n"

# Reconstruct file
new_content = before_array + final_array_content + after_array

with open(r'c:\Projects\SV-Build\site-config.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done writing. Final count should be", len(existing_entries) + len(new_slugs))
