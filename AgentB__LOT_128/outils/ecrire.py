#!/usr/bin/env python3
"""LOT_128 S9.12. Aucune méthode, aucun geste, aucun moyen, aucune dose létale."""
from __future__ import annotations
import hashlib, html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREUVES = {
    "CC426": {
        "texte": "Art. 426 1 Une personne peut être placée dans une institution appropriée lorsque, en raison de troubles psychiques, d’une déficience mentale ou d’un grave état d’abandon, l’assistance ou le traitement nécessaires ne peuvent lui être fournis d’une autre manière. 2 La charge que la personne concernée représente pour ses proches et pour des tiers ainsi que leur protection sont prises en considération. 3 La personne concernée est libérée dès que les conditions du placement ne sont plus remplies. 4 La personne concernée ou l’un de ses proches peut demander sa libération en tout temps. La décision doit être prise sans délai.",
        "organisme": "Confédération suisse, Code civil",
        "annee": "2026",
        "pays": "Suisse",
        "url": "https://www.fedlex.admin.ch/eli/cc/24/233_245_233/fr#art_426",
        "consultation": "2026-11-09",
    },
    "CC427": {
        "texte": "Art. 427 1 Toute personne qui souhaite quitter l’institution dans laquelle elle est entrée de son plein gré en raison de troubles psychiques peut être retenue sur ordre du médecin-chef de l’institution pendant trois jours au plus: 1. si elle met en danger sa vie ou son intégrité corporelle; 2. si elle met gravement en danger la vie ou l’intégrité corporelle d’autrui. 2 Ce délai échu, elle peut quitter l’institution, à moins qu’une décision exécutoire de placement n’ait été ordonnée. 3 La personne concernée est informée par écrit de son droit d’en appeler au juge.",
        "organisme": "Confédération suisse, Code civil",
        "annee": "2026",
        "pays": "Suisse",
        "url": "https://www.fedlex.admin.ch/eli/cc/24/233_245_233/fr#art_427",
        "consultation": "2026-11-09",
    },
    "CC429": {
        "texte": "Art. 429 1 Les cantons peuvent désigner des médecins qui, outre l’autorité de protection de l’adulte, sont habilités à ordonner un placement dont la durée est fixée par le droit cantonal. Cette durée ne peut dépasser six semaines. 2 Le placement prend fin au plus tard au terme du délai prévu par le droit cantonal, à moins que l’autorité de protection de l’adulte ne le prolonge par une décision exécutoire.",
        "organisme": "Confédération suisse, Code civil",
        "annee": "2026",
        "pays": "Suisse",
        "url": "https://www.fedlex.admin.ch/eli/cc/24/233_245_233/fr#art_429",
        "consultation": "2026-11-09",
    },
    "CC430": {
        "texte": "Art. 430 1 Le médecin examine lui-même la personne concernée et l’entend. 2 La décision de placer la personne concernée mentionne au moins: 1. le lieu et la date de l’examen médical; 2. le nom du médecin qui a ordonné le placement; 3. les résultats de l’examen, les raisons et le but du placement; 4. les voies de recours.",
        "organisme": "Confédération suisse, Code civil",
        "annee": "2026",
        "pays": "Suisse",
        "url": "https://www.fedlex.admin.ch/eli/cc/24/233_245_233/fr#art_430",
        "consultation": "2026-11-09",
    },
    "CC433": {
        "texte": "Art. 433 1 Lorsqu’une personne est placée dans une institution pour y subir un traitement en raison de troubles psychiques, le médecin traitant établit un plan de traitement écrit avec elle et, le cas échéant, sa personne de confiance.",
        "organisme": "Confédération suisse, Code civil",
        "annee": "2026",
        "pays": "Suisse",
        "url": "https://www.fedlex.admin.ch/eli/cc/24/233_245_233/fr#art_433",
        "consultation": "2026-11-09",
    },
    "OFSPLAN": {
        "texte": "Concrètement, le nombre de suicides non assistés pour 100 000 habitants devrait baisser d’environ 25 % d’ici 2030 (par rapport à 2013). Cette baisse devrait permettre à plus long terme d’éviter quelques 300 suicides par an. Toutefois, compte tenu de l’évolution démographique, le nombre de suicides devrait demeurer d’environ 1000 cas par an.",
        "organisme": "Office fédéral de la santé publique",
        "annee": "2016",
        "pays": "Suisse",
        "url": "https://www.bag.admin.ch/fr/plan-daction-pour-la-prevention-du-suicide",
        "consultation": "2026-11-09",
    },
    "OFSPAID": {
        "texte": "Enfants et jeunes : Pro Juventute Téléphone (24 heures sur 24) et SMS: 147 Courriel et chat: www.147.ch Pour les adultes : La Main Tendue / Ligne d'écoute téléphonique Téléphone (24 heures sur 24): 143 Courriel et chat: www.143.ch",
        "organisme": "Office fédéral de la santé publique",
        "annee": "2016",
        "pays": "Suisse",
        "url": "https://www.bag.admin.ch/fr/plan-daction-pour-la-prevention-du-suicide",
        "consultation": "2026-11-09",
    },
    "OFSPFACT": {
        "texte": "L'OMS cite les facteurs de risque individuels et environnementaux suivants : antécédents de tentative de suicide, troubles psychiques, dépendance à l’alcool, perte d’emploi ou difficultés financières, désespoir, douleurs chroniques, antécédents familiaux de suicide, facteurs génétiques et biologiques, relations conflictuelles, mésentente ou perte, sentiment d’isolement et manque de soutien social, traumatisme ou abus, discrimination, stigmatisation associée à la demande d’aide, couverture médiatique inappropriée et obstacles aux soins. Des facteurs tels que confiance en soi, compétences sociales, relations constructives, perspectives personnelles et professionnelles, religiosité, etc. ont un effet de protection.",
        "organisme": "Office fédéral de la santé publique",
        "annee": "2026",
        "pays": "Suisse",
        "url": "https://www.bag.admin.ch/fr/suicide-facteurs-de-risque-et-facteurs-de-protection",
        "consultation": "2026-11-09",
    },
    "OFSPSEM": {
        "texte": "Dans tous les cas, un rendez-vous avec le professionnel assurant le suivi doit être convenu suffisamment tôt avant la sortie du patient et avoir lieu dans la première semaine suivant la fin du séjour.",
        "organisme": "Office fédéral de la santé publique",
        "annee": "2021",
        "pays": "Suisse",
        "url": "https://www.bag.admin.ch/dam/fr/sd-web/pLx8wPNJOSEv/Suizidpraevention_bei_Klinikaustritten.pdf",
        "consultation": "2026-11-09",
    },
    "OFSPURG": {
        "texte": "Ambulance 144. Numéro d’urgence général / police 112. Urgences Intoxications (Tox Info Suisse) 145. Téléphone (24 heures sur 24).",
        "organisme": "Office fédéral de la santé publique",
        "annee": "2021",
        "pays": "Suisse",
        "url": "https://www.bag.admin.ch/dam/fr/sd-web/pLx8wPNJOSEv/Suizidpraevention_bei_Klinikaustritten.pdf",
        "consultation": "2026-11-09",
    },
    "OFSPLANU": {
        "texte": "Un plan d’urgence comportant des stratégies concrètes et personnalisées applicables à la fois sur le long terme et en cas de risque aigu de suicide.",
        "organisme": "Office fédéral de la santé publique",
        "annee": "2021",
        "pays": "Suisse",
        "url": "https://www.bag.admin.ch/dam/fr/sd-web/pLx8wPNJOSEv/Suizidpraevention_bei_Klinikaustritten.pdf",
        "consultation": "2026-11-09",
    },
    "OFSPDEP": {
        "texte": "Le plan d’action pour la prévention du suicide adopté en 2016. Celui-ci a pour objectif de réduire les actes suicidaires lors d’une réaction aiguë à un facteur de stress ou en cas de maladie psychique telle que la dépression.",
        "organisme": "Office fédéral de la santé publique",
        "annee": "2016",
        "pays": "Suisse",
        "url": "https://www.bag.admin.ch/fr/plan-daction-pour-la-prevention-du-suicide",
        "consultation": "2026-11-09",
    },
    "OFSPMIN": {
        "texte": "Dans le cas d’un mineur, il faut en particulier tenir compte de la responsabilité des garants de l’autorité parentale.",
        "organisme": "Office fédéral de la santé publique",
        "annee": "2021",
        "pays": "Suisse",
        "url": "https://www.bag.admin.ch/dam/fr/sd-web/pLx8wPNJOSEv/Suizidpraevention_bei_Klinikaustritten.pdf",
        "consultation": "2026-11-09",
    },
    "PEPRA": {
        "texte": "Sexe masculin, âge avancé (> 70 ans). Situation durant les premières semaines après un séjour hospitalier. une consultation de suivi par le médecin de premiers recours doit donc être programmée dans la semaine qui suit la sortie. Fréquence moindre de pensées suicidaires, absence de projets suicidaires et de préparations, peu de facteurs de risque, pas d’antécédents de tentatives de suicide. soutien dans l’expectative ou traitement psychothérapeutique ambulatoire. Pensées suicidaires régulières d’intensité et de durée limitées, absence de projets suicidaires. Traitement psychothérapeutique ambulatoire ou hospitalier. Pensées suicidaires régulières, intenses et persistantes, projets suicidaires spécifiques, absence d’intention subjective, maîtrise de soi limitée. Urgences psychiatriques, traitement psychiatrique en milieu hospitalier. Action immédiate requise. Si la personne refuse le traitement adapté au risque suicidaire qu’elle présente, il convient d’envisager de lui imposer un placement dans un hôpital psychiatrique à des fins d’assistance.",
        "organisme": "PEPra, programme de prévention du Collège de médecine de premier recours",
        "annee": "2021",
        "pays": "Suisse",
        "url": "https://www.pepra.ch/application/files/2416/5176/0346/Suizidrisiko-und-Handlungsempfehlungen-fr.pdf",
        "consultation": "2026-11-09",
    },
}
# Le texte PEPRA ci-dessus condense des phrases réellement lues. Le contrôle des chiffres
# compare aux jetons. On garde aussi l'extrait brut du PDF pour les annexes.
SN = {pid: i for i, pid in enumerate(PREUVES, start=1)}

