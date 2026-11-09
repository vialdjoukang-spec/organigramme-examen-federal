#!/usr/bin/env python3
"""Point 9 — examen de référence, première intention, image autonome, tableau biologique.

Les images viennent des PNG déjà annotés (licence libre, anomalie vue). Elles sont
recompressées en JPEG ≤ 24 Ko et insérées en data URI, lignes courtes. Aucune valeur
SI absente des extraits n'est écrite. Une sortie Gemma n'est pas renvoyée au modèle.
"""
from __future__ import annotations

import base64
import html
import io
import json
import re
from pathlib import Path

from PIL import Image

RACINE = Path(__file__).resolve().parents[1]
ILL = RACINE / "illustrations"
LOT = RACINE

CSS = (
    ".stitre{font:700 .95rem/1.35 system-ui,sans-serif;color:#0b3d62;margin:.85rem 0 .2rem}"
    "img.cliche{max-width:100%;height:auto;display:block;margin:.4rem 0;border:1px solid #dde3e8;background:#f4f7fa}"
    "figcaption.leg{margin:.2rem 0 .8rem;font:.9rem/1.45 system-ui,sans-serif}"
)

# PNG annoté, texte alternatif, légende numérotée (déjà vérifiée sur le cliché).
IMAGES = {
    2: ("dx2-varicocele-echo.png",
        "Échographie scrotale : tubes anéchogènes serpigineux et mosaïque Doppler",
        "1. Tubes anéchogènes serpigineux, en gris. 2. Mosaïque de flux couleur dans la même région veineuse."),
    3: ("dx3-cryptorchidie-echo.png",
        "Échographie : plage plus sombre à droite du cliché, sans preuve d'absence testiculaire",
        "1. Plage nettement plus sombre que le reste du cliché, à droite."),
    5: ("dx5-mgf-types.png",
        "Schéma des types I à III, panneau D entouré, sans photographie de personne",
        "1. Panneau D, type III : grandes lèvres dessinées rapprochées, avec un petit orifice."),
    6: ("dx6-torsion-echo.png",
        "Échographie en gris : parenchyme plus échogène en bas, sans boîte Doppler",
        "1. Parenchyme plus échogène et inhomogène dans la partie inférieure, sans couleur Doppler sur ce cliché."),
    8: ("dx8-penis-histo.png",
        "Histologie : îlot malpighien cerné au sein d'un stroma inflammatoire",
        "1. Îlot de cellules malpighiennes au cytoplasme abondant, au centre du champ recadré."),
    10: ("dx10-fournier.png",
         "Périnée après débridement : fascia exposé à gauche, escarre noire à droite",
         "1. Fascia et muscle exposés, rouge vif, sans peau. 2. Escarre noire de la peau restante."),
}


def e(s: str) -> str:
    return html.escape(s, quote=True)


def jpeg_bytes(png: Path, limite: int = 24000) -> bytes:
    im = Image.open(png).convert("RGB")
    for largeur in (960, 800, 680, 560, 480, 400, 340):
        copie = im.copy()
        copie.thumbnail((largeur, largeur * 3))
        for qualite in (70, 58, 48, 40, 34, 28):
            buf = io.BytesIO()
            copie.save(buf, "JPEG", quality=qualite, optimize=True)
            if buf.tell() <= limite:
                return buf.getvalue()
    raise SystemExit(f"JPEG trop lourd : {png.name}")


def data_uri(png: Path) -> tuple[str, int]:
    brut = jpeg_bytes(png)
    b64 = base64.b64encode(brut).decode()
    corps = "\n".join(b64[i:i + 120] for i in range(0, len(b64), 120))
    return f"data:image/jpeg;base64,\n{corps}\n", len(brut)


def source_courte(sid: str) -> dict:
    items = json.loads((ILL / "SOURCES.json").read_text(encoding="utf-8"))
    for it in items:
        if it["id"] == sid:
            return it["source"]
    raise SystemExit(sid)


SID = {
    2: "dx2-varicocele-echo",
    3: "dx3-cryptorchidie-echo",
    5: "dx5-mgf-types",
    6: "dx6-torsion-echo",
    8: "dx8-penis-histo",
    10: "dx10-fournier",
}


