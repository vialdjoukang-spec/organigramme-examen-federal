import os, sys
# Patch 0026 · Hygie · 17.10.2026 · Les monographies quittent assets/ck/ pour assets/mono/ (budget séparé,
# décision de Vial) : monoLoad(t) charge assets/mono/mono-<t>.js à la demande, une seule fois ; un échec
# de chargement libère la tranche pour un nouvel essai au survol suivant. Prérequis : patch 0025.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

rep('const MONO_T={};function monoId(n){',
    "const MONO_T={},MONO_P={};function monoLoad(t){const v='CK_MONO_'+t.toUpperCase();if(window[v])return Promise.resolve(window[v]);"
    "return MONO_P[t]||(MONO_P[t]=new Promise((ok,ko)=>{const e=document.createElement('script');e.src='assets/mono/mono-'+t+'.js';e.async=true;"
    "const no=()=>{delete MONO_P[t];e.remove();ko(new Error('monoLoad '+t))};e.onload=()=>window[v]?ok(window[v]):no();e.onerror=no;document.head.appendChild(e)}))}\n"
    'function monoId(n){')
rep("if(!MONO_T[t]&&typeof ckLoad==='function'){MONO_T[t]=1;ckLoad('mono-'+t).then(",
    "if(!MONO_T[t]){MONO_T[t]=1;monoLoad(t).then(")
rep("tipOp||TIPEL,false,true)}).catch(()=>{})}return null}",
    "tipOp||TIPEL,false,true)}).catch(()=>{delete MONO_T[t]})}return null}")
open(p, 'w', encoding='utf-8').write(s)
print('0026 appliqué')
