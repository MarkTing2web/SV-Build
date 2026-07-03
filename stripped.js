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
  authorTitle: 'Founder & CEO, Securevision Pte Ltd',
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



  // Years of experience since 1989 — class: .sv-years-experience
  null('.sv-years-experience').forEach(el => {
    el.textContent = SECUREVISION.yearsExperience;
  });

  // Sites protected — class: .sv-sites
  // Renders as "2,000+" (formatted with comma)
  null('.sv-sites').forEach(el => {
    el.textContent = SECUREVISION.siteDisplay;
  });

  // Licence number — class: .sv-licence
  null('.sv-licence').forEach(el => {
    el.textContent = SECUREVISION.licenceNumber;
  });

  // Founded year — class: .sv-founded
  null('.sv-founded').forEach(el => {
    el.textContent = SECUREVISION.foundedYear;
  });

  // Current year (for copyright) — class: .sv-current-year
  null('.sv-current-year').forEach(el => {
    el.textContent = new Date().getFullYear();
  });

  // Author name — class: .sv-author-name
  null('.sv-author-name').forEach(el => {
    el.textContent = SECUREVISION.authorName;
  });

  // Author title — class: .sv-author-title
  null('.sv-author-title').forEach(el => {
    el.textContent = SECUREVISION.authorTitle;
  });

  // Author credentials — class: .sv-author-quals
  null('.sv-author-quals').forEach(el => {
    el.textContent = SECUREVISION.authorQuals;
  });

  // WhatsApp link — updates href on all .sv-wa-link anchors
  null('.sv-wa-link').forEach(el => {
    if (el.tagName === 'A') el.href = SECUREVISION.whatsappLink;
  });

  // bizSAFE level — class: .sv-bizsafe
  null('.sv-bizsafe').forEach(el => {
    el.textContent = 'bizSAFE ' + SECUREVISION.bizSafe;
  });

  // Tagline — class: .sv-tagline
  null('.sv-tagline').forEach(el => {
    el.textContent = SECUREVISION.tagline;
  });

});

// ── INSIGHTS ARTICLE REGISTRY ──────────────────────────────────────────
// Drives the automatic Related Security Insights section on every
// article page. Add one entry per published article.
// slug must match the HTML filename exactly (without .html).
// To add a new article: add one object here. Nothing else needed.

