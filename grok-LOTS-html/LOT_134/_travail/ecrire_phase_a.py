#!/usr/bin/env python3
"""Phase A V8 du LOT_134 (F1.5). Sources lues le 31.10.2026."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v8lib import LOT, abbr, bouton, ecrire, fenetre, ilot, page, sup

A = abbr
S = sup
B = bouton

DX = [
    "Œdème veineux chronique des membres inférieurs",
    "Anévrisme de l'aorte abdominale",
    "Cholécystite aiguë",
    "Appendicite aiguë",
    "Cirrhose hépatique",
    "Adénopathie périphérique maligne",
    "Arthrite septique",
    "Péritonite aiguë généralisée",
    "Ischémie mésentérique aiguë",
    "Fasciite nécrosante",
]


def extrait(path, debut, fin):
    t = Path(path).read_text(encoding="utf-8")
    i = t.find(debut)
    j = t.find(fin, i + len(debut))
    if i < 0 or j < 0:
        raise SystemExit(f"extrait introuvable : {debut!r}")
    return " ".join(t[i:j].split())


def jusqua(path, debut, fin):
    t = Path(path).read_text(encoding="utf-8")
    i = t.find(debut)
    j = t.find(fin, i + len(debut))
    if i < 0 or j < 0:
        raise SystemExit(f"jusqua introuvable : {debut!r} / {fin!r}")
    return " ".join(t[i:j + len(fin)].split())


RMS = "/home/ubuntu/.cursor/projects/workspace/agent-tools/8fcd7dbf-404e-4ce2-a2f6-b24e09909c30.txt"
AAA = "/home/ubuntu/.cursor/projects/workspace/agent-tools/e9ce014f-3406-47e0-8027-68cf28d60e98.txt"
AMI = "/home/ubuntu/.cursor/projects/workspace/agent-tools/7e08e978-c344-4ed8-88d4-45ed57eea96c.txt"
WSES = "/home/ubuntu/.cursor/projects/workspace/agent-tools/c19b26c1-737c-4403-8eb6-2218148d9698.txt"
SA = "/home/ubuntu/.cursor/projects/workspace/agent-tools/9a5af575-66bf-485e-a06f-9fc4fb925e2e.txt"
AIPS = "/workspace/ressources_ia/aips/fi_fr/69266.txt.gz"

Q = {
    "douleur": extrait(RMS, "Les douleurs abdominales aiguës représentent", "1 Les douleurs"),
    "appendice": extrait(RMS, "La prévalence des appendicites", "Les signes cliniques typiques"),
    "cholecystite": extrait(RMS, "Environ 5 % des patients", "Aucune combinaison"),
    "murphy": extrait(RMS, "Le signe de Murphy", "(tableau 7)"),
    "foie": extrait(RMS, "La hauteur normale du foie", "L’estimation peut varier"),
    "foie_rv": extrait(RMS, "Le fait de palper ou non un foie", "0,4."),
    "rate": extrait(RMS, "En condition normale, la rate", "Pour augmenter"),
    "rate_rv": extrait(RMS, "Le RV+ de cet examen est de 8,2", "Cet examen est plus"),
    "masse": extrait(RMS, "La palpation profonde permet", "en profondeur que"),
    "peritonite": extrait(RMS, "Il faut également rechercher des signes de péritonite", "L’infarctus mésentérique"),
    "mesentere_rms": extrait(RMS, "L’infarctus mésentérique est un diagnostic", "Positionnement"),
    "hernie": extrait(RMS, "Un homme sur quatre", "Les orifices herniaires inguinaux"),
    "palpation_aaa": extrait(AAA, "Physical examination may reveal a pulsatile mass", "#### 3.2.1"),
    "prev_aaa": extrait(AAA, "The prevalence in 65 year old men", "In contrast"),
    "echo_aaa": extrait(AAA, "Abdominal US and duplex ultrasound (DUS) are first line", "Measurements must"),
    "ami1": extrait(AMI, "It has been estimated that around 1%", "The incidence"),
    "ami70": extrait(AMI, "AMI is the cause of acute abdomen in up to 10%", "The prevalence of acute mesenteric"),
    "malmo": extrait(AMI, "an overall incidence rate of AMI of 12.9/100,000", "Arterial thromboembolic"),
    "finlande": extrait(AMI, "A recent study from Finland reported", "Contemporary incidences"),
    "triade": extrait(AMI, "The typical clinical triad", "This clinical triad"),
    "wses12": extrait(WSES, "Provide (surgical) source control in patients with NSSTI", "(recommendation 1B)."),
    "bilton": extrait(WSES, "The mortality in the latter group was 38%", "[99]."),
    "principe_b": extrait(SA, "Principle B-Efforts should be made", "Treatment of SA"),
    "reco9": extrait(SA, "Recommendation 9-Except where there are signs", "Probabilistic antibiotic therapy can also"),
}


def aips_verifier():
    import gzip
    t = gzip.open(AIPS, "rt", encoding="utf-8").read()
    cites = {
        "aips_4g": "Il ne faut pas dépasser la dose quotidienne maximale de 4'000 mg de paracétamol.",
        "aips_enfant": "La dose quotidienne maximale pour les enfants âgés de 9 à 12 ans est de 2'000 mg.",
        "aips_moins9": "Les enfants âgés de moins de 9 ans ne doivent pas être traités par Dafalgan 500 mg comprimés.",
        "aips_intervalle": "Respecter un intervalle de 4 à 8 h (adultes) ou 6 à 8 h (enfants) entre chaque prise.",
        "aips_2g": "La dose quotidienne ne doit pas dépasser 2 g",
        "aips_foie": "Chez les patients ayant une maladie hépatique chronique ou compensée active, en particulier une insuffisance hépatocellulaire légère à modérée, alcoolisme chronique, déficit d'alimentation chronique (faibles réserves de glutathion hépatique) ou déshydratation, ainsi que dans les patients adultes souffrant de cachexie la dose doit être réduite ou l'intervalle entre les doses étendu.",
        "aips_ci": "Troubles fonctionnels hépatiques graves (cirrhose hépatique et ascite)/hépatite aiguë ou maladie hépatique décompensée active.",
        "aips_gros1": "En cas de nécessité clinique, le paracétamol peut être pris ou utilisé pendant la grossesse.",
        "aips_gros2": "Toutefois, il convient de prendre ou d'utiliser la dose efficace la plus faible pendant la durée la plus courte possible et à la fréquence la plus basse possible.",
        "aips_lait1": "Le paracétamol passe dans le lait maternel.",
        "aips_lait2": "La concentration dans le lait maternel est similaire à la concentration momentanée dans le plasma de la mère.",
        "aips_lait3": "Des cas de rashs cutanés chez les nourrissons allaités ont été rapportés.",
        "aips_lait4": "Des conséquences préjudiciables durables pour le nourrisson ne sont pas connues.",
        "aips_lait5": "Bien que l'utilisation du paracétamol soit considérée comme compatible avec l'allaitement, la prudence est de mise lors de l'utilisation du Dafalgan comprimés pendant l'allaitement.",
    }
    for cle, phrase in cites.items():
        if phrase not in t:
            raise SystemExit(f"citation AIPS absente : {cle}")
    return cites


Q.update(aips_verifier())
Q["masse"] = jusqua(RMS, "La palpation profonde permet", "respiration.")
Q["foie_rv"] = jusqua(RMS, "Le fait de palper ou non un foie", "0,4.")
Q["hernie"] = jusqua(RMS, "Un homme sur quatre", "examen clinique.")
Q["mesentere_rms"] = jusqua(RMS, "L’infarctus mésentérique est un diagnostic", "ischémique.")
Q["prev_se"] = jusqua(AAA, "The prevalence in 65 year old men", "Swedish Screening Programme")
Q["palp_sens"] = jusqua(AAA, "abdominal palpation has a sensitivity", "14% to 100%.")
Q["echo_court"] = jusqua(AAA, "with high (> 97%)", "specificity.")
Q["triade_douleur"] = jusqua(AMI, "severe abdominal pain with minimal findings", "clinical signs)")


def guillemets(cle):
    return "«" + Q[cle] + "»"


def preuves():
    d = LOT / "evidence"
    d.mkdir(parents=True, exist_ok=True)
    lignes = ["# Extraits lus le 31.10.2026 (Europe/Zurich)", ""]
    for cle, texte in Q.items():
        lignes.append(f"## {cle}")
        lignes.append(texte)
        lignes.append("")
    (d / "extraits_lus.txt").write_text("\n".join(lignes), encoding="utf-8")
    (d / "INDEX.md").write_text(
        """# INDEX des preuves — LOT_134

