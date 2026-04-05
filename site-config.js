const SECUREVISION = {
  // ── CORE IDENTITY ──────────────────────────────────────────────────
  foundedYear: 2006,
  experienceStartYear: 1989,
  licenceNumber: 'L/PS/000267/2023P',
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

  // Tagline — class: .sv-tagline
  document.querySelectorAll('.sv-tagline').forEach(el => {
    el.textContent = SECUREVISION.tagline;
  });

});
