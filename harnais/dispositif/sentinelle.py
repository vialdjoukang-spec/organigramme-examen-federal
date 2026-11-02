#!/usr/bin/env python3
"""Sentinelle des effectifs : rédacteurs (3 obligatoires tant qu'il reste du travail), auditeurs (1 à 2).
Sortie : une ligne à chaque CHANGEMENT d'état (pour Monitor) + .cache/harnais/sentinelle.json (lu par le tableau de bord).
  python3 harnais/dispositif/sentinelle.py [période_s=5]"""
import glob, json, os, sys, time
from pathlib import Path
R = Path(__file__).resolve().parents[2]; WF = Path.home() / ".claude/projects/-home-user-organigramme-examen-federal"
def agents():
    now = time.time(); out = []
    for jf in glob.glob(str(WF / "*/subagents/workflows/wf_*/journal.jsonl")):
        if now - os.path.getmtime(jf) > 3 * 3600: continue
        d = Path(jf).parent; st = {}
        for l in open(jf):
            try: e = json.loads(l)
            except Exception: continue
            if e.get("type") == "started": st[e["agentId"]] = e["label"]
            elif e.get("type") == "result": st.pop(e["agentId"], None)
        for i, lab in st.items():
            j = d / f"agent-{i}.jsonl"; m = d / f"agent-{i}.meta.json"
            if j.exists() and now - j.stat().st_mtime <= 180:
                try: tp = json.loads(m.read_text()).get("agentType", "")
                except Exception: tp = ""
                out.append((tp, lab))
    return out
def taches():
    p = sorted(glob.glob(str(R / ".cache/travail/LOT_*/taches.json")), key=os.path.getmtime)
    if not p: return None
    d = json.load(open(p[-1])); e = d["ecrire"]
    return dict(lot=d["lot"], cycle=d["cycle"], total=len(e), a_faire=sum(v["etat"] == "a_faire" for v in e.values()), pris=sum(v["etat"] == "pris" for v in e.values()),
                a_auditer=sum(1 for i in e if e[i]["etat"] == "fait" and (d["med"][i] != "fait" or d["conf"][i] != "fait")))
last = None; per = float(sys.argv[1]) if len(sys.argv) > 1 else 5
while True:
    ag = agents(); tk = taches()
    red = sum(t in ("redacteur", "redacteur-phase-a") for t, _ in ag); au = sum(t in ("auditeur-medical", "auditeur-conformite") for t, _ in ag)
    al = []
    if tk:
        reste = tk["a_faire"] + tk["pris"]
        if reste >= 1 and tk["total"] > 10 and red < min(8, reste): al.append(f"RÉDACTEURS {red}/8 (reste {reste} fichiers) → RELANCER ecrire.js")
        if red > 8: al.append(f"RÉDACTEURS {red} > 8")
    e = dict(t=time.strftime("%H:%M:%S"), redacteurs=red, auditeurs=au, taches=tk, alertes=al)
    (R / ".cache/harnais/sentinelle.json").write_text(json.dumps(e, ensure_ascii=False))
    s = json.dumps([red, au, al]) 
    if s != last: print(f"{e['t']} rédacteurs={red} auditeurs={au} " + ("ALERTE " + " | ".join(al) if al else "OK"), flush=True); last = s
    time.sleep(per)
