#!/usr/bin/env python3
"""Génère SEMIOLOGIE.html (cinq onglets) et STATUS.html (alias de compatibilité).

Onglets : Status (status/S-*.json), Syndromes (syndromes/SY-*.json), Anamnèse
(anamnese/A-*.json), Management (management/M-*.json), Communication
(communication/K-*.json). Relit les dossiers à chaque exécution (d'autres agents
écrivent encore) ; un JSON illisible est sauté et signalé. Images en relatif img/…
Règle EYE SPOT : fond blanc, texte noir ; une couleur par rôle de titre.
Renvois S-xx / SY-xx / A-xx / M-xx / K-xx cliquables ; sigles en <abbr title>.
"""
import glob
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RECENSEMENT = os.path.normpath(os.path.join(ICI, "..", "..", "recensement_sf", "recensement_sf.json"))
SORTIE = os.path.join(ICI, "SEMIOLOGIE.html")
ALIAS = os.path.join(ICI, "STATUS.html")

# Une couleur par rôle (jamais de mélange ni de dégradé), contraste ≥ 7:1 sur blanc.
COULEURS = {
    "fiche": "#0B3B8C",    # bandeau et titre de fiche
    "temps": "#0B5A2E",    # titres de sections (temps d'examen, rubriques)
    "carte": "#6A1B7A",    # sous-titres des cartes
    "cs": "#8A3B00",       # encadré « Version CS » / synthèse CS (réservée)
    "alerte": "#8B0000",   # encadré « Drapeaux rouges » (réservée)
}

GROUPES_STATUS = [
    ("Généralités", range(1, 5)), ("Tête et cou", range(5, 9)), ("Thorax", range(9, 12)),
    ("Abdomen et pelvis", range(12, 17)), ("Rachis et membres", range(17, 23)),
    ("Vaisseaux périphériques", range(23, 25)), ("Système nerveux", range(25, 30)),
    ("Psychisme", range(30, 31)), ("Situations particulières", range(31, 36)),
]
TEMPS_ORDRE = ["Inspection", "Palpation", "Percussion", "Auscultation", "Manœuvres"]
# Mots-clés → code système du recensement (ordre topo-systémique S1…S12, T).
SYSTEME_CLES = [
    ("S1", "neuro"), ("S2", "orl"), ("S2", "ophtalm"), ("S2", "tête"), ("S3", "cardio"), ("S4", "respir"),
    ("S5", "digest"), ("S6", "néphro"), ("S7", "reproduction"), ("S7", "gyné"), ("S8", "endocrin"),
    ("S9", "locomot"), ("S10", "sang"), ("S11", "psych"), ("S12", "peau"), ("T", "transvers"),
]
SIGLES_SUPPL = {
    "EIC": "espace intercostal", "IMC": "indice de masse corporelle", "FR": "fréquence respiratoire",
    "USZ": "Hôpital universitaire de Zurich", "ASSM": "Académie suisse des sciences médicales",
    "OMS": "Organisation mondiale de la santé", "ESC": "Société européenne de cardiologie",
    "RV": "rapport de vraisemblance", "MIN": "niveau minimal exigé", "CIBLE": "niveau cible",
    "ARRR": "Attendre, Répéter, Reformuler, Résumer",
}
SIGLES_EXCLUS = {"OR", "NET", "NURSE", "KK", "SA", "CD", "TR", "PS"}


def ratio_contraste(hexa):
    def lin(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hexa[i:i + 2], 16) for i in (1, 3, 5))
    return 1.05 / (0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b) + 0.05)


for _role, _c in COULEURS.items():
    assert ratio_contraste(_c) >= 7, f"contraste insuffisant {_role} {_c}"

# ---------------------------------------------------------------- recensement
REC = json.load(open(RECENSEMENT, encoding="utf-8"))
SEM = REC["semiologie"]
NOMS_SYSTEMES = {s["code"]: s["nom"] for s in REC.get("systemes", [])}
SIGLES = {k: v for k, v in REC.get("sigles", {}).items() if k not in SIGLES_EXCLUS}
SIGLES.update(SIGLES_SUPPL)
CS_T = SIGLES.get("CS", "Clinical Skills")


def sy_norm(x):
    m = re.match(r"SY-0*(\d+)$", str(x).strip())
    return f"SY-{int(m.group(1))}" if m else str(x).strip()


REC_S = {x["id"]: x for x in SEM["S"] if x.get("type") == "status"}
REC_SY = {sy_norm(x["id"]): x for x in SEM["S"] if x.get("type") == "syndrome"}
REC_A = {x["id"]: x for x in SEM.get("A", [])}
REC_M = {x["id"]: x for x in SEM.get("M", [])}
REC_K = {x["id"]: x for x in SEM.get("KK", [])}


def e(t):
    return html.escape(str(t), quote=True)


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


# ---------------------------------------------------------------- chargement
SIGNALEMENTS = []


def signaler(msg):
    SIGNALEMENTS.append(msg)
    print(f"[signalement] {msg}", file=sys.stderr)


def charger(dossier, motif, norm=lambda x: x):
    fiches, illisibles = {}, []
    for f in sorted(glob.glob(os.path.join(ICI, dossier, motif))):
        base = os.path.basename(f)
        try:
            with open(f, encoding="utf-8") as h:
                d = json.load(h)
            if not isinstance(d, dict):
                raise ValueError("racine non objet")
            sid = norm(d.get("id") or base[:-5])
            d["id"] = sid
            fiches[sid] = d
        except Exception as ex:
            illisibles.append(base)
            signaler(f"{dossier}/{base} illisible, sauté : {ex}")
    return fiches, illisibles