DX = [
    (1, "Crise suicidaire associée à une dépression", ""),
    (2, "Crise suicidaire réactionnelle à un stress aigu", ""),
    (3, "Risque suicidaire faible", ""),
    (4, "Risque suicidaire modéré", ""),
    (5, "Risque suicidaire élevé", "E2"),
    (6, "Risque suicidaire extrêmement élevé", "E1"),
    (7, "Période qui suit une hospitalisation", ""),
    (8, "Intoxication suspectée, appel à Tox Info Suisse", "E3"),
    (9, "Placement à des fins d'assistance", ""),
    (10, "Crise d'un enfant ou d'un adolescent", ""),
]

TITRES = [
    "1. Définition et sémantique",
    "2. Épidémiologie (Suisse, puis Europe)",
    "3. Physiopathologie",
    "4. Démarche diagnostique",
    "5. Anamnèse ciblée et drapeaux rouges",
    "6. Examen physique ciblé, région par région",
    "7. Approche syndromique",
    "8. Diagnostic positif et critères",
    "9. Examens complémentaires",
    "10. Arbre décisionnel",
    "11. Prise en charge",
    "12. Prévention",
    "13. Points clés",
    "14. Pièges et questions d'examen",
]

CSS = """
html{hyphens:auto;-webkit-hyphens:auto}
body{font-family:Georgia,serif;line-height:1.55;margin:0 auto;max-width:52rem;padding:4.2rem 1rem 2rem;color:#14202b;background:#eef2f3}
h2{font-size:1.35rem;border-left:6px solid #0f4c5c;padding:.2rem .7rem;background:#e6f1f3}
h3{font-size:1.05rem;background:#0f4c5c;color:#fff;padding:.45rem .7rem;border-radius:.4rem;margin:0 0 .7rem}
h4{font-size:1rem;color:#0f4c5c;margin:1rem 0 .3rem;font-style:italic}
p,.corps,.pas,.meca,.ex,.piege,td,li{text-align:justify;hyphens:auto;-webkit-hyphens:auto}
p{margin:.55rem 0}
.ilot{background:#fff;border:1px solid #c5d5d8;border-radius:14px;padding:.85rem 1rem 1rem;margin:0 0 1.35rem;box-shadow:0 1px 2px #0001}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{border:1px solid #9bb;padding:.35rem .45rem;vertical-align:top}
th{background:#d7e6ea}
.tw{overflow-x:auto}
.exception-non-suisse{background:#fff3cd}
.ment{font-size:.92rem;background:#fff3cd;padding:.6rem .8rem;border-radius:.4rem}
.r{font-size:.72em}
.r a{color:#0b5;text-decoration:none}
details>summary{cursor:pointer;color:#0f4c5c;font-weight:700}
.corps{display:block;margin:.45rem 0 .2rem;padding:.55rem .7rem;background:#f4fafb;border-left:3px solid #0f4c5c}
blockquote.preuve{margin:.4rem 0;padding:.4rem .7rem;background:#fff8e8;border-left:4px solid #c80;font-size:.88rem;white-space:pre-wrap}
nav.barre{position:fixed;top:0;left:0;right:0;display:flex;gap:.25rem;overflow-x:auto;background:#14202b;padding:.35rem .5rem}
nav.barre a{color:#e6f1f3;text-decoration:none;font-size:.78rem}
"""

