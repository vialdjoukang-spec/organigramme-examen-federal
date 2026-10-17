import os, re, sys
# Patch 0001 · Hermès · 17.10.2026 · clic sur le mot (fenêtre d'information épinglée au clic et au toucher).
# Déjà appliqué : app_v2.html = ce patch appliqué à orig/app.html. Il sert de modèle au skill ssp-patch.
# Rejeu : APP_FILE=/tmp/copie.html python3 tools/patches/0001-clic-sur-le-mot.py (jamais sur orig/app.html).
p=os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s=open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
TWA='tabindex="0" role="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="tip"'
# 1. Notions CK word
rep("<span>${esc(n.t)}${n.k[0]!=='u'?'<button class=\"ti\"",
    "<span>${n.k[0]!=='u'?`<span class=\"tw\" "+TWA+">${esc(n.t)}</span>`:esc(n.t)}${n.k[0]!=='u'?'<button class=\"ti\"")
# 2. Gestes word
rep('<b>${esc(it.s)}</b><button class="ti"', '<b class="tw" '+TWA+'>${esc(it.s)}</b><button class="ti"')
# 3. keyboard shortcut hint on list items
rep('draggable="true" tabindex="0" data-c="${s[0]}" data-t="s|${s[0]}"','draggable="true" tabindex="0" aria-keyshortcuts="i" data-c="${s[0]}" data-t="s|${s[0]}"')
rep('tabindex="0" data-n="${s[0]}" data-t="s|${s[0]}"','tabindex="0" aria-keyshortcuts="i" data-n="${s[0]}" data-t="s|${s[0]}"')
# 4. CSS
rep("[data-t]:hover{outline:1px dashed color-mix(in srgb,var(--gold) 55%,transparent);outline-offset:-1px}",
 "[data-t]:hover{outline:1px dashed color-mix(in srgb,var(--gold) 55%,transparent);outline-offset:-1px}\n"
 ".tw{cursor:pointer;text-decoration:underline dotted color-mix(in srgb,var(--gold) 70%,transparent);text-underline-offset:3px;border-radius:4px;-webkit-tap-highlight-color:transparent}.tw:hover,.tw[aria-expanded=true]{color:var(--gold);text-decoration-style:solid}.tw:focus-visible,[data-t]:focus-visible{outline:2px solid var(--gold);outline-offset:2px}\n"
 "#tip{overscroll-behavior:contain;-webkit-overflow-scrolling:touch;overflow-wrap:anywhere}#tip .h{position:sticky;top:-12px;margin:-12px -14px 6px;padding:10px 14px 6px;background:var(--paper);z-index:1}#tip .h button{min-width:28px;min-height:28px;display:grid;place-items:center;border-radius:8px}#tip .h button:focus-visible{outline:2px solid var(--gold)}#tip img{max-width:100%;height:auto}\n"
 "@media (max-width:620px){#tip{left:8px!important;right:8px!important;top:auto!important;bottom:calc(8px + env(safe-area-inset-bottom))!important;max-width:none;max-height:min(60vh,520px);font-size:.9rem;border-radius:16px 16px 12px 12px}#tip .h button{min-width:40px;min-height:40px;font-size:1.35rem}}")
