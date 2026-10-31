#!/usr/bin/env python3
"""Copie dans evidence/ des extraits réellement lus le 31.10.2026. Ne invente rien."""
from __future__ import annotations

import re
from pathlib import Path

LOT = Path("/workspace/grok-LOTS-html/LOT_136")
EV = LOT / "evidence"
SRC = Path("/tmp/aips_scan")
TOOLS = Path("/home/ubuntu/.cursor/projects/workspace/agent-tools")


def nettoyer(t: str) -> str:
    t = t.replace("\u00a0", " ").replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")
    t = t.replace("\u2019", "'").replace("\u2018", "'").replace("\u202f", " ")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?i)</?[a-z][^>]*>", " ", t)
    t = t.replace("<=", " inférieur ou égal à ").replace(">=", " supérieur ou égal à ")
    t = t.replace("<", " inférieur à ").replace(">", " supérieur à ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip() + "\n"


def ecrire(nom: str, texte: str) -> None:
    (EV / nom).write_text(nettoyer(texte), encoding="utf-8")


def coupe_aips(num: str, debut: str, fin: str | None) -> str:
    brut = (SRC / f"{num}.txt").read_text(encoding="utf-8") if False else None
    # fichiers nommés NUM_nom
    p = next(SRC.glob(f"{num}_*.txt"))
    t = p.read_text(encoding="utf-8")
    i = t.find(debut)
    if i < 0:
        raise SystemExit(f"ancre absente {num} {debut[:40]}")
    j = t.find(fin, i + len(debut)) if fin else -1
    return t[i:] if j < 0 else t[i:j]


def main() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    ecrire("profiles2023.txt", """
# PROFILES 2023, PDF Université de Genève, lu le 31.10.2026
# https://www.unige.ch/medecine/application/files/6617/5939/2636/2023_PROFILES_final_Intregre2025.pdf
# Validated on the 1st of November 2023. Mandated by the Joint Commission of Swiss Medical Schools.
Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland
SSP F1.7 bradycardia, tachycardia, irregular pulse
SSP F1.6 abnormal findings upon percussion
SSP F1.18 pulseless patient, cardiorespiratory disturbances and arrest
""")
    usz = (Path("/tmp/src136/usz.html")).read_text(encoding="utf-8", errors="replace")
    # extraits visibles déjà lus
    ecrire("usz2026_fa.txt", """
# Hôpital universitaire de Zurich, page fibrillation auriculaire, lue le 31.10.2026
# https://www.usz.ch/en/disease/atrial-fibrillation/
# Last updated on May 29, 2026. First published on April 23, 2024.
Atrial fibrillation is the most common cardiac arrhythmia. In Switzerland, around one percent of the population is affected. That is the equivalent of around 100,000 people. Heart disease is particularly common in older people. Around ten percent of people over the age of 75 suffer from atrial fibrillation.
A healthy heart beats about 60 to 100 times per minute (at rest).
The clock for the normal heart rhythm is the so-called sinus node, which is considered the natural pacemaker. It is located in the wall of the right atrium and generates the electrical excitations. The AV node, which is located at the junction between the atria and the ventricles, then transmits the electrical impulses to the heart muscles.
In atrial fibrillation, however, the electrical impulses circulate arrhythmically and rapidly in the atrium. The atria are excited at a rate of more than 350 times per minute. The sinus node itself is overrun during fibrillation and its function is no longer effective. Cardiac output therefore decreases (by approx. 20%).
Therefore, the most important therapy for patients with atrial fibrillation and additional risk factors is reliable blood thinning.
Without treatment, atrial fibrillation can have further consequences, such as a stroke due to a blood clot being carried over.
""")
    hug = (TOOLS / "b18278dc-8320-4574-9e8b-cb7749462e7c.txt").read_text(encoding="utf-8", errors="replace")
    ecrire("hug2023_fa.txt", "# Stratégie fibrillation auriculaire, Hôpitaux universitaires de Genève, document 2023, lu le 31.10.2026\n# https://www.hug.ch/sites/interhug/files/2023-09/strategie_fibrillation_auriculaire_2023.pdf\n\n" + hug[:8000])
    col = (TOOLS / "f3d19171-88c2-4fc0-a285-3158b77fe29a.txt").read_text(encoding="utf-8", errors="replace")
    ires = col.find("Overall, 42 cases of AF were detected")
    ecrire("colaus2023.txt", """
# Samim D et al. Prevalence of atrial fibrillation: The Swiss population-based CoLaus PsyCoLaus study. Herz. 2023. DOI 10.1007/s00059-021-05090-7. Lu le 31.10.2026.
# Électrocardiogramme unique, Lausanne, 2014 à 2017.
""" + col[1400:7000] + "\n\n" + col[ires:ires+2200])
    esc = (TOOLS / "6b41082e-95d6-41b6-a5df-f220f601dd25.txt").read_text(encoding="utf-8", errors="replace")
    # passages clés par ancres
    bouts = []
    for ancre in (
        "Atrial fibrillation (AF) is one of the most commonly encountered",
        "Atrial fibrillation is one of the most common heart rhythm disorders",
        "The optimal heart rate target in AF patients",
        "In acute settings, physicians should always evaluate",
        "Pharmacological rate control can be achieved with beta-blockers",
        "Atrial fibrillation is the most common sustained arrhythmia worldwide",
        "Oral anticoagulation is recommended in patients with clinical AF",
        "a All rate control drugs are contraindicated",
        "Symptoms related to episodes of AF are variable",
    ):
        i = esc.find(ancre)
        if i < 0:
            print("MANQUE ESC", ancre[:50])
            continue
        bouts.append(esc[i:i+1800])
    pdf = (TOOLS / "f1740473-1e0c-478c-84af-26c094e51a0e.txt").read_text(encoding="utf-8", errors="replace")
    for ancre in (
        "A CHA2DS2-VA score of 2 or more is recommended",
        "A CHA2DS2-VA score of 1 should be considered",
        "aAll rate control drugs are contraindicated in Wolff",
    ):
        i = pdf.find(ancre)
        if i >= 0:
            bouts.append(pdf[i:i+700])
    ecrire("esc2024_fa.txt", "# European Society of Cardiology, fibrillation auriculaire, European Heart Journal 2024, 45, 3314-3414, DOI 10.1093/eurheartj/ehae176, publié le 30 août 2024, lu le 31.10.2026.\n\n" + "\n\n".join(bouts))
    svt = (TOOLS / "69c2e59e-df07-493d-8c32-e17d9a18bf7d.txt").read_text(encoding="utf-8", errors="replace")
    i = svt.find("Adenosine, an endogenous purine")
    j = svt.find("modified Valsalva")
    ecrire("esc2019_tsv.txt", "# European Society of Cardiology, tachycardies supraventriculaires, European Heart Journal 2019, DOI 10.1093/eurheartj/ehz467, publié en ligne le 31 août 2019, lu le 31.10.2026.\n\n" + svt[max(0,i-500):i+2500] + "\n\n" + svt[max(0,j-400):j+900])
    pace = (TOOLS / "8a8a4ddc-dadf-422d-884f-5e178ac1a0dc.txt").read_text(encoding="utf-8", errors="replace")
    b2 = []
    for ancre in (
        "SND, also known as sick sinus syndrome",
        "In general, pacing for asymptomatic SND",
        "sinus bradycardia, even when it is 40",
        "The bradycardia-tachycardia variant of SND",
        "Syncope is a common manifestation of SND",
        "Second-degree Mobitz type II, 2:1, and advanced",
        "In patients with SR and permanent or paroxysmal third-",
        "In patients with SND including those with bradycardia",
    ):
        i = pace.find(ancre)
        if i < 0:
            print("MANQUE PACE", ancre[:40])
            continue
        b2.append(pace[i:i+1600])
    ecrire("esc2021_stimulation.txt", "# European Society of Cardiology, stimulation et resynchronisation, European Heart Journal 2021, 42, 3427, DOI 10.1093/eurheartj/ehab364, publié le 29 août 2021, lu le 31.10.2026.\n\n" + "\n\n".join(b2))
    erc = (TOOLS / "b7097b90-ab4a-4477-bc6b-b5925fcac5d5.txt").read_text(encoding="utf-8", errors="replace")
    b3 = []
    for ancre in (
        "Life-threatening features in an unstable patient",
        "Electrical cardioversion is the preferred treatment",
        "For atrial fibrillation:",
        "For atrial flutter and paroxysmal",
        "For ventricular tachycardia with a pulse:",
        "If bradycardia is accompanied by adverse signs",
        "If treatment with atropine is ineffective",
        "Atrial flutter and paroxysmal supraventricular tachycardia",
        "The energy required for cardioversion of VT",
        "An initial synchronised shock at maximum defibrillator output",
    ):
        i = erc.find(ancre)
        if i < 0:
            print("MANQUE ERC", ancre[:40])
            continue
        b3.append(erc[i:i+1200])
    ecrire("erc2021_arythmies.txt", "# European Resuscitation Council, réanimation spécialisée de l'adulte, Resuscitation 2021, DOI 10.1016/j.resuscitation.2021.02.010, publié en ligne le 24 mars 2021, lu le 31.10.2026.\n\n" + "\n\n".join(b3))
    # AIPS : rubriques lues
    specs = {
        "51567": ("aips_51567_krenosin.txt", "Indications/Possibilités", "Effets indésirables"),
        "56533": ("aips_56533_atropine.txt", "Indications/Possibilités", "Effet sur"),
        "41060": ("aips_41060_cordarone_iv.txt", "Indications/Possibilités", "Grossesse, allaitement"),
        "52110": ("aips_52110_beloc_zok.txt", "Indications/Possibilités", "Grossesse/Allaitement"),
        "56191": ("aips_56191_beloc_iv.txt", "Indications/Possibilités", "Grossesse/Allaitement"),
        "56457": ("aips_56457_isuprel.txt", "En cardiologie:", "Effets indésirables"),
        "61549": ("aips_61549_eliquis.txt", "Prévention de l'accident vasculaire cérébral et de l'embolie systémique chez les patients adultes", "Effets indésirables"),
        "45710": ("aips_45710_tambocor.txt", "Indications/Possibilités", "Grossesse, allaitement"),
        "45728": ("aips_45728_magnesiocard.txt", "Indications/Possibilités", "Grossesse, allaitement"),
        "56551": ("aips_56551_adrenaline.txt", "Indications/Possibilités", "Grossesse"),
    }
    for num, (nom, a, b) in specs.items():
        p = next(SRC.glob(f"{num}_*.txt"))
        t = p.read_text(encoding="utf-8")
        i = t.find(a)
        j = t.find(b, i + 20) if i >= 0 else -1
        corps = t if i < 0 else (t[i:] if j < 0 else t[i:j])
        entete = t.splitlines()[0]
        ecrire(nom, entete + "\n# Lu hors ligne le 31.10.2026 dans le corpus AIPS.\n\n" + corps)
    # grossesse eliquis est après effets dans le fichier : recopier le bloc lu
    eli = next(SRC.glob("61549_*.txt")).read_text(encoding="utf-8")
    k = eli.find("Grossesse, allaitement")
    ecrire("aips_61549_eliquis_grossesse.txt", eli.splitlines()[0] + "\n" + eli[k:k+900])
    cor = next(SRC.glob("41060_*.txt")).read_text(encoding="utf-8")
    k = cor.find("Grossesse, allaitement")
    ecrire("aips_41060_cordarone_grossesse.txt", cor.splitlines()[0] + "\n" + cor[k:k+800])
    bel = next(SRC.glob("56191_*.txt")).read_text(encoding="utf-8")
    k = bel.find("Grossesse/Allaitement")
    ecrire("aips_56191_beloc_grossesse.txt", bel.splitlines()[0] + "\n" + bel[k:k+1200])
    print("preuves", len(list(EV.glob('*.txt'))))


if __name__ == "__main__":
    main()
