#!/usr/bin/env python3
"""Phase A V8 — LOT_150 F2.2 Enzymes cardiaques anormales."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_html import A, P, S, b, cite, fen, ilot, page, table
from cahier_a import html as cahier_html

OUT = Path(__file__).resolve().parents[1] / "LOT_150_Phase_A_V0.html"

# Citations exactes (40–380 car., sans guillemet interne).
C_PAS_IM = cite(
    "rms2019_troponine.txt",
    "Une élévation de la hs-cTn ne correspond pas forcément à un infarctus du myocarde",
)
C_TYPE1 = cite(
    "rms2019_troponine.txt",
    "Un infarctus myocardique de type I doit être exclu en premier lieu",
)
C_SPEC = cite(
    "rms2019_troponine.txt",
    "Les troponines cardiaques I (cTnI) et T (cTnT) sont des composantes du système contractile cardiaque et spécifiques des cardiomyocytes.",
)
C_LESION = cite(
    "rms2019_troponine.txt",
    "Leur valeur au-delà du 99 e percentile de la valeur de référence définit une lésion du myocarde (myocardial injury).",
)
C_TYPE2 = cite(
    "rms2019_troponine.txt",
    "L’IM de type II est une ischémie myocardique aiguë due à un déséquilibre entre le débit sanguin coronarien",
    "sans lien avec un mécanisme athérothrombotique.",
)
C_PART = cite(
    "rms2019_troponine.txt",
    "Cette entité représente entre 2 et 57 % de tous les types d’IM",
)
C_33 = cite(
    "rms2019_troponine.txt",
    "Selon une étude observationnelle conduite dans un service d’urgences, sur 4436 patients, l’incidence de la hs-cTn secondaire était de 33 %.",
)
C_ORGANE = cite(
    "rms2019_troponine.txt",
    "son dosage ne confirme pas une ischémie myocardique et peut résulter d’autres mécanismes",
)
C_URL = cite(
    "rms2016_irc.txt",
    "Le seuil de référence supérieur (Upper Reference Limit, URL) de la troponine pour diagnostiquer un infarctus du myocarde a été placé au 99 e percentile",
    "d’une population de référence saine.",
)
C_14 = cite(
    "rms2016_irc.txt",
    "Le seuil de détection des tests ultrasensibles étant de 2 ng/l, le nouvel URL est de 14 ng/l pour la troponine T.",
)
C_IRC = cite(
    "rms2016_irc.txt",
    "On observe, selon la méthode conventionnelle, une élévation de la Tn T chez environ 53 % des patients souffrant d’IRC, contre 7 % pour la Tn I.",
)
C_81 = cite(
    "rms2016_irc.txt",
    "Avec une méthode ultrasensible, la troponine T est détectable chez 81 % de ces patients",
)
C_BANAL = cite(
    "rms2016_irc.txt",
    "Dans la majorité des cas, l’élévation des troponines ne peut être uniquement attribuée à l’insuffisance rénale et ne doit donc pas être",
)
C_ECHO = cite(
    "rms2016_irc.txt",
    "l’échocardiographie peut jouer un rôle important si le diagnostic de NSTEMI n’est pas clair",
    "sténose aortique, etc.",
)
C_ALGO = cite(
    "rms2024_sca.txt",
    "des algorithmes rapides d’inclusion/exclusion sont recommandés chez tous les patients suspects de NSTE-SCA",
    "à 2 heures (0/2 heures).",
)
C_POC = cite(
    "rms2024_sca.txt",
    "Les troponines mesurées par tests automatisés dans des laboratoires centralisés sont toujours préférées aux tests",
)
C_STEMI = cite(
    "rms2024_sca.txt",
    "Pour les patients avec STEMI, une coronarographie immé diate est indiquée.",
)
C_DELAI = cite(
    "rms2024_sca.txt",
    "effectuer la revasculari sation coronarienne dans les 60 minutes si le patient est admis dans un centre avec salle de cathétérisme cardiaque, et en moins de 90",
    "depuis un autre centre.",
)
C_120 = cite(
    "rms2024_sca.txt",
    "Si la revascularisation percutanée n’est pas possible dans les 120 minutes au moment du diagnostic, l’administration de fibrinolyse est indiquée",
    "situation pratiquement inexistante en Suisse",
)
C_GRACE = cite(
    "rms2024_sca.txt",
    "score de risque GRACE > 140 ou modifications ECG",
)
C_24 = cite(
    "rms2024_sca.txt",
    "une coronarographie est désormais recommandée au cours du séjour hospitalier mais pas obligatoirement dans les 24 heures après admission",
)
C_CHOC = cite(
    "rms2024_sca.txt",
    "il est recommandé de limiter l’angioplastie percutanée immédiate à l’artère liée à l’infarctus",
)
C_ARRET = cite(
    "rms2024_sca.txt",
    "Une angiographie immédiate de routine après un arrêt cardiaque ressuscité n’est pas recommandée",
    "sans élévation persistante du segment ST",
)
C_ASA = cite(
    "aips_51795.txt",
    "En cas d'infarctus aigu du myocarde, 200 à 300 mg d'acide acétylsalicylique par voie intraveineuse ou par voie orale",
    "forme non gastro-résistante).",
)
C_ASA2 = cite(
    "aips_51795.txt",
    "À partir du deuxième jour, 100 mg d'Aspirine Cardio par jour.",
)
C_ASA18 = cite(
    "aips_51795.txt",
    "En l'absence de données sur l'efficacité et la sécurité chez les enfants et adolescents de moins de 18 ans, Aspirine Cardio ne doit pas être utilisé",
)
C_BRI = cite(
    "aips_61389.txt",
    "Chez les patients ayant un syndrome coronarien aigu, le traitement par BRILIQUE doit être instauré avec une dose initiale de 180 mg",
    "90 mg deux fois par jour.",
)
C_BRI_G = cite(
    "aips_61389.txt",
    "BRILIQUE ne doit pas être utilisé pendant la grossesse, sauf nécessité absolue.",
)
C_BRI_A = cite(
    "aips_61389.txt",
    "BRILIQUE ne doit pas être utilisé pendant la période d'allaitement.",
)
C_PLAV = cite(
    "aips_54509.txt",
    "initier le traitement par Plavix par une dose de charge de 300 mg",
    "1 comprimé de Plavix à 75 mg",
)
C_EFI = cite(
    "aips_59136.txt",
    "Avant le début de l'ICP, administrer une dose de charge unique de 60 mg de prasugrel",
    "10 mg de prasugrel une fois par jour.",
)
C_EFI75 = cite(
    "aips_59136.txt",
    "L'utilisation d' Efient n'est en général pas recommandée chez les patients de 75 ans et plus",
)
C_EFI60 = cite(
    "aips_59136.txt",
    "Au début du traitement, ces patients doivent recevoir une dose de charge unique de 60 mg de prasugrel et prendre ensuite 5 mg",
)
C_SORT = cite(
    "aips_54085.txt",
    "La dose initiale usuelle est de 10 mg d'atorvastatine 1x par jour.",
)
C_SORT80 = cite(
    "aips_54085.txt",
    "La dose journalière maximale est de 80 mg 1x par jour.",
)
C_MYO = cite(
    "aips_54085.txt",
    "La prise d'atorvastatine (comme la prise d'autres inhibiteurs de l'HMG CoA réductase) peut augmenter le risque de développer une myalgie, une myosite ou une myopathie.",
)
C_MYODEF = cite(
    "rms2020_myocardite.txt",
    "La myocardite est une inflammation du muscle cardiaque dont les étiologies sont variées, avec une prédominance d’atteinte infectieuse virale",
)
C_TN_N = cite(
    "rms2020_myocardite.txt",
    "Les troponines seront élevées en cas de myocardite aiguë, mais elles ne sont pas spécifiques et une troponine normale n’exclut par une myocardite chronique.",
)
C_EP = cite(
    "rms2009_ep.txt",
    "un taux élevé de troponine est associé à une plus forte mortalité (17,9% vs 2,3% ; OR 5,90)",
)
C_EP10 = cite(
    "rms2009_ep.txt",
    "Chez les patients hémodynamiquement stables mais ayant une dysfonction ventriculaire droite, la mortalité de l’embolie pulmonaire (EP) peut avoisiner les 10%.",
)
C_TAKO = cite(
    "rms2021_takotsubo.txt",
    "Le syndrome de Takotsubo représente 1 à 3 % des admissions pour infarctus du myocarde avec élévation du segment ST",
)
C_TAKO_TN = cite(
    "rms2021_takotsubo.txt",
    "les biomarqueurs cardiaques tels que la troponine sont la plupart du temps élevés, mais à des niveaux toutefois moins importants qu’en cas de SCA.",
)
C_RML = cite(
    "rms2020_rhabdomyolyse.txt",
    "Le diagnostic repose sur le dosage de la créatine kinase (CK).",
)
C_RML_S = cite(
    "rms2020_rhabdomyolyse.txt",
    "Il n’existe toutefois pas de consensus sur les valeurs seuil nettes définissant la RML.",
)
C_MECA = cite(
    "rms2019_troponine.txt",
    "l’élévation de la hs-cTn peut résulter de plusieurs mécanismes cellulaires : un stress mécanique de paroi",
    "une tachycardie",
)


def construire() -> str:
    sca = A("SCA", "syndrome coronarien aigu")
    ecg = A("ECG", "électrocardiogramme")
    ck = A("CK", "créatine kinase")
    irm = A("IRM", "imagerie par résonance magnétique")
    fevg = A("FEVG", "fraction d'éjection du ventricule gauche")
    aas = A("AAS", "acide acétylsalicylique")
    aips = A("AIPS", "information professionnelle suisse")
    irc = A("IRC", "insuffisance rénale chronique")
    ep = A("EP", "embolie pulmonaire")
    ic = A("IC", "insuffisance cardiaque")
    nyha = A("NYHA", "classification de la New York Heart Association")
    grace = A("GRACE", "Global Registry of Acute Coronary Events")
    icp = A("ICP", "intervention coronarienne percutanée")

    sous = (
        f"Situation de départ {A('F2.2', 'situation de départ F2.2 de PROFILES')} "
        f"« Enzymes cardiaques anormales » de {A('PROFILES', 'Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland')}."
        f" Le texte date du 31.10.2026. Les dix diagnostics sont une démarche d'exclusion, pas un classement de prévalence suisse."
    )

    ess = ilot(
        "ess",
        "c essentiel",
        "L'essentiel",
        P(
            f"Une enzyme cardiaque anormale, ou une troponine au-dessus de sa limite, nomme une lésion. Elle ne nomme pas la maladie.",
            f"{C_PAS_IM}{S(1)}",
            f"{C_TYPE1}{S(1)}",
        )
        + P(
            f"Le médecin lit l'{ecg} tout de suite, cherche une cinétique, et ne lance le traitement du {sca} que si l'ischémie est le diagnostic de travail.",
            f"Les doses écrites plus bas viennent de l'{aips}, numéros 51795, 61389, 54509, 59136 et 54085.",
        ),
    )

    som = ilot(
        "som",
        "v",
        "Sommaire",
        """<nav><ol class="som">
