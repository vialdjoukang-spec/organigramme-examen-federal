#!/usr/bin/env python3
"""BRAIN-HARNESS · cerveau : orchestre les 160 scriptones (registre), publie les doléances sur le bus, mesure (gratuit, hors ligne).
  python3 harnais/brain/cerveau.py analyser <fichier|dossier> [--json] [--max N]   doléances typées (lecture seule)
  python3 harnais/brain/cerveau.py corriger <fichier> [--appliquer]                 corrections mécaniques sûres (dry-run par défaut)
  python3 harnais/brain/cerveau.py mesurer <fichier> [...]                           avant/après : détection, lignes, jetons
  python3 harnais/brain/cerveau.py empreintes [--ecrire]                             SHA256SUMS des scriptones
Bus : .cache/brain/doleances/<fichier>.json (dernier état) ; journal append-only .cache/brain/journal.jsonl.
Vue : S1, S2, S6, S20 jugent le rendu (fichier converti par forme_interactive.py s'il ne l'est pas) ; les autres scriptones de cours et les
140 synapses α/β jugent le texte du fichier. Circuit complet (collecte → α → nœuds Sonnet → β → vote → nœuds Opus, journal 3D) : orchestre.py."""
import importlib, json, re, sys, time
from pathlib import Path
D = Path(__file__).resolve().parent
R = D.parents[1]
sys.path[:0] = [str(D / "scriptones"), str(R / "harnais")]
import bus, reseau

RENDU = ["s1_police", "s2_rythme", "s6_barre14", "s20_ancres"]
TEXTE = ["s11_collecteur", "s3_concision", "s4_budget", "s5_arbre", "s8_tableaux", "s9_sources", "s10_memoire", "s18_vote"] + \
        [e["id"] for e in reseau.registre()["scriptones"] if e["zone"] in ("alpha", "beta")]
VIAL = ["s21_forme_vial"]       # directive de Vial du 28.10.2026 (arbre en cases, But/Moyens A/B, sous-cellules de signes) : hors registre, ajouté sans rien retirer
TEXTE += VIAL


class _Mods(dict):
    def __missing__(self, k): v = importlib.import_module(k) if k in VIAL else reseau.module(k); self[k] = v; return v
MODS = _Mods()
MARQ = "<!-- FORME_INTERACTIVE -->"


def vue(t):
    """Rendu affiché : le fichier converti (idempotent) ; brut si le convertisseur est absent."""
    if MARQ in t: return t
    try:
        import forme_interactive as FI
        return FI.convert(t)
    except Exception:
        return t


def analyser(t, nom, ecrire=True):
    v = vue(t); out = []; mes = {}
    for n in RENDU + TEXTE:
        s = bus.executer(MODS[n], nom, html=v if n in RENDU else t, ecrire=False)
        err = bus.valider(s)
        if err: raise SystemExit(f"CONTRAT ROMPU par {n} : {err[:3]}")
        out += s["doleances"]; mes[n] = s["mesures"]
    vus = set(); D_ = [d for d in out if not (d["id"] in vus or vus.add(d["id"]))]
    if ecrire:
        b = R / ".cache/brain/doleances"; b.mkdir(parents=True, exist_ok=True)
        (b / f"{nom}.json").write_text(json.dumps(dict(fichier=nom, sha256=bus.sha(t), ts=time.strftime("%Y-%m-%dT%H:%M:%S"), doleances=D_, mesures=mes), ensure_ascii=False, indent=1))
        bus.journal(dict(ts=time.strftime("%Y-%m-%dT%H:%M:%S"), cerveau="analyser", fichier=nom, entree=bus.sha(t)[:16], doleances=len(D_)))
    return D_, mes


def corriger(t, convertir=False):
    """Corrections mécaniques sûres de tous les écrivains (un par zone), jusqu'au point fixe ; convertir=True insère la conversion après l'arbre."""
    return reseau.corriger_tout(t, convertir=vue if convertir else None)[0]


