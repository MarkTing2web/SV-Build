const SECUREVISION = {
  // ── CORE IDENTITY ──────────────────────────────────────────────────
  foundedYear: 2006,
  experienceStartYear: 1989,
  licenceNumber: 'L/PS/001568/2026P',
  licenceExpiry: '2026',           // ← update annually when licence renews
  bizSafe: 'Level 3',
  totalSites: 2000,                // ← update when milestone changes

  // ── CONTACT ────────────────────────────────────────────────────────
  whatsapp: '6593860466',
  whatsappLink: 'https://wa.me/6593860466',
  phone: '+65 6286 4796',
  email: 'enquiry@securevision.com.sg',
  address: 'Blk 1013 Geylang East Avenue 3 #02-142 Singapore 389728',

  // ── SITE METADATA ──────────────────────────────────────────────────
  siteTitle: 'Securevision | Smart Security & Integrated Systems',
  tagline: 'Your partner in building smart, secure, and connected communities — powered by intelligent security systems since 2006.',

  // ── AUTHOR ─────────────────────────────────────────────────────────
  authorName: 'Ler Wee Meng',
  authorTitle: 'Founder & Director, Securevision Pte Ltd',
  authorQuals: 'BEng (NUS) · LLB (UoL)',
  get authorDescription() {
    return `Ler Wee Meng has over ${this.yearsExperience} years of experience in security systems engineering and integration. He holds a Bachelor of Engineering from the National University of Singapore and a Bachelor of Laws from the University of London.`;
  },
  get authorStory() {
    return `He founded Securevision in ${this.foundedYear} and has since led security system deployments across more than ${this.siteDisplay} in Singapore — spanning residential properties, condominiums, commercial buildings, industrial facilities, and institutions.`;
  },
  authorExpertise: 'His technical focus spans CCTV and AI video analytics, IP intercom systems, access control, licence plate recognition, and integrated platform design. He is the architect behind VESTA™, Securevision\'s unified security management platform built specifically for condominium and estate management in Singapore.',
  authorClientFocus: 'Wee Meng works directly with managing agents, MCSTs, property developers, architects, and security companies to design systems that are engineered for the site — not sold off a catalogue.',

  // ── CALCULATED VALUES ───────────────────────────────────────────────
  get yearsInBusiness() {
    return new Date().getFullYear() - this.foundedYear;
  },
  get yearsExperience() {
    return new Date().getFullYear() - this.experienceStartYear;
  },
  get siteDisplay() {
    return this.totalSites.toLocaleString() + '+';
  },
  get licenceDisplay() {
    return this.licenceNumber;
  },

  // ── STRATEGIC LINKS ─────────────────────────────────────────────────
  assessmentLink: 'request-site-assessment-singapore.html',
  generalContactLink: 'contact.html'
};

// ── DOM INJECTION ──────────────────────────────────────────────────────
// Runs on DOMContentLoaded. Populates all data-sv-* attributes and
// named span classes across every page that loads this script.
// To use in HTML: add the attribute or class shown below.

