#!/usr/bin/env python3
"""BRAIN-HARNESS · construit harnais/brain/BRAIN_3D.html (vue 3D animée, hors ligne, sans bibliothèque) depuis le gabarit brain_3d_modele.html.
  python3 harnais/brain/outils/construire_3d.py [--journal F.jsonl] [--sortie F.html]
Données injectées : registre des 160 scriptones (registre.json), paramètres des 28 synapses (synapses.json), police Atkinson (atkinson.b64.json)
et un journal d'événements brain.evenement/1 (défaut : harnais/brain/journal_exemple.jsonl, produit par orchestre.py sur le doré et 4 cours réels).
La page lit aussi un autre journal : bouton « Charger », glisser-déposer, ou ?journal=URL quand elle est servie en HTTP."""
import json, sys
from pathlib import Path
B = Path(__file__).resolve().parents[1]
R = B.parents[1]
GARDE = ("id", "fichier", "zone", "synapse", "point", "famille", "region", "signal", "nom", "fonction", "entree", "sortie", "ecrit", "jumeau", "etat", "langage", "sha256", "mutants", "doleances_vial")


def journal(p):
    out = []
    for l in Path(p).read_text(encoding="utf-8").splitlines():
        l = l.strip()
        if not l: continue
        try: e = json.loads(l)
        except ValueError: continue
        if isinstance(e, dict) and {"type", "de", "vers"} <= set(e): out.append(e)
    return out


def donnees(jp):
    reg = json.loads((B / "scriptones/registre.json").read_text(encoding="utf-8"))
    syn = json.loads((B / "scriptones/synapses.json").read_text(encoding="utf-8"))
    sc = []
    for e in reg["scriptones"]:
        x = {k: e.get(k) for k in GARDE}; x["sha256"] = (x["sha256"] or "")[:12]; x["mutants"] = [m[1] for m in (e.get("mutants") or [])]; sc.append(x)
    pts = {int(k): dict(titre=v["titre"], court=v.get("court", v["titre"])) for k, v in syn["points"].items()}
    return dict(version=reg.get("version"), total=reg.get("total"), scriptones=sc, points=pts, fam_a=syn["familles_alpha"], fam_b=syn["familles_beta"],
                jumeaux=syn["jumeaux"], journal=journal(jp), journal_nom=Path(jp).name)


def construire(jp=B / "journal_exemple.jsonl", sortie=B / "BRAIN_3D.html"):
    t = (B / "outils/brain_3d_modele.html").read_text(encoding="utf-8")
    F = json.loads((R / "harnais/atkinson.b64.json").read_text(encoding="utf-8"))
    fontes = "".join(f'@font-face{{font-family:"Atkinson Hyperlegible";font-weight:{w};font-display:swap;src:url("data:font/woff2;base64,{F[w]}") format("woff2")}}\n' for w in ("400", "700"))
    d = json.dumps(donnees(jp), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    assert "/*@DONNEES@*/" in t and "/*@FONTES@*/" in t
    Path(sortie).write_text(t.replace("/*@FONTES@*/", fontes).replace("/*@DONNEES@*/null", d), encoding="utf-8")
    return sortie


if __name__ == "__main__":
    a = sys.argv
    jp = Path(a[a.index("--journal") + 1]) if "--journal" in a else B / "journal_exemple.jsonl"
    so = Path(a[a.index("--sortie") + 1]) if "--sortie" in a else B / "BRAIN_3D.html"
    p = construire(jp, so); print(f"{p} · {p.stat().st_size // 1024} Ko")
