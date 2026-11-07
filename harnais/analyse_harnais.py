#!/usr/bin/env python3
"""Génère LOT_Claude_Finaux/ANALYSE_HARNAIS.html (zéro jeton) : historique du routage, failles, banc d'essai, scénario duo.

Entrées : journal/routage.jsonl, audits/*.jsonl, LOT_Claude_Finaux/BANC_ESSAI_LANGUE.json (harnais/banc_essai_langue.py).
Les consommations en jetons viennent de la session du 30.10.2026 (relevé fourni) ; tout le reste est marqué « estimation ».
Usage : python3 harnais/analyse_harnais.py
"""
from __future__ import annotations
import json, sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import routage_miroir as RM  # noqa: E402

RACINE = RM.RACINE
SORTIE = RACINE / "LOT_Claude_Finaux" / "ANALYSE_HARNAIS.html"

# ---- jetons mesurés (relevé de session, LOT_016), en milliers
MES = {
    "redacteurs_B": [523, 605, 674, 483, 601, 588, 538, 620, 539, 508],
    "medicaux_B": [338, 280, 294, 338, 298, 266, 326],
    "conformites_B": [88, 71, 105, 77, 67],
    "medical_A": 477, "conformite_A": 110,
}
EST = {"redacteur_A": 450, "transversale": 400}  # estimations (non relevées)
moy = lambda l: sum(l) / len(l)
BASE = {
    "Rédacteur Phase A": (EST["redacteur_A"], "estimation"),
    "Audit médical Phase A": (MES["medical_A"], "mesuré"),
    "Conformité Phase A": (MES["conformite_A"], "mesuré"),
    "10 rédacteurs Phase B": (sum(MES["redacteurs_B"]), "mesuré (10/10)"),
    "10 audits médicaux Phase B": (moy(MES["medicaux_B"]) * 10, "mesuré 7/10, extrapolé, reprises partielles"),
    "10 conformités Phase B": (moy(MES["conformites_B"]) * 10, "mesuré 5/10, extrapolé"),
    "Passe transversale": (EST["transversale"], "estimation"),
}

