with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('post-untrimmed applied:', 'post-untrimmed' in html)
print('editorial-atmosphere applied:', 'editorial-atmosphere' in html)
print('Inline failsafe present:', 'Inline failsafe for theme toggle' in html)

# Check button has no onclick
btn_start = html.find('<button id="theme-toggle"')
btn_end = html.find('</button>', btn_start) + 9
btn_html = html[btn_start:btn_end]
print('onclick removed from button:', 'onclick' not in btn_html)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()
print('post-untrimmed class in CSS:', 'post-untrimmed' in css)
print('editorial-atmosphere class in CSS:', 'editorial-atmosphere' in css)
print('aspect-ratio in CSS:', 'aspect-ratio' in css)
print('Theme Toggle Icon Switching in CSS:', 'Theme Toggle Icon Switching' in css)
print('light theme declared in CSS:', '[data-theme=' in css and 'light' in css)
