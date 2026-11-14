#!/usr/bin/env python3
"""Génère STATUS.html : page de lecture de la Sémiologie Status (S-01 → S-35).

Lit status/S-*.json à chaque exécution (d'autres agents écrivent encore) ;
un JSON illisible est sauté et signalé. Images en relatif img/…
Règle EYE SPOT : fond blanc, texte noir ; une couleur par rôle de titre.
"""
import glob
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
DOSSIER = os.path.join(ICI, "status")
RECENSEMENT = os.path.normpath(os.path.join(ICI, "..", "..", "recensement_sf", "recensement_sf.json"))
SORTIE = os.path.join(ICI, "STATUS.html")

# Une couleur par rôle (jamais de mélange ni de dégradé), contraste ≥ 7:1 sur blanc.
COULEURS = {
    "fiche": "#0B3B8C",    # bandeau et titre de fiche
    "temps": "#0B5A2E",    # titres des temps d'examen
    "carte": "#6A1B7A",    # sous-titres des cartes de manœuvre
    "cs": "#8A3B00",       # encadré « Version CS » (réservée)
}

# Regroupement par région, ordre topo-systémique et cranio-caudal.
GROUPES = [
    ("Généralités", range(1, 5)),
    ("Tête et cou", range(5, 9)),
    ("Thorax", range(9, 12)),
    ("Abdomen et pelvis", range(12, 17)),
    ("Rachis et membres", range(17, 23)),
    ("Vaisseaux périphériques", range(23, 25)),
    ("Système nerveux", range(25, 30)),
    ("Psychisme", range(30, 31)),
    ("Situations particulières", range(31, 36)),
]
TEMPS_ORDRE = ["Inspection", "Palpation", "Percussion", "Auscultation", "Manœuvres"]
SIGLES_SUPPL = {
    "EIC": "espace intercostal", "IMC": "indice de masse corporelle", "FR": "fréquence respiratoire",
    "USZ": "Hôpital universitaire de Zurich", "ASSM": "Académie suisse des sciences médicales",
    "OMS": "Organisation mondiale de la santé", "ESC": "Société européenne de cardiologie",
    "RV": "rapport de vraisemblance", "MIN": "niveau minimal exigé", "CIBLE": "niveau cible",
}
SIGLES_EXCLUS = {"OR", "NET", "NURSE", "KK", "SA", "CD", "TR", "PS"}


def ratio_contraste(hexa):
    def lin(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hexa[i:i + 2], 16) for i in (1, 3, 5))
    lum = 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
    return 1.05 / (lum + 0.05)


for _role, _c in COULEURS.items():
    assert ratio_contraste(_c) >= 7, f"contraste insuffisant {_role} {_c}"


def charger_recensement():
    d = json.load(open(RECENSEMENT, encoding="utf-8"))
    items = d["semiologie"]["S"]
    status = {x["id"]: x for x in items if x.get("type") == "status"}
    syndromes = {}
    for x in items:
        m = re.match(r"SY-0*(\d+)$", x["id"])
        if m:
            syndromes[int(m.group(1))] = x["titre"]
    sigles = {k: v for k, v in d.get("sigles", {}).items() if k not in SIGLES_EXCLUS}
    sigles.update(SIGLES_SUPPL)
    return status, syndromes, sigles


STATUS_REC, SYNDROMES, SIGLES = charger_recensement()
CS_T = SIGLES.get("CS", "Clinical Skills")
_motif_sigles = re.compile(
    r"(?<![\w-])(" + "|".join(re.escape(k) for k in sorted(SIGLES, key=len, reverse=True)) + r")(?![\w-])"
)
_motif_sy = re.compile(r"\bSY-0*(\d+)\b")


def e(t):
    return html.escape(str(t), quote=True)


def txt(t):
    """Échappe puis balise les sigles et les renvois SY-xx en <abbr title>."""
    s = e(t)
    out, pos = [], 0
    for m in _motif_sy.finditer(s):
        out.append(_sigles(s[pos:m.start()]))
        n = int(m.group(1))
        titre = SYNDROMES.get(n, "syndrome non recensé")
        out.append(f'<abbr title="{e(titre)}">SY-{n}</abbr>')
        pos = m.end()
    out.append(_sigles(s[pos:]))
    return "".join(out)