document.addEventListener('DOMContentLoaded', () => {

  // Years in business since 2006 — class: .sv-years-business
  document.querySelectorAll('.sv-years-business').forEach(el => {
    el.textContent = SECUREVISION.yearsInBusiness;
  });

  // Years of experience since 1989 — class: .sv-years-experience
  document.querySelectorAll('.sv-years-experience').forEach(el => {
    el.textContent = SECUREVISION.yearsExperience;
  });

  // Sites protected — class: .sv-sites
  // Renders as "2,000+" (formatted with comma)
  document.querySelectorAll('.sv-sites').forEach(el => {
    el.textContent = SECUREVISION.siteDisplay;
  });

  // Licence number — class: .sv-licence
  document.querySelectorAll('.sv-licence').forEach(el => {
    el.textContent = SECUREVISION.licenceNumber;
  });

  // Founded year — class: .sv-founded
  document.querySelectorAll('.sv-founded').forEach(el => {
    el.textContent = SECUREVISION.foundedYear;
  });

  // Current year (for copyright) — class: .sv-current-year
  document.querySelectorAll('.sv-current-year').forEach(el => {
    el.textContent = new Date().getFullYear();
  });

  // Author name — class: .sv-author-name
  document.querySelectorAll('.sv-author-name').forEach(el => {
    el.textContent = SECUREVISION.authorName;
  });

  // Author title — class: .sv-author-title
  document.querySelectorAll('.sv-author-title').forEach(el => {
    el.textContent = SECUREVISION.authorTitle;
  });

  // Author credentials — class: .sv-author-quals
  document.querySelectorAll('.sv-author-quals').forEach(el => {
    el.textContent = SECUREVISION.authorQuals;
  });

  // WhatsApp link — updates href on all .sv-wa-link anchors
  document.querySelectorAll('.sv-wa-link').forEach(el => {
    if (el.tagName === 'A') el.href = SECUREVISION.whatsappLink;
  });

  // bizSAFE level — class: .sv-bizsafe
  document.querySelectorAll('.sv-bizsafe').forEach(el => {
    el.textContent = 'bizSAFE ' + SECUREVISION.bizSafe;
  });

  // Tagline — class: .sv-tagline
  document.querySelectorAll('.sv-tagline').forEach(el => {
    el.textContent = SECUREVISION.tagline;
  });

});

// ── INSIGHTS ARTICLE REGISTRY ──────────────────────────────────────────
// Drives the automatic Related Security Insights section on every
// article page. Add one entry per published article.
// slug must match the HTML filename exactly (without .html).
// To add a new article: add one object here. Nothing else needed.

SECUREVISION.insights = [
  { slug: "burglar-alarm-design",                                    title: "How to Design a Burglar Alarm System",                              category: "Alarm & Intrusion",   tags: ["burglar-alarm","design","zones","planning"], excerpt: "Most alarm systems are zoned wrong from day one. Here is how professional security engineers think about scope, zones, and response priorities before a single detector goes up.", image: "burglar-alarm-design-feature.webp" },
  { slug: "burglar-alarm-detectors-sensors", title: "The Right Detector for the Right Job", category: "Alarm & Intrusion", tags: ["burglar-alarm","detectors","pir","sensors"], excerpt: "Your alarm system is only as good as the detectors in it. A plain-English guide to the main sensor types, where each one works, and how to choose the right one for each zone.", image: "burglar-alarm-detectors-sensors-feature.webp" },
  { slug: "choose-intercom-for-home",                                title: "How to Choose an Intercom for Your Home",                          category: "Access & Intercom",   tags: ["intercom","residential","homeowner","video-intercom"] },
  { slug: "compare-security-integrators",                            title: "How to Compare Two Security Integrators Fairly",           category: "Security Planning", tags: ["integrator","tender","selection","singapore","contractor","comparison"] },
  { slug: "condo-security-upgrade-timeline",                         title: "Realistic Timeline and Disruption Plan for Condo Security Upgrade",category: "Security Planning",   tags: ["condo","mcst","upgrade","timeline","residents"] },
  { slug: "hdb-landed-condo-security-differences",                   title: "HDB, Landed, or Condo — How Security Requirements Differ",         category: "Security Planning",   tags: ["residential","hdb","landed","condo","singapore"] },
  { slug: "home-security-system-cost-singapore",                     title: "How Much Does a Home Security System Cost in Singapore?",          category: "Security Planning",   tags: ["cost","residential","singapore","homeowner","budget"] },
  { slug: "how-card-access-works",                                   title: "How Card Access Control Actually Works",                           category: "Access & Intercom",          tags: ["access-control","how-it-works","card","controller"] },
  { slug: "how-intercom-systems-work",                               title: "How Intercom Systems Work",                                        category: "Access & Intercom",          tags: ["intercom","how-it-works","ip","analogue","sip"] },
  { slug: "how-technology-makes-your-guarding-team-more-competitive",title: "How Technology Makes Your Guarding Team More Competitive",  category: "Platform & Integration",        tags: ["guarding","operations","technology","singapore","ai","analytics"] },
  { slug: "how-to-choose-cctv",                                      title: "How to Choose the Right CCTV System for Your Home or Office",      category: "CCTV & Surveillance",   tags: ["cctv","selection","homeowner","commercial","singapore"] },
  { slug: "is-my-security-system-still-working",                     title: "Is Your Security System Actually Still Working?",                  category: "Security Planning",         tags: ["maintenance","health-check","cctv","burglar-alarm"] },
  { slug: "maintain-burglar-alarm",                                  title: "How to Maintain Your Burglar Alarm System",                        category: "Alarm & Intrusion",         tags: ["burglar-alarm","maintenance","battery","walk-test"] },
  { slug: "maintenance-contract",                                    title: "Do You Need a Security System Maintenance Contract?",              category: "Security Planning",         tags: ["maintenance","contract","sla","service"] },
  { slug: "managing-agents-guide-estate-security-systems",           title: "The Managing Agent's Guide to Estate Security Systems",            category: "Security Planning",   tags: ["managing-agent","estate","mcst","systems"] },
  { slug: "managing-multiple-estates-with-vesta",                    title: "Managing Multiple Estates with VESTA",                     category: "Platform & Integration",        tags: ["vesta","estate","managing-agent","platform","mcst","cctv","access-control"] },
  { slug: "mcst-legal-obligations-security",                         title: "What Are the MCST's Legal Obligations for Security Systems?",      category: "Security Planning",   tags: ["mcst","legal","bmsma","pdpa","obligations"] },
  { slug: "rackmount-nvr",                                           title: "Rack-Mount NVR vs Desktop NVR — Which Do You Need?",              category: "CCTV & Surveillance",          tags: ["nvr","cctv","rack","infrastructure"] },
  { slug: "reduce-false-alarms",                                     title: "How to Reduce False Alarms from Your Burglar Alarm",              category: "Alarm & Intrusion",         tags: ["burglar-alarm","false-alarm","pir","maintenance"] },
  { slug: "security-upgrade-condo-agm",                              title: "How to Get a Security Upgrade Approved at a Condo AGM",           category: "Security Planning",   tags: ["condo","agm","mcst","upgrade","residents"] },
  { slug: "standalone-door-access",                                  title: "How to Choose a Standalone Door Access System",                   category: "Access & Intercom",   tags: ["access-control","standalone","door","office"] },
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
];