SECUREVISION.insights = [
  { slug: "access-control-multi-door", title: "How to Choose a Multi-Door Access Control System", category: "Access & Intercom", tags: ["access-control", "multi-door", "commercial", "selection", "singapore"], image: "access-control-multi-door-feature.webp" },
  { slug: "access-control-upgrade-drivers-singapore", title: "Three Reasons Singapore Organisations Should Review Their Access Control System Now", category: "Access & Intercom", tags: ["access-control", "upgrade", "singapore", "commercial"], image: "access-control-upgrade-drivers-singapore-feature.webp" },
  { slug: "alarm-communication-paths", title: "Why Banks Use Multiple Communication Paths", category: "Alarm & Intrusion", tags: ["alarm", "monitoring", "communication", "gsm", "ip"], image: "alarm-communication-paths-feature.webp" },
  { slug: "alarm-internet-cut", title: "What Happens If a Burglar Cuts the Internet?", category: "Alarm & Intrusion", tags: ["alarm", "internet", "monitoring", "security", "backup"], image: "alarm-internet-cut-feature.webp" },
  { slug: "alarm-monitoring-history", title: "How Alarm Monitoring Worked Before the Internet", category: "Alarm & Intrusion", tags: ["alarm", "monitoring", "history", "pstn", "cms"], image: "alarm-monitoring-history-feature.webp" },
  { slug: "alarm-panel", title: "The Brain Behind Your Burglar Alarm System", category: "Alarm & Intrusion", tags: ["alarm", "panel", "controller", "zones", "singapore"], image: "alarm-panel-feature.webp" },
  { slug: "alarm-panel-polling", title: "Why Alarm Panels Used to Call Home Every Seven Days", category: "Alarm & Intrusion", tags: ["alarm", "polling", "panel", "monitoring", "pstn"], image: "alarm-panel-polling-feature.webp" },
  { slug: "alarm-power-cut", title: "What Happens If a Burglar Cuts the Power?", category: "Alarm & Intrusion", tags: ["alarm", "power", "battery", "backup", "security"], image: "alarm-power-cut-feature.webp" },
  { slug: "alarm-response", title: "What Really Happens When Your Alarm Goes Off?", category: "Alarm & Intrusion", tags: ["alarm", "response", "monitoring", "police", "singapore"], image: "alarm-response-feature.webp" },
  { slug: "alarm-siren", title: "Why Burglar Alarm Sirens Don't Ring Forever", category: "Alarm & Intrusion", tags: ["alarm", "siren", "timer", "deterrent", "singapore"], image: "alarm-siren-feature.webp" },
  { slug: "alarm-system-lifespan", title: "How Long Should a Burglar Alarm System Last?", category: "Alarm & Intrusion", tags: ["alarm", "lifespan", "upgrade", "maintenance", "singapore"], image: "alarm-system-lifespan-feature.webp" },
  { slug: "alarm-upgrade-or-replace", title: "Should I Upgrade or Replace My Alarm System?", category: "Alarm & Intrusion", tags: ["alarm", "upgrade", "replace", "decision", "singapore"], image: "alarm-upgrade-or-replace-feature.webp" },
  { slug: "alarm-usage-habits", title: "Most Alarm Systems Are Installed Correctly But Used Incorrectly", category: "Alarm & Intrusion", tags: ["alarm", "usage", "habits", "homeowner", "singapore"], image: "alarm-usage-habits-feature.webp" },
  { slug: "alarm-wiring-reuse", title: "Can I Reuse My Existing Alarm Wiring?", category: "Alarm & Intrusion", tags: ["alarm", "wiring", "reuse", "upgrade", "renovation"], image: "alarm-wiring-reuse-feature.webp" },
  { slug: "architect-security-guide", title: "The Architect's Guide to Getting Security Systems Right", category: "Security Planning", tags: ["architect", "design", "specification", "security", "singapore"], image: "architect-security-guide-feature.webp" },
  { slug: "auto-gate-motor", title: "How to Choose the Right Auto Gate Motor", category: "Vehicle & Gates", tags: ["auto-gate", "motor", "residential", "selection", "singapore"], image: "auto-gate-motor-feature.webp" },
  { slug: "break-in-nearby-security-review", title: "A Break-In Nearby Prompted This Security Review", category: "Security Planning", tags: ["break-in", "review", "residential", "singapore", "security"], image: "break-in-nearby-security-review-feature.webp" },
  { slug: "burglar-alarm-detectors-sensors", title: "Know Your Burglar Alarm Detectors and Sensors", category: "Alarm & Intrusion", tags: ["burglar-alarm", "detectors", "pir", "sensors"], image: "burglar-alarm-detectors-sensors-feature.webp" },
  { slug: "cctv-ai-upgrade", title: "Do I Need to Replace My Cameras to Get AI?", category: "CCTV & Surveillance", tags: ["cctv", "ai", "upgrade", "analytics", "hikvision"], image: "cctv-ai-upgrade-feature.webp" },
  { slug: "cctv-cable-upgrade", title: "Do I Need to Replace All My CCTV Cables to Upgrade My System?", category: "CCTV & Surveillance", tags: ["cctv", "cables", "upgrade", "ip", "coax"], image: "cctv-cable-upgrade-feature.webp" },
  { slug: "cctv-pdpa-compliance", title: "Is My CCTV System PDPA Compliant?", category: "CCTV & Surveillance", tags: ["cctv", "pdpa", "compliance", "singapore", "privacy"], image: "cctv-pdpa-compliance-feature.webp" },
  { slug: "cctv-retail-analytics", title: "Can Your CCTV System Help You Sell More?", category: "CCTV & Surveillance", tags: ["cctv", "retail", "analytics", "commercial", "singapore"], image: "cctv-retail-analytics-feature.webp" },
  { slug: "cctv-system-components", title: "Most People Think CCTV Is Just Cameras. It Isn't.", category: "CCTV & Surveillance", tags: ["cctv", "nvr", "components", "ip", "singapore"], image: "cctv-system-components-feature.webp" },
  { slug: "cctv-vs-alarm", title: "Do I Still Need a Burglar Alarm If I Have CCTV?", category: "CCTV & Surveillance", tags: ["cctv", "alarm", "comparison", "residential", "singapore"], image: "cctv-vs-alarm-feature.webp" },
  { slug: "choose-intercom-for-home", title: "How to Choose an Intercom for Your Home", category: "Access & Intercom", tags: ["intercom", "residential", "homeowner", "video-intercom"], image: "choose-intercom-for-home-feature.webp" },
  { slug: "compare-security-integrators", title: "How to Compare Two Security Integrators Fairly", category: "Security Planning", tags: ["integrator", "tender", "mcst", "selection"], image: "compare-security-integrators-feature.webp" },
  { slug: "condo-intercom-upgrade", title: "Condominium Intercom Upgrade Singapore — When Should Your Estate Start Planning?", category: "Access & Intercom", tags: ["intercom", "condo", "upgrade", "mcst", "singapore"], image: "condo-intercom-upgrade-feature.webp" },
  { slug: "condo-security-upgrade-proposals", title: "Why Some Condo Security Upgrade Proposals Get Approved — And Others Fail", category: "Security Planning", tags: ["condo", "mcst", "agm", "proposal", "upgrade"], image: "condo-security-upgrade-proposals-feature.webp" },
  { slug: "condo-security-upgrade-timeline", title: "Realistic Timeline and Disruption Plan for Condo Security Upgrade", category: "Security Planning", tags: ["condo", "mcst", "upgrade", "timeline", "residents"], image: "condo-security-upgrade-timeline-feature.webp" },
  { slug: "false-alarm-causes", title: "The Most Common Causes of False Alarms", category: "Alarm & Intrusion", tags: ["alarm", "false-alarm", "causes", "pir", "singapore"], image: "false-alarm-causes-feature.webp" },
  { slug: "false-alarms", title: "Why False Alarms Matter", category: "Alarm & Intrusion", tags: ["alarm", "false-alarm", "monitoring", "police", "singapore"], image: "false-alarms-feature.webp" },
  { slug: "gate-remote-smartphone", title: "Do You Still Need a Gate Remote?", category: "Vehicle & Gates", tags: ["auto-gate", "remote", "smartphone", "app", "singapore"], image: "gate-remote-smartphone-feature.webp" },
  { slug: "guarding-technology-singapore", title: "How Technology Makes Your Guarding Team More Competitive", category: "Security Planning", tags: ["guarding", "technology", "manpower", "singapore", "operations"], image: "guarding-technology-singapore-feature.webp" },
  { slug: "hdb-landed-condo-security-differences", title: "HDB, Landed, or Condo — How Security Requirements Differ", category: "Security Planning", tags: ["residential", "hdb", "landed", "condo", "singapore"], image: "hdb-landed-condo-security-differences-feature.webp" },
  { slug: "home-security-system-cost-singapore", title: "How Much Does a Home Security System Cost in Singapore?", category: "Security Planning", tags: ["cost", "residential", "singapore", "homeowner", "budget"], image: "home-security-system-cost-singapore-feature.webp" },
  { slug: "how-alarm-works", title: "How Does a Burglar Alarm System Work?", category: "Alarm & Intrusion", tags: ["alarm", "how-it-works", "zones", "controller", "singapore"], image: "how-alarm-works-feature.webp" },
  { slug: "how-card-access-works", title: "How Card Access Control Actually Works", category: "Access & Intercom", tags: ["access-control", "how-it-works", "card", "controller"], image: "how-card-access-works-feature.webp" },
  { slug: "how-to-choose-cctv", title: "How to Choose the Right CCTV System for Your Home or Office", category: "CCTV & Surveillance", tags: ["cctv", "selection", "homeowner", "commercial", "singapore"], image: "how-to-choose-cctv-feature.webp" },
  { slug: "installer-leaves", title: "The Real Test Begins After the Installer Leaves", category: "Security Planning", tags: ["installation", "after-sales", "support", "singapore", "maintenance"], image: "installer-leaves-feature.webp" },
  { slug: "intercom-system-evolution-singapore", title: "IP Intercom vs Traditional Intercom — What Changed and Why It Matters for Your Property", category: "Access & Intercom", tags: ["intercom", "ip", "traditional", "upgrade", "singapore"], image: "intercom-system-evolution-singapore-feature.webp" },
  { slug: "is-my-security-system-still-working", title: "Is Your Security System Actually Still Working?", category: "Security Planning", tags: ["maintenance", "health-check", "cctv", "burglar-alarm"], image: "is-my-security-system-still-working-feature.webp" },
  { slug: "lpr-vs-rfid-condo", title: "LPR vs RFID — Which Vehicle Access System Is Better For Your Condo?", category: "Vehicle & Gates", tags: ["lpr", "rfid", "condo", "vehicle", "singapore"], image: "lpr-vs-rfid-condo-feature.webp" },
  { slug: "maintain-burglar-alarm", title: "How to Maintain Your Burglar Alarm System", category: "Alarm & Intrusion", tags: ["burglar-alarm", "maintenance", "battery", "walk-test"], image: "maintain-burglar-alarm-feature.webp" },
  { slug: "maintenance-contract", title: "Do You Need a Security System Maintenance Contract?", category: "Security Planning", tags: ["maintenance", "contract", "sla", "service"], image: "maintenance-contract-feature.webp" },
  { slug: "managing-agents-guide-estate-security-systems", title: "The Managing Agent's Guide to Estate Security Systems", category: "Security Planning", tags: ["managing-agent", "estate", "mcst", "systems"], image: "managing-agents-guide-estate-security-systems-feature.webp" },
  { slug: "managing-multiple-estates-with-vesta", title: "Managing Multiple Estates with VESTA", category: "Security Planning", tags: ["vesta", "estate", "managing-agent", "platform"], image: "managing-multiple-estates-with-vesta-feature.webp" },
  { slug: "mcst-legal-obligations-security", title: "What Are the MCST's Legal Obligations for Security Systems?", category: "Security Planning", tags: ["mcst", "legal", "bmsma", "pdpa", "obligations"], image: "mcst-legal-obligations-security-feature.webp" },
  { slug: "mcst-security-tender", title: "We Got AGM Approval. Now How Do We Get Meaningful Security Quotes?", category: "Security Planning", tags: ["mcst", "agm", "tender", "quotes", "singapore"], image: "mcst-security-tender-feature.webp" },
  { slug: "mechanical-locks-not-enough", title: "Why Mechanical Locks Are No Longer Enough", category: "Access & Intercom", tags: ["locks", "access-control", "digital", "residential", "singapore"], image: "mechanical-locks-not-enough-feature.webp" },
  { slug: "modern-detectors", title: "Why Modern Motion Detectors Are Better Than Ever", category: "Alarm & Intrusion", tags: ["alarm", "detectors", "pir", "motion", "singapore"], image: "modern-detectors-feature.webp" },
  { slug: "monitoring-station", title: "Inside a Central Monitoring Station", category: "Alarm & Intrusion", tags: ["alarm", "monitoring", "cms", "response", "singapore"], image: "monitoring-station-feature.webp" },
  { slug: "network-security-systems", title: "The Cameras Were Fine. The Network Was the Problem.", category: "IP Telephony & Network", tags: ["network", "cctv", "infrastructure", "ip", "singapore"], image: "network-security-systems-feature.webp" },
  { slug: "pstn-to-ip", title: "From PSTN to IP Monitoring", category: "Alarm & Intrusion", tags: ["alarm", "pstn", "ip", "monitoring", "upgrade"], image: "pstn-to-ip-feature.webp" },
  { slug: "rackmount-nvr", title: "Rack-Mount NVR vs Desktop NVR — Which Do You Need?", category: "CCTV & Surveillance", tags: ["nvr", "cctv", "rack", "infrastructure"], image: "rackmount-nvr-feature.webp" },
  { slug: "reduce-false-alarms", title: "How to Reduce False Alarms from Your Burglar Alarm", category: "Alarm & Intrusion", tags: ["burglar-alarm", "false-alarm", "pir", "maintenance"], image: "reduce-false-alarms-feature.webp" },
  { slug: "security-assessment-10-things", title: "10 Things I Look For When Assessing a Property's Security", category: "Security Planning", tags: ["assessment", "security", "singapore", "checklist", "planning"], image: "security-assessment-10-things-feature.webp" },
  { slug: "security-upgrade-condo-agm", title: "How to Get a Security Upgrade Approved at a Condo AGM", category: "Security Planning", tags: ["condo", "agm", "mcst", "upgrade", "residents"], image: "security-upgrade-condo-agm-feature.webp" },
  { slug: "self-monitoring-vs-cms", title: "Should You Monitor Your Alarm Yourself or Use a Monitoring Centre?", category: "Alarm & Intrusion", tags: ["alarm", "monitoring", "self-monitoring", "cms", "singapore"], image: "self-monitoring-vs-cms-feature.webp" },
  { slug: "singapore-licensing", title: "Why Security System Installers Must Be Licensed in Singapore", category: "Security Planning", tags: ["licensing", "plrd", "singapore", "contractor", "regulation"], image: "singapore-licensing-feature.webp" },
  { slug: "standalone-door-access", title: "How to Choose a Standalone Door Access System", category: "Access & Intercom", tags: ["access-control", "standalone", "door", "office"], image: "standalone-door-access-feature.webp" },
  { slug: "system-repair-or-replace", title: "My System Is 10 Years Old. Should I Repair It or Replace It?", category: "Security Planning", tags: ["repair", "replace", "upgrade", "lifecycle", "singapore"], image: "system-repair-or-replace-feature.webp" },
  { slug: "video-verification", title: "Video Verification — The Technology That Changed Alarm Monitoring", category: "Alarm & Intrusion", tags: ["alarm", "video", "verification", "monitoring", "singapore"], image: "video-verification-feature.webp" },
];

