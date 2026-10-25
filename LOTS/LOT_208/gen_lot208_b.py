#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Brouillon V7, LOT_208, rôle B, DX.5 à DX.10. Ce script n'est pas un audit."""
import html
import os

OUT = os.path.dirname(os.path.abspath(__file__))
NB = "\u00a0"
DATE = "24.10.2026"

SOURCES = [
    ("S501", "Société européenne de cardiologie. Recommandations 2021 de prévention cardiovasculaire en pratique clinique. European Heart Journal. La Suisse figure parmi les pays à faible risque des abaques SCORE2. Le score calcique est de classe IIb autour des seuils de décision. Le risque vie entière est défini dans le texte.", "https://academic.oup.com/eurheartj/article/42/34/3227/6358713"),
    ("S502", "SCORE2 working group and ESC Cardiovascular risk collaboration. SCORE2 risk prediction algorithms. European Heart Journal, 2021. DOI 10.1093/eurheartj/ehab309. Modèle de 40 à 69 ans, événements fatals et non fatals, régions de risque.", "https://doi.org/10.1093/eurheartj/ehab309"),
    ("S503", "Groupe de travail Lipides et Athérosclérose (AGLA / GSLA). Calculateur de risque du GSLA, page française lue le 24.10.2026. Personnes apparemment en bonne santé, 20 à 69 ans, sans diabète. Événement coronarien fatal ou infarctus non fatal à dix ans.", "https://agla.ch/fr/calculateurs-outils/calculateur-de-risque-du-gsla"),
    ("S504", "AGLA. Calculateur ESC SCORE2/SCORE2-OP, page française lue le 24.10.2026. Personnes apparemment en bonne santé, 40 à 89 ans, sans diabète. Pour le diabète de type 2, la page renvoie à SCORE2-Diabète.", "https://agla.ch/fr/calculateurs-outils/calculateur-esc-score2"),
    ("S505", "AGLA. Détermination du risque cardiovasculaire, page allemande lue le 24.10.2026. Catégories très élevé, élevé, faible à modéré, avec seuils selon l'âge, y compris l'hypercholestérolémie familiale et la maladie rénale.", "https://agla.ch/de/rechner-und-tools/cvrisk-determination"),
    ("S506", "European Atherosclerosis Society. Page SCORE2 et SCORE2-OP lue le 24.10.2026. Le modificateur « antécédent familial de maladie cardiovasculaire précoce » y est chiffré : hommes avant 55 ans, femmes avant 60 ans. Le tableau de classe affiché sur cette page ne remplace pas le texte ESC 2021 ouvert à part.", "https://eas-society.org/publications/guidelines/score2-score2-op/"),
    ("S507", "Office fédéral de la santé publique. Consommation d'alcool en Suisse : faits et chiffres. Page lue le 24.10.2026. Chiffres 2022 et 2024, décès 2017, coûts, et position sur l'absence de quantité sans danger.", "https://www.bag.admin.ch/fr/consommation-dalcool-en-suisse-faits-et-chiffres"),
    ("S508", "Obsan, MonAM, Office fédéral de la santé publique. Consommation d'alcool à risque (15 ans et plus). Page lue le 24.10.2026. 16,4 % en 2022, seuils en grammes et en verres, enquête suisse sur la santé.", "https://ind.obsan.admin.ch/fr/indicator/monam/consommation-dalcool-a-risque-age-15"),
    ("S509", "Office fédéral de la santé publique. Le radon provoque le cancer du poumon. Page lue le 24.10.2026. 200 à 300 décès par an, environ 3 200 décès par cancer du poumon (OFS 2023), latence de plusieurs années.", "https://www.bag.admin.ch/fr/le-radon-provoque-le-cancer-du-poumon"),
    ("S510", "Office fédéral de la santé publique. Lignes directrices Radon, version 2.3 du 2 février 2023. PDF lu le 24.10.2026. Ordonnance sur la radioprotection, niveau de référence 300 Bq/m³, quinze heures par semaine, délais du tableau 4 pour la ligne 300 à 600 Bq/m³.", "https://www.bag.admin.ch/dam/fr/sd-web/eYh7M3dNFDW-/wegleitungradon.pdf"),
    ("S511", "Office fédéral de la santé publique. Legal dispositions concerning radon. Page anglaise lue via la recherche du 24.10.2026, extraits concordants avec les lignes directrices. Depuis le 1.1.2018, le niveau de référence est 300 Bq/m³ et une valeur seuil de 1 000 Bq/m³ s'applique aux postes de travail exposés.", "https://www.bag.admin.ch/en/legal-dispositions-concerning-radon"),
    ("S512", "Confédération suisse, Fedlex. Loi fédérale du 15 juin 2018 sur l'analyse génétique humaine (LAGH), RS 810.12. Texte compilé lu le 24.10.2026. Articles 5 à 9 et 20 à 22. Une note de l'article 22 indique une modification en vigueur depuis le 1er août 2025.", "https://www.fedlex.admin.ch/eli/cc/2022/537/fr"),
    ("S513", "Office fédéral de la santé publique. Analyses génétiques humaines : le point sur le cadre juridique. PDF de février 2025 lu le 24.10.2026. Droit de ne pas être informé, informations excédentaires, conseil non directif.", "https://www.bag.admin.ch/dam/fr/sd-web/HA4nF3pAuQs0/analyses-g%C3%A9n%C3%A9tiques_cadre-juridique_02.2025.pdf"),
]


