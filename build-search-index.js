/**
 * build-search-index.js
 * Generates search-index.json for sv-search.js
 *
 * Run from repo root:
 *   node build-search-index.js
 *
 * Run whenever you add articles to site-config.js or add new pages.
 * Output: search-index.json (repo root)
 */

const fs   = require('fs');
const path = require('path');

// ── 1. Read insights from site-config.js ──────────────────────────────────
// We extract the SECUREVISION.insights array by reading the file as text
// and using a simple eval in a sandboxed scope.

const configPath = path.join(__dirname, 'site-config.js');
const configText = fs.readFileSync(configPath, 'utf8');

// Define a mock document object and SECUREVISION global, then evaluate site-config.js
let SECUREVISION;
try {
  const document = {
    addEventListener: () => {},
    querySelectorAll: () => ({ forEach: () => {} })
  };
  const processed = configText.replace(/const SECUREVISION =/, 'SECUREVISION =');
  eval(processed);
} catch (e) {
  console.error('Could not parse site-config.js:', e.message);
  process.exit(1);
}
const articles = SECUREVISION.insights || [];
console.log(`✅ Read ${articles.length} articles from site-config.js`);

// ── 2. Static pages ────────────────────────────────────────────────────────
const staticPages = [
  // Homepage & core
  { url: '/',           title: 'Home',                    section: 'Securevision', excerpt: 'Security systems designed to work as one — CCTV, access control, intercoms, vehicle management, and integrated platforms for Singapore properties.' },
  { url: '/about', title: 'About Securevision',      section: 'About',        excerpt: 'Founded in 2006 by Ler Wee Meng, Securevision has delivered security systems across more than 2,000 Singapore installations.' },
  { url: '/contact', title: 'Contact Us',            section: 'About',        excerpt: 'Contact Securevision — WhatsApp, email, phone, and address for our Geylang East office.' },
  { url: '/request-site-assessment-singapore', title: 'Book a Site Assessment', section: 'About', excerpt: 'Book a free, no-obligation site assessment with a Securevision engineer.' },
  // Solutions
  { url: '/solutions/',                      title: 'Security Solutions Overview', section: 'Solutions', excerpt: 'Security solutions for residential, condominium, commercial, industrial, institutional, healthcare, managed living, and data centre properties.' },
  { url: '/solutions/residential/',          title: 'Residential Security',        section: 'Solutions', excerpt: 'CCTV, burglar alarm, video intercom, auto gate, and access control for landed homes in Singapore.' },
  { url: '/solutions/condominiums/',         title: 'Condominium Security',        section: 'Solutions', excerpt: 'Intercom upgrades, LPR vehicle management, access control, and estate-wide CCTV for Singapore condominiums and MCSTs.' },
  { url: '/solutions/commercial/',           title: 'Commercial Security',         section: 'Solutions', excerpt: 'Access control, CCTV, IP telephony, and visitor management for Singapore offices, hotels, and commercial buildings.' },
  { url: '/solutions/industrial/',           title: 'Industrial Security',         section: 'Solutions', excerpt: 'Perimeter CCTV, LPR vehicle barriers, access control, and alarm systems for Singapore factories and warehouses.' },
  { url: '/solutions/institutions/',         title: 'Institutional Security',      section: 'Solutions', excerpt: 'Security systems for schools, government offices, and civic facilities in Singapore.' },
  { url: '/solutions/healthcare/',           title: 'Healthcare Security',         section: 'Solutions', excerpt: 'Access control and surveillance for nursing homes, day care centres, and care facilities in Singapore.' },
  { url: '/solutions/managed-living/',       title: 'Managed Living Security',     section: 'Solutions', excerpt: 'Security systems for worker dormitories and co-living properties — MOM compliance and resident management.' },
  { url: '/solutions/data-centres/',         title: 'Data Centre Security',        section: 'Solutions', excerpt: 'Tiered access control, biometric verification, and comprehensive CCTV for Singapore data centres.' },
  // Systems
  { url: '/systems/',                                    title: 'Security Systems Overview',      section: 'Systems', excerpt: 'Six integrated system groups — premises security, entry and access, vehicle management, IP telephony, network infrastructure, and management platforms.' },
  { url: '/systems/premises-security',              title: 'Premises Security — CCTV & Alarms', section: 'Systems', excerpt: 'CCTV cameras, NVRs, burglar alarms, and perimeter detection for Singapore properties.' },
  { url: '/systems/entry-access-control',           title: 'Entry & Access Control',         section: 'Systems', excerpt: 'Card access, biometric readers, face recognition, and door controllers for Singapore buildings.' },
  { url: '/systems/vehicle-lpr-management',         title: 'Vehicle & LPR Management',       section: 'Systems', excerpt: 'Licence plate recognition, vehicle barriers, and carpark management systems for Singapore estates.' },
  { url: '/systems/ip-phone-communications',        title: 'IP Telephony & Communications',  section: 'Systems', excerpt: 'IP desk phones, IPPBX, and unified communications systems for Singapore offices.' },
  { url: '/systems/network-infrastructure',         title: 'Network Infrastructure',          section: 'Systems', excerpt: 'Managed switches, Wi-Fi access points, and structured cabling for security system networks.' },
  { url: '/systems/security-management-platform',   title: 'Security Management Platforms',  section: 'Systems', excerpt: 'VESTA, HikCentral, and ZKBio CVSecurity — unified platforms for managing all security systems.' },
  // Brands
  { url: '/brands/', title: 'Security Brands & Products', section: 'Brands', excerpt: 'Brands Securevision installs and supports — Hikvision, Akuvox, ZKTeco, Ajax, Suprema, HID, FAAC, and more.' },
  { url: '/brands/dahua-cctv.html', title: "Dahua CCTV Systems", section: "Brands", excerpt: "Dahua CCTV cameras and surveillance systems supplied and installed by Securevision across Singapore.", tags: ["dahua", "cctv", "surveillance", "ip camera", "brands"] },
  // Portfolio
  { url: '/portfolio/', title: 'Project Portfolio', section: 'Portfolio', excerpt: 'Completed security installations across Singapore — condominiums, offices, factories, institutions, healthcare, and residential properties.' },
  // Resources
  { url: '/resources/',                         title: 'Resources Hub',                  section: 'Resources', excerpt: 'Technical guides, checklists, calculators, product library, training videos, and FAQ for Singapore security systems.' },
  { url: '/resources/guides',              title: 'Technical Guides',               section: 'Resources', excerpt: 'Nine in-depth guides on CCTV, alarms, access control, intercoms, auto gates, networks, and renovation planning.' },
  { url: '/resources/checklists',          title: 'Security Planning Checklists',   section: 'Resources', excerpt: 'Scored gap assessments for condominiums, commercial buildings, care facilities, and dormitories.' },
  { url: '/resources/calculators',         title: 'Security System Calculators',    section: 'Resources', excerpt: 'CCTV storage, camera coverage, CCTV cost, and access control cost calculators — Singapore-calibrated.' },
  { url: '/resources/library',             title: 'Product Library',                section: 'Resources', excerpt: 'Datasheets, manuals, and specifications for every security brand Securevision installs in Singapore.' },
  { url: '/resources/library/burglar-alarm.html', title: 'Burglar Alarm Product Library', section: 'Resources · Library', excerpt: 'Datasheets and specifications for RISCO, Ajax, Paradox, DSC, and GE Caddx alarm systems.', tags: ["alarm", "library", "datasheet", "risco", "ajax", "paradox", "dsc", "ge-caddx", "lightsys2", "agility4", "hub2plus", "motioncam", "doorprotect", "spectra", "evo", "powerseries", "nx8v2", "burglar-alarm", "singapore"] },
  { url: '/resources/training-videos',     title: 'Training Videos',                section: 'Resources', excerpt: 'Akuvox SmartPlus tutorials for residents and managing agents, plus manufacturer product videos.' },
  { url: '/resources/faq',                 title: 'Security FAQ',                   section: 'Resources', excerpt: '68 answered questions on CCTV, alarms, access control, intercoms, LPR, condominiums, and renovation planning.' },
  // Insights hub
  { url: '/insights/', title: 'Insights from the Field', section: 'Insights', excerpt: 'Practical articles on security systems written from decades of Singapore installation experience.' },
];

