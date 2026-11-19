"""Enregistre une valeur lue à la source (après lecture humaine/IA). Refuse si le contexte est incomplet ou hors Europe.
Usage : python3 scripts/valider.py LOT DX eu|ch fichier.json   (fichier : un objet ou une liste de 1 à 3 paramètres)
Champs obligatoires : valeur_txt, unite, population, age_sexe, definition, mesure, annee, territoire, type_source, source, url ; conseillés : preuve, phrase."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from noyau import db, maintenant, journal
from recherche import conforme, initialiser
import plan

def valider(lot, dx, niv, P, agent=os.environ.get('EPI_AGENT', '?')):
    P = P if isinstance(P, list) else [P]
    for p in P:
        m = conforme(p, niv)
        if m: raise SystemExit(f'REFUSÉ (contexte incomplet ou hors Europe) : {", ".join(m)}')
        p['statut'] = 'vérifié'; p['hors_ch'] = int(niv == 'eu')
    c = db(); initialiser(c)
    old = json.loads((c.execute(f'SELECT params_{niv} FROM taches WHERE lot=? AND dx=?', (lot, dx)).fetchone() or ['[]'])[0])
    P = (old + P)[:3] if all(o.get('statut') == 'vérifié' for o in old) else P[:3]
    n = c.execute(f"UPDATE taches SET statut_{niv}='vérifié', params_{niv}=?, date=?, agent=? WHERE lot=? AND dx=?",
                  (json.dumps(P, ensure_ascii=False), maintenant(), agent, lot, dx)).rowcount
    c.commit(); journal(f'valider : LOT_{lot:03d} DX{dx} {niv} ({len(P)} valeur(s))')
    if not n: raise SystemExit('DX inconnu (N ou absent)')
    plan.generer(); print('OK', lot, dx, niv, len(P))

if __name__ == '__main__':
    valider(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], json.load(open(sys.argv[4])))
