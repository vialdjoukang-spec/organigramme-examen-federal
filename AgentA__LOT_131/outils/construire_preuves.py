#!/usr/bin/env python3
"""Construit preuves/preuves.jsonl : chaque extrait est une sous-chaîne du fichier source normalisé."""
from __future__ import annotations
import hashlib, html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "preuves" / "sources"
OUT = ROOT / "preuves" / "preuves.jsonl"
META = ROOT / "preuves" / "SOURCES.json"

def norm(s: str) -> str:
    s = html.unescape(s).replace("\u00a0", " ").replace("\u202f", " ")
    s = s.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u00b4", "'")
    return re.sub(r"\s+", " ", s).strip()

def load(name: str) -> str:
    raw = (SRC / name).read_text(encoding="utf-8", errors="replace")
    if name.endswith(".html"):
        raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
        raw = re.sub(r"<[^>]+>", " ", raw)
    return norm(raw)

FICHIERS = {
    "ped": ("EAU-Paediatric-Urology-2024.txt", "EAU Guidelines on Paediatric Urology", "2024", "Europe",
            "https://d56bochluxqnz.cloudfront.net/documents/full-guideline/EAU-Guidelines-on-Paediatric-Urology-2024.pdf"),
    "sex": ("EAU-Sexual-Reproductive-2025.txt", "EAU Guidelines on Sexual and Reproductive Health", "2025", "Europe",
            "https://d56bochluxqnz.cloudfront.net/documents/full-guideline/EAU-Guidelines-on-Sexual-and-Reproductive-Health-2025.pdf"),
    "inf": ("EAU-Infections-2025.txt", "EAU Guidelines on Urological Infections", "2025", "Europe",
            "https://d56bochluxqnz.cloudfront.net/documents/full-guideline/EAU-Guidelines-on-Urological-infections-2025_2025-05-24-110339_pxmf.pdf"),
    "pen": ("EAU-Penile-Cancer-2025.txt", "EAU-ASCO Guidelines on Penile Cancer", "2025", "Europe",
            "https://d56bochluxqnz.cloudfront.net/documents/full-guideline/EAU-ASCO-Guidelines-on-Penile-Cancer-2025.pdf"),
    "neo": ("Neoscreening-2023.txt", "Dépistage néonatal suisse, rapport annuel", "2023", "Suisse",
            "https://www.neoscreening.ch/wp-content/uploads/2024/08/Jahresbericht-2023-D.pdf"),
    "ofsp": ("OFSP-MGF.txt", "OFSP — Mesures contre les mutilations génitales féminines", "2026", "Suisse",
             "https://www.bag.admin.ch/fr/mesures-contre-les-mutilations-genitales-feminines"),
    "who": ("WHO-FGM.txt", "WHO fact sheet — Female genital mutilation", "2025", "International",
            "https://www.who.int/news-room/fact-sheets/detail/female-genital-mutilation"),
    "cp": ("Fedlex-CP-20240701.html", "Code pénal suisse, art. 124", "2024", "Suisse",
           "https://fedlex.data.admin.ch/eli/cc/54/757_781_799/20240701/fr/html"),
}

