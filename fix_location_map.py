import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the opening <a> tag for location map and add attributes to the inner <div>
html = html.replace(
    '<a class="glightbox" data-gallery="loc-img" href="./img/l-lpp.jpg?v=2">\n<div class="bd-img blur mt-3 mb-4">',
    '<div class="bd-img blur mt-3 mb-4" style="cursor: pointer;" data-bs-target="#enqPopup" data-bs-toggle="modal" data-form-name="View Location Map" data-formbtn="Submit" data-formtitle="View Location Map">'
)

# Remove the corresponding closing </a> tag.
# We know the inner structure is:
# <source ...>
# <img ...>
# </source></picture>
# </div>
# </a>
html = html.replace(
    '</source></picture>\n</div>\n</a>',
    '</source></picture>\n</div>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
