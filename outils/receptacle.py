#!/usr/bin/env python3
"""RÉCEPTACLE — progression.html : page d'accueil unique du projet (ordre de Vial du 11.11.2026), zéro modèle.

Quatre onglets (cahier d'architecture v2 du 13.11.2026, Claude/_progression/CAHIER_ARCHITECTURE_v2.md) :
  1. Cours — une carte par SSP, nommée par le nom véritable du SSP (jamais « LOT ») ; chaque leçon porte le nom de son
     diagnostic (jamais « DX.n ») ; un clic ouvre le cours DANS la page (visionneuse plein écran, retour arrière du
     téléphone compris). Seuls les SSP audités et fusionnés (--audites) sont ouvrables ; les autres montrent leur jauge.
  2. Examens paracliniques — 9 sous-onglets, entrée primaire puis axe secondaire (partie 5, cartographie partie 7).
  3. Pharmacologie — S1–S12 + T ; chaîne Normal → VITE DIT CAFé → pathologie → traitement → classe → molécule ;
     S11 : coque CIM-10 (vue CIM-10 et vue par âge), classes avec matrice profil → chef de file.
  4. Sciences fondamentales — par système et transversaux (partie 6).
Source de vérité des onglets 2 à 4 : Claude/_progression/donnees/ (un fichier JSON par fiche, généré par
Claude/_progression/charpente.py, contrôlé par controle.py). Le script assemble ces fichiers dans la page ; un champ
égal au gabarit (« — ») n'est pas recopié : la page le reconstruit depuis gabarits.json.
Forme (partie 0.6) : Atkinson Hyperlegible, ≈ 15 px, colonne ≤ 760 px, rail vertical + sommaire latéral numéroté,
une seule fenêtre ouverte, contraste ≥ 7:1, fond blanc, couleurs à sens fixe.

Usage : python3 outils/receptacle.py --audites 1-32 --sortie progression.html [--carte carte.json] [--base ./]
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



def progression(dossier):
    """Assemble structure, gabarits et fiches ; chaque fiche est allégée des champs encore égaux à son gabarit."""
    lire = lambda p: json.load(open(p, encoding='utf-8'))
    if not os.path.exists(os.path.join(dossier, 'structure.json')):
        return {'S': None, 'G': {}, 'F': {}}
    G = lire(os.path.join(dossier, 'gabarits.json'))
    F = {}
    for p in sorted(glob.glob(os.path.join(dossier, '*', '*.json'))):
        try:
            f = lire(p)
        except ValueError:
            continue
        g = G.get(f.get('type'), {})
        F[f['id']] = {k: v for k, v in f.items() if k not in g or g[k] != v}
    return {'S': lire(os.path.join(dossier, 'structure.json')), 'G': G, 'F': F}


POLICE = ''.join("@font-face{font-family:'Atkinson Hyperlegible';font-style:%s;font-weight:%s;font-display:swap;src:url('BASEClaude/_polices/atkinson-hyperlegible-latin-%s-%s.woff2') format('woff2')}" % (s, w, w, s) for w in ('400', '700') for s in ('normal', 'italic'))

CSS = """
:root{--fond:#fff;--carte:#fff;--encre:#111;--doux:#4a4a4a;--trait:#d5d9e0;--piste:#e9ecf1;--acc:#7f3a20;--rouge:#9e0b14;--vert:#1b5e20;
--bleu:#0a3a8c;--violet:#5b2387;--ocre:#6b4800;--orange:#8f3a00;--survol:#f3f5f9}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;background:#fff}body{margin:0;background:#fff;color:var(--encre);font:15px/1.45 "Atkinson Hyperlegible",Verdana,system-ui,sans-serif}
button,input{font-family:inherit}
header.h{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--trait);padding:10px 14px 0}
h1{font-size:1.15rem;margin:0 0 2px}.sous{color:var(--doux);font-size:.87rem;margin:0 0 8px}
nav.on{display:flex;gap:4px;overflow-x:auto;scrollbar-width:none}nav.on::-webkit-scrollbar{display:none}
nav.on button{font:inherit;border:0;background:none;color:var(--doux);padding:9px 12px;border-bottom:3px solid transparent;white-space:nowrap;cursor:pointer}
nav.on button.a{color:var(--encre);font-weight:700;border-color:var(--acc)}
main{max-width:1240px;margin:0 auto;padding:14px}
section.p{display:none}section.p.a{display:block}
.barre{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:0 0 12px}
.barre input{flex:1 1 220px;font:inherit;padding:10px 12px;border:1px solid var(--trait);border-radius:10px;background:#fff}
.pu{font:inherit;border:1px solid var(--trait);background:#fff;border-radius:999px;padding:7px 13px;cursor:pointer;color:var(--encre)}.pu.a{background:var(--encre);color:#fff;border-color:var(--encre)}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.c{background:#fff;border:1px solid var(--trait);border-radius:14px;padding:12px 14px}
.c h2{font-size:1rem;margin:0 0 2px;line-height:1.25}.c .code{color:var(--doux);font-size:.8rem;font-weight:700;letter-spacing:.02em}
.c.pret{border-left:5px solid var(--vert)}
.j{display:grid;grid-template-columns:1fr 44px;align-items:center;gap:8px;margin:6px 0}.j span{font-size:.8rem;font-weight:700;text-align:right}
.t{height:8px;background:var(--piste);border-radius:99px;overflow:hidden}.f{height:100%;width:var(--p);border-radius:inherit;background:hsl(var(--h) 60% 34%)}
details summary{cursor:pointer;color:var(--doux);font-size:.87rem;padding:4px 0}
.ls{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:2px}
.ls a,.ls span{display:flex;gap:8px;align-items:baseline;padding:8px 8px;border-radius:8px;text-decoration:none;color:var(--encre);font-size:.93rem;line-height:1.3}
.ls a{background:#fff;border:1px solid var(--trait)}.ls a:active,.ls a:hover{background:var(--survol)}.ls span{color:var(--doux)}
.ls .g{color:var(--rouge);font-weight:700;flex:none}.ls .mono{font-weight:700}
.vide{color:var(--doux);font-size:.93rem;padding:4px 0;margin:0}
#vue{position:fixed;inset:0;z-index:20;background:#fff;display:none;flex-direction:column}#vue.a{display:flex}
#vue .tete{display:flex;gap:6px;align-items:center;padding:6px 8px;border-bottom:1px solid var(--trait);background:#fff}
#vue .tete b{flex:1;min-width:0;font-size:.87rem;line-height:1.2;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
#vue .tete small{display:block;color:var(--doux);font-weight:400}
#vue button,#vue a.x{font:inherit;border:1px solid var(--trait);background:#fff;border-radius:9px;padding:8px 11px;cursor:pointer;color:var(--encre);text-decoration:none;flex:none}
#vue iframe{flex:1;border:0;width:100%}
/* ----- Modules : rail vertical + sommaire latéral numéroté + colonne ≤ 760 px ----- */
.mod{display:grid;grid-template-columns:188px 220px minmax(0,760px);gap:18px;justify-content:center;align-items:start}
.rail,.somm{position:sticky;top:96px;max-height:calc(100vh - 110px);overflow:auto}
.rail{display:flex;flex-direction:column;gap:2px;border-right:1px solid var(--trait);padding-right:10px}
.rail button{font:inherit;text-align:left;border:0;border-left:3px solid transparent;background:#fff;color:var(--encre);padding:7px 8px;cursor:pointer;display:flex;gap:8px;align-items:baseline;border-radius:0 8px 8px 0;line-height:1.25}
.rail button b{flex:0 0 auto;min-width:2.2em;font-size:.8rem;color:var(--bleu)}.rail button.a{border-left-color:var(--acc);background:var(--survol);font-weight:700}
.somm{font-size:.9rem}.somm p{margin:0 0 6px;font-weight:700;color:var(--doux);font-size:.8rem;text-transform:uppercase;letter-spacing:.08em}
.somm ol{margin:0;padding:0;list-style:none;counter-reset:s}.somm li{counter-increment:s}
.somm a{display:flex;gap:7px;padding:4px 6px;border-radius:6px;color:var(--encre);text-decoration:none;line-height:1.25}.somm a::before{content:counter(s);flex:0 0 1.7em;text-align:right;font-weight:700;color:var(--bleu)}
.somm a:hover{background:var(--survol)}
.col{min-width:0;max-width:760px}.col h2{font-size:1.25rem;margin:0 0 4px}.col h3{font-size:1.05rem;margin:18px 0 6px;display:flex;gap:8px;align-items:baseline}
.col h3 .num{color:var(--bleu);min-width:1.6em}.col h4{font-size:.9rem;margin:8px 0 2px;color:var(--doux)}
.meta{color:var(--doux);font-size:.87rem;margin:0 0 8px}.meta b{color:var(--encre)}
.bas{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}
.lf{list-style:none;margin:0;padding:0;display:grid;gap:3px}
.lf button,.lien{font:inherit;text-align:left;width:100%;border:1px solid var(--trait);background:#fff;border-radius:8px;padding:7px 10px;cursor:pointer;color:var(--encre);line-height:1.3}
.lf button:hover,.lien:hover{background:var(--survol)}.lf small,.lien small{color:var(--doux);font-size:.8rem;margin-left:6px;overflow-wrap:anywhere}
.lien{display:inline;width:auto;padding:1px 6px;border-radius:6px}
.etq{font-size:.78rem;border:1px solid var(--trait);border-radius:99px;padding:0 6px;margin-left:4px;color:var(--doux)}
/* Couleurs à sens fixe (partie 0.6) */
.c-bleu{color:var(--bleu)!important}.c-rouge{color:var(--rouge)!important}.c-vert{color:var(--vert)!important}.c-violet{color:var(--violet)!important}.c-ocre{color:var(--ocre)!important}.c-orange{color:var(--orange)!important}
.k-bleu{border-left:4px solid var(--bleu)!important}.k-rouge{border-left:4px solid var(--rouge)!important}.k-vert{border-left:4px solid var(--vert)!important}.k-violet{border-left:4px solid var(--violet)!important}.k-ocre{border-left:4px solid var(--ocre)!important}.k-orange{border-left:4px solid var(--orange)!important}
.legende{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:.82rem;margin:0 0 10px}.legende span{font-weight:700}
.chaine{display:flex;flex-wrap:wrap;gap:4px;align-items:center;margin:6px 0 10px;font-size:.87rem}.chaine span{border:1px solid var(--trait);border-radius:8px;padding:3px 8px;font-weight:700}
.lp{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);gap:8px;align-items:start;margin:6px 0}
.lp>.fl{font-weight:700;color:var(--rouge);padding-top:6px}.barre-t{display:grid;gap:3px}
.barre-t>*{font:inherit;font-size:.88rem;text-align:left;border:1px solid var(--trait);background:#fff;border-radius:6px;padding:4px 8px;cursor:help}.barre-t button{cursor:pointer}
.bande{border:1px solid var(--trait);border-radius:10px;padding:8px 10px;margin:8px 0}
.bande>button{font:inherit;font-weight:700;border:0;background:none;padding:0;cursor:pointer;color:var(--encre);text-align:left}
/* Fenêtre unique, occultante */
#fen{position:fixed;inset:0;z-index:30;background:rgba(10,12,16,.62);display:none;align-items:flex-start;justify-content:center;padding:4vh 12px;overflow:auto}#fen.a{display:flex}
#fen .fc{background:#fff;color:var(--encre);width:100%;max-width:760px;border-radius:14px;padding:16px 18px 22px;border-top:5px solid var(--acc)}
#fen .ft{display:flex;gap:8px;align-items:flex-start}#fen .ft h3{flex:1;margin:0;font-size:1.15rem}
#fen .x{font:inherit;border:1px solid var(--trait);background:#fff;border-radius:8px;padding:4px 10px;cursor:pointer}
#fen h4{margin:14px 0 4px;font-size:.98rem;padding-left:8px;border-left:4px solid var(--trait)}
#fen table{border-collapse:collapse;width:100%;font-size:.88rem;margin:2px 0}#fen td,#fen th{border:1px solid var(--trait);padding:5px 6px;vertical-align:top;text-align:left}
#fen th{background:var(--survol);font-weight:700}#fen td.l{width:38%;color:var(--doux)}#fen ul{margin:2px 0;padding-left:1.2em}
.tw{overflow-x:auto}
@media(max-width:900px){.mod{grid-template-columns:minmax(0,1fr);gap:8px}
 .rail,.somm{position:static;max-height:none}.rail{flex-direction:row;overflow-x:auto;border-right:0;border-bottom:1px solid var(--trait);padding:0 0 4px}
 .rail button{white-space:nowrap;border-left:0;border-bottom:3px solid transparent;border-radius:6px 6px 0 0}.rail button.a{border-bottom-color:var(--acc)}
 .somm ol{display:flex;gap:4px;overflow-x:auto;padding-bottom:4px}.somm a{white-space:nowrap;border:1px solid var(--trait)}
 .lp{grid-template-columns:minmax(0,1fr)}.lp>.fl{display:none}}
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
addEventListener('popstate',e=>{if(e.state&&e.state.c!=null&&location.hash.startsWith('#cours='))ouvrir(e.state.c,false);else if($('#vue').classList.contains('a'))fermer()});
document.addEventListener('click',e=>{const a=e.target.closest('a[data-c]');if(a){e.preventDefault();ouvrir(liste.findIndex(x=>x.l.id===a.dataset.c))}});
function filtrer(){const q=$('#q').value.trim().toLowerCase(),pret=$('#fp').classList.contains('a');
  $$('#p-cours .c').forEach(c=>{const t=c.dataset.t;const ok=(!pret||c.classList.contains('pret'))&&(!q||t.includes(q));c.style.display=ok?'':'none';
    if(q&&ok)c.querySelector('details').open=$$('.ls [data-n]',c).some(x=>x.dataset.n.includes(q))});}
$('#q').oninput=filtrer;$('#fp').onclick=e=>{e.target.classList.toggle('a');filtrer()};filtrer();
/* ----- Arbres (examens, pharmacologie) ----- */
/* ----- Modules du cahier d'architecture v2 (données : Claude/_progression/donnees) ----- */
const S=D.prog.S,G=D.prog.G,F=D.prog.F,V='—';
const clone=x=>JSON.parse(JSON.stringify(x));
function fi(id){const f=F[id];if(!f)return null;return Object.assign(clone(G[f.type]||{}),f);}
const LBL={nom_exact:'Nom exact',synonymes:'Synonymes',prelevement_conditions:'Prélèvement ou conditions',bon_usage_suisse:'Bon usage suisse (Liste des analyses, Smarter Medicine, dose d\'irradiation OFSP)',
 urgence_aigu:'Urgence, aigu',diagnostic_etiologie:'Diagnostic, étiologie',depistage_pretherapeutique:'Dépistage, pré-thérapeutique',suivi_surveillance:'Suivi, surveillance',ne_pas_demander:'Ne pas demander',
 seuil_alerte:'Seuil d\'alerte',entite_anormale_chiffree:'1 Entité anormale chiffrée',associees_presentes:'2 Associées : présentes',associees_a_rechercher:'2 Associées : à rechercher',
 syndrome_anamnese:'3 Syndrome : anamnèse',syndrome_status:'3 Syndrome : status',confirmation:'4 Confirmation',diagnostic:'4 Diagnostic',conduite:'4 Conduite',si:'Si…',consequence:'→ conséquence pour le patient',alors:'→ alors',
 mnemotechnique:'Mnémotechnique',lignes:'Lignes',trajet:'Trajet de ce qui circule',stations:'Stations',structure:'Structure traversée',structure_fonction:'Structure-fonction locale',si_dereglement:'Si elle se dérègle',
 vite_dit_cafe:'Altérations · VITE DIT : CAFé',nom:'Nom',station:'Station',traitement:'Traitement complet',systeme:'Médicament du système (clic)',hors_systeme:'Hors système (survol : posologie complète)',
 non_medicamenteux:'Non médicamenteux (survol)',classe_biochimique:'Classe biochimique',classe_fonctionnelle:'Classe fonctionnelle',dci:'DCI',marque:'Marque®',cible:'Cible',posologie_complete:'Posologie complète',
 procedure:'Procédure',indications:'Indications',contre_indications:'Contre-indications',classification_fonctionnelle:'Classification fonctionnelle',sous_classe:'Sous-classe',quand_la_choisir:'Quand la choisir',
 chefs_de_file:'Chefs de file suisses',profil:'Profil clinique dominant',chef_de_file:'Chef de file préféré',pourquoi:'Pourquoi (mécanisme, effet recherché)',a_eviter_pourquoi:'À éviter et pourquoi',
 pourquoi_elle:'Pourquoi elle',spectre:'Spectre',pk:'PK · A-D-M-E',absorption:'A Absorption',distribution:'D Distribution',metabolisme:'M Métabolisme',elimination:'E Élimination',courbe_commentee:'Courbe commentée',
 pd:'PD',mecanisme:'Mécanisme',profil_receptoriel:'Profil réceptoriel',effets_indesirables_par_recepteur:'Effets indésirables par récepteur',recepteur:'Récepteur',effet:'Effet',posologie:'Posologie',
 adulte:'Adulte',sujet_age:'Sujet âgé',enfant:'Enfant',adolescent:'Adolescent',sexe:'Sexe',ir_dfg:'IR (par DFG)',ih_child_pugh:'IH (Child-Pugh)',grossesse:'Grossesse',allaitement:'Allaitement',pieges:'Pièges « si → alors »',
 source:'Source',sources:'Sources',delai_titration:'Délai d\'action et titration',delai_action:'Délai d\'action',titration:'Titration',performance_par_profil:'Performance par profil clinique (matrice 4.4)',
 arret_sevrage_switch:'Arrêt, sevrage et changement',schema_arret:'Schéma d\'arrêt',syndrome_arret:'Syndrome d\'arrêt',switch:'Changement (switch)',surveillance:'Surveillance',biologie:'Biologie',ecg_qt:'ECG (QT)',
 poids_metabolique:'Poids et métabolique',taux_plasmatique:'Taux plasmatique',posologie_par_age:'Posologie par âge',autorisation_suisse_par_age:'Autorisation suisse par âge',
 criteres_cim10:'Critères CIM-10 (survol)',criteres_principaux:'Critères principaux',criteres_associes:'Critères associés',nombre_requis:'Nombre requis',duree:'Durée',specifications:'Spécifications',severite:'Sévérité',
 syndrome_somatique:'Syndrome somatique',symptomes_psychotiques:'Symptômes psychotiques',exclusions:'Exclusions',termes_discriminants:'Termes discriminants (gras)',texte_source:'Texte source',complement_recherche:'Complément : critères pour la recherche (signalé)',
 barre_traitement:'Barre de traitement',psychotherapies_mesures:'Psychothérapies et mesures (survol)',type:'Type',indication:'Indication',pharmacologie_psychiatrique:'Pharmacologie psychiatrique (clic)',
 hors_psychiatrie:'Hors psychiatrie (survol : posologie complète)',mesures_legales_sociales:'Mesures légales ou sociales (survol)',ages:'Vue par âge',presente:'Se présente à cet âge',ce_que_lage_change:'Ce que l\'âge change',
 pathologies:'Pathologies',rubriques:'Rubriques',cadre_ensemble:'Cadre d\'ensemble',entites:'Entités',liens_logiques:'Liens logiques',ponts_cliniques:'Ponts cliniques',classes:'Classes',bandes:'Bandes par sous-classe',
 matrice_profil_chef_de_file:'Matrice profil clinique → chef de file',coque:'Coque',justification_coque:'Justification (une ligne)',nombre_stations:'Nombre de stations',normal:'Normal'};
const COUL={normal:'bleu',trajet:'bleu',stations:'bleu',structure_fonction:'bleu',temps2_examen:'bleu',pathologies:'rouge',vite_dit_cafe:'rouge',si_dereglement:'rouge',anomalie:'rouge',criteres_cim10:'rouge',
 systeme:'vert',classes:'vert',bandes:'vert',pharmacologie_psychiatrique:'vert',hors_systeme:'violet',hors_psychiatrie:'violet',non_medicamenteux:'ocre',psychotherapies_mesures:'ocre',mesures_legales_sociales:'ocre',
 ne_pas_demander:'orange',seuil_alerte:'orange',annexeA_pieges:'orange',pieges:'orange'};
const lbl=k=>LBL[k]||(k.charAt(0).toUpperCase()+k.slice(1)).replace(/_/g,' ');
const lienF=id=>F[id]?'<button type="button" class="lien" data-f="'+esc(id)+'">'+esc(fi(id).titre)+'<small>'+esc(id)+'</small></button>':esc(id);
function val(v,k,t2){
  if(v==null)return esc(V);
  if(typeof v==='string'||typeof v==='number')return F[v]?lienF(v):esc(v);
  if(Array.isArray(v)){if(!v.length)return esc(V);
    if(typeof v[0]!=='object')return v.length===1?val(v[0]):'<ul>'+v.map(x=>'<li>'+val(x)+'</li>').join('')+'</ul>';
    const ks=Object.keys(v[0]).filter(x=>x!=='vite_dit_cafe'&&x!=='traitement');
    let h='<div class="tw"><table><tr>'+ks.map(x=>'<th class="'+(COUL[x]?'c-'+COUL[x]:'')+'">'+esc(t2&&t2[x]||lbl(x))+'</th>').join('')+'</tr>'+v.map(r=>'<tr>'+ks.map(x=>'<td>'+val(r[x],x)+'</td>').join('')+'</tr>').join('')+'</table></div>';
    v.forEach((r,i)=>{if(r.vite_dit_cafe)h+='<h4 class="k-rouge c-rouge">Station '+esc(r.n||i+1)+' · '+lbl('vite_dit_cafe')+'</h4>'+val(r.vite_dit_cafe);
      if(r.traitement)h+='<h4 class="k-vert">'+lbl('traitement')+' : '+esc(r.nom)+'</h4>'+val(r.traitement);});
    return h;}
  return '<table>'+Object.entries(v).map(([a,b])=>'<tr><td class="l '+(COUL[a]?'c-'+COUL[a]:'')+'">'+esc(lbl(a))+'</td><td>'+val(b,a)+'</td></tr>').join('')+'</table>';}
const BLOCS={examen:[['entete','En-tête'],['temps1_indications','Temps 1 · Indications'],['temps2_examen','Temps 2 · L\'examen — un paramètre lu seul'],
  ['temps3_interpretation','Temps 3 · Interprétation — plusieurs anomalies associées'],['annexeA_pieges','Annexe A · Pièges'],['sources','Sources']]};
const META=['id','module','type','titre','sous_onglet','systeme','etiquettes','entree_primaire','axe_secondaire','passerelles','classe','sous_classe','bloc','code_cim10'];
function rendreFiche(id){const f=fi(id);if(!f)return '<p class="vide">Identifiant absent : '+esc(id)+'</p>';
  const so=f.sous_onglet?S.examens[f.sous_onglet-1]:null;
  let h='<p class="meta"><b>'+esc(f.id)+'</b> · '+esc(f.systeme)+' '+esc((S.systemes.find(s=>s.code===f.systeme)||{}).nom||'')+(f.etiquettes&&f.etiquettes.length?' · étiquettes '+f.etiquettes.map(e=>'<span class="etq">'+esc(e)+'</span>').join(''):'')+'</p>';
  if(so)h+='<p class="meta">Sous-onglet '+so.n+' · '+esc(so.titre)+' · '+esc(so.entree_primaire)+' : <b>'+esc(f.entree_primaire.join(', '))+'</b> · '+esc(so.axe_secondaire)+' : <b>'+esc(f.axe_secondaire.join(', '))+'</b></p>';
  if(f.classe)h+='<p class="meta">Classe : '+lienF(f.classe)+' · sous-classe <b>'+esc(f.sous_classe)+'</b></p>';
  if(f.bloc)h+='<p class="meta">Bloc CIM-10 : '+lienF(f.bloc)+'</p>';
  const ordre=BLOCS[f.type]||Object.keys(f).filter(k=>!META.includes(k)).map(k=>[k,lbl(k)]);
  for(const [k,t] of ordre){if(!(k in f))continue;const c=COUL[k];
    const t2=k==='temps2_examen'&&so?{parametre:so.temps2[0],normal:so.temps2[1],anomalie:so.temps2[2]}:null;
    h+='<h4 class="'+(c?'k-'+c+' c-'+c:'')+'">'+esc(t)+'</h4>'+val(f[k],k,t2);}
  h+='<h4>Annexe B · Passerelles</h4>'+(f.passerelles.length?'<div class="tw"><table><tr><th>Type</th><th>Fiche cible</th><th>Pourquoi</th></tr>'+f.passerelles.map(p=>'<tr><td>'+esc(p.type)+'</td><td>'+lienF(p.cible)+'</td><td>'+esc(p.pourquoi)+'</td></tr>').join('')+'</table></div>':'<p class="vide">—</p>');
  return h;}
/* Une seule fenêtre ouverte : ouvrir une fiche remplace la précédente. */
function ouvrirF(id){const f=fi(id);if(!f)return;$('#fen .ft h3').textContent=f.titre;$('#fen .fb').innerHTML=rendreFiche(id);$('#fen').classList.add('a');$('#fen').scrollTop=0;
  document.body.style.overflow='hidden';history.replaceState(null,'','#f='+encodeURIComponent(id));$('#fen .x').focus();}
function fermerF(){$('#fen').classList.remove('a');document.body.style.overflow='';const o=$('nav.on button.a');history.replaceState(null,'','#'+(o?o.dataset.o:''));}
$('#fen').onclick=e=>{if(e.target.id==='fen'||e.target.closest('#fen .x'))fermerF()};
addEventListener('keydown',e=>{if(e.key==='Escape'&&$('#fen').classList.contains('a'))fermerF()});
document.addEventListener('click',e=>{const b=e.target.closest('[data-f]');if(b){e.preventDefault();ouvrirF(b.dataset.f)}});
const btnF=id=>{const f=fi(id);return '<li><button type="button" data-f="'+esc(id)+'">'+esc(f.titre)+(f.etiquettes&&f.etiquettes.length?f.etiquettes.map(e=>'<span class="etq">'+esc(e)+'</span>').join(''):'')+'<small>'+esc(id)+'</small></button></li>'};
const listeF=ids=>ids.length?'<ul class="lf">'+ids.map(btnF).join('')+'</ul>':'<p class="vide">—</p>';
const nomSys=c=>(S.systemes.find(s=>s.code===c)||{}).nom||c;
const LEG='<div class="legende"><span class="c-bleu">bleu normal</span><span class="c-rouge">rouge pathologie</span><span class="c-vert">vert traitement du système</span><span class="c-violet">violet hors système</span><span class="c-ocre">ocre non médicamenteux</span><span class="c-orange">orange danger</span></div>';
/* Gabarit commun : rail (racine) → sommaire numéroté → colonne. */
function module(sel,rail,corps){const el=$(sel);
  el.innerHTML='<div class="mod"><nav class="rail" aria-label="Rail">'+rail.map((r,i)=>'<button type="button" data-r="'+i+'"><b>'+esc(r.n)+'</b><span>'+esc(r.t)+'</span></button>').join('')+'</nav><nav class="somm" aria-label="Sommaire"><p>Sommaire</p><ol></ol></nav><div class="col"></div></div>';
  const montrer=(i,opt)=>{$$('.rail button',el).forEach(b=>b.classList.toggle('a',+b.dataset.r===i));const r=corps(i,opt||{});$('.col',el).innerHTML=r.h;
    $('.somm ol',el).innerHTML=r.s.map(([id,t])=>'<li><a href="#'+id+'" data-s="'+id+'">'+esc(t)+'</a></li>').join('');el.dataset.i=i;};
  el.addEventListener('click',e=>{const r=e.target.closest('.rail button');if(r)return montrer(+r.dataset.r);
    const s=e.target.closest('[data-s]');if(s){e.preventDefault();const c=document.getElementById(s.dataset.s);if(c)c.scrollIntoView({block:'start'});return}
    const v=e.target.closest('[data-vue]');if(v)return montrer(+el.dataset.i,{vue:v.dataset.vue});});
  montrer(0);return montrer;}
/* Examens paracliniques : 9 sous-onglets, entrée primaire puis axe secondaire. */
function corpsEx(i,o){const so=S.examens[i];const parSys=so.entree_primaire.startsWith('Système');const vue=o.vue||(parSys?'prim':'prim');
  const toutes=so.systemes.flatMap(s=>s.fiches);
  let entrees;
  if(parSys||vue==='sys')entrees=so.systemes.map(s=>({k:s.code,t:s.code+' · '+s.nom,ids:s.fiches}));
  else{entrees=so.valeurs_primaires.map(v=>({k:v,t:v,ids:toutes.filter(id=>fi(id).entree_primaire.includes(v))}));
    entrees.push({k:'na',t:'— (à attribuer)',ids:toutes.filter(id=>fi(id).entree_primaire.includes(V))});}
  let h='<h2>'+so.n+' · '+esc(so.titre)+'</h2><p class="meta">Entrée primaire : <b>'+esc(so.entree_primaire)+'</b> · axe secondaire : <b>'+esc(so.axe_secondaire)+'</b> ('+esc(so.valeurs_axe.join(', '))+') · unité de fiche : '+esc(so.unite)+' · '+toutes.length+' emplacements</p>';
  if(!parSys)h+='<div class="bas"><button type="button" class="pu'+(vue!=='sys'?' a':'')+'" data-vue="prim">Par '+esc(so.entree_primaire.toLowerCase())+'</button><button type="button" class="pu'+(vue==='sys'?' a':'')+'" data-vue="sys">Par système</button></div>';
  h+=LEG;
  entrees.forEach((en,j)=>{const id='ex'+so.n+'-'+j;h+='<h3 id="'+id+'"><span class="num">'+(j+1)+'</span>'+esc(en.t)+'</h3>';
    if(!en.ids.length){h+='<p class="vide">—</p>';return}
    const axes=[...so.valeurs_axe,V];axes.forEach(a=>{const ids=en.ids.filter(x=>fi(x).axe_secondaire.includes(a));if(ids.length)h+='<h4>'+esc(so.axe_secondaire)+' : '+esc(a===V?'— (à attribuer)':a)+'</h4>'+listeF(ids)});});
  return {h,s:entrees.map((en,j)=>['ex'+so.n+'-'+j,en.t])};}
/* Pharmacologie : S1–S12 + T ; S11 à gabarit propre. */
const CHAINE='<div class="chaine"><span class="c-bleu">Normal</span>→<span class="c-rouge">Altération (VITE DIT : CAFé)</span>→<span class="c-rouge">Pathologie</span>→<span class="c-vert">Traitement complet</span>→<span class="c-vert">Classe</span>→<span class="c-vert">Molécule</span></div>';
function ligneP(id){const f=fi(id),b=f.barre_traitement;const surv=(x,k)=>esc(lbl(k))+' : '+(Array.isArray(x)?x.map(r=>typeof r==='object'?Object.values(r).join(' · '):r).join(' ; '):x);
  return '<div class="lp"><button type="button" class="lien c-rouge" data-f="'+esc(id)+'" title="'+esc(surv(f.criteres_cim10.criteres_principaux,'criteres_principaux'))+'">'+esc(f.titre)+'</button><span class="fl">➜</span><div class="barre-t">'+
   '<span class="k-ocre" title="'+esc(surv(b.psychotherapies_mesures,'psychotherapies_mesures'))+'">Psychothérapies et mesures (survol)</span>'+
   b.pharmacologie_psychiatrique.map(c=>F[c]?'<button type="button" class="k-vert" data-f="'+esc(c)+'">'+esc(fi(c).titre)+'</button>':'<span class="k-vert">'+esc(c)+'</span>').join('')+
   '<span class="k-violet" title="'+esc(surv(b.hors_psychiatrie,'hors_psychiatrie'))+'">Hors psychiatrie (survol)</span><span class="k-ocre" title="'+esc(surv(b.mesures_legales_sociales,'mesures_legales_sociales'))+'">Mesures légales ou sociales (survol)</span></div></div>';}
function classeHtml(id){const c=fi(id);return '<div class="bande k-vert"><button type="button" data-f="'+esc(id)+'">'+esc(c.titre)+' <small class="etq">'+esc(id)+'</small></button>'+
  c.bandes.map(b=>'<div class="meta">'+esc(b.sous_classe)+' : '+b.chefs_de_file.map(x=>F[x]?lienF(x):esc(x)).join(' ')+'</div>').join('')+'</div>';}
function corpsPh(i,o){const sy=S.pharmaco[i];let h='<h2>'+esc(sy.code)+' · '+esc(sy.nom)+'</h2><p class="meta">Coque : <b>'+esc(sy.coque)+'</b></p>'+LEG,s=[];
  if(sy.code==='S11'){const P=S.psychiatrie,vue=o.vue||'cim';
    h+='<div class="bas"><button type="button" class="pu'+(vue==='cim'?' a':'')+'" data-vue="cim">Vue CIM-10</button><button type="button" class="pu'+(vue==='age'?' a':'')+'" data-vue="age">Vue par âge</button></div>';
    if(vue==='cim')P.blocs.forEach((b,j)=>{const id='ps-'+j;s.push([id,b.code+' · '+b.titre]);
      h+='<h3 id="'+id+'"><span class="num">'+(j+1)+'</span><button type="button" class="lien" data-f="'+esc(b.id)+'">'+esc(b.code)+' · '+esc(b.titre)+'</button></h3>'+(b.pathologies.length?b.pathologies.map(ligneP).join(''):'<p class="vide">— (liste des pathologies à arrêter)</p>');});
    else S.ages.forEach((a,j)=>{const id='age-'+j;s.push([id,a]);h+='<h3 id="'+id+'"><span class="num">'+(j+1)+'</span>'+esc(a)+'</h3>'+
      (P.ages[a].length?P.ages[a].map(p=>ligneP(p)+'<p class="meta">Ce que l\'âge change : '+esc(fi(p).ages[a].ce_que_lage_change)+'</p>').join(''):'<p class="vide">—</p>');});
    const id='ps-cl';s.push([id,'Classes psychiatriques']);h+='<h3 id="'+id+'"><span class="num">'+s.length+'</span>Classes psychiatriques (matrice profil → chef de file)</h3>'+sy.classes.map(classeHtml).join('');
  }else{s.push(['ph-ch','Chaîne']);h+='<h3 id="ph-ch"><span class="num">1</span>Chaîne</h3>'+CHAINE+listeF(sy.chaines);
    s.push(['ph-cl','Classes et molécules']);h+='<h3 id="ph-cl"><span class="num">2</span>Classes et molécules</h3>'+(sy.classes.length?sy.classes.map(classeHtml).join(''):'<p class="vide">—</p>');}
  return {h,s};}
/* Sciences fondamentales : par système, gabarit cadre → entités → liens → ponts cliniques. */
function corpsSF(i){const sy=S.fondamentales[i];return {h:'<h2>'+esc(sy.code)+' · '+esc(sy.nom)+'</h2><p class="meta">Gabarit : cadre d\'ensemble → entités → liens logiques → ponts cliniques</p>'+
  sy.fiches.map((id,j)=>'<h3 id="sf-'+j+'"><span class="num">'+(j+1)+'</span>'+esc(fi(id).titre)+'</h3>'+listeF([id])).join(''),s:sy.fiches.map((id,j)=>['sf-'+j,fi(id).titre])};}
if(S){module('#p-examens',S.examens.map(x=>({n:x.n,t:x.titre})),corpsEx);
  const mPh=module('#p-pharmaco',S.pharmaco.map(x=>({n:x.code,t:x.nom})),corpsPh);
  module('#p-fondamentales',S.fondamentales.map(x=>({n:x.code,t:x.nom})),corpsSF);}
else $$('#p-examens,#p-pharmaco,#p-fondamentales').forEach(x=>x.innerHTML='<p class="vide">Charpente absente : lancer Claude/_progression/charpente.py.</p>');
/* ----- Lien profond ----- */
const h=location.hash.slice(1);if(h.startsWith('cours=')){const i=liste.findIndex(x=>x.l.id===h.slice(6));if(i>=0){history.replaceState(null,'','#cours');ouvrir(i)}}
else if(h.startsWith('f=')&&F[decodeURIComponent(h.slice(2))]){const id=decodeURIComponent(h.slice(2));onglet({examens:'examens',pharmaco:'pharmaco',psychiatrie:'pharmaco',fondamentales:'fondamentales'}[F[id].module]);ouvrirF(id)}
else if(['examens','pharmaco','fondamentales'].includes(h))onglet(h);
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
    donnees = {'base': a.base, 'ssp': ssp, 'prog': progression(a.donnees)}
    n_empl = len(donnees['prog']['F'])
    maj = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).strftime('%d.%m.%Y %H:%M')
    doc = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Progression — Examen fédéral de médecine humaine</title><style>{POLICE.replace('BASE', a.base)}{CSS}</style></head><body>
<header class="h"><h1>Progression — Examen fédéral</h1><p class="sous">{len(prets)} situations de départ prêtes · {n_cours} cours ouvrables · {n_empl} emplacements de fiches · mise à jour {maj} (Zurich)</p>
<nav class="on"><button data-o="cours" class="a">Cours</button><button data-o="examens">Examens paracliniques</button><button data-o="pharmaco">Pharmacologie</button><button data-o="fondamentales">Sciences fondamentales</button></nav></header>
<main>
<section class="p a" id="p-cours">
<div class="barre"><input id="q" type="search" placeholder="Chercher un motif ou un diagnostic…" aria-label="Chercher"><button class="pu a" id="fp" type="button">Prêts seulement</button></div>
<div class="grille">{"".join(cartes)}</div></section>
<section class="p" id="p-examens"></section>
<section class="p" id="p-pharmaco"></section>
<section class="p" id="p-fondamentales"></section>
</main>
<div id="vue" role="dialog" aria-label="Cours"><div class="tete"><button id="vr" type="button" aria-label="Retour à la liste">←</button><b id="vt"></b><button id="vp" type="button" aria-label="Cours précédent">‹</button><button id="vs" type="button" aria-label="Cours suivant">›</button><a class="x" id="vn" target="_blank" rel="noopener" aria-label="Ouvrir dans un nouvel onglet">↗</a></div><iframe id="vf" title="Cours" src="about:blank"></iframe></div>
<div id="fen" role="dialog" aria-modal="true" aria-label="Fiche"><div class="fc"><div class="ft"><h3></h3><button type="button" class="x" aria-label="Fermer la fiche">✕</button></div><div class="fb"></div></div></div>
<script type="application/json" id="donnees">{json.dumps(donnees, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")}</script>
<script>{JS}</script></body></html>'''
    open(a.sortie, 'w', encoding='utf-8').write(doc)
    return len(prets), n_cours, len(doc.encode())


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--carte', default='')
    ap.add_argument('--catalogue', default='LOT_Claude_Finaux/CATALOGUE_248.csv')
    ap.add_argument('--audites', default='', help='SSP audités et fusionnés, par numéro de LOT : 1-16,18')
    ap.add_argument('--reference', default='Claude/_reference', help='ancien chemin (examens.json, pharmaco.json), conservé en lecture seule, non affiché')
    ap.add_argument('--donnees', default='Claude/_progression/donnees', help='source de vérité des onglets Examens, Pharmacologie, Sciences fondamentales')
    ap.add_argument('--base', default='', help='préfixe des liens vers les cours (vide : relatif à la page)')
    ap.add_argument('--sortie', default='progression.html')
    a = ap.parse_args()
    print('%d SSP prêts, %d cours ouvrables, %d octets' % rendre(a))
