import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the old basic interceptor
html = re.sub(r'<script>\s*// Intercept all WhatsApp link clicks globally.*?</script>', '', html, flags=re.DOTALL)

# Add the robust interceptor that handles Shadow DOM and window.open overrides
robust_interceptor = r"""
<script>
// Robust WhatsApp Link Interceptor for Chatbots & Shadow DOM
(function() {
    // 1. Override window.open
    var originalWindowOpen = window.open;
    window.open = function(url, windowName, windowFeatures) {
        if (typeof url === 'string' && url.toLowerCase().includes('api.whatsapp.com/send')) {
            url = url.replace(/phone=\d+/, 'phone=919075060900');
        }
        return originalWindowOpen(url, windowName, windowFeatures);
    };

    // 2. Intercept all clicks (including Shadow DOM via composedPath)
    document.addEventListener('click', function(e) {
        var path = e.composedPath ? e.composedPath() : (e.path || [e.target]);
        for (var i = 0; i < path.length; i++) {
            var el = path[i];
            if (el && el.tagName && el.tagName.toLowerCase() === 'a' && el.href) {
                if (el.href.toLowerCase().includes('api.whatsapp.com/send')) {
                    el.href = el.href.replace(/phone=\d+/, 'phone=919075060900');
                }
                break;
            }
        }
    }, true);
})();
</script>
"""

if "Robust WhatsApp Link Interceptor" not in html:
    html = html.replace('</body>', robust_interceptor + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
