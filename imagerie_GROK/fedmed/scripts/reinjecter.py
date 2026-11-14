#!/usr/bin/env python3
"""Réinjecte les fenêtres. Sans fusion, le fichier d'origine est restitué octet pour octet."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C
import gabarit as G

MARQUE_FIGURE = (
    "else h+=(im.normal&&im.patho?'<button type=\"button\" class=\"bascule\" aria-pressed=\"false\">Voir la pathologie</button>':'')\n"
    "     +'<figure class=\"fig\"><div class=\"cadre\"><img alt=\"\"><svg viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\" aria-hidden=\"true\"></svg></div><figcaption></figcaption></figure><div class=\"lesion\" aria-live=\"polite\" hidden></div>';"
)
FIGURE_GABARIT = (
    "else if(en.gabarit)h+='<div class=\"gm\" data-gm=\"1\"></div>';\n"
    "   else h+=(im.normal&&im.patho?'<button type=\"button\" class=\"bascule\" aria-pressed=\"false\">Voir la pathologie</button>':'')\n"
    "     +'<figure class=\"fig\"><div class=\"cadre\"><img alt=\"\"><svg viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\" aria-hidden=\"true\"></svg></div><figcaption></figcaption></figure><div class=\"lesion\" aria-live=\"polite\" hidden></div>';"
)
MARQUE_APPEL = "if(en&&en.images&&!en.images.manque&&(en.images.normal||en.images.patho))images(en.images);"
APPEL_GABARIT = (
    "if(en&&en.gabarit&&fenC.querySelector('.gm'))GM.render(fenC.querySelector('.gm'),en);"
    "else if(en&&en.images&&!en.images.manque&&(en.images.normal||en.images.patho))images(en.images);"
)
MARQUE_CREDIT = "if(!im.manque)h+=credit(mot[1]+' normal',im.normal)+credit(mot[1]+' pathologique',im.patho);"
CREDIT_GABARIT = "if(!im.manque&&!en.gabarit)h+=credit(mot[1]+' normal',im.normal)+credit(mot[1]+' pathologique',im.patho);"


def remplir_fichiers(enr, mime):
    im = enr.get("images") or {}
    for cote in ("patho", "normal"):
        bloc = im.get(cote)
        if not isinstance(bloc, dict):
            continue
        fichier = bloc.get("fichier")
        if not isinstance(fichier, str) or not fichier.startswith("images/"):
            continue
        brut = (C.FENETRES / fichier).read_bytes()
        bloc["fichier"] = C.data_uri(mime.get(cote) or "image/jpeg", brut)
    return enr


def charger_fenetre(ident):
    return C.lire_json(C.FENETRES / f"{ident}.json")


def appliquer_fusion(fiche):
    chemin = C.FUSION / f"{fiche['id']}.json"
    if not chemin.is_file():
        return fiche["enr"], fiche.get("mime") or {}
    fusion = C.lire_json(chemin)
    enr = fiche["enr"]
    mime = dict(fiche.get("mime") or {})
    im = enr.setdefault("images", {})
    for cote, motif in (fusion.get("retraits") or {}).items():
        bloc = im.get(cote)
        if isinstance(bloc, dict):
            bloc.pop("fichier", None)
        mime.pop(cote, None)
        if motif:
            im.setdefault("_signaux", []).append(f"{cote} : {motif}")
    ajout = fusion.get("normal_ajoute")
    if ajout:
        im.pop("manque_normal", None)
        im["normal"] = {
            "fichier": ajout["fichier"],
            "technique": ajout.get("technique") or "",
            "credit": ajout.get("credit") or "",
            "licence": ajout.get("licence") or "",
            "url": ajout.get("url") or "",
        }
        mime["normal"] = ajout.get("mime") or "image/jpeg"
    enr["gabarit"] = fusion["gabarit"]
    return enr, mime


def pages_depuis_squelette(fusionner):
    data = C.SQUELETTE.read_text(encoding="utf-8")
    m, page, d, obj = C.ouvrir_rts(data)
    for ident, enr in list(obj["enr"].items()):
        if not (isinstance(enr, dict) and enr.get("__fenetre__") == ident):
            continue
        fiche = charger_fenetre(ident)
        if fusionner:
            corps, mime = appliquer_fusion(fiche)
        else:
            corps, mime = fiche["enr"], fiche.get("mime") or {}
        obj["enr"][ident] = remplir_fichiers(corps, mime)
    return data, m, page, d, obj


def reconstruire_brut():
    data, m, page, d, obj = pages_depuis_squelette(False)
    return C.refermer(data, m, page, d, obj)


def polices_css():
    dossier = C.DEPOT / "Claude" / "_polices"
    faces = [
        ("400", "normal", "atkinson-hyperlegible-latin-400-normal.woff2"),
        ("400", "italic", "atkinson-hyperlegible-latin-400-italic.woff2"),
        ("700", "normal", "atkinson-hyperlegible-latin-700-normal.woff2"),
        ("700", "italic", "atkinson-hyperlegible-latin-700-italic.woff2"),
    ]
    regles = []
    for poids, style, nom in faces:
        brut = (dossier / nom).read_bytes()
        uri = C.data_uri("font/woff2", brut)
        regles.append(
            "@font-face{font-family:'Atkinson Hyperlegible';font-style:%s;font-weight:%s;font-display:swap;src:url('%s') format('woff2')}"
            % (style, poids, uri)
        )
    return "".join(regles)


def embarquer_polices_page(data, css_faces):
    for nom in (
        "atkinson-hyperlegible-latin-400-normal.woff2",
        "atkinson-hyperlegible-latin-400-italic.woff2",
        "atkinson-hyperlegible-latin-700-normal.woff2",
        "atkinson-hyperlegible-latin-700-italic.woff2",
    ):
        data = data.replace(
            f"url('Claude/_polices/{nom}')",
            "url('%s')" % _uri_police(nom),
        )
    if 'rel="icon"' not in data and "rel='icon'" not in data:
        data = data.replace(
            "<head>",
            "<head><link rel=\"icon\" href=\"data:,\">",
            1,
        )
    return data


_CACHE_POLICE = {}


def _uri_police(nom):
    if nom not in _CACHE_POLICE:
        brut = (C.DEPOT / "Claude" / "_polices" / nom).read_bytes()
        _CACHE_POLICE[nom] = C.data_uri("font/woff2", brut)
    return _CACHE_POLICE[nom]


def injecter_police_html(page, css_faces):
    style = (
        "<style id=\"gm-police\">"
        + css_faces
        + "html,body,.gm,.gm button{font-family:'Atkinson Hyperlegible',sans-serif}</style>"
    )
    if 'id="gm-police"' in page:
        return page
    return page.replace("<head>", "<head>" + style, 1)


def patch_rendu(page):
    ancre = "<script>\n(function(){\n var DON=JSON.parse(document.getElementById('donnees').textContent);"
    if 'id="gm-viewer"' not in page:
        if ancre not in page:
            raise SystemExit("ancre du script de rendu introuvable")
        page = page.replace(ancre, "<script id=\"gm-viewer\">" + G.JS + "</script>" + ancre, 1)
    css = "<style id=\"gm-css\">" + G.CSS + "</style>"
    if 'id="gm-css"' not in page:
        page = page.replace("</head>", css + "</head>", 1)
    if MARQUE_FIGURE not in page and "data-gm" not in page:
        raise SystemExit("balise de la figure introuvable, gabarit non branché")
    if MARQUE_FIGURE in page:
        page = page.replace(MARQUE_FIGURE, FIGURE_GABARIT, 1)
    if MARQUE_APPEL in page:
        page = page.replace(MARQUE_APPEL, APPEL_GABARIT, 1)
    if MARQUE_CREDIT in page:
        page = page.replace(MARQUE_CREDIT, CREDIT_GABARIT, 1)
    return page


def reconstruire_sortie():
    data, m, page, d, obj = pages_depuis_squelette(True)
    faces = polices_css()
    page = injecter_police_html(page, faces)
    page = patch_rendu(page)
    # Les pages sf et semio reçoivent la même police embarquée.
    sortie = C.refermer(data, m, page, d, obj)
    def une(morceau):
        ouvert, nom, corps, ferme = morceau.group(1), morceau.group(2), morceau.group(3), morceau.group(4)
        if nom == "rts":
            return morceau.group(0)
        html = json.loads(corps)
        html = injecter_police_html(html, faces)
        return ouvert + C.dumps_html(html) + ferme

    sortie = EMB_SAFE(sortie, une)
    sortie = embarquer_polices_page(sortie, faces)
    C.SORTIE.parent.mkdir(parents=True, exist_ok=True)
    C.SORTIE.write_text(sortie, encoding="utf-8")
    print(f"sortie {C.SORTIE} ({len(sortie)} caractères)")
    return sortie


def EMB_SAFE(data, une):
    return C.EMB_RE.sub(une, data)


def main():
    if "--brut" in sys.argv:
        texte = reconstruire_brut()
        orig = C.ORIGINAL.read_text(encoding="utf-8")
        if texte != orig:
            for i, (a, b) in enumerate(zip(texte, orig)):
                if a != b:
                    raise SystemExit(f"écart à l'octet {i}")
            raise SystemExit(f"longueurs {len(texte)} / {len(orig)}")
        print(f"octet identique ({len(texte)} caractères)")
        return
    reconstruire_sortie()


if __name__ == "__main__":
    main()
