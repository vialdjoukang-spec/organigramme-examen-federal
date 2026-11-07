#!/usr/bin/env python3
"""PONS-OBLONGATA : mémoire de reprise zéro jeton du chantier de production.

Sous-commandes : capture (défaut) | pause [motif] | reprise | etat | veille [--intervalle 20]
Lit l'état réel sur disque (aucun appel à un modèle) et écrit :
  journal/PONS_OBLONGATA.json  (machine)   journal/REPRISE.md (humain, <= 80 lignes)
  journal/pons/AAAAMMJJ-HHMM.json (historique, 50 derniers)   journal/PAUSE (drapeau)
"""
import argparse, glob, hashlib, json, os, re, signal, sys, time
from datetime import datetime
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TRAVAIL = RACINE / "lot en cours de production"
FINAUX = RACINE / "LOT_Claude_Finaux"
J = RACINE / "journal"
ROUTAGE = J / "routage.jsonl"
PAUSE = J / "PAUSE"
PID = J / "pons.pid"
MAX_REPRISE = 80
ACTIF_S = 600  # fichier modifié depuis moins de 10 min : agent probablement actif
STEPS = ["aucun fichier", "rédaction en cours", "rédigé", "audit médical fait",
         "conformité faite", "transversale faite", "déposé"]
RE_H3 = re.compile(r"<h3[^>]*\bid\s*=\s*[\"']([A-Za-z0-9_-]+?)-p(\d{1,2})[\"']", re.I)


def jl(p):
    out = []
    try:
        for l in Path(p).read_text(encoding="utf-8").splitlines():
            l = l.strip()
            if l:
                try:
                    out.append(json.loads(l))
                except ValueError:
                    pass
    except OSError:
        pass
    return out


def ts(s):
    try:
        return datetime.fromisoformat(s).timestamp()
    except Exception:
        return 0.0


def cle_fichier(nom):
    """Clé canonique d'un fichier ou d'une leçon : Phase_A ou DX.n."""
    m = re.search(r"DX\.(\d+)", nom or "")
    if m:
        return "DX." + m.group(1)
    if re.search(r"Phase[_ ]A", nom or "", re.I):
        return "Phase_A"
    return None


def cles_ligne(txt):
    """Clés visées par un texte libre (« Phase_A + DX.1–DX.8 + DX.10 », « DX.1–10 »)."""
    r = []
    if re.search(r"Phase[_ ]A", txt or "", re.I):
        r.append("Phase_A")
    for m in re.finditer(r"DX\.?(\d+)(?:\s*[–-]\s*(?:DX\.?)?(\d+))?", txt or ""):
        a = int(m.group(1)); b = int(m.group(2) or a)
        r += ["DX.%d" % i for i in range(a, b + 1)]
    return list(dict.fromkeys(r))


def nom_attendu(lot, cle):
    return "LOT_%s_Phase_A_V0.html" % lot if cle == "Phase_A" else "LOT_%s_Phase_B_V0_%s.html" % (lot, cle)


def cles_attendues():
    return ["Phase_A"] + ["DX.%d" % i for i in range(1, 11)]


def lire_octets(p):
    try:
        return p.read_bytes()
    except OSError:
        return None


def analyse_html(p):
    b = lire_octets(p)
    if b is None:
        return None
    t = b.decode("utf-8", "replace")
    pts = {m.group(2) for m in RE_H3.finditer(t)}
    return {"octets": len(b), "sha256": hashlib.sha256(b).hexdigest(),
            "points_h3": len(pts) if pts else len(re.findall(r"<h3\b", t)),
            "fin_fichier": bool(re.search(r"<!--\s*FIN_FICHIER\s+[^>]*-->\s*$", t)),
            "mtime": p.stat().st_mtime}


def parse_t(p):
    nf, tot = [], 0
    try:
        for l in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*T(\d+)\.\s*(.*)", l)
            if m:
                tot += 1
                if "**Fait**" not in l and not re.search(r"\bFait\b\s*[:.—-]", l):
                    nf.append("T" + m.group(1) + " " + m.group(2)[:90])
    except OSError:
        pass
    return tot, nf


