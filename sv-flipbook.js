/*!
 * Securevision Flipbook — self-hosted, dependency-free page-turn viewer.
 * Markup:  <section class="fb" data-fb='{"base":"/images/brochures/x/","count":8,"ratio":0.7071,"title":"…","alts":[…],"pdf":"/…pdf"}'></section>
 * Images:  {base}pNN-sm.webp (700w), pNN-lg.webp (1400w), pNN-th.webp (thumb)
 * Desktop: two-page spread with 3D page turn.  Mobile / narrow: single page.
 */
(function () {
  'use strict';

  var ICON = {
    prev: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>',
    next: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>',
    zoomIn: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3M11 8v6M8 11h6"/></svg>',
    zoomOut: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3M8 11h6"/></svg>',
    full: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>',
    exit: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 4v5H4M15 4v5h5M9 20v-5H4M15 20v-5h5"/></svg>',
    dl: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 11l5 5 5-5M5 20h14"/></svg>'
  };

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }
  function pad2(n) { return n < 10 ? '0' + n : '' + n; }

  function Flipbook(root) {
    var cfg;
    try { cfg = JSON.parse(root.getAttribute('data-fb')); } catch (e) { return; }
    var N = cfg.count, ratio = cfg.ratio || 0.7071;
    var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* ---------- DOM ---------- */
    root.innerHTML = '';
    root.classList.add('fb-ready');
    var vp = el('div', 'fb-vp');
    vp.tabIndex = 0;
    vp.setAttribute('role', 'group');
    vp.setAttribute('aria-roledescription', 'flipbook');
    vp.setAttribute('aria-label', (cfg.title || 'Brochure') + ' — use the left and right arrow keys to turn pages');
    var stage = el('div', 'fb-stage');
    var book = el('div', 'fb-book');
    stage.appendChild(book);
    vp.appendChild(stage);
    var arrowL = el('button', 'fb-arrow fb-arrow-l', ICON.prev);
    arrowL.type = 'button'; arrowL.setAttribute('aria-label', 'Previous page');
    var arrowR = el('button', 'fb-arrow fb-arrow-r', ICON.next);
    arrowR.type = 'button'; arrowR.setAttribute('aria-label', 'Next page');
    var hint = el('div', 'fb-hint', 'Click a page, swipe, or use ← → to turn');
    vp.appendChild(arrowL); vp.appendChild(arrowR); vp.appendChild(hint);

    var bar = el('div', 'fb-bar');
    var bPrev = btn('Previous page', ICON.prev, 'fb-btn');
    var counter = el('span', 'fb-count');
    counter.setAttribute('aria-live', 'polite');
    var bNext = btn('Next page', ICON.next, 'fb-btn');
    var nav = el('div', 'fb-nav'); nav.appendChild(bPrev); nav.appendChild(counter); nav.appendChild(bNext);
    var tools = el('div', 'fb-tools');
    var bZoom = btn('Zoom in', ICON.zoomIn, 'fb-btn');
    var bFull = btn('Full screen', ICON.full, 'fb-btn');
    tools.appendChild(bZoom); tools.appendChild(bFull);
    if (cfg.pdf) {
      var dl = el('a', 'fb-btn fb-dl', ICON.dl + '<span>PDF</span>');
      dl.href = cfg.pdf; dl.setAttribute('download', ''); dl.setAttribute('aria-label', 'Download PDF');
      tools.appendChild(dl);
    }
    bar.appendChild(nav); bar.appendChild(tools);

    var strip = el('div', 'fb-thumbs');
    strip.setAttribute('role', 'list');
    var thumbBtns = [];
    for (var i = 1; i <= N; i++) {
      var t = el('button', 'fb-thumb');
      t.type = 'button'; t.setAttribute('role', 'listitem');
      t.setAttribute('aria-label', 'Go to page ' + i);
      var ti = new Image();
      ti.src = cfg.base + 'p' + pad2(i) + '-th.webp'; ti.alt = ''; ti.loading = 'lazy'; ti.decoding = 'async';
      ti.width = 80; ti.height = Math.round(80 / ratio);
      t.appendChild(ti);
      t.appendChild(el('span', 'fb-thumb-n', '' + i));
      (function (n) { t.addEventListener('click', function () { goToPage(n); vp.focus({ preventScroll: true }); }); })(i);
      strip.appendChild(t); thumbBtns.push(t);
    }
    root.appendChild(vp); root.appendChild(bar); root.appendChild(strip);

    function btn(label, html, cls) {
      var b = el('button', cls, html);
      b.type = 'button'; b.setAttribute('aria-label', label); b.title = label;
      return b;
    }

    /* ---------- State ---------- */
    var mode = null, per = 2, L = 0, cur = 0, leaves = [], zoom = 1, pw = 0, ph = 0, token = 0, hinted = true, touched = false;

    function maxCur() { return per === 2 ? (N % 2 === 0 ? L : L - 1) : N - 1; }
    function leftPage() { return per === 2 ? (cur === 0 ? 1 : 2 * cur) : cur + 1; }

    function srcsetFor(n) {
      return cfg.base + 'p' + pad2(n) + '-sm.webp 700w, ' + cfg.base + 'p' + pad2(n) + '-lg.webp 1400w';
    }
    function face(cls, n) {
      var f = el('div', 'fb-face ' + cls);
      if (n <= N) {
        var img = new Image();
        img.alt = (cfg.alts && cfg.alts[n - 1]) || ((cfg.title || 'Page') + ' — page ' + n + ' of ' + N);
        img.decoding = 'async'; img.draggable = false;
        img.setAttribute('data-p', n);
        f.appendChild(img);
      } else {
        f.classList.add('fb-blank');
      }
      return f;
    }

    function build() {
      book.innerHTML = ''; leaves = [];
      per = mode === 'spread' ? 2 : 1;
      L = Math.ceil(N / per);
      for (var k = 0; k < L; k++) {
        var lf = el('div', 'fb-leaf');
        lf.appendChild(face('fb-front', k * per + 1));
        if (per === 2) lf.appendChild(face('fb-back', k * per + 2));
        book.appendChild(lf); leaves.push(lf);
      }
      root.classList.toggle('fb-single', mode === 'single');
    }

    function sizes() {
      var full = root.classList.contains('fb-full');
      var padPx = full ? 14 : (mode === 'single' ? 10 : 22);
      var availW = Math.max(200, vp.clientWidth - padPx * 2);
      var maxH = full ? Math.max(240, vp.clientHeight - padPx * 2) : Math.min(window.innerHeight * 0.82, 980);
      var pw0 = mode === 'spread' ? Math.min(availW / 2, maxH * ratio) : Math.min(availW, maxH * ratio);
      if (!full) vp.style.height = Math.round(pw0 / ratio + padPx * 2) + 'px'; else vp.style.height = '';
      pw = pw0 * zoom; ph = pw / ratio;
      book.style.setProperty('--pw', pw.toFixed(1) + 'px');
      book.style.setProperty('--ph', ph.toFixed(1) + 'px');
      book.style.setProperty('--leafx', (per === 2 ? pw : 0).toFixed(1) + 'px');
      book.style.width = (per === 2 ? pw * 2 : pw).toFixed(1) + 'px';
      book.style.height = ph.toFixed(1) + 'px';
      var s = Math.round(pw) + 'px';
      var imgs = book.querySelectorAll('img');
      for (var i = 0; i < imgs.length; i++) imgs[i].sizes = s;
    }

    function shiftX() {
      if (per !== 2 || zoom > 1) return 0;
      if (cur === 0) return -pw / 2;
      if (N % 2 === 0 && cur === L) return pw / 2;
      return 0;
    }

    function zFinal(k) { return k < cur ? k + 1 : L - k; }

    function applyState(animateFrom) {
      var t = ++token;
      var lo = animateFrom == null ? -1 : Math.min(animateFrom, cur);
      var hi = animateFrom == null ? -1 : Math.max(animateFrom, cur);
      for (var k = 0; k < L; k++) {
        var lf = leaves[k];
        var moving = animateFrom != null && k >= lo && k < hi;
        if (moving) {
          lf.style.zIndex = 1000 + (animateFrom < cur ? k : L - k);
          var order = animateFrom < cur ? k - lo : hi - 1 - k;
          lf.style.transitionDelay = reduced ? '0s' : Math.min(order, 6) * 70 + 'ms';
        } else {
          lf.style.transitionDelay = '0s';
          lf.style.zIndex = zFinal(k);
        }
        lf.classList.toggle('is-flipped', k < cur);
        lf.classList.toggle('is-top', k === cur || k === cur - 1);
      }
      book.style.transform = 'translateX(' + shiftX().toFixed(1) + 'px)';
      if (animateFrom != null) {
        setTimeout(function () {
          if (t !== token) return;
          for (var j = 0; j < L; j++) { leaves[j].style.zIndex = zFinal(j); leaves[j].style.transitionDelay = '0s'; }
        }, reduced ? 50 : 1100 + Math.min(Math.abs(cur - animateFrom), 7) * 70);
      }
      updateUI();
      loadAround();
    }

    function visiblePages() {
      if (per === 1) return [cur + 1];
      if (cur === 0) return [1];
      if (N % 2 === 0 && cur === L) return [N];
      return [2 * cur, 2 * cur + 1];
    }

    function updateUI() {
      var v = visiblePages();
      counter.textContent = (v.length === 2 ? 'Pages ' + v[0] + '–' + v[1] : 'Page ' + v[0]) + ' of ' + N;
      bPrev.disabled = arrowL.disabled = cur <= 0;
      bNext.disabled = arrowR.disabled = cur >= maxCur();
      for (var i = 0; i < thumbBtns.length; i++) {
        var on = v.indexOf(i + 1) !== -1;
        thumbBtns[i].classList.toggle('is-on', on);
        if (on) thumbBtns[i].setAttribute('aria-current', 'true'); else thumbBtns[i].removeAttribute('aria-current');
      }
      var first = thumbBtns[v[0] - 1];
      if (first && strip.scrollWidth > strip.clientWidth) {
        strip.scrollTo({ left: first.offsetLeft - strip.clientWidth / 2 + first.offsetWidth / 2, behavior: reduced ? 'auto' : 'smooth' });
      }
      if (touched) { try { history.replaceState(null, '', '#page=' + v[0]); } catch (e) { /* ignore */ } }
    }

    function loadAround() {
      var lp = leftPage();
      var imgs = book.querySelectorAll('img');
      for (var i = 0; i < imgs.length; i++) {
        var p = +imgs[i].getAttribute('data-p');
        if (!imgs[i].getAttribute('srcset') && p >= lp - 3 && p <= lp + 5) {
          imgs[i].setAttribute('srcset', srcsetFor(p));
          imgs[i].src = cfg.base + 'p' + pad2(p) + '-lg.webp';
        }
      }
    }

    /* ---------- Navigation ---------- */
    function setCur(n) {
      n = Math.max(0, Math.min(maxCur(), n));
      if (n === cur) return;
      var from = cur; cur = n;
      touched = true;
      hideHint();
      applyState(from);
    }
    function next() { setCur(cur + 1); }
    function prev() { setCur(cur - 1); }
    function goToPage(p) {
      p = Math.max(1, Math.min(N, p));
      setCur(per === 2 ? Math.floor(p / 2) : p - 1);
    }

    function hideHint() {
      if (hinted) return; hinted = true; hint.classList.remove('is-on');
    }

    /* ---------- Layout / mode ---------- */
    function pickMode() {
      var w = vp.clientWidth;
      var full = root.classList.contains('fb-full');
      var h = full ? vp.clientHeight : Math.min(window.innerHeight * 0.82, 980);
      return (w >= 760 && h >= 420) ? 'spread' : 'single';
    }

    function layout(forceRebuild) {
      var m = pickMode();
      if (m !== mode || forceRebuild) {
        var keep = mode ? leftPage() : null;
        mode = m;
        per = mode === 'spread' ? 2 : 1;
        build();
        var startPage = keep != null ? keep : initialPage;
        cur = per === 2 ? Math.floor(startPage / 2) : startPage - 1;
        cur = Math.max(0, Math.min(maxCur(), cur));
        sizes();
        root.classList.add('fb-noanim');
        applyState(null);
        void book.offsetWidth;
        root.classList.remove('fb-noanim');
      } else {
        sizes();
        root.classList.add('fb-noanim');
        book.style.transform = 'translateX(' + shiftX().toFixed(1) + 'px)';
        void book.offsetWidth;
        root.classList.remove('fb-noanim');
      }
    }

    var initialPage = 1;
    var mh = /page=(\d+)/.exec(location.hash || '');
    if (mh) initialPage = Math.max(1, Math.min(N, +mh[1]));

    /* ---------- Zoom / fullscreen ---------- */
    function setZoom(z) {
      zoom = z;
      vp.classList.toggle('is-zoomed', zoom > 1);
      bZoom.innerHTML = zoom > 1 ? ICON.zoomOut : ICON.zoomIn;
      var lbl = zoom > 1 ? 'Zoom out' : 'Zoom in';
      bZoom.setAttribute('aria-label', lbl); bZoom.title = lbl;
      layout(false);
      vp.scrollLeft = (vp.scrollWidth - vp.clientWidth) / 2;
      vp.scrollTop = (vp.scrollHeight - vp.clientHeight) / 2;
    }
    function setFull(on) {
      root.classList.toggle('fb-full', on);
      document.documentElement.classList.toggle('fb-lock', on);
      bFull.innerHTML = on ? ICON.exit : ICON.full;
      var lbl = on ? 'Exit full screen' : 'Full screen';
      bFull.setAttribute('aria-label', lbl); bFull.title = lbl;
      if (zoom > 1) { zoom = 1; vp.classList.remove('is-zoomed'); bZoom.innerHTML = ICON.zoomIn; }
      layout(false);
      if (!on) { window.scrollTo(window.scrollX, root.getBoundingClientRect().top + window.scrollY - 80); }
      vp.focus({ preventScroll: true });
    }

    /* ---------- Events ---------- */
    bNext.addEventListener('click', next); bPrev.addEventListener('click', prev);
    arrowR.addEventListener('click', function (e) { e.stopPropagation(); next(); });
    arrowL.addEventListener('click', function (e) { e.stopPropagation(); prev(); });
    bZoom.addEventListener('click', function () { setZoom(zoom > 1 ? 1 : 2); });
    bFull.addEventListener('click', function () { setFull(!root.classList.contains('fb-full')); });

    vp.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight' || e.key === 'PageDown') { e.preventDefault(); next(); }
      else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); prev(); }
      else if (e.key === 'Home') { e.preventDefault(); setCur(0); }
      else if (e.key === 'End') { e.preventDefault(); setCur(maxCur()); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && root.classList.contains('fb-full')) setFull(false);
    });

    var sx = 0, sy = 0, tracking = false, panning = false, panX = 0, panY = 0, ptype = 'mouse';
    vp.addEventListener('pointerdown', function (e) {
      if (e.target.closest('.fb-arrow')) return;
      tracking = true; sx = e.clientX; sy = e.clientY; ptype = e.pointerType;
      if (zoom > 1 && e.pointerType === 'mouse') { panning = true; panX = vp.scrollLeft; panY = vp.scrollTop; vp.classList.add('is-panning'); }
    });
    vp.addEventListener('pointermove', function (e) {
      if (panning) { vp.scrollLeft = panX - (e.clientX - sx); vp.scrollTop = panY - (e.clientY - sy); return; }
      if (e.pointerType === 'mouse' && zoom === 1 && per === 2) {
        var r = vp.getBoundingClientRect();
        var left = e.clientX < r.left + r.width / 2;
        vp.style.cursor = left ? (cur > 0 ? 'w-resize' : 'default') : (cur < maxCur() ? 'e-resize' : 'default');
      }
    });
    function endPointer(e, cancelled) {
      if (!tracking) return;
      tracking = false;
      if (panning) { panning = false; vp.classList.remove('is-panning'); return; }
      if (cancelled || zoom > 1) return;
      var dx = e.clientX - sx, dy = e.clientY - sy;
      if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy) * 1.3) { dx < 0 ? next() : prev(); return; }
      if (Math.abs(dx) < 8 && Math.abs(dy) < 8 && !e.target.closest('.fb-arrow')) {
        var r = vp.getBoundingClientRect();
        var goPrev = per === 2 ? (e.clientX < r.left + r.width / 2) : (e.clientX < r.left + r.width * 0.33);
        goPrev ? prev() : next();
      }
    }
    vp.addEventListener('pointerup', function (e) { endPointer(e, false); });
    vp.addEventListener('pointercancel', function (e) { endPointer(e, true); });
    vp.addEventListener('pointerleave', function () { if (panning) { panning = false; vp.classList.remove('is-panning'); } tracking = false; });

    var rafId = 0, lastW = 0, lastH = 0;
    function onResize() {
      if (rafId) return;
      rafId = requestAnimationFrame(function () {
        rafId = 0;
        if (vp.clientWidth === lastW && window.innerHeight === lastH) return;
        lastW = vp.clientWidth; lastH = window.innerHeight;
        layout(false);
      });
    }
    window.addEventListener('resize', onResize);
    window.addEventListener('orientationchange', onResize);
    window.addEventListener('hashchange', function () {
      var m2 = /page=(\d+)/.exec(location.hash || '');
      if (m2) goToPage(+m2[1]);
    });

    /* ---------- Go ---------- */
    lastW = vp.clientWidth; lastH = window.innerHeight;
    layout(true);
    hinted = false;
    hint.classList.add('is-on');
    setTimeout(hideHint, 7000);
    root.setAttribute('data-fb-mode', mode);
  }

  function init() {
    var nodes = document.querySelectorAll('[data-fb]');
    for (var i = 0; i < nodes.length; i++) Flipbook(nodes[i]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
