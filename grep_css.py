import os
import re

for dp, dn, files in os.walk('.'):
    for f in files:
        if f.endswith('.css'):
            path = os.path.join(dp, f)
            with open(path, encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
                if re.search(r'content:\s*[\'"]Artistic Impression[\'"]', content, re.IGNORECASE):
                    print(f"Found in {path}")
