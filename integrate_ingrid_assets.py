import os
import shutil

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

ingrid_editorial_css = """
/* Ingrid Editorial Grid & Product Refinement */
.ingrid-editorial-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin: 20px 0 32px;
}
.ingrid-editorial-card {
  background: var(--bg-surface-soft);
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid var(--border-card);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  display: flex;
  flex-direction: column;
}
.ingrid-editorial-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}
.ingrid-editorial-img {
  width: 100%;
  height: 380px;
  overflow: hidden;
  background: #111;
}
.ingrid-editorial-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.ingrid-editorial-info {
  padding: 20px 24px;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
"""

if '.ingrid-editorial-grid' not in css:
    css += '\n' + ingrid_editorial_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

if os.path.exists('css'):
    shutil.copy2('style.css', 'css/style.css')

print('Updated style.css and css/style.css')

# 2. Update portfolio.html and index.html
with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add style rule to embedded <style> if needed
if '.ingrid-editorial-grid' not in html:
    html = html.replace('.ingrid-product-card {', ingrid_editorial_css + '\n    .ingrid-product-card {')

# The new Ingrid section with the 8-slide carousel, the 2 editorial pieces, and the original crystal apostila
old_ingrid_section_snippet = '''        <!-- PRODUTO DIGITAL: APOSTILA MÉTODO ESCUDO DE CRISTAL -->
        <div class="ingrid-product-card">
          <div class="ingrid-product-img">
            <img src="images/ingrid/apostila.jpg" alt="Apostila — Método Escudo de Cristal" loading="lazy">
          </div>
          <div>
            <span class="case-sub-pill emerald" style="margin-bottom: 8px;">Infoproduto & Diagramação Editorial</span>
            <h4 style="font-family: \'Outfit\', sans-serif; font-size: 1.3rem; font-weight: 700; color: var(--text-main); margin-bottom: 8px;">
              Apostila — Método Escudo de Cristal
            </h4>
            <p style="color: var(--text-muted); line-height: 1.75; font-size: 0.95rem;">
              Desenvolvimento e diagramação completa do material didático para formação profissional em esmaltação em gel. O projeto respeita rigorosamente a identidade visual da marca: tipografia limpa, hierarquia de leitura didática e estética editorial da capa ao miolo, conferindo alto valor percebido ao curso.
            </p>
          </div>
        </div>'''

new_ingrid_section_snippet = '''        <!-- LINHA EDITORIAL & BRANDING VISUAL SENSORIAL -->
        <div style="margin: 36px 0 28px;">
          <div class="carousel-header-title">
            <h4>
              <i class="fa-solid fa-camera-retro"></i> Linha Editorial & Atmosfera de Marca
              <span class="count-tag">Autoridade Técnica & Sensorial</span>
            </h4>
          </div>

          <div class="ingrid-editorial-grid">
            <div class="ingrid-editorial-card">
              <div class="ingrid-editorial-img">
                <img src="images/ingrid/ingrid_post_3erros.jpg" alt="Carrossel Técnico — 3 Erros Fatais Que Fazem Seu Brilho Espelhado Sumir" loading="lazy">
              </div>
              <div class="ingrid-editorial-info">
                <span class="case-sub-pill emerald" style="margin-bottom: 8px; width: fit-content;">Carrossel Técnico & Retenção</span>
                <h5 style="font-family: \'Outfit\', sans-serif; font-size: 1.15rem; font-weight: 700; color: var(--text-main); margin-bottom: 8px;">
                  3 Erros Fatais: Brilho Espelhado
                </h5>
                <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.68; margin: 0;">
                  Conteúdo de atração focado na dor da manicure profissional (<em>"3 Erros fatais que fazem seu brilho espelhado sumir!"</em>). Comunicação direta que retém audiência, gera salvamentos e constrói autoridade técnica imediata.
                </p>
              </div>
            </div>

            <div class="ingrid-editorial-card">
              <div class="ingrid-editorial-img">
                <img src="images/ingrid/ingrid_cortina.jpg" alt="Atmosfera Visual Quiet Luxury — Linho Branco e Joia Minimalista" loading="lazy">
              </div>
              <div class="ingrid-editorial-info">
                <span class="case-sub-pill emerald" style="margin-bottom: 8px; width: fit-content;">Branding Sensorial & Quiet Luxury</span>
                <h5 style="font-family: \'Outfit\', sans-serif; font-size: 1.15rem; font-weight: 700; color: var(--text-main); margin-bottom: 8px;">
                  Estética Sensorial & Calma Visual
                </h5>
                <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.68; margin: 0;">
                  Fotografia editorial com linho branco, luz natural difusa e anel de design minimalista. Elimina qualquer ruído visual, transmitindo o alto padrão e a sofisticação da experiência de atendimento Ingrid Lopes.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- PRODUTO DIGITAL: APOSTILA OFICIAL MÉTODO ESCUDO DE CRISTAL (FOTO ORIGINAL) -->
        <div class="ingrid-product-card">
          <div class="ingrid-product-img">
            <img src="images/ingrid/apostila.jpg" alt="Capa Oficial da Apostila — Método Escudo de Cristal por Ingrid Lopes" loading="lazy">
          </div>
          <div>
            <span class="case-sub-pill emerald" style="margin-bottom: 8px;">Infoproduto & Diagramação Didática</span>
            <h4 style="font-family: \'Outfit\', sans-serif; font-size: 1.35rem; font-weight: 700; color: var(--text-main); margin-bottom: 8px;">
              Apostila Oficial — Método Escudo de Cristal
            </h4>
            <p style="color: var(--text-muted); line-height: 1.75; font-size: 0.95rem; margin-bottom: 12px;">
              Desenvolvimento e diagramação completa do material didático oficial para o curso de Ingrid Lopes em esmaltação de cristal. Utilizando a foto original e o conceito visual cristalino com efeito prismático suave, o projeto eleva o valor percebido do curso com tipografia limpa, hierarquia de aprendizado clara e acabamento editorial de alto padrão.
            </p>
            <div style="font-family: \'Outfit\', sans-serif; font-size: 0.88rem; font-weight: 600; color: var(--color-accent-emerald-light); display: flex; align-items: center; gap: 8px;">
              <i class="fa-solid fa-gem"></i> <em>"Menos retoques para a cliente, mais lucro para você."</em>
            </div>
          </div>
        </div>'''

# Replace in html
if old_ingrid_section_snippet in html:
    html = html.replace(old_ingrid_section_snippet, new_ingrid_section_snippet)
    print('Replaced Ingrid section snippet directly!')
else:
    # Try finding by apostila.jpg
    import re
    m = re.search(r'<!-- PRODUTO DIGITAL: APOSTILA.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
    if m:
        html = html[:m.start()] + new_ingrid_section_snippet + html[m.end():]
        print('Replaced via regex!')
    else:
        print('Could not find exact snippet, will search specifically.')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated portfolio.html and index.html with new Ingrid editorial assets!')