Extraits datés du 31.10.2026, copiés depuis les pages et l'AIPS réellement lus.
Le fichier `extraits_lus.txt` reprend les passages cités entre guillemets.

1. PROFILES 2023, PDF UNIGE, ligne SSP F1.5 « abnormal findings upon palpation ». https://www.unige.ch/medecine/application/files/6617/5939/2636/2023_PROFILES_final_Intregre2025.pdf
2. Piqueres S, Staeger P, Pasche O. Examen de l'abdomen : et si nous refaisions nos gammes ? Revue Médicale Suisse 2016;537, 2 novembre 2016. https://www.revmed.ch/revue-medicale-suisse/2016/revue-medicale-suisse-537/examen-de-l-abdomen-et-si-nous-refaisions-nos-gammes
3. Rabe E, Pannier F. What have we learned from the Bonn Vein Study? Phlebolymphology. Enquête du 13.11.2000 au 15.3.2002, 3072 adultes. https://www.phlebolymphology.org/what-have-we-learned-from-the-bonn-vein-study/ — étude princeps citée par cette page : Rabe E et al. Phlebologie 2003;32:1-14.
4. Wanhainen A et al. ESVS 2024 clinical practice guidelines on abdominal aorto-iliac artery aneurysms. Eur J Vasc Endovasc Surg. https://www.ejves.com/article/S1078-5884(23)00889-4/fulltext
5. Björck M et al. Management of the diseases of mesenteric arteries and veins. ESVS, Eur J Vasc Endovasc Surg, publié le 29.3.2017. https://doi.org/10.1016/j.ejvs.2017.01.010
6. Sartelli M et al. 2018 WSES/SIS-E consensus on skin and soft-tissue infections. World J Emerg Surg, 14 décembre 2018. https://link.springer.com/article/10.1186/s13017-018-0219-9
7. Couderc M, Bart G, Coiffier G et al. 2020 French recommendations on septic arthritis in an adult native joint. Joint Bone Spine, publié le 3.8.2020. https://doi.org/10.1016/j.jbspin.2020.07.012
8. Swissmedic, information professionnelle DAFALGAN comprimés, n° 69266, UPSA Switzerland AG, texte hors ligne du dépôt lu le 31.10.2026. https://files.refdata.ch/simis-public-prod/MedicinalDocuments/5ef966b419c74454924120d685e948cc-fr.html

