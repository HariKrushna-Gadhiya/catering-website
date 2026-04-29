import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the Book Now button link in header-actions
    content = content.replace('<a href="contact.html" class="btn btn-primary">Book Now</a>', '<a href="order.html" class="btn btn-primary">Order Now</a>')
    
    # Replace other potential links to order page
    content = content.replace('<a href="contact.html" class="btn btn-primary btn-lg">Book Now</a>', '<a href="order.html" class="btn btn-primary btn-lg">Order Now</a>')
    content = content.replace('<a href="contact.html" class="btn btn-secondary">Book Now</a>', '<a href="order.html" class="btn btn-secondary">Order Now</a>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated links')
