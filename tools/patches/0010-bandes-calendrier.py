import os, sys
# Patch 0010 · Hermès · 17.10.2026 · Bandes de séance du Calendrier : aucun texte coupé sans signe.
# Sur ordinateur, une séance de 60 min laissait sa troisième ligne coupée à mi-hauteur. Désormais, chaque bande
# masque la durée quand elle cacherait l’horaire ou le code (elle reste lisible dans la fenêtre), compte les lignes qui tiennent dans sa hauteur (-webkit-line-clamp mesuré), finit par « … » si le texte est plus
# long, et passe sur une seule ligne compacte quand moins d’une ligne tient (15 et 30 min). Le texte complet
# (activité, chapitre, horaire, durée) s’affiche dans la fenêtre de la séance, au survol, au clic, au clavier (i)
# et à l’appui long. Se rejoue après 0004. Chaque ancrage doit apparaître une seule fois.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

A = '.blk .t{white-space:normal;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}'
rep(A, A + '.blk .t{-webkit-line-clamp:var(--cl,3);overflow-wrap:anywhere}'
    '.blk b{display:block;padding-right:2.7em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
    '.blk.mini{display:flex;align-items:baseline;gap:5px;padding-top:1px;padding-bottom:1px;line-height:1;white-space:nowrap}'
    '.blk.mini b{flex:0 1 auto;min-width:0;padding-right:0;line-height:1}'
    '.blk.mini .t{display:block;flex:1 1 0;min-width:0;line-height:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
    '.blk.mini.done::after{position:static;flex:none;line-height:1}.blk.mini .du,.blk.nodu .du{display:none}.blk.nodu b{padding-right:0}')

# Le texte complet de la séance dans sa fenêtre (clé s|code|séance).
rep('data-id="${id}" data-t="s|${x.ssp}"', 'data-id="${id}" data-t="s|${x.ssp}|${id}"')
rep("if(ty==='s'){const T=TIP[a],s=BY[a];if(!T)return null;return {hd:'Fiche éclair · '+a,ti:s[1],h:'<b>Définition</b><br>'+T.c[0]",
    "if(ty==='s'){const T=TIP[a],s=BY[a];if(!T)return null;const X=b&&S.seances[b];return {hd:'Fiche éclair · '+a,ti:s[1],"
    "h:(X?'<b>Séance</b> : '+esc(X.act)+' · '+esc(s[1])+', '+calLab(X)+'–'+hm(X.start+X.dur)+' ('+X.dur+'′)<br>':'')+'<b>Définition</b><br>'+T.c[0]")

# Ajustement après chaque rendu, après un redimensionnement de séance, de la fenêtre ou des polices.
rep('g.innerHTML=h;const m0=D[0]', 'g.innerHTML=h;blkFit(g);const m0=D[0]')
rep("P.b.querySelector('.du').textContent=P.dur+'′'}", "P.b.querySelector('.du').textContent=P.dur+'′';blkFit1(P.b)}")
rep('function renderAll(){',
    "function blkFit1(k){const t=k.querySelector('.t'),b=k.querySelector('b');if(!t||!b)return;k.classList.remove('mini','nodu');t.style.removeProperty('--cl');"
    "const cs=getComputedStyle(k),H=k.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom),lh=parseFloat(getComputedStyle(t).lineHeight)||14,"
    "n=Math.floor((H-b.offsetHeight)/lh+0.02);if(n>=1)t.style.setProperty('--cl',n);else k.classList.add('mini');if(b.scrollWidth>b.clientWidth)k.classList.add('nodu')}\n"
    "function blkFit(r){(r||document).querySelectorAll('.blk').forEach(blkFit1)}\n"
    "{let bfT=0;addEventListener('resize',()=>{clearTimeout(bfT);bfT=setTimeout(()=>blkFit(),120)},{passive:true});if(document.fonts)document.fonts.ready.then(()=>blkFit())}\n"
    'function renderAll(){')

open(p, 'w', encoding='utf-8').write(s)
print('0010 appliqué')