SECUREVISION.portfolio = [
  { url: "/portfolio/commercial/altitudex-sentosa-commercial", title: "AltitudeX Sentosa", section: "Portfolio · Commercial", excerpt: "Migrating a decade-old EntryPass system to ZKTeco CV Security — 50 doors, mixed credentials, zero operational disruption.", tags: ["access-control", "zkteco", "commercial", "entrypass", "sentosa"] },
  { url: "/portfolio/commercial/catholic-centre-security-partnership", title: "Catholic Centre", section: "Portfolio · Commercial", excerpt: "A decade-long security partnership — complete fit-out for a 9-storey institutional hub, followed by CCTV and access upgrades.", tags: ["cctv", "access-control", "commercial", "waterloo"] },
  { url: "/portfolio/commercial/em-services-call-centre-redhill", title: "EM Services Call Centre", section: "Portfolio · Commercial", excerpt: "Biometric access and high-definition surveillance protecting high-density call centre operations at One@Redhill Centre.", tags: ["biometric", "access-control", "cctv", "commercial", "redhill"] },
  { url: "/portfolio/commercial/hilton-singapore-orchard-fire-door", title: "Hilton Singapore Orchard", section: "Portfolio · Commercial", excerpt: "EM lock access control and fire alarm integration for 50+ emergency stairwell doors across Asia-Pacific's largest Hilton property.", tags: ["access-control", "fire-door", "hotel", "commercial", "orchard"] },
  { url: "/portfolio/commercial/scape-commercial", title: "SCAPE Singapore", section: "Portfolio · Commercial", excerpt: "209 AI cameras, 37 biometric access points, and a Salesforce integration that automated credential management end-to-end.", tags: ["cctv", "ai", "biometric", "access-control", "commercial", "youth"] },
  { url: "/portfolio/commercial/scape-smart-booking-access", title: "SCAPE Smart Booking & Access", section: "Portfolio · Commercial", excerpt: "Connecting an online booking platform to physical room access — a confirmed reservation automatically becomes a valid entry credential.", tags: ["access-control", "integration", "booking", "commercial", "scape"] },
  { url: "/portfolio/commercial/st-engineering-mobility-cctv", title: "ST Engineering Mobility", section: "Portfolio · Commercial", excerpt: "28 cameras and a 32-channel NVR for a vehicle services facility with a wireless bridge solving a cross-building cabling problem.", tags: ["cctv", "nvr", "wireless", "commercial", "st-engineering"] },
  { url: "/portfolio/condominiums/clearwater-access-salto-partnership", title: "The Clearwater — Access Partnership", section: "Portfolio · Condominiums", excerpt: "Eight years of security partnership — from a Salto Virtual Network installation in 2017 to a cloud-based Akuvox access upgrade.", tags: ["access-control", "salto", "akuvox", "condominium", "long-term"] },
  { url: "/portfolio/condominiums/clearwater-cctv-upgrade", title: "The Clearwater — CCTV Upgrade", section: "Portfolio · Condominiums", excerpt: "Full IP CCTV upgrade completing a long-term security modernisation programme at The Clearwater condominium.", tags: ["cctv", "upgrade", "condominium", "ip", "clearwater"] },
  { url: "/portfolio/condominiums/country-grandeur-upper-thomson-condo", title: "Country Grandeur", section: "Portfolio · Condominiums", excerpt: "Restoring reliability to a boutique Upper Thomson estate with modernised visitor access and intercom infrastructure.", tags: ["intercom", "access-control", "condominium", "upper-thomson"] },
  { url: "/portfolio/condominiums/d-elias-pasir-ris-condo", title: "D'Elias Singapore", section: "Portfolio · Condominiums", excerpt: "Future-proofing residential security with cloud-ready access management for a mid-rise condominium in Pasir Ris.", tags: ["access-control", "cloud", "condominium", "pasir-ris"] },
  { url: "/portfolio/condominiums/high-oak-condominium-cctv", title: "High Oak Condominium", section: "Portfolio · Condominiums", excerpt: "Full CCTV upgrade with colour night vision — super wide-angle cameras for the basement carpark and lobbies across a 194-unit estate.", tags: ["cctv", "colour", "night-vision", "condominium", "bukit-timah"] },
  { url: "/portfolio/condominiums/hillview-park-cctv-upgrade", title: "Hillview Park", section: "Portfolio · Condominiums", excerpt: "48-camera surveillance upgrade replacing legacy analogue systems with HD colour-at-night IP technology across three towers.", tags: ["cctv", "upgrade", "analogue", "ip", "condominium", "hillview"] },
  { url: "/portfolio/condominiums/idyllic-suites-geylang-condo", title: "Idyllic Suites", section: "Portfolio · Condominiums", excerpt: "Credential overhaul and access modernisation for a 71-unit condominium in Geylang.", tags: ["access-control", "credentials", "condominium", "geylang"] },
  { url: "/portfolio/condominiums/light-cairnhill-condo", title: "Light@Cairnhill", section: "Portfolio · Condominiums", excerpt: "Consolidating fragmented intercom and lift access systems into a single coordinated workflow for a 121-unit Cairnhill estate.", tags: ["intercom", "lift", "access-control", "condominium", "cairnhill"] },
  { url: "/portfolio/condominiums/mergui-mansions-novena-condo", title: "Mergui Mansions", section: "Portfolio · Condominiums", excerpt: "System recovery and security restoration for a boutique Novena condominium after infrastructure failure.", tags: ["recovery", "intercom", "condominium", "novena"] },
  { url: "/portfolio/condominiums/newton21-newton-condo", title: "Newton 21", section: "Portfolio · Condominiums", excerpt: "Dual-infrastructure modernisation — replacing legacy intercom and access protocols while expanding CCTV visibility at a 69-unit Newton estate.", tags: ["intercom", "cctv", "access-control", "condominium", "newton"] },
  { url: "/portfolio/condominiums/rezi-3two-condo", title: "Rezi 3Two", section: "Portfolio · Condominiums", excerpt: "Complete new-build security installation — CCTV, card access, swing gate automation, and audio-video intercom for 65 freehold residents.", tags: ["cctv", "access-control", "intercom", "auto-gate", "condominium", "new-build"] },
  { url: "/portfolio/condominiums/suites-cairnhill-intercom-lpr", title: "Suites@Cairnhill", section: "Portfolio · Condominiums", excerpt: "Akuvox video intercoms, mobile app entry, custom Mifare credentials, and LPR-enabled vehicle management for a boutique District 9 condominium.", tags: ["intercom", "lpr", "akuvox", "access-control", "condominium", "cairnhill"] },
  { url: "/portfolio/condominiums/the-bale-intercom-cctv", title: "The Bale", section: "Portfolio · Condominiums", excerpt: "Replacing telephony intercom and upgrading CCTV for a 36-unit freehold estate in Bedok.", tags: ["intercom", "cctv", "upgrade", "condominium", "bedok"] },
  { url: "/portfolio/condominiums/the-lviv-newton-condo", title: "L'viv Residences", section: "Portfolio · Condominiums", excerpt: "Replacing an obsolete intercom with a modern 2-wire retrofit — restoring reliable visitor communication at a 147-unit Newton estate.", tags: ["intercom", "retrofit", "2-wire", "condominium", "newton"] },
  { url: "/portfolio/condominiums/the-verte-telok-kurau-condo", title: "The Verte", section: "Portfolio · Condominiums", excerpt: "Upgrading from delayed telephony systems to instant visual access and mobile control for a boutique Telok Kurau condominium.", tags: ["intercom", "mobile", "upgrade", "condominium", "telok-kurau"] },
  { url: "/portfolio/condominiums/village-pasir-panjang-condo", title: "The Village @ Pasir Panjang", section: "Portfolio · Condominiums", excerpt: "Scalable security infrastructure — LPR vehicle management, intercom, and estate-wide CCTV for a low-rise luxury residential cluster.", tags: ["lpr", "intercom", "cctv", "condominium", "pasir-panjang"] },
  { url: "/portfolio/data-centres/fort-data-centre-access-upgrade", title: "FORT Data Centre — Access Upgrade", section: "Portfolio · Data Centres", excerpt: "Upgrading access control infrastructure for a mission-critical data centre facility — precision engineering in a zero-tolerance environment.", tags: ["access-control", "data-centre", "upgrade", "biometric"] },
  { url: "/portfolio/data-centres/fort-st-engineering", title: "FORT by ST Engineering", section: "Portfolio · Data Centres", excerpt: "Live-environment access control upgrade across active data hall floors.", tags: ["access-control", "data-centre", "st-engineering", "live-environment"] },
  { url: "/portfolio/healthcare/sunlove-mental-wellness-centre-haig-road", title: "Sunlove Mental Wellness Centre", section: "Portfolio · Healthcare", excerpt: "Sensitive security design for a mental wellness facility on Haig Road — balancing safety requirements with a therapeutic environment.", tags: ["access-control", "cctv", "healthcare", "mental-wellness", "haig-road"] },
  { url: "/portfolio/industrial/cogent-logistics-hub-cctv", title: "Cogent Logistics Hub", section: "Portfolio · Industrial", excerpt: "CCTV surveillance across a major Singapore logistics hub — wide-area coverage for a large-footprint industrial facility.", tags: ["cctv", "logistics", "industrial", "wide-area"] },
  { url: "/portfolio/industrial/hoy-san-industrial", title: "Hoy San Industrial", section: "Portfolio · Industrial", excerpt: "LPR-enabled vehicle barrier system and gate automation for an industrial facility — streamlining vehicle entry without a guardhouse queue.", tags: ["lpr", "barrier", "auto-gate", "industrial", "vehicle"] },
  { url: "/portfolio/industrial/mitsubishi-elevator-face-access-bms", title: "Mitsubishi Elevator Singapore", section: "Portfolio · Industrial", excerpt: "Facial recognition access control integrated with BMS for Mitsubishi Elevator's Singapore facility.", tags: ["face-recognition", "access-control", "bms", "industrial"] },
  { url: "/portfolio/industrial/multibase-construction-security-upgrade", title: "Multibase Construction", section: "Portfolio · Industrial", excerpt: "Full security upgrade for a construction company — access control, surveillance, and perimeter protection.", tags: ["access-control", "cctv", "alarm", "industrial", "construction"] },
  { url: "/portfolio/industrial/smartflex-tampines", title: "Smartflex Tampines", section: "Portfolio · Industrial", excerpt: "Security infrastructure for a Tampines industrial facility — CCTV and access control for a modern light industrial space.", tags: ["cctv", "access-control", "industrial", "tampines"] },
  { url: "/portfolio/industrial/sta-compliance-imaging", title: "STA Compliance Imaging", section: "Portfolio · Industrial", excerpt: "Automated camera system triggered by vehicle entry to eliminate manual undercarriage inspection records.", tags: ["cctv", "vehicle", "automation", "industrial", "sta"] },
  { url: "/portfolio/industrial/sta-inspection-industrial", title: "STA Inspection Centre", section: "Portfolio · Industrial", excerpt: "Access control and surveillance for Singapore's vehicle inspection infrastructure at Sin Ming.", tags: ["access-control", "cctv", "industrial", "vehicle-inspection", "sin-ming"] },
  { url: "/portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm", title: "STMicroelectronics Loyang", section: "Portfolio · Industrial", excerpt: "Perimeter alarm system for STMicroelectronics' Loyang semiconductor facility — precision intrusion detection.", tags: ["alarm", "perimeter", "industrial", "semiconductor", "loyang"] },
  { url: "/portfolio/institutions/catholic-centre-waterloo", title: "Catholic Centre Waterloo", section: "Portfolio · Institutions", excerpt: "A decade-long security partnership at 55 Waterloo Street — complete fit-out in 2014 followed by CCTV and access upgrades.", tags: ["cctv", "access-control", "institution", "waterloo", "long-term"] },
  { url: "/portfolio/institutions/changi-airport-lpr-barriers", title: "Changi Airport — LPR Barriers", section: "Portfolio · Institutions", excerpt: "LPR-controlled vehicle barriers for airside access management at Changi Airport.", tags: ["lpr", "barrier", "airport", "institution", "changi"] },
  { url: "/portfolio/institutions/cpf-maxwell-institution", title: "CPF Maxwell", section: "Portfolio · Institutions", excerpt: "Access control and surveillance for a CPF Board facility at Maxwell — high-footfall government service centre.", tags: ["access-control", "cctv", "government", "institution", "maxwell"] },
  { url: "/portfolio/institutions/das-learning-centre-woodlands", title: "DAS Learning Centre Woodlands", section: "Portfolio · Institutions", excerpt: "Security design balancing open access for students with controlled entry for staff at a specialist learning centre.", tags: ["access-control", "cctv", "school", "institution", "woodlands"] },
  { url: "/portfolio/institutions/my-world-preschool-cctv", title: "My World Preschool", section: "Portfolio · Institutions", excerpt: "CCTV surveillance for a preschool campus — child-safe camera placement and coverage designed around safeguarding requirements.", tags: ["cctv", "preschool", "institution", "safeguarding", "school"] },
  { url: "/portfolio/institutions/sengkang-interim-bus-interchange", title: "Sengkang Interim Bus Interchange", section: "Portfolio · Institutions", excerpt: "Design-and-build CCTV system — 53 IP cameras, 5 NVRs, and 28-day retention for the LTA Sengkang Interim Bus Interchange.", tags: ["cctv", "lta", "institution", "bus-interchange", "sengkang"] },
  { url: "/portfolio/institutions/sfx-retreat-centre-punggol", title: "SFX Retreat Centre", section: "Portfolio · Institutions", excerpt: "Security for a religious retreat centre in Punggol — unobtrusive surveillance and access control.", tags: ["cctv", "access-control", "institution", "religious", "punggol"] },
  { url: "/portfolio/managed-living/nursing-hostel-jalan-seh-chuan", title: "Nursing Hostel @ Jln Seh Chuan", section: "Portfolio · Managed Living", excerpt: "Security infrastructure for a nursing hostel — access control and surveillance balancing resident welfare with operational oversight.", tags: ["access-control", "cctv", "healthcare", "hostel", "managed-living"] },
  { url: "/portfolio/managed-living/scb-worker-dormitory-jalan-papan", title: "SCB Worker Dormitory", section: "Portfolio · Managed Living", excerpt: "Turnstile access control with ZKTeco SpeedFace terminals and CCTV for SCB's worker dormitory at Jalan Papan.", tags: ["turnstile", "face-recognition", "cctv", "dormitory", "managed-living"] },
  { url: "/portfolio/residential/dunbar-walk-landed-home", title: "22 Dunbar Walk", section: "Portfolio · Residential", excerpt: "Security upgrade — driveway surveillance, gate automation, and perimeter coverage for a landed property.", tags: ["cctv", "auto-gate", "alarm", "residential", "landed"] },
  { url: "/portfolio/residential/dyson-8-residences-landed-home", title: "8 Dyson Road", section: "Portfolio · Residential", excerpt: "Full residential security installation — intercom, auto gate, and surveillance working as one system.", tags: ["intercom", "auto-gate", "cctv", "residential", "landed"] },
  { url: "/portfolio/residential/lengkok-mariam-landed-home", title: "26 Lengkok Mariam", section: "Portfolio · Residential", excerpt: "Camera coverage and access control designed around the property layout for a landed home.", tags: ["cctv", "access-control", "residential", "landed"] },
  { url: "/portfolio/residential/merryn-road-landed-home", title: "Merryn Road", section: "Portfolio · Residential", excerpt: "Security upgrade replacing ageing infrastructure with a modern integrated system for a landed home.", tags: ["upgrade", "cctv", "alarm", "residential", "landed"] },
  { url: "/portfolio/residential/shelford-landed-home", title: "Shelford Road", section: "Portfolio · Residential", excerpt: "Comprehensive security installation — surveillance, intercom, and gate access working together.", tags: ["cctv", "intercom", "auto-gate", "residential", "landed"] },
  { url: "/portfolio/residential/siglap-bank-landed-home", title: "29 Siglap Bank", section: "Portfolio · Residential", excerpt: "Full security fit-out — camera positions designed around the driveway approach and perimeter.", tags: ["cctv", "alarm", "residential", "landed", "siglap"] },
  { url: "/portfolio/residential/upper-east-coast-road-landed-home", title: "Upper East Coast Road", section: "Portfolio · Residential", excerpt: "Ten years of upgrades for a home — from ageing analogue CCTV to a gate motor that lasted a decade.", tags: ["cctv", "auto-gate", "upgrade", "residential", "landed"] },
];

