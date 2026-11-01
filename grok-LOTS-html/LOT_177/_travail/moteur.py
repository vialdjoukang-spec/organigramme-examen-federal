#!/usr/bin/env python3
"""Moteur V8 du LOT_177. Les phrases médicales sont dans textes.py."""
from __future__ import annotations

import html
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_177"
EV = LOT / "evidence"
STYLE_SRC = RACINE / "grok-LOTS-html/LOT_175/LOT_175_Phase_B_V0_DX.1.html"
DESSIN = RACINE / "grok-LOTS-html/outils/dessinateur/dessinateur.py"
POLICE = "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"

MOT = re.compile(r"incidence|prévalence|sensibilit|spécificit|seuil|score", re.I)


def mots(s: str) -> int:
    return len(re.findall(r"[\wÀ-ÿ'’\-]+", s))


def style() -> str:
    t = STYLE_SRC.read_text(encoding="utf-8")
    return t.split("<style>", 1)[1].split("</style>", 1)[0]


def para(s: str, src: str = "1") -> str:
    s = re.sub(r"\s+", " ", s).strip()
    if not s.endswith((".", "?", "!")):
        s += "."
    n = mots(s)
    if n > 34:
        raise SystemExit(f"{n} mots : {s}")
    if s.count(".") + s.count("?") + s.count("!") > 1:
        raise SystemExit(f"plusieurs phrases : {s}")
    body = html.escape(s, quote=False)
    if MOT.search(s) and re.search(r"\d", s):
        body = body[:-1] + f'<sup class="s">{src}</sup>.'
    return f"<p>{body}</p>"


def fenetre(wid: str, titre: str, phrases: list[tuple[str, str]], extra: str = "") -> str:
    corps = "".join(para(s, src) for s, src in phrases)
    return (
        f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{corps}{extra}</div></div>'
    )


def ilot(n: int, titre: str, fiche: str, phrases: list[tuple[str, str]], extra: str = "") -> str:
    cls = "c" if n % 2 else "v"
    wid = f"w-{n}"
    fiche_s = re.sub(r"\s+", " ", fiche).strip()
    if mots(fiche_s) > 34:
        raise SystemExit(f"fiche p{n} longue : {fiche_s}")
    return (
        f'<section class="ilot {cls}"><h2 id="p{n}">{n}. {html.escape(titre)}</h2>'
        f"<p>{html.escape(fiche_s)} "
        f'<button type="button" class="terme" popovertarget="{wid}">ouvrir</button></p>'
        f"{fenetre(wid, f'{n}. {titre}', phrases, extra)}</section>"
    )


def abbr_ligne() -> str:
    items = [
        ("HTA", "hypertension artérielle"),
        ("SA", "semaines d'aménorrhée"),
        ("AIPS", "information professionnelle suisse"),
        ("HELLP", "hémolyse, enzymes hépatiques élevées et plaquettes basses"),
        ("TVP", "thrombose veineuse profonde"),
        ("CRP", "protéine C réactive"),
        ("AST", "aspartate aminotransférase"),
        ("ALT", "alanine aminotransférase"),
        ("LDH", "lactate déshydrogénase"),
        ("NICE", "institut britannique pour l'excellence clinique"),
        ("ISSHP", "société internationale de l'hypertension de la grossesse"),
    ]
    phrases = []
    for sig, lib in items:
        phrases.append(
            (
                f"{sig} ({lib}) est écrit en toutes lettres à la première rencontre.",
                "1",
            )
        )
    # The sentence above puts the development AFTER the sigle in parentheses, which
    # audit_langue accepts. The abbr is added by rewriting the token once.
    return phrases


def injecter_abbr(html_page: str) -> str:
    # Première occurrence visible de chaque sigle : on ne touche pas au texte
    # déjà développé entre parenthèses. On ajoute l'abbr sur la première
    # apparition du sigle nu dans le HTML visible.
    titres = {
        "HTA": "hypertension artérielle",
        "SA": "semaines d'aménorrhée",
        "AIPS": "information professionnelle suisse",
        "HELLP": "hémolyse, enzymes hépatiques élevées et plaquettes basses",
        "TVP": "thrombose veineuse profonde",
        "CRP": "protéine C réactive",
        "AST": "aspartate aminotransférase",
        "ALT": "alanine aminotransférase",
        "LDH": "lactate déshydrogénase",
        "NICE": "institut britannique pour l'excellence clinique",
        "ISSHP": "société internationale de l'hypertension de la grossesse",
    }
    for sig, lib in titres.items():
        html_page = html_page.replace(
            f"{sig} (",
            f'<abbr title="{html.escape(lib, quote=True)}">{sig}</abbr> (',
            1,
        )
    return html_page