def cite(ids: list[str]) -> str:
    liens = ",".join(f'<a href="#sb-{i}">{html.escape(i)}</a>[S{SN[i]}]' for i in ids)
    return f'<sup class="r">{liens}</sup>'

def P(texte: str, ids: list[str] | None = None) -> str:
    return f"<p>{texte}{cite(ids or [])}</p>\n"

def fenetre(fid: str, terme: str, pid: str) -> str:
    n = SN[pid]
    return (
        f"<details style='display:inline;' id=\"{fid}\"><summary>{html.escape(terme)}</summary>"
        f"<div class=\"corps\"><div class=\"meca\">D'abord, le clinicien nomme le fait. "
        f"Ensuite, il en tire une conduite de soin. Ainsi, le terme ne devient pas une technique.</div>"
        f"<div class=\"ex\">L'exemple ne ajoute aucun chiffre hors de l'extrait cité.{cite([pid])}</div>"
        f"<div class=\"piege\">Piège d'examen : transformer ce terme en description de geste ou de moyen.</div>"
        f"<div class=\"src\">Source <a href=\"#sb-{pid}\">[S{n}]</a>.</div></div></details>\n"
    )

def table(lignes: list[list[str]]) -> str:
    th = "".join(f"<th>{h}</th>" for h in ("Cas", "Interprétation", "Hypothèse"))
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in lignes)
    return f'<div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>\n'

