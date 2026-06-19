import re

# Fix spelling mistake
for filename in ['index.html', 'privacy-policy.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('Terms of Conditions', 'Terms and Conditions')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
