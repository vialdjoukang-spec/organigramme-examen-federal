#!/usr/bin/env python3
"""REGISTRE IA — état d'avancement de chaque LOT et verrou d'écriture entre Claude, Codex et Grok.

Zéro jeton (Python standard). Clone identique dans claude-LOTS-html/, codex-LOTS-html/, grok-LOTS-html/.
Source de vérité : ce fichier dans harnais/ ; les clones sont recopiés à chaque `etat`.

Commandes (depuis la racine du dépôt) :
  python3 <dossier>/registre_ia.py lire <ia>               affiche lois + état, délivre le jeton de lecture
  python3 <dossier>/registre_ia.py signer <ia> <jeton>     signe la lecture (obligatoire avant toute écriture)
  python3 <dossier>/registre_ia.py etat                    recalcule l'état (toutes branches distantes) et les clones
  python3 <dossier>/registre_ia.py verifier <ia> <LOT_XXX> autorisé à écrire ce LOT ? (code 0 oui, 1 non)
  python3 <dossier>/registre_ia.py garde <ia>              contrôle des fichiers indexés (hook pre-commit) ; bloque si interdit
  python3 <dossier>/registre_ia.py installer <ia>          installe le hook git pre-commit bloquant pour cette IA
  python3 <dossier>/registre_ia.py pret <ia>               couple harnais identique + routage créé et surveillé ? (bloquant)
<ia> ∈ claude, codex, grok.
"""
import datetime, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

R = Path(__file__).resolve().parent.parent
IAS = ("claude", "codex", "grok")
DOSSIER = {ia: f"{ia}-LOTS-html" for ia in IAS}
TOTAL = 248
SOURCE = R / "harnais" / "registre_ia.py"
RESERV = R / "IA_RESERVATIONS.json"      # modifiable par Vial seul
AUTOR = R / "IA_AUTORISATIONS.json"      # modifiable par Vial seul
ZURICH = datetime.timezone(datetime.timedelta(hours=1))

LOIS = """LOIS DU REGISTRE (ordre de Vial, 30.10.2026) — lecture et signature obligatoires, sinon toute écriture est bloquée.
L1. Lis ce registre et signe-le (`signer`) au début de chaque session, avant d'écrire quoi que ce soit.
L2. Tu n'écris QUE dans ton dossier `<ia>-LOTS-html/` et sur ta propre branche (`codex/lots`, `grok/lots` ; Claude : `production-v2`). Tout le reste du dépôt est en lecture seule pour toi.
L3. Interdiction absolue de rédiger ou de modifier un LOT ou un chapitre déjà amorcé (un seul fichier suffit) par une autre IA ou par toi-même sans validation de Vial. Une entrée dans `IA_AUTORISATIONS.json`, écrite par Vial seul, est la seule exception.
L4. Tu ne rédiges que les LOTS de ta plage dans `IA_RESERVATIONS.json`, non encore amorcés, dans l'ordre croissant. Priorité : les LOTS jamais explorés.
L5. Ce qu'une autre IA a écrit est en lecture seule pour toi ; seul Vial peut lever ce verrou.
L5bis. Pour toute opération du projet, Claude compris, aucune production sans le couple [harnais + routage] : harnais identique au manifeste, ROUTAGE_<IA>.json et routage_<ia>.py créés par toi, autotest vert, veille du routage active (`pret <ia>`).
L6. Avant d'écrire dans un LOT : `verifier <ia> <LOT_XXX>` doit répondre AUTORISÉ. Le hook pre-commit (`installer`) bloque tout commit interdit.
L7. Tu ne modifies jamais ce script, ses clones, IA_RESERVATIONS.json ni IA_AUTORISATIONS.json.
L8. Règles de fond : sources suisses puis européennes lues et datées, sinon « À vérifier » ; doses tirées de l'AIPS suisse seulement, jamais du Compendium ; aucune donnée personnelle ; jamais sur main ; n'affirmer que ce qui est fait."""


def maintenant():
    return datetime.datetime.now(ZURICH).isoformat(timespec="seconds")


def git(*a):
    try:
        return subprocess.run(["git", "-C", str(R), *a], capture_output=True, text=True, timeout=60).stdout
    except Exception:
        return ""