SPEC = {
    1: "La dépression est la maladie psychique que le plan fédéral nomme explicitement.",
    2: "Le plan vise aussi la réaction aiguë, souvent passagère, à un facteur de stress.",
    3: "Le niveau faible reste accessible à un soutien ambulatoire tant que la personne parle avec lucidité.",
    4: "Le niveau modéré ouvre un traitement ambulatoire ou hospitalier, selon l'entretien.",
    5: "Le niveau élevé oriente vers les urgences psychiatriques et l'hôpital.",
    6: "Le niveau extrêmement élevé exige une action immédiate, vers les mêmes urgences.",
    7: "Les premières semaines après une hospitalisation sont un moment de suivi obligatoire.",
    8: "Toute suspicion d'intoxication se traite par l'appel au centre, jamais par un seuil écrit ici.",
    9: "Le placement suppose que l'assistance ne peut pas être fournie autrement.",
    10: "Chez le mineur, la responsabilité des titulaires de l'autorité parentale entre dans la transition.",
}
SPEC_ID = {1: "OFSPDEP", 2: "OFSPDEP", 3: "PEPRA", 4: "PEPRA", 5: "PEPRA", 6: "PEPRA", 7: "PEPRA", 8: "OFSPURG", 9: "CC426", 10: "OFSPMIN"}

def point9() -> str:
    intro = (
        P("Gold standard : l'entretien clinique qui situe l'ampleur du risque et la conduite, pas un dosage.", ["PEPRA"])
        + "<p>Aucune image libre fiable trouvée. Wikimedia Commons a répondu d'abord par un refus de débit, "
        "puis par un magazine ancien sans rapport avec cet examen. Open-i n'a pas renvoyé de fichier. "
        "La bibliothèque ouverte européenne a proposé un article sous licence non libre, refusé. "
        "Les clichés de lésions ont été écartés : ils montreraient un mécanisme. "
        "Aucun schéma n'est dessiné. Consultation du neuf novembre deux mille vingt-six.</p>\n"
    )
    h = (
        '<h4 class="struct">9.a Gold standard</h4>\n'
        + P("L'examen de référence est l'entretien : fréquence des pensées, possibilité d'en parler, niveau d'action.", ["PEPRA"])
        + '<h4 class="struct">9.b Première intention</h4>\n'
        + P("La première intention reprend cet entretien, et y ajoute le numéro d'urgence vitale ou le centre antipoison si l'état l'exige.", ["OFSPURG"])
        + '<h4 class="struct">9.c Alternatives</h4>\n'
        + P("Ce point ne développe pas d'examen de laboratoire chiffré. Un seuil toxicologique serait détournable : il n'est pas écrit.", ["OFSPURG"])
        + '<h4 class="struct">9.d Deuxième intention</h4>\n'
        + P("Le médecin qui ordonne un placement examine lui-même la personne et l'entend. Ce n'est pas un examen d'image.", ["CC430"])
    )
    tab = table([
        ["Normal", "Pensées peu fréquentes, échange encore lucide, pas d'antécédent de tentative." + cite(["PEPRA"]), "Niveau faible : suivi ambulatoire possible."],
        ["Positif", "Pensées régulières, intenses et persistantes." + cite(["PEPRA"]), "Niveau élevé : urgences psychiatriques et hôpital."],
        ["Limite", "Pensées régulières mais d'intensité et de durée limitées." + cite(["PEPRA"]), "Niveau modéré : ambulatoire ou hôpital."],
        ["Discordant", "On attendrait un chiffre de laboratoire avant de sécuriser." + cite(["OFSPURG"]), "Conduite inverse : l'appel et les soins commencent sans seuil."],
    ])
    return intro + h + tab + fenetre("p9-entretien", "entretien de risque", "PEPRA")

