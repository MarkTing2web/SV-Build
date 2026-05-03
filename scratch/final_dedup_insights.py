import os
import re

def deduplicate_content(content):
    # 1. Fix multiple "Meet the Author" in TOC
    content = re.sub(r'(<li><a href="#author">Meet the Author</a></li>\s*)+', r'<li><a href="#author">Meet the Author</a></li>\n', content)
    
    # 2. Fix multiple horizontal rules
    content = re.sub(r'(<hr>\s*)+', r'<hr>\n', content)
    
    # 3. Fix multiple Author Bio blocks
    author_bio_pattern = re.compile(r'(<section id="author" class="author-bio-footer">.*?</section>\s*)+', re.DOTALL)
    content = author_bio_pattern.sub(lambda m: m.group(0).split('</section>')[0] + '</section>\n', content)

    # 4. Fix multiple tag blocks
    tags_pattern = re.compile(r'(<div class="article-tags">.*?</div>\s*)+', re.DOTALL)
    content = tags_pattern.sub(lambda m: m.group(0).split('</div>')[0] + '</div>\n', content)

    # 5. Fix multiple nav blocks
    nav_pattern = re.compile(r'(<nav class="prev-next-nav".*?</nav>\s*)+', re.DOTALL)
    content = nav_pattern.sub(lambda m: m.group(0).split('</nav>')[0] + '</nav>\n', content)

    # 6. Remove multiple identical comment headers
    content = re.sub(r'(<!-- ═══ ARTICLE FOOTER ELEMENTS .*? ═══ -->\s*)+', r'\1', content)
    
    return content

root_dir = r'c:\Projects\SV-Build\insights'
for file in os.listdir(root_dir):
    if file.endswith('.html'):
        file_path = os.path.join(root_dir, file)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        new_content = deduplicate_content(content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"De-duplicated: {file}")