def sha_lois():
    return hashlib.sha256(LOIS.encode()).hexdigest()[:16]


def charger(p, defaut):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception:
        return defaut


def reservations():
    d = charger(RESERV, {})
    return {ia: tuple(d.get(ia, {}).get("plage", (0, -1))) for ia in IAS}


def autorise_par_vial(ia, lot):
    for a in charger(AUTOR, {"autorisations": []}).get("autorisations", []):
        if a.get("ia") == ia and a.get("lot") == lot and a.get("accorde_par") == "Vial":
            return True
    return False


# ---------- relevé de l'état sur toutes les branches ----------
MOTIF_HTML = re.compile(r"LOT_(\d{3})_Phase_(A|B)(?:_V0_DX\.(\d+))?.*\.html$")


def proprietaire(chemin):
    if chemin.startswith(("LOT_Claude_Finaux/", "lot en cours de production/", "LOTS_html/", "claude-LOTS-html/")):
        return "claude"
    for ia in ("codex", "grok"):
        if chemin.startswith(DOSSIER[ia] + "/"):
            return ia
    return None


def releve():
    """{lot: {fichier: {ia, branche, depose}}} sur la branche locale et toutes les branches distantes."""
    git("fetch", "--quiet", "--all")
    refs = ["HEAD"] + [l.strip() for l in git("branch", "-r", "--format=%(refname:short)").splitlines()
                       if l.strip() and "->" not in l and not l.strip().endswith("/HEAD")]
    lots = {}
    for ref in refs:
        for chemin in git("ls-tree", "-r", "--name-only", ref).splitlines():
            m = MOTIF_HTML.search(chemin)
            ia = proprietaire(chemin)
            if not m or not ia:
                continue
            lot = f"LOT_{m.group(1)}"
            nom = "Phase_A" if m.group(2) == "A" else f"DX.{m.group(3)}"
            e = lots.setdefault(lot, {}).setdefault(nom, {"ia": set(), "branches": set(), "depose": False})
            e["ia"].add(ia); e["branches"].add(ref)
            if chemin.startswith("LOT_Claude_Finaux/"):
                e["depose"] = True
    return lots


def etat_lots(lots):
    etat = charger(R / "LOT_Claude_Finaux" / "ETAT_FILE.json", {"lots": []})
    statut = {f"LOT_{l['lot']}": l for l in etat.get("lots", [])}
    res = reservations()
    sortie = []
    for n in range(1, TOTAL + 1):
        lot = f"LOT_{n:03d}"
        f = lots.get(lot, {})
        ias = sorted({i for v in f.values() for i in v["ia"]})
        s = statut.get(lot, {})
        if s.get("depose") or any(v["depose"] for v in f.values()):
            st = "DÉPOSÉ"
        elif f:
            st = "AMORCÉ"
        else:
            st = "LIBRE"
        reserve = next((ia for ia, (a, b) in res.items() if a <= n <= b), None)
        sortie.append({"lot": lot, "code": s.get("code", ""), "statut": st, "ia": ias, "reserve_a": reserve,
                       "fichiers": {k: sorted(v["ia"]) for k, v in sorted(f.items())},
                       "verrou": "lecture seule pour les autres IA" if ias else ""})
    return sortie


def ecrire_clones(sortie):
    resume = {"genere_le": maintenant(), "sha_lois": sha_lois(), "lots": sortie}
    md = [f"# REGISTRE IA — état au {resume['genere_le']}", "", LOIS, "",
          "| LOT | Code | Statut | IA | Réservé à | Fichiers |", "|---|---|---|---|---|---|"]
    for l in sortie:
        if l["statut"] == "LIBRE" and not l["reserve_a"]:
            continue
        md.append(f"| {l['lot']} | {l['code']} | {l['statut']} | {', '.join(l['ia']) or '—'} | {l['reserve_a'] or '—'} | {len(l['fichiers'])}/11 |")
    source = SOURCE.exists() and Path(__file__).resolve() == SOURCE.resolve()
    # Lancé depuis harnais/ (Claude) : met à jour les trois clones. Lancé depuis un clone : seulement son dossier.
    for d in ([R / DOSSIER[ia] for ia in IAS] if source else [Path(__file__).resolve().parent]):
        d.mkdir(exist_ok=True)
        if source:
            shutil.copy2(SOURCE, d / "registre_ia.py")
        (d / "REGISTRE.json").write_text(json.dumps(resume, ensure_ascii=False, indent=1), encoding="utf-8")
        (d / "REGISTRE.md").write_text("\n".join(md) + "\n", encoding="utf-8")