# id, clef fichier, ancre de début, longueur max, entités, points, securite
SPECS = [
    ("P01", "ped", "At birth the foreskin can be retracted in 4% of boys.", 520, ["DX.1", "Phase_A"], [1, 2, 6], False),
    ("P02", "ped", "the incidence of phimosis is 9-20% in five to thirteen year-olds and just 1% in males aged sixteen to eighteen years", 420, ["DX.1", "Phase_A"], [2], False),
    ("P03", "ped", "Physiological phimosis is most likely to resolve over time without intervention, whereas", 480, ["DX.1"], [1, 8], False),
    ("P04", "ped", "forced retraction of a narrow foreskin may cause scar formation resulting in secondary", 420, ["DX.1", "Phase_A"], [5, 6, 11, 12], True),
    ("P05", "ped", "(0.05-0.1%) can be administered twice a day over a period of 4-8 weeks with a success rate of > 80%", 520, ["DX.1"], [11], False),
    ("P06", "ped", "Contra-indications for circumcision are: an acute", 480, ["DX.1", "DX.4"], [11, 5], True),
    ("P07", "ped", "Paraphimosis must be regarded as a", 95, ["DX.1"], [5, 10, 11], True),
    ("P08", "ped", "Ballooning is not a sign of", 300, ["DX.1"], [6, 8], False),
    ("P09", "ped", "found in 14-20% of adolescents, with a similar incidence during adulthood.", 420, ["DX.2", "Phase_A"], [2], False),
    ("P10", "ped", "Varicocele is defined as an abnormal dilatation", 500, ["DX.2"], [1, 3], False),
    ("P11", "ped", "In pre-pubertal boys and in isolated right varicocele", 420, ["DX.2"], [4, 9, 10], True),
    ("P12", "ped", "a testis that is smaller by > 2 mL or 20%", 400, ["DX.2"], [6, 8, 9], False),
    ("P13", "ped", "affecting 1.0-4.6% of full-term and 1.1-45% of preterm", 480, ["DX.3", "Phase_A"], [2], False),
    ("P14", "ped", "In newborn cases with non-palpable or undescended testes on both sides", 420, ["DX.3", "DX.7", "Phase_A"], [4, 5, 11], True),
    ("P15", "ped", "If a testis has not concluded its descent at the age of six months", 520, ["DX.3"], [11, 8], True),
    ("P16", "ped", "Approximately 80%", 280, ["DX.3"], [6, 8], False),
    ("P17", "ped", "A typical dosage regimen consists of 1.2 mg per day", 360, ["DX.3"], [11], False),
    ("P18", "ped", "hCG treatment may be harmful to future spermatogenesis", 360, ["DX.3"], [11, 14], True),
    ("P19", "ped", "The total prevalence of hypospadias in Europe is 18.6 new cases per 10,000 births", 480, ["DX.4", "Phase_A"], [2], False),
    ("P20", "ped", "Most hypospadias patients are easily diagnosed at birth", 500, ["DX.4"], [1, 6, 8], False),
    ("P21", "ofsp", "En Suisse, on estime que près de 24 600 femmes et jeunes filles", 420, ["DX.5", "Phase_A"], [2], False),
    ("P22", "ofsp", "Depuis juillet 2012, les MGF sont punies en Suisse par le droit pénal (art. 124 CP).", 105, ["DX.5", "Phase_A"], [3, 11, 12], True),
    ("P23", "who", "Female genital mutilation (FGM) comprises all procedures that involve partial or total removal", 520, ["DX.5"], [1], False),
    ("P24", "who", "Female genital mutilation is classified into 4 major types", 900, ["DX.5"], [1, 8], False),
    ("P25", "who", "The practice has no health benefits for girls and women", 400, ["DX.5"], [3, 11, 13], True),
    ("P26", "who", "More than 230 million girls and women alive today have undergone female genital mutilation", 360, ["DX.5", "Phase_A"], [2], False),
    ("P27", "cp", "Quiconque mutile des organes génitaux féminins, compromet gravement et durablement", 520, ["DX.5"], [3, 11, 12], True),
    ("P28", "ped", "Acute scrotum is a paediatric urological emergency, most commonly caused by torsion of the testis", 480, ["DX.6", "Phase_A"], [1, 2, 4], False),
    ("P29", "ped", "Looking for absence of the cremasteric reflex is a simple method with 100% sensitivity", 400, ["DX.6"], [6, 8], False),
    ("P30", "ped", "persistent arterial flow does not exclude testicular torsion", 420, ["DX.6"], [9, 10], True),
    ("P31", "ped", "Severe testicular atrophy occurred after torsion for as little as four hours", 480, ["DX.6"], [3, 11, 13], True),
    ("P32", "ped", "Urgent surgical exploration is mandatory in all cases of testicular torsion within 24", 360, ["DX.6"], [10, 11], True),
    ("P33", "ped", "this should not delay the intervention.", 40, ["DX.6", "Phase_A"], [9, 10, 11], True),
    ("P34", "neo", "Adrenogenitales Syndrom (AGS) 16 259 1:10 200", 46, ["DX.7", "Phase_A"], [2, 8], False),
    ("P35", "sex", "Priapism is a persistent or prolonged erection in the absence of sexual stimulation", 420, ["DX.9"], [1], False),
    ("P36", "sex", "accounting for > 95% of all episodes", 420, ["DX.9", "Phase_A"], [1, 2], False),
    ("P37", "sex", "Ischaemic priapism that lasts beyond 4 hours is similar to a compartment syndrome", 520, ["DX.9"], [5, 10, 11, 13], True),
    ("P38", "sex", "interventions beyond 48-72 hours of onset may help to relieve", 300, ["DX.9"], [11], False),
    ("P39", "inf", "Fournier's gangrene is an aggressive and frequently fatal polymicrobial soft tissue infection", 400, ["DX.10"], [1, 3], False),
    ("P40", "inf", "The degree of internal necrosis is usually vastly greater than suggested by external signs", 480, ["DX.10"], [6, 11, 13], True),
    ("P41", "inf", "surgical debridement should be early (< 24 hours)", 420, ["DX.10"], [10, 11], True),
    ("P42", "inf", "Immediate empiric parenteral antibiotic treatment should be given", 400, ["DX.10"], [11], False),
    ("P43", "inf", "found mortality rates of 10%, 7.5% and 5%", 220, ["DX.10", "Phase_A"], [2, 11], True),
    ("P44", "pen", "with an overall incidence of around 0.94/100,000 males in Europe", 480, ["DX.8", "Phase_A"], [2], False),
    ("P45", "pen", "Squamous cell carcinoma accounts for over 95% of penile malignancies.", 260, ["DX.8"], [1, 8], False),
    ("P46", "pen", "acquiring a punch biopsy (e.g., 2-3 mm) under local", 480, ["DX.8"], [8, 9, 11], True),
    ("P47", "pen", "Phimosis is strongly associated with invasive penile cancer", 360, ["DX.8", "DX.1"], [3, 12], False),
]

