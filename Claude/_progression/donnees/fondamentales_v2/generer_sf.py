#!/usr/bin/env python3
"""Génère SCIENCES_FONDAMENTALES.html : 1 Anatomie (en préparation), 2 Physiologie
(physiologie/PHY-*.json), 3 Physiopathologie (physiopathologie/PP-*.json), 4 Sémiologie
(lien vers ../semiologie/SEMIOLOGIE.html).

Les JSON viennent de plusieurs agents : adapter_phy() et adapter_pp() ramènent leurs
variantes de champs à un modèle unique, sans modifier les fichiers. Relit les dossiers
à chaque exécution ; un JSON illisible est sauté et signalé.
Règle EYE SPOT : fond blanc, texte noir ; une couleur par rôle de titre.
"""
import glob
import html
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RECENSEMENT = os.path.normpath(os.path.join(ICI, "..", "..", "recensement_sf", "recensement_sf.json"))
SEMIO = "../semiologie/SEMIOLOGIE.html"
SORTIE = os.path.join(ICI, "SCIENCES_FONDAMENTALES.html")

COULEURS = {
    "fiche": "#0B3B8C",    # bandeau et titre de fiche
    "temps": "#0B5A2E",    # titres de rubriques
    "carte": "#6A1B7A",    # sous-titres des cartes et étapes de la chaîne
    "formule": "#8A3B00",  # encadré « Formule et exemple résolu » (réservée)
}
LETTRES = [("V", "Vasculaire"), ("I", "Infectieux"), ("T", "Tumoral"), ("D", "Dégénératif"),
           ("Ia", "Iatrogène, toxique"), ("Tr", "Traumatique"), ("C", "Congénital"),
           ("A", "Auto-immun, inflammatoire"), ("F", "Fonctionnel, métabolique")]
NOM_LETTRE = dict(LETTRES)
ETAPES = ["Normal", "Altération", "Lésion", "Signes"]
SIGLES_SUPPL = {"EIC": "espace intercostal", "IMC": "indice de masse corporelle", "OMS": "Organisation mondiale de la santé",
                "ESC": "Société européenne de cardiologie", "LIN": "limite inférieure de la normale",
                "ATP": "adénosine triphosphate", "SNC": "système nerveux central"}
SIGLES_EXCLUS = {"OR", "NET", "NURSE", "KK", "SA", "CD", "TR", "PS", "IC", "PL", "CS"}


def ratio(hexa):
    def lin(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hexa[i:i + 2], 16) for i in (1, 3, 5))
    return 1.05 / (0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b) + 0.05)


for _k, _c in COULEURS.items():
    assert ratio(_c) >= 7, f"contraste insuffisant {_k}"

REC = json.load(open(RECENSEMENT, encoding="utf-8"))
SYSTEMES = [s for s in REC.get("systemes", []) if s["code"] != "T"]
NOM_SYS = {s["code"]: s["nom"] for s in REC.get("systemes", [])}
SIGLES = {k: v for k, v in REC.get("sigles", {}).items() if k not in SIGLES_EXCLUS}
SIGLES.update(SIGLES_SUPPL)
TITRES_SEMIO = {}
for x in REC["semiologie"]["S"]:
    m = re.match(r"SY-0*(\d+)$", x["id"])
    TITRES_SEMIO[f"SY-{int(m.group(1))}" if m else x["id"]] = x.get("titre", "")
SIGNALEMENTS = []


def signaler(m):
    SIGNALEMENTS.append(m)
    print(f"[signalement] {m}", file=sys.stderr)


def e(t):
    return html.escape(str(t), quote=True)


def L(v):
    if v is None or v == "":
        return []
    return v if isinstance(v, list) else [v]


def premier(d, *cles, defaut=None):
    for k in cles:
        if d.get(k) not in (None, "", []):
            return d[k]
    return defaut


def ids_de(v):
    """Liste d'identifiants depuis str, dict {id}, liste de str ou de dict."""
    out = []
    for x in L(v):
        if isinstance(x, dict):
            if x.get("id"):
                out.append(str(x["id"]))
        elif str(x).strip():
            out.append(str(x).strip())
    return out


def norm_sem(i):
    m = re.match(r"SY-0*(\d+)$", i)
    if m:
        return f"SY-{int(m.group(1))}"
    m = re.match(r"S-(\d+)$", i)
    if m:
        return f"S-{int(m.group(1)):02d}"
    return i


def cibles(v):
    """cible/classe/cibles_* → [(nom, pourquoi)]."""
    out = []
    for x in L(v):
        if isinstance(x, dict):
            out.append((premier(x, "cible", "classe", "nom", "titre", defaut=""), x.get("pourquoi", "")))
        else:
            out.append((str(x), ""))
    return out


def sources(v):
    out = []
    for s in L(v):
        if isinstance(s, dict):
            extra = [s.get(k) for k in ("etiquette", "origine", "via", "recence", "statut") if s.get(k)]
            out.append(s.get("ref", "") + (f" ({' ; '.join(extra)})" if extra else ""))
        else:
            out.append(str(s))
    return out


