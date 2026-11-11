#!/usr/bin/env python3
"""RÉCEPTACLE — progression.html : page d'accueil unique du projet (ordre de Vial du 11.11.2026), zéro modèle.

Trois onglets :
  1. Cours — une carte par SSP, nommée par le nom véritable du SSP (jamais « LOT ») ; chaque leçon porte le nom de son
     diagnostic (jamais « DX.n ») ; un clic ouvre le cours DANS la page (visionneuse plein écran, retour arrière du
     téléphone compris). Seuls les SSP audités et fusionnés (--audites) sont ouvrables ; les autres montrent leur jauge.
  2. Examens complémentaires — arbre de sous-onglets lu dans Claude/_reference/examens.json.
  3. Pharmacologie — arbre classifiant lu dans Claude/_reference/pharmaco.json.
Les fiches des onglets 2 et 3 (Claude/_reference/fiches/<id>.json) sont intégrées à la page quand elles existent.

Usage : python3 outils/receptacle.py --carte carte.json --audites 1-16 --sortie progression.html
"""
import os, re, csv, json, html, glob, argparse, datetime

LECONS = ['A'] + [f'DX{i}' for i in range(1, 11)]
E = html.escape


def plage(s):
    out = set()
    for bloc in filter(None, re.split(r'[,\s]+', s or '')):
        bloc = bloc.split('=')[0]
        a, _, b = bloc.partition('-')
        out.update(range(int(a), int(b or a) + 1))
    return out


def fichier(lot, l):
    return f'Claude/LOT_{lot:03d}/LOT_{lot:03d}_Phase_A_V0.html' if l == 'A' else f'Claude/LOT_{lot:03d}/LOT_{lot:03d}_Phase_B_V0_DX.{l[2:]}.html'


def noms_dx(lot):
    """Nom de chaque diagnostic : liste gelée, sinon bandeau du cours, sinon titre du fichier."""
    noms, graves = {}, {}
    p = f'Claude/LOT_{lot:03d}/LISTE_DX_CANONIQUE.md'
    if os.path.exists(p):
        for m in re.finditer(r'^DX\.(\d+)\s*—\s*(.+?)\s*(🚩.*)?$', open(p, encoding='utf-8').read(), re.M):
            noms[f'DX{m.group(1)}'] = m.group(2).strip()
            graves[f'DX{m.group(1)}'] = bool(m.group(3))
    for l in LECONS[1:]:
        f = fichier(lot, l)
        if l in noms or not os.path.exists(f):
            continue
        h = open(f, encoding='utf-8', errors='ignore').read(200000)
        m = (re.search(r'class="fm-nom"[^>]*>(.*?)</div>', h, re.S) or re.search(r'<h[12][^>]*>\s*(?:<[^>]+>)*\s*DX\.\d+\s*[—–-]\s*(.*?)</h[12]>', h, re.S)
             or re.search(r'<title>[^<]*DX\.\d+\s*[—–-]?\s*([^<|]+)', h))
        if m:
            n = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))).strip()
            n = re.sub(r'^DX\.\d+\s*[—–-]\s*', '', n)
            if n and not re.match(r'^[GSFO]\d', n):
                noms[l] = n
    return noms, graves


def arbre(chemin):
    return json.load(open(chemin, encoding='utf-8')) if os.path.exists(chemin) else {'onglets': []}


def fiches(dossier):
    out = {}
    for f in sorted(glob.glob(os.path.join(dossier, '*.json'))):
        try:
            out[os.path.basename(f)[:-5]] = json.load(open(f, encoding='utf-8'))
        except ValueError:
            pass
    return out


