#!/usr/bin/env python3
"""Rapport qualité des LOTS (zéro jeton, bibliothèque standard) — harnais V0, 30.10.2026.

Usage
  python3 harnais/rapport_qualite.py [--racine LOT_Claude_Finaux] [--silencieux]

Collecte LOT_XXX/audits/corrections.jsonl et scores.jsonl (Prompt V0 §16.1) et écrit
<racine>/RAPPORT_QUALITE.html (sans JavaScript) et <racine>/RAPPORT_QUALITE.json :
  1. par leçon : 4 scores avant/après audit, taille, lecture estimée, corrections par gravité et type ;
  2. par LOT : moyenne et minimum des scores, taille totale, leçons achevées / 11, corrections critiques ;
  3. global : courbe d'avancement, scores moyens par vague, types d'erreurs, 20 dernières critiques.

Conventions (écrites dans le rapport) :
  - avant = scores « avant » de la première ligne de scores de la leçon ; après = scores « après » de la dernière ;
  - leçon achevée = scorée par l'auditeur médical ET par l'auditeur de conformité ;
  - vague = 10 LOTS consécutifs (file active, Prompt V0 §22.4) : vague 1 = LOT_001–010 ;
  - lecture = mots du texte visible (fenêtres comprises) ÷ 180 mots/min ; Ko = 1 000 octets.
Code 0 toujours (le rapport ne bloque jamais) ; les lignes illisibles sont comptées en anomalies.
"""
from __future__ import annotations
import argparse, hashlib, html, json, re, sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ZH = ZoneInfo("Europe/Zurich")
SCORES = ("score_medical", "score_langue", "score_pec", "score_examen")
NOMS = {"score_medical": "Médical", "score_langue": "Langue", "score_pec": "Prise en charge", "score_examen": "Examen"}
GRAVITES = ("critique", "grave", "moyen", "léger")
TYPES = ("dose", "seuil", "critère", "conduite", "source", "omission", "langue", "format")
LECONS_PAR_LOT = 11
MOTS_MIN = 180
RE_LOT = re.compile(r"LOT_(\d{3})")


def date(s) -> datetime | None:
    try:
        d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None
    return (d.replace(tzinfo=ZH) if d.tzinfo is None else d).astimezone(ZH)


def num(x) -> float | None:
    try:
        return float(str(x).replace(",", "."))
    except (TypeError, ValueError):
        return None


def lire_jsonl(p: Path, anomalies: list) -> list[dict]:
    out = []
    for i, l in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if not l.strip():
            continue
        try:
            o = json.loads(l)
            if not isinstance(o, dict):
                raise ValueError("objet attendu")
            o["_lot_dossier"] = p.parent.parent.name
            out.append(o)
        except ValueError as e:
            anomalies.append(f"{p.parent.parent.name}/audits/{p.name}:{i} illisible ({e})")
    return out


def lot_de(o: dict) -> str:
    m = RE_LOT.search(str(o.get("lot") or "")) or RE_LOT.search(o["_lot_dossier"])
    return f"LOT_{m.group(1)}" if m else o["_lot_dossier"]


def cle_lecon(o: dict) -> str:
    s = str(o.get("lecon") or o.get("fichier") or "?").strip()
    m = re.search(r"DX\.(\d{1,2})", s)
    return f"DX.{int(m.group(1))}" if m else ("Phase_A" if "phase_a" in s.lower().replace(" ", "_") else s)


def agent(o: dict) -> str:
    a = o.get("auditeur")
    return str(a.get("agent", "")) if isinstance(a, dict) else str(a or "")


def mots_visibles(p: Path) -> int:
    t = p.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", t, flags=re.S | re.I)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return len(re.findall(r"\w+", t))


def moyenne(v):
    v = [x for x in v if x is not None]
    return round(sum(v) / len(v), 1) if v else None