F_S, ILL_S = charger("status", "S-*.json")
F_SY, ILL_SY = charger("syndromes", "SY-*.json", sy_norm)
F_A, ILL_A = charger("anamnese", "A-*.json")
F_M, ILL_M = charger("management", "M-*.json")
F_K, ILL_K = charger("communication", "K-*.json")

# Index des cibles de renvoi : id → titre.
CIBLES = {}
for rec, fic in ((REC_S, F_S), (REC_SY, F_SY), (REC_A, F_A), (REC_M, F_M), (REC_K, F_K)):
    for k, v in rec.items():
        CIBLES[k] = v.get("titre", "")
    for k, v in fic.items():
        CIBLES[k] = v.get("titre", "") or CIBLES.get(k, "")

_ids_hors_sy = sorted((k for k in CIBLES if not k.startswith("SY-")), key=len, reverse=True)
_motif = re.compile(
    r"(?<![\w-])(?:(?P<sy>SY-0*\d+)|(?P<id>" + "|".join(re.escape(k) for k in _ids_hors_sy) + r")"
    r"|(?P<sig>" + "|".join(re.escape(k) for k in sorted(SIGLES, key=len, reverse=True)) + r"))(?![\w-])"
)


def lien(cible, texte=None, cls=""):
    titre = CIBLES.get(cible)
    c = f' class="{cls}"' if cls else ""
    if titre is None:
        return f'<abbr title="non recensé">{e(texte or cible)}</abbr>'
    return f'<a href="#{e(cible)}"{c} title="{e(titre)}">{e(texte or cible)}</a>'


def txt(t):
    """Échappe ; renvois S/SY/A/M/K → liens ; sigles → <abbr title>."""
    s = str(t)
    out, pos = [], 0
    for m in _motif.finditer(s):
        out.append(e(s[pos:m.start()]))
        if m.group("sy"):
            out.append(lien(sy_norm(m.group("sy"))))
        elif m.group("id"):
            out.append(lien(m.group("id")))
        else:
            k = m.group("sig")
            out.append(f'<abbr title="{e(SIGLES[k])}">{e(k)}</abbr>')
        pos = m.end()
    out.append(e(s[pos:]))
    return "".join(out)


def liste(items, balise="ul", cls=""):
    items = [i for i in as_list(items) if str(i).strip()]
    if not items:
        return ""
    c = f' class="{cls}"' if cls else ""
    return f"<{balise}{c}>" + "".join(f"<li>{txt(i)}</li>" for i in items) + f"</{balise}>"


def h3(titre):
    return f'<h3 class="temps">{e(titre)}</h3>'


def niveau(n):
    lab = {"m": "MIN", "c": "CIBLE"}.get(n)
    if not lab:
        return e(n or "—")
    return f'<abbr title="{"niveau minimal exigé" if lab == "MIN" else "niveau cible"}">{lab}</abbr>'


def bandeau(sid, titre, champs):
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in champs if v)
    return (f'<header class="bandeau"><h2 id="t-{e(sid)}"><span class="sid">{e(sid)}</span> {e(titre)}</h2>'
            + (f'<dl class="meta">{dl}</dl>' if dl else "") + "</header>")


def pastilles(ids):
    ids = [i for i in as_list(ids) if str(i).strip()]
    if not ids:
        return ""
    return '<ul class="pastilles">' + "".join(
        f"<li>{lien(sy_norm(i) if str(i).startswith('SY') else str(i).strip(), cls='pastille')}</li>" for i in ids) + "</ul>"


def est_intime(img):
    return bool(img.get("occulter")) or "image intime" in (img.get("legende", "") + img.get("credit", "")).lower() \
        or "occultante" in (img.get("legende", "") + img.get("credit", "")).lower()


def rendre_image(img, nom, sid):
    if img is None:
        return ""
    if not isinstance(img, dict):
        return '<div class="afournir"><strong>Image à fournir</strong></div>'
    if "fichier" in img:
        chemin = img["fichier"]
        cr_txt = f'{img.get("credit", "Crédit à vérifier")} — {img.get("licence", "licence à vérifier")}'
        credit = (f'<p class="credit">{e(cr_txt)}'
                  + (f' — <a href="{e(img["url"])}" target="_blank" rel="noopener">source</a>' if img.get("url") else "")
                  + "</p>")
        leg = img.get("legende") or nom
        if not os.path.exists(os.path.join(ICI, chemin)):
            signaler(f"{sid} : image annoncée absente de img/ : {chemin}")
            return (f'<div class="afournir"><strong>Image en attente de dépôt :</strong> {e(chemin)}'
                    f'<br>{txt(leg)}</div>{credit}')
        data = (f'data-src="{e(chemin)}" data-leg="{e(leg)}" data-credit="{e(cr_txt)}" '
                f'data-url="{e(img.get("url", ""))}"')
        if est_intime(img):
            return (f'<figure class="fig"><button type="button" class="vignette occulte" {data} '
                    f'aria-label="Image intime occultée : ouvrir dans la fenêtre — {e(nom)}">'
                    '<span>Image intime occultée</span><span class="petit">Cliquer pour l’ouvrir dans la fenêtre</span>'
                    f'</button>{credit}</figure>')
        return (f'<figure class="fig"><button type="button" class="vignette" {data} '
                f'aria-label="Agrandir l’image : {e(leg)}"><img src="{e(chemin)}" alt="{e(leg)}" loading="lazy"></button>'
                f'<figcaption>{txt(leg)}</figcaption>{credit}</figure>')
    if img.get("a_fournir"):
        return f'<div class="afournir"><strong>Image à fournir :</strong> {txt(img["a_fournir"])}</div>'
    return ""