Les prévalences sans dénominateur commun, et les doses absentes de cette AIPS, restent marquées « À vérifier ».
""",
        encoding="utf-8",
    )


def tableau_dx():
    lignes = [
        (1, "E10", "13,4 % des adultes examinés avaient un œdème prenant le godet à Bonn, stade C3 de la classification clinique, étiologique, anatomique et physiopathologique (CEAP). En France, le stade C3 était à 1,1 % chez les hommes et à 2,2 % chez les femmes.", "Contention d'abord. Un œdème unilatéral fait chercher une thrombose. Le score de cette thrombose est À vérifier."),
        (2, "E4", "Chez les hommes de 65 ans : 1,7 % en Suède (2006-2009) et 1,3 % au Royaume-Uni (2009-2013) ; les deux programmes nationaux rapportent moins de 1 % en 2020-2021. La palpation ne fait pas le diagnostic.", "Échographie au lit si douleur ou instabilité ; angioscanner si le patient est stable."),
        (3, "E7", "Environ 5 % des patients vus aux urgences pour une douleur abdominale aiguë. L'incidence en population est À vérifier.", "Échographie. Le signe de Murphy est peu discriminatif."),
        (4, "E6", "1 % des douleurs abdominales aiguës en premier recours ; incidence 9 pour 100 000 personnes et par année.", "Imagerie après la clinique. Le score d'Alvarado est cité par la Revue Médicale Suisse : moins de 4 évite en principe la chirurgie, 7 ou plus l'oriente."),
        (5, "E9", "Prévalence suisse ou européenne non lue dans cette session : À vérifier. Le foie palpable ne prouve pas l'hépatomégalie.", "Échographie. La hauteur clinique normale va de 6 à 12 cm."),
        (6, "E8", "Part de malignité parmi les adénopathies en premier recours : À vérifier. Toute adénopathie sus-claviculaire s'explique.", "Pas d'antibiothérapie d'épreuve à répétition. La biopsie se décide avec le spécialiste ; le délai exact est À vérifier."),
        (7, "E5", "Incidence non lue ici : À vérifier. C'est une urgence diagnostique.", "Ponction avant l'antibiotique, sauf gravité immédiate. Le score séquentiel d'évaluation des défaillances d'organe (SOFA) est alors d'au moins 2."),
        (8, "E2", "Pas d'incidence séparée lue. La défense, la détente ou le silence auscultatoire annoncent une perforation.", "Appel chirurgical. La place de l'imagerie quand le ventre est déjà de bois est À vérifier comme règle suisse formalisée."),
        (9, "E3", "Environ 1 % des abdomens aigus ont une forme artérielle ; jusqu'à 10 % après 70 ans. Malmö 1970-1982 : 12,9 pour 100 000 personnes-années. Finlande : 7,3 pour 100 000.", "Angioscanner. Revasculariser avant de réséquer si le centre le peut."),
        (10, "E1", "Incidence non lue : À vérifier. Le contrôle de la source se fait dès que possible, et au plus dans les 12 heures après l'admission.", "Bloc opératoire. Antibiotique immédiat. La dose en milligrammes se lit dans l'information professionnelle suisse (AIPS) du produit choisi."),
    ]
    rows = []
    for i, e, prev, acte in lignes:
        rows.append(
            "<tr><td>DX."
            + str(i)
            + " — "
            + DX[i - 1]
            + "</td><td>🚩 "
            + e
            + "</td><td>"
            + prev
            + "</td><td>"
            + acte
            + "</td></tr>"
        )
    return (
        '<div class="tw"><table><caption>Dix diagnostics, prévalence lue et rang d\'exclusion</caption><thead><tr>'
        "<th>Diagnostic</th><th>Rang d'exclusion</th><th>Fréquence lue, avec son dénominateur</th><th>Premier acte</th>"
        "</tr></thead><tbody>"
        + "\n".join(rows)
        + "</tbody></table></div>"
    )


def sommaire():
    items = [
        "Définition",
        "Épidémiologie",
        "Physiopathologie",
        "Démarche diagnostique",
        "Anamnèse et drapeaux rouges",
        "Examen physique",
        "Approche syndromique",
        "Diagnostic positif",
        "Examens complémentaires",
        "Arbre décisionnel",
        "Prise en charge en Suisse",
        "Prévention",
        "Points clés",
        "Pièges d'examen",
    ]
    lis = "\n".join(f'<li><a href="#p{i}">{i}. {t}</a></li>' for i, t in enumerate(items, 1))
    return f'''<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{lis}
</ol>
<p class="sous">Les mots ⧉ ouvrent une fenêtre. Les sources sont à la fin.</p>
</nav>'''


def construire():
    preuves()
    ssp = A("situation de départ", "situation de départ de PROFILES")
    profiles = A("Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland", "Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland")
    esvs = A("European Society for Vascular Surgery", "European Society for Vascular Surgery")
    aips = A("information professionnelle suisse", "information professionnelle suisse")
    sofa = A("Sequential Organ Failure Assessment", "score séquentiel d'évaluation des défaillances d'organe")
    ceap = A("Clinical-Etiological-Anatomical-Pathophysiological", "classification clinique, étiologique, anatomique et physiopathologique des veines")
    wses = A("World Society of Emergency Surgery", "société mondiale de chirurgie d'urgence")
    sise = A("Surgical Infection Society Europe", "société européenne d'infection chirurgicale")

    essentiel = (
        "Une anomalie à la palpation est un signe, et non encore un diagnostic. "
        "Le médecin décrit la consistance, les limites et la douleur avant de nommer une maladie. "
        f"Dix diagnostics organisent ce cours. Leur ordre de fréquence est sourcé quand le dénominateur est le même, et marqué À vérifier sinon. "
        f"Le rang 🚩 E, lui, dit ce qu'il faut exclure d'abord : la {B('w-dix', 'fasciite nécrosante')} passe avant l'œdème veineux, bien plus commun. "
        f"Les chiffres, les citations et la seule dose écrite ici, celle du paracétamol selon l'{aips}, sont dans les fenêtres."
    )

    p1 = (
        f"Le {ssp} F1.5 de {profiles} 2023 s'intitule, en anglais, abnormal findings upon palpation, et en français « Anomalies à la palpation » dans le catalogue du projet. "
        f"Aucune société savante lue ici n'en donne une définition officielle unique : À vérifier. "
        f"En pratique, la {B('w-masse', 'palpation profonde d\'une masse')} en précise la localisation, la dimension, la forme, la consistance, la sensibilité, le caractère pulsatile et la mobilité respiratoire" + S(2) + ". "
        "La température cutanée et le godet complètent l'examen des parties molles, sans que ces deux axes figurent dans la liste abdominale citée."
    )
    w_masse = fenetre(
        "w-masse",
        "Ce que la main doit décrire",
        f"<p>{guillemets('masse')}{S(2)}</p>"
        "<p>La Revue Médicale Suisse ajoute qu'il faut commencer par les zones non douloureuses, mains réchauffées, avant-bras à l'horizontale, doigts joints.</p>"
        "<p>Les cinq axes parfois enseignés (consistance, mobilité, sensibilité, température, limites) ne sont pas une définition de société. La liste sourcée ci-dessus en est le substitut lu.</p>",
    )

    p2 = (
        f"Les douleurs abdominales aiguës font environ 1 à 2 % des motifs en médecine de premier recours, et à peine 10 % sont des urgences vitales" + S(2) + ". "
        f"L'œdème veineux prenant le godet est, parmi les dix, le signe de population le plus fréquent qui ait été lu : {B('w-epi', '13,4 % à Bonn, beaucoup moins dans l\'étude française')}" + S(3) + ". "
        f"L'anévrisme de l'aorte abdominale touche 1,3 à 1,7 % des hommes de 65 ans dans les dépistages européens cités, et moins de 1 % dans les rapports nationaux de 2020-2021" + S(4) + ". "
        "Les autres fréquences n'ont pas le même dénominateur : le tableau le dit, et le rang reste À vérifier quand les populations diffèrent."
    )
    w_epi = fenetre(
        "w-epi",
        "Fréquences lues, chacune avec son dénominateur",
        "<p>Étude de Bonn, du 13 novembre 2000 au 15 mars 2002. L'échantillon compte 3072 adultes de 18 à 79 ans, tirés au sort. "
        "Parmi eux, 13,4 % avaient un œdème prenant le godet des jambes au moment de l'examen (11,6 % des hommes, 14,9 % des femmes), classé C3.</p>"
        "<p>L'étude française citée dans la même revue trouvait un stade C3 chez 1,1 % des hommes et 2,2 % des femmes. "
        "Les auteurs écrivent que la prévalence du stade C3 varie de 1,1 % à 14,9 % selon la façon de vérifier l'œdème.</p>"
        f"<p>{guillemets('douleur')}{S(2)}</p>"
        f"<p>{guillemets('appendice')}{S(2)}</p>"
        f"<p>{guillemets('cholecystite')}{S(2)}</p>"
        "<p>Anévrisme de l'aorte abdominale (AAA). Le chiffre suédois est cité tel quel. "
        "Le programme du Royaume-Uni, de 2009 à 2013, rapporte 1,3 %. Les deux programmes nationaux sont sous 1 % en 2020-2021.</p>"
        f"<p>{guillemets('prev_se')}{S(4)}</p>"
        "<p>L'ordre DX.1 à DX.10 suit ces ordres de grandeur. Il n'est pas une méta-analyse. Là où le dénominateur change, le rang est À vérifier.</p>",
    )

    p3 = (
        "La main ne mesure qu'une résistance à la déformation, un réflexe de paroi, ou la façon dont une onde passe dans un liquide ou un gaz. "
        f"Quand le péritoine pariétal est irrité, la paroi se défend. La Revue Médicale Suisse relie défense, détente et silence auscultatoire à une perforation" + S(2) + ". "
        f"Le {B('w-physio', 'schéma')} ramène ces signes à trois mécanismes : rigidité du tissu, réflexe de paroi, transmission d'une onde. "
        "Le détail de chaque maladie est dans son diagnostic différentiel, qui ne répète pas ce cours."
    )
    w_physio = fenetre(
        "w-physio",
        "Trois mécanismes, un schéma",
        """<figure class="schema"><svg viewBox="0 0 360 150" role="img" aria-label="Trois mécanismes d'un signe palpé">