def _sigles(s):
    return _motif_sigles.sub(lambda m: f'<abbr title="{e(SIGLES[m.group(1)])}">{m.group(1)}</abbr>', s)


def liste(items, balise="ul", cls=""):
    if not items:
        return ""
    c = f' class="{cls}"' if cls else ""
    return f"<{balise}{c}>" + "".join(f"<li>{txt(i)}</li>" for i in items) + f"</{balise}>"


def num(sid):
    return int(sid.split("-")[1])


def charger_fiches():
    fiches, illisibles = {}, []
    for f in sorted(glob.glob(os.path.join(DOSSIER, "S-*.json"))):
        try:
            with open(f, encoding="utf-8") as h:
                d = json.load(h)
            sid = d.get("id") or os.path.basename(f)[:-5]
            fiches[sid] = d
        except Exception as ex:  # JSON en cours d'écriture ou invalide
            illisibles.append(os.path.basename(f))
            print(f"[signalement] {os.path.basename(f)} illisible, sauté : {ex}", file=sys.stderr)
    return fiches, illisibles


def rendre_image(img, nom, sid):
    if not isinstance(img, dict):
        return '<div class="afournir"><strong>Image à fournir</strong></div>'
    if "fichier" in img:
        chemin = img["fichier"]
        credit = (
            f'<p class="credit">{e(img.get("credit", "Crédit à vérifier"))} — {e(img.get("licence", "licence à vérifier"))}'
            + (f' — <a href="{e(img["url"])}" target="_blank" rel="noopener">source</a>' if img.get("url") else "")
            + "</p>"
        )
        leg = img.get("legende") or nom
        if os.path.exists(os.path.join(ICI, chemin)):
            return (
                f'<figure class="fig"><button type="button" class="vignette" data-src="{e(chemin)}" '
                f'data-leg="{e(leg)}" data-credit="{e(img.get("credit", ""))} — {e(img.get("licence", ""))}" '
                f'data-url="{e(img.get("url", ""))}" aria-label="Agrandir l’image : {e(leg)}">'
                f'<img src="{e(chemin)}" alt="{e(leg)}" loading="lazy"></button>'
                f'<figcaption>{txt(leg)}</figcaption>{credit}</figure>'
            )
        print(f"[signalement] {sid} : image annoncée absente de img/ : {chemin}", file=sys.stderr)
        return (f'<div class="afournir"><strong>Image en attente de dépôt :</strong> {e(chemin)}'
                f'<br>{txt(leg)}</div>{credit}')
    return f'<div class="afournir"><strong>Image à fournir :</strong> {txt(img.get("a_fournir", ""))}</div>'