# ---------------------------------------------------------------- adaptation (unique point de normalisation)
def adapter_phy(j):
    boucle = premier(j, "boucle", "chaine_regulation", defaut=None)
    formules = []
    for f in L(premier(j, "formule", "formules", "calculs", "calcul", defaut=None)):
        if isinstance(f, dict):
            formules.append({"expression": premier(f, "expression", "formule", "calcul", defaut=""),
                             "usage": f.get("usage", ""), "exemple": premier(f, "exemple", "exemple_resolu", defaut="")})
        elif f:
            formules.append({"expression": str(f), "usage": "", "exemple": ""})
    der = []
    for d in L(premier(j, "dereglements", "affections", defaut=[])):
        if isinstance(d, dict):
            der.append({"titre": premier(d, "titre", "affection", "nom", defaut=""), "mecanisme": L(d.get("mecanisme")),
                        "pp": ids_de(premier(d, "pp", "renvoi_physiopathologie", "renvois_physiopathologie")),
                        "semio": [norm_sem(i) for i in ids_de(premier(d, "semiologie", "renvois_semiologie", "renvoi_semiologie"))]})
        else:
            der.append({"titre": str(d), "mecanisme": [], "pp": [], "semio": []})
    pas = [p for p in L(j.get("passerelles")) if isinstance(p, dict)]
    return {
        "id": j["id"], "type": "PHY", "systeme": j.get("systeme", "?"),
        "titre": premier(j, "titre", "fonction", "nom", defaut=j["id"]),
        "niveau": j.get("niveau"), "statut": j.get("statut"), "date": j.get("date"),
        "definition": j.get("definition", ""), "boucle": boucle if isinstance(boucle, dict) else None,
        "mecanisme": L(j.get("mecanisme")), "valeurs": [v for v in L(j.get("valeurs_normales")) if v],
        "regulation": j.get("regulation", ""), "formules": formules, "lien_clinique": j.get("lien_clinique", ""),
        "dereglements": der,
        "cibles": cibles(premier(j, "cibles_pharmacologiques", "cible_pharmacologique", "cibles", "cible", "classe",
                                 "cibles_therapeutiques", "cible_therapeutique")),
        "mnemo": premier(j, "mnemotechnique", "mnemo", defaut=""), "passerelles": pas,
        "sources": sources(j.get("sources")), "honnetete": j.get("honnetete", ""),
    }


def adapter_affection(a):
    if not isinstance(a, dict):
        return {"titre": str(a), "mecanisme": [], "clinique": "", "semio": [], "examen": "", "examens": [],
                "imagerie": [], "cibles": [], "pharmaco": [], "fiches": [], "mnemo": ""}
    return {
        "titre": premier(a, "titre", "nom", "affection", defaut=""),
        "mecanisme": L(a.get("mecanisme")),
        "clinique": premier(a, "consequence_clinique", "clinique", defaut=""),
        "semio": [norm_sem(i) for i in ids_de(premier(a, "renvois_semiologie", "renvoi_semiologie", "semiologie"))],
        "examen": premier(a, "examen_revelateur", "examen", defaut=""),
        "examens": ids_de(premier(a, "examens", "renvois_examen", "renvoi_examens", "renvois_examens")),
        "imagerie": ids_de(premier(a, "imagerie", "renvoi_imagerie", "renvois_imagerie")),
        "cibles": cibles(premier(a, "cibles_therapeutiques", "cible_therapeutique", "cible_pharmacologique",
                                 "cibles", "cible", "classe")),
        "pharmaco": ids_de(premier(a, "renvoi_pharmaco", "renvois_pharmaco")),
        "fiches": ids_de(premier(a, "renvoi_fiche", "renvoi_physiopathologie", "renvois_physiopathologie")),
        "mnemo": a.get("mnemotechnique", ""),
    }


def adapter_pp(j):
    det = L(premier(j, "detail_affections", defaut=None))
    brut = L(j.get("affections"))
    if det:
        noms = {str(premier(d, "nom", "titre", defaut="")) for d in det if isinstance(d, dict)}
        aff = [adapter_affection(d) for d in det] + [adapter_affection(x) for x in brut
                                                     if isinstance(x, str) and x not in noms]
    else:
        aff = [adapter_affection(x) for x in brut]
    lettre = j.get("lettre") or (j["id"].split("-")[-1] if j["id"].count("-") >= 2 else "?")
    sysc = j.get("systeme", "?")
    meca_nom = premier(j, "mecanisme_nom", defaut=NOM_LETTRE.get(lettre, lettre))
    titre = premier(j, "titre", "nom", defaut=f"{NOM_SYS.get(sysc, sysc)} — {meca_nom}")
    etapes = L(premier(j, "cascade_etapes", defaut=ETAPES))
    chaine = []
    for i, c in enumerate(L(premier(j, "cascade", "chaine", defaut=[]))):
        m = re.match(r"\s*([^:]{1,20})\s*:\s*(.*)$", str(c), re.S)
        if m and m.group(1).strip() in ETAPES + etapes:
            chaine.append((m.group(1).strip(), m.group(2)))
        else:
            chaine.append((etapes[i] if i < len(etapes) else f"Étape {i + 1}", str(c)))
    ex = j.get("examen_cle")
    return {
        "id": j["id"], "type": "PP", "systeme": sysc, "lettre": lettre, "meca_nom": meca_nom, "titre": titre,
        "niveau": j.get("niveau"), "statut": j.get("statut"), "date": j.get("date"),
        "mecanisme": j.get("mecanisme", ""), "chaine": chaine, "signes": L(premier(j, "signes_cardinaux", "signes")),
        "affections": aff, "examen_cle": ids_de(ex) if isinstance(ex, (dict, list)) else L(ex),
        "traitement": L(premier(j, "traitement_cible", "cible_therapeutique")),
        "doses": j.get("doses", ""), "mnemo": j.get("mnemotechnique", ""),
        "renvois_croises": L(j.get("renvois_croises")), "ajouts": L(j.get("ajouts_audit")),
        "a_venir": L(j.get("complements_a_venir")), "cadrage": j.get("cadrage_recensement", ""),
        "passerelles": [p for p in L(j.get("passerelles")) if isinstance(p, dict)],
        "sources": sources(j.get("sources")), "honnetete": j.get("honnetete", ""),
    }


