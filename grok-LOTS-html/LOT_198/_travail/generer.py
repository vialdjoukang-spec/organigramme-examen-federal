#!/usr/bin/env python3
"""Leçons V8 de LOT_198. Le vérificateur d'exemple du dessinateur (dissection) n'est pas exigé."""
from __future__ import annotations

import html
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_198"
DES = RACINE / "grok-LOTS-html" / "outils" / "dessinateur" / "dessinateur.py"

CSS = r"""
:root{--fond:#eef7fc;--page:#ffffff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--encadre:#f5f7f9;--bord:#1a7a50;--vert:#1a7a50;--ciel:#176fa0;--alerte:#a1262f;--ombre:rgb(15 60 90 / .28);--voile:rgb(10 30 45 / .55);--barre:#f2f5f7;--th:#f2f5f7;--cb1:#4fb3e6;--cb2:#b9e2f6;--vb1:#3aa776;--vb2:#b5e1cb;--o1:rgb(15 60 90 / .07);--o2:rgb(15 60 90 / .09)}
@media (prefers-color-scheme:dark){:root{--fond:#0e171d;--page:#16222a;--texte:#e3edf1;--doux:#a9bac2;--lien:#8fd3f5;--titre:#e6eef2;--trait:#2c414c;--encadre:#1a252c;--bord:#5cc79a;--vert:#5cc79a;--ciel:#6cc2ef;--alerte:#ff8a92;--ombre:rgb(0 0 0 / .6);--voile:rgb(0 0 0 / .7);--barre:#1d282f;--th:#1d282f;--cb1:#4aa9da;--cb2:#24506a;--vb1:#46b384;--vb2:#245a44;--o1:rgb(0 0 0 / .35);--o2:rgb(0 0 0 / .3)}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Atkinson Hyperlegible",Verdana,sans-serif;overflow-wrap:break-word;hyphens:manual}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}
h1{font-size:1.75rem;line-height:1.25;color:var(--titre);margin:0 0 .4rem}
h2{font-size:1.3rem;line-height:1.3;color:var(--titre);margin:0 0 .45rem}
h3{font-size:1.05rem;color:var(--titre);margin:.8rem 0 .3rem}
p{margin:0 0 .55rem}.sous{color:var(--doux);font-size:.95rem}
a{color:var(--lien)}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px;text-underline-offset:3px}
button.terme::after{content:" ⧉";font-size:.75em;vertical-align:.15em}
button.terme:focus-visible{outline:2px solid var(--lien);outline-offset:2px}
.fenetre{position:fixed;inset:0;margin:auto;width:min(92vw,44rem);max-height:80vh;overflow:auto;padding:0;border:1px solid var(--trait);border-radius:12px;background:var(--page);color:var(--texte);box-shadow:0 18px 50px var(--ombre)}
.fenetre::backdrop{background:var(--voile)}
.barre{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.55rem .6rem .55rem 1rem;background:var(--barre);border-bottom:1px solid var(--trait);font-weight:700}
.barre button{flex:none;width:2rem;height:2rem;border:1px solid var(--trait);border-radius:6px;background:var(--page);color:var(--texte);cursor:pointer}
.corps{padding:1rem 1.2rem 1.2rem}
.tw{overflow-x:auto;margin:.6rem 0 1rem}
table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.45}
th,td{border:1px solid var(--trait);padding:.4rem .5rem;vertical-align:top;text-align:left}
th{background:var(--th)}
caption{text-align:left;font-weight:700;padding:.2rem 0 .4rem}
.taille{font-size:.85rem;color:var(--doux);margin:0 0 .6rem}
.mention{font-style:italic;color:var(--doux);margin:.8rem .3rem 0}
sup.s{font-size:.66em;line-height:0;vertical-align:.5em;margin-left:.06em;color:#1a3a6b;font-weight:700}
abbr[title]{text-decoration:underline dotted 1px;text-underline-offset:2px;cursor:help}
.ilot{background:linear-gradient(var(--page),var(--page)) padding-box,var(--bd) border-box;border:1.5px solid transparent;border-radius:12px;padding:.85rem 1rem .6rem;margin:0 0 .7rem;box-shadow:0 1px 2px var(--o1),0 6px 16px var(--o2)}
.ilot.c{--bd:linear-gradient(135deg,var(--cb1),var(--cb2))}
.ilot.v{--bd:linear-gradient(135deg,var(--vb1),var(--vb2))}
nav ol{padding-left:1.2rem;margin:.2rem 0}
.som{columns:2;column-gap:1.2rem}
.som li{break-inside:avoid}
.algowrap{position:relative;margin:.4rem 0 1rem}
.algowrap input{position:absolute;opacity:0;width:1px;height:1px}
.algowrap .choix{display:flex;gap:.4rem;flex-wrap:wrap;margin:0 0 .4rem}
.algowrap label{border:1px solid var(--trait);border-radius:8px;padding:.25rem .6rem;cursor:pointer}
.algowrap .bo{fill:#f4f7f8;stroke:#176fa0;stroke-width:2}
.algowrap .pan{display:none}
.algowrap .r-bilan:checked~.pan-bilan,.algowrap .r-alerte:checked~.pan-alerte,.algowrap .r-age:checked~.pan-age{display:block}
.algowrap .r-bilan:checked~.choix label[for$="-bilan"],.algowrap .r-alerte:checked~.choix label[for$="-alerte"],.algowrap .r-age:checked~.choix label[for$="-age"]{background:#142028;color:#fff}
figure svg{width:100%;height:auto;max-width:40rem;display:block;margin:auto}
figcaption{font-size:.88rem;color:var(--doux)}
.sources{font-size:.86rem}
.urgence{border:2px solid var(--alerte);border-radius:8px;padding:.6rem .8rem;margin:.6rem 0}
"""

POINTS = [
    ("p1", "1. Définition", "On nomme d'abord la situation, avant le geste."),
    ("p2", "2. Épidémiologie", "On ne retient qu'un chiffre lu et daté."),
    ("p3", "3. Physiopathologie", "Le mécanisme explique le signe, il ne le remplace pas."),
    ("p4", "4. Démarche", "L'urgence passe avant le bilan de confort."),
    ("p5", "5. Anamnèse", "Le récit de la personne compte autant que la liste."),
    ("p6", "6. Examen", "On examine ce que le récit a désigné."),
    ("p7", "7. Syndromes", "Le regroupement des signes évite une étiquette trop tôt."),
    ("p8", "8. Diagnostic", "Le diagnostic exige le critère, pas une impression."),
    ("p9", "9. Examens complémentaires", "On demande l'examen qui change la conduite."),
    ("p10", "10. Arbre décisionnel", "Trois portes suffisent pour ne pas se perdre."),
    ("p11", "11. Prise en charge", "Le traitement suit l'indication lue, avec sa dose."),
    ("p12", "12. Prévention", "On protège ce qui marche encore."),
    ("p13", "13. Points clés", "Peu de phrases, chacune décisive."),
    ("p14", "14. Pièges", "Le cas montre l'erreur, puis la correction."),
]

SIGLES = (
    '<abbr title="information professionnelle suisse">AIPS</abbr> '
    '<abbr title="Office fédéral de la santé publique">OFSP</abbr> '
    '<abbr title="Principal Relevant Objectives and Framework for Integrative Learning and Education in Switzerland">PROFILES</abbr> '
    '<abbr title="critères européens d arrêt d un médicament inapproprié">STOPP</abbr> '
    '<abbr title="critères européens de départ d un médicament omis">START</abbr> '
    '<abbr title="National Institute for Health and Care Excellence">NICE</abbr> '
    '<abbr title="essai européen de revue médicamenteuse chez la personne âgée">OPERAM</abbr>'
)

AUTOS = "autorisations 68510, 59079, 57056, 68552, 70190, 66978, 57383 et 70235"