def rendre_fiche(d):
    sid = d.get("id", "?")
    niv = {"m": "MIN", "c": "CIBLE"}.get(d.get("niveau"), e(d.get("niveau", "?")))
    duree = d.get("duree") or {}
    h = [f'<section class="fiche" id="{e(sid)}" aria-labelledby="t-{e(sid)}">']
    h.append(
        f'<header class="bandeau"><h2 id="t-{e(sid)}"><span class="sid">{e(sid)}</span> {e(d.get("titre", ""))}</h2>'
        '<dl class="meta">'
        f'<div><dt>Région</dt><dd>{txt(d.get("region", "—"))}</dd></div>'
        f'<div><dt>Système</dt><dd>{txt(d.get("systeme", "—"))}</dd></div>'
        f'<div><dt><abbr title="{e(SIGLES.get("EPA", "Entrustable Professional Activity"))}">EPA</abbr></dt><dd>{txt(d.get("epa", "—"))}</dd></div>'
        f'<div><dt>Niveau</dt><dd><abbr title="{"niveau minimal exigé" if niv == "MIN" else "niveau cible"}">{niv}</abbr></dd></div>'
        f'<div><dt>Durée complète</dt><dd>{txt(duree.get("complet", "—"))}</dd></div>'
        f'<div><dt>Durée <abbr title="{e(SIGLES.get("CS", "examen clinique structuré"))}">CS</abbr></dt><dd>{txt(duree.get("cs", "—"))}</dd></div>'
        "</dl></header>"
    )
    h.append('<div class="deuxcol">'
             f'<div><h3 class="temps">Matériel</h3>{liste(d.get("materiel"))}</div>'
             f'<div><h3 class="temps">Installation</h3>{liste(d.get("installation"))}</div></div>')

    temps = sorted(d.get("examen_complet", []),
                   key=lambda t: TEMPS_ORDRE.index(t.get("temps")) if t.get("temps") in TEMPS_ORDRE else 99)
    if temps:
        h.append('<h3 class="temps titre-section">Examen complet</h3>')
    for t in temps:
        h.append(f'<h4 class="temps">{e(t.get("temps", ""))}</h4>')
        h.append('<div class="defile" tabindex="0" role="region" aria-label="Tableau '
                 f'{e(t.get("temps", ""))} — défilement horizontal"><table><thead><tr>'
                 '<th scope="col">Geste</th><th scope="col">Normal</th><th scope="col">Anomalies → signification</th>'
                 "</tr></thead><tbody>")
        for g in t.get("gestes", []):
            an = g.get("anomalies") or []
            ans = "".join(
                f'<li><strong>{txt(a.get("signe", ""))}</strong> → {txt(a.get("signifie", ""))}</li>'
                if isinstance(a, dict) else f"<li>{txt(a)}</li>" for a in an)
            h.append(f'<tr><td>{txt(g.get("geste", ""))}</td><td>{txt(g.get("normal", ""))}</td>'
                     f'<td>{"<ul>" + ans + "</ul>" if ans else "—"}</td></tr>')
        h.append("</tbody></table></div>")

    ms = d.get("manoeuvres_speciales") or []
    if ms:
        h.append('<h3 class="temps titre-section">Manœuvres spéciales</h3><div class="cartes">')
        for m in ms:
            tech = m.get("technique") or []
            if isinstance(tech, str):
                tech = [tech]
            h.append(
                '<article class="carte">'
                f'<h4 class="carte-t">{txt(m.get("nom", ""))}</h4>'
                + (f'<p><span class="lab">But</span> {txt(m["but"])}</p>' if m.get("but") else "")
                + f'<h5 class="carte-t">Technique</h5>{liste(tech, "ol")}'
                f'<h5 class="carte-t">Positif si</h5><p>{txt(m.get("positif_si", "—"))}</p>'
                f'<h5 class="carte-t">Valeur</h5><p>{txt(m.get("valeur", "À vérifier"))}</p>'
                f'<h5 class="carte-t">Interprétation</h5><p>{txt(m.get("interpretation", "—"))}</p>'
                f'{rendre_image(m.get("image"), m.get("nom", ""), sid)}</article>'
            )
        h.append("</div>")

    v = d.get("version_cs") or {}
    if v:
        h.append(
            '<aside class="cs" aria-label="Version CS">'
            f'<h3 class="cs-t">Version <abbr title="{e(CS_T)}">CS</abbr> (13 min)</h3>'
            + (f'<p><span class="lab">Cible</span> {txt(v.get("cible", ""))}</p>' if v.get("cible") else "")
            + '<h4 class="cs-t">À dire à voix haute</h4>' + liste(v.get("a_dire"))
            + '<h4 class="cs-t">À nommer sans faire</h4>' + liste(v.get("a_nommer_sans_faire"))
            + '<h4 class="cs-t">Pièges</h4>' + liste(v.get("pieges"))
            + "</aside>"
        )

    sy = d.get("syndromes_lies") or []
    if sy:
        pastilles = []
        for s in sy:
            mm = re.match(r"SY-0*(\d+)", str(s))
            n = int(mm.group(1)) if mm else None
            titre = SYNDROMES.get(n, "syndrome non recensé")
            pastilles.append(f'<li><span class="pastille" tabindex="0" title="{e(titre)}" '
                             f'aria-label="SY-{n} : {e(titre)}">SY-{n}</span></li>')
        h.append('<h3 class="temps">Syndromes liés</h3><ul class="pastilles">' + "".join(pastilles) + "</ul>")
    if d.get("sources"):
        h.append('<h3 class="temps">Sources</h3>' + liste(d["sources"], "ol", "sources"))
    h.append("</section>")
    return "".join(h)


