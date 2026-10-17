import os, sys
# Patch 0003 · Atlas · 17.10.2026 · export et import JSON de la progression, erreurs de stockage visibles, rappel d’export.
# Se rejoue après 0001 et 0002 sur une copie (APP_FILE). Chaque ancrage doit apparaître une seule fois.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

CSS = (".bak{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;padding:10px 14px;border:1px solid var(--line);"
       "border-left:4px solid var(--ok);border-radius:10px;background:var(--paper);font-size:.88rem}"
       ".bak>p{margin:0;flex:1 1 300px}.bak .row{flex:0 1 auto}.bak button.b{min-height:36px}"
       ".bak.warn{border-left-color:var(--warn)}.bak.warn>#bak-t{color:var(--warn);font-weight:600}"
       ".bak.bad{border-left-color:var(--bad)}.bak.bad>#bak-t{color:var(--bad);font-weight:600}"
       "#bak-pv,#bak-m{flex-basis:100%;margin:0}#bak-pv p{margin:0 0 8px}#bak-m.bad{color:var(--bad)}#bak-m.ok{color:var(--ok)}\n")

HTML = ('<div class="bak" id="bak" role="region" aria-label="Sauvegarde de la progression">'
        '<p id="bak-t" role="status"></p>'
        '<div class="row"><button class="b p" id="bak-x" type="button">Exporter ma progression</button>'
        '<button class="b" id="bak-i" type="button">Importer une sauvegarde</button>'
        '<input type="file" id="bak-f" accept="application/json,.json" hidden aria-label="Fichier de sauvegarde"></div>'
        '<div id="bak-pv" hidden></div><p id="bak-m" class="st" role="alert" hidden></p></div>\n')

