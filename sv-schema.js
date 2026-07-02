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
 *   3. WebSite + SearchAction               — homepage only (auto-detected)
 *   4. Article                              — opt-in via SV_PAGE.type = "article"
 *   5. TechArticle                          — opt-in via SV_PAGE.type = "guide"
 *   6. WebApplication                       — opt-in via SV_PAGE.type = "tool"
 *   7. FAQPage                              — opt-in via SV_PAGE.faqs array
 *   8. BreadcrumbList                       — opt-in via SV_PAGE.breadcrumbs array
 *
 * To activate schema on a page, add this BEFORE sv-schema.js loads:
 *
 *   window.SV_PAGE = {
 *     type: "article",              // "article" | "guide" | "tool"
 *     title: "Page H1 title here",
 *     description: "Meta description text here",
 *     datePublished: "2026-04-01",  // ISO format
 *     dateModified: "2026-06-01",   // ISO format
 *     faqs: [                       // optional
 *       { q: "Question?", a: "Answer." }
 *     ],
 *     breadcrumbs: [                // optional — omit on homepage only
 *       { name: "Home",     url: "https://www.securevision.com.sg/" },
 *       { name: "Insights", url: "https://www.securevision.com.sg/insights/" },
 *       { name: "Article Title Here" }  // last item: no url
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
    "taxID": "200614644E",
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
    "openingHoursSpecification": [
      {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "09:00",
        "closes": "18:00"
      },
      {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": "Saturday",
        "opens": "09:00",
        "closes": "13:00",
        "description": "By appointment"
      }
    ],
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
      "Condominium Security Management",
      "MCST Security Procurement",
      "Singapore Security Licensing"
    ],
    "hasCredential": [
      {
        "@type": "EducationalOccupationalCredential",
        "name": "Bachelor of Engineering",
        "credentialCategory": "degree",
        "recognizedBy": {
          "@type": "CollegeOrUniversity",
          "name": "National University of Singapore"
        }
      },
      {
        "@type": "EducationalOccupationalCredential",
        "name": "Bachelor of Laws",
        "credentialCategory": "degree",
        "recognizedBy": {
          "@type": "CollegeOrUniversity",
          "name": "University of London"
        }
      }
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
    },
    "url": "https://sg.linkedin.com/in/lerweemeng"
  };

  // ── 3. ARTICLE / TECHARTICLE SCHEMA ─────────────────────────────────────

  function buildArticleSchemas(page) {
    var schemas = [];

    function toSGT(dateStr) {
      if (!dateStr) return null;
      if (dateStr.length > 10) return dateStr;
      return dateStr + "T00:00:00+08:00";
    }

    var ogImageEl = document.querySelector('meta[property="og:image"]');
    var articleImage = page.image || (ogImageEl ? ogImageEl.getAttribute("content") : null);
    var articleType = (page.type === "guide") ? "TechArticle" : "Article";

    schemas.push({
      "@context": "https://schema.org",
      "@type": articleType,
      "headline": page.title,
      "description": page.description,
      "image": articleImage,
      "datePublished": toSGT(page.datePublished),
      "dateModified": toSGT(page.dateModified || page.datePublished),
      "author": {
        "@type": "Person",
        "name": SECUREVISION.authorName,
        "jobTitle": SECUREVISION.authorTitle,
        "url": "https://sg.linkedin.com/in/lerweemeng"
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
        "@id": (function () {
          var canonical = document.querySelector('link[rel="canonical"]');
          return canonical ? canonical.href : window.location.href;
        }())
      }
    });

    if (page.faqs && page.faqs.length > 0) {
      schemas.push({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": page.faqs.map(function (faq) {
          return {
            "@type": "Question",
            "name": faq.q,
            "acceptedAnswer": { "@type": "Answer", "text": faq.a }
          };
        })
      });
    }

    return schemas;
  }

  // ── 4. WEB APPLICATION SCHEMA (calculators & tools) ──────────────────────

  function buildToolSchema(page) {
    var canonical = document.querySelector('link[rel="canonical"]');
    var url = canonical ? canonical.href : window.location.href;
    if (url && !url.endsWith(".html")) url = url + ".html";

    var descEl = document.querySelector('meta[name="description"]');
    var description = page.description || (descEl ? descEl.getAttribute("content") : "");

    var titleEl = document.querySelector('title');
    var name = page.title || (titleEl ? titleEl.textContent.replace(/\s*[|·].*$/, "").trim() : "");

    return {
      "@context": "https://schema.org",
      "@type": "WebApplication",
      "name": name,
      "description": description,
      "url": url,
      "applicationCategory": "SecurityApplication",
      "operatingSystem": "Web",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "SGD"
      },
      "provider": {
        "@type": "LocalBusiness",
        "name": "Securevision Pte Ltd",
        "url": "https://www.securevision.com.sg"
      }
    };
  }

  // ── 5. BREADCRUMBLIST SCHEMA ─────────────────────────────────────────────

  function buildBreadcrumbSchema(crumbs) {
    return {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": crumbs.map(function (crumb, index) {
        var item = {
          "@type": "ListItem",
          "position": index + 1,
          "name": crumb.name
        };
        if (crumb.url) item.item = crumb.url;
        return item;
      })
    };
  }

  // ── 6. WEBSITE + SEARCH ACTION SCHEMA (homepage only) ────────────────────

  var websiteSchema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Securevision",
    "url": "https://www.securevision.com.sg",
    "description": SECUREVISION.tagline,
    "publisher": {
      "@type": "Organization",
      "name": "Securevision Pte Ltd",
      "url": "https://www.securevision.com.sg"
    },
    "potentialAction": {
      "@type": "SearchAction",
      "target": {
        "@type": "EntryPoint",
        "urlTemplate": "https://www.securevision.com.sg/?s={search_term_string}"
      },
      "query-input": "required name=search_term_string"
    }
  };

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

  // WebSite schema — homepage only
  var path = window.location.pathname;
  if (path === "/" || path === "/") {
    injectSchema(websiteSchema);
  }

  if (window.SV_PAGE) {

    // Article or Guide
    if (window.SV_PAGE.type === "article" || window.SV_PAGE.type === "guide") {
      buildArticleSchemas(window.SV_PAGE).forEach(function (s) { injectSchema(s); });
    }

    // Tool (calculator or checklist)
    if (window.SV_PAGE.type === "tool") {
      injectSchema(buildToolSchema(window.SV_PAGE));
    }

    // Breadcrumbs — any page that declares them
    if (window.SV_PAGE.breadcrumbs && window.SV_PAGE.breadcrumbs.length > 0) {
      injectSchema(buildBreadcrumbSchema(window.SV_PAGE.breadcrumbs));
    }

  }

})();
