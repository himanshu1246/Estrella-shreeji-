import urllib.request, re
js = urllib.request.urlopen('https://s3.ap-south-1.amazonaws.com/microsites.images/temp_assets/temp-xi/js/app.js').read().decode('utf-8')
urls = re.findall(r'https?://[^\'\"]+', js)
print("JS URLs found in app.js:")
for u in urls:
    if 'js' in u.lower():
        print(u)