<g fill="none" stroke="currentColor" stroke-width="1.4">
<rect x="8" y="20" width="100" height="70" rx="8"/>
<rect x="130" y="20" width="100" height="70" rx="8"/>
<rect x="252" y="20" width="100" height="70" rx="8"/>
</g>
<g fill="currentColor" font-family="Atkinson Hyperlegible, Verdana, sans-serif" font-size="12" text-anchor="middle">
<text x="58" y="48">Rigidité</text>
<text x="58" y="66">du tissu</text>
<text x="180" y="48">Réflexe</text>
<text x="180" y="66">de paroi</text>
<text x="302" y="48">Onde</text>
<text x="302" y="66">transmise</text>
</g>
</svg>
<figcaption>Masse dure, défense et flot relèvent de trois physiques différentes. Le schéma est pédagogique ; il ne remplace pas une source anatomique de société, À vérifier pour un traité nommé.</figcaption></figure>
<p>Le foie normal mesure 6 à 12 cm de hauteur clinique sur la ligne médioclaviculaire, selon la taille du patient. Palper un bord ne prouve pas l'hépatomégalie : le rapport de vraisemblance positif n'est que de 2, et le rapport négatif est de 0,4.</p>""",
    )

    p4 = (
        "La démarche sépare la fréquence et la gravité. "
        f"DX.1 est l'{DX[0]}, parce que c'est le signe de population le plus répandu parmi les chiffres lus. "
        f"DX.10 est la {DX[9]}, parce qu'aucune incidence lue n'est plus basse, et ce rang de fréquence est À vérifier. "
        f"Le {B('w-dix', 'tableau des dix')} donne pour chacun le rang 🚩 E, le chiffre et le premier acte. L'algorithme du point 10 commence par E1."
    )
    w_dix = fenetre("w-dix", "Tableau comparatif des dix diagnostics", tableau_dx())

    p5 = (
        "L'anamnèse précède la main : siège, migration, toux, fièvre, sueurs, amaigrissement chiffré, arrêt des gaz, et médicaments. "
        f"Un abdomen très douloureux avec peu de signes, surtout s'il existe une fibrillation, fait évoquer l'ischémie mésentérique" + S(2, 5) + ". "
        f"Une hypotension orthostatique avec douleur abdominale peut annoncer une grossesse extra-utérine ou une rupture d'anévrisme" + S(2) + ". "
        f"Les {B('w-rouges', 'drapeaux rouges')} se cherchent avant le diagnostic fin."
    )
    w_rouges = fenetre(
        "w-rouges",
        "Drapeaux rouges lus",
        f"<p>{guillemets('peritonite')}{S(2)}</p>"
        f"<p>{guillemets('mesentere_rms')}{S(2)} Le passage s'arrête ici dans l'article, au seuil de la section suivante.</p>"
        "<p>Artère mésentérique supérieure (SMA). La triade lue associe une douleur sévère avec peu de signes, une vidange intestinale, et une source d'embole, le plus souvent une fibrillation. "
        "Elle était présente chez 80 % des patients d'une étude prospective citée par la même recommandation.</p>"
        f"<p>{guillemets('triade_douleur')}{S(5)}</p>"
        "<p>Crépitation, douleur disproportionnée et induration au-delà de l'érythème orientent vers une infection nécrosante des parties molles. "
        "L'articulation chaude, tendue, avec fièvre, oriente vers une arthrite septique. "
        "Ces deux tableaux sont repris aux points 7 et 10.</p>",
    )

    p6 = (
        "On palpe du non douloureux vers le douloureux, du superficiel vers le profond, en regardant le visage" + S(2) + ". "
        f"La hauteur du foie se situe entre 6 et 12 cm. La rate normale {B('w-foie', 'ne se palpe pas')}" + S(2) + ". "
        f"La palpation d'un anévrisme a une sensibilité de 33 à 100 % et ne suffit pas" + S(4) + ". "
        f"L'échographie, elle, dépasse 97 % de sensibilité et de spécificité pour le petit anévrisme" + S(4) + "."
    )
    w_foie = fenetre(
        "w-foie",
        "Foie, rate, anévrisme, hernie",
        "<p>Rapport de vraisemblance (RV).</p>"
        f"<p>{guillemets('foie')}{S(2)}</p>"
        f"<p>{guillemets('foie_rv')}{S(2)}</p>"
        f"<p>{guillemets('rate')}{S(2)}</p>"
        f"<p>{guillemets('rate_rv')}{S(2)} Si l'anamnèse fait suspecter une rate augmentée et que la rate est palpée, le diagnostic clinique de splénomégalie peut être posé, dit l'article. Sinon, il faut des examens.</p>"
        f"<p>{guillemets('palp_sens')}{S(4)} La même recommandation conclut que la palpation abdominale n'est pas fiable pour ce diagnostic.</p>"
        "<p>Échographie abdominale (US). Échodoppler duplex (DUS).</p>"
        f"<p>{guillemets('echo_court')}{S(4)} Ce taux vise le petit anévrisme, avec l'échographie et l'échodoppler comme examens de première ligne.</p>"
        f"<p>{guillemets('hernie')}{S(2)} La hernie inguinale n'est pas l'un des dix diagnostics de ce lot. Elle rappelle qu'un orifice se palpe debout, avec une toux.</p>",
    )

    p7 = (
        "Quatre syndromes suffisent à orienter la main. "
        "L'irritation péritonéale associe douleur, immobilité, toux pénible, défense ou contracture. "
        "Le syndrome de masse se décrit sur les caractères du point 1, sans étiquette précoce. "
        f"L'organomégalie se mesure. L'atteinte des parties molles ou d'une articulation se reconnaît à la chaleur, au godet, à la fluctuation ou à la crépitation, détaillés dans la {B('w-synd', 'fenêtre syndromique')}."
    )
    w_synd = fenetre(
        "w-synd",
        "Quatre syndromes et ce qu'ils changent",
        """<div class="tw"><table><caption>Syndromes palpatoires</caption><thead><tr><th>Syndrome</th><th>Signe qui l'ouvre</th><th>Ce qu'on ne conclut pas</th></tr></thead><tbody>
