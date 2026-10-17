import os, sys
# Patch 0010 · Atlas · 17.10.2026 · Chargement différé des données CK (chantier Nerfs crâniens et CK, NC-0).
# ckLoad(nom) injecte <script src="assets/ck/<nom>.js"> une seule fois et rend une promesse de window.CK_<NOM>
# (compatible file://, contrairement à fetch) ; ckGlo(id) charge la tranche de définitions du glossaire.
# L'index du glossaire (glo-index) se charge quand le navigateur est inactif. Aucune donnée CK dans app_v2.html.
# Se rejoue après 0009. L'ancrage doit apparaître une seule fois.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

rep('function tipFor(key){',
    "const CKP={};function ckLoad(n){const v='CK_'+n.toUpperCase().replace(/[^A-Z0-9]/g,'_');if(window[v])return Promise.resolve(window[v]);"
    "return CKP[n]||(CKP[n]=new Promise((ok,ko)=>{const e=document.createElement('script');e.src='assets/ck/'+n+'.js';e.async=true;"
    "const no=()=>{delete CKP[n];e.remove();ko(new Error('ckLoad '+n))};e.onload=()=>window[v]?ok(window[v]):no();e.onerror=no;document.head.appendChild(e)}))}\n"
    "function ckGlo(id){return ckLoad('glo-'+(/^[a-z]/.test(id)?id[0]:'0')).then(T=>T[id]||null)}\n"
    "(window.requestIdleCallback||(f=>setTimeout(f,1200)))(()=>ckLoad('glo-index').catch(()=>{}),{timeout:4000});\n"
    'function tipFor(key){')

open(p, 'w', encoding='utf-8').write(s)
print('0010 appliqué')
