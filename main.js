// Interactive behaviors for Evelin Lins Hybrid Portfolio (Marketing & Analytics)

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
