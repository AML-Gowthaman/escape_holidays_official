import sys
import re

with open(r's:\escape holidays\original_site\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove section
text = re.sub(r'\s*<!-- CLIENT VIDEO REVIEWS -->\s*<section id="testimonials">.*?(?=<!-- ABOUT -->)', '\n\n        ', text, flags=re.DOTALL)

# Remove links
text = re.sub(r'\s*<li><a href="#testimonials">Reviews</a></li>', '', text)
text = re.sub(r'\s*<a href="#testimonials" onclick="closeMenu\(\)">Reviews</a>', '', text)

with open(r's:\escape holidays\original_site\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Done!')