def rendre_absente(sid, motif):
    rec = STATUS_REC.get(sid, {})
    return (f'<section class="fiche" id="{e(sid)}" aria-labelledby="t-{e(sid)}">'
            f'<header class="bandeau"><h2 id="t-{e(sid)}"><span class="sid">{e(sid)}</span> {e(rec.get("titre", ""))}</h2></header>'
            f'<div class="afournir"><strong>{e(motif)}</strong></div></section>')


CSS = """
:root{--fiche:%(fiche)s;--temps:%(temps)s;--carte:%(carte)s;--cs:%(cs)s;--trait:#5A5A5A;--fin:#BDBDBD}
*{box-sizing:border-box}
html{scroll-padding-top:12px}
body{margin:0;background:#FFFFFF;color:#000000;font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;overflow-x:hidden}
a{color:#000000;text-decoration:underline}
abbr[title]{text-decoration:underline dotted;cursor:help}
.saut{position:absolute;left:-9999px}.saut:focus{left:16px;top:8px;background:#FFFFFF;padding:8px;border:2px solid #000;z-index:50}
.cadre{display:grid;grid-template-columns:290px minmax(0,1fr);min-height:100vh}
nav.menu{position:sticky;top:0;height:100vh;overflow-y:auto;border-right:1px solid var(--fin);padding:16px 12px 32px;background:#FFFFFF}
nav.menu .marque{font-weight:700;font-size:1.05rem;color:var(--fiche);margin:0 0 12px}
nav.menu h2{font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;margin:16px 0 4px;color:#000}
nav.menu ul{list-style:none;margin:0;padding:0}
nav.menu a{display:block;padding:4px 8px;text-decoration:none;border-left:3px solid transparent;font-size:.92rem}
nav.menu a:hover,nav.menu a:focus{text-decoration:underline}
nav.menu a[aria-current=true]{border-left-color:#000;font-weight:700}
nav.menu .absent{font-style:italic}
.basc{display:none}
main{padding:24px 32px 64px;max-width:1180px;min-width:0}
main p,main li,main dd,figcaption{overflow-wrap:break-word}
.sources,.credit,.afournir{overflow-wrap:anywhere}
main>h1{font-size:1.6rem;margin:0 0 4px;color:var(--fiche)}
.chapeau{margin:0 0 8px}
.alerte{border:2px solid #000;padding:8px 12px;margin:12px 0}
.fiche{border-top:3px solid var(--fiche);padding-top:8px;margin:40px 0 0}
.bandeau h2{color:var(--fiche);font-size:1.5rem;margin:4px 0 8px}
.sid{font-variant-numeric:tabular-nums;margin-right:.3em}
.meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:4px 20px;margin:0 0 8px;padding:8px 0;border-bottom:1px solid var(--fin)}
.meta div{min-width:0}.meta dt{font-weight:700;font-size:.82rem}.meta dd{margin:0}
h3.temps,h4.temps{color:var(--temps)}
h3.temps{font-size:1.15rem;margin:20px 0 6px}
h3.titre-section{font-size:1.25rem;border-bottom:1px solid var(--temps);padding-bottom:2px;margin-top:28px}
h4.temps{font-size:1.05rem;margin:16px 0 6px}
.deuxcol{display:grid;grid-template-columns:1fr 2fr;gap:0 32px}
.deuxcol ul{margin:0;padding-left:1.2em}
.defile{overflow-x:auto;border:1px solid var(--fin)}
.defile:focus{outline:2px solid #000}
table{border-collapse:collapse;width:100%%;min-width:760px}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--fin)}
th{font-weight:700;border-bottom:2px solid #000;background:#FFFFFF}
td:nth-child(1){width:34%%}td:nth-child(2){width:24%%}
td ul{margin:0;padding-left:1.1em}td li{margin:0 0 4px}
.cartes{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}
.carte{border:1px solid var(--trait);padding:12px 14px;min-width:0}
.carte h4.carte-t{font-size:1.05rem;margin:0 0 6px}
.carte-t{color:var(--carte)}
h5.carte-t{font-size:.9rem;margin:10px 0 2px}
.carte p{margin:0}.carte ol{margin:0;padding-left:1.4em}
.lab{font-weight:700;margin-right:.3em}
.fig{margin:12px 0 0}
.vignette{display:block;padding:0;border:1px solid var(--trait);background:#FFFFFF;cursor:zoom-in;width:100%%}
.vignette img{display:block;width:100%%;max-height:240px;object-fit:contain;background:#FFFFFF}
.vignette:focus{outline:3px solid #000;outline-offset:2px}
figcaption{font-size:.9rem;margin-top:4px}
.credit{font-size:.82rem;margin:2px 0 0}
.afournir{border:1px dashed #000;padding:8px 10px;margin:12px 0 0;font-size:.92rem}
.cs{border:3px solid var(--cs);padding:12px 16px;margin:28px 0 0}
.cs-t{color:var(--cs)}
h3.cs-t{margin:0 0 6px;font-size:1.2rem}
h4.cs-t{margin:12px 0 4px;font-size:1rem}
.cs ul{margin:0;padding-left:1.2em}
.pastilles{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:8px}
.pastille{display:inline-block;border:1px solid #000;border-radius:999px;padding:2px 12px;font-size:.88rem;cursor:help}
.pastille:focus{outline:2px solid #000}
.sources{font-size:.9rem;padding-left:1.4em}
/* Fenêtre image centrale ; page derrière floutée */
body.modal-ouverte .cadre{filter:blur(6px)}
#fenetre{position:fixed;inset:0;display:none;align-items:center;justify-content:center;padding:16px;background:rgba(255,255,255,.55);z-index:100}
#fenetre.ouverte{display:flex}
#fenetre .boite{background:#FFFFFF;border:2px solid #000;max-width:min(1100px,100%%);max-height:100%%;overflow:auto;padding:12px 14px;position:relative}
#fenetre img{display:block;max-width:100%%;max-height:72vh;margin:0 auto}
#fenetre .fermer{position:absolute;top:6px;right:6px;font:700 1rem system-ui,sans-serif;background:#FFFFFF;color:#000;border:2px solid #000;padding:4px 10px;cursor:pointer}
#fenetre .leg{margin:8px 40px 0 0}
#fenetre .cr{font-size:.85rem;margin:4px 0 0}
@media (max-width:860px){
 .cadre{display:block}
 .basc{display:block;position:sticky;top:0;z-index:20;width:100%%;text-align:left;background:#FFFFFF;color:#000;border:0;border-bottom:2px solid #000;font:700 1rem system-ui,sans-serif;padding:12px 16px;cursor:pointer}
 nav.menu{position:static;height:auto;max-height:none;border-right:0;border-bottom:1px solid var(--fin);padding:8px 16px 16px;display:none}
 nav.menu.ouvert{display:block}
 main{padding:16px 16px 48px}
 .deuxcol{grid-template-columns:1fr}
 .cartes{grid-template-columns:minmax(0,1fr)}
 table{min-width:640px}
 .meta{grid-template-columns:1fr}
}
@media print{nav.menu,.basc{display:none}.cadre{display:block}.defile{overflow:visible}}
""" % COULEURS