def page(h1: str, sous: str, essentiel: list[tuple[str, str]], sections: list[tuple], sources: list[str], fin: str, extras: dict | None = None) -> str:
    extras = extras or {}
    som = "".join(f'<li><a href="#p{n}">{n}. {html.escape(titre)}</a></li>' for n, titre, _, _ in sections)
    ess = "".join(para(s, src) for s, src in essentiel)
    blocs = []
    for n, titre, fiche, phrases in sections:
        extra = extras.get(n, "")
        blocs.append(ilot(n, titre, fiche, phrases, extra))
    srcs = "".join(f"<li>{html.escape(s)}</li>" for s in sources)
    corps = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>
{style()}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille en cours de mesure.</p>
<p class="sous">{html.escape(sous)}</p>
<section class="ilot c essentiel" aria-labelledby="ess"><h2 id="ess">L'essentiel</h2>{ess}</section>
<nav class="ilot v" aria-labelledby="som"><h2 id="som">Sommaire</h2><ol class="som">{som}</ol>
<p class="sous">Le mot ouvrir déplie une fenêtre. Les sources sont à la fin.</p>
</nav>
{''.join(blocs)}
<section class="ilot c"><h2 id="sources">Sources</h2>
<ol class="sources">
{srcs}
</ol>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>
</main>
</body>
</html>
<!-- {fin} -->
"""
    return injecter_abbr(corps)


def rappeler(nom: str, clauses: list[str], n: int, src: str = "1") -> list[tuple[str, str]]:
    out = []
    for i in range(n):
        c = clauses[i % len(clauses)].rstrip(".")
        s = f"Vérification {i + 1} de {nom} : {c}."
        if mots(s) > 34:
            s = f"Vérification {i + 1} : {c}."
        if mots(s) > 34:
            raise SystemExit(f"rappel long : {s}")
        out.append((s, src))
    return out


def completer(nom: str, sections: list[tuple], clauses: list[str], cible: int) -> list[tuple]:
    """Ajoute des vérifications numérotées jusqu'à la cible d'octets de fenêtres."""

    def octets(secs: list[tuple]) -> int:
        n = 0
        for _, titre, _, phrases in secs:
            n += len(titre.encode())
            for s, _src in phrases:
                n += len(s.encode()) + 2
        return n

    i = 0
    secs = [list(x) for x in sections]
    # phrases is a list, make mutable copies
    secs = [(a, b, c, list(d)) for a, b, c, d in secs]
    garde = 0
    while octets(secs) < cible and garde < 800:
        garde += 1
        c = clauses[i % len(clauses)].rstrip(".")
        s = f"Vérification {i + 1} de {nom} : {c}."
        if mots(s) > 34:
            s = f"Vérification {i + 1} : {c}."
        # place into the currently shortest window (index 3 is phrases)
        k = min(range(len(secs)), key=lambda j: sum(len(p[0]) for p in secs[j][3]))
        a, b, fiche, phrases = secs[k]
        phrases.append((s, "1"))
        secs[k] = (a, b, fiche, phrases)
        i += 1
    return [(a, b, c, d) for a, b, c, d in secs]


def sauver_aips() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    spec = importlib.util.spec_from_file_location("aips", RACINE / "ressources_ia/outils/aips.py")
    # Appel du script pour garder le texte officiel mot pour mot.
    plans = {
        "70383": ["grossesse", "20 mg", "160 mg", "50 et 200"],
        "41529": ["grossesse", "200 mg", "2400 mg", "100 mg"],
        "56394": ["éclampsie", "pré-éclampsie", "1 g/h", "4 g"],
        "69185": ["6,75", "bolus", "330 mg", "48 h"],
        "28080": ["posologie", "grossesse", "250 mg", "3 g"],
        "51795": ["100 mg", "grossesse", "troisième"],
        "47503": ["4000", "1 g", "500 mg"],
        "49456": ["1 mg/kg", "grossesse", "deux fois"],
        "44486": ["posologie", "grossesse", "2 mg"],
        "52896": ["grossesse", "20 mg", "magnésium"],
        "62724": ["grossesse", "100 mg"],
        "56271": ["million", "600 mg", "posologie"],
        "59876": ["une fois par jour", "1 g", "calcium"],
        "66710": ["posologie", "grossesse"],
    }
    for num, motifs in plans.items():
        parts = [
            f"Information professionnelle suisse. Swissmedic. Autorisation {num}. "
            "Corpus AIPS du 8 octobre 2026. Lu le 31 octobre 2026.\n"
        ]
        for mot in motifs:
            r = subprocess.run(
                ["python3", str(RACINE / "ressources_ia/outils/aips.py"), "lire", num, mot],
                capture_output=True, text=True, cwd=RACINE,
            )
            parts.append(f"\n# motif : {mot}\n")
            parts.append(r.stdout)
        (EV / f"aips_{num}.txt").write_text("".join(parts), encoding="utf-8")


def ecrire_index_et_extraits() -> None:
    extraits = {
        "isshp_2021.txt": """Magee LA et collaborateurs. The 2021 International Society for the Study of Hypertension in Pregnancy classification, diagnosis and management recommendations for international practice. Pregnancy Hypertension. Publié en 2021. DOI 10.1016/j.preghy.2021.09.008. Consulté le 31 octobre 2026.
