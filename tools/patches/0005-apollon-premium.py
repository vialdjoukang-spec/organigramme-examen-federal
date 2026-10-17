import os, sys
# Patch 0005 · Apollon · 17.10.2026 · présentation premium (jetons, typographie, composants, thèmes clair, doré et sombre).
# Présentation seule : feuille tools/patches/apollon.css ajoutée en fin du bloc de style principal ; police Google retirée
# (polices du système, aucun CDN) ; attribut lang="fr" sur <html> (accessibilité, aucun texte modifié).
# Rejeu : APP_FILE=app_v2.html python3 tools/patches/0005-apollon-premium.py (jamais sur orig/app.html).
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()
css = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'apollon.css'), encoding='utf-8').read().strip()
assert '</style' not in css
def rep(a, b):
    global s
    c = s.count(a); assert c == 1, (a[:80], c); s = s.replace(a, b)
assert s.count('Apollon · présentation premium') == 0, 'Patch déjà appliqué.'
rep('<!doctype html><html><head>', '<!doctype html><html lang="fr"><head>')
rep('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">\n', '')
rep('@media (prefers-reduced-motion:reduce){*{transition:none!important}}\n</style>',
    '@media (prefers-reduced-motion:reduce){*{transition:none!important}}\n' + css + '\n</style>')
open(p, 'w', encoding='utf-8', newline='').write(s)
print('Patch 0005 appliqué.')
