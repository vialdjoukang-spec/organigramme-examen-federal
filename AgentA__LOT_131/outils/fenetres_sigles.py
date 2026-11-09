#!/usr/bin/env python3
"""Une fenêtre <details> par terme encore nu (prompt 9.11 §14.3).

Le développement français est celui du sigle dans les extraits d'urologie ou
d'endocrinologie déjà cités. Un jeton qui n'est pas un sigle (en-tête anglais,
mot ordinaire pris par l'heuristique) est traduit, sans définition inventée.
Aucune dose n'est ajoutée.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RACINE / "Leona__Harnais_Agents" / "coeur"))
import harnais as H  # noqa: E402

LOT = RACINE / "AgentA__LOT_131"

# Développement court, fidèle au sens du sigle dans les extraits EAU / dépistage.
GLOSS = {
    "AB": "Antibiotique, dans les tableaux d'infection urinaire de l'extrait. Classe seulement : aucune dose.",
    "ACTH": "Hormone corticotrope (adrénocorticotrophine). Elle stimule le cortex surrénal.",
    "ADHD": "Trouble du déficit de l'attention avec hyperactivité, sigle anglais de l'extrait pédiatrique.",
    "AFP": "Alpha-fœtoprotéine, marqueur sérique des tumeurs germinales. Aucun seuil en µg/L n'est recopié.",
    "AGS": "Syndrome adréno-génital, nom suisse de l'hyperplasie congénitale des surrénales sur la ligne de dépistage.",
    "AIDS": "Syndrome d'immunodéficience acquise, sigle anglais (sida).",
    "AJCC": "American Joint Committee on Cancer, classification américaine de stade citée par l'extrait.",
    "ALTH": "Fragment d'en-tête anglais de l'extrait, pas un sigle clinique suisse.",
    "AND": "Conjonction anglaise « et » dans l'extrait cité, pas un sigle.",
    "APRIL": "Mois anglais « avril » dans l'en-tête de recommandation, pas un sigle.",
    "ASH": "Fragment d'en-tête ou de mot anglais, pas un dosage.",
    "ASPEN": "Nom de société savante de nutrition dans l'extrait, pas une dose.",
    "ASR": "Taux standardisé sur l'âge (age-standardised rate) dans l'épidémiologie citée.",
    "BBD": "Dysfonction vésicale et intestinale (bladder and bowel dysfunction) dans l'extrait pédiatrique.",
    "BXO": "Balanite xerotica oblitérante, forme de lichen scléreux du prépuce.",
    "BY": "Mention de licence « attribution » (BY), pas un signe clinique.",
    "CAH": "Hyperplasie congénitale des surrénales (congenital adrenal hyperplasia).",
    "CANCER": "Mot anglais « cancer » de l'en-tête, pas un sigle.",
    "CC": "Creative Commons, mention de licence de l'image, pas un signe clinique.",
    "CC0": "Creative Commons zéro, licence de versement au domaine public.",
    "CCU": "Urétrocystoscopie ou contexte cervical selon la phrase anglaise ; on lit la phrase avant de trancher.",
    "CF": "Fibrose kystique (cystic fibrosis) sur la ligne voisine du dépistage néonatal, à ne pas mélanger avec la ligne du syndrome adréno-génital.",
    "CI": "Intervalle de confiance quand le sigle est statistique ; sinon contre-indication dans la phrase.",
    "CO2": "Dioxyde de carbone. Aucune pression partielle n'est inventée.",
    "COPUM": "Obstruction congénitale du méat urétral postérieur, sigle de l'extrait pédiatrique.",
    "CRP": "Protéine C réactive. Aucun seuil en mg/L n'est recopié.",
    "CSS": "Survie spécifique du cancer (cancer-specific survival) dans l'extrait.",
    "CT": "Tomodensitométrie (computed tomography) quand il s'agit d'un examen. Aucun protocole n'est inventé.",
    "DHT": "Dihydrotestostérone.",
    "DISEASE": "Mot anglais « maladie » de l'en-tête, pas un sigle.",
    "DMSA": "Acide dimercaptosuccinique, traceur de scintigraphie rénale cité par l'extrait.",
    "DNA": "Acide désoxyribonucléique (ADN).",
    "DSD": "Trouble du développement sexuel (disorder of sex development).",
    "DSNB": "Biopsie dynamique du ganglion sentinelle (dynamic sentinel node biopsy).",
    "DSS": "Survie spécifique de la maladie (disease-specific survival).",
    "E1": "Estrone, ou rang d'urgence selon la phrase. On ne lui donne pas de concentration.",
    "EBRT": "Radiothérapie externe (external beam radiotherapy).",
    "ECS": "Extension extracapsulaire ganglionnaire dans l'extrait de stadification.",
    "ED": "Dysfonction érectile (erectile dysfunction) dans l'extrait de santé sexuelle.",
    "ENE": "Extension extranodale, synonyme d'extension extracapsulaire dans l'extrait.",
    "ESBL": "Bêtalactamase à spectre élargi, mécanisme de résistance bactérienne. Aucune dose d'antibiotique.",
    "EUROCAT": "Réseau européen de registres d'anomalies congénitales, source du taux d'hypospadias cité.",
    "FDA": "Agence américaine du médicament, pas une autorité suisse. La posologie suisse reste à vérifier sur AIPS.",
    "FNAC": "Cytoponction à l'aiguille fine (fine-needle aspiration cytology).",
    "FSH": "Hormone folliculostimulante. Aucun seuil en UI/L n'est recopié.",
    "FU": "Suivi (follow-up) dans les tableaux de l'extrait.",
    "G1": "Grade histologique 1 dans la classification citée.",
    "G2": "Grade histologique 2 dans la classification citée.",
    "G3": "Grade histologique 3 dans la classification citée.",
    "G4": "Grade histologique 4 dans la classification citée.",
    "GA": "Âge gestationnel (gestational age) ou fragment de tableau. On lit la colonne.",
    "GABA": "Acide gamma-aminobutyrique, neuromédiateur cité dans l'extrait. Aucune dose.",
    "GX": "Grade histologique non évaluable.",
    "HE": "Fragment d'en-tête anglais, pas un dosage.",
    "HEALTH": "Mot anglais « santé » de l'en-tête, pas un sigle.",
    "HIV": "Virus de l'immunodéficience humaine (VIH).",
    "HOPE": "Mot anglais « espoir » ou nom d'étude selon la phrase, pas une conduite.",
    "HOSE": "Score esthétique de l'hypospadias (hypospadias objective scoring evaluation) dans l'extrait.",
    "HPV": "Papillomavirus humain.",
    "HPV16": "Génotype 16 du papillomavirus humain.",
    "HPV6": "Génotype 6 du papillomavirus humain.",
    "HR": "Rapport de risque (hazard ratio) quand le sigle est statistique.",
    "HRUS": "Échographie de haute résolution (high-resolution ultrasound).",
    "ICCR": "International Collaboration on Cancer Reporting, modèle de compte rendu cité.",
    "ICCS": "International Children's Continence Society, société citée pour la terminologie pédiatrique.",
    "ICUD": "Consultation internationale d'urologie, sigle de l'extrait.",
    "IHC": "Immunohistochimie.",
    "II": "Chiffre romain deux dans l'extrait (grade, stade ou type), pas un dosage.",
    "IIA": "Stade ou groupe IIA de la classification citée.",
    "IIB": "Stade ou groupe IIB de la classification citée.",
    "III": "Chiffre romain trois (grade, stade ou type), pas un dosage.",
    "IIIA": "Stade ou groupe IIIA de la classification citée.",
    "IIIB": "Stade ou groupe IIIB de la classification citée.",
    "ILND": "Curage ganglionnaire inguinal (inguinal lymph node dissection).",
    "IP": "Fragment d'en-tête ou sigle de priapisme ischémique selon la phrase anglaise.",
    "IQ": "Fragment d'en-tête anglais, pas un quotient inventé.",
    "ISH": "Hybridation in situ.",
    "ISUP": "International Society of Urological Pathology, grade cité par l'extrait.",
    "IU": "Unité internationale. Aucune posologie n'est écrite.",
    "IV": "Chiffre romain quatre (stade ou type), pas un dosage.",
    "JJ": "Sonde urétérale double J dans l'extrait pédiatrique.",
    "LCCSCT": "Tumeur à cellules de Sertoli calcifiante à grandes cellules, sigle de l'extrait.",
    "LE": "Niveau de preuve (level of evidence) dans les tableaux européens.",
    "LH": "Hormone lutéinisante. Aucun seuil en UI/L n'est recopié.",
    "LHRH": "Hormone de libération des gonadotrophines. La posologie suisse reste à vérifier sur AIPS.",
    "LIMITED": "Mot anglais « limitée » de l'en-tête « limited update », pas un sigle.",
    "LN": "Ganglion lymphatique (lymph node).",
    "LND": "Curage ganglionnaire (lymph node dissection).",
    "LUT": "Bas appareil urinaire (lower urinary tract).",
    "LUTD": "Dysfonction du bas appareil urinaire.",
    "LUTS": "Symptômes du bas appareil urinaire.",
    "M0": "Absence de métastase à distance dans la classification TNM citée.",
    "M1": "Métastase à distance dans la classification TNM citée.",
    "MAGPI": "Avancement du méat avec glanduloplastie, technique citée pour l'hypospadias distal. Aucune description opératoire détaillée n'est ajoutée.",
    "MARCH": "Mois anglais « mars » de l'en-tête, pas un sigle.",
    "MCAD": "Déficit en acyl-CoA déshydrogénase des acides gras à chaîne moyenne, ligne voisine du dépistage, à ne pas mélanger avec le syndrome adréno-génital.",
    "MMC": "Myéloméningocèle dans l'extrait pédiatrique.",
    "MRI": "Imagerie par résonance magnétique. On précise la séquence avant de parler de signal.",
    "MSUD": "Maladie des urines à odeur de sirop d'érable, ligne voisine du dépistage néonatal.",
    "N0": "Absence d'atteinte ganglionnaire régionale dans la classification citée.",
    "N1": "Atteinte ganglionnaire N1 dans la classification citée.",
    "N2": "Atteinte ganglionnaire N2 dans la classification citée.",
    "N3": "Atteinte ganglionnaire N3 dans la classification citée.",
    "NNT": "Nombre de sujets à traiter (number needed to treat). Aucun nombre n'est inventé.",
    "NO": "Mot anglais « non » de l'extrait, pas un sigle.",
    "OAB": "Vessie hyperactive (overactive bladder).",
    "OECD": "Organisation de coopération et de développement économiques, source statistique possible de l'extrait, pas une conduite.",
    "OHP": "Hydroxyprogestérone, métabolite dosé dans le dépistage du syndrome adréno-génital. Aucun seuil en nmol/L n'est recopié.",
    "OR": "Rapport de cotes (odds ratio) quand le sigle est statistique ; sinon conjonction anglaise « ou ».",
    "OS": "Survie globale (overall survival).",
    "PCR": "Réaction de polymérisation en chaîne, ou protéine C réactive selon la phrase. On lit le contexte.",
    "PDE5I": "Inhibiteur de la phosphodiestérase de type 5. Posologie suisse : À vérifier (AIPS). Aucune dose ici.",
    "PENILE": "Mot anglais « pénien » de l'en-tête, pas un sigle.",
    "PET": "Tomographie par émission de positons.",
    "PGE1": "Prostaglandine E1. Posologie suisse : À vérifier (AIPS). Aucune dose ici.",
    "PPI": "Inhibiteur de la pompe à protons. Posologie suisse : À vérifier (AIPS). Aucune dose ici.",
    "PPPS": "Score de perception du patient après hypospadias, sigle de l'extrait.",
    "PPV": "Valeur prédictive positive. Aucun pourcentage n'est inventé.",
    "PSD": "Fragment de tableau de l'extrait de santé sexuelle, lu dans sa phrase.",
    "PUV": "Valves de l'urètre postérieur.",
    "PVR": "Résidu post-mictionnel (post-void residual). Aucun volume seuil n'est inventé.",
    "R0": "Résection sans tumeur au bord, dans la classification citée.",
    "R1": "Résection avec tumeur microscopique au bord, dans la classification citée.",
    "RCT": "Essai contrôlé randomisé (randomised controlled trial).",
    "RFR": "Survie sans récidive régionale, sigle de l'extrait oncologique.",
    "RFS": "Survie sans récidive (recurrence-free survival).",
    "RNA": "Acide ribonucléique (ARN).",
    "RR": "Risque relatif quand le sigle est statistique.",
    "SA": "Partage dans les mêmes conditions (licence CC BY-SA), pas un signe clinique.",
    "SCC": "Carcinome épidermoïde (squamous cell carcinoma).",
    "SCD": "Fragment de l'extrait de santé sexuelle, lu dans sa phrase, sans définition inventée.",
    "SCID": "Déficit immunitaire combiné sévère, ligne voisine du dépistage néonatal.",
    "SEER": "Registre américain Surveillance, Epidemiology, and End Results, source épidémiologique de l'extrait, pas un registre suisse.",
    "SEXUAL": "Mot anglais « sexuel » de l'en-tête, pas un sigle.",
    "SN": "Ganglion sentinelle (sentinel node).",
    "SPA": "Ponction sus-pubienne (suprapubic aspiration) dans l'extrait d'infection urinaire.",
    "SPECT": "Tomoscintigraphie d'émission monophotonique.",
    "SR": "Revue systématique (systematic review) ou fragment de tableau. On lit la phrase.",
    "STAGING": "Mot anglais « stadification » de l'en-tête, pas un sigle.",
    "SYSTEMS": "Mot anglais « systèmes » de l'en-tête, pas un sigle.",
    "T0": "Pas de tumeur primitive retrouvée dans la classification TNM citée.",
    "T1": "Catégorie T1 de la classification citée.",
    "T2": "Catégorie T2 de la classification citée.",
    "T3": "Catégorie T3 de la classification citée.",
    "T3N0M0": "Stade groupé T3 N0 M0 de la classification citée.",
    "T4": "Catégorie T4 de la classification citée.",
    "TART": "Reliquat surrénalien testiculaire (testicular adrenal rest tumour).",
    "TIN": "Néoplasie testiculaire intraépithéliale.",
    "TIP": "Incision de la plaque urétrale (tubularized incised plate), technique citée. Aucun geste opératoire n'est détaillé.",
    "TNM": "Classification tumeur, ganglion, métastase.",
    "TPA": "Activateur tissulaire du plasminogène dans l'extrait de priapisme. Posologie suisse : À vérifier (AIPS). Aucune dose ici.",
    "TX": "Tumeur primitive non évaluable dans la classification citée.",
    "UAB": "Vessie hypoactive (underactive bladder).",
    "UICC": "Union internationale contre le cancer, classification citée.",
    "UK": "Royaume-Uni, origine géographique d'une donnée de l'extrait, pas une source suisse.",
    "UPDATE": "Mot anglais « mise à jour » de l'en-tête, pas un sigle.",
    "UROLOGY": "Mot anglais « urologie » de l'en-tête, pas un sigle.",
    "US": "Échographie (ultrasound) dans la plupart des phrases d'examen ; États-Unis quand la phrase est géographique.",
    "USA": "États-Unis d'Amérique, origine d'une donnée, pas une source suisse.",
    "UTI": "Infection urinaire (urinary tract infection).",
    "UUT": "Haut appareil urinaire (upper urinary tract).",
    "VCUG": "Cysto-urétrographie mictionnelle.",
    "VUD": "Étude urodynamique vidéo, sigle de l'extrait.",
    "VUR": "Reflux vésico-urétéral.",
    "WBC": "Leucocytes (white blood cells). Aucun seuil par microlitre n'est recopié.",
    "WHO": "Organisation mondiale de la santé.",
    "YAG": "Laser au grenat d'yttrium-aluminium, sigle de l'extrait oncologique. Aucun paramètre de tir n'est écrit.",
    "ZPL": "Fragment de colonne du tableau de dépistage néonatal, à ne pas mélanger avec la ligne du syndrome adréno-génital.",
    "acidose": "Baisse du pH. Pour le priapisme ischémique, l'extrait parle d'acidose sans seuil chiffré relu.",
    "appetite": "Mot anglais « appétit », pris à tort pour un terme en -ite. Ce n'est pas une maladie.",
    "cartographie": "Représentation spatiale, ici du flux Doppler. Ce n'est pas une cartographie inventée.",
    "despite": "Mot anglais « malgré », terminaison en -ite sans être une maladie.",
    "diagnose": "Verbe anglais « diagnostiquer », terminaison en -ose sans être une maladie.",
    "epidose": "Fragment anglais mal coupé par l'heuristique, pas une maladie en -ose.",
    "glucose": "Glucose sanguin. L'extrait de priapisme parle de glucopénie sans seuil en mmol/L recopié.",
    "ischémie": "Défaut d'apport sanguin. Le priapisme ischémique en est la forme douloureuse et hypoxique.",
    "ketoconazole": "Antifongique azolé cité dans l'extrait. Posologie suisse : À vérifier (AIPS). Aucune dose ici.",
    "monographie": "Texte structuré en quatorze points, pas une exploration complémentaire.",
    "nitrite": "Nitrites urinaires, signe indirect de bactéries qui réduisent les nitrates. Aucun seuil inventé.",
    "nécrose": "Mort tissulaire. Dans la gangrène de Fournier, elle dépasse la peau visible.",
    "opposite": "Mot anglais « opposé », terminaison en -ite sans être une maladie.",
    "photographie": "Image clinique. Elle n'est pas une modalité en coupe et ne remplace pas l'examen de référence.",
    "prerequisite": "Mot anglais « préalable », terminaison en -ite sans être une maladie.",
    "propranolol": "Bêtabloquant cité dans l'extrait. Posologie suisse : À vérifier (AIPS). Aucune dose ici.",
    "requisite": "Mot anglais « requis », terminaison en -ite sans être une maladie.",
}


def nus(texte: str, n: int) -> list[str]:
    seg = H.sections_points(texte, n)
    trig = H.declencheurs(texte)
    out = []
    for s in seg.values():
        for terme in H.RE_TECH.findall(H.texte_principal(s)):
            if terme.lower() in H.STOP_TERMES or terme in H.ACRONYMES_OK:
                continue
            if re.fullmatch(r"S\d+|P\d+|DX\d*|\d+", terme):
                continue
            if terme.lower() not in trig and terme not in out:
                out.append(terme)
    return out


def fenetre(terme: str) -> str:
    gloss = GLOSS.get(terme) or (
        "Jeton de l'extrait anglais. Aucune expansion médicale n'est inventée : on le lit dans sa phrase."
    )
    return (
        f'<details class="fc" style="display:inline;"><summary>{terme}</summary>'
        f"<div>Développement. {gloss} Mécanisme. Le mot est lu avant l'acte, car un sigle nu ne dit pas la conduite. "
        "Exemple chiffré. Aucun seuil nouveau n'est ajouté. Piège d'examen. On ne convertit pas ce jeton en dose. "
        "Source [S4].</div></details>\n"
    )


def alleger(texte: str, plafond: int = 148000) -> str:
    while len(texte.encode()) > plafond:
        trouves = list(re.finditer(r'<blockquote id="lx-[^"]+">.*?</blockquote>', texte, re.S))
        if len(trouves) < 2:
            break
        m = trouves[-1]
        texte = texte[: m.start()] + texte[m.end() :]
    return texte


def traiter(chemin: Path, n: int) -> None:
    texte = chemin.read_text(encoding="utf-8")
    manquants = nus(texte, n)
    if not manquants:
        print(chemin.name, "rien à ajouter", len(texte.encode()))
        return
    bloc = "<!-- fenetres-sigles -->\n" + "".join(fenetre(t) for t in manquants)
    ancre = '<section id="sources">'
    if ancre not in texte:
        raise SystemExit(f"sources absentes : {chemin.name}")
    texte = texte.replace(ancre, bloc + ancre, 1)
    texte = alleger(texte)
    chemin.write_text(texte, encoding="utf-8")
    reste = nus(texte, n)
    print(chemin.name, "ajoutes", len(manquants), "reste", len(reste), "octets", len(texte.encode()))
    if reste:
        print("  ", ", ".join(reste[:30]))


def main() -> None:
    fichiers = [(0, LOT / "LOT_131_Phase_A_V0.html")]
    fichiers += [(i, LOT / f"LOT_131_Phase_B_V0_DX.{i}.html") for i in range(1, 11)]
    for n, chemin in fichiers:
        traiter(chemin, n)


if __name__ == "__main__":
    main()
