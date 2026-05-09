import sys

html_path = r"s:\escape holidays\original_site\index.html"
css_path = r"s:\escape holidays\original_site\css\style.css"

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix CSS grid for contact so it doesn't overlap
css = css.replace("grid-template-columns: 1fr 1.1fr;", "grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Swap sections in HTML so Why Escape is above Contact
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

contact_start = html.find('<!-- CONTACT -->')
contact_end = html.find('</section>', contact_start) + len('</section>')

why_start = html.find('<!-- WHY ESCAPE -->')
why_end = html.find('</section>', why_start) + len('</section>')

if contact_start != -1 and why_start != -1:
    contact_block = html[contact_start:contact_end]
    why_block = html[why_start:why_end]
    
    # We want Why Escape to be above Contact
    # Remove Why block
    html = html[:why_start] + html[why_end:]
    
    # Now replace Contact block with Why block + Contact block
    html = html.replace(contact_block, why_block + "\n\n        " + contact_block)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done swapping and fixing CSS")
else:
    print("Could not find sections")