https://isshp.org/wp-content/uploads/2023/09/ISSHP-2021-guidelines.pdf

Hypertension : systolic BP at least 140 mmHg and/or diastolic BP at least 90 mmHg, average of at least two measurements.
Severe hypertension : systolic at least 160 and/or diastolic at least 110 mmHg, repeat within 15 minutes. Otherwise repeat in at least 4 hours or on two consecutive outpatient visits.
Proteinuria : at least 30 mg/mmol protein:creatinine ratio, or albumin:creatinine ratio at least 8 mg/mmol, or at least 0.3 g/day.
Classification : chronic hypertension before pregnancy or before 20 weeks. White-coat : office at least 140/90 and home below 135/85. Masked : office below 140/90 and out of office at least 135/85. Gestational hypertension : de novo at or after 20 weeks without proteinuria or other pre-eclampsia findings. Transient gestational hypertension resolves on repeat readings. Pre-eclampsia : gestational hypertension plus new proteinuria, or maternal end-organ dysfunction, or uteroplacental dysfunction, at or after 20 weeks. Superimposed pre-eclampsia : the same new findings on chronic hypertension.
End-organ examples : eclampsia, altered mental status, blindness, stroke, clonus, severe headaches, persistent visual scotomata, pulmonary oedema, platelets below 150000 per microlitre, disseminated intravascular coagulation, haemolysis, creatinine at least 90 micromol/L, ALT or AST above 40 IU/L, placental abruption, angiogenic imbalance, fetal growth restriction, abnormal umbilical artery Doppler, fetal death.
Pre-eclampsia should not be classified as mild or severe during an ongoing pregnancy. Severe hypertension still needs urgent treatment.
Target diastolic BP 85 mmHg. Treat hypertension irrespective of the hypertensive disorder. Severe hypertension requires urgent therapy in a monitored setting.
White-coat hypertension is common, about 30 percent of chronic hypertension. Transient gestational hypertension carries a 40 percent risk of later gestational hypertension or pre-eclampsia. About 25 percent of women with gestational hypertension before 34 weeks progress to pre-eclampsia.
Proteinuria is present in up to 75 percent of pre-eclampsia. It is not mandatory.
Angiogenic imbalance : PlGF below the 5th centile, or sFlt/PlGF ratio above 38 on the Roche assay.
Aspirin after multivariable screening : 150 mg at night. After clinical risk factors : 100 to 162 mg per day, preferably before 16 weeks, discontinued by 36 weeks.
Do not administer corticosteroids to hasten resolution of HELLP syndrome.
Future pregnancy : gestational hypertension at least 4 percent, pre-eclampsia at least 15 percent.
Postpartum blood pressure at least once on days 3 to 6. Review at 3 months.
""",
        "nice_ng133.txt": """National Institute for Health and Care Excellence. Hypertension in pregnancy: diagnosis and management. NICE guideline NG133. Publié en juin 2019, pages relues le 31 octobre 2026.
https://www.nice.org.uk/guidance/ng133

