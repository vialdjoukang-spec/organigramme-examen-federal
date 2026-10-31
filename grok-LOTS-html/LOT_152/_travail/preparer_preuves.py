#!/usr/bin/env python3
"""Découpe les textes lus le 31.10.2026 vers LOT_152/evidence. Ne télécharge rien."""
from __future__ import annotations

import gzip
import re
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "evidence"
SRC = Path("/home/ubuntu/.cursor/projects/workspace/agent-tools")
AIPS = Path(__file__).resolve().parents[3] / "ressources_ia" / "aips" / "fi_fr"

FICHIERS = {
    "rms2019_thorax.txt": "cf6cd1e2-ac3b-45b4-b9fa-11f30079311f.txt",
    "rms2015_dyspnee.txt": "220bd0c9-a3d0-4f1c-b780-d3b921ebd607.txt",
    "rms2017_echo.txt": "7f7d3f08-25ef-407a-bd67-36514c5bfd71.txt",
    "rms2008_plevre.txt": "83585e38-cacb-4fea-a596-f0a2ed0e85af.txt",
    "rms2004_pno.txt": "b22dc5a2-9ad7-4e67-88da-49a9f6b83eb9.txt",
    "rms2020_main.txt": "2e0b5c5c-e1b2-44bb-8450-bac8429363e6.txt",
    "rms2008_cal.txt": "c6f99faa-9d22-4377-b820-42f4e0cdbaf8.txt",
    "rms2018_radio.txt": "0f4c057e-9b59-4d68-b569-b439394d28af.txt",
    "wses2018_asbo.txt": "f55d570b-2e2a-456f-9cc1-024fae8ef4c9.txt",
    "wses2020_ulcere.txt": "bc4bfcdb-25f6-4797-a5ab-64e8af22cfbd.txt",
}

COUPES = (
    "Comité de rédaction",
    "## References",
    "Author information",
    "Acknowledgements",
)


def nettoyer(brut: str) -> str:
    t = brut.replace("\u00a0", " ")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</(p|div|h\d|li|tr)>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = t.replace("<", " inférieur à ").replace(">", " supérieur à ")
    lignes = []
    for l in t.splitlines():
        l = " ".join(l.split())
        if not l:
            continue
        if "@" in l or l.lower().startswith("http") or "Comité de rédaction" in l:
            continue
        if any(l.startswith(c) or c in l for c in ("E-mail", "Tél.", "ISSN", "Chantal Lavanchy")):
            continue
        lignes.append(l)
    t = "\n".join(lignes)
    for c in COUPES:
        i = t.find(c)
        if i > 1500:
            t = t[:i]
            break
    return t.strip() + "\n"


def aips(num: str) -> str:
    t = gzip.open(AIPS / f"{num}.txt.gz", "rt", encoding="utf-8").read()
    t = t.replace("<", " inférieur à ").replace(">", " supérieur à ")
    entete = (
        f"Information professionnelle suisse. Numero d'autorisation {num}. "
        "Corpus AIPS local, lu le 31 octobre 2026. Swissmedic.\n\n"
    )
    return entete + t


SSI = """Recommandation suisse d'infectiologie. Pneumonie acquise en communauté. Page ssi.guidelines.ch/guideline/3007/fr lue le 31 octobre 2026. Elle s'appuie notamment sur Ewig 2021. Les posologies d'antibiotiques de cette page ne sont pas recopiées ici : elles ne sont pas la phrase de l'information professionnelle citée.

Cette recommandation concerne le diagnostic et le traitement chez l'adulte de la pneumonie acquise dans la communauté. Elle ne concerne pas la pneumonie nosocomiale ni la pneumonie chez les patients avec immunosuppression sévère.

Nouvel infiltrat pulmonaire (radiographie du thorax, échographie, ou tomodensitométrie) et symptômes cliniques d'infection respiratoire basse (fièvre, frissons, toux, expectorations, dyspnée, tachypnée, douleurs thoraciques).

Pneumonie acquise en communauté : acquisition extra-hospitalière ou, si le patient est hospitalisé, début dans les 48 heures après l'admission. Comprend les patients qui vivent dans des institutions.

Imagerie. En cas de suspicion, par exemple signe vital anormal ou auscultation pulmonaire anormale : imagerie exigée si le patient est hospitalisé, imagerie recommandée s'il est ambulatoire.

Radiographie du thorax de face et de profil pour confirmer le diagnostic : nouvel infiltrat sans diagnostic alternatif.

Alternative : échographie pulmonaire si le personnel est qualifié et si la radiographie du thorax n'est pas disponible. Elle ne visualise pas les pneumonies centrales.

Score CRB-65 en contexte ambulatoire, un point pour chaque critère. Plus de 2 points indiquent une pneumonie sévère. Confusion récente. Fréquence respiratoire égale ou supérieure à 30 par minute. Pression systolique inférieure à 90 mmHg ou pression diastolique égale ou inférieure à 60 mmHg. Âge égal ou supérieur à 65 ans.

L'hospitalisation est une décision clinique. Elle devrait être envisagée si le score CRB-65 atteint 1 point, sauf si l'âge égal ou supérieur à 65 ans est le seul critère. Indépendamment du score : hypoxémie, saturation en oxygène inférieure à 90 pour cent à l'air ambiant, comorbidités instables, complication telle qu'un épanchement pleural, facteurs sociaux.

Infiltrat multilobaire à la radiographie de thorax figure parmi les signes associés à une surveillance accrue.

Pour les patients ambulatoires, réévaluation à 48-72 heures.

La pneumonie persistante est l'absence de régression complète de l'infiltrat à la radiographie du thorax au-delà de 30 jours après le début des symptômes.
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for nom, src in FICHIERS.items():
        brut = (SRC / src).read_text(encoding="utf-8", errors="replace")
        texte = nettoyer(brut)
        (OUT / nom).write_text(texte, encoding="utf-8")
        print(f"{nom}\t{len(texte)}")
    (OUT / "ssi_pac.txt").write_text(SSI, encoding="utf-8")
    print("ssi_pac.txt", len(SSI))
    for num in ("55185", "30630", "47503"):
        p = OUT / f"aips_{num}.txt"
        p.write_text(aips(num), encoding="utf-8")
        print(p.name, p.stat().st_size)


if __name__ == "__main__":
    main()