JS = r"""
(function(){
 var f=document.getElementById('fenetre'),img=f.querySelector('img'),leg=f.querySelector('.leg'),cr=f.querySelector('.cr'),
     btnF=f.querySelector('.fermer'),dernier=null;
 function ouvrir(b){dernier=b;img.src=b.dataset.src;img.alt=b.dataset.leg||'';leg.textContent=b.dataset.leg||'';
  cr.textContent='';cr.appendChild(document.createTextNode(b.dataset.credit||''));
  if(b.dataset.url){cr.appendChild(document.createTextNode(' — '));var a=document.createElement('a');a.href=b.dataset.url;
   a.target='_blank';a.rel='noopener';a.textContent='source';cr.appendChild(a);}
  f.classList.add('ouverte');f.setAttribute('aria-hidden','false');document.body.classList.add('modal-ouverte');btnF.focus();}
 function fermer(){f.classList.remove('ouverte');f.setAttribute('aria-hidden','true');document.body.classList.remove('modal-ouverte');
  img.removeAttribute('src');if(dernier)dernier.focus();}
 document.addEventListener('click',function(ev){var b=ev.target.closest('.vignette');if(b){ouvrir(b);}});
 btnF.addEventListener('click',fermer);
 f.addEventListener('click',function(ev){if(ev.target===f)fermer();});
 document.addEventListener('keydown',function(ev){if(ev.key==='Escape'&&f.classList.contains('ouverte'))fermer();});
 var nav=document.getElementById('menu'),basc=document.querySelector('.basc');
 basc.addEventListener('click',function(){var o=nav.classList.toggle('ouvert');basc.setAttribute('aria-expanded',o?'true':'false');});
 nav.addEventListener('click',function(ev){if(ev.target.closest('a')&&window.matchMedia('(max-width:860px)').matches){
  nav.classList.remove('ouvert');basc.setAttribute('aria-expanded','false');}});
 var liens={};nav.querySelectorAll('a[href^="#S-"]').forEach(function(a){liens[a.getAttribute('href').slice(1)]=a;});
 if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){
  Object.keys(liens).forEach(function(k){liens[k].removeAttribute('aria-current');});
  var a=liens[x.target.id];if(a)a.setAttribute('aria-current','true');}});},{rootMargin:'0px 0px -80% 0px'});
  document.querySelectorAll('section.fiche').forEach(function(s){io.observe(s);});}
})();
"""


