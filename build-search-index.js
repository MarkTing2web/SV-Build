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

// Strip the DOM injection block (it references document which doesn't exist in Node)
const stripped = configText
  .replace(/document\.addEventListener[\s\S]*?\}\);/g, '')
  .replace(/document\.\w+/g, 'null');

// Evaluate to extract SECUREVISION object
let SECUREVISION;
try {
  eval(stripped);  // populates SECUREVISION in this scope
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
  { url: '/about.html', title: 'About Securevision',      section: 'About',        excerpt: 'Founded in 2006 by Ler Wee Meng, Securevision has delivered security systems across more than 2,000 Singapore installations.' },
  { url: '/contact.html', title: 'Contact Us',            section: 'About',        excerpt: 'Contact Securevision — WhatsApp, email, phone, and address for our Geylang East office.' },
  { url: '/request-site-assessment-singapore.html', title: 'Book a Site Assessment', section: 'About', excerpt: 'Book a free, no-obligation site assessment with a Securevision engineer.' },
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
  { url: '/systems/premises-security.html',              title: 'Premises Security — CCTV & Alarms', section: 'Systems', excerpt: 'CCTV cameras, NVRs, burglar alarms, and perimeter detection for Singapore properties.' },
  { url: '/systems/entry-access-control.html',           title: 'Entry & Access Control',         section: 'Systems', excerpt: 'Card access, biometric readers, face recognition, and door controllers for Singapore buildings.' },
  { url: '/systems/vehicle-lpr-management.html',         title: 'Vehicle & LPR Management',       section: 'Systems', excerpt: 'Licence plate recognition, vehicle barriers, and carpark management systems for Singapore estates.' },
  { url: '/systems/ip-phone-communications.html',        title: 'IP Telephony & Communications',  section: 'Systems', excerpt: 'IP desk phones, IPPBX, and unified communications systems for Singapore offices.' },
  { url: '/systems/network-infrastructure.html',         title: 'Network Infrastructure',          section: 'Systems', excerpt: 'Managed switches, Wi-Fi access points, and structured cabling for security system networks.' },
  { url: '/systems/security-management-platform.html',   title: 'Security Management Platforms',  section: 'Systems', excerpt: 'VESTA, HikCentral, and ZKBio CVSecurity — unified platforms for managing all security systems.' },
  // Brands
  { url: '/brands/', title: 'Security Brands & Products', section: 'Brands', excerpt: 'Brands Securevision installs and supports — Hikvision, Akuvox, ZKTeco, Ajax, Suprema, HID, FAAC, and more.' },
  // Portfolio
  { url: '/portfolio/', title: 'Project Portfolio', section: 'Portfolio', excerpt: 'Completed security installations across Singapore — condominiums, offices, factories, institutions, healthcare, and residential properties.' },
  // Resources
  { url: '/resources/',                         title: 'Resources Hub',                  section: 'Resources', excerpt: 'Technical guides, checklists, calculators, product library, training videos, and FAQ for Singapore security systems.' },
  { url: '/resources/guides.html',              title: 'Technical Guides',               section: 'Resources', excerpt: 'Nine in-depth guides on CCTV, alarms, access control, intercoms, auto gates, networks, and renovation planning.' },
  { url: '/resources/checklists.html',          title: 'Security Planning Checklists',   section: 'Resources', excerpt: 'Scored gap assessments for condominiums, commercial buildings, care facilities, and dormitories.' },
  { url: '/resources/calculators.html',         title: 'Security System Calculators',    section: 'Resources', excerpt: 'CCTV storage, camera coverage, CCTV cost, and access control cost calculators — Singapore-calibrated.' },
  { url: '/resources/library.html',             title: 'Product Library',                section: 'Resources', excerpt: 'Datasheets, manuals, and specifications for every security brand Securevision installs in Singapore.' },
  { url: '/resources/training-videos.html',     title: 'Training Videos',                section: 'Resources', excerpt: 'Akuvox SmartPlus tutorials for residents and managing agents, plus manufacturer product videos.' },
  { url: '/resources/faq.html',                 title: 'Security FAQ',                   section: 'Resources', excerpt: '68 answered questions on CCTV, alarms, access control, intercoms, LPR, condominiums, and renovation planning.' },
  // Insights hub
  { url: '/insights/', title: 'Insights from the Field', section: 'Insights', excerpt: 'Practical articles on security systems written from decades of Singapore installation experience.' },
];

// ── 3. Build index ─────────────────────────────────────────────────────────
const index = [];

// Static pages first
staticPages.forEach(function (p) {
  index.push({ url: p.url, title: p.title, section: p.section, excerpt: p.excerpt, tags: [] });
});

// Articles from site-config.js
articles.forEach(function (a) {
  index.push({
    url:     '/insights/' + a.slug + '.html',
    title:   a.title,
    section: 'Insights · ' + (a.category || 'General'),
    excerpt: (a.category || 'Insights') + ' article from the Securevision field library.',
    tags:    a.tags || [],
  });
});

// ── 4. Write output ────────────────────────────────────────────────────────
const outPath = path.join(__dirname, 'search-index.json');
fs.writeFileSync(outPath, JSON.stringify(index, null, 2), 'utf8');

console.log(`✅ search-index.json written — ${index.length} entries`);
console.log(`   Static pages: ${staticPages.length}`);
console.log(`   Articles:     ${articles.length}`);
console.log(`   Output:       ${outPath}`);
