import json, os, sys
# Patch 0005 · Apollon · 17.10.2026 · présentation premium et sélecteur « Thème de fond d’écran ».
# 1. tools/patches/apollon-jetons.css entre dans le style de head (jetons, :root:root pour primer sur les jetons historiques).
# 2. tools/patches/apollon.css entre en fin du style de body dans « @scope { … } » : le validateur Nu y admet les règles,
#    et à spécificité égale une règle scopée l’emporte sur une règle non scopée (proximité).
# 3. La feuille Google Fonts est retirée (polices du système, aucun CDN) ; lang="fr" sur <html>.
# 4. Sélecteur de fond (10 thèmes de tools/patches/fonds.json) : bouton fixe, panneau à radios, choix dans localStorage « orga-fond ».
#    Seul ajout de comportement, demandé par le titulaire le 17.10.2026 ; aucun texte, aucune donnée ni aucun ID existant ne change.
# Rejeu : APP_FILE=app_v2.html python3 tools/patches/0005-apollon-premium.py (jamais sur orig/app.html).
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
D = os.path.dirname(os.path.abspath(__file__))
s = open(p, encoding='utf-8').read()
rd = lambda n: open(os.path.join(D, n), encoding='utf-8').read().strip()
css, tok, F = rd('apollon.css'), rd('apollon-jetons.css'), json.load(open(os.path.join(D, 'fonds.json'), encoding='utf-8'))
assert '</style' not in css + tok
def rep(a, b):
    global s
    c = s.count(a); assert c == 1, (a[:80], c); s = s.replace(a, b)
assert s.count('Apollon · présentation premium') == 0, 'Patch déjà appliqué.'
ids = [f['id'] for f in F]
early = ("<script>/* Apollon : thème de fond mémorisé, appliqué avant le premier affichage. */try{var f=localStorage.getItem('orga-fond'),T="
         + json.dumps({f['id']: f['schema'] for f in F}, separators=(',', ':'))
         + ";if(f&&T[f]){document.documentElement.setAttribute('data-fond',f);document.documentElement.setAttribute('data-theme',T[f])}}catch(e){}</script>")
rep('<!doctype html><html><head>', '<!doctype html><html lang="fr"><head>')
rep('</style></head>', '\n' + tok + '\n</style>' + early + '</head>')
rep('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">\n', '')
rep('@media (prefers-reduced-motion:reduce){*{transition:none!important}}\n</style>',
    '@media (prefers-reduced-motion:reduce){*{transition:none!important}}\n@scope{\n' + css + '\n}\n</style>')
opts = ''.join(f'<label><input type="radio" name="fond" value="{f["id"]}"><span class="sw" style="--sw-bg:{f["bg"]};background:{f["paper"]}"></span><span>{f["nom"]}</span></label>' for f in F)
ui = ('<button type="button" class="fond-btn" id="fond-btn" aria-haspopup="dialog" aria-expanded="false" aria-controls="fond-pan"><i aria-hidden="true">◐</i><span>Thème de fond d’écran</span></button>\n'
      '<div class="fond-pan" id="fond-pan" role="dialog" aria-labelledby="fond-h" hidden><p class="fond-h" id="fond-h">Thème de fond d’écran</p>'
      '<div role="radiogroup" aria-labelledby="fond-h"><label><input type="radio" name="fond" value=""><span class="sw" style="--sw-bg:#f5efe1;background:#fffefb"></span><span>Par défaut (réglage « Fond doré »)</span></label>' + opts + '</div>'
      '<div class="row"><button type="button" class="b" id="fond-x">Fermer</button></div></div>\n'
      "<script>/* Apollon : sélecteur de fond d’écran. */(function(){var B=document.getElementById('fond-btn'),P=document.getElementById('fond-pan'),R=document.documentElement,T="
      + json.dumps({f['id']: f['schema'] for f in F}, separators=(',', ':')) +
      ";function cur(){return R.getAttribute('data-fond')||''}"
      "function set(f){if(f&&T[f]){R.setAttribute('data-fond',f);R.setAttribute('data-theme',T[f])}else{R.removeAttribute('data-fond');R.removeAttribute('data-theme')}try{f?localStorage.setItem('orga-fond',f):localStorage.removeItem('orga-fond')}catch(e){}}"
      "function open(o){P.hidden=!o;B.setAttribute('aria-expanded',String(o));if(o){var c=P.querySelector('input[value=\"'+cur()+'\"]')||P.querySelector('input');c.checked=true;c.focus({preventScroll:true})}}"
      "B.addEventListener('click',function(e){e.stopPropagation();open(P.hidden)});document.getElementById('fond-x').addEventListener('click',function(){open(false);B.focus()});"
      "P.addEventListener('change',function(e){if(e.target.name==='fond')set(e.target.value)});"
      "document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!P.hidden){open(false);B.focus()}});"
      "document.addEventListener('click',function(e){if(!P.hidden&&!P.contains(e.target)&&e.target!==B&&!B.contains(e.target))open(false)})})();</script>\n")
rep('<nav class="tabs" role="tablist">', ui + '<nav class="tabs" role="tablist">')
open(p, 'w', encoding='utf-8', newline='').write(s)
print('Patch 0005 appliqué.')
