import re
import os
import shutil

# ==========================================
# 1. UPDATE style.css & css/style.css
# ==========================================
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix Ingrid Editorial Image: 4/5 aspect ratio, NO CROPPING on post!
old_ingrid_css = """.ingrid-editorial-img {
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
}"""

new_ingrid_css = """.ingrid-editorial-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
  margin: 24px 0 36px;
  align-items: stretch;
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
  aspect-ratio: 4 / 5;
  overflow: hidden;
  background: var(--bg-surface);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}
.ingrid-editorial-img img {
  width: 100%;
  height: 100%;
  display: block;
}
.ingrid-editorial-img img.post-untrimmed {
  object-fit: contain !important; /* 100% VISÍVEL: NUNCA CORTA NENHUMA LETRA OU MARGEM */
  background: #faf8f5;
}
.ingrid-editorial-img img.editorial-atmosphere {
  object-fit: cover !important;
  object-position: center center;
}
.ingrid-editorial-info {
  padding: 22px 24px;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}"""

if old_ingrid_css in css:
    css = css.replace(old_ingrid_css, new_ingrid_css)
else:
    # Replace any previous .ingrid-editorial-img block
    css = re.sub(r'\.ingrid-editorial-img\s*\{[^}]*\}\s*\.ingrid-editorial-img\s*img\s*\{[^}]*\}', new_ingrid_css, css)

# Explicit [data-theme="light"] declaration
light_theme_tokens = """
:root,
[data-theme="light"] {
  --bg-page: #fbfafd;
  --bg-surface: #ffffff;
  --bg-surface-soft: #f5edf7;          /* Lavanda suave */
  --bg-surface-tint: #edf7f3;          /* Esmeralda suave */
  --bg-dark-card: #1f0b24;
  --bg-navbar: rgba(251, 250, 253, 0.94);
  --bg-card-contrast: #1c0a21;
  --bg-card: #ffffff;
  --border-card: rgba(38, 13, 43, 0.08);

  --text-main: #180e1c;
  --text-muted: #574b5c;
  --text-light: #83758a;
  --text-white: #ffffff;

  --color-primary-dark: #260d2b;
  --color-primary-soft: #3f1547;
  --color-primary-light: #6a2478;
  --color-accent-emerald: #0b4a3c;
  --color-accent-emerald-light: #12725c;
  --color-accent-emerald-glow: #2dd4bf;
  --color-accent-lime: #a3e635;
  --color-accent-gold: #d97706;

  --border-light: rgba(38, 13, 43, 0.08);
  --border-hover: rgba(38, 13, 43, 0.2);
  --shadow-sm: 0 2px 10px rgba(32, 13, 35, 0.04);
  --shadow-md: 0 10px 30px rgba(32, 13, 35, 0.08);
  --shadow-lg: 0 20px 50px rgba(32, 13, 35, 0.12);
  --shadow-glow: 0 0 25px rgba(18, 114, 92, 0.22);
}
"""

if '[data-theme="light"]' not in css:
    css = css.replace(':root {', light_theme_tokens)

# Ensure Theme Toggle Icon Rules
icon_rules = """
/* Theme Toggle Icon Switching */
.theme-toggle-btn .sun-icon {
  display: none !important;
  color: #facc15;
}
.theme-toggle-btn .moon-icon {
  display: inline-block !important;
  color: var(--text-main);
}
[data-theme="dark"] .theme-toggle-btn .moon-icon {
  display: none !important;
}
[data-theme="dark"] .theme-toggle-btn .sun-icon {
  display: inline-block !important;
}
[data-theme="light"] .theme-toggle-btn .moon-icon {
  display: inline-block !important;
}
[data-theme="light"] .theme-toggle-btn .sun-icon {
  display: none !important;
}
"""

if '/* Theme Toggle Icon Switching */' not in css:
    css += '\n' + icon_rules

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

if os.path.exists('css'):
    shutil.copy2('style.css', 'css/style.css')

print('Updated style.css and css/style.css!')

