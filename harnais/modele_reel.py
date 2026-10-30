#!/usr/bin/env python3
"""Modèle et effort RÉELLEMENT servis, lus dans les transcriptions de Claude Code (zéro jeton). Article 4 : aucune déclaration sans preuve.

  python3 harnais/modele_reel.py etat [--tout]     agents en cours (ou tous) : modèle demandé, modèle servi, effort servi, écart au contrat
  python3 harnais/modele_reel.py ecarts            seulement les écarts au contrat (code de sortie 1 s'il y en a un en cours)
  python3 harnais/modele_reel.py rapport           écrit journal/MODELE_REEL.md (tous les agents de la session, vérité servie)
  python3 harnais/modele_reel.py veille [s]        boucle : imprime une ligne à chaque agent nouveau, terminé ou en écart ; réécrit le rapport

Source de vérité : chaque ligne de transcription porte `message.model` (modèle servi) et `effort` / `perTurnEffort` (effort servi).
Contrat (journal/routage.jsonl, .claude/agents/*.md) : rédaction, refonte et audit médical = Opus · xhigh ; conformité = Sonnet · high ; mécanique = Haiku · medium.
"""
import json, os, re, sys, time
from pathlib import Path

R = Path(__file__).resolve().parents[1]
PROJ = Path.home() / ".claude" / "projects" / ("-" + str(R).strip("/").replace("/", "-"))
EN_COURS_S = 600  # sans « finished » et écrit il y a moins de 10 min = en cours

CONTRAT = [  # (motif sur type ou description, famille de modèle, effort)
    (r"auditeur-conformite|conformit", "sonnet", "high"),
    (r"mecanique|captures|copie|inventaire", "haiku", "medium"),
    (r"refonte|audit|r[ée]dact|redacteur|phase a|dx\.", "opus", "xhigh"),
]


def session():
    js = sorted(PROJ.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    if not js:
        sys.exit(f"aucune session sous {PROJ}")
    return js[-1]


def servi(fichier):
    """Dernier (modèle servi, effort servi, horodatage) et compte des tours par (modèle, effort)."""
    dernier, tours = (None, None, None), {}
    try:
        with open(fichier, encoding="utf-8") as f:
            for l in f:
                if '"effort"' not in l:
                    continue
                try:
                    o = json.loads(l)
                except Exception:
                    continue
                m = (o.get("message") or {}).get("model") or o.get("requestedModel")
                e = o.get("perTurnEffort") or o.get("effort")
                if m:
                    dernier = (m, e, o.get("timestamp"))
                    tours[(m, e)] = tours.get((m, e), 0) + 1
    except FileNotFoundError:
        pass
    return dernier, tours


def contrat(texte):
    t = texte.lower()
    for motif, fam, eff in CONTRAT:
        if re.search(motif, t):
            return fam, eff
    return None, None


def statuts(s):
    """Dernier statut notifié par agent (completed, killed, failed) dans la session principale."""
    st = {}
    try:
        t = s.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return st
    for m in re.finditer(r"<task-id>(\w+)</task-id>.{0,400}?<status>(\w+)</status>", t, re.S):
        st[m.group(1)] = m.group(2)
    return st


def agents():
    s = session()
    d = s.with_suffix("") / "subagents"
    st = statuts(s)
    out = []
    for meta in sorted(d.glob("agent-*.meta.json"), key=lambda p: p.stat().st_mtime):
        try:
            m = json.loads(meta.read_text())
        except Exception:
            continue
        j = meta.with_name(meta.name.replace(".meta.json", ".jsonl"))
        (mod, eff, ts), tours = servi(j)
        age = time.time() - j.stat().st_mtime if j.exists() else 1e9
        aid = meta.name[6:-10]
        notif = st.get(aid)
        etat = ("terminé" if m.get("finished") or notif == "completed" else "arrêté" if notif in ("killed", "failed", "stopped")
                else "en cours" if age < EN_COURS_S else "arrêté")
        fam, eff_c = contrat(f"{m.get('agentType','')} {m.get('description','')}")
        ecart = []
        if fam and mod and fam not in mod:
            ecart.append(f"modèle {mod} ≠ {fam}")
        if eff_c and eff and eff != eff_c:
            ecart.append(f"effort {eff} ≠ {eff_c}")
        out.append(dict(id=meta.name[6:-10], desc=m.get("description", ""), type=m.get("agentType", ""),
                        demande=f"{m.get('model','hérité')} · {m.get('effort','non passé')}", servi=f"{mod} · {eff}",
                        tours=tours, etat=etat, ecart="; ".join(ecart), ts=ts or ""))
    (pm, pe, pts), _ = servi(s)
    return dict(principal=f"{pm} · {pe}", principal_ts=pts), out


def ligne(a):
    return f"{a['etat']:<9} {a['servi']:<24} demandé {a['demande']:<18} {a['desc'][:52]:<52} {('⚠ ' + a['ecart']) if a['ecart'] else 'conforme'}"


def etat(tout=False):
    p, ags = agents()
    print(f"Session principale : {p['principal']} (dernier tour {p['principal_ts']})")
    sel = ags if tout else [a for a in ags if a["etat"] == "en cours"]
    print(f"{len(sel)} agent(s) {'au total' if tout else 'en cours'}")
    for a in sel:
        print(ligne(a))
    return sel


def ecarts():
    _, ags = agents()
    e = [a for a in ags if a["ecart"]]
    for a in e:
        print(ligne(a))
    return 1 if any(a["etat"] == "en cours" for a in e) else 0


def rapport():
    p, ags = agents()
    n_e = sum(1 for a in ags if a["ecart"])
    t = ["# Modèle et effort réellement servis — vérité lue dans les transcriptions (Article 4)", "",
         f"Relevé {time.strftime('%d.%m.%Y %H:%M')} · session principale : **{p['principal']}** · {len(ags)} agents · **{n_e} en écart au contrat**.", "",
         "| État | Agent | Demandé | Servi (dernier tour) | Tours par modèle · effort | Contrat |", "|---|---|---|---|---|---|"]
    for a in reversed(ags):
        tours = ", ".join(f"{m} · {e} : {n}" for (m, e), n in a["tours"].items())
        t.append(f"| {a['etat']} | {a['desc']} | {a['demande']} | {a['servi']} | {tours} | {'⚠ ' + a['ecart'] if a['ecart'] else 'conforme'} |")
    (R / "journal" / "MODELE_REEL.md").write_text("\n".join(t) + "\n", encoding="utf-8")
    print(f"journal/MODELE_REEL.md : {len(ags)} agents, {n_e} écarts")


def veille(pas=60):
    vu = {}
    while True:
        try:
            _, ags = agents()
            for a in ags:
                cle = (a["etat"], a["servi"], a["ecart"])
                if vu.get(a["id"]) != cle:
                    if a["id"] in vu or a["etat"] == "en cours" or a["ecart"]:
                        print(time.strftime("%H:%M"), ligne(a), flush=True)
                    vu[a["id"]] = cle
            rapport_silencieux()
        except Exception as x:
            print("veille : erreur", x, flush=True)
        time.sleep(pas)


def rapport_silencieux():
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):
        rapport()


if __name__ == "__main__":
    a = sys.argv[1:] or ["etat"]
    if a[0] == "etat":
        etat("--tout" in a)
    elif a[0] == "ecarts":
        sys.exit(ecarts())
    elif a[0] == "rapport":
        rapport()
    elif a[0] == "veille":
        veille(int(a[1]) if len(a) > 1 else 60)
    else:
        print(__doc__)
        sys.exit(2)