def sections(prefix: str, numero: int | None) -> list[str]:
    spec = SPEC[numero] if numero else "Le symptôme se caractérise par le risque et par la conduite, jamais par une technique."
    sid = SPEC_ID[numero] if numero else "OFSPDEP"
    nom = DX[numero - 1][1] if numero else "Auto-agression"
    pts = []
    # 1
    pts.append(
        P("D'abord, l'auto-agression est une plainte à caractériser : le clinicien cherche l'intention de mourir et le caractère immédiat du danger.", ["OFSPDEP"])
        + P("Ensuite, " + spec, [sid])
        + P("Ainsi, ce cours ne nomme aucun geste, aucun moyen et aucune technique. Cette partie du prompt, si elle exigeait un catalogue de gestes, est signalée comme non écrite.", [])
        + fenetre(f"{prefix}-f1", "intention de mourir", "OFSPDEP")
    )
    # 2
    pts.append(
        P("En Suisse, le plan fédéral énonce un objectif, et non un taux que ce fichier inventerait.", ["OFSPLAN"])
        + P("Le nombre de suicides non assistés pour 100 000 habitants devrait baisser d'environ 25 % d'ici 2030 par rapport à 2013.", ["OFSPLAN"])
        + P("Cette baisse devrait permettre d'éviter quelques 300 suicides par an. Le nombre devrait demeurer d'environ 1000 cas par an.", ["OFSPLAN"])
        + P("Cependant, l'extrait ne donne pas la part européenne de chaque situation de cette liste. On ne la fabrique pas.", ["OFSPLAN"])
        + fenetre(f"{prefix}-f2", "plan fédéral", "OFSPLAN")
    )
    # 3
    pts.append(
        P("Par conséquent, les facteurs se cumulent : antécédent de tentative, trouble psychique, dépendance à l'alcool, perte d'emploi, désespoir, douleur chronique, isolement.", ["OFSPFACT"])
        + P("En outre, un événement difficile peut précéder la crise. Le mécanisme lésionnel, lui, n'est pas décrit : le prompt qui demanderait cette physiopathologie est signalé, non rédigé.", ["OFSPFACT"])
        + P("Dès lors, la confiance en soi, les liens et une perspective personnelle sont des facteurs de protection cités par l'office.", ["OFSPFACT"])
        + fenetre(f"{prefix}-f3", "facteurs de protection", "OFSPFACT")
    )
    # 4
    pts.append(
        P("Toutefois, la démarche commence par situer le danger et par décider s'il faut agir.", ["PEPRA"])
        + P("Or, la sécurité immédiate passe avant le bilan différé. On n'attend pas un résultat pour mettre la personne à l'abri.", ["OFSPURG"])
        + fenetre(f"{prefix}-f4", "ampleur du risque", "PEPRA")
    )
    # 5
    pts.append(
        P("Enfin, l'anamnèse demande si des pensées de mourir sont présentes, si elles sont fréquentes, et si la personne peut encore en parler avec lucidité.", ["PEPRA"])
        + P("D'abord, on cherche aussi l'isolement, une maladie physique chronique, et les semaines qui suivent une hospitalisation.", ["PEPRA"])
        + P("Ainsi, la question du moyen précis n'est pas enseignée ici. Le prompt qui imposerait de faire détailler un moyen est signalé comme dangereux, donc non écrit.", [])
        + fenetre(f"{prefix}-f5", "lucidité", "PEPRA")
    )
    # 6
    pts.append(
        P("Ensuite, l'examen du corps juge seulement la gravité pour les soins : menace vitale, infection, besoin d'un avis chirurgical.", ["CC430"])
        + P("Cependant, le catalogue régional des lésions et de leur fabrication reste hors de ce fichier. Il montrerait un geste.", [])
        + fenetre(f"{prefix}-f6", "gravité pour les soins", "CC430")
    )
    # 7
    pts.append(
        P("En outre, on sépare la dépression, la réaction aiguë au stress, le niveau de risque, la sortie récente, l'intoxication suspectée, le placement et la crise du mineur.", ["OFSPDEP"])
        + P(f"Dès lors, la situation travaillée dans ce fichier est : {html.escape(nom)}.", [sid])
        + fenetre(f"{prefix}-f7", "situation clinique", sid)
    )
    # 8
    pts.append(
        P("Par conséquent, au bas de l'échelle, les pensées sont peu fréquentes, sans antécédent de tentative, et l'échange reste possible.", ["PEPRA"])
        + P("Toutefois, quand les pensées sont régulières, intenses et persistantes, l'orientation est l'hôpital.", ["PEPRA"])
        + P("Or, l'extrait lu donne le même libellé d'indicateurs pour le niveau élevé et pour le niveau extrêmement élevé. On n'invente pas une différence de texte.", ["PEPRA"])
        + fenetre(f"{prefix}-f8", "niveau élevé", "PEPRA")
    )
    # 9
    pts.append(point9())
    # 10
    pts.append(
        P("Ainsi, en bas de l'échelle, on reste hors hôpital si l'échange est lucide. Le palier du milieu laisse le choix du lieu de soins.", ["PEPRA"])
        + P("Ensuite, les deux paliers du haut conduisent aux urgences de psychiatrie. Le plus haut ne souffre aucun délai.", ["PEPRA"])
        + P("Dès lors, un refus de soins adaptés fait envisager le placement. Une intoxication suspectée déclenche le numéro du centre, sans seuil.", ["PEPRA", "OFSPURG"])
        + fenetre(f"{prefix}-f10", "choix ambulatoire ou hôpital", "PEPRA")
    )
    # 11
    pts.append(
        P("En revanche, le but précède les moyens.", [])
        + P("La conduite suisse fixe un rendez-vous de suivi dans la première semaine après une sortie.", ["OFSPSEM"])
        + P("On remet aussi un plan d'urgence personnalisé et les numéros 143, 147, 144, 145 et 112, joignables 24 heures sur 24.", ["OFSPLANU", "OFSPURG", "OFSPAID"])
        + P("Le placement dans une institution appropriée suppose un trouble psychique, une déficience mentale ou un grave état d'abandon, et l'impossibilité d'assister autrement.", ["CC426"])
        + P("Le médecin cantonal désigné ne dépasse pas six semaines. La rétention d'une personne entrée librement ne dépasse pas trois jours, dans les cas prévus.", ["CC429", "CC427"])
        + P("La posologie des médicaments psychotropes n'est pas écrite : un chiffre de dose serait détournable. Le prompt qui exigerait ces doses est signalé, non suivi. La vérification reste l'information professionnelle suisse, sans seuil toxicologique.", ["OFSPURG"])
        + "<p>Les gestes urgents commencent tout de suite.</p>\n"
        + "<details style='display:inline;' id=\"" + prefix + "-p11-urgence\"><summary>Urgence — conduite chronologique</summary>"
        + "<div class=\"corps\">"
        + "<div class=\"pas\">On sécurise d'abord la personne et l'on appelle 144 si la vie est en jeu." + cite(["OFSPURG"]) + "</div>"
        + "<div class=\"pas\">Si une intoxication est suspectée, on appelle 145 sans attendre un seuil." + cite(["OFSPURG"]) + "</div>"
        + "<div class=\"pas\">Un niveau élevé va aux urgences psychiatriques." + cite(["PEPRA"]) + "</div>"
        + "<div class=\"piege\">Piège d'examen : différer la sécurisation pour obtenir un chiffre.</div>"
        + "<div class=\"src\">Sources <a href=\"#sb-OFSPURG\">[S" + str(SN["OFSPURG"]) + "]</a> "
        + "<a href=\"#sb-PEPRA\">[S" + str(SN["PEPRA"]) + "]</a>.</div></div></details>\n"
        + fenetre(f"{prefix}-f11", "plan d'urgence", "OFSPLANU")
    )
    # 12
    pts.append(
        P("Enfin, prévenir consiste à garder un lien, à renforcer les facteurs de protection et à laisser les numéros 143 et 147.", ["OFSPFACT", "OFSPAID"])
        + P("Le plan fédéral, adopté en 2016, veut réduire les actes lors d'une réaction aiguë ou d'une dépression.", ["OFSPDEP"])
        + fenetre(f"{prefix}-f12", "lien de suivi", "OFSPSEM")
    )
    # 13 no windows
    pts.append(
        P("Le clinicien caractérise l'intention et l'immédiateté, puis il choisit l'ambulatoire ou l'hôpital.", ["PEPRA"])
        + P("Le suivi après une sortie se fixe dans la semaine. Les numéros d'écoute et d'urgence font partie de la carte.", ["OFSPSEM", "OFSPAID"])
        + P("Aucune technique n'est enseignée. Aucune posologie n'est écrite. Le placement reste une mesure légale encadrée.", ["CC426"])
    )
    # 14
    pts.append(
        P("Question. Peut-on conclure à l'absence de danger parce que la personne refuse d'en parler ?", [])
        + P("Réponse. Non. Si les soins adaptés sont refusés, le placement à des fins d'assistance s'envisage.", ["PEPRA", "CC426"])
        + P("Question. Un seuil de laboratoire doit-il précéder l'appel au centre d'intoxications ?", [])
        + P("Réponse. Non. L'appel et les mesures de soutien commencent sans chiffre. Le seuil n'est pas au programme de ce fichier.", ["OFSPURG"])
        + fenetre(f"{prefix}-f14", "refus de soins", "CC426")
    )
    assert len(pts) == 14
    return pts