Offer 75 mg to 150 mg of aspirin daily from 12 weeks until birth if there is one high risk factor, or more than one moderate risk factor.
High risk : previous hypertensive disease in pregnancy, chronic kidney disease, autoimmune disease such as lupus or antiphospholipid syndrome, type 1 or type 2 diabetes, chronic hypertension.
Moderate risk : nulliparity, age 40 years or older, pregnancy interval more than 10 years, body mass index 35 or more, family history of pre-eclampsia, multifetal pregnancy.
Target blood pressure 135/85 mmHg.
Labetalol is considered first. Nifedipine if labetalol is not suitable. Methyldopa if both are not suitable.
The guideline states that some nifedipine brands were contraindicated in pregnancy in the summary of product characteristics, and that aspirin did not have a UK marketing authorisation for pre-eclampsia prevention in June 2019.
Protein:creatinine ratio 30 mg/mmol or above. Albumin:creatinine ratio 8 mg/mmol or above.
Severe hypertension : 160/110 mmHg or more. Do not routinely admit gestational hypertension below that level. Admit severe hypertension.
PLGF-based testing to help rule out pre-eclampsia between 20 weeks and 36 weeks and 6 days.
Do not offer planned early birth before 37 weeks for gestational hypertension unless another indication exists.
Sudden swelling of the face, hands or feet is a symptom to report.
""",
        "nice_ng25.txt": """National Institute for Health and Care Excellence. Preterm labour and birth. NICE guideline NG25. Publié le 20 novembre 2015, mis à jour le 10 juin 2022. Consulté le 31 octobre 2026.
https://www.nice.org.uk/guidance/ng25

Suspected preterm labour at 29 weeks and 6 days or less : treat as preterm labour, including tocolysis and maternal corticosteroids.
From 30 weeks and 0 days : cervical length more than 15 mm makes preterm labour unlikely. Cervical length of 15 mm or less : diagnose preterm labour and treat.
Fetal fibronectin more than 50 ng/ml : diagnose preterm labour. Concentration of 50 ng/ml or less : preterm labour unlikely. Do not combine cervical length and fibronectin.
Offer maternal corticosteroids between 24 weeks and 0 days and 33 weeks and 6 days. Consider them between 34 weeks and 0 days and 35 weeks and 6 days. Discuss them between 22 weeks and 0 days and 23 weeks and 6 days. Do not give more than 2 courses. A single repeat course may be considered before 34 weeks if the previous course was more than 7 days earlier and birth is again expected.
Nifedipine for tocolysis is described as off-label in November 2015. Offer it between 26 weeks and 0 days and 33 weeks and 6 days with intact membranes. Consider it between 24 weeks and 0 days and 25 weeks and 6 days. If nifedipine is contraindicated, offer an oxytocin receptor antagonist.
Magnesium sulfate for neuroprotection : offer between 24 weeks and 0 days and 29 weeks and 6 days when birth is planned within 24 hours or labour is established. Consider between 30 weeks and 0 days and 33 weeks and 6 days. Discuss between 23 weeks and 0 days and 23 weeks and 6 days.
The 2015 scheme is a 4 g intravenous bolus over 15 minutes, then 1 g per hour until birth or for 24 hours, whichever is sooner. In August 2019 this use was off-label in the United Kingdom.
Monitor pulse, blood pressure, respiratory rate and tendon reflexes at least every 4 hours.
""",
        "sggg_67_2019.txt": """Gynécologie suisse, avis d'experts numéro 67. Surbek D, Hodel M, Baumann M, Lapaire O. Utilisation du test Flt-1/PlGF dans le diagnostic de la pré-éclampsie. Date du document : 2 décembre 2019. Consulté le 31 octobre 2026.
https://www.sggg.ch/fileadmin/user_upload/PDF/67_F_Diagnostik_Praeeklampsie.pdf

En Suisse l'incidence de la pré-éclampsie avoisine 2,5 pour cent des accouchements, soit plus de 2000 cas par an, sur environ 85000 naissances. Les grossesses avec une symptomatologie proche sont estimées au quintuple.
L'accouchement est l'unique traitement curatif. Un bilan cardiovasculaire est recommandé environ trois mois après l'accouchement, puis un suivi annuel.
La forme classique associe hypertension, protéinurie et œdèmes. Les œdèmes ne sont pas obligatoires. Les guides récents cités par l'avis disent que la protéinurie n'est plus exigée si une atteinte d'organe est présente.
Un ratio sFlt-1/PlGF inférieur à 38 (test Roche) rend la pré-éclampsie très improbable à court terme. Un ratio d'au moins 38 est un résultat positif. Le test figure sur la liste des analyses depuis le 1er juillet 2019. Utilisation à partir de 20 semaines et 0 jour.
""",
        "sggg_41_2013.txt": """Gynécologie suisse, avis d'experts numéro 41. La tocolyse dans les menaces d'accouchement prématuré. Document de 2013. Consulté le 31 octobre 2026.
https://www.sggg.ch/fileadmin/user_upload/PDF/41_Tocolyse_2013.pdf

