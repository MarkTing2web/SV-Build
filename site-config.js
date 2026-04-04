const SECUREVISION = {
  foundedYear: 2006,
  experienceStartYear: 1989,
  licenceNumber: 'L/PS/000267/2023P',
  licenceExpiry: '2024', // update annually
  totalSites: 1000,
  whatsapp: '6593860466',
  phone: '+65 6286 4796',
  email: 'enquiry@securevision.com.sg',
  address: 'Blk 1013 Geylang East Avenue 3 #02-142 Singapore 389728',
  
  // Site Metadata
  siteTitle: 'Securevision | Smart Security & Integrated Systems',
  tagline: 'Connecting People, Securing Places',
  
  // Author Info
  authorName: 'Ler Wee Meng',
  authorTitle: 'Founder & CEO, Securevision Pte Ltd',
  get authorDescription() {
    return `Wee Meng has over ${this.yearsExperience} years of experience in security systems engineering and integration. He holds a BEng in Electrical and Electronic Engineering from the National University of Singapore and a law degree from the University of London.`;
  },
  get authorStory() {
    return `He founded Securevision in ${this.foundedYear} and has since led security system deployments across more than ${this.siteDisplay} in Singapore — spanning residential properties, condominiums, commercial buildings, industrial facilities, and institutions.`;
  },
  authorExpertise: "His technical focus spans CCTV and AI video analytics, IP intercom systems, access control, licence plate recognition, and integrated platform design. He is the architect behind VESTA, Securevision's unified security platform built specifically for condominium management in Singapore.",
  authorClientFocus: "Wee Meng works directly with managing agents, MCSTs, property developers, architects, and security companies to design systems that are engineered for the site, not sold off a catalogue.",

  // Calculated values
  get yearsInBusiness() {
    return new Date().getFullYear() - this.foundedYear;
  },
  get yearsExperience() {
    return new Date().getFullYear() - this.experienceStartYear;
  },
  get siteDisplay() {
    return this.totalSites.toLocaleString() + '+ Sites';
  },

  // Strategic Endpoints
  assessmentLink: 'request-site-assessment-singapore.html',
  whatsappLink: 'https://wa.me/6593860466',
  generalContactLink: 'contact.html'
};