CSS = """
:root{--fond:#f6f3ee;--carte:#fff;--encre:#141414;--doux:#6a6258;--trait:#e2d9cc;--piste:#ece6dc;--acc:#7f3a20;--rouge:#b3121d;--vert:#2f6b3c}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--fond);color:var(--encre);font:16px/1.45 "Atkinson Hyperlegible",system-ui,-apple-system,"Segoe UI",sans-serif}
header.h{position:sticky;top:0;z-index:5;background:var(--carte);border-bottom:1px solid var(--trait);padding:10px 14px 0}
h1{font-size:1.15rem;margin:0 0 2px}.sous{color:var(--doux);font-size:.82rem;margin:0 0 8px}
nav.on{display:flex;gap:4px;overflow-x:auto;scrollbar-width:none}nav.on::-webkit-scrollbar{display:none}
nav.on button,.so button{font:inherit;border:0;background:none;color:var(--doux);padding:9px 12px;border-bottom:3px solid transparent;white-space:nowrap;cursor:pointer}
nav.on button.a{color:var(--encre);font-weight:700;border-color:var(--acc)}
main{max-width:1180px;margin:0 auto;padding:14px}
section.p{display:none}section.p.a{display:block}
.barre{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:0 0 12px}
.barre input{flex:1 1 220px;font:inherit;padding:10px 12px;border:1px solid var(--trait);border-radius:10px;background:var(--carte)}
.pu{font:inherit;border:1px solid var(--trait);background:var(--carte);border-radius:999px;padding:7px 13px;cursor:pointer;color:var(--encre)}.pu.a{background:var(--encre);color:#fff;border-color:var(--encre)}
.kpi{display:flex;gap:18px;flex-wrap:wrap;margin:0 0 12px;font-size:.84rem;color:var(--doux)}.kpi b{display:block;font-size:1.15rem;color:var(--encre)}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.c{background:var(--carte);border:1px solid var(--trait);border-radius:14px;padding:12px 14px}
.c h2{font-size:1rem;margin:0 0 2px;line-height:1.25}.c .code{color:var(--doux);font-size:.78rem;font-weight:600;letter-spacing:.02em}
.c.pret{border-left:5px solid var(--vert)}
.j{display:grid;grid-template-columns:1fr 44px;align-items:center;gap:8px;margin:6px 0}.j span{font-size:.76rem;font-weight:700;text-align:right}
.t{height:8px;background:var(--piste);border-radius:99px;overflow:hidden}.f{height:100%;width:var(--p);border-radius:inherit;background:hsl(var(--h) 60% 40%)}
details summary{cursor:pointer;color:var(--doux);font-size:.84rem;padding:4px 0}
.ls{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:2px}
.ls a,.ls span{display:flex;gap:8px;align-items:baseline;padding:8px 8px;border-radius:8px;text-decoration:none;color:var(--encre);font-size:.93rem;line-height:1.3}
.ls a{background:#faf7f2;border:1px solid var(--trait)}.ls a:active,.ls a:hover{background:#f2ece3}.ls span{color:var(--doux)}
.ls .g{color:var(--rouge);font-weight:700;flex:none}.ls .mono{font-weight:700}
.vide{color:var(--doux);font-size:.9rem;padding:8px 0}
#vue{position:fixed;inset:0;z-index:20;background:var(--carte);display:none;flex-direction:column}#vue.a{display:flex}
#vue .tete{display:flex;gap:6px;align-items:center;padding:6px 8px;border-bottom:1px solid var(--trait);background:var(--carte)}
#vue .tete b{flex:1;min-width:0;font-size:.86rem;line-height:1.2;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
#vue .tete small{display:block;color:var(--doux);font-weight:400}
#vue button,#vue a.x{font:inherit;border:1px solid var(--trait);background:var(--carte);border-radius:9px;padding:8px 11px;cursor:pointer;color:var(--encre);text-decoration:none;flex:none}
#vue iframe{flex:1;border:0;width:100%}
#fv{position:fixed;inset:0;z-index:19;background:var(--fond);display:none;flex-direction:column}#fv.a{display:flex}
#fv .tete{display:flex;gap:8px;align-items:center;padding:6px 8px;border-bottom:1px solid var(--trait);background:var(--carte)}#fv .tete b{flex:1;font-size:.9rem;line-height:1.2}
#fv .tete button{font:inherit;border:1px solid var(--trait);background:var(--carte);border-radius:9px;padding:8px 11px;cursor:pointer}
#fv .corps{flex:1;overflow:auto;padding:10px;max-width:860px;width:100%;margin:0 auto}#fv .fiche{margin:0}#fv .fiche ul{margin:4px 0;padding-left:18px}#fv .fiche li{margin:3px 0}
.so{display:flex;gap:2px;overflow-x:auto;border-bottom:1px solid var(--trait);margin:0 0 10px;scrollbar-width:none}.so button.a{color:var(--encre);font-weight:700;border-color:var(--acc)}
.so.n2 button{font-size:.92rem;padding:7px 10px}.so.n3 button{font-size:.86rem;padding:6px 9px}
.arb{list-style:none;margin:0;padding:0}.arb ul{list-style:none;margin:0 0 0 14px;padding:0 0 0 12px;border-left:2px solid var(--trait)}
.arb button{font:inherit;text-align:left;width:100%;border:1px solid var(--trait);background:var(--carte);border-radius:10px;padding:9px 12px;margin:4px 0;cursor:pointer;color:var(--encre)}
.arb button[aria-expanded=true]{background:#f2ece3;font-weight:700}.arb button.fe{border-style:dashed}.arb button small{color:var(--doux);font-weight:400}
.arb li>ul{display:none}.arb li.o>ul{display:block}
.fiche{background:var(--carte);border:1px solid var(--trait);border-radius:14px;padding:14px;margin:10px 0}
.fiche h3{margin:0 0 8px;font-size:1.08rem}.fiche h4{margin:14px 0 4px;font-size:.95rem;color:var(--acc)}
.ind{color:var(--rouge);font-weight:700}
.fiche table{border-collapse:collapse;width:100%;font-size:.88rem}.fiche td,.fiche th{border:1px solid var(--trait);padding:6px;vertical-align:top;text-align:left}.fiche th{background:#f2ece3}
.tw{overflow-x:auto}.cas{border:1px solid var(--trait);border-radius:10px;padding:8px 10px;margin:6px 0;background:#faf7f2}
.cas>button{font:inherit;border:0;background:none;padding:2px 0;cursor:pointer;color:var(--acc);font-weight:700;text-align:left}
.cas .suite{display:none;margin:6px 0 0 10px}.cas.o>.suite{display:block}.concl{font-weight:700}
.fiche figure{margin:8px 0}.fiche img{max-width:100%;border-radius:8px}.fiche figcaption{font-size:.82rem;color:var(--doux)}
.src{font-size:.78rem;color:var(--doux);overflow-wrap:anywhere}
@media(max-width:520px){main{padding:10px}.grille{grid-template-columns:1fr}}
"""

