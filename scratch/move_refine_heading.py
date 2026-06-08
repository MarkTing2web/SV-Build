import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# The heading to remove
heading = '<p style="font-size: 0.9rem; color: #64748b; margin-bottom: 24px;">Refine project case studies by property type, system, or year:</p>'

# Create the wrapper
wrapper = f"""<div class="container" style="padding-top: 32px; padding-bottom: 16px;">
    {heading}
</div>
"""

# Replace the heading inside the file with nothing first
# We should only remove it from inside the filter-section
# Let's find filter-section
start = content.find('class="filter-section"')
if start != -1:
    section_start = content.rfind('<section', 0, start)
    section_end = content.find('</section>', section_start)
    
    if section_end != -1:
        # Extract the section text
        section_text = content[section_start:section_end]
        
        # Remove the heading from the section text
        # Also remove any whitespace before it
        section_text_new = re.sub(r'\s*<p style="font-size: 0.9rem; color: #64748b; margin-bottom: 24px;">Refine project case studies by property type, system, or year:</p>', '', section_text)
        
        # Insert the wrapper before the section
        new_content = content[:section_start] + wrapper + section_text_new + content[section_end:]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Success")
    else:
        print("Failed to find section end")
else:
    print("Failed to find section start")