def construire(racine: Path) -> dict:
    anomalies: list[str] = []
    corr, sco = [], []
    for d in sorted(racine.glob("LOT_*/audits")):
        if (d / "corrections.jsonl").is_file():
            corr += lire_jsonl(d / "corrections.jsonl", anomalies)
        if (d / "scores.jsonl").is_file():
            sco += lire_jsonl(d / "scores.jsonl", anomalies)
    for o in corr + sco:
        o["_lot"], o["_lecon"], o["_t"] = lot_de(o), cle_lecon(o), date(o.get("horodatage"))
        if o["_t"] is None:
            anomalies.append(f"{o['_lot']} {o['_lecon']} : horodatage illisible « {o.get('horodatage')} »")
    tri = lambda o: o["_t"] or datetime.min.replace(tzinfo=ZH)

    # 1. Leçons
    lecons: dict[tuple, dict] = {}
    for o in sorted(sco, key=tri):
        k = (o["_lot"], o["_lecon"])
        L = lecons.setdefault(k, {"lot": k[0], "lecon": k[1], "nom": str(o.get("lecon") or k[1]),
                                   "code_ssp": o.get("code_ssp"), "auditeurs": [], "avant": None})
        if L["avant"] is None and isinstance(o.get("avant"), dict):
            L["avant"] = {s: num(o["avant"].get(s)) for s in SCORES}
        if isinstance(o.get("apres"), dict):
            L["apres"] = {s: num(o["apres"].get(s)) for s in SCORES}
        L["auditeurs"].append(agent(o))
        L["fichier"], L["octets"], L["sha256"] = o.get("fichier"), o.get("octets"), o.get("sha256")
        L["termine_le"] = o["_t"].isoformat(timespec="minutes") if o["_t"] else None
        L["_t"] = o["_t"]
    for c in corr:
        k = (c["_lot"], c["_lecon"])
        L = lecons.setdefault(k, {"lot": k[0], "lecon": k[1], "nom": str(c.get("lecon") or k[1]),
                                   "code_ssp": c.get("code_ssp"), "auditeurs": [], "avant": None, "_t": None})
        L.setdefault("gravite", Counter())[str(c.get("gravite", "?")).lower()] += 1
        L.setdefault("type", Counter())[str(c.get("type", "?")).lower()] += 1
    for (lot, _), L in lecons.items():
        L.setdefault("apres", None); L.setdefault("gravite", Counter()); L.setdefault("type", Counter())
        ag = " ".join(L["auditeurs"]).lower()
        L["achevee"] = "medical" in ag and "conformite" in ag
        L["ko"] = round(L["octets"] / 1000, 1) if isinstance(L.get("octets"), (int, float)) else None
        f = racine / lot / str(L.get("fichier") or "")
        L["lecture_min"] = L["sha_conforme"] = None
        if L.get("fichier") and f.is_file():
            L["lecture_min"] = round(mots_visibles(f) / MOTS_MIN)
            if L.get("sha256"):
                L["sha_conforme"] = hashlib.sha256(f.read_bytes()).hexdigest() == L["sha256"]
                if not L["sha_conforme"]:
                    anomalies.append(f"{lot} {L['lecon']} : SHA-256 du fichier ≠ dernier score (modifié après audit)")

    # 2. LOTS
    lots: dict[str, dict] = {}
    for L in lecons.values():
        lots.setdefault(L["lot"], {"lot": L["lot"], "lecons": []})["lecons"].append(L)
    crit = sorted((c for c in corr if str(c.get("gravite", "")).lower() == "critique"), key=tri)
    for lot, D in lots.items():
        D["lecons"].sort(key=lambda L: (L["lecon"] != "Phase_A", int(L["lecon"][3:]) if L["lecon"].startswith("DX.") and L["lecon"][3:].isdigit() else 99))
        fin = [L for L in D["lecons"] if L["apres"]]
        D["moyenne"] = {s: moyenne([L["apres"][s] for L in fin]) for s in SCORES}
        D["minimum"] = {s: min((L["apres"][s] for L in fin if L["apres"][s] is not None), default=None) for s in SCORES}
        D["ko_total"] = round(sum(L["ko"] or 0 for L in D["lecons"]), 1)
        D["achevees"] = sum(L["achevee"] for L in D["lecons"])
        D["attendues"] = LECONS_PAR_LOT
        ach = [L["_t"] for L in D["lecons"] if L["achevee"] and L["_t"]]
        D["achevé_le"] = max(ach).isoformat(timespec="minutes") if D["achevees"] >= LECONS_PAR_LOT and ach else None
        D["critiques"] = [{"heure": c["_t"].isoformat(timespec="minutes") if c["_t"] else None, "lecon": c["_lecon"],
                           "point": c.get("point"), "type": c.get("type"), "apres": c.get("apres")}
                          for c in crit if c["_lot"] == lot]

    # 3. Global
    evts = sorted([(L["_t"], "lecon") for L in lecons.values() if L["achevee"] and L["_t"]] +
                  [(date(D["achevé_le"]), "lot") for D in lots.values() if D["achevé_le"]])
    courbe, nl, nL = [], 0, 0
    for t, k in evts:
        nl += k == "lecon"; nL += k == "lot"
        courbe.append({"t": t.isoformat(timespec="minutes"), "lecons": nl, "lots": nL})
    vagues = defaultdict(list)
    for L in lecons.values():
        m = RE_LOT.search(L["lot"])
        if m and L["apres"]:
            vagues[(int(m.group(1)) - 1) // 10 + 1].append(L)
    par_vague = [{"vague": v, "lots": f"LOT_{(v-1)*10+1:03d}–{v*10:03d}", "lecons": len(Ls),
                  **{s: moyenne([L["apres"][s] for L in Ls]) for s in SCORES},
                  **{f"{s}_avant": moyenne([(L["avant"] or {}).get(s) for L in Ls]) for s in SCORES}}
                 for v, Ls in sorted(vagues.items())]
    types = Counter(str(c.get("type", "?")).lower() for c in corr)
    grav = Counter(str(c.get("gravite", "?")).lower() for c in corr)
    dernieres = [{"heure": c["_t"].isoformat(timespec="minutes") if c["_t"] else None, "lot": c["_lot"],
                  "lecon": c["_lecon"], "point": c.get("point"), "type": c.get("type"),
                  "avant": str(c.get("avant", ""))[:200], "apres": str(c.get("apres", ""))[:200],
                  "source": c.get("source")} for c in crit[-20:][::-1]]
    for L in lecons.values():
        L.pop("_t", None); L["gravite"] = dict(L["gravite"]); L["type"] = dict(L["type"])
    return {"genere_le": datetime.now(ZH).isoformat(timespec="minutes"),
            "conventions": {"lecture_mots_par_minute": MOTS_MIN, "lecons_par_lot": LECONS_PAR_LOT,
                            "vague": "10 LOTS consécutifs", "achevee": "scorée par auditeur-medical et auditeur-conformite",
                            "avant_apres": "avant = première ligne de scores ; après = dernière"},
            "totaux": {"lots": len(lots), "lots_acheves": sum(1 for D in lots.values() if D["achevé_le"]),
                       "lecons": len(lecons), "lecons_achevees": sum(L["achevee"] for L in lecons.values()),
                       "corrections": len(corr), "par_gravite": dict(grav), "par_type": dict(types.most_common())},
            "lots": [lots[k] for k in sorted(lots)], "courbe": courbe, "vagues": par_vague,
            "critiques_recentes": dernieres, "anomalies": anomalies}


# ---------- HTML (aucun JavaScript) ----------
E = lambda x: html.escape("" if x is None else str(x))
f1 = lambda x: "—" if x is None else (f"{x:.0f}" if float(x).is_integer() else f"{x:.1f}".replace(".", ","))


def table(entetes, lignes, cls="") -> str:
    th = "".join(f"<th>{E(h)}</th>" for h in entetes)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in lignes)
    if not lignes:
        tr = f"<tr><td colspan='{len(entetes)}'>Aucune donnée.</td></tr>"
    return f"<div class='defil'><table class='{cls}'><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>"


