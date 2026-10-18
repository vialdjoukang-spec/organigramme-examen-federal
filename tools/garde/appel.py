#!/usr/bin/env python3
"""Appel de Vial (R15) : une ligne sur « Pilote Codex » avec @vialdjoukang-spec (courriel GitHub),
puis un « @codex » qui ordonne de continuer ailleurs, sans jamais attendre Vial.

  appel.py --lien URL --decision "texte d'une ligne" [--force]
Anti-spam : au plus un appel par lien et par CFG.appel_vial_min (état sur la branche garde/etat).
"""
import argparse, sys
from commun import CFG, api, commenter, ecrire_etat, iso, lire_etat, minutes_depuis, now, pilote, tok_bot, tok_codex, resume


def appeler(lien, decision, etat, force=False):
    cle = f"vial:{lien}"
    vus = etat.setdefault("appels", {})
    if not force and minutes_depuis(vus.get(cle)) < CFG["appel_vial_min"]:
        resume(f"Appel déjà fait pour {lien} il y a < {CFG['appel_vial_min']} min : rien.")
        return False
    n = pilote()
    ok = commenter(n, f"@{CFG['vial']} Décision requise : {decision} → {lien}", tok_bot())
    commenter(n, "@codex Ordre de Vial : n'attends pas sa réponse sur " + lien +
              ". Continue tout de suite le lot suivant de l'étape courante (rédaction de contenu), "
              "puis reviens à ce point quand l'étiquette vial-ok apparaît.", tok_codex())
    if ok:
        vus[cle] = iso(now())
    resume(f"Appel de Vial : {decision} ({lien}) → Pilote #{n}")
    return ok


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--lien", required=True)
    a.add_argument("--decision", required=True)
    a.add_argument("--force", action="store_true")
    x = a.parse_args()
    e = lire_etat()
    if appeler(x.lien, " ".join(x.decision.split())[:240], e, x.force):
        ecrire_etat(e)
