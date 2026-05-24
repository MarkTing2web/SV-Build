import os

portfolio_dir = r"c:\Projects\SV-Build\images\portfolio"
for root, dirs, files in os.walk(portfolio_dir):
    for f in files:
        if "-rel" in f:
            full_path = os.path.join(root, f)
            rel_path = full_path.replace("\\", "/").replace("c:/Projects/SV-Build", "")
            print(rel_path)