// ── GUIDES REGISTRY ────────────────────────────────────────────────────
// Drives the automatic Related Guides section on every guide page.
// slug must match the HTML filename exactly (without .html).
// To add a new guide: add one object here. Nothing else needed.

SECUREVISION.guides = [
  { slug: "cctv-guide",                          title: "The Complete CCTV Guide",                             category: "Surveillance",   tags: ["cctv","cameras","nvr","surveillance"] },
  { slug: "burglar-alarm-guide",                 title: "The Complete Burglar Alarm Guide",                    category: "Intrusion",      tags: ["burglar-alarm","intrusion","detector","zones"] },
  { slug: "door-access-guide",                   title: "The Complete Door Access Control Guide",              category: "Access Control", tags: ["access-control","door","card","reader"] },
  { slug: "auto-gate-guide",                     title: "The Complete Auto Gate Guide",                        category: "Vehicle & Gate", tags: ["auto-gate","motor","gate","residential"] },
  { slug: "intercom-guide",                      title: "The Complete Intercom Guide",                         category: "Communications", tags: ["intercom","video-intercom","ip","visitor"] },
  { slug: "office-telephone-guide",              title: "The Complete Office Telephone Guide",                 category: "Communications", tags: ["ip-phone","voip","pbx","office","telephony"] },
  { slug: "wifi-network-guide",                  title: "The Complete WiFi & Network Guide",                   category: "Network",        tags: ["wifi","networking","router","infrastructure"] },
  { slug: "security-renovation-guide",           title: "Security Planning for Renovations",                  category: "Planning",       tags: ["renovation","planning","multi-system","new-build"] },
  { slug: "how-to-evaluate-security-contractor", title: "How to Evaluate a Security Contractor",              category: "Planning",       tags: ["contractor","selection","tender","integrator"] }
];