def parse_help(d):
    ouvertes = []
    for p in sorted(d.glob("HELP*.md")):
        t = p.read_text(encoding="utf-8", errors="replace")
        for bloc in re.split(r"(?m)^(?=## H)", t):
            m = re.match(r"## (H[\w-]+)", bloc)
            if m and not re.search(r"\bCLOSE?\b|\bCLOS\b|\bCLÔTURÉ", bloc, re.I):
                ouvertes.append("%s (%s)" % (m.group(1), p.name))
    return ouvertes


def etat_lots():
    try:
        return {l["lot"]: l for l in json.load(open(FINAUX / "ETAT_FILE.json"))["lots"]}
    except Exception:
        return {}


def lots_ouverts(etat):
    cand = sorted(p.name[4:] for p in TRAVAIL.glob("LOT_*") if p.is_dir())
    ouv = [n for n in cand if not etat.get(n, {}).get("depose")]
    dep = [n for n in cand if etat.get(n, {}).get("depose")]
    return ouv, dep


def capture_lot(num, etat, rout):
    lot = "LOT_" + num
    dt = TRAVAIL / lot
    df = FINAUX / lot
    deposeLot = bool(etat.get(num, {}).get("depose"))
    scores = jl(df / "audits" / "scores.jsonl")
    corr = jl(df / "audits" / "corrections.jsonl")
    tot_t, t_nf = parse_t(dt / "CORRECTIONS_AUDIT.md")
    helps = parse_help(dt)
    canon = (dt / "LISTE_DX_CANONIQUE.md").exists() or (df / "LISTE_DX_CANONIQUE.md").exists()
    rl = [r for r in rout if r.get("lot") == lot]
    fichiers, non_revenus = {}, []
    for cle in cles_attendues():
        nom = nom_attendu(num, cle)
        pw, pf = dt / nom, df / nom
        p = pw if pw.exists() else pf
        a = analyse_html(p) if p.exists() else None
        sc = [s for s in scores if cle_fichier(s.get("fichier") or s.get("lecon")) == cle]
        med = [s for s in sc if s.get("auditeur", {}).get("agent") == "auditeur-medical"]
        con = [s for s in sc if s.get("auditeur", {}).get("agent") == "auditeur-conformite"]
        lancers = [r for r in rl if cle in cles_ligne((r.get("fichier") or "") + " " + (r.get("lecon") or ""))
                   or (cle == "Phase_A" and (r.get("lecon") or "") == "Phase_A")]
        trans = [r for r in lancers if "transvers" in (r.get("raison", "") + r.get("fichier", "") + r.get("lecon", "")).lower()]
        lr = [r for r in lancers if r not in trans]
        # étape
        if a is None:
            etape = 0
        elif deposeLot and pf.exists():
            etape = 6
        elif not a["fin_fichier"]:
            etape = 1
        else:
            etape = 2
            if med:
                etape = 3
            if med and con:
                etape = 4
            if med and con and trans and tot_t and not t_nf and max(ts(r["horodatage"]) for r in trans) > ts(con[-1]["horodatage"]) - 1:
                etape = 5
        # agents non revenus (dernier lancement par rôle)
        def dernier(agent_pred):
            c = [r for r in lancers if agent_pred(r.get("agent", ""))]
            return max(c, key=lambda r: ts(r["horodatage"])) if c else None
        if not deposeLot:
            r = dernier(lambda x: x.startswith("redacteur"))
            if r and not (a and a["fin_fichier"] and a["mtime"] >= ts(r["horodatage"]) - 1 and time.time() - a["mtime"] > ACTIF_S):
                non_revenus.append({"fichier": cle, "agent": r["agent"], "lance": r["horodatage"], "modele": r.get("modele"), "effort": r.get("effort"), "fichier_modifie_il_y_a_min": a and round((time.time() - a["mtime"]) / 60)})
            for ag, liste in (("auditeur-medical", med), ("auditeur-conformite", con)):
                r = dernier(lambda x, ag=ag: x == ag and True)
                if r and r not in trans and not any(ts(s["horodatage"]) >= ts(r["horodatage"]) - 1 for s in liste):
                    non_revenus.append({"fichier": cle, "agent": ag, "lance": r["horodatage"], "modele": r.get("modele"), "effort": r.get("effort")})
            if trans:
                r = max(trans, key=lambda x: ts(x["horodatage"]))
                if not any(ts(s["horodatage"]) >= ts(r["horodatage"]) - 1 for s in sc) and etape < 5:
                    non_revenus.append({"fichier": cle, "agent": r["agent"] + " (transversale)", "lance": r["horodatage"], "modele": r.get("modele"), "effort": r.get("effort")})
        if etape <= 2 and any(x["agent"].startswith("redacteur") for x in non_revenus if x["fichier"] == cle):
            etape = 1
        cs = [c for c in corr if cle_fichier(c.get("lecon")) == cle]
        fichiers[cle] = {
            "fichier": nom, "etape": STEPS[etape], "etape_n": etape,
            "octets": a and a["octets"], "sha256": a and a["sha256"], "points_h3": a and a["points_h3"],
            "fin_fichier": a and a["fin_fichier"], "age_min": a and round((time.time() - a["mtime"]) / 60),
            "corrections": {"n": len(cs), "graves": sum(1 for c in cs if c.get("gravite") == "grave"),
                            "critiques": sum(1 for c in cs if c.get("gravite") == "critique")},
            "scores": {"medical": bool(med), "conformite": bool(con)},
            "non_revenus": [x for x in non_revenus if x["fichier"] == cle],
        }
    # prochaine action
    for cle, f in fichiers.items():
        f["action"] = action(num, cle, f, canon, fichiers, t_nf)
    return {"lot": lot, "depose": deposeLot, "statut": etat.get(num, {}).get("statut_audit"),
            "liste_canonique_gelee": canon, "t_total": tot_t, "t_non_faits": t_nf,
            "help_ouvertes": helps, "agents_non_revenus": non_revenus, "fichiers": fichiers}