def section(sid, corps):
    return f'<section class="fiche" id="{e(sid)}" aria-labelledby="t-{e(sid)}">{corps}</section>'


def absente(sid, titre, illisible):
    motif = "Fiche en cours d’écriture : JSON illisible à la génération." if illisible else "Fiche en rédaction."
    return section(sid, bandeau(sid, titre, []) + f'<div class="afournir"><strong>{motif}</strong></div>')


def encadre_cs(titre, corps):
    return (f'<aside class="cs" aria-label="{e(titre)}"><h3 class="cs-t">{titre}</h3>{corps}</aside>')


def encadre_alerte(corps):
    return f'<aside class="alerte-b" aria-label="Drapeaux rouges"><h3 class="alerte-t">Drapeaux rouges</h3>{corps}</aside>'


def table(entetes, lignes, nom):
    if not lignes:
        return ""
    th = "".join(f'<th scope="col">{x}</th>' for x in entetes)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in lignes)
    return (f'<div class="defile" tabindex="0" role="region" aria-label="{e(nom)} — défilement horizontal">'
            f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>")


# ---------------------------------------------------------------- Status
def rendre_status(d):
    sid = d["id"]
    duree = d.get("duree") or {}
    h = [bandeau(sid, d.get("titre", ""), [
        ("Région", txt(d.get("region", "—"))), ("Système", txt(d.get("systeme", "—"))),
        ('<abbr title="%s">EPA</abbr>' % e(SIGLES.get("EPA", "")), txt(d.get("epa", "—"))),
        ("Niveau", niveau(d.get("niveau"))),
        ("Durée complète", txt(duree.get("complet", "—"))),
        (f'Durée <abbr title="{e(CS_T)}">CS</abbr>', txt(duree.get("cs", "—")))])]
    h.append(f'<div class="deuxcol"><div>{h3("Matériel")}{liste(d.get("materiel"))}</div>'
             f'<div>{h3("Installation")}{liste(d.get("installation"))}</div></div>')
    temps = sorted(d.get("examen_complet") or [],
                   key=lambda t: TEMPS_ORDRE.index(t.get("temps")) if t.get("temps") in TEMPS_ORDRE else 99)
    if temps:
        h.append('<h3 class="temps titre-section">Examen complet</h3>')
    for t in temps:
        lignes = []
        for g in t.get("gestes", []):
            ans = "".join(
                f'<li><strong>{txt(a.get("signe", ""))}</strong> → {txt(a.get("signifie", ""))}</li>'
                if isinstance(a, dict) else f"<li>{txt(a)}</li>" for a in as_list(g.get("anomalies")))
            lignes.append([txt(g.get("geste", "")), txt(g.get("normal", "")), f"<ul>{ans}</ul>" if ans else "—"])
        h.append(f'<h4 class="temps">{e(t.get("temps", ""))}</h4>'
                 + table(["Geste", "Normal", "Anomalies → signification"], lignes, f'Tableau {t.get("temps", "")}'))
    ms = d.get("manoeuvres_speciales") or []
    if ms:
        h.append('<h3 class="temps titre-section">Manœuvres spéciales</h3><div class="cartes">')
        for m in ms:
            h.append(
                f'<article class="carte"><h4 class="carte-t">{txt(m.get("nom", ""))}</h4>'
                + (f'<p><span class="lab">But</span> {txt(m["but"])}</p>' if m.get("but") else "")
                + f'<h5 class="carte-t">Technique</h5>{liste(m.get("technique"), "ol")}'
                f'<h5 class="carte-t">Positif si</h5><p>{txt(m.get("positif_si", "—"))}</p>'
                f'<h5 class="carte-t">Valeur</h5><p>{txt(m.get("valeur", "À vérifier"))}</p>'
                f'<h5 class="carte-t">Interprétation</h5><p>{txt(m.get("interpretation", "—"))}</p>'
                f'{rendre_image(m.get("image"), m.get("nom", ""), sid)}</article>')
        h.append("</div>")
    v = d.get("version_cs") or {}
    if v:
        h.append(encadre_cs(f'Version <abbr title="{e(CS_T)}">CS</abbr> (13 min)',
                            (f'<p><span class="lab">Cible</span> {txt(v["cible"])}</p>' if v.get("cible") else "")
                            + '<h4 class="cs-t">À dire à voix haute</h4>' + liste(v.get("a_dire"))
                            + '<h4 class="cs-t">À nommer sans faire</h4>' + liste(v.get("a_nommer_sans_faire"))
                            + '<h4 class="cs-t">Pièges</h4>' + liste(v.get("pieges"))))
    if d.get("syndromes_lies"):
        h.append(h3("Syndromes liés") + pastilles(d["syndromes_lies"]))
    if d.get("sources"):
        h.append(h3("Sources") + liste(d["sources"], "ol", "sources"))
    return section(sid, "".join(h))


# ---------------------------------------------------------------- Syndromes
def code_systeme(s):
    s0 = str(s or "").split("/")[0].lower()
    m = re.search(r"\((S\d+|T)\)", str(s or ""))
    if m:
        return m.group(1)
    for code, cle in SYSTEME_CLES:
        if cle in s0:
            return code
    return "T"


def ordre_code(c):
    return 99 if c == "T" else int(c[1:])


def rendre_syndrome(d):
    sid = d["id"]
    h = [bandeau(sid, d.get("titre", ""), [
        ("Système", txt(d.get("systeme", "—"))), ("Région", txt(d.get("region", "—"))),
        ("Niveau", niveau(d.get("niveau")))])]
    if d.get("definition"):
        h.append(h3("Définition") + f'<p>{txt(d["definition"])}</p>')
    h.append('<div class="deuxcol egal">')
    h.append(f'<div>{h3("Symptômes")}{liste(d.get("symptomes"))}</div>')
    h.append(f'<div>{h3("Physiopathologie")}{liste(d.get("physiopathologie"))}</div></div>')
    sig = [s for s in as_list(d.get("signes"))]
    if sig:
        avec_val = any(isinstance(s, dict) and s.get("valeur") for s in sig)
        lignes = []
        for s in sig:
            if isinstance(s, dict):
                l = [txt(s.get("signe", "")), txt(s.get("comment_le_chercher", "—"))]
                if avec_val:
                    l.append(txt(s.get("valeur", "—")))
            else:
                l = [txt(s), "—"] + (["—"] if avec_val else [])
            lignes.append(l)
        h.append(h3("Signes") + table(["Signe", "Comment le chercher (renvoi status)"] + (["Valeur"] if avec_val else []),
                                      lignes, "Signes"))
    eti = as_list(d.get("etiologies"))
    if eti:
        lignes = [[f'<strong>{txt(x.get("lettre", ""))}</strong>', liste(x.get("causes")) or "—"]
                  if isinstance(x, dict) else ["", txt(x)] for x in eti]
        h.append(h3("Étiologies — VITE DIT CAFé") + table(["Lettre", "Causes"], lignes, "Étiologies").replace(
            "<table>", '<table class="etroit">'))
    if d.get("drapeaux_rouges"):
        h.append(encadre_alerte(liste(d["drapeaux_rouges"])))
    ex = as_list(d.get("examens_cles"))
    if ex:
        items = []
        for x in ex:
            if isinstance(x, dict):
                r = f' <span class="renvoi">[{e(x["renvoi"])}]</span>' if x.get("renvoi") else ""
                items.append(f'<li><strong>{txt(x.get("examen", ""))}</strong> — {txt(x.get("pourquoi", ""))}{r}</li>')
            else:
                items.append(f"<li>{txt(x)}</li>")
        h.append(h3("Examens clés") + "<ul>" + "".join(items) + "</ul>")
    h.append('<div class="deuxcol egal">')
    h.append(f'<div>{h3("Management initial")}{liste(d.get("management_initial"))}</div>')
    h.append(f'<div>{h3("Diagnostics différentiels")}{liste(d.get("diagnostics_differentiels"))}</div></div>')
    if d.get("a_dire_cs"):
        h.append(encadre_cs(f'Synthèse orale <abbr title="{e(CS_T)}">CS</abbr>', liste(d["a_dire_cs"])))
    img = rendre_image(d.get("image"), d.get("titre", ""), sid)
    if img:
        h.append(h3("Image") + f'<div class="img-seule">{img}</div>')
    if d.get("status_lies"):
        h.append(h3("Status liés") + pastilles(d["status_lies"]))
    if d.get("sources"):
        h.append(h3("Sources") + liste(d["sources"], "ol", "sources"))
    return section(sid, "".join(h))


# ---------------------------------------------------------------- Anamnèse
def rendre_etapes(etapes):
    out = []
    for x in as_list(etapes):
        if not isinstance(x, dict):
            out.append(f"<li>{txt(x)}</li>")
            continue
        corps = ""
        faire = as_list(x.get("faire"))
        dire = as_list(x.get("dire"))
        if faire:
            corps += '<h5 class="carte-t">Faire</h5>' + (liste(faire) if len(faire) > 1 else f"<p>{txt(faire[0])}</p>")
        if dire:
            corps += '<h5 class="carte-t">Dire</h5>' + liste(dire)
        if x.get("ref"):
            corps += f'<p class="credit">Référence : {txt(x["ref"])}</p>'
        out.append(f'<article class="carte"><h4 class="carte-t">{txt(x.get("etape", ""))}</h4>{corps}</article>')
    return '<div class="cartes">' + "".join(out) + "</div>" if out else ""


def rendre_anamnese(d):
    sid = d["id"]
    h = [bandeau(sid, d.get("titre", ""), [
        ("Système", txt(d.get("systeme", "—"))), ("Niveau", niveau(d.get("niveau"))),
        ("SSP / EPA", txt(d.get("ssp", "")))])]
    if d.get("ouverture"):
        h.append(h3("Ouverture") + f'<blockquote class="citation">{txt(d["ouverture"])}</blockquote>')
    if d.get("etapes"):
        h.append(h3("Étapes") + rendre_etapes(d["etapes"]))
    qs = as_list(d.get("questions"))
    if qs:
        lignes = [[f'<strong>{txt(q.get("axe", ""))}</strong>', liste(q.get("items"))] if isinstance(q, dict)
                  else ["", txt(q)] for q in qs]
        h.append(h3("Questions par axe") + table(["Axe", "Questions au patient"], lignes, "Questions").replace(
            "<table>", '<table class="etroit">'))
    dr = as_list(d.get("drapeaux_rouges"))
    if dr:
        h.append(encadre_alerte("<ul>" + "".join(
            f'<li><strong>{txt(x.get("question", ""))}</strong> → {txt(x.get("si_oui", ""))}</li>'
            if isinstance(x, dict) else f"<li>{txt(x)}</li>" for x in dr) + "</ul>"))
    hy = as_list(d.get("hypotheses"))
    if hy:
        lignes = [[f'<strong>{txt(x.get("lettre", ""))}</strong>', liste(x.get("diagnostics")) or "—",
                   txt(x.get("question_discriminante", "—"))] if isinstance(x, dict) else ["", txt(x), ""] for x in hy]
        h.append(h3("Hypothèses — VITE DIT CAFé") + table(["Lettre", "Diagnostics", "Question discriminante"], lignes,
                                                          "Hypothèses"))
    if d.get("idees_craintes_attentes"):
        h.append(h3("Idées, craintes, attentes") + liste(d["idees_craintes_attentes"]))
    li = d.get("liens") or {}
    if isinstance(li, dict):
        if li.get("status"):
            h.append(h3("Status liés") + pastilles(li["status"]))
        if li.get("syndromes"):
            h.append(h3("Syndromes liés") + pastilles(li["syndromes"]))
        if li.get("imagerie"):
            h.append(h3("Imagerie liée") + '<p class="credit">' + e(", ".join(li["imagerie"])) + "</p>")
    elif li:
        h.append(h3("Liens") + pastilles(li))
    if d.get("synthese_cs"):
        h.append(encadre_cs(f'Synthèse orale <abbr title="{e(CS_T)}">CS</abbr>', f'<p>{txt(d["synthese_cs"])}</p>'))
    if d.get("pieges"):
        h.append(h3("Pièges") + liste(d["pieges"]))
    if d.get("sources"):
        h.append(h3("Sources") + liste(d["sources"], "ol", "sources"))
    return section(sid, "".join(h))


# ---------------------------------------------------------------- Management / Communication
def rendre_mk(d):
    sid = d["id"]
    h = [bandeau(sid, d.get("titre", ""), [("Niveau", niveau(d.get("niveau")))])]
    if d.get("objectif"):
        h.append(h3("Objectif") + f'<p>{txt(d["objectif"])}</p>')
    if d.get("etapes"):
        h.append(h3("Étapes") + rendre_etapes(d["etapes"]))
    h.append('<div class="deuxcol egal">')
    h.append(f'<div>{h3("Grille : ce qui rapporte")}{liste(d.get("grille"))}</div>')
    h.append(f'<div>{h3("Erreurs")}{liste(d.get("erreurs"))}</div></div>')
    if d.get("exemple_station"):
        h.append(encadre_cs("Exemple de station", "".join(f"<p>{txt(p)}</p>" for p in as_list(d["exemple_station"]))))
    li = d.get("liens")
    if isinstance(li, dict):
        li = [x for v in li.values() for x in as_list(v)]
    if li:
        h.append(h3("Liens") + pastilles(li))
    if d.get("sources"):
        h.append(h3("Sources") + liste(d["sources"], "ol", "sources"))
    return section(sid, "".join(h))


# ---------------------------------------------------------------- assemblage
def entree_menu(sid, titre, present):
    return f'<li><a href="#{e(sid)}"{"" if present else " class=absent"}>{e(sid)} {e(titre)}</a></li>'


def onglet_status():
    menu, corps = [], []
    for nom, plage in GROUPES_STATUS:
        menu.append(f"<h2>{e(nom)}</h2><ul>")
        for i in plage:
            sid = f"S-{i:02d}"
            t = (F_S.get(sid) or {}).get("titre") or REC_S.get(sid, {}).get("titre", "")
            menu.append(entree_menu(sid, t, sid in F_S))
            corps.append(rendre_status(F_S[sid]) if sid in F_S else absente(sid, t, f"{sid}.json" in ILL_S))
        menu.append("</ul>")
    for sid in sorted(set(F_S) - {f"S-{i:02d}" for i in range(1, 36)}):
        corps.append(rendre_status(F_S[sid]))
    return "".join(menu), "".join(corps), len(F_S), 35, ILL_S


def onglet_syndromes():
    ids = sorted(set(REC_SY) | set(F_SY), key=lambda x: int(x.split("-")[1]) if x.split("-")[1].isdigit() else 999)
    groupes = {}
    for sid in ids:
        d = F_SY.get(sid) or REC_SY.get(sid, {})
        code = code_systeme(d.get("systeme"))
        groupes.setdefault(code, []).append(sid)
    menu, corps = [], []
    for code in sorted(groupes, key=ordre_code):
        menu.append(f"<h2>{e(NOMS_SYSTEMES.get(code, code))}</h2><ul>")
        corps.append(f'<h2 class="groupe">{e(NOMS_SYSTEMES.get(code, code))}</h2>')
        for sid in groupes[code]:
            t = (F_SY.get(sid) or {}).get("titre") or REC_SY.get(sid, {}).get("titre", "")
            menu.append(entree_menu(sid, t, sid in F_SY))
            corps.append(rendre_syndrome(F_SY[sid]) if sid in F_SY else absente(sid, t, f"{sid}.json" in ILL_SY))
        menu.append("</ul>")
    return "".join(menu), "".join(corps), len(F_SY), len(ids), ILL_SY


def onglet_simple(rec, fic, ill, rendu, groupes_fn):
    ids = list(rec) + [k for k in fic if k not in rec]
    menu, corps, courant = [], [], None
    for sid in ids:
        g = groupes_fn(sid)
        if g != courant:
            if courant is not None:
                menu.append("</ul>")
            menu.append(f"<h2>{e(g)}</h2><ul>")
            courant = g
        t = (fic.get(sid) or {}).get("titre") or rec.get(sid, {}).get("titre", "")
        menu.append(entree_menu(sid, t, sid in fic))
        corps.append(rendu(fic[sid]) if sid in fic else absente(sid, t, f"{sid}.json" in ill))
    if courant is not None:
        menu.append("</ul>")
    return "".join(menu), "".join(corps), len(fic), len(ids), ill


def groupe_a(sid):
    if sid.startswith("A-TRAME"):
        return "Trame"
    if sid.startswith("A-SPE"):
        return "Anamnèses spécifiques"
    return "Motifs de consultation"


ONGLETS = [
    ("status", "Status", onglet_status),
    ("syndromes", "Syndromes", onglet_syndromes),
    ("anamnese", "Anamnèse", lambda: onglet_simple(REC_A, F_A, ILL_A, rendre_anamnese, groupe_a)),
    ("management", "Management", lambda: onglet_simple(REC_M, F_M, ILL_M, rendre_mk, lambda s: "Management")),
    ("communication", "Communication", lambda: onglet_simple(REC_K, F_K, ILL_K, rendre_mk, lambda s: "Communication")),
]

CSS = """
:root{--fiche:%(fiche)s;--temps:%(temps)s;--carte:%(carte)s;--cs:%(cs)s;--alerte:%(alerte)s;--trait:#5A5A5A;--fin:#BDBDBD}
*{box-sizing:border-box}
html{scroll-padding-top:76px}
body{margin:0;background:#FFFFFF;color:#000000;font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
a{color:#000000;text-decoration:underline}
abbr[title]{text-decoration:underline dotted;cursor:help}
.saut{position:absolute;left:-9999px}.saut:focus{left:16px;top:8px;background:#FFFFFF;padding:8px;border:2px solid #000;z-index:50}
.cadre{display:grid;grid-template-columns:290px minmax(0,1fr);min-height:100vh}
.menus{position:sticky;top:0;height:100vh;overflow-y:auto;border-right:1px solid var(--fin);padding:16px 12px 32px;background:#FFFFFF}
.menus .marque{font-weight:700;font-size:1.05rem;color:var(--fiche);margin:0 0 4px}
nav.menu h2{font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;margin:16px 0 4px;color:#000}
nav.menu ul{list-style:none;margin:0;padding:0}
nav.menu a{display:block;padding:4px 8px;text-decoration:none;border-left:3px solid transparent;font-size:.92rem}
nav.menu a:hover,nav.menu a:focus{text-decoration:underline}
nav.menu a[aria-current=true]{border-left-color:#000;font-weight:700}
nav.menu a.absent{font-style:italic}
.basc{display:none}
main{padding:0 32px 64px;max-width:1180px;min-width:0}
.onglets{position:sticky;top:0;z-index:15;background:#FFFFFF;display:flex;flex-wrap:wrap;gap:4px 8px;padding:12px 0 0;border-bottom:2px solid #000;margin:0 0 8px}
.onglets button{font:600 1rem system-ui,sans-serif;color:#000;background:#FFFFFF;border:1px solid var(--trait);border-bottom:0;padding:8px 14px;cursor:pointer}
.onglets button[aria-selected=true]{border:2px solid #000;border-bottom:4px solid #FFFFFF;margin-bottom:-2px;font-weight:800}
.onglets button:focus-visible{outline:3px solid #000;outline-offset:2px}
.onglets .compte{font-weight:400;font-size:.85rem}
.panneau>h1{font-size:1.6rem;margin:16px 0 4px;color:var(--fiche)}
.chapeau{margin:0 0 8px}
.alerte-liste{border:2px solid #000;padding:8px 12px;margin:12px 0}
main p,main li,main dd,figcaption,td{overflow-wrap:break-word}
.sources,.credit,.afournir{overflow-wrap:anywhere}
h2.groupe{font-size:1.1rem;text-transform:uppercase;letter-spacing:.04em;margin:48px 0 0;color:#000;border-bottom:1px solid #000}
.fiche{border-top:3px solid var(--fiche);padding-top:8px;margin:40px 0 0}
h2.groupe+.fiche{margin-top:16px}
.bandeau h2{color:var(--fiche);font-size:1.5rem;margin:4px 0 8px}
.sid{font-variant-numeric:tabular-nums;margin-right:.3em}
.meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:4px 20px;margin:0 0 8px;padding:8px 0;border-bottom:1px solid var(--fin)}
.meta div{min-width:0}.meta dt{font-weight:700;font-size:.82rem}.meta dd{margin:0}
h3.temps,h4.temps{color:var(--temps)}
h3.temps{font-size:1.15rem;margin:20px 0 6px}
h3.titre-section{font-size:1.25rem;border-bottom:1px solid var(--temps);padding-bottom:2px;margin-top:28px}
h4.temps{font-size:1.05rem;margin:16px 0 6px}
.deuxcol{display:grid;grid-template-columns:1fr 2fr;gap:0 32px}
.deuxcol.egal{grid-template-columns:1fr 1fr}
.deuxcol>div{min-width:0}
main ul{padding-left:1.2em}
.deuxcol ul{margin:0}
.defile{overflow-x:auto;border:1px solid var(--fin);max-width:100%%}
.defile:focus{outline:2px solid #000}
table{border-collapse:collapse;width:100%%;min-width:720px}
table.etroit{min-width:0}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--fin)}
th{font-weight:700;border-bottom:2px solid #000;background:#FFFFFF}
td ul{margin:0;padding-left:1.1em}td li{margin:0 0 4px}
table.etroit td:first-child{width:28%%}
.cartes{display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:16px}
.carte{border:1px solid var(--trait);padding:12px 14px;min-width:0}
.carte h4.carte-t{font-size:1.05rem;margin:0 0 6px}
.carte-t{color:var(--carte)}
h5.carte-t{font-size:.9rem;margin:10px 0 2px}
.carte p{margin:0}.carte ol,.carte ul{margin:0;padding-left:1.4em}
.lab{font-weight:700;margin-right:.3em}
.citation{margin:0;padding:8px 14px;border-left:3px solid #000;font-style:italic}
.fig{margin:12px 0 0}
.img-seule{max-width:520px}
.vignette{display:block;padding:0;border:1px solid var(--trait);background:#FFFFFF;cursor:zoom-in;width:100%%;color:#000}
.vignette img{display:block;width:100%%;max-height:240px;object-fit:contain;background:#FFFFFF}
.vignette:focus{outline:3px solid #000;outline-offset:2px}
.vignette.occulte{min-height:140px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;border:2px dashed #000;font:700 1rem system-ui,sans-serif}
.vignette.occulte .petit{font-weight:400;font-size:.85rem}
figcaption{font-size:.9rem;margin-top:4px}
.credit{font-size:.82rem;margin:2px 0 0}
.renvoi{font-size:.85rem}
.afournir{border:1px dashed #000;padding:8px 10px;margin:12px 0 0;font-size:.92rem}
.cs{border:3px solid var(--cs);padding:12px 16px;margin:28px 0 0}
.cs-t{color:var(--cs)}
h3.cs-t{margin:0 0 6px;font-size:1.2rem}
h4.cs-t{margin:12px 0 4px;font-size:1rem}
.cs ul{margin:0}
.alerte-b{border:3px solid var(--alerte);padding:12px 16px;margin:24px 0 0}
h3.alerte-t{color:var(--alerte);margin:0 0 6px;font-size:1.15rem}
.alerte-b ul{margin:0}
.pastilles{list-style:none;padding:0!important;margin:0;display:flex;flex-wrap:wrap;gap:8px}
.pastille{display:inline-block;border:1px solid #000;border-radius:999px;padding:2px 12px;font-size:.88rem;text-decoration:none}
.pastille:hover,.pastille:focus{text-decoration:underline}
.sources{font-size:.9rem;padding-left:1.4em}
.vide{border:1px dashed #000;padding:12px 14px;margin:16px 0}
body.modal-ouverte .cadre{filter:blur(6px)}
#fenetre{position:fixed;inset:0;display:none;align-items:center;justify-content:center;padding:16px;background:rgba(255,255,255,.55);z-index:100}
#fenetre.ouverte{display:flex}
#fenetre .boite{background:#FFFFFF;border:2px solid #000;max-width:min(1100px,100%%);max-height:100%%;overflow:auto;padding:12px 14px;position:relative}
#fenetre img{display:block;max-width:100%%;max-height:72vh;margin:0 auto}
#fenetre .fermer{position:absolute;top:6px;right:6px;font:700 1rem system-ui,sans-serif;background:#FFFFFF;color:#000;border:2px solid #000;padding:4px 10px;cursor:pointer}
#fenetre .leg{margin:8px 40px 0 0}
#fenetre .cr{font-size:.85rem;margin:4px 0 0}
@media (max-width:860px){
 html{scroll-padding-top:130px}
 .cadre{display:block}
 .basc{display:block;width:100%%;text-align:left;background:#FFFFFF;color:#000;border:0;border-bottom:2px solid #000;font:700 1rem system-ui,sans-serif;padding:10px 0 8px;cursor:pointer}
 .menus{position:static;height:auto;border-right:0;padding:0 16px}
 .menus .marque{display:none}
 .menus nav.menu{display:none!important;padding-bottom:16px;border-bottom:1px solid var(--fin)}
 .menus.ouvert nav.menu.actif{display:block!important}
 main{padding:0 16px 48px}
 .onglets button{padding:6px 10px;font-size:.92rem}
 .deuxcol,.deuxcol.egal{grid-template-columns:1fr}
 .cartes{grid-template-columns:minmax(0,1fr)}
 table{min-width:600px}
 table.etroit{min-width:0}
 .meta{grid-template-columns:1fr}
}
@media print{.menus,.basc,.onglets{display:none}.cadre{display:block}.defile{overflow:visible}.panneau[hidden]{display:block}}
""" % COULEURS

JS = r"""
(function(){
 var panneaux=[].slice.call(document.querySelectorAll('.panneau')),menus=[].slice.call(document.querySelectorAll('nav.menu')),
     boutons=[].slice.call(document.querySelectorAll('.onglets button')),boiteMenus=document.querySelector('.menus'),
     basc=document.querySelector('.basc');
 function activer(nom){
  panneaux.forEach(function(p){p.hidden=p.dataset.onglet!==nom;});
  menus.forEach(function(m){var a=m.dataset.onglet===nom;m.hidden=!a;m.classList.toggle('actif',a);});
  boutons.forEach(function(b){var a=b.dataset.onglet===nom;b.setAttribute('aria-selected',a?'true':'false');b.tabIndex=a?0:-1;});
  try{localStorage.setItem('semio-onglet',nom);}catch(e){}
 }
 function route(){
  var h=decodeURIComponent(location.hash.slice(1));
  if(h.indexOf('onglet-')===0){activer(h.slice(7));window.scrollTo(0,0);return;}
  var el=h&&document.getElementById(h);
  if(el){var p=el.closest('.panneau');if(p){activer(p.dataset.onglet);el.scrollIntoView();}}
 }
 boutons.forEach(function(b,i){
  b.addEventListener('click',function(){history.pushState(null,'','#onglet-'+b.dataset.onglet);activer(b.dataset.onglet);window.scrollTo(0,0);});
  b.addEventListener('keydown',function(ev){var d=ev.key==='ArrowRight'?1:ev.key==='ArrowLeft'?-1:0;if(!d)return;
   var n=boutons[(i+d+boutons.length)%boutons.length];n.focus();n.click();});
 });
 window.addEventListener('hashchange',route);
 if(location.hash){route();}else{var s=null;try{s=localStorage.getItem('semio-onglet');}catch(e){}activer(s&&document.querySelector('.panneau[data-onglet="'+s+'"]')?s:'status');}
 basc.addEventListener('click',function(){var o=boiteMenus.classList.toggle('ouvert');basc.setAttribute('aria-expanded',o?'true':'false');});
 boiteMenus.addEventListener('click',function(ev){if(ev.target.closest('a')){boiteMenus.classList.remove('ouvert');basc.setAttribute('aria-expanded','false');}});
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
 if('IntersectionObserver' in window){
  var liens={};menus.forEach(function(m){m.querySelectorAll('a[href^="#"]').forEach(function(a){liens[a.getAttribute('href').slice(1)]=a;});});
  var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){var a=liens[x.target.id];if(!a)return;
   a.closest('nav').querySelectorAll('a[aria-current]').forEach(function(z){z.removeAttribute('aria-current');});
   a.setAttribute('aria-current','true');}});},{rootMargin:'0px 0px -80% 0px'});
  document.querySelectorAll('section.fiche').forEach(function(s){io.observe(s);});}
})();
"""


def main():
    navs, panneaux, boutons, total = [], [], [], 0
    for cle, nom, fn in ONGLETS:
        menu, corps, n, attendu, ill = fn()
        total += n
        alerte = (f'<p class="alerte-liste">JSON illisible(s) sauté(s) : {e(", ".join(ill))}.</p>' if ill else "")
        if n == 0:
            alerte += '<p class="vide">Fiches en cours d’écriture : aucune fiche lisible à cette génération. Le menu liste le plan prévu.</p>'
        navs.append(f'<nav class="menu" data-onglet="{cle}" aria-label="Fiches — {e(nom)}">{menu}</nav>')
        boutons.append(f'<button type="button" role="tab" id="tab-{cle}" data-onglet="{cle}" aria-controls="p-{cle}" '
                       f'aria-selected="false">{e(nom)} <span class="compte">({n}/{attendu})</span></button>')
        panneaux.append(f'<div class="panneau" id="p-{cle}" role="tabpanel" aria-labelledby="tab-{cle}" data-onglet="{cle}">'
                        f'<h1>Sémiologie — {e(nom)}</h1><p class="chapeau">{n} fiche(s) rédigée(s) sur {attendu}. '
                        f'Niveau <abbr title="niveau minimal exigé">MIN</abbr> ou <abbr title="niveau cible">CIBLE</abbr> ; '
                        f'encadrés <abbr title="{e(CS_T)}">CS</abbr> pour la station de 13 min.</p>{alerte}{corps}</div>')
    page = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sémiologie clinique</title><style>{CSS}</style></head>
<body><a class="saut" href="#contenu">Aller au contenu</a>
<div class="cadre">
<div class="menus"><p class="marque">Sémiologie</p>
<button type="button" class="basc" aria-expanded="false">☰ Menu des fiches de l’onglet</button>{"".join(navs)}</div>
<main id="contenu"><div class="onglets" role="tablist" aria-label="Volets de la sémiologie">{"".join(boutons)}</div>
{"".join(panneaux)}</main></div>
<div id="fenetre" role="dialog" aria-modal="true" aria-label="Image agrandie" aria-hidden="true">
<div class="boite"><button type="button" class="fermer" aria-label="Fermer la fenêtre">✕ Fermer</button>
<img alt=""><p class="leg"></p><p class="cr"></p></div></div>
<script>{JS}</script></body></html>
"""
    with open(SORTIE, "w", encoding="utf-8") as h:
        h.write(page)
    alias = ("<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\"><title>Sémiologie Status</title>"
             "<meta http-equiv=\"refresh\" content=\"0; url=SEMIOLOGIE.html#onglet-status\">"
             "<script>location.replace('SEMIOLOGIE.html'+(location.hash||'#onglet-status'));</script></head>"
             "<body style=\"background:#FFFFFF;color:#000000\"><p>Page déplacée : "
             "<a href=\"SEMIOLOGIE.html#onglet-status\">SEMIOLOGIE.html</a>.</p></body></html>")
    with open(ALIAS, "w", encoding="utf-8") as h:
        h.write(alias)
    print(f"SEMIOLOGIE.html : {total} fiches, {len(SIGNALEMENTS)} signalement(s), {len(page)//1024} Ko ; STATUS.html = alias")


if __name__ == "__main__":
    main()
