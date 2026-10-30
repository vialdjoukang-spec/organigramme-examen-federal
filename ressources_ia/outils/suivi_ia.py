#!/usr/bin/env python3
"""Routage et mémoire de reprise pour Codex et Grok (équivalent portable du routage et de PONS-OBLONGATA de Claude ; zéro jeton).

  python3 ressources_ia/outils/suivi_ia.py router <ia> <LOT_XXX> <fichier> <poste> <modèle> "<raison>"
      ajoute une ligne à <ia>-LOTS-html/ROUTAGE_<IA>.jsonl (poste : redacteur, auditeur-medical, auditeur-conformite, transversale)
  python3 ressources_ia/outils/suivi_ia.py capture <ia>
      relit le disque et écrit <ia>-LOTS-html/REPRISE_<IA>.md : par LOT et par fichier, étape déduite, taille T = x (+ y),
      postes déjà passés, prochaine action en une ligne
  python3 ressources_ia/outils/suivi_ia.py etat <ia>      affiche la reprise
<ia> ∈ codex, grok. À lancer en fin de passe (router) et en fin de session (capture).
"""
import datetime, json, re, sys
from pathlib import Path

R = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(R / "harnais"))
try:
    import taille_xy
except Exception:
    taille_xy = None
ZH = datetime.timezone(datetime.timedelta(hours=1))
ORDRE = ["Phase_A"] + [f"DX.{i}" for i in range(1, 11)]


def dossier(ia):
    return R / f"{ia}-LOTS-html"


def journal(ia):
    return dossier(ia) / f"ROUTAGE_{ia.upper()}.jsonl"


def router(ia, lot, fichier, poste, modele, raison):
    l = {"horodatage": datetime.datetime.now(ZH).isoformat(timespec="seconds"), "lot": lot, "fichier": fichier,
         "poste": poste, "modele": modele, "raison": raison}
    with journal(ia).open("a", encoding="utf-8") as f:
        f.write(json.dumps(l, ensure_ascii=False) + "\n")
    print("routage consigné :", l["lot"], l["fichier"], l["poste"])


def capture(ia):
    passes = {}
    if journal(ia).exists():
        for x in journal(ia).read_text(encoding="utf-8").splitlines():
            try:
                o = json.loads(x); passes.setdefault((o["lot"], o["fichier"]), []).append(o["poste"])
            except Exception:
                pass
    out = [f"# REPRISE {ia.upper()} — {datetime.datetime.now(ZH):%d.%m.%Y %H:%M}", ""]
    for d in sorted(dossier(ia).glob("LOT_[0-9][0-9][0-9]")):
        lot = d.name; out.append(f"## {lot}")
        liste = (d / "LISTE_DX_CANONIQUE.md").exists()
        for nom in ORDRE:
            f = d / (f"{lot}_Phase_A_V0.html" if nom == "Phase_A" else f"{lot}_Phase_B_V0_{nom}.html")
            p = passes.get((lot, nom), [])
            if not f.exists():
                action = "attendre le gel de LISTE_DX_CANONIQUE.md" if nom != "Phase_A" and not liste else "rédiger"
                out.append(f"- {nom} : aucun fichier → {action}"); continue
            h = f.read_text(encoding="utf-8"); fin = "FIN_FICHIER" in h
            t = ""
            if taille_xy:
                m = taille_xy.mesurer(h); t = f"T = {m.x[1]/1000:.1f} (+ {m.y[1]/1000:.1f}) Ko"
            if not fin: etape, action = "rédaction inachevée", "terminer la rédaction jusqu'à FIN_FICHIER"
            elif "auditeur-medical" not in p: etape, action = "rédigé", "audit médical (passe distincte)"
            elif "auditeur-conformite" not in p: etape, action = "audit médical fait", "audit de conformité (passe distincte)"
            else: etape, action = "audité deux fois", "passe transversale du LOT puis clôture" if nom == "DX.10" else "—"
            out.append(f"- {nom} : {etape} · {t} · postes : {', '.join(p) or 'aucun consigné'} → {action}")
        out.append("")
    (dossier(ia) / f"REPRISE_{ia.upper()}.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


def main(a):
    if len(a) >= 7 and a[0] == "router":
        router(*a[1:7])
    elif len(a) >= 2 and a[0] == "capture":
        capture(a[1])
    elif len(a) >= 2 and a[0] == "etat":
        p = dossier(a[1]) / f"REPRISE_{a[1].upper()}.md"
        print(p.read_text(encoding="utf-8") if p.exists() else "Aucune reprise : lancer capture.")
    else:
        print(__doc__); return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