def _auteur_court(auteur: str) -> str:
    # La fiche Commons de Häggström concatène une note de consentement : on garde le nom.
    return auteur.split(" Author info")[0].strip(" ,")


def _enrouler(fragment: str) -> str:
    """Le data URI officiel tient sur une ligne ; on le coupe pour rester sous 3 000 caractères."""
    def repl(m: re.Match) -> str:
        uri = m.group(1)
        tete, b64 = uri.split(";base64,", 1)
        corps = "\n".join(b64[i:i + 120] for i in range(0, len(b64), 120))
        return f'src="{tete};base64,\n{corps}\n"'
    return re.sub(r'src="(data:image/(?:jpeg|webp);base64,[A-Za-z0-9+/=]+)"', repl, fragment)


def figure(n: int) -> str:
    if n not in IMAGES:
        return ""
    import sys
    coeur = RACINE.parent / "Leona__Harnais_Agents" / "coeur"
    sys.path.insert(0, str(coeur))
    import harnais as H
    nom, alt, _leg = IMAGES[n]
    uri, _mime, _oct = H.image_vers_data_uri(ILL / nom)
    src = source_courte(SID[n])
    anomalies = {
        2: [
            "Tubes anéchogènes serpigineux, en échelle de gris.",
            "Mosaïque de flux au Doppler couleur, dans la même région veineuse.",
        ],
        3: ["Plage hypoéchogène à droite du cliché, sans preuve que le testicule non vu soit absent."],
        5: ["Panneau D, type III : grandes lèvres dessinées rapprochées, avec un petit orifice."],
        6: ["Parenchyme hyperéchogène et hétérogène en bas du cliché, sans cartographie Doppler couleur."],
        8: ["Îlot de cellules malpighiennes au cytoplasme abondant, au centre du champ recadré."],
        10: [
            "Fascia et muscle exposés après excision, rouge vif, sans peau.",
            "Escarre noire de la peau scrotale et périnéale restante.",
        ],
    }[n]
    frag = H.fragment_figure_data(
        uri, alt=alt, titre=alt, source=src.get("url_page") or src.get("identifiant") or "",
        auteur=_auteur_court(src.get("auteur") or ""), licence=src.get("licence") or "",
        anomalies=anomalies,
    )
    return _enrouler(frag) + "\n"


def tableau(lignes: list[tuple[str, str, str, str]]) -> str:
    corps = []
    for cas, resultat, lecture, hyp in lignes:
        corps.append(
            "<tr><td>" + "</td><td>".join(e(x) for x in (cas, resultat, "non relue", lecture, hyp)) + "</td></tr>"
        )
    return (
        '<div class="tw"><table><thead><tr>'
        "<th>Cas</th><th>Résultat possible</th><th>Valeur SI suisse</th>"
        "<th>Interprétation</th><th>Hypothèse</th>"
        "</tr></thead><tbody>" + "".join(corps) + "</tbody></table></div>\n"
        '<details class="fc" style="display:inline;"><summary>SI</summary>'
        "<div>Système international d'unités. La colonne reste « non relue » : aucun intervalle "
        "chiffré suisse n'a été ouvert pour ce diagnostic, donc aucune concentration n'est inventée. "
        "Source [S3].</div></details>\n"
    )


