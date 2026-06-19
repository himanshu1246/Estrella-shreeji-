import re

# 1. Fix privacy-policy.html layout
with open('privacy-policy.html', 'r', encoding='utf-8') as f:
    pp_html = f.read()
pp_html = pp_html.replace('</head>', '<style>.lp-layout{display:block !important;}</style></head>')
with open('privacy-policy.html', 'w', encoding='utf-8') as f:
    f.write(pp_html)

# 2. Update form actions in index.html to go to thank-you.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()
index_html = index_html.replace('action="./server.php"', 'action="./thank-you.html"')
index_html = index_html.replace('method="post"', 'method="get"')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# 3. Create thank-you.html using header and footer
header_match = re.search(r'([\s\S]*?</nav>)', index_html)
header = header_match.group(1) if header_match else ''
header = header.replace('isThanksPage = false;', 'isThanksPage = true;')
header = header.replace('</head>', '<style>.lp-layout{display:block !important;}</style></head>')

footer_match = re.search(r'(<footer[\s\S]*)', index_html)
footer = footer_match.group(1) if footer_match else ''

thank_you_content = """
<div class="container py-5 mt-5 text-center" style="min-height: 50vh;">
    <h1 class="mb-4" style="color: #cda857;">Thank You!</h1>
    <h3 class="mb-4">Your enquiry has been successfully submitted.</h3>
    <p>Our team will get back to you shortly with the requested information.</p>
    <a href="index.html" class="btn btn-dark btn-cta mt-4">Return to Home</a>
</div>
"""

with open('thank-you.html', 'w', encoding='utf-8') as f:
    f.write(header + thank_you_content + footer)
