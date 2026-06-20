/*!
 * sv-search.js — Securevision Site Search
 * Uses Fuse.js for fuzzy client-side search over search-index.json
 * Triggered by #desktopSearchBtn and #mobileSearchBtn in nav-footer.js
 */

(function () {
  'use strict';

  var FUSE_CDN = 'https://cdnjs.cloudflare.com/ajax/libs/fuse.js/7.0.0/fuse.min.js';
  var INDEX_URL = '/search-index.json';

  var _fuse       = null;
  var _index      = null;
  var _overlay    = null;
  var _input      = null;
  var _results    = null;
  var _fuseLoaded = false;

  // ── Inject overlay HTML + CSS ─────────────────────────────────────────
  function injectOverlay() {
    if (document.getElementById('sv-search-overlay')) return;

    var style = document.createElement('style');
    style.textContent = [
      '#sv-search-overlay{',
        'display:none;position:fixed;inset:0;z-index:9999;',
        'background:rgba(10,18,32,0.92);backdrop-filter:blur(6px);',
        'padding:80px 20px 40px;box-sizing:border-box;',
      '}',
      '#sv-search-overlay.sv-search-open{display:flex;flex-direction:column;align-items:center;}',
      '#sv-search-box{',
        'width:100%;max-width:680px;',
        'background:#fff;border-radius:16px;',
        'box-shadow:0 24px 64px rgba(0,0,0,0.4);',
        'overflow:hidden;',
      '}',
      '#sv-search-input-wrap{',
        'display:flex;align-items:center;gap:12px;',
        'padding:16px 20px;border-bottom:1px solid #e2e8f0;',
      '}',
      '#sv-search-input-wrap svg{flex-shrink:0;color:#94a3b8;}',
      '#sv-search-input{',
        'flex:1;border:none;outline:none;',
        'font-family:\'Montserrat\',sans-serif;font-size:17px;',
        'color:#0f172a;background:transparent;',
      '}',
      '#sv-search-input::placeholder{color:#94a3b8;}',
      '#sv-search-close{',
        'background:none;border:none;cursor:pointer;',
        'font-size:22px;color:#94a3b8;padding:0 4px;line-height:1;',
        'transition:color 0.2s;',
      '}',
      '#sv-search-close:hover{color:#0f172a;}',
      '#sv-search-results{',
        'max-height:480px;overflow-y:auto;padding:8px 0;',
      '}',
      '.sv-sr-item{',
        'display:flex;flex-direction:column;gap:2px;',
        'padding:12px 20px;text-decoration:none;',
        'border-bottom:1px solid #f1f5f9;transition:background 0.15s;',
      '}',
      '.sv-sr-item:last-child{border-bottom:none;}',
      '.sv-sr-item:hover{background:#f8fafc;}',
      '.sv-sr-section{',
        'font-size:10px;font-weight:700;text-transform:uppercase;',
        'letter-spacing:1px;color:#0056b3;margin-bottom:2px;',
      '}',
      '.sv-sr-title{',
        'font-family:\'Montserrat\',sans-serif;font-size:14px;',
        'font-weight:600;color:#0f172a;line-height:1.3;',
      '}',
      '.sv-sr-excerpt{',
        'font-size:12px;color:#64748b;line-height:1.5;margin-top:3px;',
      '}',
      '#sv-search-empty{',
        'padding:32px 20px;text-align:center;',
        'font-size:14px;color:#64748b;',
      '}',
      '#sv-search-hint{',
        'margin-top:16px;font-size:12px;color:#64748b;text-align:center;',
      '}',
      '@media(max-width:600px){',
        '#sv-search-overlay{padding:60px 12px 20px;}',
        '#sv-search-input{font-size:15px;}',
        '#sv-search-results{max-height:360px;}',
      '}',
    ].join('');
    document.head.appendChild(style);

    var html = [
      '<div id="sv-search-overlay" role="dialog" aria-modal="true" aria-label="Site search">',
        '<div id="sv-search-box">',
          '<div id="sv-search-input-wrap">',
            '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">',
              '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
            '</svg>',
            '<input id="sv-search-input" type="search" placeholder="Search Securevision…" autocomplete="off" spellcheck="false" aria-label="Search"/>',
            '<button id="sv-search-close" aria-label="Close search">✕</button>',
          '</div>',
          '<div id="sv-search-results" role="listbox"></div>',
        '</div>',
        '<p id="sv-search-hint">Press <kbd style="background:#e2e8f0;border-radius:4px;padding:2px 6px;font-size:11px;">Esc</kbd> to close</p>',
      '</div>',
    ].join('');

    var container = document.createElement('div');
    container.innerHTML = html;
    document.body.appendChild(container.firstChild);

    _overlay = document.getElementById('sv-search-overlay');
    _input   = document.getElementById('sv-search-input');
    _results = document.getElementById('sv-search-results');

    // Close handlers
    document.getElementById('sv-search-close').addEventListener('click', closeSearch);
    _overlay.addEventListener('click', function (e) {
      if (e.target === _overlay) closeSearch();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeSearch();
    });

    // Search on input
    _input.addEventListener('input', function () {
      runSearch(_input.value.trim());
    });
  }

  // ── Load Fuse.js from CDN ──────────────────────────────────────────────
  function loadFuse(callback) {
    if (_fuseLoaded) { callback(); return; }
    var s = document.createElement('script');
    s.src = FUSE_CDN;
    s.onload = function () { _fuseLoaded = true; callback(); };
    s.onerror = function () { console.warn('sv-search: Fuse.js failed to load'); };
    document.head.appendChild(s);
  }

  // ── Load search index ──────────────────────────────────────────────────
  function loadIndex(callback) {
    if (_index) { callback(); return; }
    fetch(INDEX_URL)
      .then(function (r) { return r.json(); })
      .then(function (data) {
        _index = data;
        _fuse = new Fuse(data, {
          keys: [
            { name: 'title',   weight: 0.6 },
            { name: 'excerpt', weight: 0.25 },
            { name: 'tags',    weight: 0.1 },
            { name: 'section', weight: 0.05 },
          ],
          threshold:        0.35,
          includeScore:     false,
          minMatchCharLen:  2,
          ignoreLocation:   true,
        });
        callback();
      })
      .catch(function (err) {
        console.warn('sv-search: could not load search-index.json', err);
      });
  }

  // ── Run search and render results ─────────────────────────────────────
  function runSearch(query) {
    if (!_fuse || !query) {
      _results.innerHTML = '';
      return;
    }

    var hits = _fuse.search(query, { limit: 10 });

    if (hits.length === 0) {
      _results.innerHTML = '<div id="sv-search-empty">No results for <strong>' + escHtml(query) + '</strong><br>Try a different keyword — CCTV, intercom, access control, LPR…</div>';
      return;
    }

    _results.innerHTML = hits.map(function (h) {
      var item = h.item;
      return [
        '<a class="sv-sr-item" href="' + item.url + '" role="option">',
          '<span class="sv-sr-section">' + escHtml(item.section) + '</span>',
          '<span class="sv-sr-title">'   + escHtml(item.title)   + '</span>',
          item.excerpt ? '<span class="sv-sr-excerpt">' + escHtml(item.excerpt) + '</span>' : '',
        '</a>',
      ].join('');
    }).join('');
  }

  // ── Open / close ──────────────────────────────────────────────────────
  function openSearch() {
    if (!_overlay) injectOverlay();
    loadFuse(function () {
      loadIndex(function () {
        _overlay.classList.add('sv-search-open');
        document.body.style.overflow = 'hidden';
        setTimeout(function () { _input.focus(); }, 50);
      });
    });
  }

  function closeSearch() {
    if (_overlay) _overlay.classList.remove('sv-search-open');
    document.body.style.overflow = '';
    if (_input) { _input.value = ''; _results.innerHTML = ''; }
  }

  // ── Wire to nav buttons once DOM is ready ─────────────────────────────
  function wireButtons() {
    var ids = ['desktopSearchBtn', 'mobileSearchBtn'];
    ids.forEach(function (id) {
      var btn = document.getElementById(id);
      if (btn) {
        btn.removeAttribute('onclick');
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          openSearch();
        });
      }
    });
  }

  function escHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // Run after nav-footer.js has injected the nav buttons
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wireButtons);
  } else {
    wireButtons();
  }

  // Also wire after a short delay in case nav-footer.js is slow
  setTimeout(wireButtons, 300);

})();
