#!/usr/bin/env python3
"""Copie dans LOT_137/evidence les extraits réellement lus le 31.10.2026.

Sources : corpus AIPS local (gzip), pages GLIM et Friedli déjà récupérées, résumés Imoberdorf et Fearon lus le même jour.
N'invente aucune ligne : découpe ou recopie.
"""
from __future__ import annotations

import gzip
from pathlib import Path

ROOT = Path("/workspace")
EV = ROOT / "grok-LOTS-html/LOT_137/evidence"
AIPS = ROOT / "ressources_ia/aips/fi_fr"
GLIM = Path("/home/ubuntu/.cursor/projects/workspace/agent-tools/c7fa4d03-021f-4b2e-96f9-f7cc18389979.txt")
FRIEDLI = Path("/home/ubuntu/.cursor/projects/workspace/agent-tools/c664b612-45fb-4d9f-aaca-f8d39a7f422a.txt")


def aips(num: str, debut: str, fin: str | None, nom: str) -> str:
    lignes = gzip.open(AIPS / f"{num}.txt.gz", "rt", encoding="utf-8").read().splitlines()
    i = next(k for k, l in enumerate(lignes) if debut in l)
    j = len(lignes)
    if fin:
        for k in range(i + 1, len(lignes)):
            if fin in lignes[k]:
                j = k
                break
    corps = "\n".join(lignes[i:j])
    return f"# {nom} — n° Swissmedic {num}\n# Extrait du corpus AIPS local, lu le 31.10.2026. Information professionnelle suisse.\n\n{corps}\n"