def action(num, cle, f, canon, tous, t_nf):
    n = f["etape_n"]; nom = f["fichier"]; lot = "LOT_" + num
    brief_b = "'lot en cours de production/%s/BRIEF_PHASE_B.md'" % lot
    if f["non_revenus"]:
        a = f["non_revenus"][0]
        return "agent %s lancé %s sans retour : vérifier d'abord le disque (état ci-dessus) ; ne relancer que s'il est mort" % (a["agent"], a["lance"][11:16])
    if n == 6:
        return "rien (déposé)"
    if n == 0:
        if cle == "Phase_A":
            return "lancer redacteur-phase-a (opus, xhigh) pour %s" % lot
        if not canon:
            return "attendre le gel de LISTE_DX_CANONIQUE.md (audit médical de la Phase A)"
        return "lancer redacteur (opus, xhigh) %s avec %s" % (cle, brief_b)
    if n == 1:
        return "rédaction à terminer (FIN_FICHIER absent) : relancer le rédacteur sur %s en continuant le fichier existant" % nom
    if n == 2:
        return "lancer auditeur-medical (opus, xhigh) avec harnais/briefs/AUDIT_MEDICAL.md sur %s" % nom
    if n == 3:
        return "lancer auditeur-conformite (sonnet, high) avec harnais/briefs/CONFORMITE.md sur %s" % nom
    if n == 4:
        return "passe transversale T1–Tn (auditeur-medical opus xhigh), puis dépôt"
    if n == 5:
        return "déposer le LOT (procédure PROMPT_PRODUCTION_V2.md §9)"
    return ""