<li><a href="#p1">Définition</a></li>
<li><a href="#p2">Épidémiologie</a></li>
<li><a href="#p3">Physiopathologie</a></li>
<li><a href="#p4">Démarche diagnostique</a></li>
<li><a href="#p5">Anamnèse et drapeaux rouges</a></li>
<li><a href="#p6">Examen physique</a></li>
<li><a href="#p7">Approche syndromique</a></li>
<li><a href="#p8">Diagnostic positif</a></li>
<li><a href="#p9">Examens complémentaires</a></li>
<li><a href="#p10">Arbre décisionnel</a></li>
<li><a href="#p11">Prise en charge en Suisse</a></li>
<li><a href="#p12">Prévention</a></li>
<li><a href="#p13">Points clés</a></li>
<li><a href="#p14">Pièges d'examen</a></li>
</ol></nav>
<p class="sous">Les mots ⧉ ouvrent une fenêtre. Les sources sont à la fin.</p>""",
    )

    p1 = ilot(
        "p1",
        "c",
        "1. Définition",
        P(
            f"Le résultat anormal désigne d'abord la troponine, marqueur de souffrance du cardiomyocyte, et les enzymes historiques : {ck}, fraction MB, aspartate aminotransférase, lactate déshydrogénase.",
            f"La myoglobine n'est pas une enzyme. La troponine non plus.",
            b("w-termes", "le vocabulaire exact"),
            f"{S(1,3)}",
        )
        + P(
            f"{C_SPEC} {C_LESION}{S(1)}",
            f"La revue lausannoise et genevoise de 2016 place le même repère au 99e percentile, et donne 14 ng/l pour la troponine T ultrasensible de l'époque du texte.",
            f"{C_14}{S(3)}",
        )
        + fen(
            "w-termes",
            "Termes : enzyme, troponine, lésion, infarctus",
            P(f"{C_ORGANE}{S(1)}")
            + table(
                "Ce que le mot change au lit",
                ["Mot", "Sens retenu", "Conséquence"],
                [
                    ["Enzyme cardiaque", f"{ck}, fraction MB, aspartate aminotransférase, lactate déshydrogénase.", "Une {ck} isolée peut venir du muscle. Elle ne prouve pas l'infarctus.".format(ck=ck)],
                    ["Troponine I ou T", "Protéines du sarcomère, spécifiques du cardiomyocyte dans les revues lues.", "Au-dessus du 99e percentile : lésion myocardique, pas encore un infarctus."],
                    ["Lésion myocardique", "Valeur au-delà du 99e percentile, avec ou sans ischémie.", "On cherche la cinétique et la clinique avant de nommer un infarctus."],
                    ["Infarctus", "Lésion aiguë avec preuve d'ischémie.", "Le type 1 est athérothrombotique. Le type 2 est un déséquilibre sans athérothrombose."],
                    ["Élévation plate", "Variation faible, revue de 2019 : au plus 20 % dans le texte genevois.", "Penser à une cause chronique ou non ischémique, sans oublier le type 1 si la clinique est ischémique."],
                ],
            )
            + P(
                "La fraction MB a servi à rendre la créatine kinase plus cardiaque. Le muscle strié en contient un peu. Une rhabdomyolyse peut donc élever la créatine kinase totale, et parfois un peu la fraction MB, sans être un infarctus. Le cours ne donne pas de sensibilité chiffrée de cette fraction : aucune n'a été lue ici.",
            ),
        ),
    )

    p2 = ilot(
        "p2",
        "v",
        "2. Épidémiologie",
        P(
            f"Aucune des sources lues ne donne la part suisse de chacune des dix causes.",
            f"L'ordre du lot suit la démarche d'exclusion, pas une prévalence.",
            b("w-chiffres", "les seuls chiffres lus"),
            f"{S(1,5,6)}",
        )
        + fen(
            "w-chiffres",
            "Chiffres lus, et ce qu'ils ne disent pas",
            P(f"{C_PART} Ce pourcentage mélange des études. Il ne classe pas les dix diagnostics du lot.{S(1)}")
            + P(f"{C_33} Le mot secondaire, dans cet article, désigne une hausse hors infarctus de type 1 typique. Ce n'est pas un taux suisse.{S(1)}")
            + P(f"{C_IRC} {C_81}{S(3)}")
            + P(f"{C_EP10} {C_EP}{S(5)}")
            + P(f"{C_TAKO}{S(6)}")
            + P(
                "La myocardite de la revue 2020 n'a pas d'incidence suisse. Une série finlandaise y est citée : les hommes semblent plus touchés, âge médian 33 ans. Une série de 443 patients confirmés par imagerie ou biopsie compte plus de 25 % de formes compliquées à l'admission, et 3,2 % de décès ou transplantations pendant le séjour. Ces chiffres ne sont pas une prévalence aux urgences suisses."
                + S(4)
            )
            + P(
                "La rhabdomyolyse : l'incidence suisse exacte est inconnue dans la revue 2020. La mortalité d'effort y est dite faible, sous 2 %. Elle peut atteindre 60 % si l'origine est traumatique ou si plusieurs risques s'ajoutent, dont un pic très haut de créatine kinase. Le cours n'écrit pas ce pic avec l'abréviation d'unité, pour ne pas le faire passer pour une dose."
                + S(7)
            ),
        ),
    )

    p3 = ilot(
        "p3",
        "c",
        "3. Physiopathologie",
        P(
            "Le sarcomère règle la contraction par un complexe de troponines. Les formes I et T cardiaques quittent la cellule quand la membrane souffre.",
            b("w-bio", "le rappel biochimique"),
            b("w-meca", "cinq mécanismes de sortie"),
            f"{S(1,3)}",
        )
        + fen(
            "w-bio",
            "Rappel : sarcomère, troponine, créatine kinase",
            P(f"{C_SPEC}{S(1)}")
            + P(
                "Trois troponines existent : C, I et T. La revue de 2016 rappelle que I et T sont spécifiques du myocarde, et que les sociétés lues ne demandent pas de préférer l'une à l'autre pour reconnaître une souffrance. La troponine C est partagée avec le muscle. Ce n'est pas le dosage usuel."
                + S(3)
            )
            + P(
                "La créatine kinase catalyse le transfert d'un phosphate entre la phosphocréatine et l'adénosine diphosphate. Elle est abondante dans le muscle strié, le myocarde et le cerveau. Une hausse totale dit qu'un de ces tissus a souffert. Elle ne dit pas lequel. L'aspartate aminotransférase et la lactate déshydrogénase sont encore moins spécifiques : foie, muscle, hémolyse et myocarde les élèvent."
            )
            + P(
                "Le 99e percentile se calcule dans une population de référence saine, pour le dosage utilisé. Changer de réactif change le chiffre. La troponine I n'a pas, dans la revue de 2016, une limite unique. Le cours n'en invente pas."
                + S(3)
            )
            + fen(
                "w-schema",
                "Schéma : de la membrane à la veine",
                """<figure class="schema"><svg viewBox="0 0 360 160" role="img" aria-label="Schéma simplifié de la sortie de la troponine du cardiomyocyte">