def charger(dossier, motif, adapter):
    out = {}
    for f in sorted(glob.glob(os.path.join(ICI, dossier, motif))):
        base = os.path.basename(f)
        try:
            with open(f, encoding="utf-8") as h:
                j = json.load(h)
            j.setdefault("id", base[:-5])
            d = adapter(j)
            out[d["id"]] = d
        except Exception as ex:
            signaler(f"{dossier}/{base} illisible, sauté : {ex}")
    return out


PHY = charger("physiologie", "PHY-*.json", adapter_phy)
PP = charger("physiopathologie", "PP-*.json", adapter_pp)


def cle_tri(i):
    m = re.match(r"(?:PHY|PP)-S(\d+)-(\w+)", i)
    if not m:
        return (99, 99, i)
    s = m.group(2)
    lettres = [x for x, _ in LETTRES]
    return (int(m.group(1)), int(s) if s.isdigit() else (lettres.index(s) if s in lettres else 50), i)


# Physiologie correspondante d'une fiche PP : passerelles directes + index inverse.
PHY_DE_PP = {k: [] for k in PP}
for pid, p in PHY.items():
    cibles_pp = {i for d in p["dereglements"] for i in d["pp"]} | {x["id"] for x in p["passerelles"] if str(x.get("id", "")).startswith("PP-")}
    for c in cibles_pp:
        if c in PHY_DE_PP and pid not in PHY_DE_PP[c]:
            PHY_DE_PP[c].append(pid)
for k, d in PP.items():
    for x in d["passerelles"]:
        i = str(x.get("id", ""))
        if i.startswith("PHY-") and i in PHY and i not in PHY_DE_PP[k]:
            PHY_DE_PP[k].append(i)
    PHY_DE_PP[k].sort(key=cle_tri)

# ---------------------------------------------------------------- texte : renvois et sigles
TITRES = {k: v["titre"] for k, v in {**PHY, **PP}.items()}
_motif = re.compile(
    r"(?<![\w-])(?:(?P<int>(?:PHY|PP)-S\d+-\w+)|(?P<sf>SF-S\d+-\w+)|(?P<sem>SY-0*\d+|S-\d{2})"
    r"|(?P<sig>" + "|".join(re.escape(k) for k in sorted(SIGLES, key=len, reverse=True)) + r"))(?![\w-])")


def lien_id(i, cls=""):
    c = f' class="{cls}"' if cls else ""
    if i in TITRES:
        return f'<a href="#{e(i)}"{c} title="{e(TITRES[i])}">{e(i)}</a>'
    m = re.match(r"SF-(S\d+)-", i)
    if m:
        return f'<a href="#phy-{m.group(1)}"{c} title="Physiologie — {e(NOM_SYS.get(m.group(1), ""))}">{e(i)}</a>'
    n = norm_sem(i)
    if n in TITRES_SEMIO:
        return f'<a href="{SEMIO}#{e(n)}"{c} title="{e(TITRES_SEMIO[n])} (Sémiologie)">{e(n)}</a>'
    return f'<span class="code">{e(i)}</span>'


def txt(t):
    s, out, pos = str(t), [], 0
    for m in _motif.finditer(s):
        out.append(e(s[pos:m.start()]))
        if m.group("sig"):
            out.append(f'<abbr title="{e(SIGLES[m.group("sig")])}">{e(m.group("sig"))}</abbr>')
        else:
            out.append(lien_id(m.group(0)))
        pos = m.end()
    out.append(e(s[pos:]))
    return "".join(out)


def liste(items, balise="ul", cls=""):
    items = [i for i in L(items) if str(i).strip()]
    if not items:
        return ""
    c = f' class="{cls}"' if cls else ""
    return f"<{balise}{c}>" + "".join(f"<li>{txt(i)}</li>" for i in items) + f"</{balise}>"


def h3(t):
    return f'<h3 class="rub">{e(t)}</h3>'


def pastilles(ids):
    ids = [i for i in ids if i]
    if not ids:
        return ""
    return '<ul class="pastilles">' + "".join(f"<li>{lien_id(i, 'pastille')}</li>" for i in ids) + "</ul>"