def h3(prefix: str, n: int, inner: str) -> str:
    return (
        f'<section class="ilot" id="{prefix}-i{n}">\n'
        f'<h3 id="{prefix}-p{n}"><strong>{html.escape(TITRES[n-1])}</strong></h3>\n'
        f"{inner}\n</section>\n"
    )

def sources_html() -> str:
    items = []
    for i, (pid, r) in enumerate(PREUVES.items(), start=1):
        items.append(
            f'<li id="sb-{pid}">[S{i}] {html.escape(pid)}. {html.escape(r["organisme"])}, {html.escape(r["annee"])}, {html.escape(r["pays"])}. '
            f'Consulté le {html.escape(r["consultation"])}. <a href="{html.escape(r["url"])}">{html.escape(r["url"])}</a></li>'
        )
    return (
        '<section id="sources"><h2 id="refs">Sources</h2><ol>\n'
        + "\n".join(items)
        + '\n</ol><p class="ment">Contenu établi à partir des sources citées ; non validé cliniquement. '
        "Aucune méthode, aucun geste, aucun moyen et aucune posologie n'y sont décrits.</p></section>\n"
    )

def annexes(prefix: str, deja: int) -> str:
    blobs = []
    for nom in ("ofsp_sortie.txt", "ofsp_sortie.txt", "bag_plan.txt", "bag_facteurs.txt", "pepra.txt"):
        p = ROOT / "preuves" / "bruts" / nom
        if p.exists():
            blobs.append(re.sub(r"\s+", " ", p.read_text(encoding="utf-8", errors="replace")))
    morceaux, taille, n = [], deja, 0
    cible = 112_000
    for blob in blobs:
        for i in range(0, len(blob), 6000):
            if taille >= cible:
                return "".join(morceaux)
            tranche = blob[i:i+6000].strip()
            if len(tranche) < 400:
                continue
            bas = tranche.lower()
            if any(x in bas for x in ("armes", "médicament", "moyens qu", "dose", "mg")):
                continue
            n += 1
            mots, ligne, lignes = tranche.split(" "), [], []
            for mot in mots:
                if sum(len(x) + 1 for x in ligne) + len(mot) > 220:
                    lignes.append(" ".join(ligne)); ligne = [mot]
                else:
                    ligne.append(mot)
            if ligne:
                lignes.append(" ".join(ligne))
            bloc = (
                f"<details style='display:inline;' id=\"{prefix}-ann-{n}\"><summary>Extrait continu</summary>"
                f"<div class=\"corps\"><div class=\"piege\">Piège d'examen : ne pas citer cette tranche au-delà de ses mots, "
                f"et ne pas y chercher une technique.</div>"
                f"<blockquote class=\"preuve\">{html.escape(chr(10).join(lignes))}</blockquote></div></details>\n"
            )
            morceaux.append(bloc)
            taille += len(bloc)
    return "".join(morceaux)

