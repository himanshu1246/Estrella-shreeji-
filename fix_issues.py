import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the stray literal \n at the start of body
# The stray \n is actually `<p>\n\n</p>` which I saw earlier
html = re.sub(r'<p>\s*\\n\s*</p>', '', html)
html = re.sub(r'<p>\s*\n\s*</p>', '', html) # Just in case

# Fix the stray literal \n at the top of the screen:
# The user's screenshot literally shows \n at the very top. 
# Let me replace any literal '\n' string at the start of the body.
html = re.sub(r'<body>\s*\\n', '<body>', html)

# Task 2: Replace Favicon
# Currently: <link href="./img/comman/favicon.svg" rel="icon" sizes="16x16"/>
# I will replace it with: 
# <link href="./asset/favicon.ico" rel="icon" type="image/x-icon"/>
# <link rel="apple-touch-icon" sizes="180x180" href="./asset/apple-touch-icon.png">
# <link rel="icon" type="image/png" sizes="32x32" href="./asset/favicon-32x32.png">
# <link rel="icon" type="image/png" sizes="192x192" href="./asset/favicon-192x192.png">

favicons = """<!-- Favicon -->
<link href="./asset/favicon.ico" rel="icon" type="image/x-icon"/>
<link rel="apple-touch-icon" sizes="180x180" href="./asset/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="./asset/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="192x192" href="./asset/favicon-192x192.png">"""

html = re.sub(r'<!-- Favicon -->.*?<link[^>]+favicon\.svg[^>]+>', favicons, html, flags=re.DOTALL)


# Let's add a script to intercept ANY WhatsApp link clicks globally
interceptor = """
<script>
// Intercept all WhatsApp link clicks globally to ensure they go to the new number
document.addEventListener('click', function(e) {
    // Find the closest anchor tag
    var a = e.target.closest('a');
    if (a && a.href && a.href.toLowerCase().includes('api.whatsapp.com/send')) {
        // Replace whatever phone number is there with our new one
        a.href = a.href.replace(/phone=\d+/, 'phone=919075060900');
    }
}, true); // Use capture phase to intercept before third-party scripts
</script>
"""

if "Intercept all WhatsApp link clicks" not in html:
    html = html.replace('</body>', interceptor + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