<tr><td>Irritation péritonéale</td><td>Défense, détente, silence auscultatoire</td><td>Le diagnostic de cause (appendicite, perforation, autre) n'est pas fait par la main seule.</td></tr>
<tr><td>Masse</td><td>Limites, consistance, mobilité, pouls</td><td>Une aorte battante chez une personne maigre peut être normale. L'anévrisme, lui, n'est pas affirmé par la main.</td></tr>
<tr><td>Organomégalie</td><td>Hauteur du foie, pointe de rate</td><td>Un bord hépatique palpable n'est pas une hépatomégalie.</td></tr>
<tr><td>Parties molles ou articulation</td><td>Chaleur, fluctuation, crépitation, épanchement</td><td>Un érysipèle simple ne explique pas une douleur disproportionnée ni une crépitation.</td></tr>
</tbody></table></div>""",
    )

    p8 = (
        "Le diagnostic positif du signe est la description, pas le nom de la maladie. "
        "On note le côté, les centimètres, la consistance, la mobilité, la douleur et la chaleur, puis on compare à l'autre côté. "
        f"Le diagnostic de la cause vient ensuite : échographie pour la vésicule et l'aorte, angioscanner pour l'ischémie, ponction pour l'articulation, chirurgie pour la nécrose et pour le ventre de bois. "
        f"Aucun de ces examens n'efface un signe déjà écrit dans le dossier."
    )

    p9 = (
        "Le premier bilan dépend du signe, pas d'un panel unique. "
        f"Chez la femme en âge de procréer, une grossesse doit être connue avant l'imagerie : la démarche exacte du dosage est À vérifier dans une recommandation suisse non lue ici. "
        f"L'artérite mésentérique se confirme par l'angioscanner, pas par un abdomen souple" + S(5) + ". "
        f"Le score de laboratoire du risque d'infection nécrosante (LRINEC) ne doit pas servir à exclure. "
        f"À 6 ou plus, sa sensibilité n'est que de 68,2 % dans la méta-analyse citée par le consensus {wses} et {sise}" + S(6) + "."
    )

    p10 = (
        "L'arbre commence par ce qui tue dans les heures, même si c'est rare. "
        f"E1, fasciite : bloc dans les 12 heures après l'admission" + S(6) + ". "
        f"E2, péritonite généralisée : chirurgien. E3, ischémie mésentérique : angioscanner. E4, anévrisme douloureux ou instable : échographie au lit. "
        f"La {B('w-algo', 'suite E5 à E10')} garde la ponction articulaire, l'appendicite, la vésicule, le ganglion, le foie et l'œdème."
    )
    w_algo = fenetre(
        "w-algo",
        "Algorithme : exclure d'abord les graves",
        """<ol class="algo">