def main():
    fiches, illisibles = charger_fiches()
    ids = [f"S-{i:02d}" for i in range(1, 36)]
    menu, corps = [], []
    for nom_g, plage in GROUPES:
        menu.append(f"<h2>{e(nom_g)}</h2><ul>")
        for i in plage:
            sid = f"S-{i:02d}"
            titre = (fiches.get(sid) or {}).get("titre") or STATUS_REC.get(sid, {}).get("titre", "")
            cls = "" if sid in fiches else ' class="absent"'
            menu.append(f'<li><a href="#{sid}"{cls}>{sid} {e(titre)}</a></li>')
        menu.append("</ul>")
    for sid in ids:
        if sid in fiches:
            corps.append(rendre_fiche(fiches[sid]))
        elif f"{sid}.json" in illisibles:
            corps.append(rendre_absente(sid, "Fiche en cours d’écriture : JSON illisible à la génération."))
        else:
            corps.append(rendre_absente(sid, "Fiche en rédaction."))
    for sid in sorted(set(fiches) - set(ids)):
        corps.append(rendre_fiche(fiches[sid]))
    alerte = ""
    if illisibles:
        alerte = f'<p class="alerte">JSON illisible(s) sauté(s) : {e(", ".join(illisibles))}.</p>'
    page = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sémiologie Status</title><style>{CSS}</style></head>
<body><a class="saut" href="#contenu">Aller au contenu</a>
<div class="cadre">
<button type="button" class="basc" aria-expanded="false" aria-controls="menu">☰ Menu des fiches S-01 → S-35</button>
<nav class="menu" id="menu" aria-label="Fiches du status"><p class="marque">Sémiologie — Status</p>{"".join(menu)}</nav>
<main id="contenu"><h1>Sémiologie — Status</h1>
<p class="chapeau">{len(fiches)} fiches sur 35, ordre topo-systémique et cranio-caudal. Niveau <abbr title="niveau minimal exigé">MIN</abbr> ou <abbr title="niveau cible">CIBLE</abbr> ; encadré « Version <abbr title="{e(CS_T)}">CS</abbr> » pour la station de 13 min.</p>
{alerte}{"".join(corps)}</main></div>
<div id="fenetre" role="dialog" aria-modal="true" aria-label="Image agrandie" aria-hidden="true">
<div class="boite"><button type="button" class="fermer" aria-label="Fermer la fenêtre">✕ Fermer</button>
<img alt=""><p class="leg"></p><p class="cr"></p></div></div>
<script>{JS}</script></body></html>
"""
    with open(SORTIE, "w", encoding="utf-8") as h:
        h.write(page)
    print(f"STATUS.html : {len(fiches)} fiches, {len(illisibles)} illisible(s), {len(page)//1024} Ko → {SORTIE}")


if __name__ == "__main__":
    main()