JS = r"""
const D=JSON.parse(document.getElementById('donnees').textContent);
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function onglet(id){$$('nav.on button').forEach(b=>b.classList.toggle('a',b.dataset.o===id));$$('section.p').forEach(s=>s.classList.toggle('a',s.id==='p-'+id));}
$$('nav.on button').forEach(b=>b.onclick=()=>{onglet(b.dataset.o);history.replaceState(null,'','#'+b.dataset.o)});
/* ----- Cours ----- */
const liste=[];D.ssp.forEach(s=>s.lecons.forEach(l=>{if(l.f)liste.push({s,l})}));
function ouvrir(i,pousser=true){const {s,l}=liste[i];$('#vue').dataset.i=i;$('#vt').innerHTML=esc(l.n)+'<small>'+esc(s.nom)+'</small>';
  const vieux=$('#vf');const cadre=document.createElement('iframe');cadre.id='vf';cadre.title='Cours';cadre.src=D.base+l.f;vieux.replaceWith(cadre);$('#vn').href=D.base+l.f;$('#vue').classList.add('a');document.body.style.overflow='hidden';
  if(pousser)history.pushState({c:i},'','#cours='+l.id);}
/* Le cadre est recréé à chaque ouverture et retiré à la fermeture : les ancres suivies dans un cours ne s'empilent pas dans l'historique de la page. */
function fermer(){$('#vue').classList.remove('a');const v=$('#vf');const c=document.createElement('iframe');c.id='vf';c.title='Cours';c.src='about:blank';v.replaceWith(c);document.body.style.overflow='';}
$('#vr').onclick=()=>{fermer();history.replaceState(null,'','#cours')};
$('#vp').onclick=()=>{const i=+$('#vue').dataset.i;if(i>0)ouvrir(i-1,false),history.replaceState({c:i-1},'','#cours='+liste[i-1].l.id)};
$('#vs').onclick=()=>{const i=+$('#vue').dataset.i;if(i<liste.length-1)ouvrir(i+1,false),history.replaceState({c:i+1},'','#cours='+liste[i+1].l.id)};
addEventListener('popstate',e=>{if(e.state&&e.state.c!=null&&location.hash.startsWith('#cours='))ouvrir(e.state.c,false);else{if($('#vue').classList.contains('a'))fermer();if($('#fv').classList.contains('a'))fermerFiche()}});
document.addEventListener('click',e=>{const a=e.target.closest('a[data-c]');if(a){e.preventDefault();ouvrir(liste.findIndex(x=>x.l.id===a.dataset.c))}});
function filtrer(){const q=$('#q').value.trim().toLowerCase(),pret=$('#fp').classList.contains('a');
  $$('#p-cours .c').forEach(c=>{const t=c.dataset.t;const ok=(!pret||c.classList.contains('pret'))&&(!q||t.includes(q));c.style.display=ok?'':'none';
    if(q&&ok)c.querySelector('details').open=$$('.ls [data-n]',c).some(x=>x.dataset.n.includes(q))});}
$('#q').oninput=filtrer;$('#fp').onclick=e=>{e.target.classList.toggle('a');filtrer()};filtrer();
/* ----- Arbres (examens, pharmacologie) ----- */
function algo(n){if(!n)return'';if(typeof n==='string')return '<p class="concl">'+esc(n)+'</p>';
  return '<p>'+esc(n.question||'')+'</p>'+(n.branches||[]).map(b=>'<div class="cas"><button type="button">'+esc(b.si)+'</button><div class="suite">'+algo(b.alors)+'</div></div>').join('');}
function tableau(t){if(!t||!t.length)return'';const k=Object.keys(t[0]);return '<div class="tw"><table><tr>'+k.map(x=>'<th>'+esc(x)+'</th>').join('')+'</tr>'+t.map(r=>'<tr>'+k.map(x=>'<td>'+esc(r[x])+'</td>').join('')+'</tr>').join('')+'</table></div>';}
function para(v){return Array.isArray(v)?'<ul>'+v.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul>':'<p>'+esc(v)+'</p>';}
function fiche(id){const f=D.fiches[id];if(!f)return '<div class="fiche"><p class="vide">Fiche en préparation : elle sera rédigée sur sources suisses lues, puis auditée.</p></div>';
  let h='<div class="fiche"><h3>'+esc(f.titre)+'</h3>';
  if(f.indication)h+='<h4>'+(id.startsWith('ph-')?'Indications actuelles':'Indication de la demande')+'</h4><div class="ind">'+para(f.indication)+'</div>';
  for(const s of f.sections||[]){h+='<h4>'+esc(s.titre)+'</h4>'+(s.texte?para(s.texte):'')+tableau(s.tableau)+(s.algorithme?algo(s.algorithme):'');}
  for(const g of f.images||[])h+='<figure><img loading="lazy" src="'+esc(D.base+g.fichier)+'" alt="'+esc(g.legende)+'"><figcaption>'+esc(g.legende)+' — '+esc(g.source||'')+'</figcaption></figure>';
  if(f.sources)h+='<h4>Sources</h4><ol class="src">'+f.sources.map(s=>'<li>'+esc(s)+'</li>').join('')+'</ol>';
  return h+'</div>';}
function ouvrirFiche(id,titre){$('#ft').textContent=titre;$('#fc').innerHTML=fiche(id);$('#fc').scrollTop=0;$('#fv').classList.add('a');document.body.style.overflow='hidden';history.pushState({f:id},'','#fiche='+id);}
function fermerFiche(){$('#fv').classList.remove('a');document.body.style.overflow='';}
$('#fr').onclick=()=>history.back();$('#fc').onclick=e=>{const c=e.target.closest('.cas>button');if(c)c.parentElement.classList.toggle('o')};
function nbFiches(n){return (n.fiche&&D.fiches[n.fiche]?1:0)+(n.enfants||[]).reduce((a,x)=>a+nbFiches(x),0);}
function nbFeuilles(n){return (n.enfants&&n.enfants.length)?n.enfants.reduce((a,x)=>a+nbFeuilles(x),0):1;}
function branche(n){const feuille=!(n.enfants&&n.enfants.length);
  return '<li><button type="button" aria-expanded="false" class="'+(feuille?'fe':'')+'"'+(feuille?' data-fiche="'+esc(n.fiche||n.id)+'"':'')+'>'+esc(n.titre)+(n.aide?' <small>— '+esc(n.aide)+'</small>':'')+(feuille?'':' <small>('+nbFiches(n)+'/'+nbFeuilles(n)+')</small>')+'</button>'+(feuille?'<ul></ul>':'<ul>'+n.enfants.map(branche).join('')+'</ul>')+'</li>';}
function monter(racine,arbre){const el=$(racine);if(!arbre.onglets.length){el.innerHTML='<p class="vide">Structure en préparation.</p>';return}
  el.innerHTML='<div class="so n2">'+arbre.onglets.map((o,i)=>'<button data-i="'+i+'"'+(i?'':' class="a"')+'>'+esc(o.titre)+'</button>').join('')+'</div><div class="corps"></div>';
  const montrer=i=>{const o=arbre.onglets[i];$$('.so button',el).forEach(b=>b.classList.toggle('a',+b.dataset.i===i));
    $('.corps',el).innerHTML=(o.intro?'<p class="sous">'+esc(o.intro)+'</p>':'')+'<ul class="arb">'+(o.enfants||[]).map(branche).join('')+'</ul>';};
  el.onclick=e=>{const b=e.target.closest('.so button');if(b)return montrer(+b.dataset.i);
    const c=e.target.closest('.cas>button');if(c)return c.parentElement.classList.toggle('o');
    const a=e.target.closest('.arb button');if(!a)return;const li=a.parentElement,o=li.classList.toggle('o');a.setAttribute('aria-expanded',o);
    if(a.dataset.fiche){li.classList.remove('o');a.setAttribute('aria-expanded',false);ouvrirFiche(a.dataset.fiche,a.textContent)}};
  montrer(0);}
monter('#p-examens .arbre',D.examens);monter('#p-pharmaco .arbre',D.pharmaco);
/* ----- Lien profond ----- */
const h=location.hash.slice(1);if(h.startsWith('cours=')){const i=liste.findIndex(x=>x.l.id===h.slice(6));if(i>=0){history.replaceState(null,'','#cours');ouvrir(i)}}else if(['examens','pharmaco'].includes(h))onglet(h);
"""