// ── 3. Build index ─────────────────────────────────────────────────────────
const index = [];

// Static pages first
staticPages.forEach(function (p) {
  index.push({ url: p.url, title: p.title, section: p.section, excerpt: p.excerpt, tags: p.tags || [] });
});

// Articles from site-config.js
articles.forEach(function (a) {
  let url = '/insights/' + a.slug;
  let excerpt = (a.category || 'Insights') + ' article from the Securevision field library.';
  let tags = a.tags || [];

  if (a.slug === 'ge-caddx-networx-support-singapore') {
    url = '/insights/ge-caddx-networx-support-singapore.html';
    excerpt = 'Interlogix ceased manufacturing in 2019. Here is what Securevision can still do for your NX4, NX6, NX8, or NX8E panel — and when it is time to upgrade.';
    tags = ["ge-caddx", "networx", "nx8v2", "nx8", "nx4", "burglar-alarm", "upgrade", "interlogix", "singapore", "alarm"];
  }

  index.push({
    url:     url,
    title:   a.title,
    section: 'Insights · ' + (a.category || 'General'),
    excerpt: excerpt,
    tags:    tags,
  });
});

// ── 4. Write output ────────────────────────────────────────────────────────
const outPath = path.join(__dirname, 'search-index.json');
fs.writeFileSync(outPath, JSON.stringify(index, null, 2), 'utf8');

console.log(`✅ search-index.json written — ${index.length} entries`);
console.log(`   Static pages: ${staticPages.length}`);
console.log(`   Articles:     ${articles.length}`);
console.log(`   Output:       ${outPath}`);