# ---- failles : (id, titre, cause, k jetons/LOT min, max, source, correctif, effort)
FAILLES = [
    ("F1", "Ordre de lecture de CLAUDE.md appliqué par chaque sous-agent",
     "CLAUDE.md impose « lis CONTINUATION.md en entier » (74,5 Ko ≈ 21 k jetons) et PROCHAINE_ACTION.md (85,5 Ko ≈ 24 k) ; PROMPT_ULTIME fait 87 Ko ≈ 25 k. Un sous-agent qui obéit relit ≈ 45 k avant de commencer. 32 à 35 lancements par LOT (journal/routage.jsonl).",
     0, 1500, "tailles mesurées ; obéissance des sous-agents = estimation",
     "Ajouter en tête de CLAUDE.md et dans .claude/agents/*.md : « Sous-agent : n'applique pas l'ordre de lecture ; lis seulement ton brief et ton fichier ». Découper CONTINUATION/PROMPT en extraits par rôle (grep ciblé).", "5 min"),
    ("F2", "Rédacteurs Phase B : 568 k jetons pour ≈ 40 k jetons de HTML produit",
     "Un fichier de 135 Ko ≈ 39 k jetons de sortie ; le reste (≈ 93 %) est lecture de sources, essais, réécritures. 10 rédacteurs opus xhigh = 5,7 M, soit 52 % du LOT. Les mêmes sources (OPAS, AIPS, ESC) sont retéléchargées par chaque agent.",
     570, 1400, "568 k mesuré ; gain = estimation 10–25 %",
     "Cache de sources par LOT (dossier daté, lu une fois, extraits texte par script) ; gabarit HTML/CSS/popover fourni (le rédacteur ne rédige que le contenu) ; plafond de WebFetch par agent.", "0,5 j"),
    ("F3", "Audits médicaux repris après coupure",
     "Coupure (limite de 5 h, ≈ 16 agents opus en parallèle) : l'agent repris relit le fichier (≈ 40 k) et reconstruit son contexte (30–60 k). 7 audits sur 10 sont partiels dans le relevé (266–338 k).",
     280, 700, "estimation (4 à 7 reprises par LOT × 70–100 k)",
     "Point de reprise : corrections.jsonl écrit au fil de l'eau, point par point ; brief de reprise « continue au point N » avec `controle_lot.py extraire --points N-14`, jamais relecture entière.", "2 h"),
    ("F4", "Relectures complètes de fichiers de 130–150 Ko",
     "Chaque fichier est lu en entier par le rédacteur, l'auditeur médical, la conformité, puis la passe transversale (11 fichiers ≈ 440 k). Le texte visible ne fait que 78 % du HTML (mesuré sur LOT_015 DX.6) ; le reste est balisage et CSS.",
     150, 450, "78 % mesuré ; reste = estimation",
     "`controle_lot.py extraire --texte` (texte seul, sans CSS ni balises) pour les auditeurs et la passe transversale ; lecture HTML seulement des points à corriger.", "1 h"),
    ("F5", "Parallélisme opus saturant la limite d'usage de 5 h",
     "≈ 16 agents opus simultanés ont atteint la limite une fois. Le total consommé ne baisse pas, mais l'arrêt crée des reprises (F3), des audits partiels et du temps mort.",
     100, 400, "limite atteinte = constat ; coût = estimation",
     "File d'attente : 5 à 6 agents opus au plus ; rédacteurs étalés ; auditeur médical lancé dès qu'un rédacteur finit (déjà le cas) ; marge de 20 % de budget avant une vague.", "30 min"),
    ("F6", "Scratchpad partagé : écrasements entre rédacteurs",
     "Incidents consignés : `scratchpad/dl/opas.txt` écrasé (LOT_016 DX.1) ; script d'extraction écrasé (LOT_013 DX.7). Conséquence : extractions refaites, risque de dose lue dans le mauvais fichier.",
     60, 200, "2 incidents consignés (JOURNAL_DX*.md) ; coût = estimation",
     "Imposer dans le brief `scratchpad/<LOT>_<DX>/` par agent et nom de fichier préfixé ; contrôle `controle_lot.py` des sources citées ↔ extraits.", "10 min"),
    ("F7", "Session principale réveillée par chaque notification CI de la PR #498",
     "Une notification par push ; 531 commits le 30.10 en ≈ 12 h (374 intitulés « en cours »). Chaque réveil recharge le contexte de la session principale.",
     0, 2700, "531 commits mesurés ; coût par tour (5–20 k effectifs) = estimation, très incertain",
     "`unsubscribe_pr_activity` pendant la production ; pousser une fois par LOT ou par vague ; `paths-ignore` sur `lot en cours de production/**` pour le CI de la PR (garder la vérification à la fusion).", "10 min"),
    ("F8", "Hook Stop qui exige un commit",
     "Chaque fin de tour avec des fichiers modifiés renvoie un tour à la session principale (jusqu'à 374 commits « en cours »).",
     0, 1500, "374 commits mesurés ; coût par tour = estimation",
     "Remplacer l'exigence par un hook script zéro jeton (`git add -A && git commit -m auto`) ou la limiter à la fin de vague.", "15 min"),
    ("F9", "Fichiers proches du plafond de 150 Ko : compressions de forme",
     "LOT_013 : 4 fichiers sur 10 au-dessus de 140 Ko (max 149,2) ; LOT_014 : 6 sur 10 (max 144,4). Les raisons de routage citent « compression prioritaire » pour la conformité (6 mentions).",
     100, 300, "tailles mesurées ; coût de compression = estimation",
     "Cible rédacteur 120–135 Ko ; alerte à 140 Ko dans `controle_lot.py`; CSS et fenêtres de gabarit mutualisés.", "1 h"),
    ("F10", "Journal des corrections écrit par le modèle",
     "3 534 lignes (≈ 600 octets ≈ 170 jetons chacune) ; ≈ 150 k jetons de SORTIE par LOT, plus chers que l'entrée.",
     100, 150, "mesuré sur corrections.jsonl ; pondération sortie = estimation",
     "Journal de la conformité produit par différence avant/après (script) ; le modèle n'ajoute que type et gravité pour les corrections médicales.", "0,5 j"),
    ("F11", "Briefs et définitions d'agents répétés",
     "Définitions d'agents 1,5–3,9 Ko et briefs 1,6–3,2 Ko : négligeables (≈ 1–2 k par lancement).",
     20, 60, "tailles mesurées", "Rien à faire avant F1.", "—"),
    ("F12", "Téléchargements et archives à la racine du dépôt",
     "`LOTS_Finaux avec statut-….zip` (25 Mo) à la racine ; fichiers racine de 74–150 Ko (HANDOFF, PROCHAINE_ACTION, ETAT) lus par réflexe.",
     0, 50, "taille mesurée ; jetons = estimation (coût surtout en clone/CI)",
     "Déplacer ou ignorer (`.gitignore`) les archives ; téléchargements dans `scratchpad/`.", "5 min"),
]