JS = r"""/* ---------- ATLAS : sauvegarde (export, import, erreurs de stockage) ---------- */
/* Format v1 : {format:"organigramme-examen-federal",version:1,exporte:ISO,cles:{"orga-…":"<valeur brute>"}} ; orga-bak (date du dernier export) n’est pas exporté. */
var BAK_V=1,BAK_F='organigramme-examen-federal',BAK_KEY='orga-bak',BAK_DAYS=7,lsBad={},bakPend=null;
function lsSet(k,v){try{localStorage.setItem(k,v);if(lsBad[k]){delete lsBad[k];bakShow()}return true}catch(e){lsBad[k]=(e&&e.name)||'erreur';const y=document.getElementById('sync');if(y)y.textContent='Non enregistré dans ce navigateur ('+lsBad[k]+')';bakShow();return false}}
function bakKeys(){const o={};for(let i=0;i<localStorage.length;i++){const k=localStorage.key(i);if(k&&k.indexOf('orga-')===0&&k!==BAK_KEY&&k!=='orga-probe')o[k]=localStorage.getItem(k)}return o}
function bakDate(t){const d=new Date(t);return isNaN(d)?'?':d.toLocaleDateString('fr-CH')+' à '+d.toLocaleTimeString('fr-CH',{hour:'2-digit',minute:'2-digit'})}
function bakMsg(t,c){const m=document.getElementById('bak-m');m.textContent=t;m.className='st '+(c||'');m.hidden=!t}
function bakShow(){const el=document.getElementById('bak');if(!el)return;const bad=Object.keys(lsBad);let t,c='';
 if(bad.length){c='bad';t='L’enregistrement dans ce navigateur a échoué ('+lsBad[bad[0]]+'), car son stockage est plein ou bloqué : vos dernières modifications risquent de se perdre. Exportez votre progression maintenant, puis libérez de l’espace.'}
 else{let last=null;try{last=localStorage.getItem(BAK_KEY)}catch(e){}const n=last?Math.floor((Date.now()-new Date(last))/864e5):null;
  if(!last){c='warn';t='Votre progression vit seulement dans ce navigateur, et vous ne l’avez encore jamais exportée. Exportez-la chaque semaine, car Safari peut effacer ce stockage après sept jours sans visite.'}
  else if(!(n<BAK_DAYS)){c='warn';t='Votre dernier export date du '+bakDate(last)+', il y a '+n+' jours. Exportez votre progression, car Safari peut effacer ce stockage après sept jours sans visite.'}
  else t='Votre progression est enregistrée dans ce navigateur, et votre dernier export date du '+bakDate(last)+'.'}
 el.className='bak'+(c?' '+c:'');document.getElementById('bak-t').textContent=t}
function bakSum(k){const P=x=>{try{return JSON.parse(k[x]||'null')||{}}catch(e){return {}}},ef=P('orga-ef'),n=o=>Object.keys(o||{}).length;
 return n(ef.seances)+' séances, '+Object.values(ef.exi||{}).filter(v=>v===true).length+' exigences cochées, '+n(P('orga-not'))+' SSP suivis en Notions CK, '+n(P('orga-ges'))+' gestes cochés et '+n(P('orga-cs'))+' simulations CS'}
function bakExport(){local(true);let k;try{k=bakKeys()}catch(e){bakMsg('L’export a échoué, car ce navigateur refuse la lecture de son stockage.','bad');return}
 const d=new Date(),f={format:BAK_F,version:BAK_V,exporte:d.toISOString(),cles:k},a=document.createElement('a');
 a.href=URL.createObjectURL(new Blob([JSON.stringify(f,null,1)],{type:'application/json'}));a.download='organigramme-progression-'+iso(d)+'.json';
 document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},1500);
 lsSet(BAK_KEY,d.toISOString());bakShow();bakMsg('Le fichier « '+a.download+' » contient '+bakSum(k)+'. Gardez-le hors de ce navigateur, par exemple dans votre stockage en ligne.','ok')}
function bakCheck(f){if(!f||typeof f!=='object'||f.format!==BAK_F)return 'Ce fichier ne provient pas d’un export de l’organigramme.';
 if(typeof f.version!=='number'||f.version<1)return 'Ce fichier ne porte pas de numéro de version valide.';
 if(f.version>BAK_V)return 'Ce fichier provient d’une version plus récente de l’application ; rechargez d’abord la page en ligne.';
 if(!f.cles||typeof f.cles!=='object'||!Object.keys(f.cles).length)return 'Ce fichier ne contient aucune donnée de progression.';
 for(const k in f.cles){if(k.indexOf('orga-')!==0||k===BAK_KEY)return 'La clé « '+k+' » n’appartient pas à l’organigramme.';
  if(typeof f.cles[k]!=='string')return 'La clé « '+k+' » n’a pas le format attendu.';
  if(k!=='orga-tab'){try{JSON.parse(f.cles[k])}catch(e){return 'La clé « '+k+' » est endommagée.'}}}return null}
function bakMigrate(f){/* v1 : format initial ; une version future convertira ici les anciennes clés. */return f.cles}
function bakRead(file){bakMsg('');const r=new FileReader();r.onerror=()=>bakMsg('La lecture du fichier a échoué ; votre progression reste inchangée.','bad');
 r.onload=()=>{let f;try{f=JSON.parse(r.result)}catch(e){bakMsg('Ce fichier n’est pas un JSON valide ; votre progression reste inchangée.','bad');return}
  const er=bakCheck(f);if(er){bakMsg(er+' Votre progression reste inchangée.','bad');return}
  bakPend=bakMigrate(f);let cur={};try{cur=bakKeys()}catch(e){}const pv=document.getElementById('bak-pv');
  pv.innerHTML='<p>Ce fichier date du <b>'+esc(bakDate(f.exporte))+'</b> et contient '+esc(bakSum(bakPend))+'.</p><p>Ce navigateur contient actuellement '+esc(bakSum(cur))+'. L’import remplacera toute cette progression, et vous ne pourrez pas l’annuler sans un autre export.</p><div class="row"><button class="b p" id="bak-ok" type="button">Remplacer ma progression</button><button class="b" id="bak-no" type="button">Annuler</button></div>';
  pv.hidden=false;document.getElementById('bak-ok').focus()};r.readAsText(file)}
function bakApply(){if(!bakPend)return;let old={};try{old=bakKeys()}catch(e){}
 try{Object.keys(old).forEach(k=>localStorage.removeItem(k));for(const k in bakPend)localStorage.setItem(k,bakPend[k])}
 catch(e){try{Object.keys(bakKeys()).forEach(k=>localStorage.removeItem(k));for(const k in old)localStorage.setItem(k,old[k])}catch(_){}
  bakMsg('L’import a échoué, car le stockage de ce navigateur est plein ou bloqué ; l’état antérieur est rétabli.','bad');return}
 lsSet(BAK_KEY,new Date().toISOString());try{sessionStorage.setItem('orga-imp','1')}catch(e){}location.reload()}
try{localStorage.setItem('orga-probe','1');localStorage.removeItem('orga-probe')}catch(e){lsBad['orga-probe']=(e&&e.name)||'erreur'}
document.getElementById('bak-x').onclick=bakExport;
document.getElementById('bak-i').onclick=()=>{const f=document.getElementById('bak-f');f.value='';f.click()};
document.getElementById('bak-f').onchange=e=>{const f=e.target.files&&e.target.files[0];if(f)bakRead(f);e.target.value=''};
document.getElementById('bak-pv').addEventListener('click',e=>{if(e.target.id==='bak-ok')bakApply();else if(e.target.id==='bak-no'){bakPend=null;e.currentTarget.hidden=true;bakMsg('L’import est annulé ; votre progression reste inchangée.','ok')}});
bakShow();try{if(sessionStorage.getItem('orga-imp')){sessionStorage.removeItem('orga-imp');bakMsg('La sauvegarde importée est chargée dans ce navigateur.','ok')}}catch(e){}

"""

