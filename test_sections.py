import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*class="([^"]+)"', html)
if not sections:
    sections = re.findall(r'<section[^>]*class="([^"]+)"[^>]*id="([^"]+)"', html)

print('Sections in portfolio.html:')
for a, b in sections:
    print(f'section id={b if not " " in a else a}, class={a if not " " in a else b}')
