import os
import shutil

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add --bg-card and --border-card to :root if not present
if '--bg-card:' not in css:
    css = css.replace(
        '--bg-surface-tint: #edf7f3;',
        '--bg-surface-tint: #edf7f3;\n  --bg-card: #ffffff;\n  --border-card: rgba(38, 13, 43, 0.08);'
    )

# Add --bg-card and --border-card to [data-theme="dark"] if not present
if '--bg-card: #180d21;' not in css:
    css = css.replace(
        '--bg-surface-tint: #102620;',
        '--bg-surface-tint: #102620;\n  --bg-card: #180d21;\n  --border-card: rgba(255, 255, 255, 0.08);'
    )

extra_css = """
/* ==========================================================================
   Editorial Text Justification & Typographic Standards
   ========================================================================== */
.about-bio p,
.about-text p,
.hero-description,
.case-quote-box,
.case-quote-box p,
.case-narrative p,
.marketing-case-card p,
.pillar-card p,
.flagship-desc,
.timeline-content p,
.faq-answer p,
.text-justified {
  text-align: justify;
  text-justify: inter-word;
  hyphens: auto;
  -webkit-hyphens: auto;
}

/* Ensure smooth theme transitions */
*, *::before, *::after {
  transition: background-color 0.25s ease, border-color 0.25s ease, color 0.2s ease;
}

/* Mobile Responsiveness Refinements */
@media (max-width: 768px) {
  .nav-container {
    padding: 10px 16px;
  }
  .brand-logo {
    font-size: 1.15rem;
  }
  .nav-actions {
    gap: 8px;
  }
  .nav-actions .btn-sm {
    padding: 6px 12px;
    font-size: 0.78rem;
  }
  .theme-toggle-btn {
    width: 36px;
    height: 36px;
    font-size: 0.95rem;
  }
  .social-nav-link {
    width: 36px;
    height: 36px;
    font-size: 1rem;
  }
  .hero-section {
    padding: 40px 0 30px;
  }
  .hero-title {
    font-size: 2rem;
  }
  .arch-container {
    width: 260px;
    height: 350px;
    margin: 0 auto;
  }
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .stat-card {
    border-right: none;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding: 16px 0;
  }
  .stat-number {
    font-size: 2.2rem;
  }
  .marketing-case-card {
    padding: 24px 16px;
    border-radius: var(--radius-lg);
  }
  .case-badge-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
  .palette-pill-bar {
    width: 100%;
    justify-content: space-between;
  }
  .horizontal-slider-strip {
    gap: 12px;
  }
  .carousel-item-slide {
    flex: 0 0 190px;
  }
  .reel-player-box video {
    height: 360px;
  }
  .mirella-gallery-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }
  .mirella-lifestyle-card,
  .ingrid-product-card {
    grid-template-columns: 1fr;
    padding: 20px 16px;
    gap: 20px;
    text-align: left;
  }
  .ingrid-product-img {
    max-width: 220px;
    margin: 0 auto;
  }
  .flagship-box {
    grid-template-columns: 1fr;
    border-radius: var(--radius-lg);
  }
  .flagship-content {
    padding: 28px 20px;
  }
  .flagship-actions {
    flex-direction: column;
  }
  .flagship-actions .btn {
    width: 100%;
    text-align: center;
  }
  .timeline-container::before {
    left: 20px;
  }
  .timeline-item {
    padding-left: 50px;
  }
  .timeline-item::after {
    left: 11px;
  }
  .cta-box {
    padding: 48px 24px;
    border-radius: var(--radius-lg);
  }
  .cta-actions {
    flex-direction: column;
    width: 100%;
  }
  .cta-actions .btn {
    width: 100%;
    text-align: center;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 1.75rem;
  }
  .hero-actions {
    flex-direction: column;
    width: 100%;
  }
  .hero-actions .btn {
    width: 100%;
    text-align: center;
  }
  .carousel-item-slide {
    flex: 0 0 165px;
  }
  .mirella-gallery-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
  }
}
"""

if '/* Editorial Text Justification' not in css:
    css = css + '\n' + extra_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

if os.path.exists('css'):
    shutil.copy2('style.css', 'css/style.css')

print('style.css updated and synced to css/style.css')