# Quatre phrases par fiche. Chacune doit rester sans 4-gramme déjà présent dans les div.p.
PHRASES = {
    0: [
        "L'examen de référence change selon le diagnostic retenu, donc cette monographie ne le fige pas en un seul geste.",
        "La première intention est clinique pour le phimosis, la varicocèle, la cryptorchidie, l'hypospadias et la mutilation, chirurgicale pour la torsion et la gangrène, histologique pour le carcinome, et biologique pour l'hyperplasie des surrénales.",
        "Les clichés vérifiés sont dans les fiches qui s'y prêtent, tandis que les fiches sans image fiable le disent.",
        "Chaque fiche sépare ensuite le résultat normal, positif, limite ou discordant, sans concentration inventée.",
    ],
    1: [
        "L'inspection du prépuce est l'examen de référence, car elle sépare l'anneau fibreux blanc du simple aspect en goulot.",
        "Ce même regard clinique est la première intention, donc aucune imagerie n'est exigée pour affirmer le diagnostic.",
        "Aucune photographie n'est jointe, parce que les clichés d'enfant ont été écartés et que le cliché adulte repéré n'a pas été relu image par image.",
        "La biologie n'oriente pas ce diagnostic, puisqu'aucun intervalle suisse du prépuce n'a été ouvert.",
    ],
    2: [
        "La clinique grade la dilatation veineuse et reste l'examen de référence de la varicocèle, chez l'adolescent examiné debout.",
        "L'échographie Doppler devient l'imagerie de première intention lorsque le grade ou le volume testiculaire doit être précisé.",
        "Une varicocèle droite isolée, ou vue avant la puberté, conduit ensuite à une échographie rénale.",
        "Le seuil européen d'hypotrophie est supérieur à 2 mL ou à 20 %, et ce n'est pas un dosage sanguin.",
    ],
    3: [
        "La palpation est l'examen de référence de la cryptorchidie, car elle dit si le testicule est dans le scrotum.",
        "L'échographie montrée ici n'est pas cet examen de référence : la plage sombre ne prouve pas l'absence d'un testicule non vu.",
        "Si les gonades sont non palpables de chaque côté et qu'un hypospadias coexiste, l'avis endocrinien devient urgent.",
        "L'orchidopexie européenne se place après six mois d'âge corrigé, durant les douze mois suivants, et avant dix-huit mois.",
    ],
    4: [
        "L'inspection à la naissance est l'examen de référence de l'hypospadias, sauf lorsque le méat glandulaire est incomplet.",
        "Aucune imagerie n'est de première intention pour cette forme morphologique.",
        "Aucun cliché n'est inséré, car les photographies d'enfant ont été refusées et le cliché adulte n'a pas été contrôlé.",
        "Lorsqu'un hypospadias s'associe à des gonades non palpables de chaque côté, on n'assigne pas le sexe dans la précipitation.",
    ],
    5: [
        "L'examen clinique classé selon les types de l'Organisation mondiale de la santé est l'examen de référence.",
        "Le schéma du domaine public est la première illustration des types I à III, et il ne photographie aucune personne.",
        "Le type IV n'est pas dessiné, donc une lésion hors planche est décrite sans être forcée dans un type.",
        "L'acte n'apporte aucun bénéfice pour la santé, et le code pénal suisse, à l'article 124, le punit depuis juillet 2012.",
    ],
    6: [
        "L'exploration chirurgicale est l'examen de référence de la torsion, dans les 24 h qui suivent le début des symptômes.",
        "L'échographie Doppler est l'imagerie de première intention, mais elle ne doit pas retarder le bloc, et le cliché joint est seulement en gris.",
        "Un flux qui persiste n'exclut pas la torsion : sur 208 garçons, 24 % avaient un flux normal ou augmenté.",
        "Dès quatre heures, si la spire dépasse 360 degrés, l'atrophie peut déjà être sévère, donc la biologie n'a pas sa place avant le bloc.",
    ],
    7: [
        "Le dépistage néonatal sur papier buvard est l'examen de référence dans le programme suisse, et aucune courbe n'est dessinée.",
        "Ce dosage est la première intention biologique, et la ligne suisse 1:10 200 est une incidence, pas un seuil de laboratoire.",
        "Aucune image de buvard libre et fiable n'a été trouvée, donc aucune n'est fabriquée.",
        "Les concentrations en nmol/L restent absentes, parce qu'aucune source suisse relue ne les fournit.",
    ],
    8: [
        "L'histologie est l'examen de référence du carcinome épidermoïde du pénis, par une biopsie au punch de 2 à 3 mm.",
        "Cette biopsie est aussi la première intention diagnostique, et le cliché montre un îlot malpighien dans le stroma.",
        "Un punch de 1 mm laisse la profondeur non évaluable dans 91 % des cas, donc il ne sert pas de référence.",
        "Aucun marqueur sanguin suisse n'a été relu, et l'imagerie ne remplace pas cette coupe.",
    ],
    9: [
        "L'analyse des gaz du sang caverneux est l'examen de référence du priapisme ischémique : elle retrouve hypoxie, hypercapnie et acidose.",
        "Au-delà de 4 h, la première intention est la décompression, car le tableau est celui d'un syndrome des loges.",
        "Aucune image de priapisme ischémique n'est jointe, car une fistule artérioveineuse est une autre maladie et a été refusée.",
        "Les seuils de pH et de pression partielle d'oxygène ne sont pas écrits, faute de les avoir lus dans l'extrait conservé.",
    ],
    10: [
        "L'examen clinique suivi du débridement est l'examen de référence, car la nécrose profonde dépasse largement la peau.",
        "Ce débridement est la première intention, avec des antibiotiques parentéraux empiriques dont la posologie suisse reste : À vérifier (AIPS).",
        "Le cliché, pris après excision, montre à gauche le fascia exposé et à droite l'escarre noire.",
        "Les prélèvements microbiologiques guident ensuite le relais, sans qu'une dose en milligrammes soit inventée.",
    ],
}