SECUREVISION.guides = [
  { url: "/resources/guides/auto-gate-guide", title: "Auto Gate Guide", section: "Resources · Guides", excerpt: "How auto gate systems work, motor types, safety requirements, and what to specify for your property.", tags: ["auto-gate", "motor", "residential", "guide", "singapore"] },
  { url: "/resources/guides/burglar-alarm-guide", title: "Burglar Alarm Guide", section: "Resources · Guides", excerpt: "How burglar alarm systems work, zone design, detector types, monitoring options, and Singapore regulations.", tags: ["burglar-alarm", "guide", "zones", "monitoring", "singapore"] },
  { url: "/resources/guides/car-park-barrier-guide", title: "Car Park Barrier Guide", section: "Resources · Guides", excerpt: "LPR barriers, boom gates, RFID, and vehicle management systems for Singapore car parks.", tags: ["lpr", "barrier", "car-park", "vehicle", "guide", "singapore"] },
  { url: "/resources/guides/cctv-guide", title: "CCTV Guide", section: "Resources · Guides", excerpt: "IP cameras, resolution, storage, NVR selection, night vision, analytics, PDPA compliance, and brand evaluation.", tags: ["cctv", "nvr", "ip", "resolution", "guide", "singapore", "pdpa"] },
  { url: "/resources/guides/door-access-guide", title: "Door Access Control Guide", section: "Resources · Guides", excerpt: "Card access, biometrics, face recognition, door controllers, and access management for Singapore buildings.", tags: ["access-control", "biometric", "card", "face-recognition", "guide", "singapore"] },
  { url: "/resources/guides/how-to-evaluate-security-contractor", title: "How to Evaluate a Security Contractor", section: "Resources · Guides", excerpt: "PLRD licensing, reading a quotation, site assessment standards, red flags, warranty terms, and correct handover.", tags: ["contractor", "plrd", "quotation", "evaluation", "guide", "singapore"] },
  { url: "/resources/guides/intercom-guide", title: "Intercom Systems Guide", section: "Resources · Guides", excerpt: "Analogue vs IP, 2-wire retrofit, cloud platforms, door release, lift integration, and mobile app considerations.", tags: ["intercom", "ip", "2-wire", "mobile", "guide", "singapore", "akuvox"] },
  { url: "/resources/guides/office-telephone-guide", title: "IP Telephony Guide", section: "Resources · Guides", excerpt: "IP desk phones, IPPBX systems, SIP protocols, and how to replace legacy keyphone systems in Singapore offices.", tags: ["ip-phone", "ippbx", "sip", "telephony", "guide", "singapore"] },
  { url: "/resources/guides/security-renovation-guide", title: "Security Planning During Renovation", section: "Resources · Guides", excerpt: "Conduit routes, M&E coordination, and what retrofitting costs later — for Singapore BTO, resale, and commercial renovations.", tags: ["renovation", "conduit", "cabling", "guide", "singapore", "bto"] },
  { url: "/resources/guides/wifi-network-guide", title: "Network & Wi-Fi Guide", section: "Resources · Guides", excerpt: "Managed switches, PoE, Wi-Fi access points, and network infrastructure for security systems in Singapore.", tags: ["network", "wifi", "poe", "switches", "guide", "singapore"] },
];