# ==========================================
# 2. UPDATE main.js & js/main.js
# ==========================================
main_js_content = """// Interactive behaviors for Evelin Lins Hybrid Portfolio (Marketing & Analytics)

// --- Rock-solid Theme Toggle Engine ---
let lastThemeToggle = 0;

function applyTheme(theme) {
  const root = document.documentElement;
  root.setAttribute('data-theme', theme);
  try {
    localStorage.setItem('evelin_theme', theme);
  } catch (e) {}
}

window.toggleTheme = function() {
  const now = Date.now();
  if (now - lastThemeToggle < 300) {
    return; // Debounce guard against multiple fast clicks or duplicate event handlers
  }
  lastThemeToggle = now;

  const root = document.documentElement;
  const current = root.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  const target = current === 'light' ? 'dark' : 'light';
  applyTheme(target);
};

function initTheme() {
  const root = document.documentElement;
  const btn = document.getElementById('theme-toggle');

  // Resolve initial theme
  let saved = null;
  try {
    saved = localStorage.getItem('evelin_theme');
  } catch (e) {}

  if (saved === 'light' || saved === 'dark') {
    applyTheme(saved);
  } else {
    // Check system preference or default to dark
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    applyTheme(prefersDark ? 'dark' : 'light');
  }

  if (btn) {
    // Single, clean handler that cannot double-fire
    btn.onclick = function(e) {
      if (e) {
        if (e.preventDefault) e.preventDefault();
        if (e.stopPropagation) e.stopPropagation();
      }
      window.toggleTheme();
    };
  }
}

function initApp() {
  initTheme();

  // FAQ Accordion toggle
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    if (!questionBtn || questionBtn.dataset.bound) return;
    questionBtn.dataset.bound = 'true';

    questionBtn.onclick = function() {
      const isActive = item.classList.contains('active');
      
      faqItems.forEach(otherItem => {
        if (otherItem !== item) {
          otherItem.classList.remove('active');
        }
      });
      
      if (!isActive) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    };
  });

  // Smooth scrolling for internal anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    if (anchor.dataset.bound) return;
    anchor.dataset.bound = 'true';

    anchor.onclick = function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        if (e && e.preventDefault) e.preventDefault();
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    };
  });

  // Navbar scroll shadow effect
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    if (!navbar) return;
    if (window.scrollY > 40) {
      navbar.style.boxShadow = '0 8px 24px rgba(32, 13, 35, 0.08)';
    } else {
      navbar.style.boxShadow = 'none';
    }
  });

  // Number animation on stats
  const statNumbers = document.querySelectorAll('.stat-number');
  let animated = false;

  const triggerAnimation = () => {
    if (animated) return;
    const statsSection = document.querySelector('.stats-strip');
    if (!statsSection) return;

    const rect = statsSection.getBoundingClientRect();
    if (rect.top <= window.innerHeight * 0.85) {
      animated = true;
      statNumbers.forEach(stat => {
        stat.style.opacity = '0';
        stat.style.transform = 'translateY(10px)';
        setTimeout(() => {
          stat.style.transition = 'all 0.6s ease';
          stat.style.opacity = '1';
          stat.style.transform = 'translateY(0)';
        }, 100);
      });
    }
  };

  window.addEventListener('scroll', triggerAnimation);
  triggerAnimation();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}
"""

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(main_js_content)

if os.path.exists('js'):
    shutil.copy2('main.js', 'js/main.js')

print('Updated main.js and js/main.js!')

# ==========================================
# 3. UPDATE portfolio.html & index.html
# ==========================================
for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean button markup (NO inline onclick to prevent double-firing with JS!)
    old_btn_regex = r'<button\s+id="theme-toggle"[^>]*>.*?</button>'
    new_btn = """<button id="theme-toggle" class="theme-toggle-btn" aria-label="Alternar modo claro e escuro" title="Alternar modo claro e escuro">
          <i class="fa-solid fa-moon moon-icon"></i>
          <i class="fa-solid fa-sun sun-icon"></i>
        </button>"""
    html = re.sub(old_btn_regex, new_btn, html, flags=re.DOTALL)

    # In embedded <style>, update .ingrid-editorial-img
    html = re.sub(
        r'\.ingrid-editorial-img\s*\{[^}]*\}\s*\.ingrid-editorial-img\s*img\s*\{[^}]*\}',
        new_ingrid_css,
        html
    )

    # Update images to add class="post-untrimmed" and class="editorial-atmosphere"
    html = html.replace(
        '<img src="images/ingrid/ingrid_post_3erros.jpg" alt="Carrossel Técnico — 3 Erros Fatais Que Fazem Seu Brilho Espelhado Sumir" loading="lazy">',
        '<img src="images/ingrid/ingrid_post_3erros.jpg" alt="Carrossel Técnico — 3 Erros Fatais Que Fazem Seu Brilho Espelhado Sumir" class="post-untrimmed" loading="lazy">'
    )
    html = html.replace(
        '<img src="images/ingrid/ingrid_cortina.jpg" alt="Atmosfera Visual Quiet Luxury — Linho Branco e Joia Minimalista" loading="lazy">',
        '<img src="images/ingrid/ingrid_cortina.jpg" alt="Atmosfera Visual Quiet Luxury — Linho Branco e Joia Minimalista" class="editorial-atmosphere" loading="lazy">'
    )

    # Add inline backup right before </body>
    failsafe_script = """  <!-- Inline failsafe for theme toggle -->
  <script>
    (function() {
      var btn = document.getElementById('theme-toggle');
      if (btn) {
        btn.onclick = function(e) {
          if (e && e.preventDefault) e.preventDefault();
          if (window.toggleTheme) {
            window.toggleTheme();
          } else {
            var root = document.documentElement;
            var curr = root.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
            var next = curr === 'light' ? 'dark' : 'light';
            root.setAttribute('data-theme', next);
            try { localStorage.setItem('evelin_theme', next); } catch(err) {}
          }
        };
      }
    })();
  </script>
</body>"""

    if '<!-- Inline failsafe for theme toggle -->' not in html:
        html = html.replace('</body>', failsafe_script)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'Updated {filename} successfully!')

print('ALL FIXES APPLIED SUCCESSFULLY!')