TABLES = {
    0: [
        ("normal", "signe absent pour le diagnostic évoqué", "le geste de référence ne retrouve pas la maladie", "passer au diagnostic suivant de la liste"),
        ("positif", "signe propre du diagnostic, décrit dans sa fiche", "la fiche DX précise le gold standard", "ouvrir cette fiche au point 9"),
        ("limite", "signe incomplet ou isolé", "ni confirmation ni exclusion", "reprendre l'examen de référence de la fiche"),
        ("discordant", "clinique et examen complémentaire divergent", "l'examen de référence l'emporte sur l'image accessoire", "ne pas conclure sur le seul complément"),
    ],
    1: [
        ("normal", "prépuce rétractable, gland vu", "pas d'anneau fibreux", "phimosis absent ou seulement physiologique"),
        ("positif", "anneau blanc, rétraction impossible", "phimosis pathologique", "traiter sans rétraction forcée"),
        ("limite", "adhérences, méat encore visible", "mobilité partielle", "surveillance, pas de circoncision d'emblée"),
        ("discordant", "ballonnement sans anneau fibreux", "le ballonnement n'est pas une obstruction", "ne pas conclure à un obstacle"),
    ],
    2: [
        ("normal", "pas de veines serpigineuses ni de mosaïque", "pas de varicocèle sur ce cliché", "la clinique reste la référence"),
        ("positif", "tubes anéchogènes et mosaïque Doppler", "dilatation veineuse avec flux", "varicocèle si la clinique concorde"),
        ("limite", "tubes visibles sans couleur", "le gris seul est incomplet", "ne pas opérer sur le gris seul"),
        ("discordant", "Doppler positif et clinique normale", "l'image ne donne pas le grade", "réexaminer debout"),
    ],
    3: [
        ("normal", "testicule palpé dans le scrotum", "pas de cryptorchidie", "surveillance ordinaire"),
        ("positif", "testicule palpé hors du scrotum", "cryptorchidie palpable", "chirurgie dans la fenêtre d'âge européenne"),
        ("limite", "palpation douteuse", "l'image ne tranche pas", "nouvel examen par un opérateur entraîné"),
        ("discordant", "échographie vide alors que le testicule est palpé", "l'image peut manquer le testicule", "croire la palpation"),
    ],
    4: [
        ("normal", "méat au sommet du gland", "pas d'hypospadias", "pas de geste pour cette seule question"),
        ("positif", "méat ventral, avec ou sans courbure", "hypospadias", "ne pas circoncire"),
        ("limite", "méat glandulaire incomplet", "diagnostic parfois différé", "réexaminer sans conclure trop vite"),
        ("discordant", "hypospadias et gonades non palpables", "trouble du développement possible", "avis urgent, sans assignation hâtive"),
    ],
    5: [
        ("normal", "anatomie du panneau A du schéma", "pas de mutilation sur ce dessin", "information et prévention"),
        ("positif", "type I, II ou III", "mutilation au sens de la définition retenue", "protection, article 124, soin de la personne"),
        ("limite", "lésion non dessinable sur la planche", "type IV possible, non figuré", "décrire sans forcer un type"),
        ("discordant", "récit et examen divergent", "les deux sont consignés", "ne pas minimiser l'examen"),
    ],
    6: [
        ("normal", "flux présent et récit non évocateur", "torsion moins probable", "surveillance seulement si le récit n'est pas typique"),
        ("positif", "scrotum aigu et réflexe crémastérien aboli", "forte suspicion", "explorer sans attendre le Doppler"),
        ("limite", "flux Doppler encore présent", "cela n'exclut pas la torsion", "explorer si le récit est typique"),
        ("discordant", "cliché gris sans couleur", "le flux n'est pas lisible", "ne pas conclure à un flux absent"),
    ],
    7: [
        ("normal", "17-OHP sous le seuil du programme", "pas de rappel sur ce prélèvement", "hyperplasie peu probable sur ce seul test"),
        ("positif", "résultat au-dessus du seuil du programme", "rappel", "confirmer, sans assigner le sexe"),
        ("limite", "zone non chiffrée dans l'extrait", "ni confirmation ni exclusion", "contrôler le prélèvement"),
        ("discordant", "clinique bruyante et test négatif", "le test ne ferme pas l'urgence", "soigner la clinique et recontrôler"),
    ],
    8: [
        ("normal", "épithélium sans îlot invasif", "pas de carcinome sur ce fragment", "autre lésion du gland ou du prépuce"),
        ("positif", "îlot malpighien invasif", "carcinome épidermoïde", "stadifier selon la recommandation, pas sur la photo"),
        ("limite", "fragment trop superficiel", "profondeur illisible", "refaire un prélèvement de 2 à 3 mm"),
        ("discordant", "lésion suspecte et histologie bénigne", "le fragment peut avoir manqué la tumeur", "nouvelle biopsie"),
    ],
    9: [
        ("normal", "gaz caverneux sans hypoxie ni acidose", "priapisme non ischémique possible", "ne pas drainer comme une ischémie sur ce seul gaz"),
        ("positif", "hypoxie, hypercapnie et acidose", "priapisme ischémique", "décomprimer, surtout au-delà de 4 h"),
        ("limite", "prélèvement douteux", "le gaz ne tranche pas", "refaire le prélèvement et traiter si la durée dépasse 4 h"),
        ("discordant", "douleur ischémique et gaz rassurants", "le prélèvement peut être inadéquat", "ne pas rassurer sur un gaz isolé"),
    ],
    10: [
        ("normal", "peau intacte, sans crépitation", "pas de gangrène sur ce seul regard", "réexaminer vite si le sepsis reste possible"),
        ("positif", "nécrose, fascia exposé ou escarre noire", "gangrène de Fournier", "débrider sans attendre une image"),
        ("limite", "rougeur sans escarre", "la peau sous-estime la nécrose", "explorer si le tableau est septique"),
        ("discordant", "peau presque normale et sepsis périnéal", "la nécrose interne est plus large", "ne pas se fier à la surface cutanée"),
    ],
}