def main() -> None:
    textes = {k: load(v[0]) for k, v in FICHIERS.items()}
    # Le remap ci-dessus est une erreur de brouillon : les entités sont déjà justes
    # dans SPECS après relecture (cancer = DX.8, priapisme = DX.9, Fournier = DX.10).
    rows = []
    for pid, clef, start, maxlen, entites, points, secu in SPECS:
        n = textes[clef]
        i = n.find(start)
        if i < 0:
            raise SystemExit(f"ANCRE ABSENTE {pid}: {start[:90]}")
        frag = n[i:i + maxlen]
        cut = frag.rfind(". ")
        if cut >= 40:
            frag = frag[:cut + 1]
        frag = frag.strip()
        if frag not in n:
            raise SystemExit(f"SOUS-CHAINE ROMPUE {pid}")
        fiche, titre, annee, pays, url = FICHIERS[clef]
        rows.append({
            "id": pid,
            "entites": entites,
            "points": points,
            "securite": secu,
            "source": titre,
            "annee": annee,
            "pays": pays,
            "url": url,
            "fichier": fiche,
            "consulte": "2026-11-09",
            "extrait": frag,
        })
    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    sources = []
    for clef, (fiche, titre, annee, pays, url) in FICHIERS.items():
        b = (SRC / fiche).read_bytes()
        sources.append({"clef": clef, "fichier": fiche, "titre": titre, "annee": annee, "pays": pays,
                        "url": url, "octets": len(b), "sha256": hashlib.sha256(b).hexdigest(),
                        "consulte": "2026-11-09"})
    META.write_text(json.dumps({"sources": sources, "nb_extraits": len(rows)}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(rows)} extraits, {OUT}")

if __name__ == "__main__":
    main()
