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
  { slug: "10-tips-securing-your-premises",                          title: "10 Tips for Securing Your Home or Office in Singapore",              category: "Security Planning",   tags: ["homeowner","commercial","perimeter","singapore"] },
  { slug: "after-security-installation-support",                     title: "After Installation — Who Do You Call and What to Expect?",          category: "Security Planning",   tags: ["after-sales","maintenance","warranty","user-guide"] },
  { slug: "ai-analytics-hikvision",                                  title: "AI Analytics in Hikvision Systems — What It Actually Does",         category: "CCTV & Surveillance",          tags: ["cctv","ai","hikvision","analytics"] },
  { slug: "analogue-to-ip-migration",                                title: "How Do I Migrate from Analogue to IP CCTV Without Full Replacement?",category: "CCTV & Surveillance",          tags: ["cctv","ip","analogue","upgrade","migration"] },
  { slug: "architect-id-guide-security",                             title: "The Architect and ID's Guide to Security Systems in Singapore",     category: "Security Planning",   tags: ["architect","id","design","specification","singapore"] },
  { slug: "burglar-alarm-design",                                    title: "How to Design a Burglar Alarm System",                              category: "Alarm & Intrusion",   tags: ["burglar-alarm","design","zones","planning"], excerpt: "Most alarm systems are zoned wrong from day one. Here is how professional security engineers think about scope, zones, and response priorities before a single detector goes up.", image: "burglar-alarm-design-feature.webp" },
  { slug: "burglar-alarm-detectors-sensors", title: "The Right Detector for the Right Job", category: "Alarm & Intrusion", tags: ["burglar-alarm","detectors","pir","sensors"], excerpt: "Your alarm system is only as good as the detectors in it. A plain-English guide to the main sensor types, where each one works, and how to choose the right one for each zone.", image: "burglar-alarm-detectors-sensors-feature.webp" },
  { slug: "alarm-communication-paths", title: "Why Banks Use Multiple Communication Paths", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-monitoring","communication-paths","singapore"], excerpt: "Why do banks use multiple communication paths for alarm monitoring? Learn how leased lines, PSTN, IP networks and mobile data work together to eliminate single points of failure and improve alarm reliability.", image: "alarm-communication-paths-feature.webp" },
  { slug: "alarm-internet-cut", title: "What Happens If a Burglar Cuts the Internet?", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-reliability","communication-paths","singapore"], excerpt: "What happens if a burglar cuts your internet connection? Learn how modern alarm systems continue operating without internet access, why sirens remain effective, and how dual-path communications provide additional protection.", image: "alarm-internet-cut-feature.webp" },
  { slug: "alarm-panel-polling", title: "Why Alarm Panels Used to Call Home Every Seven Days", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-monitoring","security-history","singapore"], excerpt: "Why did alarm panels send test signals every seven days? Discover the hidden engineering behind telephone-line alarm monitoring and how monitoring centres managed tens of thousands of accounts before the internet era.", image: "alarm-panel-polling-feature.webp" },
  { slug: "alarm-monitoring-history", title: "How Alarm Monitoring Worked Before the Internet", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-monitoring","security-history","singapore"], excerpt: "How did burglar alarm monitoring work before the internet? Discover how alarm panels used telephone lines, diallers and Central Monitoring Stations to protect homes and businesses long before mobile apps existed.", image: "alarm-monitoring-history-feature.webp" },
  { slug: "alarm-panel", title: "The Alarm Panel: The Brain Behind Your Burglar Alarm System", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-panel","wired","wireless"], excerpt: "The alarm panel is the brain behind every burglar alarm system. Learn how panels work, how many zones you need, the difference between wired and wireless, and how to choose the right one for your property.", image: "alarm-panel-feature.webp" },
  { slug: "choose-intercom-for-home",                                title: "How to Choose an Intercom for Your Home",                          category: "Access & Intercom",   tags: ["intercom","residential","homeowner","video-intercom"] },
  { slug: "compare-security-integrators",                            title: "How to Compare Two Security Integrators Fairly",           category: "Security Planning", tags: ["integrator","tender","selection","singapore","contractor","comparison"] },
  { slug: "condo-security-upgrade-proposal",                         title: "What Does a Security Upgrade Proposal to Residents Look Like?",    category: "Security Planning",   tags: ["condo","mcst","agm","proposal","upgrade"] },
  { slug: "condo-security-upgrade-quotes",                           title: "How Do I Get Quotes for an AGM-Approved Security Upgrade?",        category: "Security Planning",   tags: ["condo","mcst","agm","tender","quotes"] },
  { slug: "condo-security-upgrade-timeline",                         title: "Realistic Timeline and Disruption Plan for Condo Security Upgrade",category: "Security Planning",   tags: ["condo","mcst","upgrade","timeline","residents"] },
  { slug: "hdb-landed-condo-security-differences",                   title: "HDB, Landed, or Condo — How Security Requirements Differ",         category: "Security Planning",   tags: ["residential","hdb","landed","condo","singapore"] },
  { slug: "home-security-system-cost-singapore",                     title: "How Much Does a Home Security System Cost in Singapore?",          category: "Security Planning",   tags: ["cost","residential","singapore","homeowner","budget"] },
  { slug: "how-burglar-alarm-works",                                 title: "How Your Burglar Alarm Actually Works",                            category: "Alarm & Intrusion",          tags: ["burglar-alarm","how-it-works","controller","zones"] },
  { slug: "how-card-access-works",                                   title: "How Card Access Control Actually Works",                           category: "Access & Intercom",          tags: ["access-control","how-it-works","card","controller"] },
  { slug: "how-intercom-systems-work",                               title: "How Intercom Systems Work",                                        category: "Access & Intercom",          tags: ["intercom","how-it-works","ip","analogue","sip"] },
  { slug: "how-ip-cctv-works",                                       title: "How an IP CCTV Network Actually Works",                            category: "CCTV & Surveillance",          tags: ["cctv","ip","how-it-works","nvr","poe"] },
  { slug: "how-technology-makes-your-guarding-team-more-competitive",title: "How Technology Makes Your Guarding Team More Competitive",  category: "Platform & Integration",        tags: ["guarding","operations","technology","singapore","ai","analytics"] },
  { slug: "how-to-choose-auto-gate-motor",                           title: "How to Choose an Auto Gate Motor for Your Home",                   category: "Vehicle & Gates",   tags: ["auto-gate","motor","residential","homeowner"] },
  { slug: "how-to-choose-cctv",                                      title: "How to Choose the Right CCTV System for Your Home or Office",      category: "CCTV & Surveillance",   tags: ["cctv","selection","homeowner","commercial","singapore"] },
  { slug: "how-to-choose-multi-door-access",                         title: "How to Choose a Multi-Door Access Control System",                 category: "Access & Intercom",   tags: ["access-control","multi-door","commercial","selection"] },
  { slug: "lpr-vs-rfid-vehicle-access-singapore",                    title: "LPR vs RFID for Vehicle Access in Singapore Condominiums",  category: "Vehicle & Gates",        tags: ["lpr","rfid","vehicle","access-control","condo","car-park","singapore"] },
  { slug: "is-my-security-system-still-working",                     title: "Is Your Security System Actually Still Working?",                  category: "Security Planning",         tags: ["maintenance","health-check","cctv","burglar-alarm"] },
  { slug: "maintain-burglar-alarm",                                  title: "How to Maintain Your Burglar Alarm System",                        category: "Alarm & Intrusion",         tags: ["burglar-alarm","maintenance","battery","walk-test"] },
  { slug: "maintenance-contract",                                    title: "Do You Need a Security System Maintenance Contract?",              category: "Security Planning",         tags: ["maintenance","contract","sla","service"] },
  { slug: "managing-agents-guide-estate-security-systems",           title: "The Managing Agent's Guide to Estate Security Systems",            category: "Security Planning",   tags: ["managing-agent","estate","mcst","systems"] },
  { slug: "managing-multiple-estates-with-vesta",                    title: "Managing Multiple Estates with VESTA",                     category: "Platform & Integration",        tags: ["vesta","estate","managing-agent","platform","mcst","cctv","access-control"] },
  { slug: "mcst-legal-obligations-security",                         title: "What Are the MCST's Legal Obligations for Security Systems?",      category: "Security Planning",   tags: ["mcst","legal","bmsma","pdpa","obligations"] },
  { slug: "pdpa-cctv-singapore",                                      title: "PDPA and CCTV in Singapore: What Property Managers Must Know", category: "CCTV & Surveillance", tags: ["pdpa","cctv","compliance","singapore","legal","privacy"] },
  { slug: "rackmount-nvr",                                           title: "Rack-Mount NVR vs Desktop NVR — Which Do You Need?",              category: "CCTV & Surveillance",          tags: ["nvr","cctv","rack","infrastructure"] },
  { slug: "reduce-false-alarms",                                     title: "How to Reduce False Alarms from Your Burglar Alarm",              category: "Alarm & Intrusion",         tags: ["burglar-alarm","false-alarm","pir","maintenance"] },
  { slug: "security-system-refresh",                                 title: "Why Your Security System Needs a Refresh",                        category: "Security Planning",          tags: ["upgrade","refresh","lifecycle","singapore"] },
  { slug: "security-upgrade-condo-agm",                              title: "How to Get a Security Upgrade Approved at a Condo AGM",           category: "Security Planning",   tags: ["condo","agm","mcst","upgrade","residents"] },
  { slug: "standalone-door-access",                                  title: "How to Choose a Standalone Door Access System",                   category: "Access & Intercom",   tags: ["access-control","standalone","door","office"] },
  { slug: "upgrade-condo-intercom",                                  title: "Upgrading Your Condo Intercom System",                            category: "Access & Intercom",   tags: ["intercom","condo","upgrade","ip","akuvox"] },
  { slug: "upgrade-existing-security-system",                        title: "Upgrading Your Existing Security System",                         category: "Security Planning",          tags: ["upgrade","existing","cctv","access-control"] },
  { slug: "upgrade-or-repair",                                       title: "Should You Upgrade or Repair Your Security System?",       category: "Security Planning", tags: ["upgrade","repair","decision","lifecycle","maintenance","cctv","burglar-alarm"] },
  { slug: "video-analytics-retail-singapore",                         title: "Video Analytics in Retail Security: A Singapore Guide",      category: "CCTV & Surveillance",        tags: ["video-analytics","retail","cctv","ai","analytics","singapore"] },
  { slug: "using-your-burglar-alarm",                                title: "Using Your Burglar Alarm Correctly",                              category: "Alarm & Intrusion",   tags: ["burglar-alarm","user-guide","homeowner","arming"] },
  { slug: "why-mechanical-locks-not-enough",                         title: "Why Mechanical Locks Are Not Enough",                             category: "Access & Intercom",   tags: ["locks","access-control","digital","residential"] },
  { slug: "wifi-remote-control-auto-gate",                           title: "WiFi and Remote Control for Your Auto Gate",               category: "Vehicle & Gates",        tags: ["auto-gate","wifi","remote","smart-home","upgrade","residential"] }
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
