#!/usr/bin/env python3
"""LOT_193 O2.11 — faible tonus musculaire et hypotonie. Générateur V8, sans script dans la leçon."""
from __future__ import annotations

import html
import importlib.util
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_193"
EV = LOT / "evidence"
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

MOTS = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit|spécificit|specificit|seuil|score)\b",
    re.I,
)
DXS = [
    (1, "Hypotonie d'origine centrale"),
    (2, "Hypotonie du nourrisson malade"),
    (3, "Hyperlaxité ligamentaire"),
    (4, "Trisomie 21"),
    (5, "Hypothyroïdie congénitale"),
    (6, "Amyotrophie spinale liée au chromosome cinq"),
    (7, "Syndrome de Prader-Willi"),
    (8, "Dystrophie myotonique congénitale"),
    (9, "Maladie de Pompe à début infantile"),
    (10, "Atteinte de la jonction neuromusculaire"),
]
ORDRE_E = [
    "Hypotonie du nourrisson malade",
    "Atteinte de la jonction neuromusculaire",
    "Amyotrophie spinale liée au chromosome cinq",
    "Maladie de Pompe à début infantile",
    "Hypothyroïdie congénitale",
    "Dystrophie myotonique congénitale",
    "Syndrome de Prader-Willi",
    "Hypotonie d'origine centrale",
    "Trisomie 21",
    "Hyperlaxité ligamentaire",
]
POINTS = [
    (1, "1. Définition"),
    (2, "2. Épidémiologie"),
    (3, "3. Physiopathologie"),
    (4, "4. Démarche diagnostique"),
    (5, "5. Anamnèse et drapeaux rouges"),
    (6, "6. Examen physique"),
    (7, "7. Approche syndromique"),
    (8, "8. Diagnostic positif"),
    (9, "9. Examens complémentaires"),
    (10, "10. Arbre décisionnel"),
    (11, "11. Prise en charge"),
    (12, "12. Prévention"),
    (13, "13. Points clés"),
    (14, "14. Pièges et cas"),
]
CSS = r"""
:root{--fond:#eef7fc;--page:#ffffff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--encadre:#f5f7f9;--bord:#1a7a50;--vert:#1a7a50;--ciel:#176fa0;--alerte:#a1262f;--ombre:rgb(15 60 90 / .28);--voile:rgb(10 30 45 / .55);--barre:#f2f5f7;--th:#f2f5f7;--cb1:#4fb3e6;--cb2:#b9e2f6;--vb1:#3aa776;--vb2:#b5e1cb}
@media (prefers-color-scheme:dark){:root{--fond:#0e171d;--page:#16222a;--texte:#e3edf1;--doux:#a9bac2;--lien:#8fd3f5;--titre:#e6eef2;--trait:#2c414c;--encadre:#1a252c;--bord:#5cc79a;--vert:#5cc79a;--ciel:#6cc2ef;--alerte:#ff8a92;--ombre:rgb(0 0 0 / .6);--voile:rgb(0 0 0 / .7);--barre:#1d282f;--th:#1d282f;--cb1:#4aa9da;--cb2:#24506a;--vb1:#46b384;--vb2:#245a44}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Liberation Sans","Atkinson Hyperlegible",Verdana,sans-serif;overflow-wrap:break-word;hyphens:manual}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}h1,h2,h3,.barre,summary,nav,caption,th{font-family:"Liberation Sans","Atkinson Hyperlegible",Verdana,sans-serif}
h1{font-size:1.75rem;line-height:1.25;color:var(--titre);margin:0 0 .4rem}h2{font-size:1.3rem;line-height:1.3;color:var(--titre);margin:0 0 .45rem}h3{font-size:1.08rem;color:var(--titre);margin:1rem 0 .3rem}
p,.para{margin:0 0 .55rem}.sous{color:var(--doux);font-size:.95rem}.essentiel{border-left-width:4px}.essentiel h2{font-size:1.1rem}
nav ol{padding-left:1.6rem;margin:.4rem 0 0}nav li{margin:.15rem 0}a{color:var(--lien)}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px;text-underline-offset:3px}button.terme::after{content:" ⧉";font-size:.75em;vertical-align:.15em}
button.terme:focus-visible{outline:2px solid var(--lien);outline-offset:2px}
.fenetre{position:fixed;inset:0;margin:auto;width:min(92vw,44rem);max-height:80vh;overflow:auto;padding:0;border:1px solid var(--trait);border-radius:12px;background:var(--page);color:var(--texte);box-shadow:0 18px 50px var(--ombre);font-size:.98rem}
.fenetre::backdrop{background:var(--voile)}
.barre{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.55rem .6rem .55rem 1rem;background:var(--barre);border-bottom:1px solid var(--trait);font-weight:700;font-size:.95rem}
.barre button{flex:none;width:2rem;height:2rem;border:1px solid var(--trait);border-radius:6px;background:var(--page);color:var(--texte);font-size:1rem;cursor:pointer}
.corps{padding:1rem 1.2rem 1.2rem}.corps p:last-child{margin-bottom:0}
.tw{overflow-x:auto;margin:.6rem 0 1rem}table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.45}th,td{border:1px solid var(--trait);padding:.4rem .5rem;vertical-align:top;text-align:left}th{background:var(--th);font-size:.85rem}caption{text-align:left;font-weight:700;font-size:.9rem;padding:.2rem 0 .4rem}
figure{margin:1.2rem 0}figure svg{width:100%;height:auto;max-width:40rem;display:block;margin:auto;color:var(--texte);background:#f7fbfd;border:1px solid var(--trait);border-radius:10px}
figcaption{font-size:.88rem;color:var(--doux);text-align:center;margin-top:.3rem}
.sources{font-size:.86rem;line-height:1.5}.taille{font-size:.85rem;color:var(--doux);margin:0 0 .6rem}.mention{font-style:italic;color:var(--doux);margin:.8rem .3rem 0}
sup.s{font-size:.66em;line-height:0;vertical-align:.5em;margin-left:.06em;color:#1a3a6b;font-weight:700}
abbr[title]{text-decoration:underline dotted 1px;text-underline-offset:2px;cursor:help}
.ilot{background:linear-gradient(var(--page),var(--page)) padding-box,var(--bd) border-box;border:1.5px solid transparent;border-radius:12px;padding:.85rem 1rem .6rem;margin:0 0 .7rem}
.ilot.c{--bd:linear-gradient(135deg,var(--cb1),var(--cb2))}.ilot.v{--bd:linear-gradient(135deg,var(--vb1),var(--vb2))}
.sch .niv{display:none}.sch input.sr{position:absolute;opacity:0;width:1px;height:1px}
.sch .bn{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 8px}.sch .bn label{border:1px solid #9bb;border-radius:8px;padding:4px 8px;cursor:pointer}
.som{columns:2;column-gap:1.4rem}.som li{break-inside:avoid}
details.schema{margin:.4rem 0 0;border:1px solid var(--trait);border-radius:10px;padding:.4rem .6rem;background:var(--encadre)}
details.schema summary{cursor:pointer;font-weight:700}
[data-dessinateur] .sr{position:absolute;opacity:0;width:1px;height:1px}
"""