SECUREVISION.checklists = [
  { url: "/resources/checklists/care-facility-checklist", title: "Care Facility Security Checklist", section: "Resources · Checklists", excerpt: "Scored security gap assessment for nursing homes, day care centres, and care facilities in Singapore.", tags: ["checklist", "healthcare", "care-facility", "assessment", "singapore"] },
  { url: "/resources/checklists/commercial-security-checklist", title: "Commercial Security Checklist", section: "Resources · Checklists", excerpt: "Scored security gap assessment for Singapore commercial buildings, offices, and retail properties.", tags: ["checklist", "commercial", "assessment", "office", "singapore"] },
  { url: "/resources/checklists/dormitory-checklist", title: "Dormitory Security Checklist", section: "Resources · Checklists", excerpt: "Scored security gap assessment for worker dormitories — MOM compliance and operational requirements.", tags: ["checklist", "dormitory", "mom", "assessment", "singapore"] },
  { url: "/resources/checklists/institutional-security-checklist", title: "Institutional Security Checklist", section: "Resources · Checklists", excerpt: "Scored security gap assessment for schools, government offices, and civic facilities in Singapore.", tags: ["checklist", "institution", "school", "government", "assessment", "singapore"] },
  { url: "/resources/checklists/intercom-checklist", title: "Intercom System Checklist", section: "Resources · Checklists", excerpt: "Assessment checklist for evaluating intercom system condition and planning an upgrade.", tags: ["checklist", "intercom", "upgrade", "assessment", "condominium", "singapore"] },
  { url: "/resources/checklists/mcst-checklist", title: "MCST Condominium Security Assessment", section: "Resources · Checklists", excerpt: "28-question scored assessment for MCSTs and managing agents — structured for AGM proposals and contractor briefings.", tags: ["checklist", "mcst", "condominium", "agm", "assessment", "singapore"] },
];

