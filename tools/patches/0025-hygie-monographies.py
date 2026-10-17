import os, sys
# Patch 0025 · Hygie · 17.10.2026 · Monographie au survol (et au clic) de chaque diagnostic différentiel.
# Données : assets/ck/mono-<lettre>.js (tools/mono_build.py), chargées à la demande par ckLoad ; une
# monographie par libellé normalisé, partagée par tous les SSP. Sans monographie : texte TIP.d inchangé.
# Ne touche ni l'ordre ni la prévalence des différentiels (chantier d'Asclépios).
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

rep('#tip .ck-fil{', '#tip .mono-r{color:#b3261e}#tip .ck-fil{')
rep('function tipFor(key){',
    "const MONO_T={};function monoId(n){return (n||'').toLowerCase().normalize('NFKD').replace(/[\\u0300-\\u036f]/g,'').replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'')}\n"
    "function monoGet(n,key){const k=monoId(n);if(!k)return null;const t=/[a-z]/.test(k[0])?k[0]:'0',M=window['CK_MONO_'+t.toUpperCase()];if(M)return M[k]||null;"
    "if(!MONO_T[t]&&typeof ckLoad==='function'){MONO_T[t]=1;ckLoad('mono-'+t).then(()=>{if(!TIPEL.hidden&&tipK===key)showTip({dataset:{t:key}},tipPin,tipOp||TIPEL,false,true)}).catch(()=>{})}return null}\n"
    'function tipFor(key){')
rep("else if(b[0]==='d'){ti='Diagnostic différentiel : '+((NOT[a]||[[]])[0][i]||'');h=T.d[i];src=T.s}",
    "else if(b[0]==='d'){const dn=(NOT[a]||[[]])[0][i]||'',MO=monoGet(dn,key);ti='Diagnostic différentiel : '+dn;h=T.d[i];src=T.s;"
    "if(MO)return {hd:'Monographie · '+a,ti:dn,h:MO.h,src:MO.s}}")
open(p, 'w', encoding='utf-8').write(s)
print('0025 appliqué')