def codes(ids, label):
    ids = [i for i in ids if i]
    return f'<p class="petit"><span class="lab">{e(label)}</span> {", ".join(lien_id(i) for i in ids)}</p>' if ids else ""


def niveau(n):
    lab = {"m": "MIN", "c": "CIBLE"}.get(n)
    return (f'<abbr title="{"niveau minimal exigé" if lab == "MIN" else "niveau cible"}">{lab}</abbr>' if lab
            else e(n or "—"))


def bandeau(i, titre, champs):
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in champs if v)
    return (f'<header class="bandeau"><h2 id="t-{e(i)}"><span class="sid">{e(i)}</span> {e(titre)}</h2>'
            f'<dl class="meta">{dl}</dl></header>')


def table(entetes, lignes, nom, cls=""):
    if not lignes:
        return ""
    th = "".join(f'<th scope="col">{x}</th>' for x in entetes)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in lignes)
    return (f'<div class="defile" tabindex="0" role="region" aria-label="{e(nom)} — défilement horizontal">'
            f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')


def bloc_passerelles(pas, exclure=()):
    groupes = {}
    for p in pas:
        i = str(p.get("id", ""))
        if not i or i in exclure:
            continue
        vers = str(p.get("vers", "autre")).strip().capitalize()
        groupes.setdefault(vers, []).append(i)
    if not groupes:
        return ""
    lignes = []
    for v, ids in groupes.items():
        lignes.append(f'<li><span class="lab">{e(v)}</span> ' + ", ".join(lien_id(i) for i in dict.fromkeys(ids)) + "</li>")
    return h3("Passerelles") + '<ul class="passerelles">' + "".join(lignes) + "</ul>"


# ---------------------------------------------------------------- rendus
def rendre_phy(d):
    h = [bandeau(d["id"], d["titre"], [("Système", e(f'{d["systeme"]} — {NOM_SYS.get(d["systeme"], "")}')),
                                       ("Niveau", niveau(d["niveau"])), ("Statut", txt(d["statut"] or "")),
                                       ("Date", e(d["date"] or ""))])]
    if d["definition"]:
        h.append(h3("Définition") + f'<p>{txt(d["definition"])}</p>')
    b = d["boucle"]
    if b:
        etapes = [(k.capitalize().replace("Integrateur", "Intégrateur"), b[k]) for k in ("capteur", "integrateur", "effecteur") if b.get(k)]
        h.append(h3("Boucle de régulation") + '<ol class="chaine trois">' + "".join(
            f'<li><span class="etape">{e(k)}</span><p>{txt(v)}</p></li>' for k, v in etapes) + "</ol>")
    if d["mecanisme"]:
        h.append(h3("Mécanisme") + liste(d["mecanisme"], "ol"))
    vals = []
    for v in d["valeurs"]:
        if isinstance(v, dict):
            vals.append([txt(v.get("parametre", "")), txt(v.get("valeur", "")), txt(v.get("unite", "")), txt(v.get("sources", "—"))])
        else:
            vals.append([txt(v), "", "", ""])
    if vals:
        h.append(h3("Valeurs normales") + table(["Paramètre", "Valeur", "Unité", "Source"], vals, "Valeurs normales"))
    if d["regulation"]:
        h.append(h3("Régulation") + f'<p>{txt(d["regulation"])}</p>')
    for f in d["formules"]:
        h.append('<aside class="formule" aria-label="Formule et exemple résolu"><h3 class="formule-t">Formule et exemple résolu</h3>'
                 f'<p class="expr">{txt(f["expression"])}</p>'
                 + (f'<h4 class="formule-t">Usage</h4><p>{txt(f["usage"])}</p>' if f["usage"] else "")
                 + (f'<h4 class="formule-t">Exemple résolu</h4><p>{txt(f["exemple"])}</p>' if f["exemple"] else "")
                 + "</aside>")
    if d["lien_clinique"]:
        h.append(h3("Lien clinique") + f'<p>{txt(d["lien_clinique"])}</p>')
    if d["dereglements"]:
        h.append(h3("Dérèglements") + '<div class="cartes">' + "".join(
            f'<article class="carte"><h4 class="carte-t">{txt(x["titre"])}</h4>{liste(x["mecanisme"])}'
            + (f'<h5 class="carte-t">Physiopathologie</h5>{pastilles(x["pp"])}' if x["pp"] else "")
            + (f'<h5 class="carte-t">Sémiologie</h5>{pastilles(x["semio"])}' if x["semio"] else "")
            + "</article>" for x in d["dereglements"]) + "</div>")
    if d["cibles"]:
        h.append(h3("Cibles pharmacologiques") + "<ul>" + "".join(
            f"<li><strong>{txt(n)}</strong>{(' — ' + txt(p)) if p else ''}</li>" for n, p in d["cibles"]) + "</ul>")
    if d["mnemo"]:
        h.append(h3("Mnémotechnique") + f'<p>{txt(d["mnemo"])}</p>')
    h.append(bloc_passerelles(d["passerelles"]))
    if d["sources"]:
        h.append(h3("Sources") + liste(d["sources"], "ol", "sources"))
    if d["honnetete"]:
        h.append(f'<p class="petit"><span class="lab">Honnêteté</span> {txt(d["honnetete"])}</p>')
    return f'<section class="fiche" id="{e(d["id"])}" aria-labelledby="t-{e(d["id"])}">{"".join(h)}</section>'


def rendre_affection(a):
    c = [f'<article class="carte"><h4 class="carte-t">{txt(a["titre"])}</h4>']
    if a["mecanisme"]:
        c.append('<h5 class="carte-t">Mécanisme</h5>' + liste(a["mecanisme"]))
    if a["clinique"]:
        c.append(f'<h5 class="carte-t">Conséquence clinique</h5><p>{txt(a["clinique"])}</p>')
    if a["semio"]:
        c.append('<h5 class="carte-t">Sémiologie</h5>' + pastilles(a["semio"]))
    if a["examen"] or a["examens"] or a["imagerie"]:
        c.append('<h5 class="carte-t">Examen révélateur</h5>' + (f'<p>{txt(a["examen"])}</p>' if a["examen"] else "")
                 + codes(a["examens"], "Examens") + codes(a["imagerie"], "Imagerie"))
    if a["cibles"]:
        c.append('<h5 class="carte-t">Cible thérapeutique</h5><ul>' + "".join(
            f"<li><strong>{txt(n)}</strong>{(' — ' + txt(p)) if p else ''}</li>" for n, p in a["cibles"]) + "</ul>")
    c.append(codes(a["pharmaco"], "Pharmacologie"))
    if a["fiches"]:
        c.append('<h5 class="carte-t">Voir aussi</h5>' + pastilles(a["fiches"]))
    if a["mnemo"]:
        c.append(f'<p class="petit"><span class="lab">Mnémotechnique</span> {txt(a["mnemo"])}</p>')
    return "".join(c) + "</article>"


def rendre_pp(d):
    h = [bandeau(d["id"], d["titre"], [
        ("Système", e(f'{d["systeme"]} — {NOM_SYS.get(d["systeme"], "")}')),
        ("Lettre VITE DIT CAFé", e(f'{d["lettre"]} — {d["meca_nom"]}')),
        ("Niveau", niveau(d["niveau"])), ("Statut", txt(d["statut"] or ""))])]
    if d["mecanisme"]:
        h.append(h3("Mécanisme") + f'<p>{txt(d["mecanisme"])}</p>')
    if d["chaine"]:
        h.append(h3("Chaîne Normal → Altération → Lésion → Signes") + '<ol class="chaine">' + "".join(
            f'<li><span class="etape">{e(k)}</span><p>{txt(v)}</p></li>' for k, v in d["chaine"]) + "</ol>")
    if d["signes"]:
        h.append(h3("Signes cardinaux") + liste(d["signes"]))
    if d["affections"]:
        h.append(h3("Affections") + '<div class="cartes">' + "".join(rendre_affection(a) for a in d["affections"]) + "</div>")
    if d["renvois_croises"]:
        h.append(h3("Renvois croisés") + liste(d["renvois_croises"]))
    phys = PHY_DE_PP.get(d["id"], [])
    generiques = [str(p.get("id")) for p in d["passerelles"] if str(p.get("id", "")).startswith("SF-")]
    h.append(h3("Physiologie correspondante") + (pastilles(phys + generiques) if (phys or generiques)
                                                  else '<p class="petit">Aucune fiche de physiologie reliée.</p>'))
    if d["examen_cle"] or d["traitement"]:
        h.append('<div class="deuxcol">' + (f'<div>{h3("Examen clé")}{codes(d["examen_cle"], "Fiche")}</div>' if d["examen_cle"] else "<div></div>")
                 + (f'<div>{h3("Traitement ciblé")}{codes(d["traitement"], "Fiche")}</div>' if d["traitement"] else "") + "</div>")
    if d["doses"]:
        h.append(f'<p class="petit"><span class="lab">Doses</span> {txt(d["doses"])}</p>')
    if d["mnemo"]:
        h.append(h3("Mnémotechnique") + f'<p>{txt(d["mnemo"])}</p>')
    if d["cadrage"]:
        h.append(f'<p class="petit"><span class="lab">Cadrage</span> {txt(d["cadrage"])}</p>')
    if d["a_venir"]:
        h.append(h3("Compléments à venir") + liste(d["a_venir"]))
    if d["ajouts"]:
        h.append(h3("Ajouts après audit") + liste(d["ajouts"]))
    h.append(bloc_passerelles(d["passerelles"], exclure=set(phys) | set(generiques)))
    if d["sources"]:
        h.append(h3("Sources") + liste(d["sources"], "ol", "sources"))
    if d["honnetete"]:
        h.append(f'<p class="petit"><span class="lab">Honnêteté</span> {txt(d["honnetete"])}</p>')
    return f'<section class="fiche" id="{e(d["id"])}" aria-labelledby="t-{e(d["id"])}">{"".join(h)}</section>'


def panneau_phy():
    menu, corps = [], []
    par_sys = {}
    for k in sorted(PHY, key=cle_tri):
        par_sys.setdefault(PHY[k]["systeme"], []).append(k)
    for s in [x["code"] for x in SYSTEMES] + [c for c in par_sys if c not in NOM_SYS or c == "T"]:
        ids = par_sys.get(s, [])
        if not ids:
            continue
        menu.append(f'<h2><a href="#phy-{e(s)}">{e(s)} — {e(NOM_SYS.get(s, s))}</a></h2><ul>'
                    + "".join(f'<li><a href="#{e(i)}">{e(i)} {e(PHY[i]["titre"])}</a></li>' for i in ids) + "</ul>")
        corps.append(f'<h2 class="groupe" id="phy-{e(s)}">{e(s)} — {e(NOM_SYS.get(s, s))}</h2>'
                     + "".join(rendre_phy(PHY[i]) for i in ids))
    return "".join(menu), "".join(corps)


def grille_pp():
    th = '<th scope="col">Système</th>' + "".join(
        f'<th scope="col"><abbr title="{e(n)}">{e(l)}</abbr></th>' for l, n in LETTRES)
    lignes = []
    for s in SYSTEMES:
        c = s["code"]
        cells = []
        for l, n in LETTRES:
            i = f"PP-{c}-{l}"
            if i in PP:
                na = len(PP[i]["affections"])
                noms = " ; ".join(a["titre"] for a in PP[i]["affections"][:6])
                cells.append(f'<td><a class="case" href="#{e(i)}" title="{e(PP[i]["titre"])} : {e(noms)}" '
                             f'aria-label="{e(i)} {e(PP[i]["titre"])}">{na}</a></td>')
            else:
                cells.append('<td><span class="case vide" title="fiche absente">—</span></td>')
        lignes.append(f'<tr><th scope="row"><a href="#pp-{e(c)}">{e(c)}</a> <span class="nomsys">{e(s["nom"])}</span></th>{"".join(cells)}</tr>')
    return ('<div class="defile" tabindex="0" role="region" aria-label="Grille système × lettre — défilement horizontal">'
            f'<table class="grille"><thead><tr>{th}</tr></thead><tbody>{"".join(lignes)}</tbody></table></div>'
            '<p class="petit">Chaque case donne le nombre d’affections et ouvre la fiche ; lettres VITE DIT CAFé en survol.</p>')


def panneau_pp():
    menu, corps = [], []
    par_sys = {}
    for k in sorted(PP, key=cle_tri):
        par_sys.setdefault(PP[k]["systeme"], []).append(k)
    for s in [x["code"] for x in SYSTEMES] + [c for c in par_sys if c not in NOM_SYS]:
        ids = par_sys.get(s, [])
        if not ids:
            continue
        menu.append(f'<h2><a href="#pp-{e(s)}">{e(s)} — {e(NOM_SYS.get(s, s))}</a></h2><ul>'
                    + "".join(f'<li><a href="#{e(i)}">{e(PP[i]["lettre"])} — {e(PP[i]["meca_nom"])}</a></li>' for i in ids) + "</ul>")
        corps.append(f'<h2 class="groupe" id="pp-{e(s)}">{e(s)} — {e(NOM_SYS.get(s, s))}</h2>'
                     + "".join(rendre_pp(PP[i]) for i in ids))
    return "".join(menu), grille_pp() + "".join(corps)


CSS = """
:root{--fiche:%(fiche)s;--rub:%(temps)s;--carte:%(carte)s;--formule:%(formule)s;--trait:#5A5A5A;--fin:#BDBDBD}
*{box-sizing:border-box}
html{scroll-padding-top:76px}
body{margin:0;background:#FFFFFF;color:#000000;font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
a{color:#000000;text-decoration:underline}
abbr[title]{text-decoration:underline dotted;cursor:help}
.saut{position:absolute;left:-9999px}.saut:focus{left:16px;top:8px;background:#FFFFFF;padding:8px;border:2px solid #000;z-index:50}
.cadre{display:grid;grid-template-columns:290px minmax(0,1fr);min-height:100vh}
.menus{position:sticky;top:0;height:100vh;overflow-y:auto;border-right:1px solid var(--fin);padding:16px 12px 32px;background:#FFFFFF}
.menus .marque{font-weight:700;font-size:1.05rem;color:var(--fiche);margin:0 0 4px}
nav.menu h2{font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;margin:16px 0 4px}
nav.menu h2 a{text-decoration:none}
nav.menu ul{list-style:none;margin:0;padding:0}
nav.menu li a{display:block;padding:3px 8px;text-decoration:none;border-left:3px solid transparent;font-size:.9rem}
nav.menu a:hover,nav.menu a:focus{text-decoration:underline}
nav.menu a[aria-current=true]{border-left-color:#000;font-weight:700}
.basc{display:none}
main{padding:0 32px 64px;max-width:1180px;min-width:0}
.onglets{position:sticky;top:0;z-index:15;background:#FFFFFF;display:flex;flex-wrap:wrap;gap:4px 8px;padding:12px 0 0;border-bottom:2px solid #000;margin:0 0 8px}
.onglets button,.onglets a{font:600 1rem system-ui,sans-serif;color:#000;background:#FFFFFF;border:1px solid var(--trait);border-bottom:0;padding:8px 14px;cursor:pointer;text-decoration:none}
.onglets a{font-weight:400}
.onglets button[aria-selected=true]{border:2px solid #000;border-bottom:4px solid #FFFFFF;margin-bottom:-2px;font-weight:800}
.onglets button:focus-visible,.onglets a:focus-visible{outline:3px solid #000;outline-offset:2px}
.panneau>h1{font-size:1.6rem;margin:16px 0 4px;color:var(--fiche)}
main p,main li,main dd,td{overflow-wrap:break-word}
.sources{overflow-wrap:anywhere}
h2.groupe{font-size:1.1rem;text-transform:uppercase;letter-spacing:.04em;margin:48px 0 0;border-bottom:1px solid #000}
.fiche{border-top:3px solid var(--fiche);padding-top:8px;margin:40px 0 0}
h2.groupe+.fiche{margin-top:16px}
.bandeau h2{color:var(--fiche);font-size:1.45rem;margin:4px 0 8px}
.sid{margin-right:.3em}
.meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:4px 20px;margin:0 0 8px;padding:8px 0;border-bottom:1px solid var(--fin)}
.meta div{min-width:0}.meta dt{font-weight:700;font-size:.82rem}.meta dd{margin:0}
h3.rub{color:var(--rub);font-size:1.12rem;margin:20px 0 6px}
main ul,main ol{padding-left:1.3em}
.deuxcol{display:grid;grid-template-columns:1fr 1fr;gap:0 32px}.deuxcol>div{min-width:0}
.defile{overflow-x:auto;border:1px solid var(--fin);max-width:100%%}
.defile:focus{outline:2px solid #000}
table{border-collapse:collapse;width:100%%}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--fin)}
thead th{font-weight:700;border-bottom:2px solid #000}
table.grille{min-width:760px}
table.grille td{text-align:center;vertical-align:middle;padding:4px}
table.grille tbody th{font-weight:700;white-space:nowrap}
.nomsys{font-weight:400;font-size:.85rem;white-space:normal}
.case{display:block;padding:6px 0;border:1px solid #000;text-decoration:none;font-weight:700;min-width:44px}
.case:hover,.case:focus{text-decoration:underline;outline:2px solid #000}
.case.vide{border-style:dashed;font-weight:400}
.chaine{list-style:none;padding:0!important;margin:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0}
.chaine.trois{grid-template-columns:repeat(3,minmax(0,1fr))}
.chaine li{border:1px solid var(--trait);padding:10px 12px;position:relative;margin-right:22px}
.chaine li:last-child{margin-right:0}
.chaine li:not(:last-child)::after{content:"→";position:absolute;right:-20px;top:50%%;transform:translateY(-50%%);font-weight:700;font-size:1.1rem}
.chaine .etape{display:block;font-weight:700;color:var(--carte);margin-bottom:4px}
.chaine p{margin:0}
.cartes{display:grid;grid-template-columns:repeat(auto-fill,minmax(400px,1fr));gap:16px}
.carte{border:1px solid var(--trait);padding:12px 14px;min-width:0}
.carte h4.carte-t{font-size:1.05rem;margin:0 0 6px}
.carte-t{color:var(--carte)}
h5.carte-t{font-size:.9rem;margin:10px 0 2px}
.carte p{margin:0}.carte ul,.carte ol{margin:0}
.lab{font-weight:700;margin-right:.3em}
.petit{font-size:.88rem;margin:6px 0}
.code{font-size:.9em}
.formule{border:3px solid var(--formule);padding:12px 16px;margin:24px 0 0}
.formule-t{color:var(--formule)}
h3.formule-t{margin:0 0 6px;font-size:1.12rem}
h4.formule-t{margin:10px 0 2px;font-size:.95rem}
.formule p{margin:0}
.expr{font-weight:600}
.pastilles{list-style:none;padding:0!important;margin:0;display:flex;flex-wrap:wrap;gap:8px}
.pastille{display:inline-block;border:1px solid #000;border-radius:999px;padding:2px 12px;font-size:.88rem;text-decoration:none}
.pastille:hover,.pastille:focus{text-decoration:underline}
span.pastille{border-style:dashed}
.passerelles{list-style:none;padding:0!important}
.passerelles li{margin:0 0 4px}
.sources{font-size:.9rem}
.prep{border:1px dashed #000;padding:16px;margin:24px 0}
@media (max-width:860px){
 html{scroll-padding-top:130px}
 .cadre{display:block}
 .basc{display:block;width:100%%;text-align:left;background:#FFFFFF;color:#000;border:0;border-bottom:2px solid #000;font:700 1rem system-ui,sans-serif;padding:10px 0 8px;cursor:pointer}
 .menus{position:static;height:auto;border-right:0;padding:0 16px}
 .menus .marque{display:none}
 .menus nav.menu{display:none!important;padding-bottom:16px;border-bottom:1px solid var(--fin)}
 .menus.ouvert nav.menu.actif{display:block!important}
 main{padding:0 16px 48px}
 .onglets button,.onglets a{padding:6px 10px;font-size:.92rem}
 .deuxcol{grid-template-columns:1fr}
 .cartes{grid-template-columns:minmax(0,1fr)}
 .chaine,.chaine.trois{grid-template-columns:minmax(0,1fr)}
 .chaine li{margin:0 0 22px 0}
 .chaine li:not(:last-child)::after{content:"↓";right:auto;left:50%%;top:auto;bottom:-22px;transform:none}
 .meta{grid-template-columns:1fr}
}
@media print{.menus,.basc,.onglets{display:none}.cadre{display:block}.panneau[hidden]{display:block}}
""" % COULEURS

JS = r"""
(function(){
 var panneaux=[].slice.call(document.querySelectorAll('.panneau')),menus=[].slice.call(document.querySelectorAll('nav.menu')),
     boutons=[].slice.call(document.querySelectorAll('.onglets button')),boite=document.querySelector('.menus'),basc=document.querySelector('.basc');
 function activer(nom){
  panneaux.forEach(function(p){p.hidden=p.dataset.onglet!==nom;});
  menus.forEach(function(m){var a=m.dataset.onglet===nom;m.hidden=!a;m.classList.toggle('actif',a);});
  boutons.forEach(function(b){var a=b.dataset.onglet===nom;b.setAttribute('aria-selected',a?'true':'false');b.tabIndex=a?0:-1;});
  basc.hidden=!document.querySelector('nav.menu[data-onglet="'+nom+'"]');
  try{localStorage.setItem('sf-onglet',nom);}catch(e){}
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
 if(location.hash){route();}else{var s=null;try{s=localStorage.getItem('sf-onglet');}catch(e){}
  activer(s&&document.querySelector('.panneau[data-onglet="'+s+'"]')?s:'physiologie');}
 basc.addEventListener('click',function(){var o=boite.classList.toggle('ouvert');basc.setAttribute('aria-expanded',o?'true':'false');});
 boite.addEventListener('click',function(ev){if(ev.target.closest('a')){boite.classList.remove('ouvert');basc.setAttribute('aria-expanded','false');}});
 if('IntersectionObserver' in window){
  var liens={};menus.forEach(function(m){m.querySelectorAll('li a[href^="#"]').forEach(function(a){liens[a.getAttribute('href').slice(1)]=a;});});
  var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){var a=liens[x.target.id];if(!a)return;
   a.closest('nav').querySelectorAll('a[aria-current]').forEach(function(z){z.removeAttribute('aria-current');});
   a.setAttribute('aria-current','true');}});},{rootMargin:'0px 0px -80% 0px'});
  document.querySelectorAll('section.fiche').forEach(function(s){io.observe(s);});}
})();
"""


def main():
    m_phy, c_phy = panneau_phy()
    m_pp, c_pp = panneau_pp()
    alerte = (f'<p class="prep">Signalements : {e(" ; ".join(SIGNALEMENTS))}</p>' if SIGNALEMENTS else "")
    onglets = [
        ("anatomie", "1 Anatomie", "", '<h1>Anatomie</h1><p class="prep"><strong>En préparation.</strong> Les fiches d’anatomie topo-systémique seront publiées dans cet onglet.</p>'),
        ("physiologie", f"2 Physiologie ({len(PHY)})", m_phy,
         f'<h1>Physiologie</h1><p>{len(PHY)} fiches, ordre topo-systémique S1 → S12.</p>{alerte}{c_phy}'),
        ("physiopathologie", f"3 Physiopathologie ({len(PP)})", m_pp,
         f'<h1>Physiopathologie</h1><p>{len(PP)} fiches : grille système × lettre <abbr title="Vasculaire, Infectieux, Tumoral, Dégénératif, Iatrogène, Traumatique, Congénital, Auto-immun, Fonctionnel">VITE DIT CAFé</abbr>.</p>{c_pp}'),
    ]
    boutons = "".join(f'<button type="button" role="tab" id="tab-{k}" data-onglet="{k}" aria-controls="p-{k}" aria-selected="false">{e(n)}</button>'
                      for k, n, _, _ in onglets)
    boutons += f'<a href="{SEMIO}">4 Sémiologie ↗</a>'
    navs = "".join(f'<nav class="menu" data-onglet="{k}" aria-label="Fiches — {e(n)}">{m}</nav>' for k, n, m, _ in onglets if m)
    panneaux = "".join(f'<div class="panneau" id="p-{k}" role="tabpanel" aria-labelledby="tab-{k}" data-onglet="{k}">{c}</div>'
                       for k, _, _, c in onglets)
    page = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sciences fondamentales</title><style>{CSS}</style></head>
<body><a class="saut" href="#contenu">Aller au contenu</a>
<div class="cadre"><div class="menus"><p class="marque">Sciences fondamentales</p>
<button type="button" class="basc" aria-expanded="false">☰ Menu des fiches de l’onglet</button>{navs}</div>
<main id="contenu"><div class="onglets" role="tablist" aria-label="Sous-onglets des sciences fondamentales">{boutons}</div>{panneaux}</main></div>
<script>{JS}</script></body></html>
"""
    with open(SORTIE, "w", encoding="utf-8") as h:
        h.write(page)
    print(f"SCIENCES_FONDAMENTALES.html : {len(PHY)} PHY, {len(PP)} PP, {len(SIGNALEMENTS)} signalement(s), {len(page)//1024} Ko")


if __name__ == "__main__":
    main()