def courbe_svg(tous: list[dict], cle: str, titre: str) -> str:
    """Escalier cumulatif en SVG statique ; infobulles natives <title> ; aucun script."""
    points = [p for i, p in enumerate(tous) if p[cle] != (tous[i - 1][cle] if i else 0)]
    if not points:
        return f"<p class='muet'>{E(titre)} : aucun achèvement encore.</p>"
    W, H, g, b, h, d = 640, 180, 48, 30, 12, 12
    ts = [date(p["t"]).timestamp() for p in points]
    t0 = date(tous[0]["t"]).timestamp()  # axe du temps commun aux deux courbes
    t1 = max(date(tous[-1]["t"]).timestamp(), t0 + 60)
    ymax = max(p[cle] for p in points) or 1
    X = lambda t: g + (t - t0) / (t1 - t0) * (W - g - d)
    Y = lambda v: H - b - v / ymax * (H - b - h)
    chemin, prev = [f"M{X(t0):.1f},{Y(0):.1f}"], 0
    for t, p in zip(ts, points):
        chemin += [f"L{X(t):.1f},{Y(prev):.1f}", f"L{X(t):.1f},{Y(p[cle]):.1f}"]
        prev = p[cle]
    chemin.append(f"L{X(t1):.1f},{Y(prev):.1f}")
    grille = "".join(f"<line x1='{g}' x2='{W-d}' y1='{Y(v):.1f}' y2='{Y(v):.1f}' class='grille'/>"
                     f"<text x='{g-6}' y='{Y(v)+4:.1f}' class='axe' text-anchor='end'>{v}</text>"
                     for v in sorted({0, ymax // 2, ymax}))
    pts = "".join(f"<circle cx='{X(t):.1f}' cy='{Y(p[cle]):.1f}' r='4' class='pt'><title>{E(p['t'][:16].replace('T', ' '))} — {p[cle]}</title></circle>"
                  for t, p in zip(ts, points))
    lab = lambda t: datetime.fromtimestamp(t, ZH).strftime("%d.%m %H:%M")
    return (f"<figure><figcaption>{E(titre)}</figcaption><svg viewBox='0 0 {W} {H}' role='img' aria-label='{E(titre)}'>"
            f"{grille}<path d='{' '.join(chemin)}' class='serie'/>{pts}"
            f"<text x='{g}' y='{H-8}' class='axe'>{lab(t0)}</text><text x='{W-d}' y='{H-8}' class='axe' text-anchor='end'>{lab(t1)}</text>"
            f"</svg></figure>")


CSS = """
:root{--fond:#f7f7f5;--carte:#fcfcfb;--texte:#1d1d1b;--texte2:#52514e;--trait:#d9d8d3;--serie:#2a78d6;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--fond:#121211;--carte:#1a1a19;--texte:#f0efec;--texte2:#c3c2b7;--trait:#3a3a37;--serie:#3987e5;color-scheme:dark}}
body{margin:0;background:var(--fond);color:var(--texte);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1100px;margin:0 auto;padding:16px}
h1{font-size:1.5rem;margin:.2rem 0}h2{font-size:1.2rem;margin:2rem 0 .5rem;border-bottom:1px solid var(--trait)}
h3{font-size:1rem;margin:1.2rem 0 .3rem}.muet{color:var(--texte2)}
.defil{overflow-x:auto;background:var(--carte);border:1px solid var(--trait);border-radius:6px;margin:.4rem 0 1rem}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}
th,td{padding:4px 8px;border-bottom:1px solid var(--trait);text-align:left;vertical-align:top;white-space:nowrap}
td.long,th.long{white-space:normal;min-width:16rem}th{font-weight:600;color:var(--texte2)}
.kpi{display:flex;flex-wrap:wrap;gap:8px}.kpi div{background:var(--carte);border:1px solid var(--trait);border-radius:6px;padding:8px 12px}
.kpi b{display:block;font-size:1.4rem}
figure{max-width:760px;margin:.5rem 0 1rem;background:var(--carte);border:1px solid var(--trait);border-radius:6px;padding:8px}
figcaption{color:var(--texte2);font-weight:600}svg{width:100%;height:auto}
.serie{fill:none;stroke:var(--serie);stroke-width:2}.pt{fill:var(--serie);stroke:var(--carte);stroke-width:2}
.grille{stroke:var(--trait);stroke-width:1}.axe{fill:var(--texte2);font-size:11px}
"""


def html_rapport(R: dict) -> str:
    T = R["totaux"]
    sc = lambda d: [f1((d or {}).get(s)) for s in SCORES]
    o = [f"<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
         f"<title>Rapport qualité</title><style>{CSS}</style></head><body><main>",
         f"<h1>Rapport qualité — LOTS Claude</h1><p class='muet'>Généré le {E(R['genere_le'].replace('T', ' '))} (Europe/Zurich) par <code>harnais/rapport_qualite.py</code>, sans modèle. Scores sur 100, après audit et correction (Prompt V0 §16.1).</p>",
         "<div class='kpi'>" + "".join(f"<div><b>{v}</b>{E(k)}</div>" for k, v in (
             ("LOTS achevés", f"{T['lots_acheves']} / {T['lots']}"), ("Leçons achevées", f"{T['lecons_achevees']} / {T['lecons']}"),
             ("Corrections", T["corrections"]), ("Critiques corrigées", T["par_gravite"].get("critique", 0)))) + "</div>"]
    # 3. Global
    o.append("<h2>Avancement global</h2>")
    o.append(courbe_svg(R["courbe"], "lots", "LOTS achevés (cumul)"))
    o.append(courbe_svg(R["courbe"], "lecons", "Leçons achevées (cumul)"))
    o.append("<details><summary>Tableau de l'avancement</summary>" +
             table(["Horodatage", "LOTS", "Leçons"], [[E(p["t"].replace("T", " ")), p["lots"], p["lecons"]] for p in R["courbe"]]) + "</details>")
    o.append("<h3>Scores moyens par vague (après audit ; avant entre parenthèses)</h3>")
    o.append(table(["Vague", "LOTS", "Leçons"] + [NOMS[s] for s in SCORES],
                   [[v["vague"], E(v["lots"]), v["lecons"]] + [f"{f1(v[s])} ({f1(v[s + '_avant'])})" for s in SCORES] for v in R["vagues"]]))
    o.append("<h3>Types d'erreurs les plus fréquents</h3>")
    o.append(table(["Type", "Corrections", "Part"], [[E(k), n, f"{100 * n / max(T['corrections'], 1):.0f} %"] for k, n in T["par_type"].items()]))
    o.append("<h3>20 dernières corrections critiques</h3>")
    o.append(table(["Heure", "LOT", "Leçon", "Point", "Type", "Avant", "Après", "Source"],
                   [[E((c["heure"] or "")[:16].replace("T", " ")), E(c["lot"]), E(c["lecon"]), E(c["point"]), E(c["type"]),
                     f"<span>{E(c['avant'])}</span>", f"<span>{E(c['apres'])}</span>", E(c["source"])] for c in R["critiques_recentes"]], "crit")
             .replace("<td><span>", "<td class='long'><span>"))
    # 2. LOTS, puis 1. leçons
    o.append("<h2>Par LOT</h2>")
    o.append(table(["LOT", "Leçons achevées", "Taille totale (Ko)"] + [f"{NOMS[s]} moy. / min." for s in SCORES] + ["Critiques"],
                   [[E(D["lot"]), f"{D['achevees']} / {D['attendues']}", f1(D["ko_total"])] +
                    [f"{f1(D['moyenne'][s])} / {f1(D['minimum'][s])}" for s in SCORES] + [len(D["critiques"])] for D in R["lots"]]))
    for D in R["lots"]:
        o.append(f"<h3 id='{E(D['lot'])}'>{E(D['lot'])} — {D['achevees']} / {D['attendues']} leçons"
                 + (f", achevé le {E(D['achevé_le'].replace('T', ' '))}" if D["achevé_le"] else "") + "</h3>")
        o.append(table(["Leçon", "Achevée", "Ko", "Lecture (min)"] + [f"{NOMS[s]} avant → après" for s in SCORES] +
                       [g.capitalize() for g in GRAVITES] + ["Types"],
                       [[E(L["nom"]), "oui" if L["achevee"] else "non", f1(L["ko"]), f1(L["lecture_min"])] +
                        [f"{a} → {b}" for a, b in zip(sc(L["avant"]), sc(L["apres"]))] +
                        [L["gravite"].get(g, 0) for g in GRAVITES] +
                        [E(", ".join(f"{k} {n}" for k, n in sorted(L["type"].items(), key=lambda kv: -kv[1])) or "—")]
                        for L in D["lecons"]]))
        if D["critiques"]:
            o.append(table(["Heure", "Leçon", "Point", "Type", "Correction (après)"],
                           [[E((c["heure"] or "")[:16].replace("T", " ")), E(c["lecon"]), E(c["point"]), E(c["type"]),
                             E(str(c["apres"] or "")[:200])] for c in D["critiques"]]))
    if R["anomalies"]:
        o.append("<h2>Anomalies de collecte</h2><ul>" + "".join(f"<li>{E(a)}</li>" for a in R["anomalies"]) + "</ul>")
    c = R["conventions"]
    o.append(f"<p class='muet'>Conventions : leçon achevée = {E(c['achevee'])} ; {E(c['avant_apres'])} ; vague = {E(c['vague'])} ; "
             f"lecture = mots visibles ÷ {c['lecture_mots_par_minute']} mots/min ; {c['lecons_par_lot']} leçons attendues par LOT ; Ko = 1 000 octets.</p>")
    o.append("</main></body></html>\n")
    return "\n".join(o)


def ecrire(p: Path, texte: str):
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(texte, encoding="utf-8")
    tmp.replace(p)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--racine", default=str(Path(__file__).resolve().parent.parent / "LOT_Claude_Finaux"))
    ap.add_argument("--silencieux", action="store_true")
    a = ap.parse_args()
    racine = Path(a.racine)
    if not racine.is_dir():
        print(f"racine absente : {racine}", file=sys.stderr)
        return 0
    R = construire(racine)
    ecrire(racine / "RAPPORT_QUALITE.json", json.dumps(R, ensure_ascii=False, indent=1) + "\n")
    ecrire(racine / "RAPPORT_QUALITE.html", html_rapport(R))
    if not a.silencieux:
        T = R["totaux"]
        print(f"RAPPORT_QUALITE : {T['lots_acheves']}/{T['lots']} LOTS achevés, {T['lecons_achevees']}/{T['lecons']} leçons, "
              f"{T['corrections']} corrections ({T['par_gravite'].get('critique', 0)} critiques), {len(R['anomalies'])} anomalie(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
