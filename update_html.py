import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Gabriel's repository link with Evelin's link
old_repo = 'https://github.com/GabrielVieiraDL/aerometrics-dashboard'
new_repo = 'https://github.com/evelinlins/Aerometrics-projeto'
if old_repo in html:
    html = html.replace(old_repo, new_repo)
    print('Replaced AeroMetrics GitHub repo link.')
else:
    print('Old repo link not found.')

# 2. Add inline theme initializer script in <head>
head_script = '''  <script>
    (function() {
      try {
        var t = localStorage.getItem('evelin_theme');
        if (t === 'light' || t === 'dark') {
          document.documentElement.setAttribute('data-theme', t);
        }
      } catch(e) {}
    })();
  </script>
</head>'''

if 'localStorage.getItem(\'evelin_theme\')' not in html:
    html = html.replace('</head>', head_script)
    print('Added theme script to <head>.')

# 3. Add onclick fallback to #theme-toggle button
old_btn = '<button id="theme-toggle" class="theme-toggle-btn" aria-label="Alternar modo claro e escuro" title="Alternar modo claro e escuro">'
new_btn = '<button id="theme-toggle" class="theme-toggle-btn" onclick="if(window.toggleTheme) window.toggleTheme();" aria-label="Alternar modo claro e escuro" title="Alternar modo claro e escuro">'
if old_btn in html:
    html = html.replace(old_btn, new_btn)
    print('Added onclick to #theme-toggle.')

# 4. Remove duplicate script tag
dup_scripts = '''  <script src="js/main.js"></script>
  <script src="main.js"></script>'''
single_script = '''  <script src="main.js"></script>'''
if dup_scripts in html:
    html = html.replace(dup_scripts, single_script)
    print('Removed duplicate script tag.')

# 5. Fix embedded <style> variables and text justification
old_style_start = '.marketing-cases-section {'
new_style_start = ''':root {
      --bg-card: var(--bg-surface, #ffffff);
      --border-card: var(--border-light, rgba(38, 13, 43, 0.08));
    }
    [data-theme="dark"] {
      --bg-card: var(--bg-surface, #180d21);
      --border-card: var(--border-light, rgba(255, 255, 255, 0.08));
    }

    .marketing-cases-section {'''

if old_style_start in html and '--bg-card: var(--bg-surface' not in html:
    html = html.replace(old_style_start, new_style_start, 1)
    print('Added CSS variable fallbacks to embedded <style>.')

# 6. Ensure Ingrid carousel slides have clear labels and alts
ingrid_carousel_old = '''          <div class="horizontal-slider-strip">
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Capa</span>
              <img src="images/ingrid/ingrid_c1_s1_capa.jpg" alt="Tendências de Beleza de 2026 (Demi Moore)" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 1</span>
              <img src="images/ingrid/ingrid_c1_s2_franja.jpg" alt="Micro Franja" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 2</span>
              <img src="images/ingrid/ingrid_c1_s3_wethair.jpg" alt="Penteado Wet Hair" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 3</span>
              <img src="images/ingrid/ingrid_c1_s4_makefresh.jpg" alt="Make Fresh e Iluminada" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 4</span>
              <img src="images/ingrid/ingrid_c1_s5_acessorios.jpg" alt="Penteados com Acessórios" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 5</span>
              <img src="images/ingrid/ingrid_c1_s6_unhas.jpg" alt="Unhas Minimalistas e Futuristas" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 6</span>
              <img src="images/ingrid/ingrid_c1_s7_sobrancelhas.jpg" alt="Sobrancelhas Naturais" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">CTA</span>
              <img src="images/ingrid/ingrid_c1_s8_cta.jpg" alt="Qual você mais gostou? - CTA Final" loading="lazy">
            </div>
          </div>'''

ingrid_carousel_new = '''          <div class="horizontal-slider-strip">
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Capa</span>
              <img src="images/ingrid/ingrid_c1_s1_capa.jpg" alt="Tendências de Beleza de 2026 - Demi Moore (Capa Oficial)" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 1</span>
              <img src="images/ingrid/ingrid_c1_s2_franja.jpg" alt="Micro Franja: Ousadia e Retrô" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 2</span>
              <img src="images/ingrid/ingrid_c1_s3_wethair.jpg" alt="Penteado Wet Hair: Sofisticação Moderna" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 3</span>
              <img src="images/ingrid/ingrid_c1_s4_makefresh.jpg" alt="Make Fresh e Iluminada: Naturalidade e Saúde" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 4</span>
              <img src="images/ingrid/ingrid_c1_s5_acessorios.jpg" alt="Penteados com Acessórios: Criatividade" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 5</span>
              <img src="images/ingrid/ingrid_c1_s6_unhas.jpg" alt="Unhas Minimalistas e Futuristas: Quiet Luxury" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">Slide 6</span>
              <img src="images/ingrid/ingrid_c1_s7_sobrancelhas.jpg" alt="Sobrancelhas Naturais e Autênticas" loading="lazy">
            </div>
            <div class="carousel-item-slide">
              <span class="slide-badge-label">CTA</span>
              <img src="images/ingrid/ingrid_c1_s8_cta.jpg" alt="Qual você mais gostou? - Me conta nos comentários" loading="lazy">
            </div>
          </div>'''

# normalize and replace if needed
if ingrid_carousel_old in html:
    html = html.replace(ingrid_carousel_old, ingrid_carousel_new)
    print('Updated Ingrid carousel markup with enhanced alts.')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated both portfolio.html and index.html successfully!')
