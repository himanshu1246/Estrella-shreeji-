import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix image wrapper link
html = html.replace(
    '<a class="glightbox" data-gallery="masterplanimg" href="./img/mp.jpg?v=2">\n<div class="bd-img blur mt-3 mb-4">',
    '<div class="bd-img blur mt-3 mb-4" style="cursor: pointer;" data-bs-target="#enqPopup" data-bs-toggle="modal" data-form-name="View Master Plan Layout" data-formbtn="Submit" data-formtitle="View Master Plan Layout">'
)

# Fix button and remove closing </a> for the image wrapper
html = html.replace(
    '</a><a class="btn btn-dark btn-cta mt-3 glightbox" data-gallery="masterplanbtn" href="./img/mp.jpg?v=2">',
    '<button class="btn btn-dark btn-cta mt-3" data-bs-target="#enqPopup" data-bs-toggle="modal" data-form-name="View Master Plan Layout" data-formbtn="Submit" data-formtitle="View Master Plan Layout">'
)

# Fix closing tag for the button (since we changed <a> to <button>)
html = html.replace(
    'View Master Plan Layout\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</a>\n</div>',
    'View Master Plan Layout\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</button>\n</div>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