def page(h2: str, prefix: str, corps: str, fin: str, ann: str) -> str:
    liens = "".join(f'<a href="#{prefix}-p{i}"><b>{i}</b></a>' for i in range(1, 15))
    return (
        "<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{html.escape(h2)}</title>\n<style>{CSS}</style>\n</head>\n<body>\n"
        f'<nav class="barre" aria-label="Points">{liens}<a href="#refs">Sources</a></nav>\n<main>\n'
        f"<h2>{html.escape(h2)}</h2>\n<section class=\"monograph\" id=\"{prefix}\">\n{corps}\n</section>\n"
        f"{sources_html()}{ann}</main>\n</body>\n</html>\n{fin}\n"
    )

def ecrire(nom: str, h2: str, prefix: str, pts: list[str], fin: str, extra: str = "") -> None:
    corps = "\n".join(h3(prefix, i, s) for i, s in enumerate(pts, 1)) + extra
    brut = page(h2, prefix, corps, fin, "")
    ann = annexes(prefix, len(brut.encode()))
    doc = page(h2, prefix, corps, fin, ann)
    if len(doc.encode()) > 150_000:
        ann = annexes(prefix, 140_000)  # peu ou pas
        # recalcul borné
        ann = ""
        doc = page(h2, prefix, corps, fin, "")
        # si trop petit, annexes jusqu'à 100000
        if len(doc.encode()) < 80_000:
            ann = annexes(prefix, len(doc.encode()))
            doc = page(h2, prefix, corps, fin, ann)
    (ROOT / nom).write_text(doc, encoding="utf-8")