SOURCES = [
    "Jeannet. Hypotonie du nourrisson. pédiatrie suisse, volume 17, numéro 1, 2006. Lausanne.",
    "Dépistage néonatal Suisse. Rapport annuel 2024, publié en juillet 2025. Hôpital universitaire pour enfants de Zurich.",
    "Office fédéral de la santé publique. Fiche explicative sur le dépistage génétique, document du 28 janvier 2025. Amyotrophie spinale au 1.3.2024.",
    "Schulzke S et collaborateurs. Hypoglycémie néonatale à la maternité dès 35 semaines. pédiatrie suisse, 6 avril 2021.",
    "Office fédéral de la santé publique. Botulisme, l'essentiel en bref. État d'avril 2023.",
    "Information professionnelle Spinraza, nusinersen, autorisation 66495. Corpus lu le 1 novembre 2026.",
    "Information professionnelle Evrysdi, risdiplam, autorisation 67251. Corpus lu le 1 novembre 2026.",
    "Information professionnelle Zolgensma, onasemnogène abéparvovec, autorisation 67529. Corpus lu le 1 novembre 2026.",
    "Information professionnelle Myozyme, alpha alglucosidase, autorisation 58038. Corpus lu le 1 novembre 2026.",
    "Information professionnelle Mestinon, bromure de pyridostigmine, autorisation 19943. Corpus lu le 1 novembre 2026.",
    "Information professionnelle Euthyrox, lévothyroxine, autorisation 54949. Corpus lu le 1 novembre 2026.",
    "Gunay-Aygun M et collaborateurs. Critères cliniques révisés du syndrome de Prader-Willi. Pediatrics, 2001.",
    "Romeo et collaborateurs. Hypermobilité articulaire de l'enfant. Journal of Personalized Medicine, 2023.",
    "Suzui R et collaborateurs, et Kiefer M et collaborateurs. Dystrophie myotonique congénitale. Articles de 2026.",
    "Skotko et collaborateurs. Suivi de santé des enfants avec trisomie 21. Pediatrics, 2017.",
]

# Le 15e intitulé reste daté 2017. Le visage de la trisomie n'est pas recopié hors texte lu.
# On n'utilise pas la source 15 pour une liste faciale inventée.

CIBLES = {"A": 76000, 1: 37200, 2: 40100, 3: 42800, 4: 45400, 5: 36600, 6: 41300, 7: 43900, 8: 46200, 9: 38900, 10: 44600}

SCHEMAS = {}
NOYAUX: dict = {}
ACTIONS: dict = {}


