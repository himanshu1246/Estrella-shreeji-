import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the Cloudflare anti-bot challenge script which causes the redirect
html = re.sub(r'<script[^>]*>(?:(?!</script>).)*cdn-cgi(?:(?!</script>).)*</script>', '', html, flags=re.DOTALL | re.IGNORECASE)

# 2. Replace all remaining URLs pointing to the old scraped domain with relative paths
html = html.replace('https://bellevuemahalaxmis.com/Lodha-4bhk/', './')
html = html.replace('https://bellevuemahalaxmis.com/', './')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