def capture():
    etat = etat_lots()
    ouv, dep = lots_ouverts(etat)
    rout = jl(ROUTAGE)
    lots = [capture_lot(n, etat, rout) for n in ouv]
    snap = {"horodatage": datetime.now().astimezone().isoformat(timespec="seconds"),
            "branche": branche(), "pause": pause_info(), "lots_deposes_dans_travail": dep,
            "dernier_routage": rout[-1] if rout else None, "lots": lots}
    J.mkdir(exist_ok=True)
    (J / "PONS_OBLONGATA.json").write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
    (J / "REPRISE.md").write_text(reprise_md(snap), encoding="utf-8")
    h = J / "pons"; h.mkdir(exist_ok=True)
    (h / (datetime.now().strftime("%Y%m%d-%H%M") + ".json")).write_text(json.dumps(snap, ensure_ascii=False), encoding="utf-8")
    for old in sorted(h.glob("*.json"))[:-50]:
        old.unlink()
    return snap


def branche():
    try:
        t = (RACINE / ".git" / "HEAD").read_text().strip()
        return t.split("/", 2)[-1] if t.startswith("ref:") else t[:10]
    except OSError:
        return "?"


def pause_info():
    try:
        return PAUSE.read_text(encoding="utf-8").strip()
    except OSError:
        return None


def reprise_md(s):
    L = ["# REPRISE — PONS-OBLONGATA (généré %s, branche %s)" % (s["horodatage"], s["branche"])]
    if s["pause"]:
        L += ["", "**PAUSE ACTIVE** — %s" % s["pause"].replace("\n", " ; "),
              "Règle : pendant la pause, aucun agent n'est lancé ; les agents en cours finissent leur fichier (pause douce, aucun jeton perdu) ; arrêt dur seulement sur ordre explicite de Vial. Sortie : `python3 harnais/pons_oblongata.py reprise`."]
    L += ["", "## Où on en est"]
    for lot in s["lots"]:
        c = {}
        for f in lot["fichiers"].values():
            c[f["etape"]] = c.get(f["etape"], 0) + 1
        L.append("- %s (%s) : %s" % (lot["lot"], lot["statut"] or "?", " ; ".join("%d %s" % (v, k) for k, v in c.items())))
    if s["lots_deposes_dans_travail"]:
        L.append("- Déposés (dossier de travail conservé) : " + ", ".join(s["lots_deposes_dans_travail"]))
    L += ["", "## Sûr (lu sur disque)"]
    for lot in s["lots"]:
        for cle, f in lot["fichiers"].items():
            if f["octets"]:
                L.append("- %s %s : %s, %s o, h3=%s, FIN_FICHIER=%s, corr %d (g %d, c %d)" % (
                    lot["lot"][4:], cle, f["etape"], f["octets"], f["points_h3"], "oui" if f["fin_fichier"] else "NON",
                    f["corrections"]["n"], f["corrections"]["graves"], f["corrections"]["critiques"]))
        if lot["liste_canonique_gelee"]:
            L.append("- %s : liste canonique gelée" % lot["lot"])
    L += ["", "## Incertain"]
    inc = 0
    for lot in s["lots"]:
        for a in lot["agents_non_revenus"]:
            L.append("- %s %s : %s lancé %s (%s/%s), aucun retour final sur disque%s : probablement en cours ou interrompu" % (
                lot["lot"], a["fichier"], a["agent"], a["lance"][5:16], a["modele"], a["effort"],
                (" (fichier modifié il y a %s min)" % a["fichier_modifie_il_y_a_min"]) if a.get("fichier_modifie_il_y_a_min") is not None else "")); inc += 1
        if lot["t_non_faits"]:
            L.append("- %s items T non faits : %s" % (lot["lot"], " | ".join(x[:60] for x in lot["t_non_faits"][:5]))); inc += 1
        if lot["help_ouvertes"]:
            L.append("- %s questions HELP ouvertes : %d (%s…)" % (lot["lot"], len(lot["help_ouvertes"]), lot["help_ouvertes"][0])); inc += 1
    if not inc:
        L.append("- rien")
    L += ["", "## Prochaines actions (une ligne)"]
    for lot in s["lots"]:
        vus = {}
        for cle, f in lot["fichiers"].items():
            vus.setdefault(f["action"], []).append(cle)
        for act, cles in vus.items():
            if act and not act.startswith("rien"):
                L.append("- %s [%s] : %s" % (lot["lot"][4:], ",".join(cles) if len(cles) < 4 else "%d fichiers" % len(cles), act))
    L += ["", "## Briefs types et commandes",
          "- Rédacteur Phase B : `lot en cours de production/LOT_XXX/BRIEF_PHASE_B.md` ; audit médical : `harnais/briefs/AUDIT_MEDICAL.md` ; conformité : `harnais/briefs/CONFORMITE.md`.",
          "- Prompt d'une ligne : « Lis <brief> ; fichier : <nom> ; LOT_XXX. » Au plus 5 agents opus en parallèle.",
          "- `python3 harnais/pons_oblongata.py etat` ; `python3 harnais/controle_lot.py verifier \"lot en cours de production/LOT_XXX\"` ; `python3 harnais/audit_langue.py <fichier> --json`.",
          "- Ne jamais reprendre un agent par SendMessage (recharge tout son historique) : relancer un agent neuf avec le brief et l'état disque. Détail : PROMPT_PRODUCTION_V2.md."]
    if len(L) > MAX_REPRISE:
        L = L[:MAX_REPRISE - 1] + ["… (tronqué ; voir journal/PONS_OBLONGATA.json)"]
    return "\n".join(L) + "\n"