def compte(D_):
    c = {}
    for d in D_: c[d["code"]] = c.get(d["code"], 0) + 1
    return dict(sorted(c.items()))


def ligne_resume(D_, n=25):
    o = {k: i for i, k in enumerate(bus.SEVERITES)}
    L = sorted(D_, key=lambda d: (o[d["severite"]], d["code"]))
    r = [f"- {d['severite']} {d['code']} {d['ancre']} : {d['constat']} → {d['correction_prescrite']}" for d in L[:n]]
    return "\n".join(r + ([f"- … {len(L) - n} de plus (--json)"] if len(L) > n else []))


def mesurer(f):
    """Avant/après sur une copie en mémoire (le fichier n'est jamais écrit)."""
    t = Path(f).read_text(encoding="utf-8", errors="replace"); nom = Path(f).name
    D0, M0 = analyser(t, nom, ecrire=False); t1 = corriger(t); D1, M1 = analyser(t1, nom, ecrire=False)
    texte_cours = bus.texte_visible(t[slice(*bus.bornes_cours(t))])
    compact = ligne_resume([d for d in D1 if d["executant"] == "agent"], 10 ** 6)
    return dict(fichier=nom, octets=len(t.encode()), avant=compte(D0), apres_script=compte(D1),
                resolues_par_script=len(D0) - len(D1), restantes_agent=sum(d["executant"] == "agent" for d in D1),
                lignes_point2=M0["s4_budget"].get("lignes_point_2"), jetons_relecture_integrale=bus.estime_jetons(t),
                jetons_texte_cours=bus.estime_jetons(texte_cours), jetons_doleances=bus.estime_jetons(compact),
                gain_jetons_pct=round(100 * (1 - bus.estime_jetons(compact) / max(1, bus.estime_jetons(t))), 1), idempotent=corriger(t1) == t1)


def main(a):
    if not a or a[0] in ("-h", "--help"): print(__doc__); return 0
    alt = bus.verifier_empreintes()
    if alt and a[0] != "empreintes": print(f"ALTÉRATION DÉTECTÉE : {', '.join(alt)} (SHA256SUMS). STOP."); return 3
    cmd = a[0]
    if cmd == "empreintes":
        if "--ecrire" in a: print("écrit :", ", ".join(bus.ecrire_empreintes())); return 0
        print("intactes" if not alt else f"ALTÉRÉES : {alt}"); return 1 if alt else 0
    if len(a) < 2: print(__doc__); return 2
    cible = Path(a[1])
    if not cible.exists(): print(f"INTROUVABLE : {cible}"); return 2
    if cmd == "analyser":
        fs = sorted(cible.glob("*.html")) if cible.is_dir() else [cible]; mx = int(a[a.index("--max") + 1]) if "--max" in a else 25; tot = []
        for f in fs:
            D_, M_ = analyser(f.read_text(encoding="utf-8", errors="replace"), f.name); tot += D_
            if "--json" not in a: print(f"## {f.name} · {len(D_)} doléance(s) · {compte(D_)}\n" + ligne_resume(D_, mx))
        if "--json" in a: print(json.dumps(tot, ensure_ascii=False, indent=1))
        return 1 if any(d["severite"] == "CRITIQUE" for d in tot) else 0
    if cmd == "corriger":
        t = cible.read_text(encoding="utf-8", errors="replace"); t1 = corriger(t)
        print(f"{cible.name} : {'aucune correction' if t1 == t else f'{len(t1.encode()) - len(t.encode()):+d} octets'}{'' if '--appliquer' in a else ' (dry-run : rien écrit)'}")
        if "--appliquer" in a and t1 != t: cible.write_text(t1, encoding="utf-8")
        return 0
    if cmd == "mesurer":
        print(json.dumps([mesurer(x) for x in a[1:] if not x.startswith("--")], ensure_ascii=False, indent=1)); return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