<li>E1. Crépitation, douleur hors de proportion, induration au-delà de la rougeur : infection nécrosante. Contrôle chirurgical de la source dès que possible, au plus dans les 12 heures après l'admission. Une série citée par le consensus oppose 38 % de mortalité après débridement tardif ou incomplet à 4,2 % après débridement précoce et complet.</li>
<li>E2. Contracture généralisée, détente, silence auscultatoire : péritonite. Appel chirurgical. Ne pas rassurer sur un ventre encore souple si la douleur est majeure et le contexte vasculaire.</li>
<li>E3. Douleur sévère, examen pauvre, souvent fibrillation : ischémie mésentérique. Angioscanner artériel et veineux. Environ 1 % des abdomens aigus, jusqu'à 10 % après 70 ans.</li>
<li>E4. Masse pulsatile, douleur, hypotension : anévrisme. Échographie au lit. La palpation seule n'est pas fiable. L'échographie ne voit pas bien un saignement rétropéritonéal ; un anévrisme chez un patient instable suggère fortement la rupture.</li>
<li>E5. Articulation chaude et tendue : arthrite septique de l'adulte sur articulation native. Ponction et hémocultures avant l'antibiotique, sauf signe de gravité immédiate avec un score SOFA d'au moins 2.</li>
<li>E6. Douleur migrée, fosse iliaque droite : appendicite. Incidence lue : 9 pour 100 000 par année. L'absence des signes classiques n'exclut pas.</li>
<li>E7. Hypocondre droit : cholécystite possible, environ 5 % des douleurs abdominales aiguës aux urgences. Murphy peu discriminatif. Échographie.</li>
<li>E8. Ganglion dur, fixé, sus-claviculaire : malignité à documenter. La part exacte en premier recours est À vérifier.</li>
<li>E9. Foie dur ou rate palpable : mesurer, puis échographie. Bord palpable n'égale pas hépatomégalie.</li>
<li>E10. Œdème bilatéral, mou, prenant le godet : maladie veineuse chronique jusqu'à preuve du contraire. Un œdème unilatéral fait chercher une thrombose. Le score clinique de cette thrombose est À vérifier dans cette session.</li>
</ol>""",
    )

    p11 = (
        f"En Suisse, la dose écrite dans cette leçon est celle du paracétamol, lue dans l'{aips} de Dafalgan comprimés, numéro Swissmedic 69266. "
        f"Au-delà de 40 kg, la prise va de 500 à 1 000 mg, sans dépasser 4 000 mg par jour, avec 4 à 8 heures entre les prises" + S(8) + ". "
        f"La cirrhose avec ascite figure parmi les contre-indications, et la maladie hépatique chronique limite la journée à 2 g. "
        f"Les autres médicaments de ce lot, antibiotiques compris, n'ont pas leur milligramme ici : il se lit dans l'AIPS du produit réellement choisi. Le {B('w-aips', 'texte lu')} est cité mot pour mot."
    )
    w_aips = fenetre(
        "w-aips",
        "Dafalgan comprimés, n° 69266, texte lu",
        f"<p>{guillemets('aips_4g')}{S(8)} {guillemets('aips_intervalle')}{S(8)}</p>"
        f"<p>{guillemets('aips_enfant')}{S(8)} {guillemets('aips_moins9')}{S(8)}</p>"
        f"<p>{guillemets('aips_foie')} {guillemets('aips_2g')}{S(8)}</p>"
        f"<p>Grossesse. {guillemets('aips_gros1')}{S(8)} {guillemets('aips_gros2')}{S(8)}</p>"
        f"<p>Allaitement. {guillemets('aips_lait1')} {guillemets('aips_lait2')}{S(8)}</p>"
        f"<p>{guillemets('aips_lait3')} {guillemets('aips_lait4')} {guillemets('aips_lait5')}{S(8)}</p>"
        f"<p>Contre-indication hépatique. {guillemets('aips_ci')}{S(8)}</p>"
        "<p>Ce texte ne choisit pas un antibiotique. La recommandation française de 2020 sur l'arthrite septique native décrit quand commencer, pas la dose suisse.</p>",
    )

    p12 = (
        "La prévention suit le signe, pas un programme unique. "
        f"Le dépistage par échographie, dans les populations à haut risque, est recommandé en classe I par la société européenne de chirurgie vasculaire en 2024. La cible n'est plus fixée dans la recommandation : elle dépend des conditions locales. La palpation n'en est pas l'outil" + S(4) + ". "
        "La contention est, dans l'étude de Bonn, le traitement veineux le plus fréquent, devant la chirurgie et le médicament. "
        "Aucun chiffre suisse de dépistage national de l'anévrisme n'a été lu ici : À vérifier."
    )

    p13 = (
        "Décrire avant de nommer. "
        "Exclure E1 à E4 avant de rassurer sur un signe fréquent. "
        "Un bord de foie palpable et une aorte battante sont des pièges de normalité. "
        f"La dose de paracétamol citée ne se transfère pas à un autre antalgique, ni à un foie décompensé" + S(8) + "."
    )

    p14 = (
        "Quatorze questions reprennent les confusions classiques de ce signe. "
        f"Répondez avant d'ouvrir les {B('w-pieges', 'pièges d\'examen')}."
    )
    quizzes = [
        ("Un ventre de bois attend-il le scanner ?", "Non comme réflexe enseigné ici. La défense, la détente et le silence annoncent une perforation, et le chirurgien est appelé. Une règle suisse qui interdirait toute image n'a pas été lue : À vérifier."),
        ("Une aorte que l'on palpe est-elle un anévrisme ?", "Pas forcément. La sensibilité de la palpation va de 33 à 100 %. L'échographie dépasse 97 % pour le petit anévrisme."),
        ("Un abdomen souple écarte-t-il l'ischémie mésentérique ?", "Non. La douleur peut être majeure avec peu de signes. Environ 1 % des abdomens aigus ont une forme artérielle, et jusqu'à 10 % après 70 ans."),
        ("Quel délai pour la fasciite une fois admis ?", "Le consensus WSES/SIS-E de 2018 demande le contrôle de la source dès que possible, et au moins dans les 12 premières heures après l'admission."),
        ("38 % et 4,2 %, qu'est-ce que c'est ?", "Dans la série de Bilton citée par ce consensus, la mortalité était de 38 % après débridement tardif ou incomplet, et de 4,2 % après débridement précoce et complet."),
        ("Faut-il un antibiotique avant la ponction d'une arthrite ?", "Non, sauf gravité immédiate avec un score SOFA d'au moins 2, selon les recommandations françaises de 2020. La dose en milligrammes se lit dans l'information professionnelle suisse du produit, elle n'est pas dans ces recommandations."),
        ("Quelle prise de Dafalgan comprimés 69266 après 40 kg ?", "500 à 1 000 mg par prise, au plus 4 000 mg par jour, en espaçant de 4 à 8 heures. La maladie hépatique chronique limite à 2 g par jour."),
        ("Peut-on donner ce paracétamol dans une cirrhose avec ascite ?", "Non. L'information professionnelle contre-indique les troubles fonctionnels hépatiques graves, et elle cite la cirrhose hépatique et l'ascite."),
        ("Et pendant la grossesse ?", "S'il est nécessaire, la dose efficace la plus faible, le moins longtemps et le moins souvent possible. Il n'existe pas d'études contrôlées chez la femme enceinte, dit le texte."),
        ("Et pendant l'allaitement ?", "Le paracétamol passe dans le lait. L'usage est considéré comme compatible, mais la prudence reste de mise. Des éruptions ont été rapportées chez le nourrisson."),
        ("Un foie dont on sent le bord est-il gros ?", "Pas sur ce seul signe. La hauteur normale va de 6 à 12 cm. Le rapport de vraisemblance positif d'un foie palpé pour l'hépatomégalie n'est que de 2."),
        ("Ne pas palper la rate, est-ce rassurant ?", "Non à soi seul. Le rapport de vraisemblance négatif de la palpation est de 0,4. La rate normale, en revanche, ne se palpe pas."),
        ("Le signe de Murphy affirme-t-il la cholécystite ?", "Non. L'article le juge peu discriminatif. Environ 5 % des douleurs abdominales aiguës aux urgences sont une cholécystite, et aucune combinaison clinique ne suffit."),
        ("L'œdème veineux se traite-t-il par un diurétique ?", "Pas d'après les sources lues. À Bonn, la contention était le traitement le plus fréquent. Prescrire un diurétique à la place n'est pas décrit ici, et une telle interdiction formelle est À vérifier."),
    ]
    items_q = "\n".join(
        f'<details class="quiz"><summary>{q}</summary><p>{r}</p></details>' for q, r in quizzes
    )
    w_pieges = fenetre(
        "w-pieges",
        "Pièges d'examen",
        "<p>Répondez avant d'ouvrir la réponse.</p>\n" + items_q,
    )

    sources = """<section class="ilot v"><h2 id="sources">Sources</h2>