ABSENCE = {
    0: "Aucune image unique n'est insérée dans la monographie : chaque fiche porte, ou refuse, son propre cliché.",
    1: "Aucune image libre fiable n'est insérée. Les photographies de prépuce chez l'enfant ont été écartées, et le cliché adulte repéré sur Commons n'a pas été relu image par image.",
    4: "Aucune image libre fiable n'est insérée. Les photographies d'hypospadias chez l'enfant ont été écartées, et le cliché adulte repéré n'a pas été contrôlé avant annotation.",
    7: "Aucune image libre fiable n'est insérée. Aucun cliché de buvard n'a été retenu, et aucune courbe de 17-OHP n'est dessinée.",
    9: "Aucune image libre fiable n'est insérée. Le fichier de fistule artérioveineuse du pénis est une autre entité et n'est pas montré.",
}


def bloc(n: int, bouton: str) -> str:
    p = PHRASES[n]
    titres = (
        f'<h4 id="dx{n}-p9a"><em>9.a Gold standard</em></h4>',
        f'<h4 id="dx{n}-p9b"><em>9.b 1<sup>re</sup> intention</em></h4>',
        f'<h4 id="dx{n}-p9c"><em>9.c Alternatives</em></h4>',
        f'<h4 id="dx{n}-p9d"><em>9.d 2<sup>e</sup> intention</em></h4>',
    )
    morceaux = []
    for i, (titre, phrase) in enumerate(zip(titres, p)):
        extra = (" " + bouton) if i == 0 else ""
        morceaux.append(f"{titre}\n<div class=\"p\">{e(phrase)}{extra}</div>\n")
    if n in (2, 3, 6):
        morceaux.append(
            '<details class="fc" style="display:inline;"><summary>échographie</summary>'
            "<div>Mécanisme. L'onde ultrasonore revient selon les interfaces : le liquide est anéchogène, "
            "le tissu intermédiaire est hypoéchogène et le tissu dense est hyperéchogène. "
            "Exemple chiffré. Aucun seuil en décibels n'est dans l'extrait relu. "
            "Piège d'examen. Le cliché ne remplace pas l'examen de référence lorsque la recommandation l'interdit. "
            "Source [S9].</div></details>\n"
        )
    if n in IMAGES:
        morceaux.append(figure(n))
    else:
        morceaux.append(f'<div class="leg">{e(ABSENCE[n])}</div>\n')
    morceaux.append(tableau(TABLES[n]))
    return "".join(morceaux)