<rect x="20" y="30" width="140" height="90" rx="8" fill="none" stroke="currentColor"/>
<text x="90" y="55" text-anchor="middle" font-size="12" fill="currentColor">Cardiomyocyte</text>
<text x="90" y="78" text-anchor="middle" font-size="11" fill="currentColor">troponine I et T</text>
<text x="90" y="98" text-anchor="middle" font-size="11" fill="currentColor">créatine kinase</text>
<path d="M160 75 H230" stroke="currentColor" marker-end="url(#fl150)"/>
<rect x="230" y="45" width="110" height="60" rx="8" fill="none" stroke="currentColor"/>
<text x="285" y="80" text-anchor="middle" font-size="12" fill="currentColor">Sang veineux</text>
<defs><marker id="fl150" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker></defs>
</svg><figcaption>La sortie vers le sang signe une lésion du cardiomyocyte ou, pour la créatine kinase totale, d'un muscle. Elle ne nomme pas la cause.</figcaption></figure>""",
                sous=True,
            )
            + P("Le " + b("w-schema", "schéma") + " reste volontairement simple. Il ne remplace pas la cinétique."),
        )
        + fen(
            "w-meca",
            "Mécanismes lus en 2019",
            P(f"{C_MECA}{S(1)}")
            + P(
                "Traduction clinique. Un stress de paroi libère de la troponine dans l'insuffisance cardiaque et dans la surcharge de pression ou de volume. Une tachycardie agit sur les intégrines. Les catécholamines montent dans le tako-tsubo et dans certains accidents vasculaires cérébraux. Les motifs associés aux pathogènes et les lipopolysaccharides agissent dans le sepsis. La myocardite détruit des cellules par inflammation, virale, bactérienne ou immune."
                + S(1)
            )
            + P(
                f"Le type 2 est autre chose : il y a une ischémie, mais pas d'athérothrombose aiguë. {C_TYPE2}{S(1)} L'anémie, le monoxyde de carbone, le spasme, l'embolie coronarienne, la dissection coronarienne et une sténose stable face à une demande accrue sont des exemples écrits dans le même article."
            ),
        ),
    )

    p4 = ilot(
        "p4",
        "v",
        "4. Démarche diagnostique",
        P(
            "On exclut d'abord l'infarctus de type 1, y compris celui qui sus-décalle le segment ST.",
            "Ensuite on sépare le type 2, puis les lésions sans ischémie.",
            b("w-dix", "les dix diagnostics du lot"),
            f"{S(1)}",
        )
        + fen(
            "w-dix",
            "Dix concurrents, gravité d'exclusion, pas une prévalence",
            table(
                "Liste du lot. E1 s'exclut en premier.",
                ["Rang d'exclusion", "Diagnostic", "Ce qui l'évoque devant le résultat"],
                [
                    ["E1", "Infarctus du myocarde de type 1", "Douleur ischémique, sus-décalage, ou cinétique avec athérothrombose probable."],
                    ["E2", "Dissection aortique aiguë", "Douleur déchirante, asymétrie tensionnelle, trouble neurologique. La troponine n'écarte pas."],
                    ["E3", "Embolie pulmonaire", "Dyspnée, facteur de risque veineux, cœur droit."],
                    ["E4", "Myocardite", "Douleur, infection récente, trouble du rythme, âge souvent jeune. Coronaire à écarter si le risque existe."],
                    ["E5", "Infarctus du myocarde de type 2", "Choc, saignement, anémie, tachycardie, hypoxie, sans athérothrombose comme moteur."],
                    ["E6", "Syndrome de tako-tsubo", "Stress, sus-décalage, troponine souvent plus basse que l'infarctus, coronaire sans occlusion coupable."],
                    ["E7", "Lésion myocardique du sepsis", "Infection grave, motifs bactériens, hypoxie ou hypotension souvent associées."],
                    ["E8", "Insuffisance cardiaque aiguë", "Surcharge, tension de paroi. La troponine peut monter sans occlusion aiguë."],
                    ["E9", "Rhabdomyolyse", "Myalgies, urines foncées, créatine kinase haute, troponine souvent non concernée."],
                    ["E10", "Lésion myocardique de la maladie rénale chronique", "Valeur déjà haute, cinétique plate, risque malgré tout."],
                ],
            )
            + P(
                "Le rang E n'est pas la fréquence. La revue de 2019 demande d'écarter le type 1 en premier. La dissection passe juste après parce qu'une troponine positive ne doit pas endormir la recherche, comme le rappelle le rôle de l'échocardiographie en 2016 quand l'infarctus sans sus-décalage reste douteux."
                + S(1, 3)
            )
            + cahier_html(),
        ),
    )

    p5 = ilot(
        "p5",
        "c",
        "5. Anamnèse et drapeaux rouges",
        P(
            "On date le début, le siège, l'effort, le repos, la dyspnée, la syncope, le trauma, l'infection, les urines et les médicaments.",
            b("w-drapeaux", "drapeaux qui ne peuvent pas attendre"),
        )
        + fen(
            "w-drapeaux",
            "Drapeaux rouges",
            table(
                "Ce que l'anamnèse change",
                ["Élément", "Piste", "Geste immédiat"],
                [
                    ["Douleur constrictive, sueurs, irradiation", "Type 1 jusqu'à preuve contraire.", "ECG sans délai. Ne pas attendre la troponine si le sus-décalage est déjà là."],
                    ["Douleur déchirante vers le dos, déficit, pouls asymétriques", "Dissection aortique aiguë.", "Ne pas traiter comme un infarctus banal. La troponine peut être haute."],
                    ["Dyspnée, immobilisation, cancer, jambe gonflée", "Embolie pulmonaire.", "Instabilité : réanimation. Stabilité : stratification, dont la troponine comme marqueur de gravité."],
                    ["Choc, hémorragie, hypoxie, tachycardie longue", "Type 2.", "Corriger le moteur du déséquilibre en même temps que l'on cherche une coronaire."],
                    ["Infection virale, douleur pleurétique, sujet jeune", "Myocardite.", "Hospitaliser si la forme est aiguë. Écarter une coronaire si les facteurs de risque existent."],
                    ["Stress intense, sus-décalage, femme âgée possible", "Tako-tsubo.", "Même circuit que l'infarctus tant que l'occlusion n'est pas écartée."],
                    ["Myalgies, effort inhabituel, statine, crush", "Rhabdomyolyse.", "Créatine kinase, potassium, créatinine. Ne pas conclure à un infarctus sur la seule enzyme musculaire."],
                    ["Rein connu, valeur ancienne déjà haute", "Lésion chronique.", "Comparer. Une cinétique plate n'autorise pas à ignorer une douleur ischémique."],
                ],
            ),
        ),
    )

    p6 = ilot(
        "p6",
        "v",
        "6. Examen physique",
        P(
            "Les signes vitaux passent avant le laboratoire.",
            "On ausculte, on compare les pouls et les tensions, on regarde les jambes et les muscles.",
            b("w-exam", "fenêtres d'examen"),
        )
        + fen(
            "w-exam",
            "Examen : ce que chaque geste cherche",
            P("Tension aux deux bras et pouls. Une asymétrie oriente vers la dissection. Elle ne la prouve pas à elle seule.")
            + P("Poumons. Des crépitants et une désaturation vont avec l'œdème, l'infarctus compliqué ou l'embolie grave. Un murmure unilatéral absent fait chercher un pneumothorax, qui n'est pas une enzyme cardiaque, mais qui tue aussi.")
            + P("Cœur. Un souffle nouveau peut être une complication mécanique ou une valve qui a précipité un type 2. Un frottement oriente vers le péricarde, souvent avec un peu de muscle : myopéricardite.")
            + P("Jambes. Un mollet tendu, une douleur à la dorsiflexion, une immobilisation récente pèsent pour l'embolie. Leur absence ne l'écarte pas.")
            + P("Muscles. Un œdème douloureux des loges, des urines brunes, un effort récent : créatine kinase, pas seulement troponine.")
            + P("Abdomen. Une douleur épigastrique reproductible n'innocente pas le cœur. La vignette genevoise de 2016 commence par un épigastre et une troponine haute, puis finit par une cholécystite, avec une valeur stable." + S(3))
            + P("Neurologie. Un déficit au moment d'une douleur thoracique fait chercher la dissection et l'accident vasculaire, deux situations où la troponine peut monter."),
        ),
    )

    p7 = ilot(
        "p7",
        "c",
        "7. Approche syndromique",
        P(
            "Quatre tableaux suffisent à ne pas mélanger les réponses.",
            b("w-synd", "les quatre tableaux"),
        )
        + fen(
            "w-synd",
            "Quatre syndromes devant un résultat anormal",
            table(
                "Syndrome et premier réflexe",
                ["Tableau", "Lecture", "Réflexe"],
                [
                    ["Sus-décalage et douleur", "Infarctus de type 1 jusqu'à preuve angiographique, ou tako-tsubo, ou myocardite, ou dissection.", "Salle de cathétérisme sans attendre le deuxième dosage."],
                    ["Douleur sans sus-décalage", "Algorithme de troponine du laboratoire, voie d'observation si le couple de valeurs ne tranche pas.", "ECG répétés. Échocardiographie si le diagnostic reste trouble."],
                    ["Valeur haute, patient calme, rein ou cœur connus", "Lésion chronique possible.", "Comparer à une ancienne valeur. Ne pas banaliser si la douleur est nouvelle."],
                    ["Créatine kinase haute, troponine non demandée ou basse, muscles douloureux", "Rhabdomyolyse ou autre muscle.", "Potassium, rein, débit urinaire. Ne pas ouvrir un protocole coronarien sur la seule enzyme."],
                ],
            ),
        ),
    )

    p8 = ilot(
        "p8",
        "v",
        "8. Diagnostic positif",
        P(
            "Le diagnostic positif de cette situation de départ est le résultat lui-même, interprété avec la limite du dosage du laboratoire.",
            "Le diagnostic de la maladie vient ensuite.",
            b("w-pos", "ce qui affirme, ce qui n'affirme pas"),
            f"{S(1,3)}",
        )
        + fen(
            "w-pos",
            "Affirmer la lésion, ne pas affirmer trop tôt la cause",
            P(f"{C_URL}{S(3)} {C_LESION}{S(1)}")
            + P(
                "Une seule valeur au-dessus de la limite affirme la lésion. Elle n'affirme l'infarctus que s'il existe une preuve d'ischémie et, hors sus-décalage déjà décisif, une cinétique. La revue de 2019 décrit une montée puis une descente pour l'événement aigu, et une courbe plate, variation d'au plus 20 %, pour l'élévation chronique ou non ischémique."
                + S(1)
            )
            + P(
                "Pour la troponine T ultrasensible, la revue de 2016 retient comme cinétique significative un changement de 50 % de la limite, soit 7 ng/l en valeur absolue dans ce texte, et elle discute un changement relatif de plus de 20 % quand toutes les valeurs sont déjà positives chez l'insuffisant rénal. Ces repères sont ceux de 2016. L'algorithme actuel dépend du coffret utilisé. Les seuils en ng/l de l'algorithme à une heure ne sont pas recopiés ici."
                + S(3)
            ),
        ),
    )

    p9 = ilot(
        "p9",
        "c",
        "9. Examens complémentaires",
        P(
            f"L'{ecg} et la troponine du laboratoire central viennent en premier chez le patient suspect de {sca} sans sus-décalage.",
            b("w-ecg", "électrocardiogramme"),
            b("w-labo", "cinétique de laboratoire"),
            b("w-echo", "échocardiographie"),
            b("w-image", "scanner et coronarographie"),
            f"{S(2,3)}",
        )
        + fen(
            "w-ecg",
            "Électrocardiogramme : principe et limites",
            P("Principe. Douze dérivations, comparées à un tracé ancien si l'on en a un. On cherche un sus-décalage, un sous-décalage, une onde T négative, un bloc nouveau, une arythmie.")
            + P("Interprétation. Un sus-décalage avec douleur ouvre la coronarographie immédiate, selon la revue genevoise des recommandations européennes de 2023. On ne dose pas une deuxième troponine pour « confirmer » avant de partir." + S(2))
            + P("Ce qu'il ne fait pas. Un tracé normal n'écarte ni l'infarctus précoce, ni l'embolie, ni la dissection. On le répète si la douleur continue.")
            + P(f"La vignette de 2016 montre des sous-décalages de 1 à 2 mm et des ondes T négatives de V3 à V6, avec une troponine T à 73 ng/l pour une limite de 14 ng/l, chez un patient dont la coronaire était ensuite sans lésion significative et dont la valeur restait stable. L'{ecg} inquiétant n'était pas un infarctus.{S(3)}"),
        )
        + fen(
            "w-labo",
            "Laboratoire : troponine, créatine kinase, reste du bilan",
            P(f"{C_ALGO}{S(2)}")
            + P(f"{C_POC}{S(2)}")
            + P(
                "La voie d'observation reçoit ceux qui ne sont ni exclus ni inclus. Une troisième mesure à 3 heures, et une échocardiographie si besoin, font partie du texte genevois de 2024."
                + S(2)
            )
            + P(
                f"Créatine kinase. Elle sert quand le muscle est en cause, et comme contexte d'une statine. Elle ne remplace pas la troponine pour l'infarctus. {C_RML} {C_RML_S}{S(7)}"
            )
            + P(
                "Autour : créatinine et potassium, hémoglobine, saturation ou gaz si la dyspnée domine, peptide natriurétique si l'insuffisance cardiaque est la question. La revue de myocardite 2020 ajoute la protéine C réactive et, si l'allergie est plausible, les éosinophiles."
                + S(4)
            ),
        )
        + fen(
            "w-echo",
            "Échocardiographie",
            P(f"{C_ECHO}{S(3)}")
            + P(
                "Principe. Elle montre la contraction segmentaire, la fraction d'éjection, le péricarde, le cœur droit, la valve aortique et parfois un flap si la fenêtre est favorable."
            )
            + P(
                "Interprétation. Un trouble segmentaire nouveau va avec l'ischémie, mais la myocardite et le tako-tsubo en font aussi. Un cœur droit dilaté, avec la clinique, va avec l'embolie. Un épanchement va avec la péricardite. Rien de tout cela ne remplace la coronarographie si le sus-décalage ou l'instabilité l'exigent."
            ),
        )
        + fen(
            "w-image",
            "Scanner coronaire et coronarographie",
            P(
                "La revue de 2024 reclasse le scanner coronaire, chez le patient suspect sans sus-décalage, d'une classe I vers une classe IIa. Les études citées n'ont pas montré de gain clair sur le séjour, les examens d'aval, le coût ou le résultat clinique."
                + S(2)
            )
            + P(f"{C_STEMI} {C_DELAI}{S(2)}")
            + P(f"{C_120} Le cours n'écrit aucune dose de fibrinolytique : aucune information professionnelle de ce médicament n'a été relue.{S(2)}")
            + P(f"{C_24} Le haut risque, dans ce texte, inclut un {grace} au-dessus de 140, un infarctus sans sus-décalage avéré, ou des modifications dynamiques de l'{ecg}.{S(2)}")
            + P(f"Très haut risque : instabilité, douleur réfractaire, insuffisance cardiaque ischémique en cours, arythmie menaçante, arrêt, complication mécanique, changements électriques récurrents. Coronarographie immédiate.{S(2)}")
            + P(f"{C_CHOC} C'est la leçon de l'étude citée par la revue pour le choc.{S(2)}")
            + P(f"{C_ARRET} Cette phrase vise le patient stable, sans sus-décalage persistant.{S(2)}"),
        ),
    )

    p10 = ilot(
        "p10",
        "v",
        "10. Arbre décisionnel",
        P(
            "L'arbre commence par ce qui tue si on le rate, pas par la cause la plus fréquente.",
            b("w-arbre", "les pas"),
        )
        + fen(
            "w-arbre",
            "Arbre",
            """<ol class="algo">
<li>Voie veineuse, surveillance, électrocardiogramme. Si sus-décalage et clinique compatible : filière d'infarctus de type 1, coronarographie immédiate. Ne pas attendre une deuxième troponine.</li>
<li>Douleur déchirante, déficit, asymétrie des pouls : dissection aortique aiguë en parallèle. Une troponine haute ne ferme pas cette piste.</li>
<li>Instabilité et dyspnée sans sus-décalage : embolie pulmonaire et choc du type 2 restent ouverts pendant que l'ischémie est cherchée.</li>
<li>Patient stable, sans sus-décalage : algorithme de troponine du laboratoire central, à 0 puis 1 heure, ou à 0 puis 2 heures si la première cadence est impossible.</li>
<li>Ni exclusion ni inclusion : troisième dosage vers 3 heures, échocardiographie si le diagnostic reste trouble.</li>
<li>Cinétique plate et clinique non ischémique : myocardite, tako-tsubo, sepsis, insuffisance cardiaque, rein chronique, selon le tableau. Le type 1 reste exclu par la clinique, pas par habitude.</li>
<li>Créatine kinase seule, muscles, urines foncées : rhabdomyolyse. Potassium et rein.</li>
</ol>"""
            + P(f"{C_TYPE1}{S(1)}"),
        ),
    )

    p11 = ilot(
        "p11",
        "c",
        "11. Prise en charge en Suisse",
        P(
            f"Le geste dépend de la cause. On ne donne pas l'aspirine d'un infarctus à une dissection non reconnue, ni à une rhabdomyolyse.",
            f"Quand l'infarctus aigu est le diagnostic, l'{aips} d'Aspirine Cardio, numéro 51795, écrit la dose.",
            b("w-doses", "doses lues mot pour mot"),
            b("w-suite", "ce que la revue 2024 ajoute sans milligramme nouveau"),
        )
        + fen(
            "w-doses",
            "Informations professionnelles lues le 31.10.2026",
            P(f"Aspirine Cardio, n° 51795. {C_ASA} {C_ASA2}{S(8)}")
            + P(
                f"Les comprimés gastro-résistants ne sont pas la forme à résorption rapide du premier jour. {C_ASA18}{S(8)} Contre-indications lues : ulcère ou saignement digestif actif, maladie inflammatoire intestinale, insuffisance rénale sévère avec clairance de la créatinine inférieure à 30 ml/min, insuffisance cardiaque sévère {nyha} III-IV, troisième trimestre de grossesse, méthotrexate à 15 mg par semaine ou plus, diathèse hémorragique."
            )
            + P(f"BRILIQUE, ticagrélor, n° 61389. {C_BRI} Le même texte demande une faible dose quotidienne d'aspirine, 75 à 150 mg, sauf contre-indication, et une durée d'au moins 12 mois sauf raison clinique d'arrêt.{S(9)}")
            + P(f"{C_BRI_G} {C_BRI_A}{S(9)} Contre-indications lues : saignement pathologique en cours, antécédent d'hémorragie intracrânienne, insuffisance hépatique sévère.")
            + P(f"Plavix, clopidogrel, n° 54509. Pour le syndrome coronaire aigu sans sus-décalage du segment ST, {C_PLAV} L'association à l'aspirine, dans cette phrase, va de 75 mg à 325 mg par jour.{S(10)}")
            + P(
                "Grossesse : le texte dit qu'il n'y a pas d'étude spécifique contrôlée chez la femme enceinte, et que le clopidogrel n'est donné pendant la grossesse que si l'indication est indispensable. Aucun ajustement n'est écrit pour le sujet âgé. Sous 18 ans, tolérance et efficacité non démontrées."
                + S(10)
            )
            + P(f"EFIENT, prasugrel, n° 59136. {C_EFI} Une aspirine de 75 mg à 325 mg une fois par jour est associée dans le même texte. La poursuite conseillée est de 15 mois, sauf nécessité clinique d'arrêt.{S(11)}")
            + P(f"{C_EFI75} S'il est malgré tout jugé nécessaire, la poursuite lue est de 5 mg une fois par jour après la charge de 60 mg. {C_EFI60} Cette phrase vise le poids sous 60 kg. Pour un angor instable ou un infarctus sans sus-décalage, si la coronarographie est prévue dans les 48 heures, la charge se donne au moment de l'{icp}, pas avant.{S(11)}")
            + P(
                "La revue genevoise de 2024 ne recommande pas le prétraitement par inhibiteur du récepteur avant la coronarographie dans le syndrome sans sus-décalage, et elle ne fait du prétraitement avant l'angioplastie primaire qu'une considération de classe IIb. L'information professionnelle du ticagrélor, elle, demande la charge dès que possible. Les deux textes sont lus. Le cours ne fabrique pas le protocole d'un hôpital."
                + S(2, 9)
            )
            + P(f"Sortis, atorvastatine, n° 54085. {C_SORT} {C_SORT80} Le produit n'est pas autorisé chez l'enfant et l'adolescent. La grossesse et l'allaitement figurent aux contre-indications. {C_MYO} De rares rhabdomyolyses sont écrites dans la même rubrique. Une douleur musculaire avec fièvre ou épuisement doit faire revoir le traitement.{S(12)}"),
        )
        + fen(
            "w-suite",
            "Conduite lue sans nouvelle dose",
            P(
                "Double antiagrégation d'un an puis aspirine seule : stratégie par défaut après angioplastie dans la revue 2024. Une désescalade les 30 premiers jours n'est pas recommandée. Une monothérapie après 3 à 6 mois doit être considérée chez certains patients sans événement et sans haut risque ischémique. Le prasugrel est préféré au ticagrélor, classe IIa, dans cette revue."
                + S(2)
            )
            + P(
                "Hypolipémiant : intensifier pendant le séjour si le patient en prenait déjà, classe I. L'association statine intense et ézétimibe peut être considérée, classe IIb. Le cours ne recopie pas de milligramme d'ézétimibe."
                + S(2)
            )
            + P(
                "Réhabilitation, arrêt du tabac, activité, facteurs de risque : la figure genevoise les place après la phase aiguë. Aucun programme chiffré suisse n'est recopié."
                + S(2)
            )
            + P(
                f"Héparine, énoxaparine, fondaparinux : aucun schéma propre au {sca} n'est écrit dans cette leçon. Les unités lues pour l'héparine Bichsel concernent d'autres indications. Les milligrammes n'ont pas été recopiés."
            ),
        ),
    )

    p12 = ilot(
        "p12",
        "v",
        "12. Prévention",
        P(
            "On ne dépiste pas la troponine chez une personne sans symptôme pour « voir le cœur ».",
            "Après un événement, la prévention est celle de la cause retenue.",
            b("w-prev", "ce qui est écrit"),
        )
        + fen(
            "w-prev",
            "Prévention selon la cause, pas selon le chiffre seul",
            P("Infarctus de type 1 : antiagrégation selon l'information professionnelle, statine, réhabilitation, tabac, tension, comme la revue 2024 le cadre. Le détail des doses est au point 11." + S(2))
            + P("Type 2 : prévenir, c'est traiter le moteur. Anémie, hypoxie, tachycardie, valve, saignement. Une statine ne corrige pas une hémorragie.")
            + P("Myocardite aiguë : la revue 2020 hospitalise, surveille le rythme et l'insuffisance cardiaque, et écarte l'effort. Pour la myopéricardite, l'éviction lue est plus longue que pour une péricardite isolée, six mois dans ce texte." + S(4))
            + P("Rhabdomyolyse : éviter le nouvel effort tant que la créatine kinase n'est pas redevenue normale, revoir une statine si elle est en cause, hydrater tôt. Les débits en millilitres par heure de la revue 2020 ne sont pas recopiés dans la leçon.")
            + P(f"{irc} : une troponine chronique élevée annonce un risque, y compris hors syndrome coronarien. La revue de 2016 dit que la prise en charge standardisée de ce seul fait n'est pas encore définie. On ne crée pas un protocole de dépistage." + S(3)),
        ),
    )

    p13 = ilot(
        "p13",
        "c",
        "13. Points clés",
        P("La troponine est spécifique d'organe, pas d'une maladie. L'infarctus de type 1 s'exclut en premier.")
        + P("Le sus-décalage ne se confirme pas par un deuxième tube. La valeur plate ne se traite pas comme une occlusion.")
        + P("La créatine kinase haute avec des muscles douloureux est une rhabdomyolyse jusqu'à preuve du contraire, pas un infarctus par défaut.")
        + P(f"Toute dose de ce cours est une phrase d'{aips}. Le rein chronique élève souvent la troponine T. Il n'explique pas à lui seul une douleur ischémique."),
    )

    p14 = ilot(
        "p14",
        "v",
        "14. Pièges d'examen",
        P("Les pièges tiennent dans une fenêtre. Chaque question a sa réponse sous le titre.")
        + fen(
            "w-pieges",
            "Pièges d'examen",
            """<details class="quiz"><summary>Une troponine au-dessus de la limite est-elle un infarctus ?</summary>
<p>Non. C'est une lésion. L'infarctus demande une ischémie. La revue genevoise de 2019 le dit dans ses implications.</p></details>
<details class="quiz"><summary>Par quoi commence l'exclusion ?</summary>
<p>Par l'infarctus de type 1, y compris celui qui sus-décalle. Ce n'est pas par la cause statistiquement la plus fréquente, qui n'a pas été lue pour la Suisse.</p></details>
<details class="quiz"><summary>Peut-on attendre la troponine devant un sus-décalage ?</summary>
<p>Non. La coronarographie est immédiate. Le délai lu est de 60 minutes dans un centre équipé, et de moins de 90 minutes si le patient vient d'un autre centre.</p></details>
<details class="quiz"><summary>Le comprimé gastro-résistant est-il la dose de la première heure ?</summary>
<p>Non. L'information professionnelle n° 51795 demande, pour l'infarctus aigu, une voie intraveineuse ou une forme orale à résorption rapide, non gastro-résistante. Aspirine Cardio à 100 mg vient à partir du deuxième jour.</p></details>
<details class="quiz"><summary>Une valeur stable chez un insuffisant rénal est-elle toujours bénigne ?</summary>
<p>Non. La revue de 2016 refuse de la banaliser. Elle peut rester un marqueur de risque, et une vraie ischémie peut s'y ajouter.</p></details>
<details class="quiz"><summary>La créatine kinase MB prouve-t-elle l'infarctus ?</summary>
<p>Non. Le muscle en contient. Aucune sensibilité chiffrée n'est enseignée ici, parce qu'aucune n'a été lue.</p></details>
<details class="quiz"><summary>L'embolie pulmonaire élève-t-elle la troponine ?</summary>
<p>Oui, souvent par souffrance du ventricule droit. Dans la méta-analyse citée en 2009, la mortalité était plus haute si la troponine était haute. Ce n'est pas une raison pour oublier l'infarctus si l'électrocardiogramme le montre.</p></details>
<details class="quiz"><summary>Le tako-tsubo se traite-t-il comme bénin parce que la troponine est « trop basse » ?</summary>
<p>Non. Il imite l'infarctus, peut choquer, et ne se distingue qu'après avoir écarté l'occlusion. La troponine y est souvent moins haute, pas toujours rassurante.</p></details>""",
        )
        + P(b("w-pieges", "Ouvrir les huit pièges")),
    )

    sources = ilot(
        "sources",
        "c",
        "Sources",
        """<ol class="sources">
<li>Von Düring et al., Revue Médicale Suisse 2019, n° 652.</li>
<li>Planchat et al., Revue Médicale Suisse 2024, n° 875. Recommandations européennes 2023.</li>
<li>Kolb et al., Revue Médicale Suisse 2016, n° 535.</li>
<li>Revue Médicale Suisse 2020, n° 696, myocardite.</li>
<li>Blaudszun et al., Revue Médicale Suisse 2009, n° 221.</li>
<li>Revue Médicale Suisse 2021, n° 728, tako-tsubo.</li>
<li>Revue Médicale Suisse 2020, n° 716, rhabdomyolyse.</li>
<li>AIPS Aspirine Cardio, n° 51795.</li>
<li>AIPS BRILIQUE, n° 61389.</li>
<li>AIPS Plavix, n° 54509.</li>
<li>AIPS EFIENT, n° 59136.</li>
<li>AIPS Sortis, n° 54085.</li>
</ol>
<p>Extraits datés dans le dossier evidence. Les trous sont dans INCERTITUDES.md, pas dans les îlots.</p>""",
    )

    blocs = [ess, som, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, sources]
    return page(
        "LOT_150_Phase_A_V0.html",
        "Enzymes cardiaques anormales",
        sous,
        blocs,
    )


if __name__ == "__main__":
    OUT.write_text(construire(), encoding="utf-8")
    print("écrit", OUT, OUT.stat().st_size)