def main() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / "aips_10989_benerva.txt").write_text(
        aips("10989", "Posologie/Mode", "Interactions", "Benerva"), encoding="utf-8"
    )
    # grossesse Benerva : lignes après Contre-indications, on ajoute le bloc Grossesse s'il est après Interactions
    ben = gzip.open(AIPS / "10989.txt.gz", "rt", encoding="utf-8").read()
    g = ben.find("Grossesse/Allaitement")
    (EV / "aips_10989_benerva.txt").write_text(
        (EV / "aips_10989_benerva.txt").read_text(encoding="utf-8") + "\n" + ben[g:g + 900] + "\n",
        encoding="utf-8",
    )
    (EV / "aips_38219_creon.txt").write_text(
        aips("38219", "Posologie/Mode", "Interactions", "Creon"), encoding="utf-8"
    )
    (EV / "aips_45880_kaliumphosphat.txt").write_text(
        aips("45880", "Posologie/Mode", "Surdosage", "Kaliumphosphat 1 Molar B. Braun"), encoding="utf-8"
    )
    (EV / "aips_56471_kcl.txt").write_text(
        aips("56471", "Posologie/Mode", "Effets indésirables", "Chlorure de potassium Bichsel"), encoding="utf-8"
    )
    (EV / "aips_21278_hausmann.txt").write_text(
        aips("21278", "Posologie/Mode", "Effets indésirables", "Potassium Hausmann"), encoding="utf-8"
    )
    (EV / "aips_57974_dexamethasone.txt").write_text(
        aips("57974", "Indications/Possibilités", "Instructions posologiques particulières", "Dexaméthasone Galepharm"),
        encoding="utf-8",
    )
    dex = gzip.open(AIPS / "57974.txt.gz", "rt", encoding="utf-8").read()
    gd = dex.find("Grossesse, allaitement")
    (EV / "aips_57974_dexamethasone.txt").write_text(
        (EV / "aips_57974_dexamethasone.txt").read_text(encoding="utf-8") + "\n" + dex[gd:gd + 1200] + "\n",
        encoding="utf-8",
    )
    (EV / "aips_42847_nutriflex.txt").write_text(
        aips("42847", "Posologie/Mode", "Contre-indications", "Nutriflex special"), encoding="utf-8"
    )
    # GLIM : le corps utile de la page lue (critères, tableaux 3 et 4, inflammation)
    glim = GLIM.read_text(encoding="utf-8", errors="replace")
    (EV / "glim2019.txt").write_text(
        "# Cederholm T et al. GLIM criteria for the diagnosis of malnutrition.\n"
        "# Clinical Nutrition / Journal of Cachexia, Sarcopenia and Muscle, 2019.\n"
        "# Page PMC6438340 lue le 31.10.2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC6438340/\n\n"
        + glim,
        encoding="utf-8",
    )
    fried = FRIEDLI.read_text(encoding="utf-8", errors="replace")
    (EV / "friedli2018.txt").write_text(
        "# Friedli N, Stanga Z, Culkin A, Crook M, Laviano A, Sobotka L, et al.\n"
        "# Management and prevention of refeeding syndrome in medical inpatients.\n"
        "# Nutrition 2018;47:13-20. DOI 10.1016/j.nut.2017.09.007. Texte lu le 31.10.2026.\n\n"
        + fried,
        encoding="utf-8",
    )
    (EV / "imoberdorf2010.txt").write_text(
        "# Imoberdorf R, Meier R, Krebs P, Hangartner PJ, Hess B, Stäubli M, Wegmann D, Rühlin M, Ballmer PE.\n"
        "# Prevalence of undernutrition on admission to Swiss hospitals.\n"
        "# Clinical Nutrition 2010. DOI 10.1016/j.clnu.2009.06.005. Résumé lu le 31.10.2026.\n\n"
        "According to the literature, undernutrition is prevalent in 20-60% of patients on hospital admission. "
        "The differences in the rate of undernutrition arise from different diagnostic tools used in the studies. "
        "We aimed to investigate the prevalence of undernutrition in Swiss hospitals using a standardized screening tool. "
        "All patients admitted to the departments of internal medicine of 7 Swiss hospitals were screened at entry "
        "for nutritional status using the Nutrition Risk Screening 2002 score. "
        "Patients with a score of 3 or more, which denotes severe undernutrition or patient at risk for undernutrition were analyzed. "
        "Between May 2003 and April 2006 32,837 patients were included in the study. "
        "5978 (18.2%) had a score of 3 or more and were classified as severely undernourished or at high risk for undernutrition "
        "(age under 45 y: 8%; 45-64 y: 11%; 65-84 y: 22%; over 85 y: 28%). "
        "A nutritional intervention was made in 4175 patients (12.7%). "
        "Nearly one in five patients was severely undernourished or at risk for undernutrition. "
        "Undernutrition was directly related to age. "
        "Patients with a clear indication for nutrition therapy, as suggested by the formal screening procedure, obtained nutritional intervention in 70%.\n",
        encoding="utf-8",
    )
    (EV / "fearon2011.txt").write_text(
        "# Fearon K, Strasser F, Anker SD, et al. Definition and classification of cancer cachexia: an international consensus.\n"
        "# The Lancet Oncology, 2011. Résumé lu le 31.10.2026.\n"
        "# Le signe inférieur du résumé a été écrit en toutes lettres pour éviter une balise (P-19). Le sens est celui du résumé.\n\n"
        "Cancer cachexia was defined as a multifactorial syndrome defined by an ongoing loss of skeletal muscle mass "
        "(with or without loss of fat mass) that cannot be fully reversed by conventional nutritional support and leads to "
        "progressive functional impairment. Its pathophysiology is characterised by a negative protein and energy balance "
        "driven by a variable combination of reduced food intake and abnormal metabolism. "
        "The agreed diagnostic criterion for cachexia was weight loss greater than 5%, or weight loss greater than 2% "
        "in individuals already showing depletion according to current bodyweight and height "
        "(body-mass index below 20 kg/m2) or skeletal muscle mass (sarcopenia). "
        "An agreement was made that the cachexia syndrome can develop progressively through various stages: "
        "precachexia to cachexia to refractory cachexia.\n",
        encoding="utf-8",
    )
    (EV / "INDEX.md").write_text(
        """# INDEX des preuves — LOT_137

Extraits datés, lus le 31.10.2026. Les incertitudes qui ne sont pas des faits sont dans `../INCERTITUDES.md`, pas dans les leçons.

1. Cederholm et al., critères GLIM, Clinical Nutrition et Journal of Cachexia, Sarcopenia and Muscle, 2019. Page PMC6438340. `glim2019.txt`.
2. Imoberdorf et al., Clinical Nutrition, 2010, DOI 10.1016/j.clnu.2009.06.005. Sept hôpitaux suisses, mai 2003 à avril 2006. `imoberdorf2010.txt`.
3. Fearon et al., The Lancet Oncology, 2011, consensus sur la cachexie cancéreuse. Résumé. `fearon2011.txt`.
4. Friedli, Stanga et al., Nutrition, 2018, DOI 10.1016/j.nut.2017.09.007. Syndrome de renutrition, patients de médecine. `friedli2018.txt`.
5. AIPS Benerva, n° 10989, corpus local lu le 31.10.2026. `aips_10989_benerva.txt`.
6. AIPS Creon, n° 38219, corpus local lu le 31.10.2026. `aips_38219_creon.txt`.
7. AIPS Kaliumphosphat 1 Molar B. Braun, n° 45880, corpus local lu le 31.10.2026. `aips_45880_kaliumphosphat.txt`.
8. AIPS Chlorure de potassium Bichsel, n° 56471, corpus local lu le 31.10.2026. `aips_56471_kcl.txt`.
9. AIPS Potassium Hausmann, n° 21278, corpus local lu le 31.10.2026. `aips_21278_hausmann.txt`.
10. AIPS Dexaméthasone Galepharm, n° 57974, corpus local lu le 31.10.2026. `aips_57974_dexamethasone.txt`.
11. AIPS Nutriflex special, n° 42847, corpus local lu le 31.10.2026. `aips_42847_nutriflex.txt`.
""",
        encoding="utf-8",
    )
    print("preuves", EV)


if __name__ == "__main__":
    main()