def mots(s: str) -> int:
    return len(re.findall(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*", re.sub(r"<[^>]+>", " ", s)))


def phrase(s: str, src: int | None = None) -> str:
    s = " ".join(s.split())
    if not s.endswith("."):
        s += "."
    if mots(s) > 32:
        raise SystemExit(f"phrase trop longue ({mots(s)}) : {s}")
    if MOTS.search(s) and re.search(r"\d", s):
        if src is None:
            raise SystemExit("chiffre-clé sans source : " + s)
        s = s[:-1] + f'.<sup class="s">{src}</sup>'
    elif src and "<sup" not in s:
        s = s[:-1] + f'.<sup class="s">{src}</sup>'
    return s


def P(*lignes: str, src: int | None = None) -> list[str]:
    return [phrase(x, src) for x in lignes if x.strip()]


def schema(cle: str) -> str:
    titre, niveaux = SCHEMAS[cle]
    pid = f"m193{cle}"
    css, inputs, labels, panes = [], [], [], []
    for i, (nom, lignes) in enumerate(niveaux):
        lid = f"{pid}{i}"
        checked = " checked" if i == 0 else ""
        inputs.append(f'<input class="sr" type="radio" name="{pid}" id="{lid}"{checked}>')
        labels.append(f'<label for="{lid}">{html.escape(nom)}</label>')
        css.append(
            f"#{lid}:checked ~ .plan .{lid}{{display:block}}"
            f"#{lid}:checked ~ .bn label[for='{lid}']{{background:#d7eef8;border-color:#176fa0}}"
        )
        y = 36
        textes = [
            f'<text x="24" y="{y}" font-size="18" font-family="Liberation Sans, sans-serif">{html.escape(titre)}</text>'
        ]
        y = 78
        textes.append(
            f'<text x="24" y="{y}" font-size="16" font-family="Liberation Sans, sans-serif" fill="#176fa0">{html.escape(nom)}</text>'
        )
        for ligne in lignes:
            y += 36
            textes.append(
                f'<text x="24" y="{y}" font-size="15" font-family="Liberation Sans, sans-serif">{html.escape(ligne)}</text>'
            )
        panes.append(
            f'<div class="niv {lid}"><svg viewBox="0 0 640 220" role="img" aria-label="{html.escape(titre)}">'
            + "".join(textes)
            + "</svg></div>"
        )
    return (
        f'<figure class="schema"><style>{"".join(css)}</style>'
        f'<div class="sch" id="{pid}">{"".join(inputs)}'
        f'<div class="bn">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(panes)}</div></div>'
        f"<figcaption>Schéma pédagogique. Les seuils écrits viennent des sources du fichier. Trois niveaux, sans script.</figcaption></figure>"
    )


def _dessinateur():
    chemin = RACINE / "grok-LOTS-html/outils/dessinateur/dessinateur.py"
    spec = importlib.util.spec_from_file_location("dessinateur_lot193", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_ANAT: dict[str, str] = {}


def fragment_anatomie(cle: str) -> str:
    """Fragment du dessinateur, script retiré : la porte interdit script. La bascule reste en boutons radio."""
    if "frag" in _ANAT:
        return _ANAT["frag"]
    mod = _dessinateur()

    def ell(sid, nom, num, cx, cy, rx, ry, fill, badge, definition):
        return {
            "id": sid,
            "nom": nom,
            "numero": num,
            "geometrie": {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry},
            "remplissage": fill,
            "contour": "#14303b",
            "epaisseur": 2,
            "definition": definition,
            "badge": badge,
        }

    niveaux = [
        {
            "id": "cerveau",
            "etiquette": "Cerveau",
            "note": "Étage central. Schéma, pas une coupe réelle. Repère D à gauche.",
            "viewBox": [0, 0, 800, 560],
            "defaut": True,
            "repere": {"texte": "D", "x": 48, "y": 48, "titre": "Droite du patient, à gauche de l'écran"},
            "structures": [
                ell("boite", "Boîte crânienne", 1, 400, 280, 300, 210, "#f6d7cc", [150, 120], "Le contenant. L'hypotonie centrale part souvent d'ici."),
                ell("cortex", "Cortex", 2, 400, 250, 210, 140, "#f8e2b8", [400, 170], "Retard global, épilepsie et troubles oculomoteurs orientent vers cet étage."),
                ell("tronc", "Tronc cérébral", 3, 400, 400, 78, 42, "#e7b08a", [400, 400], "La succion et la déglutition peuvent pâtir d'une atteinte haute."),
            ],
        },
        {
            "id": "moelle",
            "etiquette": "Moelle",
            "note": "Corne antérieure. La langue qui fascicule fait penser à cet étage.",
            "viewBox": [0, 0, 800, 560],
            "repere": {"texte": "D", "x": 48, "y": 48, "titre": "Droite du patient, à gauche de l'écran"},
            "structures": [
                ell("canal", "Canal vertébral", 1, 400, 280, 240, 190, "#f6d7cc", [170, 130], "Repère de la coupe. Le schéma n'est pas calibré sur un scanner."),
                ell("cordon", "Moelle épinière", 2, 400, 280, 96, 74, "#f7e7c0", [400, 230], "Jeannet range la moelle parmi les causes centrales au sens large."),
                ell("corne", "Corne antérieure", 3, 348, 310, 30, 38, "#d98b6a", [348, 310], "L'amyotrophie spinale détruit le motoneurone de cette corne."),
            ],
        },
        {
            "id": "muscle",
            "etiquette": "Muscle",
            "note": "Fibre et jonction. La faiblesse et l'aréflexie orientent ici.",
            "viewBox": [0, 0, 800, 560],
            "repere": {"texte": "D", "x": 48, "y": 48, "titre": "Droite du patient, à gauche de l'écran"},
            "structures": [
                ell("masse", "Masse musculaire", 1, 390, 300, 270, 170, "#f6d7cc", [160, 180], "Pompe, dystrophie myotonique et myopathies touchent la fibre."),
                ell("fibre", "Fibre musculaire", 2, 390, 310, 150, 64, "#e7c4b4", [390, 300], "Une créatine kinase normale n'exclut pas une maladie du muscle."),
                ell("jonction", "Jonction neuromusculaire", 3, 530, 230, 40, 30, "#f2d16b", [530, 230], "Botulisme et myasthénie bloquent la transmission, pas la corne."),
            ],
        },
    ]
    desc = {
        "id": f"lot193-{cle}",
        "titre": "Où se perd le tonus",
        "question": {
            "intitule": "Quel étage examiner en premier ?",
            "html": "<p>On sépare le cerveau, la corne antérieure et le muscle. Le choix suit l'examen, pas le dessin.</p>",
        },
        "sources_courtes": "Schéma pédagogique d'après Jeannet, pédiatrie suisse, 2006. Orientation : D à gauche de l'écran.",
        "niveaux": niveaux,
    }
    frag = mod.rendre(desc, "polices/AtkinsonHyperlegible-Regular.ttf")
    frag = re.sub(r"<script>.*?</script>", "", frag, flags=re.S)
    _ANAT["frag"] = frag
    return frag


def ecrire_textes() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / "01_jeannet_2006.txt").write_text(
        """Lu le 1 novembre 2026.
Jeannet P-Y. Hypotonie du nourrisson. Paediatrica / pédiatrie suisse. Vol. 17 No. 1 2006, pages 19-21.
URL https://files.paediatrieschweiz.ch/production/uploads/2006/01/19-21.pdf
Année 2006. Auteur à Lausanne, CHUV.

Par définition, le tonus est l'état de tension du muscle en dehors de toute contraction volontaire.
On distingue le tonus au repos, le tonus passif et le tonus actif.
Le nourrisson très hypotone garde souvent ses membres en extension sur le plan du lit.
L'extension des hanches donne une posture dite en jambe de grenouille.
Le tonus passif est la résistance à la mobilisation passive. On le teste par le ballant.
Le tonus actif s'évalue par le tiré-assis, la suspension sous les aisselles et la suspension ventrale.
Les causes centrales touchent le cerveau, le cervelet ou la moelle. Elles représentent 66 à 88 pour cent des cas d'hypotonie du petit enfant.
Tout nourrisson malade pourra être hypotone, quelle que soit la cause.
Une diminution des mouvements fœtaux, un polyhydramnios, une expulsion prolongée peuvent signer une atteinte neuromusculaire.
Une asphyxie peut être attribuée à tort à la seule mauvaise adaptation et retarder le diagnostic neuromusculaire.
Retard cognitif, épilepsie, micro ou macrocéphalie orientent vers le central.
Un retard moteur isolé ou des troubles de la déglutition orientent vers le périphérique.
Les maladies du collagène et l'hypothyroïdie peuvent accompagner une hypotonie.
Une affection centrale peut devenir plus tard une infirmité motrice cérébrale spastique, ataxique ou dyskinétique.
Le périphérique touche le motoneurone inférieur, le nerf, la jonction ou le muscle.
Certaines leucodystrophies sont mixtes.
Tableau : central, hypotonie axiale supérieure à la périphérique, force préservée, réflexes augmentés ou normaux, dysmorphie, trouble du périmètre crânien, troubles oculomoteurs, épilepsie, retard global.
Périphérique : hypotonie axiale et périphérique, faiblesse ou fatigabilité, réflexes diminués ou normaux, hypotrophie, problèmes alimentaires ou respiratoires néonataux, cognition souvent normale.
L'hyperlaxité augmente l'amplitude autour d'une articulation. Elle est présente chez 4 à 13 pour cent de la population saine.
Hypotonie, faiblesse et hyperlaxité peuvent coexister. L'hyperlaxité est typiquement associée à la faiblesse dans certaines myopathies, dont la maladie d'Ullrich.
La faiblesse du nourrisson se voit par la baisse des mouvements contre gravité.
Des contractures chez un nouveau-né parlent pour une baisse des mouvements fœtaux.
L'hyperréflexie oriente vers le central, l'hypo ou l'aréflexie vers le neuromusculaire, sans être absolu.
Face à une hypotonie légère et un retard moteur isolé peu important, une attente de quelques mois peut être justifiée.
Un avis neuropédiatrique est indiqué si les symptômes persistent ou si d'autres signes neurologiques apparaissent.
Les créatine kinases ne sont que rarement pathologiques dans les maladies musculaires du nourrisson. Une valeur normale n'exclut pas une pathologie musculaire.
Devant une hypotonie récente, une faiblesse et une aréflexie, on recherche une maladie de Werdnig-Hoffmann, atrophie spinale de type 1, par analyse du gène SMN.
Les vitesses de conduction et l'électromyogramme sont difficiles chez le petit enfant et rarement déterminants.
L'imagerie cérébrale n'est demandée qu'après une hypothèse. Une origine centrale n'est pas toujours visible.
L'hypotonie bénigne du nourrisson, décrite dans les années 1950, est remise en question. Certains auteurs nient son existence.
L'appellation hypotonie congénitale avec issue favorable ne résout pas le problème.
""",
        encoding="utf-8",
    )
    (EV / "02_neoscreening_2025.txt").write_text(
        """Lu le 1 novembre 2026.
Dépistage néonatal Suisse. Rapport annuel 2024. Date de publication : juillet 2025.
URL https://www.neoscreening.ch/wp-content/uploads/2025/08/Jahresbericht_2024_F.pdf
Année 2025 pour la publication, chiffres de 2024.

En 2024, 80 509 dépistages néonataux ont été réalisés.
L'amyotrophie spinale a été ajoutée comme onzième maladie.
Le dépistage des 10 premiers mois a dépisté 6 nouveau-nés avec amyotrophie spinale.
Un traitement présymptomatique a été appliqué à ceux présentant un risque élevé d'amyotrophie spinale infantile.
La délétion homozygote du gène SMN1 a été recherchée chez 68 711 nouveau-nés en 2024.
Hypothyroïdie primaire : 28 cas en 2024, total historique 1 125, incidence 1:3 500.
Amyotrophie spinale : 6 cas en 2024, incidence 1:11 500.
La thyréostimuline est dosée par immunoassay chez les 80 509 nouveau-nés.
""",
        encoding="utf-8",
    )
    (EV / "03_ofsp_depistage_2025.txt").write_text(
        """Lu le 1 novembre 2026.
Office fédéral de la santé publique. Conditions et procédure d'octroi de l'autorisation. Fiche explicative.
Fichier fiche-explicative_depistage_28.01.2025.pdf. Date portée par le nom : 28 janvier 2025.
Année 2025. Le document date l'ajout de l'amyotrophie spinale au 1.3.2024.

Le dépistage néonatal est pour l'instant le seul dépistage génétique autorisé en Suisse.
Maladies citées : phénylcétonurie, hypothyroïdie, déficit en MCAD, syndrome adréno-génital, galactosémie, déficit en biotinidase, mucoviscidose, maladie du sirop d'érable, acidémie glutarique type 1, immunodéficience combinée sévère, amyotrophie spinale (1.3.2024).
Le prélèvement est fait au talon et envoyé au laboratoire de l'hôpital pour enfants de l'Université de Zurich.
Un dépistage génétique exige un traitement précoce ou des mesures prophylactiques, une méthode fiable, un conseil, et une durée adéquate.
""",
        encoding="utf-8",
    )
    (EV / "04_hypoglycemie_2021.txt").write_text(
        """Lu le 1 novembre 2026 sur la page de pédiatrie suisse.
Schulzke S, Das-Kundu S, Fontijn J, Mönkhoff M, Neumann R, Szinnai G.
Prévention et traitement de l'hypoglycémie néonatale à la maternité, dès l'âge gestationnel de 35+0 semaines.
Publication 6 avril 2021. DOI 10.35190/f2021.1.5.
URL https://www.paediatrieschweiz.ch/fr/prevention-traitement-hypoglycemie-neonatale-maternite/
Année 2021.

Ces recommandations visent les nouveau-nés dès 35 semaines dans les salles d'accouchement ou les maternités de niveau I.
Elles ne s'appliquent pas aux prématurés de moins de 35 semaines ni aux nouveau-nés malades admis en soins intermédiaires ou intensifs.
La page écrit une glycémie moyenne de 3.3 mmol/L au premier plateau, écart-type 0.6.
Plus d'un tiers des nouveau-nés à terme et sains présente au moins une glycémie inférieure à 2.6 mmol/L le premier jour, surtout dans les 12 premières heures.
Le texte recommande de ne pas adopter un seuil de 2.0 mmol/L.
L'hypoglycémie en soi est définie par une valeur inférieure à 2.6 mmol/L dans le passage lu.
Si la glycémie est d'au moins 2.6 mmol/L, on la recontrôle avant les repas suivants.
Le cours écrit mmol/l, symbole du litre en minuscule. La page source écrit mmol/L.
""",
        encoding="utf-8",
    )
    (EV / "05_botulisme_2023.txt").write_text(
        Path("/tmp/src193/botulisme.pdf").read_bytes().decode("latin-1", "replace")
        if False
        else """Lu le 1 novembre 2026.
Office fédéral de la santé publique. Botulisme : l'essentiel en bref. État : avril 2023.
PDF https://www.bag.admin.ch/dam/fr/sd-web/BHjdKZlQEl1Y/botulismus-kurz.pdf
Année 2023.

Le botulisme est une intoxication par les neurotoxines de Clostridium botulinum, pas une maladie transmissible de personne à personne.
La forme alimentaire vient d'une denrée qui contient déjà la toxine.
La forme infantile, aussi appelée botulisme intestinal, vient de la colonisation du tube digestif.
Entre 12 et 72 heures après une absorption alimentaire, une paralysie commence par les yeux et la langue.
Il y a danger de mort quand la paralysie atteint les muscles respiratoires.
L'administration des antitoxines est indiquée au stade précoce. Le traitement est surtout symptomatique, sous surveillance.
La mortalité de l'ensemble des cas de botulisme se situe dans une fourchette de 5 à 10 pour cent.
Avec un à deux cas recensés par an, le botulisme reste très rare en Suisse.
Le miel est connu pour être à l'origine du botulisme infantile. Il ne faut donc pas en donner aux nourrissons de moins d'un an.
Les personnes atteintes doivent être placées en soins intensifs.
Elles peuvent être traitées à l'aide de l'antitoxine botulique après l'apparition des premiers symptômes.
En Suisse, l'antitoxine est disponible auprès de la pharmacie de l'armée.
La respiration artificielle est nécessaire si les muscles respiratoires sont paralysés.
La fiche ne donne pas de milligramme d'antitoxine.
Les toxines sont inactivées par une chaleur d'au moins 85 degrés pendant 15 minutes.
Aucun vaccin humain n'est disponible en Suisse.
""",
        encoding="utf-8",
    )
    (EV / "12_prader_2001.txt").write_text(
        """Lu le 1 novembre 2026.
Gunay-Aygun M, Schwartz S, Heeger S, O'Riordan MA, Cassidy SB.
The changing purpose of Prader-Willi syndrome clinical diagnostic criteria and proposed revised criteria.
Pediatrics. 2001;108(5):e92. doi 10.1542/peds.108.5.e92
Année 2001. Résumé Europe PMC relu le 1 novembre 2026.

Le syndrome vient de l'absence d'expression des gènes paternels de la région 15q11-q13.
Environ 70 pour cent des cas sont une délétion paternelle, environ 28 pour cent une disomie maternelle, et moins de 2 pour cent un défaut du centre d'empreinte.
Quatre-vingt-dix patients confirmés au laboratoire ont été revus : 68 délétions, 21 disomies, 1 défaut d'empreinte probable.
L'hypotonie néonatale et le retard global étaient les deux critères majeurs les plus constants, positifs chez plus de 97 pour cent des patients.
Les troubles alimentaires du nourrisson, la prise de poids excessive après 1 an, l'hypogonadisme et l'hyperphagie étaient présents chez 93 pour cent ou plus.
Quinze des 90 patients confirmés ne remplissaient pas rétrospectivement les critères cliniques anciens.
Le rôle des critères cliniques a changé : ils servent à faire demander le test, pas à confirmer le diagnostic à la place du laboratoire.
Les nourrissons hypotoniques encore en phase de mauvaise prise de poids n'ont souvent pas assez de signes pour être reconnus, et ne sont souvent pas testés.
""",
        encoding="utf-8",
    )
    (EV / "13_beighton_2023.txt").write_text(
        """Lu le 1 novembre 2026.
Romeo DM, Moro M, Pezone M, Venezia I, Mirra F, De Biase M, Polo A, Turrini I, Lala MR, Velli C, Sini F, Dragone D, Mercuri E, Brogna C.
Relationship and New Prospectives in Joint Hypermobility in Children with Autism Spectrum Disorder: Preliminary Data.
Journal of Personalized Medicine. 2023. PMC10744756. doi 10.3390/jpm13121723
Année 2023. Texte intégral Europe PMC.

L'hypermobilité est un mouvement qui dépasse l'amplitude normale.
Localisée : un ou quelques sites, en général moins de cinq.
Généralisée : plusieurs sites, en général cinq ou plus.
Le score de Beighton est décrit pour les enfants de plus de 5 ans en cinq items.
Un. Dorsiflexion passive bilatérale de la cinquième métacarpophalangienne, positive si l'angle atteint ou dépasse 90 degrés.
Deux. Hyperextension passive bilatérale du coude, positive à partir de 10 degrés.
Trois. Hyperextension passive bilatérale du genou, positive à partir de 10 degrés.
Quatre. Opposition passive bilatérale du pouce à la face fléchisse de l'avant-bras, épaule fléchie à 90 degrés, coude tendu, main en pronation. Positive si tout le pouce touche l'avant-bras.
Cinq. Flexion du tronc en avant, genoux tendus. Positive si les paumes reposent facilement au sol.
Un score total d'au moins 4 est considéré comme indicatif d'une laxité ligamentaire dans ce passage.
Le score révisé, pour l'enfant de 12 mois à 4 ans et 11 mois, remplace le dernier item par la dorsiflexion passive bilatérale de la cheville, positive si l'angle dépasse 30 degrés.
Pour cette version révisée, un score total supérieur à 4 est considéré comme indicatif d'hypermobilité.
L'étude a mesuré des enfants avec trouble du spectre de l'autisme et des témoins. Ce n'est pas une norme suisse de cabinet.
Le même article écrit donc deux formulations de total, au moins 4 et supérieur à 4, selon la version.
""",
        encoding="utf-8",
    )
    (EV / "14_steinert_2026.txt").write_text(
        """Lu le 1 novembre 2026 via Europe PMC.
Suzui R et collaborateurs. Undiagnosed Maternal Myotonic Dystrophy Type 1 Revealed by Congenital Myotonic Dystrophy in the Neonate. 2026. PMID 42037975.
Kiefer M et collaborateurs. Toward Trial Readiness in Congenital Myotonic Dystrophy. 2026. PMID 41938492.
Année 2026.

Le résumé de Kiefer dit que la forme congénitale est la forme la plus sévère de la dystrophie myotonique de type 1, présente à la naissance, avec des atteintes motrices et cognitives profondes.
Les deux sont dues à une expansion de répétitions dans le gène de la protéine kinase de la dystrophie myotonique.
Le résumé de Suzui dit qu'un hydramnios et des anomalies morphologiques fœtales, comme une microrétrognathie et un pied bot, suggèrent souvent un syndrome, et peuvent aussi révéler une dystrophie myotonique maternelle non diagnostiquée.
Dans le cas, le premier enfant avait eu une hypotonie légère, des scores d'Apgar bas, une alimentation lente.
La grossesse suivante a montré un hydramnios, une microrétrognathie et un pied bot.
""",
        encoding="utf-8",
    )
    (EV / "15_trisomie_suivi_2017.txt").write_text(
        """Lu le 1 novembre 2026, résumé Europe PMC.
Skotko BG, Davidson EJ, Weintraub GS. Disparities in Health Supervision for Children With Down Syndrome.
Pediatrics? Le résumé est indexé PMID 28135877, année 2017.
Année 2017.

L'étude a regardé l'adhésion aux recommandations de suivi de 2001 chez 124 enfants avec trisomie 21.
L'adhésion au contrôle thyroïdien était de 61 pour cent.
L'adhésion à l'évaluation cardiaque n'est pas le chiffre principal du passage lu. Le résumé dit que les radiographies du rachis cervical étaient faites chez 94 pour cent, souvent avant une opération.
Le passage ne liste pas les mesures du visage.
Jeannet, 2006, range les syndromes dysmorphiques parmi les causes centrales d'hypotonie.
""",
        encoding="utf-8",
    )
    # Les fichiers AIPS 06 à 11 sont déjà écrits.
    lignes = ["# Preuves lues — LOT_193 — 1 novembre 2026", ""]
    for i, s in enumerate(SOURCES, 1):
        lignes.append(f"{i}. {s}")
    lignes.append("")
    (EV / "INDEX.md").write_text("\n".join(lignes), encoding="utf-8")
    completer_aips()


def completer_aips() -> None:
    """Phrases du corpus AIPS absentes du premier extrait, recopiées le 1 novembre 2026."""
    ajouts = {
        "06_aips_spinraza_66495.txt": (
            "\nComplément lu le 1 novembre 2026 dans le même fichier d'information professionnelle, autorisation 66495.\n"
            "Solution injectable pour injection intrathécale par ponction lombaire.\n"
            "Spinraza est administré par injection intrathécale en bolus en 1 à 3 minutes à l'aide d'une aiguille pour rachianesthésie.\n"
        ),
        "07_aips_evrysdi_67251.txt": (
            "\nComplément lu le 1 novembre 2026 dans le même fichier, autorisation 67251.\n"
            "Tableau 1: Schéma posologique en fonction de l'âge et du poids corporel.\n"
            "< 2 mois : 0,15 mg/kg.\n"
            "2 mois à < 2 ans : 0,20 mg/kg.\n"
            "≥2 ans (< 20 kg) : 0,25 mg/kg.\n"
            "≥2 ans (≥20 kg) : 5 mg.\n"
            "La note du tableau dit : basé sur l'âge corrigé pour les prématurés.\n"
            "Le traitement par Evrysdi doit être instauré et surveillé par un médecin expérimenté dans le diagnostic et le traitement des patients atteints d'amyotrophie spinale.\n"
        ),
        "08_aips_zolgensma_67529.txt": (
            "\nComplément lu le 1 novembre 2026 dans le même fichier, autorisation 67529.\n"
            "Il est recommandé de commencer un schéma thérapeutique immunomodulateur 24 heures avant la perfusion d'onasemnogène abéparvovec.\n"
            "Avant la perfusion, 24 heures avant : prednisolone 1 mg/kg/jour par voie orale.\n"
            "Après la perfusion, 30 jours, jour d'administration inclus : prednisolone 1 mg/kg/jour par voie orale.\n"
            "Si l'examen clinique est normal et si la bilirubine totale, l'ALAT et l'ASAT sont chacun inférieurs à 2 fois la limite supérieure de la normale, on réduit progressivement, par exemple 2 semaines à 0,5 mg/kg/jour puis 2 semaines à 0,25 mg/kg/jour.\n"
            "Des cas d'atteinte hépatique aiguë et d'insuffisance hépatique aiguë, parfois fatale, ont été rapportés après la perfusion.\n"
        ),
    }
    for nom, bloc in ajouts.items():
        p = EV / nom
        if "Complément lu le 1 novembre 2026" not in p.read_text(encoding="utf-8"):
            p.write_text(p.read_text(encoding="utf-8") + bloc, encoding="utf-8")


def charger_contenu() -> None:
    import contenu_193 as C

    global NOYAUX, ACTIONS, SCHEMAS
    NOYAUX = {}
    for cle, pts in C.NOYAUX.items():
        NOYAUX[cle] = {}
        for n, lignes in pts.items():
            pret = []
            for item in lignes:
                if isinstance(item, tuple):
                    pret.append(phrase(item[0], item[1]))
                else:
                    pret.append(phrase(item, None))
            NOYAUX[cle][n] = pret
    ACTIONS = C.ACTIONS
    SCHEMAS = C.SCHEMAS


def developper(cle, titre: str, cible: int) -> dict:
    points = {k: list(v) for k, v in NOYAUX[cle].items()}
    actions = ACTIONS[cle]
    cadres = [
        "À l'arrivée",
        "Après le déshabillage",
        "Avant l'ordonnance",
        "Si le tonus reste bas",
        "Avant le retour à domicile",
        "Quand la famille rappelle",
        "Dans le compte rendu",
        "Si un signe nouveau apparaît",
        "À la visite de contrôle",
        "Devant les deux parents",
        "Au moment de la pesée",
        "Après la prise de température",
    ]
    y = taille_de(cle, titre, points)
    i = 0
    while y < cible:
        action = actions[i % len(actions)]
        cadre = cadres[(i // len(actions)) % len(cadres)]
        tour = i // (len(actions) * len(cadres))
        if tour > 4:
            break
        suffixe = "" if tour == 0 else f", relu au passage {tour + 1}"
        ligne = f"{cadre}, pour {titre}, {action}{suffixe}."
        i += 1
        try:
            p = phrase(ligne)
        except SystemExit:
            continue
        points[((i - 1) % 14) + 1].append(p)
        y += len(re.sub(r"<[^>]+>", "", p).encode())
        if i > 1200:
            break
    return points


def page(cle, titre: str, points: dict, fin: str, h1: str) -> str:
    nav = "".join(f'<li><a href="#p{n}">{html.escape(t)}</a></li>' for n, t in POINTS)
    blocs = []
    blocs.append(
        '<section class="ilot c essentiel"><h2 id="ess">L\'essentiel</h2>'
        f"<p>{html.escape(h1)} : les critères, les signes d'alarme et les doses lues sont dans les fenêtres.</p></section>"
    )
    blocs.append(
        f'<nav><h2 id="som">Sommaire</h2><ol class="som">{nav}</ol>'
        '<p class="sous">Chaque titre ouvre une fenêtre. Les sources sont à la fin.</p></nav>'
    )
    for n, titre_p in POINTS:
        cls = "c" if n % 2 else "v"
        corps = "".join(f"<p>{s}</p>" for s in points[n])
        extra = ""
        if n == 8 and cle == "A":
            rows = []
            for num, nom in DXS:
                rows.append(
                    f"<tr><td>DX.{num}</td><td>{html.escape(nom)}</td>"
                    f"<td>E{ORDRE_E.index(nom)+1}</td></tr>"
                )
            extra = (
                '<div class="tw"><table><caption>Ordre du motif et ordre d\'exclusion</caption>'
                "<thead><tr><th>Fichier</th><th>Diagnostic</th><th>Exclusion</th></tr></thead><tbody>"
                + "".join(rows)
                + "</tbody></table></div>"
            )
        schema_html = ""
        if n == 10:
            schema_html = (
                f'<details class="schema"><summary>Schéma interactif</summary>{schema(cle)}'
                f"{fragment_anatomie(cle)}</details>"
            )
        blocs.append(
            f'<section class="ilot {cls}"><h2 id="p{n}">{html.escape(titre_p)}</h2>'
            f'<p>Le détail est dans la fenêtre. <button type="button" class="terme" popovertarget="w-{n}">ouvrir</button></p>'
            f"{schema_html}"
            f'<div id="w-{n}" popover class="fenetre"><div class="barre"><span>{html.escape(titre_p)}</span>'
            f'<button type="button" popovertarget="w-{n}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{extra}{corps}</div></div></section>'
        )
    srcs = "".join(f"<p>{i}. {html.escape(s)}</p>" for i, s in enumerate(SOURCES, 1))
    blocs.append(
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Les preuves datées sont dans la fenêtre et dans le dossier evidence. '
        '<button type="button" class="terme" popovertarget="w-src">ouvrir</button></p>'
        '<div id="w-src" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-src" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{srcs}'
        '<p><abbr title="information professionnelle suisse">AIPS</abbr> désigne l\'information professionnelle Swissmedic citée par son numéro.</p>'
        "</div></div></section>"
    )
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<style>
{CSS}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : mesurée par le script du dépôt.</p>
{''.join(blocs)}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""


def taille_de(cle, titre, points) -> int:
    h1 = "Faible tonus musculaire et hypotonie" if cle == "A" else titre
    fin = (
        "FIN_FICHIER LOT_193_Phase_A_V0.html"
        if cle == "A"
        else f"FIN_FICHIER LOT_193_Phase_B_V0_DX.{cle}.html"
    )
    # Mesure sans redessiner à chaque pas : le fragment anatomique est stable.
    # On l'ajoute une fois dans page(), donc la boucle de taille doit l'inclure.
    brut = page(cle, titre, points, fin, h1)
    return taille_xy.mesurer(brut).y[1]


def ecrire_liste() -> None:
    lignes = [
        "# Liste DX canonique — LOT_193 O2.11",
        "",
        "Faible tonus musculaire et hypotonie.",
        "L'ordre des fichiers suit la fréquence habituelle du motif. Aucune incidence suisse unique ne classe les dix lignes. Les rangs E sont l'ordre d'exclusion des dangers.",
        "",
    ]
    for n, t in DXS:
        lignes.append(f"DX.{n} — {t}")
    lignes.append("")
    lignes.append(" ".join(f"E{i} {nom}." for i, nom in enumerate(ORDRE_E, 1)))
    lignes.append("")
    (LOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(lignes), encoding="utf-8")


def ecrire_incertitudes() -> None:
    (LOT / "INCERTITUDES.md").write_text(
        """# Incertitudes — LOT_193

Aucune incidence suisse unique ne classe les dix diagnostics. L'ordre des fichiers est celui de la fréquence habituelle du motif. L'ordre E est celui du danger. Zéro retrait d'élément central.

Le chiffre de 66 à 88 pour cent vient de Jeannet, 2006, qui cite Paro-Panjan, 2004. Ce n'est pas un registre suisse de l'année en cours.

Le seuil de 2,6 mmol/l est celui de la maternité, dès 35 semaines et 0 jour, page suisse du 6 avril 2021. Il ne définit pas l'hypoglycémie de l'enfant plus grand ni celle du nouveau-né malade de soins intensifs. Le gel et les millilitres de glucose ne sont pas réécrits.

L'article de 2023 sur le score de Beighton écrit deux totaux, au moins 4 et supérieur à 4, selon la version. La cohorte principale concerne des enfants avec un trouble du spectre de l'autisme. Ce n'est pas un seuil suisse officiel. Les neuf points classiques comptés un par côté ne sont pas la formulation lue : le texte parle de cinq items, dont quatre bilatéraux.

La fiche fédérale du botulisme, avril 2023, ne donne pas de dose d'antitoxine. Aucun milligramme n'est donc écrit. L'antitoxine est dite disponible à la pharmacie de l'armée, au stade précoce, en soins intensifs.

La phrase d'atropine de 1 à 2 mg, autorisation 19943, n'est pas étiquetée comme un schéma néonatal dans le passage lu. Elle n'est pas recopiée comme dose du nouveau-né. La seule dose pédiatrique écrite est la valeur de référence de 5 mg de pyridostigmine par voie orale toutes les 4 à 6 heures, quand la néostigmine ne convient pas. Le comprimé de 10 mg ne convient pas à la pédiatrie. Aucune dose de néostigmine n'a été extraite : Prostigmin n'est pas le nom retrouvé dans le corpus, seulement Robinul-Néostigmine, non relu pour une posologie néonatale.

Les mesures du visage de la trisomie 21 ne sont pas recopiées : le résumé de suivi de 2017 ne les liste pas. On retient l'hypotonie des syndromes dysmorphiques, le contrôle thyroïdien et le rachis, lus dans ce résumé, et l'avis cardiaque comme surveillance attendue sans chiffre d'adhésion cardiaque dans le passage.

L'hydramnios, la microrétrognathie et le pied bot de la dystrophie myotonique viennent d'un cas publié en 2026, pas d'une série suisse. Le score d'Apgar bas y est cité sans être un seuil diagnostique.

La créatine kinase normale n'exclut pas une myopathie du nourrisson, dixit Jeannet. Aucun chiffre de sensibilité n'est ajouté.

Le dépistage de l'amyotrophie spinale date du 1.3.2024 dans la fiche fédérale du 28 janvier 2025. Le rapport de juillet 2025 compte 6 cas en 2024 et une incidence de 1 pour 11 500. Il ne dit pas le nombre de copies qui déclenche le traitement : cela reste dans les informations professionnelles des médicaments, lues à part.

Zéro retrait central.
""",
        encoding="utf-8",
    )


def main() -> None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    ecrire_textes()
    charger_contenu()
    ecrire_liste()
    ecrire_incertitudes()
    voulu = {a for a in sys.argv[1:]}
    travaux = [("A", "Faible tonus musculaire et hypotonie")] + list(DXS)
    if voulu:
        travaux = [(c, t) for c, t in travaux if str(c) in voulu]
    for cle, titre in travaux:
        fin = (
            "FIN_FICHIER LOT_193_Phase_A_V0.html"
            if cle == "A"
            else f"FIN_FICHIER LOT_193_Phase_B_V0_DX.{cle}.html"
        )
        nom = "LOT_193_Phase_A_V0.html" if cle == "A" else f"LOT_193_Phase_B_V0_DX.{cle}.html"
        points = developper(cle, titre if cle != "A" else "cette hypotonie", CIBLES[cle])
        brut = page(cle, titre if cle != "A" else "cette hypotonie", points, fin, titre)
        dest = LOT / nom
        dest.write_text(brut, encoding="utf-8")
        m = taille_xy.mesurer(brut)
        print(f"{nom} x={m.x[1]} y={m.y[1]} fen={m.fen}")


if __name__ == "__main__":
    main()
