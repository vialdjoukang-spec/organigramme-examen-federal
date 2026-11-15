#!/usr/bin/env python3
"""Extrait le référentiel épidémiologique PROFILES 2023 d'une capture MHT (Google Site).
Usage : parse_mht.py <fichier.mht> <dossier_sortie>"""
import email, json, csv, re, sys, unicodedata
from collections import Counter
from bs4 import BeautifulSoup

OFFICIELLES = ["OFS", "ONEC", "OFSP", "Swissnoso", "Suva", "Obsan", "Swisstransplant",
               "Tox Info", "NICER", "SIRIS", "AMIS", "Swissmedic", "BFS", "SAKK", "Sentinella",
               "ESS", "Registre", "SwissDRG", "Promotion Santé", "Addiction Suisse", "Unisanté",
               "Cancer", "ISPM", "Swiss"]
TYPES = {"Prévalence": "prevalence", "Incidence": "incidence", "Cas annuels": "cas_annuels",
         "Effectif": "cas_annuels", "Fréq. cohorte": "cohorte", "Part du motif": "cohorte"}

def classe_source(src):
    s = src or ""
    if re.search(r"Cours PROFILES|Littérature", s, re.I) and not re.search(
            r"\b(OFS|ONEC|OFSP|Swissnoso|Suva|Obsan|Swisstransplant|Tox Info)\b", s):
        return "non_primaire"
    if re.search(r"\b(OFS|ONEC|OFSP|Swissnoso|Suva|Obsan|Swisstransplant|Tox Info|NICER|SIRIS|AMIS|Swissmedic|Sentinella)\b", s):
        return "officielle_suisse"
    return "non_primaire"

def norm(t):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", t or "")).strip()

def main(mht, out):
    msg = email.message_from_binary_file(open(mht, "rb"))
    html = None
    for p in msg.walk():
        if p.get_content_type() == "text/html":
            b = p.get_payload(decode=True) or b""
            if b"results-counter" in b:
                cs = p.get_content_charset() or "utf-8"
                html = b.decode("utf-8" if b"charset=UTF-8" in b[:600] else cs, errors="strict")
    if html is None:
        sys.exit("Tableau introuvable dans le MHT")
    soup = BeautifulSoup(html, "lxml")
    counter = norm(soup.find(id="results-counter").get_text())
    rows = []
    for tr in soup.select("#content-area tbody tr"):
        td = tr.find_all("td")
        if len(td) != 6:
            continue
        code = norm(td[0].get_text()).lstrip('↳').strip()  # « ↳ » marque la 2e mesure d'une même entité
        ent_strong = td[1].find("strong")
        entite = norm(ent_strong.get_text()) if ent_strong else norm(td[1].get_text())
        typ = norm(td[2].get_text())
        rows.append({
            "n": len(rows) + 1, "code_ssp": code, "entite": entite, "type_libelle": typ,
            "type": next((v for k, v in TYPES.items() if k in typ), "autre"),
            "valeur": norm(td[3].get_text()), "population": norm(td[4].get_text()),
            "source": norm(td[5].get_text()),
        })
    for r in rows:
        r["classe_source"] = classe_source(r["source"])
        m = re.search(r"(19|20)\d\d", r["source"]) or re.search(r"(19|20)\d\d", r["population"])
        r["annee"] = m.group(0) if m else ""
    ent = {(r["code_ssp"], r["entite"]) for r in rows}
    import itertools
    groupes = len([k for k, _ in itertools.groupby(rows, key=lambda x: (x["code_ssp"], x["entite"]))])
    ent2 = {r["entite"] for r in rows}
    c = Counter(r["type"] for r in rows)
    # compteurs affichés dans les cartes
    txt = norm(soup.get_text(" "))
    cartes = {}
    for lab, key in [("Prévalence", "prevalence"), ("Incidence", "incidence"),
                     ("Cas annuels / Effectif", "cas_annuels"), ("Part du motif / Cohorte", "cohorte")]:
        m = re.search(re.escape(lab) + r" (\d+) ", txt)
        cartes[key] = int(m.group(1)) if m else None
    rep = {"compteur_affiche": counter, "valeurs": len(rows),
           "entites_code_nom": len(ent), "entites_affichees_groupes": groupes, "entites_nom": len(ent2),
           "types": dict(c), "cartes": cartes,
           "classes": dict(Counter(r["classe_source"] for r in rows)),
           "check_221": len(rows) == 221, "check_194": groupes == 194 or len(ent) == 194,
           "check_types": all(cartes[k] == c.get(k) for k in cartes)}
    json.dump(rows, open(f"{out}/referentiel.json", "w"), ensure_ascii=False, indent=1)
    with open(f"{out}/referentiel.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    json.dump(rep, open(f"{out}/parse_rapport.json", "w"), ensure_ascii=False, indent=1)
    print(json.dumps(rep, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