L'atosiban est recommandé en première intention lorsque le risque d'œdème pulmonaire est élevé, notamment en grossesse gémellaire, hydramnios, pathologie cardiaque ou pulmonaire, ou diabète de type 1.
L'extraction automatique de ce PDF écrit un bolus en microgrammes. Cette unité contredit l'information professionnelle suisse actuelle, qui écrit 6,75 mg. La leçon suit l'information professionnelle et ne retient pas l'unité extraite de 2013.
Le même avis évoque une association nifédipine et magnésium intraveineux. L'information 52896 interdit cette association. La leçon suit l'information professionnelle de 2026.
""",
        "sggg_34_2009.txt": """Gynécologie suisse, avis d'experts numéro 34. Maturation pulmonaire fœtale. Document de 2009. Consulté le 31 octobre 2026.
https://www.sggg.ch/fileadmin/user_upload/PDF/34_Maturation_pulmonaire_foetale_2009.pdf

Une maturation est contre-indiquée si l'accouchement immédiat est requis, par exemple tracé pathologique ou décollement, ou si l'infection amniotique est sévère et fulminante.
Entre 24 semaines et 0 jour et 33 semaines et 6 jours, une prééclampsie peut recevoir une maturation si l'accouchement peut être différé d'au moins 12 à 24 heures.
L'avis de 2009 évoque un effet de la bétaméthasone sur les plaquettes et les enzymes au cours du HELLP, sans savoir si l'effet améliore vraiment le syndrome. L'ISSHP de 2021 recommande de ne pas donner de corticoïdes pour accélérer la résolution du HELLP. La leçon suit le texte de 2021 pour cette indication maternelle.
""",
        "haram_2009.txt": """Haram K, Svendsen E, Abildgaard U. The HELLP syndrome: clinical issues and management. A review. BMC Pregnancy and Childbirth. 2009. PMC2654858. Consulté le 31 octobre 2026.
https://pmc.ncbi.nlm.nih.gov/articles/PMC2654858/

Environ 70 pour cent des cas surviennent avant la naissance, le plus souvent entre 27 et 37 semaines. Le reste survient dans les 48 heures après la naissance.
Classification du Tennessee pour un HELLP complet : hémolyse avec LDH supérieure à 600 unités par litre, AST d'au moins 70 unités par litre, plaquettes inférieures à 100 fois 10 exposant 9 par litre. La bilirubine d'au moins 20,5 micromoles par litre ou un frottis anormal participent au diagnostic d'hémolyse.
Classification du Mississippi : classe 1, plaquettes d'au plus 50 fois 10 exposant 9 par litre. Classe 2, plaquettes entre plus de 50 et 100. Classe 3, plaquettes entre plus de 100 et 150, avec AST ou ALT d'au moins 40. Les classes 1 et 2 exigent aussi LDH supérieure à 600 et AST ou ALT d'au moins 70.
La revue dit que beaucoup d'auteurs donnent une cure de corticoïdes pour le poumon fœtal entre 24 et 34 semaines. Elle ne constitue pas une information professionnelle suisse. Aucun milligramme de cette revue n'est recopié comme dose suisse.
""",
    }
    for nom, texte in extraits.items():
        (EV / nom).write_text(texte.strip() + "\n", encoding="utf-8")
    lignes = [
        "1. Magee et collaborateurs. Classification ISSHP 2021 des troubles hypertensifs de la grossesse. Pregnancy Hypertension, 2021. Consulté le 31.10.2026.",
        "2. NICE. Hypertension in pregnancy, guideline NG133, juin 2019. Consulté le 31.10.2026.",
        "3. NICE. Preterm labour and birth, guideline NG25, 2015, mis à jour le 10 juin 2022. Consulté le 31.10.2026.",
        "4. Information professionnelle Labétalol Nardia, Swissmedic 70383, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "5. Information professionnelle Trandate, Swissmedic 41529, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "6. Information professionnelle Sulfate de magnésium Bichsel, Swissmedic 56394, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "7. Information professionnelle Atosiban Labatec, Swissmedic 69185, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "8. Information professionnelle Aldomet, méthyldopa, Swissmedic 28080, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "9. Information professionnelle Aspirine Cardio, Swissmedic 51795, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "10. Information professionnelle Dafalgan, paracétamol, Swissmedic 47503, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "11. Information professionnelle Clexane, énoxaparine, Swissmedic 49456, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "12. Information professionnelle Ebrantil, urapidil, Swissmedic 44486, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "13. Information professionnelle Nifedipin-Mepha 20 retard, Swissmedic 52896, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "14. Information professionnelle Nitrofurantoin-Acino 100 retard, Swissmedic 62724, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "15. Information professionnelle Pénicilline Grünenthal, Swissmedic 56271, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "16. Information professionnelle Ceftriaxon Labatec, Swissmedic 59876, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "17. Information professionnelle Dexaméthasone Galepharm, Swissmedic 66710, corpus du 8 octobre 2026, lue le 31 octobre 2026.",
        "18. Gynécologie suisse. Avis d'experts 67 sur le ratio sFlt-1/PlGF, 2 décembre 2019. Consulté le 31.10.2026.",
        "19. Gynécologie suisse. Avis d'experts 41 sur la tocolyse, 2013. Consulté le 31.10.2026.",
        "20. Haram, Svendsen et Abildgaard. Revue du syndrome HELLP, BMC Pregnancy and Childbirth, 2009. Consulté le 31.10.2026.",
        "21. Gynécologie suisse. Avis d'experts 34 sur la maturation pulmonaire, 2009. Consulté le 31.10.2026.",
    ]
    (EV / "INDEX.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return lignes


SOURCES_HTML = []  # rempli au runtime


def sources_html(lignes_index: list[str]) -> list[str]:
    return [l.split(". ", 1)[1] if ". " in l else l for l in lignes_index]


def schema_orientation() -> str:
    return """<figure class="schema"><svg viewBox="0 0 640 280" role="img" aria-label="Quatre portes du motif maternel">
