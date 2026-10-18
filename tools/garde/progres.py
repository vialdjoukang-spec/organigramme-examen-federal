#!/usr/bin/env python3
"""Garde du progrès (R15) · lancé toutes les CFG.cron_min minutes par .github/workflows/garde-progres.yml.

1. Mesure le contenu réel de origin/main : prévalences remplies, monographies complètes
   (tools/jauge/binomes.py), lignes de doses (data/ck/doses_ch.json), entrées du glossaire (data/ck/glo.json).
2. Compare au commit de main d'il y a CFG.fenetre_stall_min minutes (sans état : git rev-list --before).
3. Classe les PR fusionnées ou ayant reçu un commit dans la fenêtre : contenu / releve / autre.
STALL = aucun compteur n'a monté ET aucune PR de contenu active dans la fenêtre.
  → « @codex » sur « Pilote Codex » (au plus 1 par CFG.relance_codex_min) ;
  → après CFG.stalls_avant_vial stalls consécutifs : @vialdjoukang-spec (1 par CFG.appel_vial_min).
4. Recyclage des PR inactives (tools/garde/recyclage.py).

  progres.py [--sec] [--json]     --sec : n'écrit rien sur GitHub (essai local)
Code de sortie 0 toujours (une garde ne casse pas la file) ; le verdict est dans le résumé du job.
"""
import datetime as dt, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if "--sec" in sys.argv:
    os.environ["GARDE_SEC"] = "1"
from commun import (CFG, REPO, ROOT, api, classer, commenter, ecrire_etat, fichiers_pr, git, iso, lire_etat,
                    minutes_depuis, now, pilote, resume, tok_codex)

sys.path.insert(0, os.path.join(ROOT, "tools", "jauge"))
os.environ.setdefault("OEF_REPO", ROOT)
import binomes  # noqa: E402


def mesure(ref):
    R = binomes.mesurer(ref)
    def n(path):
        try:
            d = json.loads(binomes.show(ref, path) or "[]")
            return len(d) if isinstance(d, list) else len([k for k in d if not k.startswith("_")])
        except json.JSONDecodeError:
            return 0
    return {"prevalences": R["prevalences"]["ok"], "prev_total": R["prevalences"]["total"],
            "monographies": R["monographies"]["ok"], "mono_total": R["monographies"]["total"],
            "doses": n("data/ck/doses_ch.json"), "glossaire": n("data/ck/glo.json")}


COMPTEURS = ("prevalences", "monographies", "doses", "glossaire")


def activite(debut):
    """PR fusionnées dans main ou ayant reçu un commit depuis `debut` → [(n, classe, titre, quand)]."""
    out, vus = [], set()
    for ligne in git("log", "origin/main", "--first-parent", f"--since={iso(debut)}", "--format=%cI %s").splitlines():
        m = re.search(r"Merge pull request #(\d+)", ligne)
        if m and m.group(1) not in vus:
            vus.add(m.group(1))
            out.append((int(m.group(1)), classer(fichiers_pr(m.group(1))), "fusionnée", ligne[:25]))
    for p in api(f"repos/{REPO}/pulls?state=open&per_page=100") or []:
        if p["title"] == CFG["pilote_titre"] or str(p["number"]) in vus:
            continue
        c = (api(f"repos/{REPO}/commits/{p['head']['sha']}") or {}).get("commit", {}).get("committer", {}).get("date")
        if c and minutes_depuis(c) <= CFG["fenetre_stall_min"]:
            out.append((p["number"], classer(fichiers_pr(p["number"])), "ouverte", c))
    return out


def main():
    t = now()
    fen = CFG["fenetre_stall_min"]
    debut = t - dt.timedelta(minutes=fen)
    git("fetch", "-q", "origin", "main")
    base = git("rev-list", "-1", "--first-parent", f"--before={iso(debut)}", "origin/main") or "origin/main"
    M, B = mesure("origin/main"), mesure(base)
    monte = {k: M[k] - B[k] for k in COMPTEURS if M[k] > B[k]}
    act = activite(debut)
    contenu = [a for a in act if a[1] == "contenu"]
    stall = not monte and not contenu
    etat = lire_etat()
    etat.update(maj=iso(t), mesure=M)
    raisons = []
    if stall:
        etat["stalls"] = etat.get("stalls", 0) + (1 if minutes_depuis(etat.get("dernier_stall_compte")) >= fen else 0)
        if minutes_depuis(etat.get("dernier_stall_compte")) >= fen:
            etat["dernier_stall_compte"] = iso(t)
        etat.setdefault("stall_depuis", iso(t))
        rel = [a for a in act if a[1] == "releve"]
        raison = (f"aucun progrès de contenu en {fen} min (prév. {M['prevalences']}/{M['prev_total']}, "
                  f"mono {M['monographies']}/{M['mono_total']}, doses {M['doses']}, glossaire {M['glossaire']})"
                  + (f", seulement des relevés ({', '.join('#%d' % a[0] for a in rel)})" if rel else ""))
        raisons.append(raison)
        etape = json.loads(git("show", "origin/main:ETAT.json") or "{}").get("etape_courante", "?")
        if minutes_depuis(etat.get("derniere_relance")) >= CFG["relance_codex_min"]:
            n = pilote()
            if commenter(n, f"@codex Ordre de Vial : reprends l'étape {etape}, lot suivant. Rédige du contenu "
                         f"(prévalences/monographies), pas de relevé. Présente d'abord tes automates actifs "
                         f"(`python tools/garde/checkpoint.py --inventaire`).\n\nGarde R15 : {raison}.", tok_codex()):
                etat["derniere_relance"] = iso(t)
                raisons.append(f"relance @codex postée sur Pilote #{n}")
        else:
            raisons.append("relance @codex déjà faite il y a < %d min" % CFG["relance_codex_min"])
        if etat["stalls"] >= CFG["stalls_avant_vial"]:
            from appel import appeler
            if minutes_depuis(etat.get("dernier_appel_vial")) >= CFG["appel_vial_min"]:
                lien = f"https://github.com/{REPO}/pulls"
                if appeler(lien, f"Codex bloqué depuis {int(minutes_depuis(etat['stall_depuis'])) + fen} min : {raison}.",
                           etat, force=True):
                    etat["dernier_appel_vial"] = iso(t)
                    raisons.append("Vial mentionné (courriel)")
    else:
        etat.update(stalls=0)
        etat.pop("stall_depuis", None)
        etat.pop("dernier_stall_compte", None)
    from recyclage import recycler
    try:
        recycler(etat, poster=os.environ.get("GARDE_SEC") != "1")
    except Exception as x:  # le recyclage ne bloque jamais la garde
        resume(f"Recyclage en échec : {x}")
    resume(f"## Garde du progrès · {'STALL' if stall else 'OK'}\n"
           f"- Base {base[:7]} (il y a {fen} min) → main : {json.dumps(monte or 'aucune hausse')}\n"
           f"- Activité : {', '.join(f'#{a[0]} {a[1]} ({a[2]})' for a in act) or 'aucune PR'}\n"
           + "".join(f"- {r}\n" for r in raisons))
    ecrire_etat(etat)
    if "--json" in sys.argv:
        print(json.dumps({"stall": stall, "mesure": M, "base": B, "activite": act, "etat": etat}, ensure_ascii=False))
    return stall


if __name__ == "__main__":
    main()