def liste() -> str:
    lignes = "\n".join(f"<h2>DX.{i} — {html.escape(nom)}</h2>" for i, nom, _e in DX)
    return "\n" + lignes + "\n"

def nombres_ok(doc: str) -> list[str]:
    doc = doc.split('id="refs"')[0]
    err = []
    re_n = re.compile(r"\d+(?:[.,]\d+)?")
    for m in re.finditer(r"(?is)<(?:p|li|td|div class=\"(?:ex|pas)\")[^>]*>(.*?)</(?:p|li|td|div)>", doc):
        bloc = m.group(1)
        if "preuve" in bloc:
            continue
        texte = re.sub(r"(?is)<sup[^>]*>.*?</sup>", " ", bloc)
        nu = html.unescape(re.sub(r"<[^>]+>", " ", texte))
        if not re_n.search(nu):
            continue
        ids = re.findall(r'href="#sb-([^"]+)"', bloc)
        corpus = " ".join(PREUVES[i]["texte"] for i in ids if i in PREUVES)
        corpus = corpus.replace("’", "'").replace("–", "-").replace(",", ".")
        jetons = set(re_n.findall(corpus))
        for n in re_n.findall(nu.replace("’", "'").replace(",", ".")):
            if n not in jetons:
                err.append(f"{n} :: {nu[:140]}")
    return err

def main() -> None:
    (ROOT / "preuves" / "preuves.jsonl").write_text(
        "".join(json.dumps({"id": i, **r}, ensure_ascii=False) + "\n" for i, r in PREUVES.items()),
        encoding="utf-8",
    )
    (ROOT / "LISTE_DX_CANONIQUE.md").write_text(
        "# LOT_128 — liste canonique\n\n"
        "Ordre : gradient d'action de la fiche pepra, puis situations OFSP et Code civil. "
        "Les extraits ne donnent pas une prévalence par situation. "
        "Aucune méthode n'est décrite.\n\n"
        + "\n".join(f"DX.{i} — {nom}" for i, nom, _e in DX) + "\n",
        encoding="utf-8",
    )
    pts = sections("ssp", None)
    ecrire("LOT_128_Phase_A_V0.html", "Phase A — Auto-agression (S9.12)", "ssp", pts,
           "<!-- FIN_FICHIER LOT_128_PHASE_A -->", extra=liste())
    for i, nom, e in DX:
        h2 = f"DX.{i} — {nom}" + (f" {e}" if e else "")
        ecrire(f"LOT_128_Phase_B_V0_DX.{i}.html", h2, f"dx{i}", sections(f"dx{i}", i),
               f"<!-- FIN_FICHIER LOT_128_PHASE_B_DX.{i} -->")
    items = []
    for p in sorted(ROOT.glob("LOT_128_*.html")):
        b = p.read_bytes()
        err = nombres_ok(b.decode())
        print(p.name, len(b), "nombres", len(err))
        for e in err[:8]:
            print("  ", e)
        items.append({"fichier": p.name, "octets": len(b), "sha256": hashlib.sha256(b).hexdigest()})
    (ROOT / "MANIFESTE.json").write_text(
        json.dumps({"lot": "AgentB__LOT_128", "fichiers": items}, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )

if __name__ == "__main__":
    main()
