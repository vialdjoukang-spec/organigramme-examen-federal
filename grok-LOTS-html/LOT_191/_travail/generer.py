#!/usr/bin/env python3
"""LOT_191 O2.9 — nourrisson irritable ou qui pleure. Générateur V8, zéro script dans la leçon."""
from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_191"
EV = LOT / "evidence"
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

MOTS = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit|spécificit|specificit|seuil|score)\b",
    re.I,
)

DXS = [
    (1, "Coliques du nourrisson"),
    (2, "Reflux gastro-œsophagien du nourrisson"),
    (3, "Allergie aux protéines du lait de vache"),
    (4, "Infection aiguë du nourrisson"),
    (5, "Invagination intestinale"),
    (6, "Occlusion digestive chirurgicale du nourrisson"),
    (7, "Lésion douloureuse locale du nourrisson"),
    (8, "Maltraitance du nourrisson"),
    (9, "Glaucome congénital et détresse circulatoire"),
    (10, "Hypoglycémie et erreur innée du métabolisme"),
]
TITRES = {n: t for n, t in DXS}
ORDRE_E = [
    "Infection aiguë du nourrisson",
    "Occlusion digestive chirurgicale du nourrisson",
    "Invagination intestinale",
    "Maltraitance du nourrisson",
    "Glaucome congénital et détresse circulatoire",
    "Hypoglycémie et erreur innée du métabolisme",
    "Lésion douloureuse locale du nourrisson",
    "Allergie aux protéines du lait de vache",
    "Reflux gastro-œsophagien du nourrisson",
    "Coliques du nourrisson",
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
"""

SOURCES = [
    "Benninga et collaborateurs. Troubles fonctionnels du nourrisson. Gastroenterology, 2016. Critères cliniques des coliques.",
    "Zeevenhooven J et collaborateurs. Critères de Rome IV du nourrisson. Pediatric Gastroenterology, Hepatology and Nutrition, 2017.",
    "Hôpitaux universitaires de Genève. Brochure La santé de votre enfant, chapitre des pleurs, page lue le 1 novembre 2026.",
    "Groupe francophone d'hépatologie-gastroentérologie et nutrition pédiatriques. Fiche coliques, document de septembre 2018, relu le 1 novembre 2026.",
    "Rosen R et collaborateurs. Reflux gastro-œsophagien de l'enfant. Journal of Pediatric Gastroenterology and Nutrition, 2018.",
    "Vandenplas Y et collaborateurs. Allergie aux protéines du lait de vache. Journal of Pediatric Gastroenterology and Nutrition, 2024.",
    "Groupe britannique de radiologie pédiatrique. Guide de l'invagination, document du 18 août 2017, relu le 1 novembre 2026.",
    "Pierce et collaborateurs. Règle des ecchymoses. Revue médicale en accès libre, 2021.",
    "Lips U, Wopmann M. Maltraitance infantile. pédiatrie suisse, 15 octobre 2021.",
    "Code civil suisse, articles 314c et 314d, en vigueur le 1er janvier 2019.",
    "Information professionnelle, Dafalgan enfant sirop, autorisation 43838, corpus du 8 octobre 2026.",
    "Information professionnelle, Algifor Dolo Junior, autorisation 58834, corpus du 8 octobre 2026.",
    "Information professionnelle, Nexium granulés, autorisation 58091, corpus du 8 octobre 2026.",
    "Société suisse de néonatologie. Hypoglycémie dès 35 semaines en maternité, texte 2020 publié le 6 avril 2021.",
    "Société européenne du glaucome. Glaucome congénital, 4e édition, British Journal of Ophthalmology, 2017, et 5e édition, juillet 2021.",
    "Information professionnelle, Rocephin, autorisation 44625, corpus du 8 octobre 2026.",
]


def ecrire_preuves() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    textes = {
        "01_rome_2016.txt": """Lu le 1 novembre 2026.
Benninga MA et al. Childhood Functional Gastrointestinal Disorders: Neonate/Toddler. Gastroenterology. 2016.
URL https://www.gastrojournal.org/article/S0016-5085(16)00182-7/fulltext
Année 2016.

Critères cliniques G4 des coliques, tous requis.
Un nourrisson de moins de 5 mois quand les symptômes commencent et s'arrêtent.
Périodes récurrentes et prolongées de pleurs, d'agitation ou d'irritabilité, sans cause évidente, que les proches ne peuvent ni prévenir ni faire cesser.
Pas de cassure de croissance, pas de fièvre, pas de maladie.

La recherche ajoute un récit d'au moins 3 heures par jour sur au moins 3 jours d'une semaine, et un agenda de 24 heures qui confirme au moins 3 heures.
Le texte dit qu'aucune preuve ne sépare un nourrisson qui pleure plus de 3 heures d'un nourrisson qui pleure 2 heures et 50 minutes.
Le pic moyen des pleurs se situe vers 4 à 6 semaines et diminue vers 12 semaines.
La plupart des cas représentent le haut de la courbe normale des pleurs. Le texte dit qu'il n'y a pas de preuve que ces pleurs viennent d'une douleur abdominale.
""",
        "02_zeevenhooven_2017.txt": """Lu le 1 novembre 2026.
Zeevenhooven J, Koppen IJ, Benninga MA. The New Rome IV Criteria for Functional Gastrointestinal Disorders in Infants and Toddlers.
Pediatric Gastroenterology, Hepatology and Nutrition. 2017. doi 10.5223/pghn.2017.20.1.1
Année 2017.

Rome IV retire la règle de Wessel du critère clinique.
La règle des trois heures est jugée arbitraire, dépendante de la culture, et peu pratique sur sept jours d'agenda.
Le caractère prolongé et impossible à calmer pèse plus, pour les proches, que la seule durée.
""",
        "03_hug_pleurs_2026.txt": """Lu le 1 novembre 2026.
Hôpitaux universitaires de Genève. La santé de votre enfant. Conseils pour les parents.
URL https://enfants-ados.hug.ch/sites/hde/files/documents/la_sante_de_votre_enfant.pdf
Page des pleurs consultée le 1 novembre 2026. Année de consultation 2026.

Un bébé en bonne santé peut pleurer jusqu'à 2 à 3 heures par jour, souvent en fin de journée ou le soir.
Durant les premiers mois, un bébé ne fait pas de caprice.
On peut le coucher sur le dos, dans la pénombre, et revenir toutes les 10 à 15 minutes.
Ne jamais secouer. La tête fait alors un mouvement violent d'avant en arrière, qui peut être mortel ou endommager gravement le cerveau.
Installer l'enfant dans son lit, quitter la pièce, appeler une personne de confiance.
Consulter en urgence si le teint est bleu-gris, si l'enfant est mou comme une poupée de chiffon, s'il est trop faible pour crier, s'il hurle au toucher, s'il pleure en continu et reste inconsolable même dans les bras, s'il est difficile à réveiller, ou s'il regarde dans le vide.
""",
        "04_gfhgnp_coliques_2018.txt": """Lu le 1 novembre 2026.
Groupe francophone d'hépatologie-gastroentérologie et nutrition pédiatriques. Fiche recommandations coliques du nourrisson.
URL https://www.gfhgnp.org/wp-content/uploads/2025/04/5-sept-18Fiche-recommandations-COLIQUE.pdf
Le nom de fichier porte septembre 2018. Relecture le 1 novembre 2026.

La règle des trois est dite caduque pour la pratique clinique.
Les trois critères cliniques repris sont l'âge de moins de 5 mois, les périodes prolongées sans cause évitable, et l'absence de maladie chez un nourrisson eutrophe.
La fiche estime l'incidence des coliques entre 20 et 25 pour cent dans les pays industrialisés.
Elle demande un examen complet avant de rassurer, et déconseille les changements répétés de lait et les traitements non validés.
""",
        "05_gerd_2018.txt": """Lu le 1 novembre 2026.
Rosen R et al. Pediatric Gastroesophageal Reflux Clinical Practice Guidelines. NASPGHAN et ESPGHAN.
Journal of Pediatric Gastroenterology and Nutrition. 2018. doi 10.1097/MPG.0000000000001889
Année 2018.

Le reflux devient une maladie quand les symptômes sont gênants ou qu'une complication existe.
Chez le nourrisson qui ne parle pas, dire qu'un symptôme est gênant est difficile.
Les pleurs excessifs, l'arc-boutement, les régurgitations et l'irritabilité sont décrits, mais existent aussi sans maladie de reflux.
Sans signe d'alarme, et sans retentissement sur l'alimentation, la croissance ou les acquisitions, le guide dit de ne pas lancer d'examen ni de frein d'acide.
Six études chez des nourrissons de moins de 12 mois n'ont pas montré de différence sur les pleurs ou l'irritabilité avec un inhibiteur de la pompe à protons.
La recommandation 5.5 déconseille l'anti-H2 et l'inhibiteur pour une régurgitation visible chez un nourrisson par ailleurs sain.
La recommandation 3.13 déconseille l'essai d'inhibiteur comme test diagnostique chez le nourrisson.
Signes d'alarme lus dans le tableau 2 : perte de poids, léthargie, fièvre, irritabilité excessive, dysurie, début des régurgitations après 6 mois ou persistance au-delà de 12 à 18 mois, fontanelle bombée ou périmètre qui augmente vite, convulsions, vomissements en jet et répétés jusqu'à 2 mois, vomissements nocturnes, vomissements bilieux, hématémèse, diarrhée chronique, sang rectal, distension abdominale.
Le vomissement bilieux est lu comme un signe d'occlusion, avec volvulus sur malrotation ou invagination parmi les causes.
Le syndrome de Sandifer est nommé comme posture dystonique du cou.
""",
        "06_aplv_2024.txt": """Lu le 1 novembre 2026.
Vandenplas Y et al. An ESPGHAN Position Paper on the Diagnosis, Management, and Prevention of Cow's Milk Allergy.
Journal of Pediatric Gastroenterology and Nutrition. 2024. doi 10.1097/MPG.0000000000003897
Recherche Medline jusqu'en mai 2022. Année 2024.

Les pleurs et l'irritabilité concernent environ 20 pour cent des nourrissons, et l'allergie au lait en est rarement la cause.
Pour des pleurs et une irritabilité seuls, le texte dit que les données sont insuffisantes pour recommander une éviction de 2 à 4 semaines suivie d'une réintroduction.
Si les coliques remplissent les critères de recherche de Rome IV et que d'autres symptômes font suspecter l'allergie, une éviction limitée de 2 à 4 semaines peut être tentée, suivie d'une épreuve de réintroduction.
L'allergie existe chez le nourrisson allaité exclusivement, mais elle est peu fréquente et trop souvent affirmée.
Le diagnostic repose sur l'épreuve après une éviction courte, pas sur la seule amélioration.
L'outil de vigilance lié au lait ne pose pas le diagnostic.
Les selles vertes ou glaireuses, chez un nourrisson par ailleurs sain, ne doivent pas être prises pour une allergie.
Une proctocolite minime du nourrisson allaité, sans autre signe d'atopie, peut être observée sans régime pendant le premier mois de sang dans les selles.
Le recouvrement attendu entre allergie au lait et reflux est décrit comme inférieur à 1 pour cent.
Le soja n'est pas recommandé pour les coliques dans le passage lu.
""",
        "07_invagination_2017.txt": """Lu le 1 novembre 2026.
A UK evidence based guideline for the acute management of paediatric intussusception.
BSPR Intussusception Working Group. Document daté du 18 août 2017.
URL https://www.bspr.co.uk/wp-content/uploads/2024/01/2017.08.18-Intussusception-Guideline-Final-Draft.pdf
Année 2017.

L'invagination est lue comme la cause unique la plus fréquente d'urgence chirurgicale abdominale du nourrisson.
Elle est idiopathique dans 90 pour cent des cas, avec un pic de 6 à 18 mois.
L'échographie est l'examen de première intention.
Le texte décrit une sensibilité presque de 100 pour cent et une spécificité de 80 à 100 pour cent.
Le signe de la cible, ou du beignet, en coupe transversale, et le pseudo-rein en coupe longitudinale, sont lus comme diagnostiques.
Le lavement à l'air est la technique de réduction non opératoire retenue par ce guide britannique.
Une perforation suspectée, une nécrose ou un échec du lavement mènent à la chirurgie.
Un liquide piégé ou un Doppler pauvre baisse le taux de réduction, sans interdire à eux seuls la tentative si l'enfant est stable et sans perforation.
Le texte cite des taux de réduction rapportés de 26 pour cent et de 31 pour cent dans ces situations, et un taux national d'audit de 71 pour cent, ainsi qu'un taux de 61 pour cent dans une étude de 2012.
""",
        "08_ten4_2021.txt": """Lu le 1 novembre 2026. Reprise de la lecture déjà archivée pour le LOT_185, texte rouvert pour ce LOT.
Pierce MC et al. JAMA Network Open. 2021.
2161 enfants de moins de 4,0 ans avec ecchymose.
Sensibilité 95,6 pour cent. Spécificité 87,1 pour cent.
La règle ne s'applique qu'aux enfants de moins de 4 ans qui ont une ecchymose.
Toute ecchymose, où qu'elle soit, chez un nourrisson de 4,99 mois ou moins, entre dans la règle.
Régions lues : tronc, oreille, cou, frein, angle de la mâchoire, joues charnues, paupières, conjonctives, et dessin d'un objet ou d'une prise.
Une composante positive impose une évaluation supplémentaire. Elle ne fait pas le diagnostic à elle seule.
Dans cet échantillon d'urgences, 19 pour cent ont été classés maltraitance.
""",
        "09_lips_2021.txt": """Lu le 1 novembre 2026. Article suisse rouvert.
Ulrich Lips, Markus Wopmann. Maltraitance infantile, protection de l'enfant. pédiatrie suisse, 15 octobre 2021.
URL https://www.paediatrieschweiz.ch/fr/maltraitance-infantile-protection-de-lenfant/
Année 2021.
En 2020, 21 cliniques ont enregistré 1590 cas. Mauvais traitements physiques 37 pour cent. Négligence 27 pour cent.
S'il existe un danger aigu, la protection immédiate est la mesure la plus urgente.
Les déclarations spontanées se consignent tout de suite, mot à mot.
Ne pas tenir compte d'un mauvais traitement est une faute médicale, au même titre que rater une méningite.
Le principe jamais seul est écrit.
""",
        "10_code_civil_2019.txt": """Lu le 1 novembre 2026.
Code civil suisse, articles 314c et 314d, en vigueur le 1er janvier 2019.
Année 2019.
L'article 314c donne à toute personne le droit d'aviser l'autorité de protection de l'enfant.
Les personnes tenues au secret professionnel ont aussi ce droit quand l'intérêt de l'enfant le justifie.
L'article 314d crée une obligation pour d'autres personnes, mais le médecin tenu au secret de l'article 321 du code pénal n'est pas visé par cette obligation fédérale.
Les cantons peuvent prévoir d'autres obligations.
""",
        "14_hypoglycemie_2021.txt": """Lu le 1 novembre 2026.
Société suisse de néonatologie. Prévention et traitement de l'hypoglycémie néonatale à la maternité, dès 35 semaines et 0 jour.
Texte 2020. Publication pédiatrie suisse, Schulzke et collaborateurs, 6 avril 2021.
URL https://www.paediatrieschweiz.ch/fr/prevention-traitement-hypoglycemie-neonatale-maternite/
Année 2021.
Le texte ne s'applique pas aux prématurés de moins de 35 semaines ni aux nouveau-nés malades admis en soins intermédiaires ou intensifs.
Indépendamment de la méthode de mesure, une valeur inférieure à 2,6 mmol/l est définie comme une hypoglycémie chez un nouveau-né d'au moins 35 semaines et 0 jour, et elle requiert une intervention.
Le texte recommande de ne pas adopter un seuil de 2,0 mmol/l.
La glycémie moyenne lue au plateau précoce est 3,3 mmol/l, écart-type 0,6.
Au quatrième jour, la moyenne lue est 4,6 mmol/l, écart-type 0,7.
Plus d'un tiers des nouveau-nés à terme et sains ont au moins une valeur sous 2,6 mmol/l le premier jour, surtout dans les 12 premières heures.
""",
        "15_glaucome_2017_2021.txt": """Lu le 1 novembre 2026.
European Glaucoma Society. Terminology and Guidelines for Glaucoma. 4e édition, chapitre du glaucome congénital.
British Journal of Ophthalmology. 2017. PMC 5583685.
5e édition, British Journal of Ophthalmology, publiée le 1 juin 2021, impression juillet 2021.
Années 2017 et 2021.

Signes précoces lus en 2017 : photophobie, larmoiement, blépharospasme, et frottement des yeux.
Un enfant qui pleure et semble malheureux dans les premières semaines ou la première année peut être le mode d'arrivée. Ce n'est pas constant.
Diamètre cornéen habituellement supérieur à 10,5 mm à la naissance et supérieur à 12 mm dans la première année.
Longueur axiale supérieure à 20 mm à la naissance ou supérieure à 22 mm après 1 an.
Fréquence lue d'environ 1 naissance sur 12 000 à 18 000 chez les personnes d'ascendance européenne, plus élevée si les parents sont apparentés.
Atteinte bilatérale dans 70 pour cent des cas. Plus fréquente chez les garçons, 65 pour cent.
La pression sous anesthésie est souvent abaissée par les médicaments. Une pression seule ne confirme pas, sauf si elle est extrêmement élevée et accompagnée de signes cornéens.
La 5e édition de 2021 indique une chirurgie initiale dans presque tous les cas de glaucome congénital primaire.
Le traitement médicamenteux est lu comme un pont, pas comme le traitement de fond.
""",
    }
    for nom, corps in textes.items():
        (EV / nom).write_text(corps.strip() + "\n", encoding="utf-8")
    lignes = ["# Preuves lues — LOT_191 — 1 novembre 2026", ""]
    for i, s in enumerate(SOURCES, 1):
        lignes.append(f"{i}. {s}")
    lignes.append("")
    (EV / "INDEX.md").write_text("\n".join(lignes), encoding="utf-8")


def mots(s: str) -> int:
    return len(re.findall(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*", re.sub(r"<[^>]+>", " ", s)))


def phrase(s: str, src: int | None = None) -> str:
    s = " ".join(s.split())
    if not s.endswith("."):
        s += "."
    if mots(s) > 32:
        raise SystemExit("phrase trop longue : " + s)
    if MOTS.search(s) and re.search(r"\d", s):
        if src is None:
            raise SystemExit("chiffre-clé sans source : " + s)
        s = s[:-1] + f'.<sup class="s">{src}</sup>'
    elif src and "<sup" not in s:
        s = s[:-1] + f'.<sup class="s">{src}</sup>'
    return s


def P(*lignes: str, src: int | None = None) -> list[str]:
    return [phrase(x, src) for x in lignes if x.strip()]


# Noyaux cliniques. Chaque liste est déjà une phrase complète courte.
NOYAUX: dict[str, dict[int, list[str]]] = {}

NOYAUX["A"] = {
    1: P(
        "Le motif est un nourrisson irritable ou qui pleure, pas un diagnostic unique.",
        "On sépare les pleurs habituels du premier trimestre d'un pleur qui a changé, qui dure, ou qui s'accompagne d'un signe malade.",
        "Les coliques cliniques de 2016 exigent un âge de moins de 5 mois, des périodes prolongées impossibles à calmer, et l'absence de fièvre, de maladie et de cassure de croissance.",
        "La règle des trois heures n'est plus exigée pour nommer les coliques en clinique.",
        "Elle reste un critère de recherche, avec un agenda.",
        src=1,
    ),
    2: P(
        "La fiche francophone de 2018 situe la fréquence des coliques entre 20 et 25 pour cent dans les pays industrialisés.",
        "Le texte européen de 2024 situe les pleurs et l'irritabilité autour de 20 pour cent des nourrissons.",
        "L'allergie au lait en est rarement la cause.",
        "Aucune incidence suisse unique ne classe les dix diagnostics de ce motif.",
        "L'ordre des fichiers suit la fréquence habituelle du motif. L'ordre E suit le danger à écarter.",
        src=4,
    ),
    3: P(
        "Le pic des pleurs sains se situe vers 4 à 6 semaines et diminue vers 12 semaines.",
        "Le texte de 2016 dit qu'il n'y a pas de preuve que ces pleurs viennent d'une douleur du ventre.",
        "Une infection, une occlusion, une ecchymose ou une cornée trouble ont un autre mécanisme.",
        "Le canal artériel qui se ferme peut révéler une cardiopathie, sous forme de pâleur, de fatigue alimentaire et d'irritabilité.",
        "Le jour exact de cette fermeture n'est pas fixé par une source archivée ici.",
        src=1,
    ),
    4: P(
        "La première minute juge la couleur, le tonus, la respiration et la chaleur des extrémités.",
        "On déshabille tout le corps, y compris les doigts, les orteils et les plis.",
        "On pèse et on compare à la courbe précédente.",
        "On prend la température.",
        "Un enfant gris, mou, ou impossible à réveiller sort de la filière des coliques.",
        src=3,
    ),
    5: P(
        "On demande depuis quand les pleurs ont changé, et s'ils cessent dans les bras.",
        "On demande la fièvre, les vomissements, la couleur des selles et des urines, et un traumatisme.",
        "Un vomissement vert est un signe d'occlusion dans le guide de 2018.",
        "Une fontanelle bombée ou un périmètre qui grossit vite font chercher une hypertension intracrânienne.",
        "Des ecchymoses chez un nourrisson de moins de 5 mois ne se rangent pas dans un jeu.",
        src=5,
    ),
    6: P(
        "L'examen regarde les yeux, les oreilles, la bouche, le cou, le cœur, les pouls fémoraux, le ventre, les orifices herniaires, les organes génitaux, la peau et chaque doigt.",
        "On cherche un fil serré autour d'un orteil, d'un doigt ou du pénis.",
        "On cherche une cornée grande ou trouble, une photophobie et un larmoiement.",
        "On palpe les fontanelles et on mesure le périmètre si la tête inquiète.",
        "Un ventre distendu, silencieux ou défenseux n'est pas une colique.",
        src=15,
    ),
    7: P(
        "Le groupe fièvre et tonus bas oriente vers l'infection.",
        "Le groupe vomissement vert ou ventre aigu oriente vers le chirurgien.",
        "Le groupe sang dans les selles et douleurs par vagues oriente vers l'invagination.",
        "Le groupe ecchymose, récit changeant ou retard de recours oriente vers la protection.",
        "Le groupe régurgitations chez un enfant qui grossit bien reste souvent un reflux simple.",
        src=5,
    ),
    8: P(
        "On ne pose les coliques qu'après avoir écarté la fièvre, la cassure staturale et la maladie.",
        "On ne pose pas l'allergie au lait sur les seuls pleurs.",
        "On ne pose pas une maladie de reflux sur des pleurs sans retentissement.",
        "Le diagnostic positif d'une urgence est celui du signe qui menace, pas celui du motif d'entrée.",
        "Les dix noms restent écrits dans le compte rendu tant que l'examen n'a pas tranché.",
    ),
    9: P(
        "Sans signe d'alarme, le guide de 2018 ne demande ni endoscopie ni frein d'acide pour des pleurs.",
        "L'échographie est l'examen de première intention si l'invagination est plausible.",
        "Une glycémie est lue avec le texte suisse de 2021 seulement dans son champ, le nouveau-né d'au moins 35 semaines en maternité.",
        "Une analyse d'urine se discute devant une fièvre sans foyer.",
        "On n'attend pas un examen pour commencer les gestes vitaux.",
        src=5,
    ),
    10: P(
        "Le schéma interactif sépare trois temps : les fonctions vitales, les signes qui interdisent de rassurer, puis les critères des coliques.",
        "On change de panneau selon ce qui est vu, pas selon l'habitude du service.",
        "Un panneau vert ne s'ouvre pas si la couleur, le tonus ou le ventre sont anormaux.",
        "Le retour à la maison suppose un examen complet et des parents capables de revenir.",
        "Le numéro des urgences et la consigne de ne jamais secouer sont dits à voix haute.",
        src=3,
    ),
    11: P(
        "La douleur et la fièvre, quand elles existent, peuvent relever du paracétamol selon l'information professionnelle suisse.",
        "Dafalgan enfant, autorisation 43838, écrit une dose unique de 15 mg de paracétamol par kilogramme.",
        "Le maximum quotidien lu est 75 mg par kilogramme. L'intervalle lu est de 6 à 8 heures.",
        "Sans avis médical, la durée continue maximale chez l'enfant jusqu'à 12 ans est de 3 jours.",
        "Algifor Dolo Junior, autorisation 58834, est contre-indiqué avant 6 mois et avant 5 kg.",
        "Nexium, autorisation 58091, ne doit pas être utilisé avant 1 an ni avant 10 kg.",
        "Rocephin, autorisation 44625, plafonne le nouveau-né jusqu'à 14 jours à 50 mg par kilogramme.",
        src=11,
    ),
    12: P(
        "On montre comment coucher l'enfant sur le dos et quitter la pièce si la colère monte.",
        "On dit de ne jamais secouer.",
        "On évite les changements de lait en série sans hypothèse écrite.",
        "On vérifie que les autres produits ne contiennent pas aussi du paracétamol.",
        "La prévention de la maltraitance passe par le relais humain, pas par un médicament des pleurs.",
        src=3,
    ),
    13: P(
        "Moins de cinq mois, pleurs impossibles à calmer, enfant sain : ce trio vient de 2016.",
        "Vingt à vingt-cinq pour cent est la fourchette francophone de 2018, pas un taux suisse.",
        "Vingt pour cent de pleurs, allergie rarement en cause : c'est le texte de 2024.",
        "Pas d'inhibiteur pour une régurgitation chez un nourrisson sain : recommandation de 2018.",
        "Toute ecchymose avant 4,99 mois entre dans la règle de 2021.",
        "Sous 2,6 mmol/l en maternité, dès 35 semaines : texte suisse de 2021.",
        src=1,
    ),
    14: P(
        "Le piège est de nommer des coliques chez un enfant fiévreux ou qui ne grossit plus.",
        "Le piège est de multiplier les laits et les inhibiteurs d'acide.",
        "Le piège est de laisser un fil autour d'un orteil.",
        "Le piège est de rassurer devant un vomissement vert.",
        "Cas corrigé. Un nourrisson de six semaines pleure chaque soir et tète bien. L'examen nu est normal, la courbe monte, il n'a pas de fièvre.",
        "On retient les critères cliniques de 2016. On ne prescrit pas Nexium. On explique le pic des semaines et l'interdiction de secouer.",
        "Le soir suivant, un vomissement vert apparaît. Le dossier change de catégorie et appelle le chirurgien.",
        src=1,
    ),
}

NOYAUX[1] = {
    1: P(
        "Les coliques du nourrisson sont un trouble fonctionnel, pas une douleur d'organe prouvée.",
        "En clinique, les trois critères de 2016 sont exigés ensemble.",
        "L'âge est de moins de 5 mois au début et à la fin des symptômes.",
        "Les proches décrivent des périodes répétées et longues, sans cause claire, qu'ils ne parviennent pas à empêcher ni à arrêter.",
        "Il n'y a ni cassure de croissance, ni fièvre, ni maladie.",
        "Le mot agitation désigne un état qui n'est ni le sommeil calme ni le cri franc.",
        src=1,
    ),
    2: P(
        "La fiche de 2018 estime une fréquence de 20 à 25 pour cent dans les pays industrialisés.",
        "Le pic moyen lu en 2016 se place vers 4 à 6 semaines.",
        "La décroissance habituelle va vers 12 semaines.",
        "Chez l'ancien prématuré, le texte compte 3 à 4 mois après le terme.",
        "La brochure genevoise dit qu'un bébé sain peut pleurer jusqu'à 2 à 3 heures par jour.",
        "Ce chiffre de brochure n'est pas le critère diagnostique.",
        src=4,
    ),
    3: P(
        "Le comité de 2016 écrit qu'il n'y a pas de preuve d'une douleur abdominale à l'origine de ces pleurs.",
        "Les proches interprètent souvent le cri comme un mal de ventre, ce qui mène aux consultations de gastroentérologie.",
        "La durée du cri explique moins la détresse parentale que le fait de ne pas pouvoir consoler.",
        "Deux heures et cinquante minutes ne définissent pas un autre enfant que trois heures.",
        "Le mécanisme retenu pour le cours est celui d'une variante du développement, tant que l'examen est normal.",
        src=1,
    ),
    4: P(
        "On date le début, l'heure habituelle et ce qui calme ou non.",
        "On vérifie l'alimentation, les selles, la fièvre et la courbe.",
        "On examine nu avant de prononcer le mot colique.",
        "On écrit les trois critères, et celui qui manque.",
        "Si un critère manque, on ne ferme pas le dossier sur ce nom.",
        src=1,
    ),
    5: P(
        "Une fièvre sort du cadre.",
        "Une cassure de poids sort du cadre.",
        "Un vomissement vert sort du cadre.",
        "Un sang rouge dans les selles sort du cadre des coliques simples.",
        "Un récit de secousse, une ecchymose ou un retard de recours sortent du cadre.",
        src=5,
    ),
    6: P(
        "L'enfant des coliques a un tonus normal entre les crises et un contact possible.",
        "Le ventre peut être tendu par les cris et les gaz, puis souple.",
        "On ne confond pas cette tension avec une défense.",
        "Les orteils, les doigts et le pénis sont inspectés un par un.",
        "Les yeux ne sont ni photophobes ni troubles.",
        src=3,
    ),
    7: P(
        "Le soir, les poings fermés et les genoux remontés sont classiques et non spécifiques.",
        "Le même tableau avec fièvre devient une infection jusqu'à preuve du contraire.",
        "Le même tableau avec vomissement vert devient chirurgical.",
        "Le même tableau avec sang et pâleur par à-coups fait chercher l'invagination, surtout plus tard.",
        "Le même tableau chez un enfant qui ne grossit plus fait revoir l'allergie et la maladie.",
        src=5,
    ),
    8: P(
        "Le diagnostic clinique est positif quand les trois critères sont écrits et que l'examen nu est rassurant.",
        "Le critère de recherche, lui, demande en plus au moins 3 heures par jour sur au moins 3 jours, et un agenda.",
        "On ne mélange pas les deux usages dans la même phrase du dossier.",
        "L'amélioration le lendemain ne prouve pas la cause.",
        "On revoit tôt si un signe nouveau apparaît.",
        src=1,
    ),
    9: P(
        "Aucun examen n'est exigé par les critères de 2016 quand l'enfant est sain.",
        "Une échographie, une prise de sang ou un changement de lait ne font pas partie du socle.",
        "On les ajoute seulement si un signe d'alarme a été trouvé.",
        "Un agenda d'une journée aide la recherche, pas la décision du soir aux urgences.",
        "On note l'heure de la pesée et le carnet.",
        src=1,
    ),
    10: P(
        "Le premier panneau du schéma rappelle l'âge de moins de 5 mois.",
        "Le deuxième panneau liste ce qui interdit le diagnostic.",
        "Le troisième panneau dit ce qu'on explique aux parents.",
        "On ne coche pas le panneau des coliques si la fièvre est là.",
        "On revient au panneau d'alarme si le cri change de nature.",
        src=1,
    ),
    11: P(
        "Le traitement est l'explication, le portage, le calme et le relais humain.",
        "La brochure genevoise propose de coucher sur le dos et de revenir toutes les 10 à 15 minutes.",
        "On ne traite pas les coliques par un inhibiteur d'acide.",
        "Nexium, autorisation 58091, n'a pas de dose avant 1 an ni avant 10 kg.",
        "Le paracétamol n'est pas le traitement des coliques. S'il existe une autre douleur, Dafalgan enfant, autorisation 43838, donne 15 mg par kilogramme, sans dépasser 75 mg par kilogramme et par jour.",
        "On ne change pas de lait à chaque consultation.",
        src=3,
    ),
    12: P(
        "On prévient la secousse en le disant clairement.",
        "On propose un relais la nuit.",
        "On fixe une date de revue avant la sortie.",
        "On explique que le pic régresse vers 12 semaines chez l'enfant né à terme.",
        "On demande aux parents ce qu'ils feraient si le cri devenait faible ou si un vomissement vert survenait.",
        src=1,
    ),
    13: P(
        "Trois critères cliniques, pas la règle des trois heures.",
        "Enfant eutrophe, sans fièvre, sans maladie.",
        "Pic vers 4 à 6 semaines, décroissance vers 12 semaines.",
        "Pas de preuve lue d'une douleur de ventre.",
        "Pas d'inhibiteur, pas de secousse, pas de lait changé en série.",
        src=1,
    ),
    14: P(
        "Piège : appeler colique un enfant de 7 mois. L'âge dépasse le critère.",
        "Piège : rassurer au téléphone sans savoir si l'enfant a été vu nu.",
        "Piège : conclure parce que les parents sont fatigués, sans examiner les orteils.",
        "Cas corrigé. À cinq semaines, les pleurs du soir durent, la prise de poids est régulière, la température est normale, l'examen nu est normal.",
        "On nomme les coliques selon 2016. On écrit l'interdiction de secouer. On revoit si un signe d'alarme arrive.",
        "On n'ajoute pas Nexium. On n'ajoute pas un hydrolysat sans autre symptôme.",
        src=1,
    ),
}