# ---------- couple obligatoire : harnais identique + routage créé et surveillé ----------
POSTES = ("redacteur-phase-a", "redacteur", "auditeur-medical", "auditeur-conformite", "transversale", "mecanique")
HARNAIS_FICHIERS = ("harnais/taille_xy.py", "harnais/verif_refonte.py", "harnais/controle_lot.py", "harnais/audit_langue.py",
                    "harnais/registre_ia.py", "ressources_ia/outils/aips.py", "ressources_ia/outils/suivi_ia.py",
                    "harnais/modele_lecon/MODELE_DD_V8.html", "harnais/modele_lecon/style_lecon.css")
MANIFESTE = R / "harnais" / "HARNAIS_MANIFESTE.json"


def sha(p):
    return hashlib.sha256((R / p).read_bytes()).hexdigest() if (R / p).exists() else None


def ecrire_manifeste():
    MANIFESTE.write_text(json.dumps({"genere_le": maintenant(), "fichiers": {f: sha(f) for f in HARNAIS_FICHIERS}},
                                    ensure_ascii=False, indent=1), encoding="utf-8")


def harnais_identique():
    m = charger(MANIFESTE, {}).get("fichiers", {})
    if not m:
        return False, "manifeste du harnais absent (harnais/HARNAIS_MANIFESTE.json)"
    diff = [f for f, s in m.items() if sha(f) != s]
    return (not diff), ("harnais identique" if not diff else f"harnais modifié ou absent : {', '.join(diff)}")


def routage_pret(ia):
    """Routage créé par l'IA : configuration valide, script autotesté, veille vivante (moins de 30 min)."""
    if ia == "claude":
        agents = [R / ".claude" / "agents" / f"{a}.md" for a in ("redacteur", "redacteur-phase-a", "auditeur-medical", "auditeur-conformite", "mecanique")]
        if not all(a.exists() for a in agents):
            return False, "routage Claude incomplet : définitions .claude/agents/*.md manquantes"
        j = R / "journal" / "routage.jsonl"
        if not j.exists():
            return False, "journal/routage.jsonl absent"
        return True, "routage Claude (.claude/agents, journal/routage.jsonl)"
    d = R / DOSSIER[ia]; IA = ia.upper()
    conf = charger(d / f"ROUTAGE_{IA}.json", None)
    if not conf:
        return False, f"{DOSSIER[ia]}/ROUTAGE_{IA}.json absent (table poste → modèle à créer)"
    postes = conf.get("postes", {})
    manque = [p for p in POSTES if not (isinstance(postes.get(p), dict) and postes[p].get("modele"))]
    if manque:
        return False, f"ROUTAGE_{IA}.json : postes sans modèle : {', '.join(manque)}"
    if postes["redacteur"].get("modele") == postes["auditeur-medical"].get("modele") and not conf.get("audit_croise_externe"):
        return False, "ROUTAGE : l'auditeur médical doit être un autre modèle que le rédacteur (ou déclarer audit_croise_externe)"
    script = d / f"routage_{ia}.py"
    if not script.exists():
        return False, f"{DOSSIER[ia]}/routage_{ia}.py absent (script de routage à créer)"
    try:
        r = subprocess.run([sys.executable, str(script), "autotest"], capture_output=True, text=True, timeout=60, cwd=str(R))
        if r.returncode != 0:
            return False, f"routage_{ia}.py autotest en échec : {(r.stdout + r.stderr).strip()[:200]}"
    except Exception as e:
        return False, f"routage_{ia}.py autotest impossible : {e}"
    pouls = d / ".veille_routage"
    try:
        age = (datetime.datetime.now(ZURICH) - datetime.datetime.fromisoformat(pouls.read_text().strip())).total_seconds()
    except Exception:
        return False, f"veille du routage inactive ({DOSSIER[ia]}/.veille_routage absent : lancer routage_{ia}.py veille)"
    if age > 1800:
        return False, f"veille du routage arrêtée depuis {int(age // 60)} min (relancer routage_{ia}.py veille)"
    return True, "routage prêt et surveillé"