def rendre(a):
    C = json.load(open(a.carte, encoding='utf-8')) if a.carte and os.path.exists(a.carte) else {'lecons': {}}
    L = C.get('lecons', {})
    cat = {int(r['lot']): (r['code'], r['ssp_profiles_2023_fr_en'].split('|')[0].strip()) for r in csv.DictReader(open(a.catalogue, encoding='utf-8'))}
    prets = plage(a.audites)
    ssp, cartes, n_cours = [], [], 0
    for lot in range(1, 249):
        code, nom = cat.get(lot, ('', f'SSP {lot}'))
        noms, graves = noms_dx(lot)
        rows = [L.get(f'{lot:03d}:{l}') for l in LECONS]
        if lot in prets:
            p = 100
        elif L:
            p = min(95, round(sum(r['score'] if r else 0 for r in rows) / 11))
        else:  # sans carte : part des onze fichiers déjà présents, plafonnée (rien n'est audité)
            p = round(40 * sum(os.path.exists(fichier(lot, l)) for l in LECONS) / 11)
        lecons, items = [], []
        for l in LECONS:
            n = 'Vue d\'ensemble : démarche devant ce motif, dix diagnostics comparés' if l == 'A' else noms.get(l, f'Diagnostic {l[2:]} (nom à venir)')
            f = fichier(lot, l)
            ok = lot in prets and os.path.exists(f)
            n_cours += ok
            lecons.append({'id': f'{code}-{l}'.replace('.', '_'), 'n': n if l != 'A' else f'{nom} — vue d\'ensemble', 'f': f if ok else None})
            drap = '<b class="g" aria-label="diagnostic grave">🚩</b>' if graves.get(l) else ''
            cls = ' class="mono"' if l == 'A' else ''
            items.append(f'<li>{"<a href=\"" + E(a.base + f) + "\" data-c=\"" + E(lecons[-1]["id"]) + "\" data-n=\"" + E(n.lower()) + "\">" if ok else "<span data-n=\"" + E(n.lower()) + "\">"}{drap}<span{cls}>{E(n)}</span>{"</a>" if ok else "</span>"}</li>')
        ssp.append({'code': code, 'nom': nom, 'lecons': lecons})
        recherche = E((nom + ' ' + code + ' ' + ' '.join(noms.values())).lower())
        cartes.append(
            f'<article class="c{" pret" if lot in prets else ""}" data-t="{recherche}"><div class="code">{E(code)}{" · prêt" if lot in prets else ""}</div><h2>{E(nom)}</h2>'
            f'<div class="j"><div class="t"><div class="f" style="--p:{p}%;--h:{round(1.2 * p)}"></div></div><span>{p} %</span></div>'
            f'<details{" open" if lot in prets and len(prets) <= 3 else ""}><summary>{"Ouvrir les cours" if lot in prets else "Diagnostics prévus"}</summary><ul class="ls">{"".join(items)}</ul></details></article>')
    donnees = {'base': a.base, 'ssp': ssp, 'examens': arbre(os.path.join(a.reference, 'examens.json')), 'pharmaco': arbre(os.path.join(a.reference, 'pharmaco.json')),
               'fiches': fiches(os.path.join(a.reference, 'fiches'))}
    maj = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).strftime('%d.%m.%Y %H:%M')
    doc = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Progression — Examen fédéral de médecine humaine</title><style>{CSS}</style></head><body>
