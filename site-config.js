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
  { slug: "ai-analytics-hikvision",                                  title: "AI Analytics in Hikvision Systems — What It Actually Does",         category: "Technology",          tags: ["cctv","ai","hikvision","analytics"] },
  { slug: "analogue-to-ip-migration",                                title: "How Do I Migrate from Analogue to IP CCTV Without Full Replacement?",category: "Technology",          tags: ["cctv","ip","analogue","upgrade","migration"] },
  { slug: "architect-id-guide-security",                             title: "The Architect and ID's Guide to Security Systems in Singapore",     category: "Security Planning",   tags: ["architect","id","design","specification","singapore"] },
  { slug: "burglar-alarm-design",                                    title: "How to Design a Burglar Alarm System",                              category: "Security Planning",   tags: ["burglar-alarm","design","zones","planning"] },
  { slug: "burglar-alarm-detectors-sensors",                         title: "Know Your Burglar Alarm Detectors and Sensors",                    category: "Security Planning",   tags: ["burglar-alarm","detectors","pir","sensors"] },
  { slug: "choose-intercom-for-home",                                title: "How to Choose an Intercom for Your Home",                          category: "Security Planning",   tags: ["intercom","residential","homeowner","video-intercom"] },
  { slug: "compare-security-integrators",                            title: "How to Compare Two Security Integrators Fairly",                   category: "Singapore Industry",  tags: ["integrator","tender","mcst","selection"] },
  { slug: "condo-security-upgrade-proposal",                         title: "What Does a Security Upgrade Proposal to Residents Look Like?",    category: "Estate Management",   tags: ["condo","mcst","agm","proposal","upgrade"] },
  { slug: "condo-security-upgrade-quotes",                           title: "How Do I Get Quotes for an AGM-Approved Security Upgrade?",        category: "Estate Management",   tags: ["condo","mcst","agm","tender","quotes"] },
  { slug: "condo-security-upgrade-timeline",                         title: "Realistic Timeline and Disruption Plan for Condo Security Upgrade",category: "Estate Management",   tags: ["condo","mcst","upgrade","timeline","residents"] },
  { slug: "hdb-landed-condo-security-differences",                   title: "HDB, Landed, or Condo — How Security Requirements Differ",         category: "Security Planning",   tags: ["residential","hdb","landed","condo","singapore"] },
  { slug: "home-security-system-cost-singapore",                     title: "How Much Does a Home Security System Cost in Singapore?",          category: "Security Planning",   tags: ["cost","residential","singapore","homeowner","budget"] },
  { slug: "how-burglar-alarm-works",                                 title: "How Your Burglar Alarm Actually Works",                            category: "Technology",          tags: ["burglar-alarm","how-it-works","controller","zones"] },
  { slug: "how-card-access-works",                                   title: "How Card Access Control Actually Works",                           category: "Technology",          tags: ["access-control","how-it-works","card","controller"] },
  { slug: "how-intercom-systems-work",                               title: "How Intercom Systems Work",                                        category: "Technology",          tags: ["intercom","how-it-works","ip","analogue","sip"] },
  { slug: "how-ip-cctv-works",                                       title: "How an IP CCTV Network Actually Works",                            category: "Technology",          tags: ["cctv","ip","how-it-works","nvr","poe"] },
  { slug: "how-technology-makes-your-guarding-team-more-competitive",title: "How Technology Makes Your Guarding Team More Competitive",         category: "Singapore Industry",  tags: ["guarding","pwm","operations","technology"] },
  { slug: "how-to-choose-auto-gate-motor",                           title: "How to Choose an Auto Gate Motor for Your Home",                   category: "Security Planning",   tags: ["auto-gate","motor","residential","homeowner"] },
  { slug: "how-to-choose-cctv",                                      title: "How to Choose the Right CCTV System for Your Home or Office",      category: "Security Planning",   tags: ["cctv","selection","homeowner","commercial","singapore"] },
  { slug: "how-to-choose-multi-door-access",                         title: "How to Choose a Multi-Door Access Control System",                 category: "Security Planning",   tags: ["access-control","multi-door","commercial","selection"] },
  { slug: "is-my-security-system-still-working",                     title: "Is Your Security System Actually Still Working?",                  category: "Maintenance",         tags: ["maintenance","health-check","cctv","burglar-alarm"] },
  { slug: "maintain-burglar-alarm",                                  title: "How to Maintain Your Burglar Alarm System",                        category: "Maintenance",         tags: ["burglar-alarm","maintenance","battery","walk-test"] },
  { slug: "maintenance-contract",                                    title: "Do You Need a Security System Maintenance Contract?",              category: "Maintenance",         tags: ["maintenance","contract","sla","service"] },
  { slug: "managing-agents-guide-estate-security-systems",           title: "The Managing Agent's Guide to Estate Security Systems",            category: "Estate Management",   tags: ["managing-agent","estate","mcst","systems"] },
  { slug: "managing-multiple-estates-with-vesta",                    title: "Managing Multiple Estates with VESTA",                             category: "Technology",          tags: ["vesta","estate","managing-agent","platform"] },
  { slug: "mcst-legal-obligations-security",                         title: "What Are the MCST's Legal Obligations for Security Systems?",      category: "Estate Management",   tags: ["mcst","legal","bmsma","pdpa","obligations"] },
  { slug: "rackmount-nvr",                                           title: "Rack-Mount NVR vs Desktop NVR — Which Do You Need?",              category: "Technology",          tags: ["nvr","cctv","rack","infrastructure"] },
  { slug: "reduce-false-alarms",                                     title: "How to Reduce False Alarms from Your Burglar Alarm",              category: "Maintenance",         tags: ["burglar-alarm","false-alarm","pir","maintenance"] },
  { slug: "security-system-refresh",                                 title: "Why Your Security System Needs a Refresh",                        category: "Technology",          tags: ["upgrade","refresh","lifecycle","singapore"] },
  { slug: "security-upgrade-condo-agm",                              title: "How to Get a Security Upgrade Approved at a Condo AGM",           category: "Estate Management",   tags: ["condo","agm","mcst","upgrade","residents"] },
  { slug: "standalone-door-access",                                  title: "How to Choose a Standalone Door Access System",                   category: "Security Planning",   tags: ["access-control","standalone","door","office"] },
  { slug: "upgrade-condo-intercom",                                  title: "Upgrading Your Condo Intercom System",                            category: "Estate Management",   tags: ["intercom","condo","upgrade","ip","akuvox"] },
  { slug: "upgrade-existing-security-system",                        title: "Upgrading Your Existing Security System",                         category: "Technology",          tags: ["upgrade","existing","cctv","access-control"] },
  { slug: "upgrade-or-repair",                                       title: "Should You Upgrade or Repair Your Security System?",              category: "Security Planning",   tags: ["upgrade","repair","decision","lifecycle"] },
  { slug: "using-your-burglar-alarm",                                title: "Using Your Burglar Alarm Correctly",                              category: "Security Planning",   tags: ["burglar-alarm","user-guide","homeowner","arming"] },
  { slug: "why-mechanical-locks-not-enough",                         title: "Why Mechanical Locks Are Not Enough",                             category: "Security Planning",   tags: ["locks","access-control","digital","residential"] },
  { slug: "wifi-remote-control-auto-gate",                           title: "WiFi and Remote Control for Your Auto Gate",                      category: "Technology",          tags: ["auto-gate","wifi","remote","smart-home"] }
];