RECO = [
    ("1", "Limiter l'ordre de lecture aux sessions principales (F1)", "5 min", "0,3 à 1,5 M jetons/LOT"),
    ("2", "Silence PR #498 pendant la production : désabonnement + un push par vague (F7)", "10 min", "jusqu'à plusieurs M/jour (incertain)"),
    ("3", "Hook de commit automatique à la place du tour exigé (F8)", "15 min", "jusqu'à 1,5 M/jour (incertain)"),
    ("4", "Dossier scratchpad par agent + cache de sources par LOT (F6, F2)", "0,5 j", "0,6 à 1,6 M/LOT"),
    ("5", "Point de reprise des audits + file de 5 à 6 agents opus (F3, F5)", "2 h", "0,4 à 1,1 M/LOT"),
    ("6", "Lecture texte seul pour auditeurs et passe transversale (F4)", "1 h", "0,15 à 0,45 M/LOT"),
    ("7", "audit_langue.py en pré-passe sur chaque fichier ; la conformité ne traite que ses alertes et le jugement (banc d'essai)", "1 h", "20 à 45 % du coût de conformité"),
    ("8", "Journal des corrections de conformité par différence (F10)", "0,5 j", "≈ 0,1 M/LOT sortie"),
    ("9", "Ne pas supprimer la conformité (verdict duo) ; revoir après 2 LOT de mesure", "—", "évite un risque qualité"),
]


def charger_banc() -> dict:
    p = RACINE / "LOT_Claude_Finaux" / "BANC_ESSAI_LANGUE.json"
    return json.loads(p.read_text(encoding="utf8")) if p.is_file() else {}


