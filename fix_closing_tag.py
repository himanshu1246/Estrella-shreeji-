import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the closing tag from </a> to </button>
html = re.sub(
    r'(<button class="btn btn-dark btn-cta mt-3"[^>]*>\s*View Master Plan Layout\s*)</a>',
    r'\1</button>',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
