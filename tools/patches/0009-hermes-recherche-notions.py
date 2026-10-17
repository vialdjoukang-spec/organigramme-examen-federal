import os, sys
# Patch 0009 · Hermès · 17.10.2026 · La recherche du Calendrier trouve aussi un SSP par ses diagnostics différentiels
# et ses notions (NOT) : « insuffisance cardiaque », exemple de la barre, ne renvoyait aucun résultat.
# Se rejoue après 0004. Chaque ancrage doit apparaître une seule fois.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

rep('.cq-p span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}',
    '.cq-p span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}'
    '.cq-p small{flex:0 1 auto;min-width:0;margin-left:auto;color:var(--mut);font-size:.72rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}'
    '@media (max-width:600px){.cq-p{flex-wrap:wrap;row-gap:2px}.cq-p span{flex:1 1 0}.cq-p small{flex-basis:100%;margin-left:0}}')

rep('Cherchez un cours ou un SSP par son nom ou son code, puis placez-le ou ouvrez-le.',
    'Cherchez un cours ou un SSP par son nom, son code, un diagnostic différentiel ou une notion, puis placez-le ou ouvrez-le.')

# Deuxième niveau : titres des diagnostics différentiels (NOT[c][0]) et des notions (NOT[c][1]), normalisés une fois.
rep("function fz(q,k){q=norm(String(q).trim());if(!q)return [];return SSP.map(s=>[fzScore(q,s),s]).filter(a=>a[0]>0).sort((a,b)=>b[0]-a[0]).slice(0,k||8).map(a=>a[1])}",
    "let FZN=null;function fzNot(){if(!FZN){FZN={};for(const s of SSP){const N=NOT[s[0]]||[[],[]],L=[];"
    "(N[0]||[]).forEach(t=>t&&L.push([norm(t),'Diagnostic : '+t,2]));(N[1]||[]).forEach(n=>n&&n[1]&&L.push([norm(n[1]),n[0]+' : '+n[1],0]));FZN[s[0]]=L}}return FZN}\n"
    "function fzNotScore(q,c){const T=q.split(/\\s+/).filter(Boolean);let b=null;"
    "for(const [n,lab,w] of fzNot()[c]){if(!T.every(t=>n.includes(t)))continue;const v=20*T.length+(n.includes(q)?10:0)+w;if(!b||v>b[0])b=[v,lab]}return b}\n"
    "function fz(q,k){q=norm(String(q).trim()).replace(/\\s+/g,' ');if(!q)return [];const why={},R=SSP.map(s=>{const a=fzScore(q,s);if(a>0||q.length<3)return [a,s];"
    "const b=fzNotScore(q,s[0]);if(!b)return [0,s];why[s[0]]=b[1];return [b[0],s]}).filter(a=>a[0]>0).sort((a,b)=>b[0]-a[0]).slice(0,k||8).map(a=>a[1]);R.why=why;return R}")

rep('<code>${esc(s[0])}</code><span>${esc(s[1])}</span></button><button class="b" type="button" data-a="o"',
    '<code>${esc(s[0])}</code><span>${esc(s[1])}</span>${R.why[s[0]]?`<small>${esc(R.why[s[0]])}</small>`:\'\'}</button><button class="b" type="button" data-a="o"')

open(p, 'w', encoding='utf-8').write(s)
print('0009 appliqué')