SECUREVISION.brands = [
  { url: "/brands/aiphone-intercom", title: "Aiphone Intercom", section: "Brands", excerpt: "Aiphone intercom systems — video door stations and indoor monitors for Singapore properties.", tags: ["aiphone", "intercom", "video-entry", "singapore"] },
  { url: "/brands/ajax-alarms", title: "Ajax Alarm Systems", section: "Brands", excerpt: "Ajax wireless burglar alarm systems — hubs, detectors, and sensors for Singapore residential and commercial installations.", tags: ["ajax", "alarm", "wireless", "singapore"] },
  { url: "/brands/akuvox-access", title: "Akuvox Access Control", section: "Brands", excerpt: "Akuvox access control and intercom products — SmartPlus platform for condominium and estate management.", tags: ["akuvox", "access-control", "smartplus", "condominium", "singapore"] },
  { url: "/brands/akuvox-intercom", title: "Akuvox Intercom", section: "Brands", excerpt: "Akuvox video intercom systems — IP door stations, indoor monitors, and the SmartPlus mobile app.", tags: ["akuvox", "intercom", "video-entry", "smartplus", "condominium"] },
  { url: "/brands/apollo-access", title: "Apollo Access Control", section: "Brands", excerpt: "Apollo access control systems for Singapore commercial and industrial installations.", tags: ["apollo", "access-control", "singapore"] },
  { url: "/brands/dsc-alarms", title: "DSC Alarm Systems", section: "Brands", excerpt: "DSC burglar alarm panels and detectors for Singapore residential and commercial properties.", tags: ["dsc", "alarm", "burglar", "singapore"] },
  { url: "/brands/entrypass-entry-access", title: "EntryPass Access Control", section: "Brands", excerpt: "EntryPass access control systems — readers, controllers, and management software for Singapore buildings.", tags: ["entrypass", "access-control", "singapore"] },
  { url: "/brands/faac-autogate", title: "FAAC Auto Gate", section: "Brands", excerpt: "FAAC gate automation systems — swing gate, sliding gate, and barrier motors for Singapore properties.", tags: ["faac", "auto-gate", "gate-motor", "singapore"] },
  { url: "/brands/fanvil-intercom", title: "Fanvil Intercom", section: "Brands", excerpt: "Fanvil SIP video door phones and intercom systems for Singapore commercial and residential properties.", tags: ["fanvil", "intercom", "sip", "video-entry", "singapore"] },
  { url: "/brands/fanvil-ip-phone", title: "Fanvil IP Phone", section: "Brands", excerpt: "Fanvil IP desk phones for Singapore offices — SIP compatible, PoE powered.", tags: ["fanvil", "ip-phone", "sip", "office", "singapore"] },
  { url: "/brands/gantrygo", title: "GantryGo", section: "Brands", excerpt: "GantryGo cloud-based LPR vehicle management platform — Securevision's proprietary solution for Singapore condominiums.", tags: ["gantrygo", "lpr", "vehicle", "condominium", "cloud", "singapore"] },
  { url: "/brands/ge-caddx-alarms", title: "GE Caddx Alarm Systems", section: "Brands", excerpt: "GE Caddx burglar alarm panels and accessories for Singapore installations.", tags: ["ge-caddx", "alarm", "burglar", "singapore"] },
  { url: "/brands/hanwha-cctv", title: "Hanwha Vision CCTV", section: "Brands", excerpt: "Hanwha Vision IP cameras and NVRs — AI analytics and professional surveillance for Singapore properties.", tags: ["hanwha", "cctv", "ai", "surveillance", "singapore"] },
  { url: "/brands/hid-entry-access", title: "HID Global Access Control", section: "Brands", excerpt: "HID Global access control credentials, readers, and controllers for Singapore commercial and institutional buildings.", tags: ["hid", "access-control", "credentials", "card", "singapore"] },
  { url: "/brands/hikcentral", title: "HikCentral Platform", section: "Brands", excerpt: "HikCentral Professional — unified security management platform integrating CCTV, access, and alarm for Singapore properties.", tags: ["hikcentral", "platform", "management", "hikvision", "singapore"] },
  { url: "/brands/hikvision-access", title: "Hikvision Access Control", section: "Brands", excerpt: "Hikvision access control readers, face recognition terminals, and controllers for Singapore buildings.", tags: ["hikvision", "access-control", "face-recognition", "singapore"] },
  { url: "/brands/hikvision-cctv", title: "Hikvision CCTV", section: "Brands", excerpt: "Hikvision IP cameras, NVRs, and AI analytics — the most widely deployed CCTV brand in Singapore.", tags: ["hikvision", "cctv", "ip", "ai", "nvr", "singapore"] },
  { url: "/brands/hikvision-intercom", title: "Hikvision Intercom", section: "Brands", excerpt: "Hikvision video door stations and intercom systems for Singapore residential and commercial properties.", tags: ["hikvision", "intercom", "video-entry", "singapore"] },
  { url: "/brands/hrui-network", title: "HRUI Network", section: "Brands", excerpt: "HRUI managed PoE switches and network infrastructure for Singapore security systems.", tags: ["hrui", "network", "poe", "switches", "singapore"] },
  { url: "/brands/kocom-intercom", title: "Kocom Intercom", section: "Brands", excerpt: "Kocom audio and video intercom systems for Singapore residential properties.", tags: ["kocom", "intercom", "video-entry", "residential", "singapore"] },
  { url: "/brands/microengine-entry-access", title: "MicroEngine Access Control", section: "Brands", excerpt: "MicroEngine access control systems for Singapore commercial and industrial installations.", tags: ["microengine", "access-control", "singapore"] },
  { url: "/brands/milesight-cctv", title: "Milesight CCTV", section: "Brands", excerpt: "Milesight IP cameras with AI analytics and PoE for Singapore surveillance installations.", tags: ["milesight", "cctv", "ai", "ip", "singapore"] },
  { url: "/brands/omada-network", title: "Omada (TP-Link) Network", section: "Brands", excerpt: "TP-Link Omada managed Wi-Fi and network switches for Singapore security and commercial installations.", tags: ["omada", "tp-link", "wifi", "network", "singapore"] },
  { url: "/brands/paradox-alarms", title: "Paradox Alarm Systems", section: "Brands", excerpt: "Paradox burglar alarm panels, detectors, and keypads for Singapore residential and commercial properties.", tags: ["paradox", "alarm", "burglar", "singapore"] },
  { url: "/brands/risco-alarms", title: "RISCO Alarm Systems", section: "Brands", excerpt: "RISCO wireless and hybrid burglar alarm systems for Singapore residential and commercial installations.", tags: ["risco", "alarm", "wireless", "hybrid", "singapore"] },
  { url: "/brands/ruijie-reyee-network", title: "Ruijie / Reyee Network", section: "Brands", excerpt: "Ruijie and Reyee managed switches, routers, and Wi-Fi for Singapore security network infrastructure.", tags: ["ruijie", "reyee", "network", "wifi", "singapore"] },
  { url: "/brands/suprema-entry-access", title: "Suprema Access Control", section: "Brands", excerpt: "Suprema biometric access control — face recognition, fingerprint, and card readers for Singapore buildings.", tags: ["suprema", "biometric", "face-recognition", "fingerprint", "access-control", "singapore"] },
  { url: "/brands/uniview-cctv", title: "Uniview CCTV", section: "Brands", excerpt: "Uniview IP cameras and NVRs — professional surveillance for Singapore commercial and industrial properties.", tags: ["uniview", "cctv", "ip", "nvr", "singapore"] },
  { url: "/brands/vesta", title: "VESTA Platform", section: "Brands", excerpt: "VESTA — Securevision's proprietary condominium security management platform for managing access, intercoms, and CCTV across estates.", tags: ["vesta", "platform", "condominium", "estate", "singapore"] },
  { url: "/brands/yealink-ip-phone", title: "Yealink IP Phone", section: "Brands", excerpt: "Yealink IP desk phones for Singapore offices — SIP compatible, video calling capable.", tags: ["yealink", "ip-phone", "sip", "office", "singapore"] },
  { url: "/brands/yeastar-ippbx", title: "Yeastar IPPBX", section: "Brands", excerpt: "Yeastar IPPBX systems — replacing legacy keyphone systems with modern IP telephony for Singapore offices.", tags: ["yeastar", "ippbx", "ip-phone", "office", "singapore"] },
  { url: "/brands/zkteco-cvsecurity", title: "ZKBio CVSecurity Platform", section: "Brands", excerpt: "ZKBio CVSecurity — unified access control and CCTV management platform for Singapore commercial and industrial installations.", tags: ["zkteco", "cvsecurity", "platform", "access-control", "singapore"] },
  { url: "/brands/zkteco-entry-access", title: "ZKTeco Access Control", section: "Brands", excerpt: "ZKTeco biometric readers, face recognition terminals, and access controllers for Singapore buildings.", tags: ["zkteco", "biometric", "face-recognition", "access-control", "singapore"] },
];