def pret(ia):
    for ok, msg in (harnais_identique(), routage_pret(ia)):
        if not ok:
            return False, "BLOQUÉ : " + msg
    return True, "couple harnais + routage prêt"


# ---------- lecture, signature, verrou ----------
def jeton(ia):
    jour = datetime.date.today().isoformat()
    return hashlib.sha256(f"{ia}|{jour}|{sha_lois()}".encode()).hexdigest()[:10]


def signe(ia):
    log = R / DOSSIER[ia] / "SIGNATURES.log"
    if not log.exists():
        return False
    attendu = f"jeton={jeton(ia)}"
    return any(attendu in l for l in log.read_text(encoding="utf-8").splitlines())


def verifier(ia, lot, sortie=None):
    if ia not in IAS:
        return False, f"IA inconnue : {ia}"
    if not signe(ia):
        return False, "BLOQUÉ : registre non lu ou non signé aujourd'hui (lire puis signer)"
    ok, msg = pret(ia)
    if not ok:
        return False, msg
    if autorise_par_vial(ia, lot):
        return True, "AUTORISÉ par Vial (IA_AUTORISATIONS.json)"
    sortie = sortie or etat_lots(releve())
    l = next((x for x in sortie if x["lot"] == lot), None)
    if not l:
        return False, f"BLOQUÉ : LOT inconnu {lot}"
    autres = [i for i in l["ia"] if i != ia]
    if autres:
        return False, f"BLOQUÉ : {lot} amorcé par {', '.join(autres)} (lecture seule ; accord de Vial requis)"
    if l["statut"] == "DÉPOSÉ":
        return False, f"BLOQUÉ : {lot} déjà déposé (accord de Vial requis)"
    if l["reserve_a"] != ia:
        return False, f"BLOQUÉ : {lot} réservé à {l['reserve_a'] or 'personne'} (IA_RESERVATIONS.json)"
    if l["ia"] == [ia]:
        return True, f"AUTORISÉ : {lot} amorcé par toi seul ; continue sans réécrire un chapitre déjà rédigé"
    return True, f"AUTORISÉ : {lot} libre et réservé à {ia}"