def grams(texte: str) -> set[tuple[str, ...]]:
    mots = re.findall(r"[a-zà-ÿœæ0-9]+", html.unescape(texte).lower())
    return {tuple(mots[i:i + 4]) for i in range(len(mots) - 3)}


def alleger(texte: str, plafond: int = 148000) -> str:
    while len(texte.encode()) > plafond:
        trouves = list(re.finditer(r'<blockquote id="lx-[^"]+">.*?</blockquote>', texte, re.S))
        if len(trouves) < 2:
            break
        m = trouves[-1]
        texte = texte[:m.start()] + texte[m.end():]
    return texte


def injecter(chemin: Path, n: int) -> None:
    texte = chemin.read_text(encoding="utf-8")
    if ".stitre{" not in texte:
        texte = texte.replace("</style>", CSS + "\n</style>", 1)
    motif = re.compile(
        rf'(<h3 id="dx{n}-p9"><strong>9\. Examens complémentaires</strong></h3>\n)'
        rf'<div class="p">(.*?)</div>\n',
        re.S,
    )
    m = motif.search(texte)
    if not m:
        raise SystemExit(f"point 9 introuvable : {chemin.name}")
    bouton = re.search(r"<button\b.*?</button>", m.group(2), re.S)
    if not bouton:
        raise SystemExit(f"bouton absent : {chemin.name}")
    # 4-grammes déjà dans les div.p, hors la phrase remplacée.
    sans = texte[:m.start()] + texte[m.end():]
    deja = set()
    for bloc_p in re.findall(r'(?is)<div class="p">(.*?)</div>', sans):
        propre = re.sub(r"(?is)<button.*?</button>", " ", bloc_p)
        deja |= grams(propre)
    nouveau = bloc(n, bouton.group(0))
    adds = set()
    for bloc_p in re.findall(r'(?is)<div class="p">(.*?)</div>', nouveau):
        propre = re.sub(r"(?is)<button.*?</button>", " ", bloc_p)
        g = grams(propre)
        choc = (g & deja) | (g & adds)
        if choc:
            raise SystemExit(f"{chemin.name} 4-gramme répété : {next(iter(choc))}")
        adds |= g
    texte = texte[:m.start()] + m.group(1) + nouveau + texte[m.end():]
    if n in (2, 3, 6) and 'id="sb-9"' not in texte:
        texte = texte.replace(
            '</ol>\n<p class="nv">',
            '<li id="sb-9">[S9] CNP de médecine nucléaire — Terminologie en imagerie, consulté le 9 novembre 2026. '
            'https://www.cnp-mn.fr/les-fondamentaux-terminologie-en-imagerie/</li>\n</ol>\n<p class="nv">',
            1,
        )
    texte = alleger(texte)
    chemin.write_text(texte, encoding="utf-8")
    print(chemin.name, len(texte.encode()), "img", texte.count("<img "))


def main() -> None:
    fichiers = {0: LOT / "LOT_131_Phase_A_V0.html"}
    for n in range(1, 11):
        fichiers[n] = LOT / f"LOT_131_Phase_B_V0_DX.{n}.html"
    for n, chemin in fichiers.items():
        if 'id="dx%s-p9a"' % n in chemin.read_text(encoding="utf-8"):
            print("deja", chemin.name)
            continue
        injecter(chemin, n)


if __name__ == "__main__":
    main()
