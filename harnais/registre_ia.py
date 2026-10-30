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
    for ia in IAS:
        d = R / DOSSIER[ia]
        d.mkdir(exist_ok=True)
        if SOURCE.exists() and Path(__file__).resolve() == SOURCE.resolve():
            shutil.copy2(SOURCE, d / "registre_ia.py")
        (d / "REGISTRE.json").write_text(json.dumps(resume, ensure_ascii=False, indent=1), encoding="utf-8")
        (d / "REGISTRE.md").write_text("\n".join(md) + "\n", encoding="utf-8")


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


def garde(ia):
    """Hook pre-commit : bloque les fichiers hors du dossier de l'IA et les LOTS interdits."""
    if ia == "claude":
        return 0
    indexes = [l for l in git("diff", "--cached", "--name-only").splitlines() if l]
    if not signe(ia):
        print("BLOQUÉ : registre non lu ou non signé aujourd'hui."); return 1
    sortie = etat_lots(releve())
    erreurs = []
    for f in indexes:
        if not f.startswith(DOSSIER[ia] + "/"):
            erreurs.append(f"hors de ton dossier : {f}"); continue
        if f.endswith(("registre_ia.py", "REGISTRE.json", "REGISTRE.md")):
            erreurs.append(f"fichier du registre (lecture seule) : {f}"); continue
        m = re.search(r"/(LOT_\d{3})/", f)
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
    elif cmd == "installer" and len(a) > 1:
        installer(a[1])
    else:
        print(__doc__); return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
