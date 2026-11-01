import os
import re

for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.findall(r'src="([^"]+)"', content)
    local_files = [m for m in matches if not m.startswith('http') and not m.startswith('//')]
    
    missing = []
    for f in local_files:
        norm_path = f.replace('/', os.sep)
        if not os.path.exists(norm_path):
            missing.append(f)
            
    print(f'{filename}: {len(local_files)} local media/script references, {len(missing)} missing.')
    if missing:
        print('  Missing:', missing)

print('Verification complete!')
