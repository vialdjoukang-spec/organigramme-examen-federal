#!/usr/bin/env python3
"""Assemble LOT_151 depuis les fichiers contenu_*.md du dossier _travail."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import A, P, Q, btn, ecrire, fen, page

HERE = Path(__file__).resolve().parent
F = {
    "TP": A("temps de prothrombine", "TP"),
    "TCA": A("temps de céphaline activée", "TCA"),
    "TQ": A("temps de Quick", "TQ"),
    "INR": A("international normalized ratio", "INR"),
    "TT": A("temps de thrombine", "TT"),
    "CIVD": A("coagulation intravasculaire disséminée", "CIVD"),
    "AVK": A("antagoniste de la vitamine K", "AVK"),
    "AOD": A("anticoagulant oral direct", "AOD"),
    "HNF": A("héparine non fractionnée", "HNF"),
    "HBPM": A("héparine de bas poids moléculaire", "HBPM"),
    "AIPS": A("information professionnelle suisse", "AIPS"),
    "RMS": A("Revue Médicale Suisse", "RMS"),
    "CHUV": A("Centre hospitalier universitaire vaudois", "CHUV"),
    "SSH": A("Société suisse d'hématologie", "SSH"),
    "ISTH": A("International Society on Thrombosis and Haemostasis", "ISTH"),
    "SSP": A("situation de départ", "SSP"),
    "PROFILES": A("référentiel suisse des objectifs de formation", "PROFILES"),
    "SAPL": A("syndrome des antiphospholipides", "SAPL"),
    "APL": A("anticorps antiphospholipides", "APL"),
    "GFHT": A("Groupe français d'étude sur l'hémostase et la thrombose", "GFHT"),
    "MELD": A("Model for End-Stage Liver Disease", "MELD"),
    "ISI": A("indice de sensibilité international", "ISI"),
    "EDTA": A("acide éthylènediaminetétraacétique", "EDTA"),
    "OMS": A("Organisation mondiale de la santé", "OMS"),
    "MM": A("micelles mixtes", "MM"),
    "UI": A("unité internationale", "UI"),
    "FVIII": A("facteur VIII", "FVIII"),
    "FIX": A("facteur IX", "FIX"),
    "LES": A("lupus érythémateux systémique", "LES"),
    "AIT": A("accident ischémique transitoire", "AIT"),
    "PAH": A("personne avec hémophilie", "PAH"),
}

SOURCES_HTML = [
"PROFILES 2023, validé le 1er novembre 2023, situation F2.3.",
"Reber G, Boehlen F. Revue Médicale Suisse, 6 février 2008.",
"Clauser S, Calmette L. La Revue de Médecine Interne, publié le 28 mai 2024.",
"CHUV, laboratoire central d'hématologie, LCH_MAN_LCH8_PT_003, version 3, applicable le 30 juin 2026.",
"CHUV, catalogue du temps de prothrombine, page lue le 31 octobre 2026.",
"CHUV, catalogue du temps de thromboplastine partielle activée, page lue le 31 octobre 2026.",
"CHUV, catalogue du fibrinogène, page lue le 31 octobre 2026.",
"Marcoumar, phenprocoumone, information professionnelle, numéro 19395.",
"Sintrom, acénocoumarol, information professionnelle, numéro 21693.",
"Konakion MM, phytoménadione, information professionnelle, numéro 48112013.",
"Héparine Bichsel, information professionnelle, numéro 46240.",
"Sulfate de protamine, information professionnelle, numéro 69842.",
"Praxbind, idarucizumab, information professionnelle, numéro 65804.",
"Beriplex, complexe prothrombinique, information professionnelle, numéro 00665.",
"NovoSeven, eptacog alfa, information professionnelle, numéro 58693.",
"Cyklokapron, acide tranexamique, information professionnelle, numéro 33741.",
"Minirin solution injectable, desmopressine, information professionnelle, numéro 43585.",
"Feiba, information professionnelle, numéro 41352.",
"Abetel G, Angelillo-Scherrer A, Pierre-Alain Plan. Revue Médicale Suisse, 7 mai 2014.",
"Casini A, Fontana P, Lecompte T. Revue Médicale Suisse, 5 décembre 2018.",
"Leimgruber A et collaborateurs. Revue Médicale Suisse, 25 février 2004.",
"Revue Médicale Suisse, 8 avril 2020, syndrome des antiphospholipides chez l'adulte.",
"Fontana P, Robert-Ebadi H, Righini M. Revue Médicale Suisse, 13 janvier 2021.",
"Anastasiou M, Chalandon Y, Anchisi S. Revue Médicale Suisse, 2018.",
"Hermans C, Lambert C. Revue Médicale Suisse, 15 janvier 2020.",
"Fontana P, Casini A. Société suisse d'hématologie, groupe Hémostase, mai 2023.",
"Tiede A et collaborateurs. Haematologica, DOI 10.3324/haematol.2019.230771, page lue le 31 octobre 2026.",
"Ondexxya, andexanet alfa, information professionnelle, numéro 67759.",
"Octostim, desmopressine, information professionnelle, numéro 52711.",
"MabThera, rituximab, information professionnelle, numéro 54378.",
"CellCept, mycophénolate mofétil, information professionnelle, numéro 53337.",
]

INDEX = [
"1. PROFILES 2023, validé le 1er novembre 2023, situation F2.3 abnormal coagulation profile. `profiles2023.txt`.",
"2. Reber G, Boehlen F. Revue Médicale Suisse, 6 février 2008, temps de prothrombine. `rms2008_quick.txt`.",
"3. Clauser S, Calmette L. La Revue de Médecine Interne, publié le 28 mai 2024. `rmi2024_tp_tca.txt`.",
"4. CHUV, LCH_MAN_LCH8_PT_003, version 3, applicable le 30 juin 2026, projets de recherche. `chuv2026_intervalles.txt`.",
"5. CHUV, catalogue du temps de prothrombine, page lue le 31 octobre 2026. `chuv2026_catalogue_tp.txt`.",
"6. CHUV, catalogue du temps de thromboplastine partielle activée, page lue le 31 octobre 2026. `chuv2026_catalogue_tca.txt`.",
"7. CHUV, catalogue du fibrinogène, page lue le 31 octobre 2026. `chuv2026_catalogue_fib.txt`.",
"8. Information professionnelle Marcoumar, numéro Swissmedic 19395, lue le 31 octobre 2026. `aips_19395.txt`.",
"9. Information professionnelle Sintrom, numéro Swissmedic 21693, lue le 31 octobre 2026. `aips_21693.txt`.",
"10. Information professionnelle Konakion MM, numéro Swissmedic 48112013, lue le 31 octobre 2026. `aips_48112013.txt`.",
"11. Information professionnelle Héparine Bichsel, numéro Swissmedic 46240, lue le 31 octobre 2026. `aips_46240.txt`.",
"12. Information professionnelle sulfate de protamine LEO Pharma, numéro Swissmedic 69842, lue le 31 octobre 2026. `aips_69842.txt`.",
"13. Information professionnelle Praxbind, numéro Swissmedic 65804, lue le 31 octobre 2026. `aips_65804.txt`.",
"14. Information professionnelle Beriplex, numéro Swissmedic 00665, lue le 31 octobre 2026. `aips_00665.txt`.",
"15. Information professionnelle NovoSeven, numéro Swissmedic 58693, lue le 31 octobre 2026. `aips_58693.txt`.",
"16. Information professionnelle Cyklokapron, numéro Swissmedic 33741, lue le 31 octobre 2026. `aips_33741.txt`.",
"17. Information professionnelle Minirin solution injectable, numéro Swissmedic 43585, lue le 31 octobre 2026. `aips_43585.txt`.",
"18. Information professionnelle Feiba NF, numéro Swissmedic 41352, lue le 31 octobre 2026. `aips_41352.txt`.",
"19. Abetel G, Angelillo-Scherrer A, Plan PA. Revue Médicale Suisse, 7 mai 2014. `rms2014_thrombophilie.txt`.",
"20. Casini A, Fontana P, Lecompte T. Revue Médicale Suisse, 5 décembre 2018. `rms2018_diasthese.txt`.",
"21. Leimgruber A et collaborateurs. Revue Médicale Suisse, 25 février 2004. `rms2004_sapl.txt`.",
"22. Revue Médicale Suisse, 8 avril 2020, syndrome des antiphospholipides. `rms2020_sapl_pec.txt`.",
"23. Fontana P, Robert-Ebadi H, Righini M. Revue Médicale Suisse, 13 janvier 2021. `rms2021_aod.txt`.",
"24. Anastasiou M, Chalandon Y, Anchisi S. Revue Médicale Suisse, 2018. `rms2018_civd_cancer.txt`.",
"25. Hermans C, Lambert C. Revue Médicale Suisse, 15 janvier 2020. `rms2020_hemophilie.txt`.",
"26. Fontana P, Casini A. Société suisse d'hématologie, mai 2023. `ssh2023_aha.txt`.",
"27. Tiede A et collaborateurs. Haematologica, DOI 10.3324/haematol.2019.230771, page lue le 31 octobre 2026. `haematologica2020_aha.txt`.",
"28. Information professionnelle Ondexxya, numéro Swissmedic 67759, lue le 31 octobre 2026. `aips_67759.txt`.",
"29. Information professionnelle Octostim, numéro Swissmedic 52711, lue le 31 octobre 2026. `aips_52711.txt`.",
"30. Information professionnelle MabThera, numéro Swissmedic 54378, lue le 31 octobre 2026. `aips_54378.txt`.",
"31. Information professionnelle CellCept, numéro Swissmedic 53337, lue le 31 octobre 2026. `aips_53337.txt`.",
]

TITRES = {
    "p1": "1. Définition",
    "p2": "2. Épidémiologie",
    "p3": "3. Physiopathologie",
    "p4": "4. Démarche diagnostique",
    "p5": "5. Anamnèse et drapeaux rouges",
    "p6": "6. Examen physique",
    "p7": "7. Approche syndromique",
    "p8": "8. Diagnostic positif",
    "p9": "9. Examens complémentaires",
    "p10": "10. Arbre décisionnel",
    "p11": "11. Prise en charge en Suisse",
    "p12": "12. Prévention",
    "p13": "13. Points clés",
    "p14": "14. Pièges d'examen",
}


def fmt(text):
    return text.format(**F)


def parse(path):
    texte = path.read_text(encoding="utf-8")
    suite = path.with_name(path.stem + "_suite.md")
    if suite.exists():
        texte += "\n" + suite.read_text(encoding="utf-8")
    sections = {}
    cur = None
    for raw in texte.splitlines():
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        if line.startswith("# "):
            cur = line[2:].strip()
            sections.setdefault(cur, [])
            continue
        if cur is None:
            raise SystemExit("ligne hors section : " + line[:80])
        refs = ()
        if " || " in line:
            text, ref = line.rsplit(" || ", 1)
            refs = tuple(int(x) for x in ref.split(",") if x.strip())
        else:
            text = line
        if text.startswith("Q "):
            # Q fichier | debut | fin
            corps = text[2:]
            fichier, debut, fin = [x.strip() for x in corps.split("|", 2)]
            text = Q(fichier, debut, fin)
        sections[cur].append(P(fmt(text), refs))
    return sections


def glossaire():
    paras = [P("Chaque sigle de la leçon est développé une fois dans cette fenêtre.")]
    libs = [
        ("PROFILES", "référentiel suisse des objectifs de formation"),
        ("SSP", "situation de départ"),
        ("AIPS", "information professionnelle suisse"),
        ("RMS", "Revue Médicale Suisse"),
        ("CHUV", "Centre hospitalier universitaire vaudois"),
        ("SSH", "Société suisse d'hématologie"),
        ("ISTH", "International Society on Thrombosis and Haemostasis"),
        ("OMS", "Organisation mondiale de la santé"),
        ("TP", "temps de prothrombine"),
        ("TQ", "temps de Quick"),
        ("TCA", "temps de céphaline activée"),
        ("INR", "international normalized ratio"),
        ("TT", "temps de thrombine"),
        ("CIVD", "coagulation intravasculaire disséminée"),
        ("AVK", "antagoniste de la vitamine K"),
        ("AOD", "anticoagulant oral direct"),
        ("HNF", "héparine non fractionnée"),
        ("HBPM", "héparine de bas poids moléculaire"),
        ("SAPL", "syndrome des antiphospholipides"),
        ("APL", "anticorps antiphospholipides"),
        ("GFHT", "Groupe français d'étude sur l'hémostase et la thrombose"),
        ("MELD", "Model for End-Stage Liver Disease"),
        ("ISI", "indice de sensibilité international"),
        ("EDTA", "acide éthylènediaminetétraacétique"),
        ("MM", "micelles mixtes"),
        ("UI", "unité internationale"),
        ("FVIII", "facteur VIII"),
        ("FIX", "facteur IX"),
        ("LES", "lupus érythémateux systémique"),
        ("AIT", "accident ischémique transitoire"),
        ("PAH", "personne avec hémophilie"),
    ]
    for cle, lib in libs:
        paras.append(P(f"Dans cette leçon, {lib} ({F[cle]})."))
    return "\n".join([
        P("Dix diagnostics organisent la leçon. Le rang E est l'ordre de l'algorithme, pas un classement de fréquence suisse."),
        P("Les milligrammes écrits viennent de l'information professionnelle du produit nommé, ou d'une phrase datée citée avec sa limite."),
        P(f"Les sigles s'ouvrent dans {btn('w-glossaire', 'la fenêtre des sigles')}."),
        fen("w-glossaire", "Sigles de la leçon", paras),
    ])


def blocs_depuis(path, prefixe_fenetre):
    sec = parse(path)
    blocs = {"gloss": glossaire()}
    for i in range(1, 15):
        pid = f"p{i}"
        fiche = sec.get(f"{pid} fiche", [])
        fenetre_lignes = sec.get(f"{pid} fen", [])
        if not fiche or not fenetre_lignes:
            raise SystemExit(f"section vide : {pid} dans {path.name}")
        bouton = sec.get(f"{pid} bouton", ["la fenêtre"])[0]
        # bouton est déjà un <p> ; on veut le texte. On relit autrement.
        blocs[pid] = (TITRES[pid], fiche, "")  # fenêtre ajoutée après
    # reconstruire avec boutons lus en texte brut
    return sec


def construire(path, titre, sous, h2dx, fin, nom_html):
    sec = parse(path)
    blocs = {"gloss": glossaire()}
    for i in range(1, 15):
        pid = f"p{i}"
        fiche = list(sec.get(f"{pid} fiche", []))
        fen_id = f"{prefix(nom_html)}-{pid}"
        label = sec.get(f"{pid} label", [None])
        # label stocké comme paragraphe : on le remet en lisant le fichier plus bas
        blocs[pid] = (TITRES[pid], fiche, fen_id)
    # Les labels sont dans le parse comme P() déjà. On relit les labels bruts.
    labels = labels_bruts(path)
    out = {"gloss": glossaire()}
    for i in range(1, 15):
        pid = f"p{i}"
        fid = f"{prefix(nom_html)}-{pid}"
        lab = labels.get(pid, "le détail")
        fiche = list(sec[f"{pid} fiche"])
        fiche.append(P(f"Le détail se lit dans {btn(fid, lab)}."))
        window = fen(fid, lab[:80], sec[f"{pid} fen"])
        out[pid] = (TITRES[pid], fiche, window)
    html = page(titre, sous, h2dx, out, SOURCES_HTML, fin)
    return ecrire(nom_html, html)


def prefix(nom):
    if "Phase_A" in nom:
        return "a"
    import re
    m = re.search(r"DX\.(\d+)", nom)
    return "d" + m.group(1)


def labels_bruts(path):
    labels = {}
    cur = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("# "):
            cur = line[2:].strip()
            continue
        if cur and cur.endswith(" label") and line:
            pid = cur.split()[0]
            labels[pid] = fmt(line)
    return labels


def ecrire_index():
    p = HERE.parent / "evidence" / "INDEX.md"
    p.write_text(
        "# INDEX des preuves — LOT_151\n\n"
        "Extraits lus le 31.10.2026. Les milligrammes viennent des informations professionnelles suisses, "
        "sauf mention d'une revue datée. Les faits non écrits sont dans `INCERTITUDES.md`.\n\n"
        + "\n".join(INDEX)
        + "\n",
        encoding="utf-8",
    )


def main():
    ecrire_index()
    cible = sys.argv[1] if len(sys.argv) > 1 else "A"
    if cible in ("A", "all"):
        construire(
            HERE / "contenu_a.md",
            "Bilan de coagulation anormal",
            "Cours F2.3. Le rang E n'est pas le numéro du diagnostic. Texte du 31.10.2026.",
            "",
            "FIN_FICHIER LOT_151_Phase_A",
            "LOT_151_Phase_A_V0.html",
        )
    if cible == "all" or cible.startswith("DX"):
        from dx_meta import DXS
        voulus = DXS if cible == "all" else [d for d in DXS if d["fichier"].endswith(cible + ".html") or cible in d["fichier"]]
        for d in voulus:
            construire(
                HERE / d["contenu"],
                d["nom"],
                d["sous"],
                f"DX.{d['n']} — {d['nom']}",
                f"FIN_FICHIER LOT_151_Phase_B_V0_DX.{d['n']}",
                d["fichier"],
            )


if __name__ == "__main__":
    main()