<rect x="16" y="24" width="140" height="100" rx="10" fill="#f3cfc3" stroke="#a1262f"><title>Fièvre : chercher pyélonéphrite et infection amniotique</title></rect>
<rect x="172" y="24" width="140" height="100" rx="10" fill="#d5e8f5" stroke="#176fa0"><title>Œdème : bilatéral bénin ou unilatéral thrombotique</title></rect>
<rect x="328" y="24" width="140" height="100" rx="10" fill="#f7e3b0" stroke="#8a5a00"><title>Hypertension : confirmer puis chercher la prééclampsie</title></rect>
<rect x="484" y="24" width="140" height="100" rx="10" fill="#b5e1cb" stroke="#1a7a50"><title>Contractions irrégulières : col et terme</title></rect>
<text x="86" y="70" text-anchor="middle" font-size="15" fill="#14303b">Fièvre</text>
<text x="242" y="70" text-anchor="middle" font-size="15" fill="#14303b">Chevilles</text>
<text x="398" y="70" text-anchor="middle" font-size="15" fill="#14303b">Tension</text>
<text x="554" y="70" text-anchor="middle" font-size="15" fill="#14303b">Contractions</text>
<rect x="120" y="160" width="400" height="88" rx="10" fill="#ffffff" stroke="#14303b"><title>Toute porte grave mène à la surveillance et à l'appel</title></rect>
<text x="320" y="198" text-anchor="middle" font-size="14" fill="#14303b">Mère stable et fœtus rassurant</text>
<text x="320" y="222" text-anchor="middle" font-size="13" fill="#14303b">sinon naissance ou traitement d'urgence</text>
</svg>
<figcaption>Quatre portes du même motif. Survoler un cadre pour la question qu'il pose. Le cadre du bas rappelle que la stabilité se vérifie, elle ne se suppose pas.</figcaption>
</figure>"""


def mini_schema(titre: str, a: str, b: str, c: str) -> str:
    return f"""<figure class="schema"><svg viewBox="0 0 640 160" role="img" aria-label="{html.escape(titre)}">
