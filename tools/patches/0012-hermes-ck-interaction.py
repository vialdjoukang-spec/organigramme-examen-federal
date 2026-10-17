import os, sys
# Patch 0012 · Hermès · 17.10.2026 · NC-0 : types de fenêtre CK (glo, syn, hyp, nc, loc), lieur du glossaire gloLink(),
# pile de fenêtres imbriquées (5 niveaux, « ← Retour », fil d’Ariane, sans cycle), couches, vues et tour des schémas.
# Le contrat showTip/hideTip est conservé : les appels existants (4 arguments) gardent leur effet ; le 5e argument
# (keep) remplace la fenêtre courante sans toucher à la pile. Code dans 0012-ck-interaction.js. Se rejoue après 0010.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

# Style : dans le <style> de <head> (le validateur Nu refuse toute règle nouvelle dans celui de <body>) ; variables seulement.
CSS = ('#tip .h .ck-hb{display:flex;gap:6px;align-items:center;margin-left:auto}'
       '#tip .h .bk{font:600 .74rem var(--fb);letter-spacing:0;text-transform:none;color:var(--ink);padding:2px 9px;border:1px solid var(--line);border-radius:8px;min-height:28px;display:inline-flex;align-items:center;cursor:pointer}'
       '#tip .h .bk:focus-visible{outline:2px solid var(--gold)}'
       '#tip .ck-fil{font-size:.74rem;color:var(--mut);margin:0 0 6px;line-height:1.5}#tip .ck-fil button{all:unset;cursor:pointer;color:var(--ink);text-decoration:underline;text-underline-offset:2px}'
       '#tip .ck-fil button:focus-visible{outline:2px solid var(--gold)}#tip .ck-fil [aria-current]{font-weight:700;color:var(--ink)}'
       '#tip.ck .ck-b p{margin:0 0 6px;text-align:justify}#tip.ck .ck-b ul{margin:0 0 6px;padding-left:1.2em}#tip.ck .ck-b li{text-align:justify}'
       '#tip .ck-src{font-size:.72rem;color:var(--mut);border-top:1px solid var(--line);padding-top:6px;margin-top:8px}'
       '#tip .urg{display:inline-block;padding:1px 8px;border-radius:99px;background:color-mix(in srgb,var(--bad) 14%,transparent);color:var(--bad);font-weight:700}'
       '#tip .ck-tabs,#tip .ck-vues{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 8px}#tip .ck-tabs [aria-selected=true],#tip .ck-vues [aria-pressed=true]{border-color:var(--ok);box-shadow:inset 0 -2px 0 var(--ok);font-weight:700}'
       '#tip .ck-couches{display:flex;flex-wrap:wrap;gap:2px 12px;border:1px solid var(--line);border-radius:8px;margin:0 0 8px;padding:4px 10px 6px;font-size:.8rem}'
       '#tip .ck-couches legend{font-weight:700;padding:0 4px}#tip .ck-couches label{display:inline-flex;gap:5px;align-items:center;min-height:28px}'
       '#tip .ck-fig{margin:0}#tip .ck-fig svg,#tip .ck-fig img{display:block;width:100%;height:auto;max-height:46vh}#tip .ck-cr{font-size:.68rem;color:var(--mut);margin-top:4px}'
       '#tip .ck-tour{width:100%;aspect-ratio:4/3;background-size:800% 100%;background-repeat:no-repeat;background-position:0 0;border:1px solid var(--line);border-radius:8px;cursor:ew-resize;touch-action:pan-y}'
       '#tip .ck-tour:focus-visible{outline:2px solid var(--gold)}#tip .ck-list{list-style:none;padding:0;margin:0}#tip .ck-list li{padding:6px 0;border-bottom:1px solid var(--line)}'
       '#tip .ck-fig{position:relative}#tip .ck-fig .nc-num{cursor:pointer}#tip .ck-fig .nc-num:focus-visible{outline:2px solid var(--gold);outline-offset:2px}'
       '#tip .ck-bulle{position:absolute;z-index:2;max-width:min(280px,90%);padding:4px 8px;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink);font-size:.78rem;line-height:1.35;box-shadow:0 6px 16px -8px rgba(0,0,0,.35);pointer-events:none;text-align:left}'
       '#tip .ck-etats{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 8px}#tip .ck-etats [aria-pressed=true]{border-color:var(--ok);box-shadow:inset 0 -2px 0 var(--ok);font-weight:700}'
       '#tip .ck-det{margin:8px 0 0}#tip .ck-det summary{cursor:pointer;font-weight:700;min-height:28px}#tip .ck-det ul{margin:4px 0 6px;padding-left:1.2em}#tip .ck-det li{text-align:justify;margin:0 0 4px}'
       '@media (max-width:620px){#tip.ck-nc{max-height:min(88dvh,760px)}#tip.ck-nc .ck-fig svg,#tip.ck-nc .ck-fig img{max-height:min(54dvh,520px)}#tip .ck-det summary{min-height:36px}#tip .h .bk{min-height:40px;padding:4px 12px}#tip .ck-couches label{min-height:36px}#tip .ck-list li{padding:9px 0}}')