R = [
    ('.st{font-size:.8rem;color:var(--mut)}\n.heat{', '.st{font-size:.8rem;color:var(--mut)}\n' + CSS + '.heat{'),
    ('</header>\n<nav class="tabs"', '</header>\n' + HTML + '<nav class="tabs"'),
    ('/* ---------- MNÉMOSYNE : persistance', JS + '/* ---------- MNÉMOSYNE : persistance'),
    ("function local(save){try{if(save)localStorage.setItem('orga-ef',JSON.stringify(S));else{const v=JSON.parse(localStorage.getItem('orga-ef')||'null');if(v)S=Object.assign(S,v)}}catch(e){}}",
     "function local(save){if(save){lsSet('orga-ef',JSON.stringify(S));return}try{const v=JSON.parse(localStorage.getItem('orga-ef')||'null');if(v)S=Object.assign(S,v)}catch(e){}}"),
    ("if(!db){$('#sync').textContent='Mémoire locale (ce navigateur)';return}",
     "if(!db){$('#sync').textContent=Object.keys(lsBad).length?'Non enregistré dans ce navigateur ('+Object.values(lsBad)[0]+')':'Mémoire locale (ce navigateur)';return}"),
    ("try{localStorage.setItem('orga-tab',t.dataset.v)}catch(e){}", "lsSet('orga-tab',t.dataset.v)"),
    ("try{localStorage.setItem('orga-cs',JSON.stringify(CSLOG))}catch(e){}put('cs',id,x);renderCSLog()}",
     "lsSet('orga-cs',JSON.stringify(CSLOG));put('cs',id,x);renderCSLog()}"),
    ("try{localStorage.setItem('orga-cs',JSON.stringify(CSLOG))}catch(e){}put('cs',id,x);renderCSLog();",
     "lsSet('orga-cs',JSON.stringify(CSLOG));put('cs',id,x);renderCSLog();"),
    ("try{localStorage.setItem('orga-not',JSON.stringify(NS))}catch(e){}clearTimeout(",
     "lsSet('orga-not',JSON.stringify(NS));clearTimeout("),
    ("try{localStorage.setItem('orga-not',JSON.stringify(NS))}catch(e){}if(!$('#v-not').hidden)",
     "lsSet('orga-not',JSON.stringify(NS));if(!$('#v-not').hidden)"),
    ("try{localStorage.setItem('orga-ges',JSON.stringify(GS))}catch(_){}", "lsSet('orga-ges',JSON.stringify(GS));"),
]
for a, b in R:
    assert s.count(a) == 1, ('ancrage', s.count(a), a[:60])
    s = s.replace(a, b)
assert s.count('localStorage.setItem(') == 4, s.count('localStorage.setItem(')  # lsSet, sonde, import et restauration seulement
open(p, 'w', encoding='utf-8').write(s)
print('ok')