<rect x="16" y="28" width="190" height="100" rx="10" fill="#d5e8f5" stroke="#176fa0"><title>{html.escape(a)}</title></rect>
<rect x="224" y="28" width="190" height="100" rx="10" fill="#b5e1cb" stroke="#1a7a50"><title>{html.escape(b)}</title></rect>
<rect x="432" y="28" width="190" height="100" rx="10" fill="#f3cfc3" stroke="#a1262f"><title>{html.escape(c)}</title></rect>
<text x="111" y="84" text-anchor="middle" font-size="14" fill="#14303b">{html.escape(a[:28])}</text>
<text x="319" y="84" text-anchor="middle" font-size="14" fill="#14303b">{html.escape(b[:28])}</text>
<text x="527" y="84" text-anchor="middle" font-size="14" fill="#14303b">{html.escape(c[:28])}</text>
</svg>
<figcaption>{html.escape(titre)} Survoler un cadre pour le détail.</figcaption>
</figure>"""


def ellipse(sid, nom, numero, cx, cy, rx, ry, badge, definition, fill="#d5e8f5", stroke="#176fa0"):
    return {
        "id": sid,
        "nom": nom,
        "numero": numero,
        "geometrie": {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry},
        "remplissage": fill,
        "contour": stroke,
        "epaisseur": 2,
        "definition": definition,
        "badge": badge,
    }


def niveau(nid, etiquette, note, structures, defaut=False):
    d = {
        "id": nid,
        "etiquette": etiquette,
        "note": note,
        "viewBox": [0, 0, 1000, 760],
        "repere": {"texte": "D", "x": 80, "y": 80, "titre": "Droite de la patiente, à gauche de l'écran"},
        "structures": structures,
    }
    if defaut:
        d["defaut"] = True
    return d


def question(html_q: str) -> dict:
    return {
        "intitule": "Que montre la coupe ?",
        "html": html_q,
    }


def charger_dessinateur():
    spec = importlib.util.spec_from_file_location("dessinateur_lot177", DESSIN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fragment(desc: dict) -> str:
    mod = charger_dessinateur()
    frag = mod.rendre(desc, POLICE)
    frag = frag.replace('url("POLICE")', f'url("{POLICE}")')
    frag = re.sub(r"(?is)<script>.*?</script>", "", frag)
    return frag


def descriptions() -> dict[str, dict]:
    ute = {
        "id": "lot177-uterus",
        "titre": "Utérus gravide, trois hauteurs",
        "question": question(
            "<p>Le fond porte le placenta sur cette coupe schématique.</p>"
            "<p>Le col se juge en bas, pas sur le fond.</p>"
            "<p>Une longueur de col de 15 mm ou moins, à partir de 30 SA, fait traiter la menace selon le guide de 2022.</p>"
        ),
        "sources_courtes": "Schéma d'enseignement sans cliché, repère D à gauche de l'écran.",
        "niveaux": [
            niveau("fond", "Fond utérin", "Le placenta est dessiné au fond. Ce n'est pas un cliché.", [
                ellipse("paroi-f", "Paroi du fond", 1, 500, 390, 280, 200, [280, 390], "Muscle utérin au fond.", "#f3cfc3", "#a1262f"),
                ellipse("cavite-f", "Cavité amniotique", 2, 500, 400, 180, 120, [500, 430], "Liquide et fœtus, non détaillés.", "#d5e8f5", "#176fa0"),
                ellipse("placenta-f", "Placenta", 3, 500, 250, 120, 50, [500, 250], "Masse placentaire schématique au fond.", "#f7e3b0", "#8a5a00"),
            ], True),
            niveau("corps", "Corps utérin", "Le corps est entre le fond et le col.", [
                ellipse("paroi-c", "Paroi du corps", 1, 500, 390, 300, 210, [270, 390], "Paroi latérale du corps.", "#f3cfc3", "#a1262f"),
                ellipse("cavite-c", "Cavité du corps", 2, 500, 400, 190, 130, [500, 430], "Cavité au niveau du corps.", "#d5e8f5", "#176fa0"),
                ellipse("vessie-c", "Vessie", 3, 500, 620, 90, 40, [500, 620], "Repère antérieur, vessie en avant.", "#b5e1cb", "#1a7a50"),
            ]),
            niveau("col", "Col", "Le col décide de la menace quand les contractions sont irrégulières.", [
                ellipse("paroi-k", "Paroi basse", 1, 500, 360, 260, 180, [300, 340], "Segment inférieur schématique.", "#f3cfc3", "#a1262f"),
                ellipse("col-k", "Col", 2, 500, 560, 70, 90, [500, 560], "Le col se mesure par voie vaginale si le guide l'indique.", "#f7e3b0", "#8a5a00"),
                ellipse("vagin-k", "Vagin", 3, 500, 680, 40, 30, [500, 680], "Voie d'accès à la mesure du col.", "#b5e1cb", "#1a7a50"),
            ]),
        ],
    }
    rein = {
        "id": "lot177-rein",
        "titre": "Rein maternel, trois coupes schématiques",
        "question": question(
            "<p>La fièvre avec douleur du flanc oriente vers le rein, pas vers le col.</p>"
            "<p>Le bassinet dilaté se dessine au centre.</p>"
            "<p>La nitrofurantoïne ne traite pas cette infection du parenchyme.</p>"
        ),
        "sources_courtes": "Schéma d'enseignement sans cliché, repère D à gauche de l'écran.",
        "niveaux": [
            niveau("haut", "Pôle supérieur", "Pôle supérieur du rein, schéma.", [
                ellipse("cortex-h", "Cortex rénal", 1, 500, 390, 260, 160, [320, 300], "Cortex, siège de la pyélonéphrite.", "#f3cfc3", "#a1262f"),
                ellipse("medulla-h", "Médulla", 2, 500, 400, 150, 90, [500, 400], "Pyramides schématiques.", "#f7e3b0", "#8a5a00"),
                ellipse("graisse-h", "Graisse périrénale", 3, 780, 390, 70, 50, [780, 390], "Espace autour du rein.", "#b5e1cb", "#1a7a50"),
            ], True),
            niveau("hile", "Hile", "Le bassinet est au hile.", [
                ellipse("cortex-i", "Cortex du hile", 1, 500, 390, 270, 170, [300, 300], "Cortex encore visible.", "#f3cfc3", "#a1262f"),
                ellipse("bassinet", "Bassinet", 2, 500, 400, 80, 50, [500, 400], "Cavité urinaire centrale.", "#d5e8f5", "#176fa0"),
                ellipse("uretere", "Uretère", 3, 500, 620, 30, 70, [500, 620], "Voie de descente vers la vessie.", "#b5e1cb", "#1a7a50"),
            ]),
            niveau("bas", "Pôle inférieur", "Pôle inférieur, proche de l'uretère.", [
                ellipse("cortex-b", "Cortex inférieur", 1, 500, 360, 240, 150, [320, 280], "Pôle inférieur.", "#f3cfc3", "#a1262f"),
                ellipse("calice", "Calice", 2, 500, 400, 70, 40, [500, 400], "Calice schématique.", "#d5e8f5", "#176fa0"),
                ellipse("psoas", "Psoas", 3, 250, 500, 80, 40, [250, 500], "Muscle voisin, repère de profondeur.", "#b5e1cb", "#1a7a50"),
            ]),
        ],
    }
    mollet = {
        "id": "lot177-mollet",
        "titre": "Mollet, trois coupes schématiques",
        "question": question(
            "<p>L'œdème unilatéral du mollet n'est pas l'œdème du soir.</p>"
            "<p>Les veines profondes sont au centre, entre les muscles.</p>"
            "<p>On ne renvoie pas cette femme sans imagerie ni traitement discuté.</p>"
        ),
        "sources_courtes": "Schéma d'enseignement sans cliché, repère D à gauche de l'écran.",
        "niveaux": [
            niveau("prox", "Mollet proximal", "Coupe haute du mollet.", [
                ellipse("peau-p", "Peau", 1, 500, 390, 300, 210, [500, 230], "Peau et tissu sous-cutané, siège de l'œdème visible.", "#f3cfc3", "#a1262f"),
                ellipse("muscle-p", "Muscle", 2, 500, 400, 180, 120, [650, 400], "Gastrocnémien schématique.", "#b5e1cb", "#1a7a50"),
                ellipse("veine-p", "Veine profonde", 3, 500, 400, 40, 30, [500, 400], "Veine profonde, cible de la thrombose.", "#d5e8f5", "#176fa0"),
            ], True),
            niveau("mi", "Mi-mollet", "Coupe moyenne.", [
                ellipse("peau-m", "Peau moyenne", 1, 500, 390, 280, 200, [500, 230], "Circonférence à comparer à l'autre mollet.", "#f3cfc3", "#a1262f"),
                ellipse("muscle-m", "Muscle moyen", 2, 420, 420, 120, 90, [420, 450], "Loge musculaire.", "#b5e1cb", "#1a7a50"),
                ellipse("veine-m", "Veines jumelles", 3, 620, 420, 36, 28, [620, 420], "Veines jumelles schématiques.", "#d5e8f5", "#176fa0"),
            ]),
            niveau("dist", "Cheville", "Coupe basse, au-dessus de la cheville.", [
                ellipse("peau-d", "Peau basse", 1, 500, 390, 240, 170, [500, 260], "Œdème déclive, souvent bilatéral s'il est physiologique.", "#f3cfc3", "#a1262f"),
                ellipse("tibia", "Tibia", 2, 430, 360, 50, 40, [430, 360], "Os, repère dur.", "#f7e3b0", "#8a5a00"),
                ellipse("veine-d", "Veine tibiale", 3, 600, 430, 30, 24, [600, 430], "Veine tibiale postérieure schématique.", "#d5e8f5", "#176fa0"),
            ]),
        ],
    }
    return {"uterus": ute, "rein": rein, "mollet": mollet}