def e(text):
    return html.escape(text, quote=True)


def p(*sentences):
    body = " ".join(sentences)
    return f"<p style='margin:4px 0 6px;'>{body}</p>"


def inline(term, *paras):
    inner = "".join(p(x) for x in paras)
    return (
        "<details style='display:inline;'><summary style='display:inline;cursor:pointer;"
        "color:#1f618d;text-decoration:underline dotted;'>"
        + e(term)
        + "</summary><div style='display:block;margin:4px 0 8px;padding:8px;background:#f4f6f7;"
        "border-left:3px solid #1f618d;font-size:0.93em;'>"
        + inner
        + "</div></details>"
    )


def block(title, inner):
    return (
        "<details style='margin:8px 0;border-left:4px solid #2980b9;background:#ebf5fb;padding:6px 10px;'>"
        f"<summary style='cursor:pointer;font-weight:bold;color:#1a5276;'>{e(title)}</summary>"
        f"<div style='margin-top:6px;'>{inner}</div></details>"
    )


def table(headers, rows):
    th = "".join(
        f"<th style='background:#d4e6f1;text-align:left;vertical-align:top;'>{e(h)}</th>" for h in headers
    )
    body = []
    for row in rows:
        tds = "".join(f"<td style='vertical-align:top;'>{c}</td>" for c in row)
        body.append(f"<tr>{tds}</tr>")
    return (
        "<div style='overflow-x:auto;'><table border='1' cellpadding='7' cellspacing='0' "
        "style='width:100%;border-collapse:collapse;font-size:0.92em;'><thead><tr>"
        + th
        + "</tr></thead><tbody>"
        + "".join(body)
        + "</tbody></table></div>"
    )


def td(text):
    return e(text)


def point(num, title, inner):
    return (
        f"<div style='margin:16px 0 10px;'><strong>{num}. {e(title)}</strong><br>{inner}</div>"
    )


def src(sid):
    return f" <em>Source : [{sid}].</em>"


SWISS_ORDER = [
    "S512", "S513", "S507", "S508", "S509", "S510", "S511",
    "S503", "S504", "S505", "S501", "S502", "S506",
]


def color_proba(doc):
    """Met les pourcentages en rouge charte, sans halo."""
    import re
    parts = re.split(r"(<[^>]+>)", doc)
    out = []
    pat = re.compile(r"\d+(?:,\d+)?(?:\u00a0| )?%")
    for part in parts:
        if part.startswith("<"):
            out.append(part)
        else:
            out.append(pat.sub(r"<span class='proba'>\g<0></span>", part))
    return "".join(out)


