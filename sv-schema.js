/**
 * sv-schema.js — Securevision JSON-LD Schema Generator
 * ─────────────────────────────────────────────────────
 * Injects structured schema markup into the <head> of every page.
 * Depends on site-config.js (SECUREVISION object) being loaded first.
 *
 * USAGE: Load this script in your global header template, AFTER site-config.js.
 *   <script src="/sv-schema.js"></script>
 *
 * Schema types injected:
 *   1. LocalBusiness / ProfessionalService  — global identity (all pages)
 *   2. Person (founder)                     — global (all pages)
 *   3. FAQPage                              — insights articles only (opt-in)
 *   4. Article                              — insights articles only (opt-in)
 *
 * To activate Article + FAQPage schema on an insights article, add this
 * to the page's own <script> block BEFORE sv-schema.js loads:
 *
 *   window.SV_PAGE = {
 *     type: "article",
 *     title: "Page H1 title here",
 *     description: "Meta description text here",
 *     datePublished: "2025-10-01",   // ISO format
 *     dateModified: "2026-06-01",    // ISO format
 *     faqs: [                        // optional — omit if no FAQ section
 *       { q: "Question text here?", a: "Answer paragraph here." },
 *       { q: "Second question?",    a: "Second answer." }
 *     ]
 *   };
 */

(function () {

  // ── 1. ORGANISATION / LOCAL BUSINESS SCHEMA ──────────────────────────────

  const orgSchema = {
    "@context": "https://schema.org",
    "@type": ["LocalBusiness", "ProfessionalService"],
    "name": "Securevision",
    "legalName": "Securevision Pte Ltd",
    "url": "https://www.securevision.com.sg",
    "logo": "https://www.securevision.com.sg/assets/images/sv-logo.png",
    "image": "https://www.securevision.com.sg/assets/images/hero-securevision.jpg",
    "description": SECUREVISION.tagline,
    "telephone": SECUREVISION.phone,
    "email": SECUREVISION.email,
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Blk 1013 Geylang East Avenue 3 #02-142",
      "addressLocality": "Singapore",
      "postalCode": "389728",
      "addressCountry": "SG"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 1.3185,
      "longitude": 103.8927
    },
    "openingHoursSpecification": {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "18:00"
    },
    "areaServed": {
      "@type": "AdministrativeArea",
      "name": "Singapore"
    },
    "foundingDate": String(SECUREVISION.foundedYear),
    "numberOfEmployees": {
      "@type": "QuantitativeValue",
      "minValue": 10,
      "maxValue": 49
    },
    "knowsAbout": [
      "Burglar Alarm Systems",
      "Door Access Control",
      "Video Intercom Systems",
      "CCTV Surveillance",
      "IP Camera Systems",
      "Auto Gate Systems",
      "Licence Plate Recognition",
      "MCST Security Tenders",
      "Condominium Security Systems",
      "Landed Property Security",
      "Industrial Security Systems",
      "Security System Integration Singapore"
    ],
    "hasCredential": [
      {
        "@type": "EducationalOccupationalCredential",
        "name": "PLRD Security Contractor Licence",
        "credentialCategory": "licence",
        "recognizedBy": {
          "@type": "GovernmentOrganization",
          "name": "Singapore Police Licensing & Regulatory Department"
        },
        "identifier": SECUREVISION.licenceNumber
      },
      {
        "@type": "EducationalOccupationalCredential",
        "name": "bizSAFE Level 3",
        "credentialCategory": "certification",
        "recognizedBy": {
          "@type": "Organization",
          "name": "Workplace Safety and Health Council Singapore"
        }
      }
    ],
    "sameAs": [
      "https://www.securevision.com.sg",
      "https://sg.linkedin.com/company/securevision-pte-ltd",
      "https://www.facebook.com/securevision/",
      "https://www.youtube.com/@securevision"
    ]
  };

  // ── 2. FOUNDER / PERSON SCHEMA ───────────────────────────────────────────

  const founderSchema = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": SECUREVISION.authorName,
    "jobTitle": SECUREVISION.authorTitle,
    "description": SECUREVISION.authorDescription + " " + SECUREVISION.authorStory,
    "knowsAbout": [
      "Security Systems Integration",
      "CCTV and AI Video Analytics",
      "IP Intercom Systems",
      "Access Control",
      "Licence Plate Recognition",
      "Condominium Security Management"
    ],
    "alumniOf": [
      {
        "@type": "CollegeOrUniversity",
        "name": "National University of Singapore",
        "sameAs": "https://www.nus.edu.sg"
      },
      {
        "@type": "CollegeOrUniversity",
        "name": "University of London",
        "sameAs": "https://www.london.ac.uk"
      }
    ],
    "worksFor": {
      "@type": "Organization",
      "name": "Securevision Pte Ltd",
      "url": "https://www.securevision.com.sg"
    }
  };

  // ── 3. ARTICLE + FAQPAGE SCHEMA (insights pages only) ───────────────────

  function buildArticleSchemas(page) {
    const schemas = [];

    // Article schema
    schemas.push({
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": page.title,
      "description": page.description,
      "datePublished": page.datePublished,
      "dateModified": page.dateModified || page.datePublished,
      "author": {
        "@type": "Person",
        "name": SECUREVISION.authorName,
        "jobTitle": SECUREVISION.authorTitle
      },
      "publisher": {
        "@type": "Organization",
        "name": "Securevision",
        "logo": {
          "@type": "ImageObject",
          "url": "https://www.securevision.com.sg/assets/images/sv-logo.png"
        }
      },
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": window.location.href
      }
    });

    // FAQPage schema — only if faqs array is provided and non-empty
    if (page.faqs && page.faqs.length > 0) {
      schemas.push({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": page.faqs.map(function (faq) {
          return {
            "@type": "Question",
            "name": faq.q,
            "acceptedAnswer": {
              "@type": "Answer",
              "text": faq.a
            }
          };
        })
      });
    }

    return schemas;
  }

  // ── INJECTION UTILITY ────────────────────────────────────────────────────

  function injectSchema(schemaObj) {
    var script = document.createElement("script");
    script.type = "application/ld+json";
    script.textContent = JSON.stringify(schemaObj, null, 2);
    document.head.appendChild(script);
  }

  // ── EXECUTE ──────────────────────────────────────────────────────────────

  // Always inject org + founder schema on every page
  injectSchema(orgSchema);
  injectSchema(founderSchema);

  // Inject article schemas only if this page has declared SV_PAGE
  if (window.SV_PAGE && window.SV_PAGE.type === "article") {
    var articleSchemas = buildArticleSchemas(window.SV_PAGE);
    articleSchemas.forEach(function (schema) {
      injectSchema(schema);
    });
  }

})();
