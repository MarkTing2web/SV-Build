import os, re
root = r'c:\Projects\SV-Build\portfolio\condominiums'
files = [f for f in os.listdir(root) if f.endswith('.html')]
with open(r'c:\Projects\SV-Build\scratch\out_a.txt', 'w', encoding='utf-8') as f:
    for file in files:
        content = open(os.path.join(root, file), encoding='utf-8').read()
        matches = re.finditer(r'(<a[^>]*>.*?<img[^>]*src=[\'"]([^\'"]+)[\'"].*?</a>)', content, re.DOTALL)
        for m in matches:
            img = m.group(2)
            if any(x in img for x in ['prop-condo', 'prop-commercial', 'sengkang', 'surya', 'smartflex', 'delias', 'scape', 'trilliant', 'de-elias']):
                f.write(f"[{file}]\n{m.group(1)}\n\n")
