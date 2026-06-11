import re

with open(r'd:\Ler Wee Meng\Project-Web\SV-Build\insights\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_filter_block = """<div class="filter-container">
<button class="filter-btn active" data-filter="all">All Articles</button>
<button class="filter-btn" data-filter="Security-Planning">Security Planning</button>
<button class="filter-btn" data-filter="Technology-AI">Technology &amp; AI</button>
<button class="filter-btn" data-filter="Singapore-Industry">Singapore Industry</button>
</div>"""

new_filter_block = """<div class="insights-filters" id="insightsFilters">
  <button class="filter-btn active" data-category="all">All Insights</button>
  <button class="filter-btn" data-category="alarm-intrusion">Alarm &amp; Intrusion</button>
  <button class="filter-btn" data-category="cctv-surveillance">CCTV &amp; Surveillance</button>
  <button class="filter-btn" data-category="access-intercom">Access &amp; Intercom</button>
  <button class="filter-btn" data-category="vehicle-gates">Vehicle &amp; Gates</button>
  <button class="filter-btn" data-category="ip-telephony-network">IP Telephony &amp; Network</button>
  <button class="filter-btn" data-category="platform-integration">Platform &amp; Integration</button>
  <button class="filter-btn" data-category="security-planning">Security Planning</button>
</div>"""

content = content.replace(old_filter_block, new_filter_block)

old_js_block = """// Filter Logic
const filterBtns = document.querySelectorAll('.filter-btn');
const systemTiles = document.querySelectorAll('.system-tile');
const articleCards = document.querySelectorAll('.article-card');

function filterArticles(filterVal, isSystem = false) {
    articleCards.forEach(card => {
        const cat = card.dataset.category;
        const sys = card.dataset.system;
        
        if (filterVal === 'all') {
            card.classList.remove('hidden');
        } else if (isSystem) {
            if (sys === filterVal) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        } else {
            if (cat === filterVal) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        }
    });
}

filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterArticles(btn.dataset.filter);
    });
});

systemTiles.forEach(tile => {
    tile.addEventListener('click', (e) => {
        e.preventDefault();
        const sys = tile.dataset.system;
        // Scroll to grid
        document.getElementById('articlesGrid').scrollIntoView({ behavior: 'smooth' });
        // Set main filter to 'all' to avoid confusion
        filterBtns.forEach(b => b.classList.remove('active'));
        document.querySelector('.filter-btn[data-filter="all"]').classList.add('active');
        // Apply system filter
        filterArticles(sys, true);
    });
});"""

new_js_block = """// Filter Logic
const filterBtns = document.querySelectorAll('.filter-btn');
const systemTiles = document.querySelectorAll('.system-tile');
const articleCards = document.querySelectorAll('.article-card');

function filterArticles(filterVal, isSystem = false) {
    articleCards.forEach(card => {
        let rawCat = card.dataset.category;
        if (!rawCat) {
            const catEl = card.querySelector('.ac-cat');
            if (catEl) rawCat = catEl.textContent;
        }
        rawCat = rawCat || "";
        
        const catSlug = rawCat.toLowerCase().replace(/ & /g, '-').replace(/&/g, '').replace(/\\s+/g, '-');
        const sys = card.dataset.system;
        
        if (filterVal === 'all') {
            card.classList.remove('hidden');
        } else if (isSystem) {
            if (sys === filterVal) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        } else {
            if (catSlug === filterVal) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        }
    });
}

filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        filterArticles(btn.dataset.category);
    });
});

systemTiles.forEach(tile => {
    tile.addEventListener('click', (e) => {
        e.preventDefault();
        const sys = tile.dataset.system;
        // Scroll to grid
        document.getElementById('articlesGrid').scrollIntoView({ behavior: 'smooth' });
        // Set main filter to 'all' to avoid confusion
        filterBtns.forEach(b => b.classList.remove('active'));
        document.querySelector('.filter-btn[data-category="all"]').classList.add('active');
        // Apply system filter
        filterArticles(sys, true);
    });
});"""

content = content.replace(old_js_block, new_js_block)

with open(r'd:\Ler Wee Meng\Project-Web\SV-Build\insights\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done replacing content in insights/index.html")