<details class="quiz sources"><summary>Afficher les sources lues le 31.10.2026</summary>
<ol class="sources">
<li><sup class="s">1</sup> Commission interfacultés et facultés de médecine suisses, document PROFILES hébergé par l'Université de Genève, PDF « 2023_PROFILES_final_Intregre2025 », tableau des situations de départ, ligne F1.5 abnormal findings upon palpation. https://www.unige.ch/medecine/application/files/6617/5939/2636/2023_PROFILES_final_Intregre2025.pdf</li>
<li><sup class="s">2</sup> Piqueres S, Staeger P, Pasche O. Examen de l'abdomen : et si nous refaisions nos gammes ? Revue Médicale Suisse 2016;537, 2 novembre 2016. https://www.revmed.ch/revue-medicale-suisse/2016/revue-medicale-suisse-537/examen-de-l-abdomen-et-si-nous-refaisions-nos-gammes</li>
<li><sup class="s">3</sup> Rabe E, Pannier F. What have we learned from the Bonn Vein Study ? Phlebolymphology. Enquête allemande du 13.11.2000 au 15.3.2002, 3072 adultes. La page cite aussi l'étude française de Carpentier et al., J Vasc Surg 2004. https://www.phlebolymphology.org/what-have-we-learned-from-the-bonn-vein-study/</li>
<li><sup class="s">4</sup> Wanhainen A et al. European Society for Vascular Surgery 2024 clinical practice guidelines on the management of abdominal aorto-iliac artery aneurysms. European Journal of Vascular and Endovascular Surgery. https://www.ejves.com/article/S1078-5884(23)00889-4/fulltext</li>
<li><sup class="s">5</sup> Björck M et al. Management of the diseases of mesenteric arteries and veins. European Society for Vascular Surgery. European Journal of Vascular and Endovascular Surgery, publié le 29.3.2017. https://doi.org/10.1016/j.ejvs.2017.01.010</li>
<li><sup class="s">6</sup> Sartelli M et al. 2018 WSES/SIS-E consensus conference: recommendations for the management of skin and soft-tissue infections. World Journal of Emergency Surgery, 14 décembre 2018. https://link.springer.com/article/10.1186/s13017-018-0219-9</li>
<li><sup class="s">7</sup> Couderc M, Bart G, Coiffier G et al. 2020 French recommendations on the management of septic arthritis in an adult native joint. Joint Bone Spine, publié le 3.8.2020. https://doi.org/10.1016/j.jbspin.2020.07.012</li>
<li><sup class="s">8</sup> Swissmedic, information professionnelle DAFALGAN comprimés, numéro 69266, UPSA Switzerland AG. Texte hors ligne lu le 31.10.2026. https://files.refdata.ch/simis-public-prod/MedicinalDocuments/5ef966b419c74454924120d685e948cc-fr.html</li>
</ol>
<p>L'intitulé français du catalogue interne est « Anomalies à la palpation ». Il aligne le code F1.5 sur la ligne anglaise de PROFILES. Ce n'est pas une deuxième définition de société.</p>
</details></section>"""

    sous = (
        f"Cours du {ssp} F1.5 « Anomalies à la palpation », {profiles} 2023{S(1)}. "
        "Phase A : monographie et dix diagnostics différentiels. Texte du 31.10.2026. "
        "Les diagnostics différentiels ne répètent pas ce cours."
    )
    blocs = [
        ilot(None, "", essentiel, essentiel=True),
        sommaire(),
        ilot(1, "Définition", p1, w_masse),
        ilot(2, "Épidémiologie", p2, w_epi),
        ilot(3, "Physiopathologie", p3, w_physio),
        ilot(4, "Démarche diagnostique", p4, w_dix),
        ilot(5, "Anamnèse et drapeaux rouges", p5, w_rouges),
        ilot(6, "Examen physique", p6, w_foie),
        ilot(7, "Approche syndromique", p7, w_synd),
        ilot(8, "Diagnostic positif", p8),
        ilot(9, "Examens complémentaires", p9),
        ilot(10, "Arbre décisionnel", p10, w_algo),
        ilot(11, "Prise en charge en Suisse", p11, w_aips),
        ilot(12, "Prévention", p12),
        ilot(13, "Points clés", p13),
        ilot(14, "Pièges d'examen", p14, w_pieges),
        sources,
    ]
    # ilot(None) would break. Fix essentiel call: I used numero None. Look at ilot().
    html = page(
        "Anomalies à la palpation — LOT_134 Phase A",
        "Anomalies à la palpation",
        sous,
        blocs,
        "FIN_FICHIER LOT_134_Phase_A",
    )
    dest = ecrire("LOT_134_Phase_A_V0.html", html)
    liste = LOT / "LISTE_DX_CANONIQUE_PROVISOIRE.md"
    liste.write_text(
        "# LISTE DX PROVISOIRE — LOT_134 F1.5\n\n"
        "Gel réservé à l'auditeur médical (grok-4.6, run séparé). "
        "Ordre de fréquence d'après les chiffres lus le 31.10.2026 ; rang À vérifier quand les dénominateurs diffèrent. "
        "Le rang E est l'ordre d'exclusion, distinct du numéro DX.\n\n"
        + "\n".join(f"DX.{i} — {nom}" for i, nom in enumerate(DX, 1))
        + "\n\nE1 fasciite nécrosante ; E2 péritonite aiguë généralisée ; E3 ischémie mésentérique aiguë ; "
        "E4 anévrisme de l'aorte abdominale ; E5 arthrite septique ; E6 appendicite aiguë ; "
        "E7 cholécystite aiguë ; E8 adénopathie périphérique maligne ; E9 cirrhose hépatique ; "
        "E10 œdème veineux chronique des membres inférieurs.\n",
        encoding="utf-8",
    )
    print(dest)


if __name__ == "__main__":
    construire()