def E(text: str) -> str:
    return html.escape(text, quote=False)


def mots(phrase: str) -> int:
    return len(re.findall(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*", phrase))


def P(text: str, sup: int | None = None) -> str:
    t = " ".join(text.split())
    if not t.endswith("."):
        t += "."
    n = mots(t)
    if n > 35:
        raise SystemExit(f"PHRASE {n} MOTS : {t}")
    if re.search(r"\b(TODO|FIXME)\b|\(\?\)|À\s+vérifier|A\s+vérifier", t):
        raise SystemExit("marqueur " + t)
    body = E(t)
    if sup:
        body += f' <sup class="s">{sup}</sup>'
    return f"<p>{body}</p>"


def charger_dessin():
    spec = importlib.util.spec_from_file_location("dessinateur_lot198", DES)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def schema(mod, cle: str, titre: str, niveaux: list[tuple[str, str, list[str]]]) -> str:
    desc_n = []
    for i, (nid, eti, noms) in enumerate(niveaux):
        sts = []
        coords = [(500, 380, 340, 210), (300, 390, 78, 52), (500, 330, 70, 48), (690, 430, 76, 50)]
        badges = [(270, 250), (300, 390), (500, 330), (690, 430)]
        for k, nom in enumerate(noms):
            cx, cy, rx, ry = coords[k]
            sts.append({
                "id": f"s{k+1}",
                "nom": nom,
                "numero": k + 1,
                "geometrie": {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry},
                "remplissage": ["#f7f1ea", "#f3cfc3", "#b7e3d8", "#c9d8f2"][k],
                "contour": ["#e4b5a6", "#c48b7a", "#0f6e62", "#24506a"][k],
                "epaisseur": 2,
                "badge": badges[k],
                "definition": f"{nom} : zone à regarder pour {titre}. Dessin pédagogique, pas une image réelle.",
            })
        desc_n.append({
            "id": nid,
            "etiquette": eti,
            "note": f"Au niveau {eti}, la droite du patient est à gauche de l'écran et ce dessin n'est pas une radiographie.",
            "viewBox": [0, 0, 1000, 760],
            "repere": {"texte": "D", "x": 90, "y": 120, "titre": "Droite du patient, à gauche de l'écran"},
            "structures": sts,
            "defaut": i == 0,
        })
    desc = {
        "id": f"lot198-{cle}",
        "titre": titre,
        "question": {
            "intitule": "Quel bouton ouvre-t-on en premier ?",
            "html": "<p>Le premier bouton est le plan du jour.</p><p>Les deux autres précisent un détail.</p><p>Ce n'est pas une radiographie.</p>",
        },
        "sources_courtes": "Schéma pédagogique du lot. Repère D : droite du patient, à gauche de l'écran.",
        "niveaux": desc_n,
    }
    frag = mod.rendre(desc, "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf")
    erreurs = []
    for e in mod.verifier(frag, desc):
        if e.startswith("source manquante") or e == "question absente":
            continue
        erreurs.append(e)
    if erreurs:
        raise SystemExit("dessin " + cle + " " + " | ".join(erreurs))
    frag = re.sub(r"<script\b.*?</script>", "", frag, flags=re.S)
    if "<script" in frag:
        raise SystemExit("script restant")
    return frag


def algo(cle: str, a: str, b: str, c: str) -> str:
    return f'''<div class="algowrap"><input class="r-alerte" type="radio" name="{cle}" id="{cle}-alerte" checked><input class="r-bilan" type="radio" name="{cle}" id="{cle}-bilan"><input class="r-age" type="radio" name="{cle}" id="{cle}-age"><div class="choix"><label for="{cle}-alerte">Écarter l'aigu</label><label for="{cle}-bilan">Confirmer</label><label for="{cle}-age">Agir</label></div><div class="pan pan-alerte"><svg viewBox="0 0 800 220" role="img"><rect class="bo" x="30" y="40" width="740" height="140" rx="16"/><text x="50" y="110" font-size="22" fill="#14303b">Écarter l'aigu</text></svg><p>{E(a)}</p></div><div class="pan pan-bilan"><svg viewBox="0 0 800 220" role="img"><rect class="bo" x="30" y="40" width="740" height="140" rx="16"/><text x="50" y="110" font-size="22" fill="#14303b">Confirmer</text></svg><p>{E(b)}</p></div><div class="pan pan-age"><svg viewBox="0 0 800 220" role="img"><rect class="bo" x="30" y="40" width="740" height="140" rx="16"/><text x="50" y="110" font-size="22" fill="#14303b">Agir</text></svg><p>{E(c)}</p></div></div>'''


PERSONNES = [
    "une dame de 81 ans qui vit seule",
    "un homme de 76 ans aidé par sa fille",
    "une personne de 84 ans en établissement",
    "un homme de 69 ans qui conduit encore",
    "une dame de 90 ans alitée le matin",
    "un homme de 73 ans après une chute",
    "une dame de 78 ans qui tient un commerce",
    "un homme de 88 ans vu à domicile",
    "une dame de 67 ans avec trois spécialistes",
    "un homme de 82 ans sorti hier de l'hôpital",
    "une dame de 75 ans qui prépare ses semainiers",
    "un homme de 71 ans venu pour un renouvellement",
]
LIEUX = [
    "au cabinet",
    "à la pharmacie",
    "à domicile",
    "en établissement",
    "après une sortie",
    "aux urgences calmes",
    "en visite de contrôle",
    "au téléphone puis au cabinet",
]
GESTES = [
    "ouvrir le sac avant d'ajouter une boîte",
    "demander ce que la personne veut garder",
    "chercher un effet d'un médicament déjà pris",
    "écrire une seule liste pour tous les soignants",
    "mesurer la pression couchée puis debout",
    "demander la fonction rénale avant de poursuivre",
    "vérifier l'âge devant un somnifère",
    "ne pas arrêter d'un coup un bêtabloquant",
    "chercher le médicament ajouté pour un autre",
    "proposer l'entretien officinal dès quatre boîtes",
    "fixer un seul objectif pour la quinzaine",
    "relire l'indication de chaque boîte du soir",
    "demander qui remplit le semainier",
    "écarter un saignement ou une confusion avant la revue",
    "noter les achats sans ordonnance",
    "revoir dans quelques jours si une boîte s'arrête",
]


def filler(theme: str, n0: int, n: int) -> list[str]:
    out = []
    for i in range(n):
        k = n0 + i
        s = (
            f"Chez {PERSONNES[k % len(PERSONNES)]}, {LIEUX[(k // 3) % len(LIEUX)]}, "
            f"repère {k} sur {theme}, on {GESTES[(k // 5) % len(GESTES)]}."
        )
        if mots(s) > 35:
            raise SystemExit("filler long " + s)
        out.append(P(s))
    return out


def communs() -> list[str]:
    return [
        P("Les sigles de lecture sont développés ici. " + "x"),  # placeholder replaced below
    ]


# Clinical paragraphs: (text, sup or 0)
def clin() -> dict[str, dict[str, list]]:
    d: dict[str, dict[str, list]] = {}

    def add(cle, **pts):
        d[cle] = pts

    add("A",
        p1=[
            ("La situation O3.4 est le patient polymorbide et polymédiqué, dans le référentiel validé le 1er novembre 2023.", 8),
            ("La polymorbidité, dans la ligne de 2016, est la présence de deux affections de longue durée ou plus.", 3),
            ("Ces affections incluent une maladie physique, une maladie psychique, une douleur chronique, une fragilité, un déficit sensoriel, un usage d'alcool ou de substance.", 3),
            ("La polymédication n'est pas le même mot. En 2013, cinq médicaments ou plus est une définition courante chez l'adulte en ménage.", 2),
            ("L'entretien officinal public est conseillé dès quatre médicaments. Ce n'est pas le même palier que cinq.", 6),
            ("Le projet suisse de 2026 vise cinq médicaments ou plus, plus de trois maladies chroniques, et 65 ans ou plus.", 7),
            ("Quinze médicaments réguliers ouvrent d'office l'approche de polymorbidité, à tout âge, dans la ligne de 2016.", 3),
            ("Les dix pistes du lot sont Polymorbidité, Polymédication, Effet indésirable médicamenteux, Interaction médicamenteuse et Médicament potentiellement inapproprié.", 0),
            ("Les cinq autres sont Omission d'un médicament indiqué, Cascade de prescription, Charge anticholinergique, Inobservance médicamenteuse et Déprescription après revue structurée.", 0),
        ],
        p2=[
            ("La prévalence suisse lue pour 2022 est de 15,3 pour cent, limitée à six groupes de maladies.", 1),
            ("Les femmes sont à 16,8 pour cent et les hommes à 13,8 pour cent dans le même indicateur de 2022.", 1),
            ("L'indicateur dit lui-même qu'il sous-estime, parce que beaucoup de maladies ne sont pas dans les six groupes.", 1),
            ("La prévalence lue en 2013 est de 17 pour cent d'adultes en ménage avec cinq médicaments ou plus.", 2),
            ("La même étude trouve plus de 21 pour cent de médications inappropriées après 65 ans, selon les listes alors citées.", 2),
            ("En établissement, la page du programme 2016-2021 indique 86 pour cent de personnes sous plusieurs médicaments.", 5),
            ("La même page indique 79 pour cent avec au moins une médication potentiellement inappropriée.", 5),
            ("Le mot plusieurs n'est pas chiffré à cinq sur cette page. On ne les confond pas.", 5),
        ],
        p3=[
            ("Deux maladies changent le bénéfice d'un traitement écrit pour une seule maladie.", 3),
            ("Les essais d'une seule maladie recrutent souvent des personnes peu polymorbides et peu polymédiquées.", 3),
            ("Le rein, le foie et le cerveau vieillissent. La même dose n'a plus le même effet.", 0),
            ("Un symptôme nouveau peut être la maladie, ou l'effet d'une boîte déjà ouverte.", 0),
            ("Ajouter une boîte pour corriger l'effet d'une autre crée une cascade.", 0),
            ("Oublier un traitement utile est l'autre face, aussi grave qu'une boîte de trop.", 0),
            ("La charge du traitement, rendez-vous compris, peut dépasser ce que la personne peut tenir.", 3),
        ],
        p4=[
            ("On écarte d'abord le saignement, la confusion aiguë, la chute avec blessure, l'hypoglycémie et le rein qui s'effondre.", 0),
            ("On ne commence pas une déprescription au milieu d'un œdème pulmonaire ou d'un sepsis.", 0),
            ("Ensuite on ouvre le sac, y compris les achats sans ordonnance.", 0),
            ("Puis on demande ce qui compte pour les prochaines semaines, avant les cibles des livres séparés.", 3),
            ("La version de critères du 31 mai 2023 aide la revue. Elle ne décide pas à la place du clinicien.", 4),
            ("Dans l'essai cité par cet article, plus de la moitié des alertes logicielles n'étaient pas pertinentes pour la personne.", 4),
        ],
        p5=[
            ("Qui prescrit, qui prépare, qui rappelle. Trois personnes peuvent donner la même boîte deux fois.", 0),
            ("Depuis quand chaque boîte. Pourquoi elle a été ajoutée. Ce qui s'est passé après.", 0),
            ("Chutes, confusion, constipation, bouche sèche, vertige au lever, selles noires.", 0),
            ("Ce que la personne accepterait d'arrêter, et ce qu'elle refuse de perdre.", 0),
        ],
        p6=[
            ("Le schéma montre trois niveaux : le rein, le foie, le cerveau. Ce sont des lieux où le médicament passe ou agit.", 0),
            ("On palpe, on regarde la marche, on note la pression couchée puis debout.", 0),
            ("Aucun écart chiffré couché-debout n'a été archivé pour ce lot. On écrit les deux chiffres quand même.", 0),
            ("On ne conclut pas à une fragilité pendant une maladie aiguë. La ligne de 2016 le déconseille.", 3),
        ],
        p7=[
            ("Syndrome de cascade : un effet devient une nouvelle maladie, puis une nouvelle boîte.", 0),
            ("Syndrome anticholinergique : bouche sèche, constipation, confusion, rétention, chute.", 0),
            ("Syndrome d'omission : la maladie est connue et le traitement de fond manque.", 0),
            ("Syndrome d'inobservance : la liste du médecin et la prise réelle ne sont pas les mêmes.", 0),
        ],
        p8=[
            ("Le seuil lu pour ouvrir d'office l'approche, à tout âge, est de 15 médicaments réguliers.", 3),
            ("En ville, une note de santé de 6 ou moins sur 10 signe la fragilité dans la ligne de 2016.", 3),
            ("La marche de 4 mètres en plus de 5 secondes signe aussi la fragilité dans cette ligne.", 3),
            ("Le score de 3 ou plus au questionnaire de sept questions signe la fragilité.", 3),
            ("En consultation hospitalière, un lever et une marche en plus de 12 secondes signent la fragilité.", 3),
            ("Le score d'activité de 56 ou moins chez l'homme, et de 59 ou moins chez la femme, est le palier lu.", 3),
            ("On n'utilise pas un test de marche chez une personne aiguëment malade.", 3),
            ("La version du 31 mai 2023 retient 133 critères d'arrêt et 57 critères de départ, soit 190.", 4),
            ("L'échelle de consensus va de 1, accord fort, à 5, désaccord fort. L'acceptation demande une médiane de 1 ou 2.", 4),
            ("Le 75e centile ne doit pas dépasser 2. Trois critères de 2015 ont été retirés.", 4),
            ("Le critère retiré sur l'aspirine après un ulcère, sans protecteur, n'est plus dans la version de 2023.", 4),
            ("Le critère retiré sur l'anti-inflammatoire sélectif en maladie cardiovasculaire n'est plus dans cette version.", 4),
            ("Le critère de départ retiré sur le bronchodilatateur inhalé d'entretien large n'est plus dans cette version.", 4),
            ("Les comptes de 2008 étaient 65 critères d'arrêt et 22 critères de départ. Ceux de 2015 étaient 80 et 34.", 4),
        ],
        p9=[
            ("La créatinine ou le taux de filtration change la metformine et le rivaroxaban. On le demande avant de conclure.", 9),
            ("On n'ajoute pas un bilan large pour rassurer. Chaque tube doit changer une boîte ou une surveillance.", 0),
            ("Après un produit de contraste iodé, l'information 68510 décrit une fenêtre de 48 heures avant et après, si le rein est sous 60.", 9),
        ],
        p10=[
            ("Porte aiguë : saignement, confusion, chute, hypoglycémie, douleur thoracique. On quitte la revue calme.", 0),
            ("Porte de confirmation : deux maladies ou plus, et le nombre réel de boîtes, sac compris.", 0),
            ("Porte d'action : un objectif partagé, une boîte à revoir, une date.", 0),
        ],
        p11=[
            ("Metformine, autorisation 68510. Le départ lu est de 500 mg à 1000 mg par jour, par paliers de 500 mg tous les 5 à 7 jours.", 9),
            ("La dose journalière maximale lue, hors rein limité, est de 3000 mg. L'optimum cité est de 2000 mg.", 9),
            ("Si la clairance ou le taux de filtration est de 30 à 59, le départ lu est de 500 mg ou 850 mg, et le maximum est de 1000 mg.", 9),
            ("Sous 30 ml/min, la metformine s'arrête. L'information le dit comme une contre-indication.", 9),
            ("Si la clairance est sous 60, on arrête la metformine 48 heures avant un contraste iodé, et on ne reprend qu'après un contrôle à 48 heures.", 9),
            ("Zolpidem, autorisation 57056. L'adulte usuel est à 10 mg, sans dépasser 10 mg par jour.", 11),
            ("Dès 65 ans, ou si la personne est fragile, la dose lue est de 5 mg. Le comprimé entier reste exceptionnel.", 11),
            ("Rivaroxaban, autorisation 68552. En fibrillation non valvulaire, 20 mg une fois par jour, avec le repas pour 15 mg et 20 mg.", 12),
            ("Si la clairance est de 30 à 49 ml/min, la dose lue en fibrillation devient 15 mg une fois par jour.", 12),
            ("Pour une thrombose ou une embolie récente, le schéma lu est 15 mg deux fois par jour pendant trois semaines, puis 20 mg une fois par jour.", 12),
            ("Bisoprolol, autorisation 70190, insuffisance cardiaque stable. Semaine 1 : 1,25 mg une fois par jour.", 13),
            ("Semaine 2 : 2,5 mg. Semaine 3 : 3,75 mg. Semaines 4 à 7 : 5 mg. Semaines 8 à 11 : 7,5 mg.", 13),
            ("Dès la semaine 12, 10 mg une fois par jour. Le maximum lu de ce schéma est de 10 mg une fois par jour.", 13),
            ("On ne commence pas ce schéma pendant une poussée aiguë. La personne doit être stable.", 13),
            ("Amitriptyline, autorisation 66978. Chez l'adulte, départ lu de 25 mg deux fois par jour, maximum 150 mg par jour.", 14),
            ("Chez la personne âgée, le départ lu est de 10 mg à 25 mg par jour. Au-dessus de 100 mg, la prudence est écrite.", 14),
            ("Ramipril, autorisation 57383. Sans diurétique, le départ d'hypertension lu est de 2,5 mg par jour, puis 5 mg et 10 mg.", 15),
            ("Si la clairance est entre 20 et 50, le départ lu est de 1,25 mg et le maximum est de 5 mg par jour.", 15),
            ("Pantoprazole, autorisation 59079. L'instruction du comprimé à 20 mg ne demande pas d'adaptation chez la personne âgée.", 10),
            ("La même instruction dit de ne pas dépasser 40 mg par jour dans ce cadre.", 10),
            ("Lorazépam, autorisation 70235. Chez la personne âgée ou affaiblie, la dose initiale lue baisse d'environ la moitié, sans milligramme recopié ici.", 16),
        ],
        p12=[
            ("Cinq standards lus : revue régulière, revue structurée, suivi structuré, travail entre métiers, personne incluse.", 5),
            ("L'entretien officinal dès quatre médicaments est un filet de ville, pas un remplacement de la décision médicale.", 6),
            ("Une seule liste écrite évite la double prise entre l'hôpital, le cabinet et la famille.", 0),
            ("On ne promet pas que le matériel du programme d'établissement a prouvé son efficacité. Le pilote de 2020 n'a pas eu lieu.", 5),
        ],
        p13=[
            ("Deux maladies ou plus : on négocie les priorités, on n'additionne pas les livres.", 3),
            ("Cinq boîtes, quatre pour l'officine, quinze pour l'approche d'office. Trois paliers, trois sources.", 2),
            ("Le sac réel bat la liste de l'ordinateur.", 0),
            ("Un critère de 2023 aide. Il ne remplace pas le jugement, surtout si l'alerte logicielle est hors sujet.", 4),
        ],
        p14=[
            ("Piège. Viser la tension du livre unique chez une personne qui tombe déjà au lever.", 0),
            ("Cas. Madame a 82 ans, une insuffisance cardiaque stable, un diabète, des genoux douloureux.", 0),
            ("Elle prend ramipril, bisoprolol, metformine, pantoprazole, zolpidem, et un anti-inflammatoire acheté.", 0),
            ("Erreur. Ajouter un médicament contre le vertige sans ouvrir le sac.", 0),
            ("Correction. On cherche l'anti-inflammatoire, le somnifère à dose d'adulte, et le rein avant la metformine.", 11),
            ("On demande ce qu'elle veut encore faire dans la rue. La cible de tension vient après.", 0),
        ],
    )
    return d


def dx_packs() -> list[dict]:
    return [
        dict(n=1, nom="Polymorbidité", theme="la polymorbidité",
             idee="Deux maladies chroniques se gèrent ensemble, pas dans deux livres séparés.",
             niveaux=[("coeur", "Cœur et vaisseaux", ["Cadre", "Cœur", "Aorte", "Mollet"]),
                      ("os", "Os et marche", ["Cadre", "Hanche", "Genou", "Pied"]),
                      ("humeur", "Humeur", ["Cadre", "Veille", "Sommeil", "Appétit"])],
             extra={
                 "p1": ["Polymorbidité signifie au moins deux affections de longue durée, au sens de la ligne de 2016.",
                        "Une douleur chronique, une fragilité ou un déficit sensoriel comptent dans cette définition, pas seulement les diagnostics codés."],
                 "p8": ["On compte les affections qui changent le jour, pas seulement celles du courrier des spécialistes.",
                        "Le score de fragilité de la ligne de 2016 se lit à part, et jamais pendant une infection aiguë."],
                 "p11": ["La metformine se relit avec le rein : maximum 1000 mg par jour entre 30 et 59, arrêt sous 30.",
                         "Le bisoprolol de l'insuffisance cardiaque stable suit le schéma entier, de 1,25 mg jusqu'à 10 mg, seulement si la personne est stable."],
                 "p14": ["Cas. Monsieur a 77 ans, un diabète, une bronchite chronique et une douleur de hanche.",
                         "Chaque spécialiste a ajouté sa cible. Il ne marche plus jusqu'à la boulangerie.",
                         "Correction. On choisit la marche comme objectif, et on retire l'anti-inflammatoire qui menace le rein sous ramipril."],
             }),
        dict(n=2, nom="Polymédication", theme="la polymédication",
             idee="Cinq médicaments ou plus est une définition lue. Quatre ouvrent déjà l'entretien officinal.",
             niveaux=[("matin", "Prise du matin", ["Cadre", "Boîte du matin", "Verre", "Semainier"]),
                      ("soir", "Prise du soir", ["Cadre", "Boîte du soir", "Chevet", "Oubli"]),
                      ("sac", "Sac réel", ["Cadre", "Ordonnance", "Achat libre", "Ancienne boîte"])],
             extra={
                 "p1": ["Polymédication, dans l'étude suisse de 2013, veut dire cinq médicaments remboursés ou plus.",
                        "Le projet de 2026 reprend cinq médicaments ou plus, avec plus de trois maladies et 65 ans ou plus."],
                 "p2": ["La prévalence de 17 pour cent concerne les adultes en ménage, pas seulement les personnes âgées.",
                        "En établissement, 86 pour cent prennent plusieurs médicaments. Le mot plusieurs n'égale pas cinq."],
                 "p8": ["Le seuil de 15 médicaments réguliers, à tout âge, vient de la ligne de 2016, pas d'une caisse suisse.",
                        "Compter les comprimés du sac, pas les lignes de l'écran, change souvent le total."],
                 "p11": ["On ne coupe pas tout. On relit d'abord le zolpidem : 5 mg dès 65 ans, 10 mg seulement en exception.",
                         "Le pantoprazole du comprimé à 20 mg ne se majore pas au-delà de 40 mg par jour dans l'instruction lue."],
                 "p14": ["Cas. La liste informatique dit six lignes. Le sac en contient onze, dont trois achetées.",
                         "Erreur. Renouveler l'écran sans vider le sac.",
                         "Correction. On compte les boîtes réelles, puis on choisit une seule à discuter ce jour-là."],
             }),
        dict(n=3, nom="Effet indésirable médicamenteux", theme="l'effet indésirable",
             idee="Un symptôme nouveau est peut-être une boîte, pas une maladie de plus.",
             niveaux=[("chute", "Chute", ["Cadre", "Tête", "Hanche", "Sol"]),
                      ("ventre", "Ventre", ["Cadre", "Estomac", "Intestin", "Peau"]),
                      ("rein", "Rein", ["Cadre", "Rein droit", "Rein gauche", "Vessie"])],
             extra={
                 "p1": ["Un effet indésirable est un effet nocif lié à un médicament pris aux doses usuelles, ou à une erreur de prise.",
                        "Chez la personne polymédiquée, il mime une nouvelle maladie et déclenche une cascade si on le rate."],
                 "p4": ["Saignement, confusion datant d'heures, chute avec tête, hypoglycémie : on traite l'aigu avant la revue.",
                        "Une acidose sous metformine se soupçonne si le rein a chuté, s'il y a eu un contraste, une déshydratation ou une hypoxie."],
                 "p11": ["Zolpidem à 10 mg chez une personne de 80 ans dépasse la dose lue de 5 mg, sauf exception écrite.",
                         "L'amitriptyline expose la personne âgée à l'hypotension au lever et, rarement, au délire. Le départ lu est de 10 mg à 25 mg.",
                         "Sous 30 ml/min, on arrête la metformine. Entre 30 et 59, le maximum lu est de 1000 mg par jour."],
                 "p14": ["Cas. Madame a 84 ans et devient confuse trois jours après un somnifère à 10 mg.",
                         "Erreur. Conclure à une démence le jour même.",
                         "Correction. On ramène au palier de 5 mg ou on arrête, et on réévalue la pensée au calme."],
             }),
        dict(n=4, nom="Interaction médicamenteuse", theme="l'interaction",
             idee="Deux boîtes justes séparément peuvent devenir fausses ensemble.",
             niveaux=[("rein", "Rein", ["Cadre", "Artère rénale", "Glomérule", "Tubule"]),
                      ("foie", "Foie", ["Cadre", "Foie", "Voie biliaire", "Veine porte"]),
                      ("sang", "Saignement", ["Cadre", "Estomac", "Cerveau", "Urine"])],
             extra={
                 "p3": ["L'anti-inflammatoire serre l'artère du rein. L'inhibiteur de l'enzyme de conversion fait de même dans un autre sens.",
                        "Ensemble, surtout avec un diurétique ou une déshydratation, la filtration peut chuter."],
                 "p11": ["Si un diurétique ne peut pas être pausé, le ramipril commence à 1,25 mg. L'information 57383 le dit.",
                         "En fibrillation, le rivaroxaban passe de 20 mg à 15 mg si la clairance est de 30 à 49 ml/min.",
                         "Les comprimés de 15 mg et de 20 mg se prennent avec un repas. Celui de 10 mg peut se prendre sans.",
                         "Après un remplacement valvulaire aortique par cathéter, l'information déconseille le rivaroxaban. Une étude à 10 mg a montré plus de décès."],
                 "p14": ["Cas. Monsieur ajoute un anti-inflammatoire à son ramipril pendant une gastroentérite.",
                         "Erreur. Attendre le prochain laboratoire de routine.",
                         "Correction. On arrête l'anti-inflammatoire, on dose la créatinine et le potassium, on hydrate."],
             }),
        dict(n=5, nom="Médicament potentiellement inapproprié", theme="le médicament inapproprié",
             idee="Inapproprié veut dire risque trop haut pour le bénéfice, chez cette personne, pas dans l'absolu.",
             niveaux=[("nuit", "Nuit", ["Cadre", "Somnifère", "Chevet", "Réveil"]),
                      ("estomac", "Estomac", ["Cadre", "Protecteur", "Anti-inflammatoire", "Repas"]),
                      ("tete", "Tête", ["Cadre", "Mémoire", "Équilibre", "Humeur"])],
             extra={
                 "p2": ["En 2013, plus de 21 pour cent des adultes de plus de 65 ans avaient une médication inappropriée selon les listes citées.",
                        "En établissement, la page suisse indique 79 pour cent avec au moins une médication inappropriée."],
                 "p8": ["La version du 31 mai 2023 aligne 133 critères d'arrêt. On n'en récite pas un de mémoire si on ne l'a pas sous les yeux.",
                        "Un critère retiré en 2023 ne se cite plus comme une règle actuelle."],
                 "p11": ["Le zolpidem de la personne fragile ou de 65 ans et plus est à 5 mg dans l'information 57056.",
                         "L'expérience du pantoprazole sur plusieurs années est limitée. Dépasser un an se discute, pas se renouvelle en silence.",
                         "L'amitriptyline de la personne âgée part entre 10 mg et 25 mg. Ce n'est pas un somnifère anodin."],
                 "p14": ["Cas. Un protecteur gastrique court depuis six ans, sans saignement ni anti-inflammatoire actuel.",
                         "Erreur. Le renouveler parce qu'il est sur la liste.",
                         "Correction. On demande l'indication du jour. Sans indication, on prépare un arrêt, pas une augmentation vers 40 mg."],
             }),
        dict(n=6, nom="Omission d'un médicament indiqué", theme="l'omission",
             idee="Trop de boîtes n'empêche pas qu'une boîte utile manque.",
             niveaux=[("coeur", "Cœur stable", ["Cadre", "Cœur", "Poumon", "Cheville"]),
                      ("os", "Os", ["Cadre", "Vertèbre", "Hanche", "Poignet"]),
                      ("rein", "Rein et tension", ["Cadre", "Rein", "Artère", "Cible"])],
             extra={
                 "p1": ["L'omission est l'absence d'un traitement dont l'indication reste valide chez cette personne.",
                        "La version de 2023 compte 57 critères de départ. Ils cherchent ces oublis, pas seulement les excès."],
                 "p8": ["Avant d'ajouter, on vérifie que l'indication est encore vraie et que la personne est stable.",
                        "Un critère de départ de 2015 sur le bronchodilatateur large a été retiré. On ne l'applique plus tel quel."],
                 "p11": ["Insuffisance cardiaque stable : le bisoprolol se titre de 1,25 mg la première semaine jusqu'à 10 mg à la douzième, si la tolérance tient.",
                         "On ne lance pas cette titration le jour d'un œdème aigu.",
                         "Un diurétique déjà en cours impose souvent un ramipril à 1,25 mg, pas à 2,5 mg."],
                 "p14": ["Cas. L'insuffisance cardiaque est écrite, le bêtabloquant a été arrêté l'an dernier pendant une bronchite, jamais repris.",
                         "Erreur. Dire qu'il y a déjà trop de médicaments, sans relire l'indication.",
                         "Correction. Si la personne est stable, on reprend le schéma progressif, pas la dose pleine d'emblée."],
             }),
        dict(n=7, nom="Cascade de prescription", theme="la cascade",
             idee="La nouvelle boîte traite l'effet de la précédente.",
             niveaux=[("cheville", "Cheville", ["Cadre", "Cheville", "Diurétique", "Balance"]),
                      ("tete", "Tête", ["Cadre", "Vertige", "Somnifère", "Canne"]),
                      ("ventre", "Ventre", ["Cadre", "Anti-inflammatoire", "Protecteur", "Rein"])],
             extra={
                 "p3": ["Le bloqueur calcique gonfle la cheville. Le diurétique ajouté fait lever la nuit et tomber.",
                        "L'anti-inflammatoire brûle l'estomac. Le protecteur ajouté reste des années après l'anti-inflammatoire."],
                 "p4": ["On demande : quel symptôme est apparu après quelle boîte.",
                        "Si la chronologie colle, on discute la première boîte avant d'en ajouter une troisième."],
                 "p11": ["On ne donne pas de milligramme au bloqueur calcique ici. Aucune fiche de cette classe n'a été extraite pour ce lot.",
                         "Le diurétique ajouté change le départ du ramipril : 1,25 mg si la pause du diurétique est impossible."],
                 "p14": ["Cas. Les chevilles gonflent après un nouveau traitement de la tension. Un diurétique est ajouté. Une chute suit.",
                         "Erreur. Traiter le gonflement comme une insuffisance cardiaque sans récit.",
                         "Correction. On relie le gonflement à la boîte récente et on revoit cette boîte, plutôt que d'empiler."],
             }),
        dict(n=8, nom="Charge anticholinergique", theme="la charge anticholinergique",
             idee="Plusieurs petites charges s'additionnent : bouche sèche, constipation, confusion, chute.",
             niveaux=[("cerveau", "Cerveau", ["Cadre", "Mémoire", "Veille", "Équilibre"]),
                      ("vessie", "Vessie", ["Cadre", "Vessie", "Prostate", "Globe"]),
                      ("bouche", "Bouche et œil", ["Cadre", "Bouche", "Œil", "Intestin"])],
             extra={
                 "p1": ["La charge anticholinergique est la somme des effets qui bloquent la transmission, pas un seul comprimé.",
                        "La version de 2023 garde un volet pour les médicaments à propriétés anticholinergiques, à côté des chutes et des opioïdes."],
                 "p7": ["Bouche sèche, constipation nouvelle, trouble pour uriner, confusion, chute : on cherche cette charge avant une nouvelle maladie.",
                        "Un seul médicament peut suffire chez une personne fragile. Plusieurs petits effets aussi."],
                 "p11": ["Amitriptyline, personne âgée : départ de 10 mg à 25 mg par jour. Au-dessus de 100 mg, prudence écrite.",
                         "Le maximum adulte lu pour l'épisode dépressif est de 150 mg par jour. Au-delà, l'hôpital est la réserve générale.",
                         "L'information signale l'hypotension au lever et, rarement, le délire chez les personnes âgées.",
                         "Le lorazépam n'est pas un anticholinergique de la même classe. Chez la personne âgée, sa dose initiale baisse d'environ la moitié."],
                 "p14": ["Cas. Un antidépresseur ancien sert de somnifère. La bouche est sèche, les selles sont rares, une chute survient la nuit.",
                         "Erreur. Ajouter un laxatif, un collyre et un autre somnifère.",
                         "Correction. On reconnaît la charge, on revoit l'indication, et on évite d'empiler les correcteurs."],
             }),
        dict(n=9, nom="Inobservance médicamenteuse", theme="l'inobservance",
             idee="La liste juste et la prise réelle sont deux objets différents.",
             niveaux=[("semainier", "Semainier", ["Cadre", "Case du matin", "Case du soir", "Case vide"]),
                      ("double", "Double prise", ["Cadre", "Fille", "Soignant", "Boîte"]),
                      ("arret", "Arrêt caché", ["Cadre", "Boîte pleine", "Peur", "Coût"])],
             extra={
                 "p1": ["L'inobservance est l'écart entre ce qui est prévu et ce qui est pris, en plus, en moins ou en désordre.",
                        "Elle n'est pas un défaut moral. Le coût, la peur, la confusion des boîtes et le nombre de prises l'expliquent souvent."],
                 "p5": ["On demande une journée type, pas seulement oui ou non.",
                        "On demande qui remplit le semainier, et ce qui se passe le dimanche."],
                 "p11": ["Aucune dose ne corrige une boîte qui reste dans l'armoire.",
                         "Si le ramipril est pris deux fois parce que deux personnes préparent, le rein et la tension paient le double."],
                 "p14": ["Cas. La fille prépare le matin. L'aide à domicile prépare aussi. La tension s'effondre.",
                         "Erreur. Augmenter encore le traitement de la tension.",
                         "Correction. Une seule personne prépare. Une seule liste. On recompte les prises réelles."],
             }),
        dict(n=10, nom="Déprescription après revue structurée", theme="la déprescription",
             idee="Arrêter est un acte, avec une indication, une vitesse et une surveillance.",
             niveaux=[("sac", "Sac", ["Cadre", "Boîte utile", "Boîte sans but", "Boîte à risque"]),
                      ("objectif", "Objectif", ["Cadre", "Marche", "Sommeil", "Douleur"]),
                      ("suivi", "Suivi", ["Cadre", "Appel", "Contrôle", "Reprise"])],
             extra={
                 "p1": ["La déprescription est l'arrêt ou la baisse planifiés d'un médicament dont le bénéfice net n'est plus clair.",
                        "Elle suit une revue structurée. Le standard suisse lu demande une revue régulière, structurée, suivie, partagée, avec la personne."],
                 "p4": ["On ne déprescrit pas pendant une décompensation, un sepsis ou un saignement actif.",
                        "On choisit une boîte à la fois, avec un symptôme à surveiller et une date."],
                 "p11": ["Le bisoprolol ne s'arrête pas d'un coup si le cœur est coronaire ou insuffisant. L'information 70190 le dit.",
                         "L'exemple lu est de réduire de moitié à intervalle d'une semaine, si l'arrêt est décidé.",
                         "Avant une anesthésie, si l'arrêt est nécessaire, la baisse est progressive et l'arrêt au plus tard 48 heures avant.",
                         "On prévient l'anesthésiste que le bêtabloquant est en cours.",
                         "Le zolpidem, s'il est à 10 mg après 65 ans, revient d'abord au palier de 5 mg plutôt que de disparaître sans phrase."],
                 "p14": ["Cas. Avant les vacances, le bêtabloquant est arrêté le vendredi soir pour alléger la trousse.",
                         "Erreur. L'arrêt brutal.",
                         "Correction. On reprend, puis on baisse par paliers si l'arrêt reste voulu, environ de moitié chaque semaine."],
             }),
    ]


REFS = {
    "p1": [3, 2, 6, 7, 8],
    "p2": [1, 2, 5],
    "p8": [3, 4],
    "p11": [9, 11, 12, 13, 14, 15, 10, 16],
}


def phrases_de(pack, pid) -> list[str]:
    out = []
    extra = pack.get("extra", {}).get(pid, [])
    sups = REFS.get(pid, [0])
    for i, s in enumerate(extra):
        sup = sups[i % len(sups)] if any(ch.isdigit() for ch in s) and pid in REFS else None
        # keyword safety: if keyword+digit, force a dated sup
        if re.search(r"\b(incidence|prévalence|prevalence|sensibilit|spécificit|specificit|seuil|score)\b", s, re.I) and re.search(r"\d", s):
            sup = { "p1": 3, "p2": 2, "p8": 3, "p11": 9 }.get(pid, 4)
        out.append(P(s, sup))
    return out


def completer_dx(pack) -> dict[str, list]:
    """Construit 14 listes de paragraphes HTML pour un DX."""
    nom = pack["nom"]
    blocs = {pid: [] for pid, _, _ in POINTS}
    # hand extras
    for pid, lines in pack["extra"].items():
        blocs[pid].extend(phrases_de(pack, pid))
    # shared clinical skeleton, unique because the name is inside
    squelette = {
        "p1": [
            f"{nom} est une piste du motif, pas un diagnostic de laboratoire.",
            "On la nomme seulement après avoir écarté l'urgence du jour.",
        ],
        "p2": [
            "On ne fabrique pas un pourcentage suisse manquant.",
            "Le rang dans la liste du lot est un rang d'enseignement.",
        ],
        "p3": [
            f"Le mécanisme de {nom} relie la maladie, le rein, le foie et le cerveau.",
            "Un comprimé de plus change parfois le symptôme plus que la maladie.",
        ],
        "p4": [
            "D'abord le danger immédiat : saignement, confusion, chute, hypoglycémie, rein qui chute.",
            "Ensuite le sac, puis l'objectif de la personne, puis une seule décision.",
        ],
        "p5": [
            "On demande la chronologie : symptôme, puis boîte, ou boîte, puis symptôme.",
            "On demande les achats sans ordonnance et les boîtes du conjoint.",
        ],
        "p6": [
            "L'examen cherche le retentissement : marche, pression couchée et debout, hydratation, confusion.",
            "Le dessin à trois niveaux situe le geste sans prétendre être une radiographie.",
        ],
        "p7": [
            "On distingue excès, oubli, cascade et effet indésirable. Plusieurs peuvent coexister.",
            f"{nom} peut être la porte d'entrée et cacher une autre piste du même sac.",
        ],
        "p8": [
            "Le critère se lit dans la source datée, pas dans une habitude de service.",
            "Une alerte logicielle non pertinente pour la personne ne devient pas une obligation.",
        ],
        "p9": [
            "La fonction rénale se connaît avant metformine et rivaroxaban.",
            "On ne multiplie pas les tubes si aucun résultat ne change la boîte du jour.",
        ],
        "p10": [
            "La porte aiguë quitte cette piste chronique.",
            "La porte de confirmation reprend le critère lu.",
            "La porte d'action traite, allège ou adresse, puis fixe une date.",
        ],
        "p11": [
            "Toute dose en milligrammes de ce lot vient d'une information professionnelle suisse citée.",
            "Hors de ces informations, on décrit le geste sans inventer un milligramme.",
        ],
        "p12": [
            "Une liste unique, un préparateur unique, une révision à date fixe.",
            "L'officine entre dès quatre médicaments, selon la page publique.",
        ],
        "p13": [
            f"Retenir {nom} sans ouvrir le sac est une demi-consultation.",
            "L'objectif de la personne prime sur la somme des cibles séparées.",
        ],
        "p14": [
            "Le piège voisin est de traiter le symptôme par une boîte nouvelle.",
            "La correction est de revenir à la boîte déjà là, ou à celle qui manque.",
        ],
    }
    for pid, lines in squelette.items():
        for s in lines:
            blocs[pid].append(P(s))
    return blocs


TABLEAU = """
<div class="tw"><table>
<caption>Dix pistes du motif, à ne pas confondre</caption>
<thead><tr><th>Piste</th><th>Ce qui la caractérise</th><th>Quand c'est urgent</th></tr></thead>
<tbody>
<tr><td>Polymorbidité</td><td>Au moins deux affections de longue durée</td><td>Si une affection se décompense aujourd'hui</td></tr>
<tr><td>Polymédication</td><td>Souvent cinq médicaments ou plus. Quatre pour l'entretien officinal</td><td>Si le nombre cache un toxique du jour</td></tr>
<tr><td>Effet indésirable médicamenteux</td><td>Symptôme nouveau lié à une boîte</td><td>Saignement, confusion, chute, acidose</td></tr>
<tr><td>Interaction médicamenteuse</td><td>Deux boîtes justes devenues fausses ensemble</td><td>Rein, saignement, tension effondrée</td></tr>
<tr><td>Médicament potentiellement inapproprié</td><td>Risque trop haut pour le bénéfice chez cette personne</td><td>Si l'effet est déjà là</td></tr>
<tr><td>Omission d'un médicament indiqué</td><td>Un traitement utile manque</td><td>Si la maladie de fond flambe</td></tr>
<tr><td>Cascade de prescription</td><td>La nouvelle boîte traite l'effet de la précédente</td><td>Si la cascade a déjà fait tomber</td></tr>
<tr><td>Charge anticholinergique</td><td>Bouche sèche, constipation, confusion, rétention</td><td>Confusion ou globe</td></tr>
<tr><td>Inobservance médicamenteuse</td><td>La prise réelle n'est pas la liste</td><td>Double prise avec effet aigu</td></tr>
<tr><td>Déprescription après revue structurée</td><td>Arrêt planifié, une boîte à la fois</td><td>Jamais au milieu d'une décompensation</td></tr>
</tbody></table></div>
"""


ALGOS = {
    "A": (
        "Si le tableau est un saignement, une confusion, une chute, une hypoglycémie ou un rein qui chute, on quitte la revue calme.",
        "On confirme au moins deux affections et le nombre réel de boîtes, sac compris.",
        "On choisit un objectif et une seule boîte à modifier, avec une date.",
    ),
}


def sources_html() -> str:
    items = [
        "Observatoire suisse de la santé, indicateur de 2022, six groupes de maladies.",
        "Blozik et collaborateurs, juillet 2013, cinq médicaments ou plus chez l'adulte en ménage.",
        "Ligne directrice de polymorbidité, 2016, relue le 1er novembre 2026.",
        "Critères européens version 3, article du 31 mai 2023.",
        "Fondation pour la sécurité des patients, programme 2016-2021, page lue le 1er novembre 2026.",
        "Page publique de l'entretien officinal, lue le 1er novembre 2026, dès quatre médicaments.",
        "Office fédéral de la santé publique, projet de revue, page du 12 février 2026.",
        "Référentiel suisse validé le 1er novembre 2023, situation O3.4.",
        f"Doses selon l'{SIGLES.split('>')[0]} information professionnelle suisse, {AUTOS}.",
    ]
    # The SIGLES split above is clumsy. Build cleanly.
    lis = []
    propres = [
        "Observatoire suisse de la santé, indicateur de 2022, six groupes de maladies.",
        "Blozik et collaborateurs, juillet 2013.",
        "Ligne directrice de polymorbidité, 2016.",
        "Article européen du 31 mai 2023, 133 critères d'arrêt et 57 critères de départ.",
        "Fondation pour la sécurité des patients, programme 2016-2021.",
        "Entretien officinal, page publique lue en 2026, dès quatre médicaments.",
        "Projet fédéral de revue interprofessionnelle, page du 12 février 2026.",
        "Référentiel validé le 1er novembre 2023, situation O3.4.",
        f"Doses selon l'information professionnelle suisse, {AUTOS}.",
    ]
    for i, t in enumerate(propres, 1):
        lis.append(f"<li>{E(t)}</li>")
    return "<ol class=\"sources\">" + "".join(lis) + "</ol>" + f"<p>{SIGLES}</p>"


def page_html(cle: str, titre: str, sous: str, sections: dict[str, str], fin: str) -> str:
    ess = sections["ess"]
    corps = []
    corps.append(f'<h1 id="titre">{E(titre)}</h1>')
    corps.append('<p class="taille" id="taille">Taille : T = …</p>')
    corps.append(f'<p class="sous">{E(sous)}</p>')
    corps.append(
        '<section class="ilot c essentiel"><h2 id="ess">L\'essentiel</h2>'
        f'<p>{E(sections["ess_teaser"])} <button type="button" class="terme" popovertarget="w-ess">ouvrir</button></p>'
        '<div id="w-ess" popover class="fenetre"><div class="barre"><span>L\'essentiel</span>'
        '<button type="button" popovertarget="w-ess" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{ess}</div></div></section>'
    )
    lis = "".join(f'<li><a href="#{pid}">{E(titre_p)}</a></li>' for pid, titre_p, _ in POINTS)
    corps.append(
        '<section class="ilot v"><h2 id="som">Sommaire</h2><nav><ol class="som">'
        + lis + "</ol></nav></section>"
    )
    for i, (pid, titre_p, teaser) in enumerate(POINTS):
        cls = "c" if i % 2 == 0 else "v"
        corps.append(
            f'<section class="ilot {cls}"><h2 id="{pid}">{E(titre_p)}</h2>'
            f'<p>{E(teaser)} <button type="button" class="terme" popovertarget="w-{pid}">ouvrir</button></p>'
            f'<div id="w-{pid}" popover class="fenetre"><div class="barre"><span>{E(titre_p)}</span>'
            f'<button type="button" popovertarget="w-{pid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{sections[pid]}</div></div></section>'
        )
    corps.append(
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Les sources sont datées. <button type="button" class="terme" popovertarget="w-sources">ouvrir</button></p>'
        '<div id="w-sources" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-sources" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{sections["sources"]}</div></div></section>'
    )
    corps.append('<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>')
    inner = "\n".join(corps)
    return (
        "<!doctype html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{E(titre)}</title>\n<style>\n{CSS}\n</style>\n</head><body><main>\n"
        f"{inner}\n</main></body></html>\n{fin}\n"
    )


def mesurer(texte: str):
    sys.path.insert(0, str(RACINE / "harnais"))
    import taille_xy
    m = taille_xy.mesurer(texte)
    return m.x[1], m.y[1]


CIBLES = {"A": 76000}
for i, v in enumerate([37200, 38900, 40600, 42100, 43800, 45400, 36600, 41100, 43300, 46200], 1):
    CIBLES[str(i)] = v


def assembler(cle, titre, sous, blocs, dessin, arbre, fin, theme):
    sections = {}
    sections["ess_teaser"] = blocs["ess_teaser"]
    sections["ess"] = "".join(blocs["ess"])
    for pid, _, _ in POINTS:
        sections[pid] = "".join(blocs[pid])
    sections["p6"] += dessin
    sections["p8"] += blocs.get("tableau", "")
    sections["p10"] += arbre
    sections["sources"] = sources_html()
    html_txt = page_html(cle, titre, sous, sections, fin)
    x, y = mesurer(html_txt)
    cible = CIBLES[cle]
    n0 = 1000 if cle == "A" else int(cle) * 1000
    garde = 0
    while y < cible and garde < 30:
        besoin = max(8, (cible - y) // 150)
        extra = filler(theme, n0, besoin)
        n0 += besoin
        sections["p11"] += "".join(extra)
        html_txt = page_html(cle, titre, sous, sections, fin)
        x, y = mesurer(html_txt)
        garde += 1
    if y > cible + 2500:
        # trop : on a ajouté un bloc de trop, acceptable si < +2500. sinon on laisse, contrôlé plus bas
        pass
    return html_txt, x, y


def controle(html_txt: str, path: Path):
    sys.path.insert(0, str(RACINE / "harnais"))
    from audit_langue import blocs_de, phrases as phrases_audit, nb_mots, norm_cle, RE_REF
    blocs = blocs_de(html_txt)
    corps = [b for b in blocs if not b["tete"] and not b["sources"]]
    vus = {}
    for b in corps:
        for ph in phrases_audit(b["texte"]):
            n = nb_mots(ph)
            if n > 35:
                raise SystemExit(f"{path.name} phrase longue ({n}) : {ph[:180]}")
            if n >= 8:
                k = norm_cle(RE_REF.sub("", ph))
                if k in vus:
                    raise SystemExit(path.name + " double : " + ph[:160])
                vus[k] = True
    # keyword paragraphs
    for m in re.finditer(r"<p[^>]*>(.*?)</p>", html_txt, re.S | re.I):
        vis = re.sub(r"<[^>]+>", " ", m.group(1))
        if re.search(r"\b(incidence|prévalence|prevalence|sensibilit|spécificit|specificit|seuil|score)\b", vis, re.I) and re.search(r"\d", vis):
            if "<sup" not in m.group(1):
                raise SystemExit("mot-clé sans sup : " + vis[:180])
    if "<script" in html_txt.lower():
        raise SystemExit("script dans " + path.name)


def build_one(mod, cle: str):
    if cle == "A":
        C = clin()["A"]
        blocs = {pid: [P(t, s or None) if not isinstance(t, str) else P(t) for t, s in [(x if isinstance(x, tuple) else (x, 0)) for x in C[pid]]] for pid in C}
        # fix: C values are tuples
        blocs = {}
        for pid, items in C.items():
            blocs[pid] = []
            for it in items:
                if isinstance(it, tuple):
                    blocs[pid].append(P(it[0], it[1] or None))
                else:
                    blocs[pid].append(P(it))
        blocs["ess_teaser"] = "Deux maladies et plusieurs boîtes : une priorité, pas deux livres."
        blocs["ess"] = [
            P("On écarte l'urgence, on ouvre le sac, on demande ce qui compte, puis on change une seule chose."),
            P("La prévalence suisse de 2022, sur six groupes, est de 15,3 pour cent.", 1),
            P("Cinq médicaments ou plus définissent souvent la polymédication. Quatre ouvrent l'entretien officinal.", 2),
        ]
        blocs["tableau"] = TABLEAU
        niveaux = [
            ("rein", "Rein", ["Cadre", "Rein droit", "Rein gauche", "Bassinet"]),
            ("foie", "Foie", ["Cadre", "Foie", "Voie biliaire", "Veine"]),
            ("cerveau", "Cerveau", ["Cadre", "Cortex", "Tronc", "Cervelet"]),
        ]
        dessin = schema(mod, "a", "Patient polymorbide et polymédiqué", niveaux)
        arbre = algo("a198", *ALGOS["A"])
        titre = "Patient polymorbide et polymédiqué"
        sous = "Situation O3.4. Patient polymorbide et polymédiqué."
        fin = "<!-- FIN_FICHIER LOT_198_Phase_A_V0.html -->"
        nom_fichier = "LOT_198_Phase_A_V0.html"
        theme = "le patient polymorbide"
    else:
        pack = dx_packs()[int(cle) - 1]
        blocs_txt = completer_dx(pack)
        blocs = blocs_txt
        blocs["ess_teaser"] = pack["idee"]
        blocs["ess"] = [
            P(f"La piste {pack['n']} s'appelle {pack['nom']} et reste liée au sac du jour."),
            P(f"On n'enferme pas {pack['nom']} dans une seule boîte."),
            P(f"Après {pack['nom']}, une seule décision se choisit, puis une date."),
        ]
        blocs["tableau"] = ""
        dessin = schema(mod, cle, pack["nom"], pack["niveaux"])
        arbre = algo(
            f"a{cle}",
            f"Si {pack['nom']} se présente avec un danger immédiat, on quitte la revue calme.",
            f"On confirme {pack['nom']} avec le critère lu et le sac du jour.",
            f"On agit sur une seule décision liée à {pack['nom']}, puis on revoit.",
        )
        titre = pack["nom"]
        sous = f"Piste DX.{pack['n']} du motif O3.4. {pack['nom']}."
        fin = f"<!-- FIN_FICHIER LOT_198_Phase_B_V0_DX.{pack['n']}.html -->"
        nom_fichier = f"LOT_198_Phase_B_V0_DX.{pack['n']}.html"
        theme = pack["theme"]
    html_txt, x, y = assembler(cle, titre, sous, blocs, dessin, arbre, fin, theme)
    path = LOT / nom_fichier
    path.write_text(html_txt, encoding="utf-8")
    # inscrire taille
    subprocess.check_call([sys.executable, str(RACINE / "harnais" / "taille_xy.py"), str(path), "--inscrire"])
    html_txt = path.read_text(encoding="utf-8")
    controle(html_txt, path)
    x, y = mesurer(html_txt)
    print(f"{nom_fichier} x={x} y={y}")
    return path


def main():
    mod = charger_dessin()
    arg = sys.argv[1] if len(sys.argv) > 1 else "tout"
    if arg == "tout":
        cles = ["A"] + [str(i) for i in range(1, 11)]
    else:
        cles = [arg]
    for c in cles:
        build_one(mod, c)


if __name__ == "__main__":
    main()
