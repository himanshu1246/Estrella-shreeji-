import os

for dp, dn, files in os.walk('.'):
    for f in files:
        if f.endswith('.css') or f.endswith('.js') or f.endswith('.html'):
            try:
                content = open(os.path.join(dp, f), 'r', encoding='utf-8').read()
                if 'artistic' in content.lower():
                    print(f"Found in: {f}")
            except:
                pass