def page(title, intro, body, used, fin):
    rank = {sid: i for i, sid in enumerate(SWISS_ORDER)}
    selected = [s for s in SOURCES if s[0] in used]
    selected.sort(key=lambda s: rank.get(s[0], 50))
    items = []
    for sid, desc, url in selected:
        items.append(
            f"<li><strong>[{sid}]</strong> {e(desc)} "
            f"<span style='word-break:break-all;'>{e(url)}</span> (consulté le {DATE}).</li>"
        )
    html_doc = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<style>
html {{ background:#d6eefb; }}
body {{
  background:#d6eefb;
  color:#12202c;
  font-family:"Atkinson Hyperlegible", sans-serif;
  line-height:1.55;
  margin:0;
}}
.page {{
  max-width:980px;
  margin:auto;
  padding:18px 16px 32px;
  background:#f7fbfe;
  color:#12202c;
}}
h2 {{ color:#0c3a5e; border-bottom:3px solid #1f618d; padding-bottom:6px; }}
.proba {{
  color:#C8102E;
  font-weight:700;
  text-shadow:none;
  box-shadow:none;
  background:transparent;
}}
a {{ color:#0c3a5e; }}
</style>
</head>
<body>
<div class="page">
<h2>{e(title)}</h2>
<p>{intro}</p>
{body}
<h2>Sources</h2>
<p>Les sources suisses ouvertes pour ce cahier précèdent les sources européennes. Chaque source a été lue le {DATE}.</p>
<ol>
{''.join(items)}
</ol>
<p>Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin.</p>
<p>Lacunes assumées : l'Appel A et les DX.1 à DX.4 ne sont pas rédigés dans ce fichier. L'ordre des dix situations est celui de la fiche SSP O4.7 déjà présente dans le dépôt (champ des dix facteurs), lue comme liste de travail et non comme source épidémiologique. Aucune information professionnelle Swissmedic n'a été ouverte : aucune dose chiffrée n'est prescrite. Les seuils Agatston américains ne sont pas repris, parce que le texte ESC 2021 ouvert ne les fixe pas. Aucune page SSMI, HUG ou CHUV n'a été ouverte pour ce lot : aucun chiffre de ces institutions n'est donc ajouté.</p>
</div>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""
    return html_doc


INTRO = (
    "Ce cahier sert l'examen fédéral suisse et la consultation réelle. Il traite le SSP O4.7 de PROFILES 2023, "
    "l'évaluation partagée des facteurs de risque et de protection des maladies qui engagent le pronostic vital. "
    "L'agent B de l'équipe E03, vague 2, n'écrit ici que les situations DX.5 à DX.10. L'Appel A et les quatre premières "
    "situations appartiennent à un autre auteur. Les fenêtres s'ouvrent au clic. Les sources ont été lues le 24 octobre 2026. "
    "Aucune information professionnelle Swissmedic n'a été ouverte : aucune dose n'est donc prescrite. "
    "L'ordre suit la fiche O4.7 du dépôt lorsque la Suisse n'a pas livré de pourcentage : d'abord le risque que l'âge jeune dissimule, "
    "puis le calcium coronaire qui reclasse, l'alcool qui tue encore, le stress que le score ignore, le radon derrière le tabac, "
    "et enfin l'histoire familiale, qui ouvre un droit autant qu'une artère."
)


def wrap_dx(summary, inner):
    return (
        "<details open style='border:1px solid #2980b9;border-radius:6px;margin:18px 0;padding:10px 14px;background:#fff;'>"
        f"<summary style='cursor:pointer;font-size:1.15em;font-weight:bold;color:#1a5276;'>{summary}</summary>"
        f"{inner}</details>"
    )


def _breaks(doc):
    return (
        doc.replace("</p>", "</p>\n")
        .replace("</div>", "</div>\n")
        .replace("</details>", "</details>\n")
        .replace("</tr>", "</tr>\n")
        .replace("</li>", "</li>\n")
        .replace("</table>", "</table>\n")
        .replace("</style>", "</style>\n")
    )


def assemble(title, intro, core, used, fin, fixe, suite, target=179200, hi=189440):
    """Ajoute des fenêtres jusqu'à viser ~175 Ko, sans dépasser le plafond souple."""
    def pack(chunks):
        doc = page(title, intro, core + "".join(chunks), used, fin)
        doc = color_proba(doc)
        return _breaks(doc)

    chosen = list(fixe)
    doc = pack(chosen)
    n = len(doc.encode("utf-8"))
    for chunk in suite:
        trial_chunks = chosen + [chunk]
        trial = pack(trial_chunks)
        tn = len(trial.encode("utf-8"))
        if tn > 204800:
            continue
        if n >= target and tn > hi:
            continue
        chosen.append(chunk)
        doc = trial
        n = tn
        if n >= target:
            break
    return doc, n


def write_all():
    import json
    from lot208_dx import dx5, dx6, dx7, dx8, dx9, dx10
    from lot208_plus import plus_map
    from lot208_fond import fond_map

    extra = plus_map()
    fond = fond_map()
    files = [
        ("LOT_208_Appel_B_V7_DX.5.html", "LOT_208 — SSP O4.7 — DX.5 seul (DX.3 et DX.4 hors périmètre)", dx5() + extra["dx5"], ["S501", "S502", "S503", "S504", "S505", "S506"], "LOT_208_DX5", "dx5"),
        ("LOT_208_Appel_B_V7_Partie_3_DX.6_a_DX.7.html", "LOT_208 — SSP O4.7 — Partie 3, DX.6 et DX.7", dx6() + extra["dx6"] + dx7() + extra["dx7"], ["S501", "S503", "S505", "S506", "S507", "S508"], "LOT_208_DX6_DX7", "p3"),
        ("LOT_208_Appel_B_V7_Partie_4_DX.8_a_DX.10.html", "LOT_208 — SSP O4.7 — Partie 4, DX.8 à DX.10", dx8() + extra["dx8"] + dx9() + extra["dx9"] + dx10() + extra["dx10"], ["S501", "S505", "S506", "S509", "S510", "S511", "S512", "S513"], "LOT_208_DX8_DX10", "p4"),
    ]
    for name, title, body, used, fin, key in files:
        doc, n = assemble(title, INTRO, body, used, fin, fond[key]["fixe"], fond[key]["suite"])
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(doc)
        flag = "OK" if 153600 <= n <= 204800 else "HORS-FENETRE"
        print(name, n, flag)

    evidence = {
        "lot": 208,
        "ssp": "O4.7",
        "titre": "Évaluation partagée des facteurs de risque et de protection des maladies fréquentes engageant le pronostic vital",
        "agent": "B",
        "equipe": "E03",
        "vague": 2,
        "branche": "flash/vague2/LOT_208-B",
        "perimetre": "DX.5 à DX.10",
        "appel_A_lu": False,
        "aips_ouvertes": False,
        "audit": False,
        "consulte_le": "2026-10-24",
        "ordre": [
            "DX.1 Tabac (rôle A, non rédigé ici)",
            "DX.2 Hypertension (rôle A, non rédigé ici)",
            "DX.3 Dyslipidémie LDL (rôle A, non rédigé ici)",
            "DX.4 Score de risque à dix ans AGLA/SCORE2 (rôle A, non rédigé ici)",
            "DX.5 Risque vie entière du sujet jeune",
            "DX.6 Score calcique coronaire",
            "DX.7 Alcool",
            "DX.8 Stress psychosocial et position sociale",
            "DX.9 Radon",
            "DX.10 Histoire familiale précoce et conseil génétique",
        ],
        "sources": [{"id": a, "texte": b, "url": c} for a, b, c in SOURCES],
    }
    with open(os.path.join(OUT, "evidence_DX5-DX10.json"), "w", encoding="utf-8") as f:
        json.dump(evidence, f, ensure_ascii=False, indent=1)
    print("evidence ok")


if __name__ == "__main__":
    write_all()
