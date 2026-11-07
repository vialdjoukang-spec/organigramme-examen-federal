#!/usr/bin/env python3
"""Mesures pour dimensionner le parallélisme (zéro jeton) : par agent, début, fin, durée, tokens, effort servi ; concurrence moyenne pendant sa vie."""
import json, sys, datetime as dt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); import modele_reel as mr
def ts(x): return dt.datetime.fromisoformat(x.replace("Z","+00:00")).timestamp()
s = mr.session(); d = s.with_suffix("") / "subagents"; rows = []
for meta in d.glob("agent-*.meta.json"):
    m = json.loads(meta.read_text()); j = meta.with_name(meta.name.replace(".meta.json", ".jsonl"))
    t0 = t1 = None; out = inp = cr = cw = 0; eff = mod = None; ntours = 0
    for l in open(j, encoding="utf-8"):
        try: o = json.loads(l)
        except: continue
        t = o.get("timestamp")
        if t: t0 = t0 or ts(t); t1 = ts(t)
        msg = o.get("message") or {}
        u = msg.get("usage") if isinstance(msg, dict) else None
        if u and "effort" in o:
            ntours += 1; out += u.get("output_tokens", 0); inp += u.get("input_tokens", 0)
            cr += u.get("cache_read_input_tokens", 0); cw += u.get("cache_creation_input_tokens", 0)
            eff = o.get("perTurnEffort") or o.get("effort"); mod = msg.get("model")
    if t0: rows.append(dict(desc=m.get("description",""), fini=bool(m.get("finished")), t0=t0, t1=t1, dur=t1-t0, out=out, inp=inp, cr=cr, cw=cw, eff=eff, mod=mod, tours=ntours))
for r in rows:
    pas = [r["t0"] + k*(r["dur"]/20) for k in range(21)]
    r["conc"] = sum(sum(1 for q in rows if q["t0"] <= p <= q["t1"]) for p in pas) / 21
json.dump(rows, open(sys.argv[1] if len(sys.argv) > 1 else "/dev/stdout", "w"))