def garde_claude():
    """Hook pre-commit de Claude : harnais identique, routage en place, et toute leçon commitée a une passe dans journal/routage.jsonl."""
    ok, msg = pret("claude")
    if not ok:
        print(msg); return 1
    passes = set()
    for x in (R / "journal" / "routage.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            o = json.loads(x); passes.add((o.get("lot"), str(o.get("fichier", "")).split(" ")[0]))
        except Exception:
            pass
    err = []
    for f in [l for l in git("diff", "--cached", "--name-only", "--diff-filter=AM").splitlines() if l]:
        if not f.startswith(("LOTS_V8/", "lot en cours de production/", "LOT_Claude_Finaux/")):
            continue
        h = re.search(r"(LOT_\d{3})_Phase_(A|B)_V0(?:_(DX\.\d+))?\.html$", f)
        if h and (h.group(1), "Phase_A" if h.group(2) == "A" else h.group(3)) not in passes \
           and (h.group(1), "Phase_A" if h.group(2) == "A" else h.group(3)) not in {(l, x.replace("Phase_A", "Phase_A")) for l, x in passes}:
            if not any(l == h.group(1) and (x.startswith("Phase_A") if h.group(2) == "A" else x.startswith("DX.") and (h.group(3) in x or x == "DX.1–10")) for l, x in passes):
                err.append(f"{f} : aucune passe consignée dans journal/routage.jsonl")
    for e in err:
        print("BLOQUÉ :", e)
    return 1 if err else 0


def garde(ia):
    """Hook pre-commit : bloque les fichiers hors du dossier de l'IA et les LOTS interdits."""
    if ia == "claude":
        return garde_claude()
    indexes = [l for l in git("diff", "--cached", "--name-only").splitlines() if l]
    if not signe(ia):
        print("BLOQUÉ : registre non lu ou non signé aujourd'hui."); return 1
    ok, msg = pret(ia)
    if not ok:
        print(msg); return 1
    journal = R / DOSSIER[ia] / f"ROUTAGE_{ia.upper()}.jsonl"
    passes = set()
    if journal.exists():
        for x in journal.read_text(encoding="utf-8").splitlines():
            try:
                o = json.loads(x); passes.add((o.get("lot"), o.get("fichier")))
            except Exception:
                pass
    sortie = etat_lots(releve())
    erreurs = []
    for f in indexes:
        if not f.startswith(DOSSIER[ia] + "/"):
            erreurs.append(f"hors de ton dossier : {f}"); continue
        if f.endswith("registre_ia.py"):
            erreurs.append(f"fichier du registre (lecture seule) : {f}"); continue
        m = re.search(r"/(LOT_\d{3})/", f)
        h = re.search(r"(LOT_\d{3})_Phase_(A|B)_V0(?:_(DX\.\d+))?\.html$", f)
        if h and (h.group(1), "Phase_A" if h.group(2) == "A" else h.group(3)) not in passes:
            erreurs.append(f"{f} : aucune passe consignée par le routage (routage_{ia}.py consigner …)")
        if m:
            ok, msg = verifier(ia, m.group(1), sortie)
            if not ok:
                erreurs.append(f"{f} : {msg}")
    for e in erreurs:
        print("BLOQUÉ :", e)
    return 1 if erreurs else 0


def installer(ia):
    h = R / ".git" / "hooks" / "pre-commit"
    h.write_text(f"#!/bin/sh\nexec python3 \"$(git rev-parse --show-toplevel)/{DOSSIER[ia]}/registre_ia.py\" garde {ia}\n")
    h.chmod(0o755)
    print(f"Hook pre-commit bloquant installé pour {ia}.")


def main(a):
    cmd = a[0] if a else "etat"
    if cmd == "etat":
        s = etat_lots(releve()); ecrire_clones(s)
        c = {k: sum(1 for x in s if x["statut"] == k) for k in ("DÉPOSÉ", "AMORCÉ", "LIBRE")}
        print(f"REGISTRE : {c['DÉPOSÉ']} déposés, {c['AMORCÉ']} amorcés, {c['LIBRE']} libres ; clones écrits dans {', '.join(DOSSIER.values())}")
    elif cmd == "lire" and len(a) > 1:
        s = etat_lots(releve()); ecrire_clones(s)
        print(LOIS); print()
        ia = a[1]; a_faire = [x["lot"] for x in s if x["reserve_a"] == ia and x["statut"] == "LIBRE"][:5]
        print(f"Ta plage ({ia}) : prochains LOTS libres : {', '.join(a_faire) or 'aucun'}")
        print(f"Jeton de lecture du jour : {jeton(ia)}  →  python3 {DOSSIER.get(ia, '?')}/registre_ia.py signer {ia} {jeton(ia)}")
    elif cmd == "signer" and len(a) > 2:
        ia, j = a[1], a[2]
        if ia not in IAS or j != jeton(ia):
            print("Jeton invalide : relance `lire`."); return 1
        log = R / DOSSIER[ia] / "SIGNATURES.log"; log.parent.mkdir(exist_ok=True)
        with log.open("a", encoding="utf-8") as f:
            f.write(f"{maintenant()} ia={ia} jeton={j} lois={sha_lois()} : j'ai lu les lois et l'état du registre.\n")
        print(f"Signature enregistrée pour {ia}.")
    elif cmd == "verifier" and len(a) > 2:
        ok, msg = verifier(a[1], a[2]); print(msg); return 0 if ok else 1
    elif cmd == "garde" and len(a) > 1:
        return garde(a[1])
    elif cmd == "pret" and len(a) > 1:
        ok, msg = pret(a[1]); print(msg); return 0 if ok else 1
    elif cmd == "manifeste":
        ecrire_manifeste(); print("manifeste du harnais écrit")
    elif cmd == "installer" and len(a) > 1:
        installer(a[1])
    else:
        print(__doc__); return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
