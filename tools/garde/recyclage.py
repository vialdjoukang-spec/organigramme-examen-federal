#!/usr/bin/env python3
"""Recyclage (R15) : PR ouvertes et branches sans commit depuis CFG.recyclage_inactif_min minutes.
Commente « @codex reprends ou ferme avec motif » sur chaque PR inactive (anti-spam par PR),
ne ferme RIEN lui-même. Les PR attente-vial, infra et « Pilote Codex » sont exclues.
"""
import sys
from commun import CFG, REPO, api, commenter, iso, minutes_depuis, now, resume, tok_codex

EXCLUS = {"attente-vial", "infra"}


def dernier_commit(sha):
    c = api(f"repos/{REPO}/commits/{sha}")
    return (c or {}).get("commit", {}).get("committer", {}).get("date")


def recycler(etat, poster=True):
    seuil = CFG["recyclage_inactif_min"]
    vus = etat.setdefault("recyclage", {})
    prs = api(f"repos/{REPO}/pulls?state=open&per_page=100") or []
    inactives, branches_pr = [], set()
    for p in prs:
        branches_pr.add(p["head"]["ref"])
        labels = {l["name"] for l in p["labels"]}
        if p["title"] == CFG["pilote_titre"] or labels & EXCLUS:
            continue
        d = dernier_commit(p["head"]["sha"])
        m = minutes_depuis(d)
        if m >= seuil:
            inactives.append((m, p["number"], p["title"]))
    inactives.sort(reverse=True)
    postes = 0
    for m, n, t in inactives:
        if postes >= CFG["recyclage_max_par_passage"]:
            break
        if minutes_depuis(vus.get(str(n))) < CFG["recyclage_relance_par_pr_min"]:
            continue
        if poster and commenter(n, f"@codex Ordre de Vial (recyclage R15) : cette PR n'a reçu aucun commit depuis "
                                f"{int(m)} min. Reprends-la maintenant (audit, consignes, fusion) ou ferme-la avec un "
                                f"motif écrit. Ne la laisse pas à l'abandon.", tok_codex()):
            vus[str(n)] = iso(now())
            postes += 1
    # branches sans PR ni commit récent : signalées seulement
    orph = []
    for b in api(f"repos/{REPO}/branches?per_page=100") or []:
        nm = b["name"]
        if nm in branches_pr or nm in ("main", "gh-pages", CFG["etat_branche"], CFG["pilote_branche"]):
            continue
        orph.append(nm)
    resume(f"Recyclage : {len(inactives)} PR inactives ≥ {seuil} min "
           f"({', '.join('#%d' % n for _, n, _ in inactives) or 'aucune'}), {postes} relancées ; "
           f"{len(orph)} branches sans PR (signalées, rien supprimé).")
    return inactives, orph


if __name__ == "__main__":
    from commun import lire_etat, ecrire_etat
    e = lire_etat()
    recycler(e, poster="--sec" not in sys.argv)
    if "--sec" not in sys.argv:
        ecrire_etat(e)