SECUREVISION.solutions = [
  { url: "/solutions/condominiums/condominium-security-systems", title: "Condominium Security Systems", section: "Solutions · Condominiums", excerpt: "Security systems designed for Singapore condominiums — intercom, LPR, CCTV, and access control.", tags: ["condominium", "security", "systems", "singapore", "mcst"] },
  { url: "/solutions/condominiums/managing-agents", title: "Managing Agents Security Guide", section: "Solutions · Condominiums", excerpt: "Security solutions for managing agents overseeing Singapore condominium estates.", tags: ["managing-agent", "condominium", "estate", "security", "singapore"] },
  { url: "/solutions/condominiums/mcst", title: "MCST Security Solutions", section: "Solutions · Condominiums", excerpt: "Security upgrade planning for MCST councils — AGM proposals, contractor selection, and system design.", tags: ["mcst", "condominium", "agm", "upgrade", "security", "singapore"] },
  { url: "/solutions/residential/landed-home-security-systems", title: "Landed Home Security Systems", section: "Solutions · Residential", excerpt: "Security systems for Singapore landed homes — CCTV, alarm, intercom, and auto gate as one integrated system.", tags: ["residential", "landed", "cctv", "alarm", "intercom", "auto-gate", "singapore"] },
  { url: "/solutions/residential/home-upgrade", title: "Home Security Upgrade", section: "Solutions · Residential", excerpt: "Upgrading existing security systems in Singapore landed homes — what to keep and what to replace.", tags: ["residential", "upgrade", "cctv", "alarm", "singapore"] },
  { url: "/solutions/commercial/office", title: "Office Security Systems", section: "Solutions · Commercial", excerpt: "Access control, CCTV, and IP telephony for Singapore offices — designed around operational workflows.", tags: ["commercial", "office", "access-control", "cctv", "singapore"] },
  { url: "/solutions/commercial/hotel", title: "Hotel Security Systems", section: "Solutions · Commercial", excerpt: "Security systems for Singapore hotels — access control, surveillance, and fire door integration.", tags: ["commercial", "hotel", "access-control", "cctv", "singapore"] },
  { url: "/solutions/industrial/industrial-security-systems", title: "Industrial Security Systems", section: "Solutions · Industrial", excerpt: "CCTV, LPR, access control, and alarm systems for Singapore factories, warehouses, and logistics hubs.", tags: ["industrial", "cctv", "lpr", "access-control", "alarm", "singapore"] },
  { url: "/solutions/institutions/institutions-security-systems", title: "Institutional Security Systems", section: "Solutions · Institutions", excerpt: "Security systems for Singapore schools, government offices, and civic facilities.", tags: ["institution", "school", "government", "cctv", "access-control", "singapore"] },
  { url: "/solutions/healthcare/healthcare-security-systems", title: "Healthcare Security Systems", section: "Solutions · Healthcare", excerpt: "Security systems for Singapore nursing homes, day care centres, and healthcare facilities.", tags: ["healthcare", "nursing-home", "care", "access-control", "cctv", "singapore"] },
  { url: "/solutions/managed-living/managed-living-security-systems", title: "Managed Living Security Systems", section: "Solutions · Managed Living", excerpt: "Security for worker dormitories and co-living properties — MOM compliance and resident management.", tags: ["managed-living", "dormitory", "co-living", "security", "singapore"] },
  { url: "/solutions/managed-living/dormitories", title: "Worker Dormitory Security", section: "Solutions · Managed Living", excerpt: "Security systems for Singapore worker dormitories — turnstile access, CCTV, and MOM compliance.", tags: ["dormitory", "mom", "turnstile", "access-control", "singapore"] },
  { url: "/solutions/reduce-guard-manpower", title: "Reduce Guard Manpower", section: "Solutions", excerpt: "How integrated security systems reduce reliance on security guards in Singapore properties.", tags: ["manpower", "guards", "automation", "cctv", "access-control", "singapore"] },
  { url: "/solutions/automate-vehicle-access", title: "Automate Vehicle Access", section: "Solutions", excerpt: "LPR and barrier systems to automate vehicle entry and reduce guardhouse workload in Singapore.", tags: ["lpr", "vehicle", "automation", "barrier", "singapore"] },
  { url: "/solutions/upgrade-intercom-system", title: "Upgrade Intercom System", section: "Solutions", excerpt: "Upgrading failing or outdated intercom systems in Singapore condominiums and commercial buildings.", tags: ["intercom", "upgrade", "condominium", "akuvox", "singapore"] },
  { url: "/solutions/improve-cctv-visibility", title: "Improve CCTV Visibility", section: "Solutions", excerpt: "Improving CCTV coverage and image quality in Singapore properties — camera positioning and system design.", tags: ["cctv", "visibility", "upgrade", "ai", "singapore"] },
];