A = '#grid .blk.nodu b{padding-right:0}'
rep(A, A + CSS)

# Types CK dans tipFor ; état de la pile.
# Réglage « Fond doré » retiré de l’en-tête (Athéna, 17.10.2026) : le champ reste caché pour la compatibilité (Iris, patch 0005 d’Apollon).
rep('<label>Fond doré <input type="range" id="d-gilt" min="0" max="100" step="5"> <b id="d-gv"></b></label>',
    '<span hidden><input type="range" id="d-gilt" min="0" max="100" step="5" tabindex="-1" aria-label="Fond doré (réglage retiré)"> <b id="d-gv"></b></span>')
rep('<span>0 % = feuille blanche</span></div>', '</div>')
rep("return null}\nlet tipT=null,tipK=null", "const ck=ckTip(ty,a,b);if(ck!==undefined)return ck;\n return null}\nlet tipTi='',tipT=null,tipK=null")

# showTip : empilement depuis la fenêtre, remplacement (keep), en-tête « ← Retour » et fil d’Ariane, liaison du corps.
rep("function showTip(el,pin,op,kbd){const k=el.dataset.t,x=tipFor(k);if(!x||!x.h){hideTip(true);return}op=op||el;",
    "function showTip(el,pin,op,kbd,keep){const k=el.dataset.t,x=tipFor(k);if(!x||!x.h){if(!keep)hideTip(true);return}op=op||el;"
    "const nest=!keep&&!TIPEL.hidden&&!!tipK&&TIPEL.contains(op);if(nest){if(tipStk.length>=CK_MAX-1)return;tipStk.push({k:tipK,ti:tipTi});op=tipOp&&tipOp.isConnected?tipOp:TIPEL;pin=true}"
    "else if(!keep)tipStk.length=0;const lv=tipStk.length+1;tipTi=x.ti;")
rep('TIPEL.innerHTML=`<div class="h"><span>${esc(x.hd)}</span><button aria-label="Fermer">×</button></div><div class="t">${esc(x.ti)}</div><div>${x.h}</div>',
    'TIPEL.innerHTML=`<div class="h"><span>${esc(x.hd+(lv>1?\' · niveau \'+lv:\'\'))}</span><span class="ck-hb">${lv>1?\'<button class="bk" type="button" aria-label="Retour à la fenêtre précédente">← Retour</button>\':\'\'}<button aria-label="Fermer">×</button></span></div>'
    '${lv>1?`<nav class="ck-fil" aria-label="Fil d’Ariane">${tipStk.map((s,i)=>`<button type="button" data-lv="${i}">${esc(s.ti)}</button> › `).join(\'\')}<span aria-current="page">${esc(x.ti)}</span></nav>`:\'\'}'
    '<div class="t">${esc(x.ti)}</div><div class="ck-b">${x.h}</div>')
rep("TIPEL.hidden=false;TIPEL.setAttribute('role',tipPin?'dialog':'tooltip');", "tipCk(lv,k);TIPEL.hidden=false;TIPEL.setAttribute('role',tipPin?'dialog':'tooltip');")
rep(" const r=op.getBoundingClientRect(),w=TIPEL.offsetWidth", " if(op!==TIPEL&&op.isConnected){const r=op.getBoundingClientRect(),w=TIPEL.offsetWidth")
rep("if(pin&&matchMedia('(max-width:620px)').matches){const tr=TIPEL.getBoundingClientRect();if(r.bottom>tr.top-8)scrollBy(0,r.bottom-tr.top+16)};",
    "if(pin&&!nest&&!keep&&matchMedia('(max-width:620px)').matches){const tr=TIPEL.getBoundingClientRect();if(r.bottom>tr.top-8)scrollBy(0,r.bottom-tr.top+16)}};")
rep("tipK=null;tipPin=false;tipOp=null}", "tipK=null;tipPin=false;tipOp=null;tipStk.length=0;tipTi=''}")
# Clics dans la fenêtre : retour, fil d’Ariane, commandes CK et termes reliés passent avant la fermeture.
rep("if(e.target.closest('#tip .h button')){hideTip(true);return}if(e.target.closest('#tip'))return;",
    "if(tipNav(e))return;if(e.target.closest('#tip .h button')){hideTip(true);return}if(e.target.closest('#tip'))return;")

JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '0012-ck-interaction.js'), encoding='utf-8').read()
assert '</script' not in JS
rep('function renderAll(){', JS + 'function renderAll(){')
open(p, 'w', encoding='utf-8').write(s)
print('0012 appliqué')
