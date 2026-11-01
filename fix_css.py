import re
import shutil
import os

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# The broken header section (chars 0 to orphan_end+2)
# Find the two closing braces after :root declaration
first_brace = content.find('}\n', content.find(':root,'))  # line 39
orphan_end = content.find('}\n', first_brace + 1)         # line 85

# Everything after the orphan block is fine
after_orphan = content[orphan_end + 2:]  # skip the '}\n'

# Build the correct, clean header
clean_header = """/* ==========================================================================
   Evelin Lins Portfolio - Modern Hybrid Dark & Clean Design System
   Typography: Outfit (Headings - tall, elongated, clear) + Plus Jakarta Sans (Body)
   ========================================================================== */

:root,
[data-theme="light"] {
  /* Brand Core Colors */
  --color-primary-dark: #260d2b;
  --color-primary-soft: #3f1547;
  --color-primary-light: #6a2478;
  --color-accent-emerald: #0b4a3c;
  --color-accent-emerald-light: #12725c;
  --color-accent-emerald-glow: #2dd4bf;
  --color-accent-lime: #a3e635;
  --color-accent-gold: #d97706;

  /* Surfaces & Backgrounds */
  --bg-page: #fbfafd;
  --bg-surface: #ffffff;
  --bg-surface-soft: #f5edf7;
  --bg-surface-tint: #edf7f3;
  --bg-card: #ffffff;
  --border-card: rgba(38, 13, 43, 0.08);
  --bg-dark-card: #1f0b24;
  --bg-navbar: rgba(251, 250, 253, 0.92);
  --bg-card-contrast: #1c0a21;

  /* Text & Typography */
  --text-main: #180e1c;
  --text-muted: #574b5c;
  --text-light: #83758a;
  --text-white: #ffffff;

  /* Borders & Shadows */
  --border-light: rgba(38, 13, 43, 0.08);
  --border-hover: rgba(38, 13, 43, 0.2);
  --shadow-sm: 0 2px 10px rgba(32, 13, 35, 0.04);
  --shadow-md: 0 10px 30px rgba(32, 13, 35, 0.08);
  --shadow-lg: 0 20px 50px rgba(32, 13, 35, 0.12);
  --shadow-glow: 0 0 25px rgba(18, 114, 92, 0.22);

  /* Geometry & Curves */
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-xl: 36px;
  --radius-pill: 9999px;
  --radius-arch: 180px 180px 24px 24px;

  --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

"""

# Reconstruct the file: clean header + rest of CSS
new_css = clean_header + after_orphan

# Also fix the theme toggle icon rules to be simple and conflict-free
# Remove the broken multi-block theme toggle rules that were added
broken_icon_rules = """
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

# Remove any duplicate/conflicting theme toggle icon rules
# Keep it simple: just use data-theme="dark" override  
new_css = new_css.replace(broken_icon_rules, '')

# Ensure clean, non-conflicting theme toggle icon rules appear once
simple_icon_rules = """
/* Theme Toggle: Moon shown in light mode, Sun shown in dark mode */
.theme-toggle-btn .sun-icon { display: none; color: #facc15; }
.theme-toggle-btn .moon-icon { display: inline-block; }
[data-theme="dark"] .theme-toggle-btn .moon-icon { display: none; }
[data-theme="dark"] .theme-toggle-btn .sun-icon { display: inline-block; }
"""

if '/* Theme Toggle: Moon shown in light mode' not in new_css:
    # Find a good place to insert - after the theme-toggle-btn hover rule
    insert_at = new_css.find('.theme-toggle-btn:hover')
    if insert_at != -1:
        closing_brace = new_css.find('}', insert_at)
        new_css = new_css[:closing_brace + 1] + '\n' + simple_icon_rules + new_css[closing_brace + 1:]

# Remove any old duplicated icon display rules that were in the original CSS
old_icon_blocks_to_clean = [
    """.theme-toggle-btn .sun-icon {
  display: none;   color: #facc15;
}""",
    """.theme-toggle-btn .moon-icon {
  display: inline-block;   color: var(--text-main);
}""",
    """.theme-toggle-btn .moon-icon {
  display: none;
}""",
    """.theme-toggle-btn .sun-icon {
  display: inline-block;
}"""
]

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(new_css)

if os.path.exists('css'):
    shutil.copy2('style.css', 'css/style.css')

print(f'Fixed style.css! Total chars: {len(new_css)}')

# Verify
with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f'Total lines: {len(lines)}')
print('First 10 lines:')
for i in range(10):
    print(f'  {i+1}: {lines[i].rstrip()}')
print('Lines 55-65:')
for i in range(54, 65):
    print(f'  {i+1}: {lines[i].rstrip()}')