SECUREVISION.library = [
  { url: "/resources/library/burglar-alarm", title: "Burglar Alarm Product Library", section: "Resources · Library", excerpt: "Datasheets and specifications for RISCO, Ajax, Paradox, DSC, and GE Caddx alarm systems.", tags: ["alarm", "library", "datasheet", "risco", "ajax", "paradox"] },
  { url: "/resources/library/cctv", title: "CCTV Product Library", section: "Resources · Library", excerpt: "Datasheets and specifications for Hikvision, Milesight, Hanwha, and Uniview cameras and NVRs.", tags: ["cctv", "library", "datasheet", "hikvision", "milesight", "hanwha"] },
  { url: "/resources/library/access-control", title: "Access Control Product Library", section: "Resources · Library", excerpt: "Datasheets for ZKTeco, Suprema, HID, EntryPass, MicroEngine, and Apollo access control products.", tags: ["access-control", "library", "datasheet", "zkteco", "suprema", "hid"] },
  { url: "/resources/library/intercom", title: "Intercom Product Library", section: "Resources · Library", excerpt: "Datasheets for Akuvox, Hikvision, Aiphone, Fanvil, and Kocom intercom products.", tags: ["intercom", "library", "datasheet", "akuvox", "hikvision", "aiphone"] },
  { url: "/resources/library/vehicle", title: "Vehicle Management Product Library", section: "Resources · Library", excerpt: "Datasheets for GantryGo, FAAC, MAG, Dormer, and VIRO vehicle management products.", tags: ["vehicle", "lpr", "library", "datasheet", "faac", "gantrygo"] },
  { url: "/resources/library/ip-telephony", title: "IP Telephony Product Library", section: "Resources · Library", excerpt: "Datasheets for Yeastar, Fanvil, and Yealink IP phones and IPPBX systems.", tags: ["ip-phone", "library", "datasheet", "yeastar", "fanvil", "yealink"] },
  { url: "/resources/library/network", title: "Network Infrastructure Product Library", section: "Resources · Library", excerpt: "Datasheets for Omada, Ruijie/Reyee, and HRUI network switches and Wi-Fi access points.", tags: ["network", "library", "datasheet", "omada", "ruijie", "hrui"] },
  { url: "/resources/library/platform", title: "Platform & Management Product Library", section: "Resources · Library", excerpt: "Documentation for VESTA, HikCentral Professional, and ZKBio CVSecurity management platforms.", tags: ["platform", "library", "datasheet", "vesta", "hikcentral", "cvsecurity"] },
];
