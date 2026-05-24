import os, re

root = r'c:\Projects\SV-Build\portfolio\condominiums'
files = [f for f in os.listdir(root) if f.endswith('.html')]

broken_list = ['prop-condo.webp', 'prop-commercial.webp', 'portfolio-delias.webp', 
               'portfolio-scape.webp', 'de-elias-hero.webp', 'trilliant-hero.webp', 
               'sengkang-interim-thumb.webp', 'surya-home-thumb.webp', 'smartflex-thumb.webp']

files_updated = 0

for file in files:
    path = os.path.join(root, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    # We will iterate over all <a> tags that contain <img> tags
    # We use a non-greedy regex to match <a>...</a>
    # Wait, <a> tags can contain a lot of stuff. It's safer to find all <img> tags first.
    # Actually, we can use a simpler approach: find all occurrences of the broken images
    # and replace them directly.
    
    # But wait! We wanted to map prop-condo.webp based on the <a> href.
    # Let's find all <a>...</a> blocks.
    
    def replacer(match):
        a_block = match.group(0)
        
        # Does it contain a broken image?
        if not any(b in a_block for b in broken_list):
            return a_block
            
        # Find href
        href_match = re.search(r'href=[\'"]([^\'"]+)[\'"]', a_block)
        if not href_match: return a_block
        href = href_match.group(1)
        
        # Find src
        src_match = re.search(r'src=[\'"]([^\'"]+)[\'"]', a_block)
        if not src_match: return a_block
        src = src_match.group(1)
        
        if not any(b in src for b in broken_list):
            return a_block
            
        new_src = src
        
        if 'suites-cairnhill' in href:
            new_src = '/images/portfolio/condominiums/suites-cairnhill-rel.webp'
        elif 'clearwater' in href:
            new_src = '/images/portfolio/condominiums/the-clearwater-rel.webp'
        elif 'catholic-centre' in href:
            new_src = '/images/portfolio/commercial/catholic-centre-rel.webp'
        elif 'd-elias' in href:
            new_src = '/images/portfolio/condominiums/d-elias-rel.webp'
        elif 'hillview-park' in href:
            new_src = '/images/portfolio/condominiums/hillview-park-condo-rel.webp'
        elif 'scape' in href:
            new_src = '/images/portfolio/commercial/scape-building-profile.webp'
        elif 'surya-home' in href:
            new_src = '/images/portfolio/healthcare/sunlove-rel.webp'
        elif 'smartflex' in href:
            new_src = '/images/portfolio/industrial/smartflex-at-tampines-rel.webp'
        elif 'sengkang' in href:
            new_src = '/images/portfolio/institutions/changi-airside-rel.webp'
        elif href == '/' or href == '/portfolio/':
            if 'All Condominiums' in a_block:
                new_src = '/images/solutions/hero-solutions/condominium-estate-security-singapore-rel.webp'
            elif 'The Clearwater' in a_block:
                new_src = '/images/portfolio/condominiums/the-clearwater-rel.webp'
            else:
                new_src = '/images/portfolio/condominiums/country-grandeur-rel.webp'
                
        if new_src == src:
            if 'trilliant' in src:
                new_src = '/images/portfolio/condominiums/hillview-park-condo-rel.webp'
            elif 'delias' in src or 'de-elias' in src:
                new_src = '/images/portfolio/condominiums/d-elias-rel.webp'
            elif 'scape' in src:
                new_src = '/images/portfolio/commercial/scape-building-profile.webp'
            elif 'sengkang' in src:
                new_src = '/images/portfolio/institutions/changi-airside-rel.webp'
            elif 'surya' in src:
                new_src = '/images/portfolio/healthcare/sunlove-rel.webp'
            elif 'smartflex' in src:
                new_src = '/images/portfolio/industrial/smartflex-at-tampines-rel.webp'
                
        # Replace the src
        new_a_block = a_block.replace(src, new_src)
        return new_a_block

    new_content = re.sub(r'<a\b[^>]*>(?:(?!</a>).)*?</a>', replacer, content, flags=re.DOTALL)
    
    if new_content != original_content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        files_updated += 1
        print(f"Updated {file}")

print(f"Total files updated: {files_updated}")
