#!/usr/bin/env python3
"""Tableau de tâches d'un LOT (atomique, flock) : rédacteurs et auditeurs s'y servent eux-mêmes.
  init <LOT> <N> [fichiers_déjà_écrits...]     · prendre ecrire|audit-med|audit-conf <LOT> <label>
  fait ecrire|audit-med|audit-conf <LOT> <i>   · bilan <LOT>   · cycle2 <LOT>   · etat <LOT>
Sortie de 'prendre' : TACHE <i> <chemin> <cycle> [CORR=<rapports>]  |  ATTENDRE  |  FINI"""
import fcntl, json, re, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent
a = sys.argv[1:]; lot = a[2] if a[0] in ("prendre", "fait") else a[1]
D = R / ".cache/travail" / f"LOT_{lot}"; T = D / "taches.json"
fn = lambda i: f"LOT_{lot}_Phase_A_V0.html" if str(i) == "A" else f"LOT_{lot}_Phase_B_V0_DX.{i}.html"
rapport = lambda k, i, c: f"audits/{'MED' if k == 'med' else 'CONF'}_{fn(i)}_C{c}.md"
def lire(): return json.loads(T.read_text())
def ecrire(d): T.write_text(json.dumps(d, ensure_ascii=False, indent=1))
D.mkdir(parents=True, exist_ok=True); (D / "audits").mkdir(exist_ok=True)
with open(D / ".taches.lock", "w") as lk:
    fcntl.flock(lk, fcntl.LOCK_EX)
    if a[0] == "init":
        N = int(a[2]); deja = {str(x) for x in a[3:]}; ids = ["A"] + [str(i) for i in range(1, N + 1)]
        ch = -(-N // 3); ecrire(dict(lot=lot, N=N, cycle=1, ecrire={i: {"etat": "fait" if i in deja else "a_faire", "corr": "", "prop": "A" if i == "A" else str(1 + (int(i) - 1) // ch)} for i in ids}, med={i: "a_faire" for i in ids}, conf={i: "a_faire" for i in ids})); print("init", len(ids), "tâches")
    elif a[0] == "prendre":
        d = lire(); role = a[1]; c = d["cycle"]
        if role == "ecrire":
            W = a[4] if len(a) > 4 else None
            for i, t in d["ecrire"].items():
                if t["etat"] == "a_faire" and (W is None or t.get("prop") == W):
                    t["etat"] = "pris"; ecrire(d); print(f"TACHE {i} {D}/{fn(i)} {c}" + (f" CORR={t['corr']}" if t["corr"] else "")); break
            else: print("FINI")
        else:
            k = role.split("-")[1]
            for i in d["ecrire"]:
                if d["ecrire"][i]["etat"] == "fait" and d[k][i] == "a_faire":
                    d[k][i] = "pris"; ecrire(d); print(f"TACHE {i} {D}/{fn(i)} {c} RAPPORT={D}/{rapport(k, i, c)}"); break
            else:
                print("ATTENDRE" if any(t["etat"] != "fait" for t in d["ecrire"].values()) or any(v == "a_faire" for v in d[k].values()) else "FINI")
    elif a[0] == "fait":
        d = lire(); r = a[1]; i = a[3]
        if r == "ecrire": d["ecrire"][i]["etat"] = "fait"
        else: d[r.split("-")[1]][i] = "fait"
        ecrire(d); print("ok")
    elif a[0] in ("bilan", "cycle2"):
        d = lire(); c = d["cycle"]; res = {}
        for i in d["ecrire"]:
            r = {}
            for k in ("med", "conf"):
                p = D / rapport(k, i, c)
                m = re.search(r"RESULTAT\s+score=([\d.]+)\s+critiques=(\d+)\s+question=(oui|non)", p.read_text(encoding="utf-8")) if p.exists() else None
                r[k] = dict(score=float(m.group(1)), crit=int(m.group(2)), q=m.group(3)) if m else None
            ok = all(r[k] and r[k]["score"] >= 90 and r[k]["crit"] == 0 and r[k]["q"] == "oui" for k in r)
            res[i] = dict(ok=ok, **r)
        if a[0] == "bilan":
            sc = lambda k, ids: [res[i][k]["score"] for i in ids if res[i][k]]
            B = [i for i in res if i != "A"]
            print(json.dumps(dict(cycle=c, ok=all(v["ok"] for v in res.values()), ko=[i for i, v in res.items() if not v["ok"]], score_A=round(sum(sc("med", ["A"]) + sc("conf", ["A"])) / max(1, len(sc("med", ["A"]) + sc("conf", ["A"]))), 1), score_B=round(sum(sc("med", B) + sc("conf", B)) / max(1, len(sc("med", B) + sc("conf", B))), 1)), ensure_ascii=False))
        else:
            ko = [i for i, v in res.items() if not v["ok"]]; d["cycle"] = c + 1
            for i in ko:
                d["ecrire"][i] = {"etat": "a_faire", "prop": d["ecrire"][i].get("prop"), "corr": f"{D}/{rapport('med', i, c)} {D}/{rapport('conf', i, c)}"}; d["med"][i] = d["conf"][i] = "a_faire"
            for i in d["ecrire"]:
                if i not in ko: d["med"][i] = d["conf"][i] = "fait"
            ecrire(d); print("cycle", c + 1, "pour", ko)
    elif a[0] == "etat": print(json.dumps(lire(), ensure_ascii=False))
