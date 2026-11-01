# Test script to inspect portfolio.html and main.js for theme toggle logic

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
btns = re.findall(r'<button[^>]*theme-toggle[^>]*>.*?</button>', html, re.DOTALL)
print('Theme toggle button in HTML:')
for b in btns:
    print(' ', b.strip())

scripts = re.findall(r'<script[^>]*>.*?</script>', html, re.DOTALL)
print(f'\nTotal scripts in HTML: {len(scripts)}')
for s in scripts:
    print('--- Script:\n', s[:120])
