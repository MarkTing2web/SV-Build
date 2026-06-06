import os
import re

w = r"c:\Projects\SV-Build"

files = [
    "portfolio/industrial/sta-compliance-imaging.html",
    "portfolio/commercial/scape-commercial.html",
    "portfolio/commercial/scape-smart-booking-access.html"
]

overlay_css = """
  .portfolio-hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(105deg, rgba(14,26,43,0.72) 0%, rgba(14,26,43,0.45) 60%, rgba(14,26,43,0.3) 100%);
    z-index: 1;
  }"""

for file in files:
    path = os.path.join(w, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure position: relative is in .portfolio-hero
    # Some might have it already, some might not.
    # The canonical css looks like:
    # .portfolio-hero { background-image: url('...'); }
    # So we replace `.portfolio-hero { background-image:` with `.portfolio-hero { position: relative; background-image:`
    # If it already has position: relative, we shouldn't add it again.
    
    # Let's do a simple regex for adding position: relative;
    def add_relative(match):
        inner = match.group(1)
        if 'position: relative' not in inner:
            return f".portfolio-hero {{{inner} position: relative; }}"
        return match.group(0)

    # First add position: relative
    content = re.sub(r'\.portfolio-hero\s*\{([^}]+)\}', add_relative, content)
    
    # For sta-compliance-imaging.html, it already has an old .portfolio-hero::before, let's remove it if it exists
    # It looks like: .portfolio-hero::before { ... }
    content = re.sub(r'\.portfolio-hero::before\s*\{[^}]+\}', '', content, flags=re.DOTALL)
    
    # We want to add overlay_css right after `.portfolio-hero { ... }` or before `</style>`
    # The safest is to add it just before </style> to ensure it applies.
    content = content.replace("</style>", overlay_css + "\n</style>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Task A completed.")