# 5. JS
old_start=s.index("let tipT=null,tipK=null,tipPin=false;const TIPEL=$('#tip');")
old_end=s.index("addEventListener('scroll',()=>{if(!tipPin)hideTip()},{passive:true});")
block=s[old_start:old_end]
# showTip: keep body, add opener/aria/focus
m=re.search(r"function showTip\(el,pin\)\{(.*?)\nfunction hideTip", block, re.S); body=m.group(1)
assert "const r=el.getBoundingClientRect()" in body
body=body.replace("tipK=k;tipPin=!!pin;","op=op||el;if(tipOp&&tipOp!==op&&tipOp.hasAttribute('aria-expanded'))tipOp.setAttribute('aria-expanded','false');tipK=k;tipPin=!!pin;tipOp=op;")
body=body.replace("TIPEL.hidden=false;","TIPEL.hidden=false;TIPEL.setAttribute('role',tipPin?'dialog':'tooltip');TIPEL.setAttribute('aria-label',x.hd+' · '+x.ti);if(op.hasAttribute('aria-expanded'))op.setAttribute('aria-expanded',String(tipPin));")
body=body.replace("const r=el.getBoundingClientRect()","const r=op.getBoundingClientRect()")
body=body.rstrip()
assert body.endswith("TIPEL.style.left=left+'px'}")
body=body[:-1]+";if(kbd){const cb=TIPEL.querySelector('.h button');if(cb)cb.focus({preventScroll:true})}}"
new=("let tipT=null,tipK=null,tipPin=false,tipOp=null,tipSup=null,lpT=null,lpFired=false,lpXY=null;const TIPEL=$('#tip');\n"
"function showTip(el,pin,op,kbd){"+body+"\n"
"function hideTip(force){if(tipPin&&!force)return;const back=TIPEL.contains(document.activeElement);TIPEL.hidden=true;TIPEL.setAttribute('role','tooltip');if(tipOp){if(tipOp.hasAttribute('aria-expanded'))tipOp.setAttribute('aria-expanded','false');if(back&&tipOp.isConnected)tipOp.focus({preventScroll:true})}tipK=null;tipPin=false;tipOp=null}\n"
"function tipToggle(el,op,kbd){clearTimeout(tipT);if(tipPin&&tipK===el.dataset.t){tipSup=el.dataset.t;hideTip(true)}else showTip(el,true,op,kbd)}\n"
"const fine=matchMedia('(hover:hover) and (pointer:fine)').matches;\n"
"/* Contrôles qui gardent leur propre action : un clic dessus n'épingle pas la fenêtre (le petit i et le mot souligné, eux, l'épinglent toujours). */\n"
"const TIP_NOPIN='button,input,select,textarea,a,label,summary,.it,.blk,[data-open],[data-plan],[data-x]';\n"
"document.addEventListener('mouseover',e=>{if(!fine||tipPin)return;if(e.target.closest('#tip')){clearTimeout(tipT);return}const el=e.target.closest('[data-t]');clearTimeout(tipT);if(!el){tipSup=null;tipT=setTimeout(()=>hideTip(),260);return}if(el.dataset.t===tipSup)return;tipSup=null;if(el.dataset.t===tipK)return;tipT=setTimeout(()=>showTip(el,false),220)});\n"
"document.addEventListener('click',e=>{if(lpFired){lpFired=false;e.preventDefault();e.stopPropagation();return}\n"
" if(e.target.closest('#tip .h button')){hideTip(true);return}if(e.target.closest('#tip'))return;\n"
" const b=e.target.closest('.ti');if(b){const el=b.closest('[data-t]');if(el){e.preventDefault();e.stopPropagation();tipToggle(el,b);return}}\n"
" const w=e.target.closest('.tw');if(w){const el=w.closest('[data-t]');if(el){e.preventDefault();e.stopPropagation();tipToggle(el,w);return}}\n"
" const el=e.target.closest('[data-t]');if(el){const ia=e.target.closest(TIP_NOPIN);if(!ia||!(el.contains(ia)||ia.contains(el))){tipToggle(el,el.querySelector('.tw')||el);return}}\n"
" if(tipPin)hideTip(true)},true);\n"
"document.addEventListener('keydown',e=>{if(e.key==='Escape'){hideTip(true);return}const t=e.target;if(!(t instanceof Element)||e.ctrlKey||e.metaKey||e.altKey)return;\n"
" if((e.key==='Enter'||e.key===' ')&&t.classList.contains('tw')){const el=t.closest('[data-t]');if(el){e.preventDefault();e.stopPropagation();tipToggle(el,t,true)}return}\n"
" if((e.key==='i'||e.key==='I')&&t.matches('.it[data-t],.blk[data-t]')){e.preventDefault();tipToggle(t,t,true)}},true);\n"
"/* Appui long (tactile) sur les éléments dont le clic sert déjà à autre chose : liste des SSP, séances du calendrier. */\n"
"document.addEventListener('pointerdown',e=>{lpFired=false;clearTimeout(lpT);if(e.pointerType==='mouse')return;const el=e.target.closest('[data-t]');if(!el||e.target.closest('input,select,textarea,.ti,.tw,#tip'))return;lpXY=[e.clientX,e.clientY];lpT=setTimeout(()=>{lpFired=true;showTip(el,true)},550)},{passive:true});\n"
"['pointerup','pointercancel'].forEach(n=>document.addEventListener(n,()=>clearTimeout(lpT),{passive:true}));\n"
"document.addEventListener('pointermove',e=>{if(lpXY&&Math.hypot(e.clientX-lpXY[0],e.clientY-lpXY[1])>10)clearTimeout(lpT)},{passive:true});\n"
"document.addEventListener('contextmenu',e=>{if(lpFired&&e.target.closest('[data-t]'))e.preventDefault()});\n")
s=s[:old_start]+new+s[old_end:]
open(p,'w',encoding='utf-8').write(s)
print('ok')