def cmd_etat(s):
    if s["pause"]:
        print("PAUSE:", s["pause"].replace("\n", " "))
    for lot in s["lots"]:
        for cle, f in lot["fichiers"].items():
            print("%s %-7s %-20s %7s o %s%s" % (lot["lot"][4:], cle, f["etape"], f["octets"] or "-",
                  "!" if f["non_revenus"] else " ", f["action"][:60]))


def sig():
    r = []
    pats = [str(TRAVAIL / "**" / "*"), str(FINAUX / "*" / "audits" / "*"), str(ROUTAGE)]
    for pat in pats:
        for p in glob.glob(pat, recursive=True):
            try:
                st = os.stat(p); r.append((p, st.st_mtime_ns, st.st_size))
            except OSError:
                pass
    return hash(tuple(sorted(r)))


def veille(inter):
    J.mkdir(exist_ok=True)
    PID.write_text(str(os.getpid()))
    stop = []
    signal.signal(signal.SIGTERM, lambda *a: stop.append(1))
    signal.signal(signal.SIGINT, lambda *a: stop.append(1))
    try:
        last = sig()
        capture()
        while not stop:
            for _ in range(int(inter * 2)):
                if stop:
                    break
                time.sleep(0.5)
            cur = sig()
            if cur != last and not stop:
                time.sleep(2)
                last = sig()
                capture()
    finally:
        try:
            PID.unlink()
        except OSError:
            pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd")
    c = sp.add_parser("capture"); c.add_argument("--silencieux", action="store_true")
    p = sp.add_parser("pause"); p.add_argument("motif", nargs="*")
    sp.add_parser("reprise"); sp.add_parser("etat")
    v = sp.add_parser("veille"); v.add_argument("--intervalle", type=float, default=20)
    a = ap.parse_args()
    cmd = a.cmd or "capture"
    if cmd == "capture":
        s = capture()
        if not getattr(a, "silencieux", False):
            print("capture ok : journal/REPRISE.md, journal/PONS_OBLONGATA.json (%d LOT en cours)" % len(s["lots"]))
    elif cmd == "pause":
        J.mkdir(exist_ok=True)
        PAUSE.write_text("%s\nmotif : %s\n" % (datetime.now().astimezone().isoformat(timespec="seconds"), " ".join(a.motif) or "non précisé"), encoding="utf-8")
        capture()
        print("PAUSE posée. Aucun agent à lancer ; les agents en cours finissent leur fichier. journal/REPRISE.md à jour.")
    elif cmd == "reprise":
        if not (J / "REPRISE.md").exists():
            capture()
        try:
            PAUSE.unlink()
        except OSError:
            pass
        capture()
        print((J / "REPRISE.md").read_text(encoding="utf-8"))
    elif cmd == "etat":
        cmd_etat(capture())
    elif cmd == "veille":
        veille(a.intervalle)


if __name__ == "__main__":
    main()