def hist_svg(data) -> tuple[str, str, str]:
    ev = data["ev"]
    x0, x1 = ev[0]["t"].timestamp(), ev[-1]["t"].timestamp()
    h = 3600
    prem = int(x0 // h + 1) * h
    ticks = [(x, f"{(int(x // h) % 24 + RM.ZURICH) % 24:02d}h") for x in range(prem, int(x1), 2 * h)]
    ser, cpt = defaultdict(list), Counter()
    for e in ev:
        cpt[e["agent"]] += 1
        ser[e["agent"]].append((e["t"].timestamp(), cpt[e["agent"]]))
        ser["total"].append((e["t"].timestamp(), sum(cpt.values())))
    noms = [a for a in RM.AGENTS if a in ser] + ["total"]
    g1 = RM.svg_lignes({n: ser[n] for n in noms}, x0, x1, "décisions cumulées", ticks_x=ticks, couleurs=dict(RM.COUL, total="c5"))
    rep = Counter(e["cle"] for e in ev)
    g2 = RM.svg_barres_h([(k, v, RM.COUL.get(k.split(" · ")[0], "c7")) for k, v in sorted(rep.items(), key=lambda x: -x[1])])
    lots = sorted({e["lot"] for e in ev if e["lot"].startswith("LOT")})
    dur = []
    for lot in lots:
        es = [e for e in ev if e["lot"] == lot]
        dur.append((lot, (es[-1]["t"] - es[0]["t"]).total_seconds() / 3600, "c2"))
    g3 = RM.svg_barres_h(dur, " h", fmt="{:.1f}")
    return RM.legende(noms) + g1, g2, g3


PAGE = """<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Analyse du Harness</title><style>@@CSS@@
header{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap}
nav.onglets{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0;position:sticky;top:0;background:var(--bg);padding:6px 0;z-index:2}
nav.onglets button,.btn{font:inherit;border:1px solid var(--li);background:var(--ca);color:var(--fg);border-radius:8px;padding:8px 12px;cursor:pointer;min-height:40px}
nav.onglets button[aria-selected=true]{background:var(--c2);color:#fff;border-color:var(--c2)}
section.panneau{display:none}section.panneau.actif{display:block}
.bar{height:10px;background:var(--li);border-radius:5px;overflow:hidden;min-width:70px}.bar i{display:block;height:100%;background:var(--c3)}
.bar.v i{background:var(--c4)}.bar.b i{background:var(--c2)}
.src{color:var(--mu);font-size:.78rem}td.w{white-space:normal;min-width:230px}
.sl{display:grid;grid-template-columns:1fr;gap:2px;margin:10px 0}.sl label{display:flex;justify-content:space-between;gap:8px}
input[type=range]{width:100%}.gros{font-size:1.6rem;font-weight:700}.pos{color:var(--c4)}.neg{color:var(--c3)}
.verdict{border-left:4px solid var(--c6);padding:8px 12px;background:var(--ca);margin:10px 0;border-radius:6px}
ol.reco li{margin:6px 0}
</style></head><body><main>
<header><h1>Analyse du Harness — jetons, failles, duo médical</h1><button class="btn" id="theme">Thème</button></header>
<p class="mu">Généré par harnais/analyse_harnais.py (zéro jeton) le @@DATE@@. Chaque chiffre dit sa source : « mesuré » (journaux, relevé de session, git) ou « estimation ».</p>
<nav class="onglets" role="tablist">
<button role="tab" data-p="hist" aria-selected="true">Historique</button><button role="tab" data-p="failles" aria-selected="false">Failles</button>
<button role="tab" data-p="banc" aria-selected="false">Banc d'essai</button><button role="tab" data-p="duo" aria-selected="false">Scénario duo</button>
<button role="tab" data-p="reco" aria-selected="false">Recommandations</button></nav>

<section class="panneau actif" id="hist">
<div class="kpis">@@KPIS@@</div>
<h2>Décisions de routage cumulées</h2><div class="carte">@@G1@@<p class="src">Source : journal/routage.jsonl, mesuré. Axe : heure de Zurich.</p></div>
<h2>Répartition</h2><div class="carte">@@G2@@</div>
<h2>Durée par LOT</h2><div class="carte">@@G3@@<p class="src">Première à dernière décision de routage du LOT, mesuré ; LOT_016 en cours.</p></div>
<h2>Coût de référence d'un LOT (milliers de jetons)</h2><div class="carte"><table>@@BASE@@</table><p class="src">Relevé de session LOT_016 ; lignes « estimation » non relevées.</p></div>
</section>

<section class="panneau" id="failles">
<h2>Carte des failles</h2>
<div><button class="btn" data-tri="max">Tri par coût max</button> <button class="btn" data-tri="min">par coût min</button> <button class="btn" data-tri="id">par numéro</button></div>
<div class="carte"><table id="tf"><thead><tr><th>#</th><th>Faille</th><th>Coût/LOT (k jetons)</th><th></th><th>Cause et chiffres</th><th>Correctif</th><th>Effort</th></tr></thead><tbody></tbody></table></div>
<p class="src">Les fourchettes ne s'additionnent pas (recouvrements). Gains cumulés plausibles : 15 à 35 % du coût d'un LOT, estimation.</p>
</section>

<section class="panneau" id="banc">
<h2>Banc d'essai : audit_langue.py contre l'auditeur de conformité</h2>
<div id="bancc" class="carte"></div>
</section>

<section class="panneau" id="duo">
<h2>Scénario « duo médical » : supprimer la conformité</h2>
<div class="carte">
<div class="sl"><label>Fichiers par LOT <b id="vn"></b></label><input id="n" type="range" min="1" max="11" value="11"><span class="src">11 = Phase A + 10 Phase B (mesuré).</span></div>
<div class="sl"><label>Coût conformité par fichier, jetons Sonnet (k) <b id="vc"></b></label><input id="c" type="range" min="40" max="140" value="@@CONF@@"><span class="src">Mesuré : 67–105 k (moyenne @@CONF@@ k) ; Phase A 110 k.</span></div>
<div class="sl"><label>Surcroît pour l'auditeur médical, jetons Opus (k) <b id="vs"></b></label><input id="s" type="range" min="10" max="150" value="60"><span class="src">Estimation : lire le rapport du script (3–8 k) + appliquer ≈ 38 corrections non mécaniques à ≈ 1,6 k chacune.</span></div>
<div class="sl"><label>Poids d'un jeton Opus / Sonnet <b id="vw"></b></label><input id="w" type="range" min="10" max="30" value="17"><span class="src">Estimation d'après les tarifs publics (≈ 1,67).</span></div>
<div class="sl"><label>Coût total d'un LOT, k jetons <b id="vt"></b></label><input id="t" type="range" min="6000" max="16000" step="100" value="@@TOT@@"><span class="src">Somme de la table Historique (partiellement estimée).</span></div>
</div>
<div class="kpis">
<div class="kpi"><b id="r1"></b><span class="mu">économie brute/fichier (k jetons)</span></div>
<div class="kpi"><b id="r2"></b><span class="mu">économie pondérée/fichier (k éq. Sonnet)</span></div>
<div class="kpi"><b id="r3"></b><span class="mu">économie brute/LOT (k)</span></div>
<div class="kpi"><b id="r4"></b><span class="mu">part du coût du LOT</span></div>
<div class="kpi"><b id="r5"></b><span class="mu">facteur (coût chaîne duo / actuel)</span></div></div>
<div class="verdict" id="vd"></div>
<div class="carte"><b>Ce que le script ne voit pas</b> (banc d'essai, @@RAPPEL@@) :
<ul><li>cohérence Phase A ↔ Phase B, affectation des points, contradictions : @@JUG@@ des corrections de conformité, aucune détection fiable ;</li>
<li>phrases nominales à verbaliser, redites non identiques, reformulations de style : @@STY@@ ; le script n'en attrape qu'une part par le point-virgule et la longueur ;</li>
<li>le script signale ≈ @@FLAGS@@ alertes par fichier pour ≈ @@NC@@ corrections réelles : sans tri, l'auditeur médical lirait du bruit.</li></ul>
<p><b>Verdict.</b> La conformité pèse ≈ 8 % du coût d'un LOT : même supprimée, le gain reste inférieur à 9 % et devient nul ou négatif en équivalent de limite d'usage dès que le surcroît médical dépasse ≈ @@BE@@ k par fichier. Le risque qualité est réel (langue ≈ 97 % des corrections de conformité, et l'auditeur médical consacre 3,6 % des siennes à la langue). <b>Non au duo tel quel.</b> Oui à une conformité allégée : audit_langue.py en pré-passe, corrections sûres appliquées par script, conformité limitée aux alertes et aux contrôles de jugement.</p></div>
</section>

<section class="panneau" id="reco"><h2>Recommandations ordonnées</h2><div class="carte"><ol class="reco" id="rl"></ol></div></section>
</main>
<script>
const F=@@FAILLES@@, R=@@RECO@@, B=@@BANC@@;
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
function onglet(p){$$('section.panneau').forEach(s=>s.classList.toggle('actif',s.id===p));$$('nav.onglets button').forEach(b=>b.setAttribute('aria-selected',b.dataset.p===p));try{history.replaceState(null,'','#'+p)}catch(e){}}
$$('nav.onglets button').forEach(b=>b.onclick=()=>onglet(b.dataset.p));
if(location.hash&&$(location.hash.slice(0,20)+'.panneau'))onglet(location.hash.slice(1));
$('#theme').onclick=()=>{const r=document.documentElement;const d=getComputedStyle(document.body).backgroundColor;const sombre=r.dataset.theme?r.dataset.theme==='dark':matchMedia('(prefers-color-scheme: dark)').matches;r.dataset.theme=sombre?'light':'dark';try{localStorage.setItem('th',r.dataset.theme)}catch(e){}};
try{const t=localStorage.getItem('th');if(t)document.documentElement.dataset.theme=t}catch(e){}
// failles
let tri='max';
function fk(n){return n.toLocaleString('fr-CH').replace(/\\u202f|\\u00a0/g,' ')}
function dessinerF(){const mx=Math.max(...F.map(f=>f[4]));const l=[...F].sort((a,b)=>tri==='max'?b[4]-a[4]:tri==='min'?b[3]-a[3]:a[0].slice(1)-b[0].slice(1));
$('#tf tbody').innerHTML=l.map(f=>`<tr><td>${f[0]}</td><td class="w"><b>${f[1]}</b></td><td class="n">${fk(f[3])} – ${fk(f[4])}</td><td><div class="bar"><i style="width:${f[4]/mx*100}%"></i></div></td><td class="w">${f[2]}<div class="src">Source : ${f[5]}</div></td><td class="w">${f[6]}</td><td>${f[7]}</td></tr>`).join('')}
$$('[data-tri]').forEach(b=>b.onclick=()=>{tri=b.dataset.tri;dessinerF()});dessinerF();
$('#rl').innerHTML=R.map(r=>`<li><b>${r[1]}</b> — effort ${r[2]} ; gain : ${r[3]} <span class="src">(estimation)</span></li>`).join('');
// banc
(function(){const g=B.agreg;if(!g){$('#bancc').textContent='Banc d\\'essai non généré : python3 harnais/banc_essai_langue.py';return}
const pc=x=>(x*100).toFixed(1).replace('.',',')+' %';
let h=`<p>${g.fichiers_rejoues} fichiers rejoués (LOT_013 à LOT_016, ${g.fichiers_ignores} ignorés faute de version d'avant audit), ${g.corrections_conformite} corrections de conformité journalisées. <span class="src">Source : git + corrections.jsonl, mesuré ; version retrouvée par recoupement des passages « avant », confiance moyenne ${g.confiance_version_moyenne}.</span></p>
<div class="kpis"><div class="kpi"><b>${pc(g.rappel_strict)}</b><span class="mu">rappel strict (contrôles du cahier)</span></div><div class="kpi"><b>${pc(g.rappel_etendu)}</b><span class="mu">rappel étendu (+ points-virgules, bruyant)</span></div><div class="kpi"><b>${pc(g.part_jugement)}</b><span class="mu">corrections de jugement (borne basse)</span></div><div class="kpi"><b>${pc(g.part_medical_langue_format)}</b><span class="mu">corrections médicales de type langue/format (${g.medical_langue_format}/${g.medical_total})</span></div></div>
<table><tr><th>Catégorie (classée par règles)</th><th>n</th><th>détectées (strict)</th><th></th><th>détectées (étendu)</th></tr>`;
const nom={reformulation:'Reformulation, phrase nominale, style',scission_phrase:'Scission de phrase (point-virgule)',redite:'Redite, suppression',sigle_developpe:'Sigle développé',format:'Format',contradiction:'Contradiction',coherence_phase_A:'Cohérence Phase A / titres',affectation_point:'Affectation des points'};
Object.entries(g.par_categorie).sort((a,b)=>b[1].n-a[1].n).forEach(([k,v])=>{h+=`<tr><td>${nom[k]||k}</td><td class="n">${v.n}</td><td class="n">${v.detectees}</td><td><div class="bar v"><i style="width:${v.detectees/v.n*100}%"></i></div></td><td class="n">${v.detectees_etendu}</td></tr>`});
h+=`</table><p class="src">Mesuré : la conformité n'ajoute aucune espace insécable (≈ 760 manquantes par fichier avant et après) et laisse 26 phrases de plus de 35 mots par fichier en moyenne (33 avant) ; les contrôles « cahier » du script sont donc plus stricts que la pratique actuelle. Le classement par catégorie est fait par expressions régulières : « reformulation » est le fourre-tout et contient du jugement.</p>`;
$('#bancc').innerHTML=h})();
// duo
function calc(){const n=+$('#n').value,c=+$('#c').value,s=+$('#s').value,w=+$('#w').value/10,t=+$('#t').value;
$('#vn').textContent=n;$('#vc').textContent=c;$('#vs').textContent=s;$('#vw').textContent=w.toFixed(1).replace('.',',');$('#vt').textContent=fk(t);
const brut=c-s,pond=c-s*w,lot=n*brut,part=n*pond/t*100,fac=(t-n*c+n*s)/t;
const f=(v,el)=>{el.textContent=(v>0?'+':'')+Math.round(v);el.className=v>0?'pos':'neg'};
f(brut,$('#r1'));f(pond,$('#r2'));f(lot,$('#r3'));$('#r4').textContent=part.toFixed(1).replace('.',',')+' %';$('#r4').className=part>0?'pos':'neg';$('#r5').textContent=fac.toFixed(3).replace('.',',');
$('#vd').innerHTML=pond>0?`Avec ces hypothèses, le duo économise ${Math.round(pond)} k éq. Sonnet par fichier, soit ${part.toFixed(1).replace('.',',')} % du LOT. Gain réel mais faible ; le risque qualité (voir ci-dessous) l'emporte.`:`Avec ces hypothèses, le duo coûte plus qu'il ne rapporte en équivalent de limite d'usage (${Math.round(pond)} k par fichier) : le travail passe d'un modèle moins cher à un modèle plus cher.`}
$$('#duo input').forEach(i=>i.oninput=calc);calc();
</script></body></html>"""


def main() -> int:
    data = RM.charger()
    banc = charger_banc()
    g1, g2, g3 = hist_svg(data)
    ev = data["ev"]
    n_ag = Counter(e["agent"] for e in ev)
    ncorr = sum(len(v) for v in data["corr"].values())
    kp = [("décisions", len(ev)), ("rédactions", n_ag["redacteur"] + n_ag["redacteur-phase-a"]),
          ("audits médicaux", n_ag["auditeur-medical"]), ("audits conformité", n_ag["auditeur-conformite"]), ("corrections", ncorr)]
    kpis = "".join(f'<div class="kpi"><b>{v}</b><span class="mu">{k}</span></div>' for k, v in kp)
    tot = sum(v for v, _ in BASE.values())
    base = "<tr><th>Poste</th><th>k jetons</th><th>part</th><th>source</th></tr>" + "".join(
        f'<tr><td>{k}</td><td class="n">{v:,.0f}</td><td class="n">{v / tot * 100:.1f} %</td><td class="src">{s}</td></tr>'.replace(",", " ")
        for k, (v, s) in BASE.items()) + f'<tr><th>Total</th><th class="n">{tot:,.0f}</th><th></th><th></th></tr>'.replace(",", " ")
    conf = round(moy(MES["conformites_B"]))
    g = banc.get("agreg", {})
    fl = [f for f in banc.get("fichiers", []) if "ignore" not in f]
    nflags = round(sum(sum(f["flags_avant"].get(k, 0) for k in ("phrase_longue", "phrase_double", "sigle_non_developpe", "insecable", "pv_simple", "chaine_pv")) for f in fl) / max(1, len(fl)))
    ncorr_f = round(sum(f["n_corr"] for f in fl) / max(1, len(fl)))
    pc = lambda x: f"{x * 100:.1f}".replace(".", ",") + " %" if x is not None else "n.d."
    rep = {
        "@@CSS@@": RM.CSS, "@@DATE@@": __import__("datetime").datetime.now().strftime("%d.%m.%Y %H:%M"), "@@KPIS@@": kpis,
        "@@G1@@": g1, "@@G2@@": g2, "@@G3@@": g3, "@@BASE@@": base, "@@CONF@@": str(conf), "@@TOT@@": str(round(tot)),
        "@@RAPPEL@@": f"rappel strict {pc(g.get('rappel_strict'))}", "@@JUG@@": f"au moins {pc(g.get('part_jugement'))}",
        "@@STY@@": pc(g.get("part_style_reformulation")), "@@FLAGS@@": str(nflags), "@@NC@@": str(ncorr_f),
        "@@BE@@": str(round(conf / 1.67)),
        "@@FAILLES@@": json.dumps([list(f) for f in FAILLES], ensure_ascii=False),
        "@@RECO@@": json.dumps([list(r) for r in RECO], ensure_ascii=False),
        "@@BANC@@": json.dumps(banc, ensure_ascii=False),
    }
    out = PAGE
    for k, v in rep.items():
        out = out.replace(k, v)
    SORTIE.write_text(out, encoding="utf8")
    print(f"{SORTIE} ({len(out)} octets) ; coût LOT de référence {tot:,.0f} k ; conformité {sum(MES['conformites_B']) / len(MES['conformites_B']):.0f} k/fichier")
    return 0


if __name__ == "__main__":
    sys.exit(main())