<header class="h"><h1>Progression — Examen fédéral</h1><p class="sous">{len(prets)} situations de départ prêtes · {n_cours} cours ouvrables · mise à jour {maj} (Zurich)</p>
<nav class="on"><button data-o="cours" class="a">Cours</button><button data-o="examens">Examens complémentaires</button><button data-o="pharmaco">Pharmacologie</button></nav></header>
<main>
<section class="p a" id="p-cours">
<div class="barre"><input id="q" type="search" placeholder="Chercher un motif ou un diagnostic…" aria-label="Chercher"><button class="pu a" id="fp" type="button">Prêts seulement</button></div>
<div class="grille">{"".join(cartes)}</div></section>
<section class="p" id="p-examens"><p class="sous">Réviser l'interprétation des examens : indication de la demande en rouge, valeurs, raisonnement par cases, images.</p><div class="arbre"></div></section>
<section class="p" id="p-pharmaco"><p class="sous">Du système à la classe, de la classe au chef de file : indications, posologie selon l'information professionnelle suisse, cinétique et dynamique.</p><div class="arbre"></div></section>
</main>
<div id="vue" role="dialog" aria-label="Cours"><div class="tete"><button id="vr" type="button" aria-label="Retour à la liste">←</button><b id="vt"></b><button id="vp" type="button" aria-label="Cours précédent">‹</button><button id="vs" type="button" aria-label="Cours suivant">›</button><a class="x" id="vn" target="_blank" rel="noopener" aria-label="Ouvrir dans un nouvel onglet">↗</a></div><iframe id="vf" title="Cours" src="about:blank"></iframe></div>
<div id="fv" role="dialog" aria-label="Fiche"><div class="tete"><button id="fr" type="button" aria-label="Retour">←</button><b id="ft"></b></div><div class="corps" id="fc"></div></div>
<script type="application/json" id="donnees">{json.dumps(donnees, ensure_ascii=False).replace("</", "<\\/")}</script>
<script>{JS}</script></body></html>'''
    open(a.sortie, 'w', encoding='utf-8').write(doc)
    return len(prets), n_cours, len(doc.encode())


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--carte', default='')
    ap.add_argument('--catalogue', default='LOT_Claude_Finaux/CATALOGUE_248.csv')
    ap.add_argument('--audites', default='', help='SSP audités et fusionnés, par numéro de LOT : 1-16,18')
    ap.add_argument('--reference', default='Claude/_reference')
    ap.add_argument('--base', default='', help='préfixe des liens vers les cours (vide : relatif à la page)')
    ap.add_argument('--sortie', default='progression.html')
    a = ap.parse_args()
    print('%d SSP prêts, %d cours ouvrables, %d octets' % rendre(a))
