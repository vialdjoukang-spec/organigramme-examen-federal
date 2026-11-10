#!/usr/bin/env python3
"""Archive les tentatives P1 déjà auditées ; ne produit aucune leçon."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys


def git(*args):
    return subprocess.run(['git', *args], check=True, text=True, capture_output=True).stdout


def main():
    root = Path.cwd()
    notes = {}
    debut = int(sys.argv[1]) if len(sys.argv) > 1 else 86
    assert 86 <= debut <= 102
    for n in range(debut, 103):
        d = root / f'ChatGPT_Codex/LOT_{n:03d}'
        prep = (d / '_travail/preparation_sources.json').read_bytes()
        audit = (d / 'audits/P1.audit.json').read_bytes()
        s, a = json.loads(prep), json.loads(audit)
        assert a['verdict'] == 'NON_FRANCHIE'
        assert a['preparation_sha256'] == hashlib.sha256(prep).hexdigest()
        assert a['auditeur'] != s['collecteur']
        titre = s['ssp']
        if isinstance(titre, dict):
            titre = titre['code'] + ' — ' + titre['intitule']
        assert isinstance(titre, str)
        assert all(isinstance(x, str) for z in s['sources'] for x in z['extraits'])
        notes[n] = prep, audit, titre

    for n, (prep, audit, titre) in notes.items():
        branch = f'codex/lot-{n:03d}'
        existe = subprocess.run(['git', 'show-ref', '--verify', '--quiet', f'refs/heads/{branch}']).returncode == 0
        git('switch', branch) if existe else git('switch', '-c', branch, 'origin/main')
        d = root / f'ChatGPT_Codex/LOT_{n:03d}'
        (d / '_travail').mkdir(parents=True, exist_ok=True)
        (d / 'audits').mkdir(exist_ok=True)
        (d / '_travail/preparation_sources.json').write_bytes(prep)
        (d / 'audits/P1.audit.json').write_bytes(audit)
        s, a = json.loads(prep), json.loads(audit)
        ev = d / '_travail/evidence'
        ev.mkdir(exist_ok=True)
        textes = []
        for i, source in enumerate(s['sources'], 1):
            if not source['extraits']:
                continue
            f = ev / f'source-{i:02d}.txt'
            f.write_text(f"URL: {source['url']}\nConsulté: {s['date']}\n\n" + '\n\n'.join(source['extraits']) + '\n')
            textes.append(str(f))
        pa = d / '_travail/PA/paquet.json'
        subprocess.run([sys.executable, 'ChatGPT_Codex/_outils/paquet.py', '--entite', titre,
                        '--sortie', str(pa), '--registres', 'data/ck/src.json',
                        'tools/prevalences/sources_reconnues.json', '--textes', *textes],
                       check=True, stdout=subprocess.DEVNULL)
        assert json.loads(pa.read_text())['passages']
        decision = f'''# LOT_{n:03d} — décision de séance

Ordre de Vial du 10 novembre 2026 : contenu seul ; images et perfectionnement renvoyés à une passe commune. Branche `{branch}` créée depuis `main` après consolidation préalable ; écritures limitées au ressort autorisé.

Référence unique : prompt Lo_9.11.26 et outils de `reference/prompts-9.11.26`, commit `037545b80fe03166dec9e05f70e24fb9f008821d` (absents du main initial). Détection : aucune des 253 leçons des LOTs 080–102 n'existe. Consolidation : 858 copies vérifiées, PR516 fusionnée après CI verte.

E2/E3 : recherche par `{s['collecteur']}`, extraits archivés, `paquet.py` original exécuté. E4 : audit indépendant par `{a['auditeur']}` ; P1 non franchie. Aucun gel de liste, aucun lancement des dix DX, aucun HTML produit. Le blocage est consigné puis la file passe au LOT suivant après cette tentative, selon l'ordre de Vial.
'''
        (d / 'DECISION_SEANCE.md').write_text(decision)
        candidats = s.get('candidats_non_classes', [])
        (d / '_travail/LISTE_DX_BROUILLON.md').write_text(
            '# Candidats documentaires — liste non gelée\n\nCes noms ne constituent ni dix diagnostics sélectionnés ni un classement ; aucun numéro DX ni rang E ne leur est attribué.\n\n'
            + '\n'.join('- ' + (x if isinstance(x, str) else json.dumps(x, ensure_ascii=False)) for x in candidats) + '\n')
        limites = s.get('limites', [])
        if isinstance(limites, str):
            limites = [limites]
        (d / 'HELP.md').write_text(f"# LOT_{n:03d} — obstacles documentaires\n\n## Porte P1\n\n{s['constat_p1']}\n\n"
            + '\n'.join('- ' + x for x in a['motifs']) + '\n\n## Conditions de reprise\n\n'
            + '\n'.join('- ' + x for x in a['conditions_reprise']) + '\n\n## Limites du paquet consulté\n\n'
            + '\n'.join('- ' + x for x in limites) + '\n\n## Sources déjà consultées le 10.11.2026\n\n'
            + '\n'.join('- ' + z['url'] for z in s['sources'])
            + '\n\nCes résultats ne démontrent pas une absence de données dans toute la littérature.\n')
        (d / 'JOURNAL.md').write_text(f'''2026-11-10 | E0 | aucune leçon existante dans le LOT.
2026-11-10 | E1 | branche {branch} créée depuis main.
2026-11-10 | E2 | sources lues et extraits archivés ; paquet.py original exécuté.
2026-11-10 | E3–E4 | candidats non classés ; audit indépendant P1 NON_FRANCHIE lié au SHA-256 des preuves.
2026-11-10 | suite | aucun HTML ni score clinique ; blocage consigné, LOT suivant.
''')
        etat = dict(lot=f'LOT_{n:03d}', statut='BLOQUE_P1', porte='P1', audit='audits/P1.audit.json',
                    preparation_sha256=hashlib.sha256(prep).hexdigest(),
                    paquet_sha256=hashlib.sha256(pa.read_bytes()).hexdigest(),
                    html_produits=[], liste_gelee=False, motifs=a['motifs'], prochaine_action=a['conditions_reprise'])
        (d / 'ETAT_FILE.json').write_text(json.dumps(etat, ensure_ascii=False, indent=1) + '\n')
        (root / 'ChatGPT_Codex/JOURNAL_NUIT.md').write_text(f'''# Journal — ordre de Vial du 10 novembre 2026

Consolidation préalable : 858 leçons existantes copiées à destination unique et vérifiées par empreinte ; neuf copies périmées supprimées dans le ressort calculé. PR516 fusionnée après CI verte : https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/516 . Aucune des 253 leçons absentes des LOTs 080–102 n'est produite par cette récupération.

## Tentative LOT_{n:03d}

Sources et paquet préparatoire dans `LOT_{n:03d}/_travail/` ; audit indépendant dans `LOT_{n:03d}/audits/P1.audit.json`. P1 non franchie :

''' + '\n'.join('- ' + x for x in a['motifs']) + f'''

La branche `{branch}` conserve les preuves. Aucun HTML, score clinique ou gel de liste n'est annoncé. Passage au LOT suivant après cette tentative documentée.

LOTs livrés (080–102) : 0 ; leçons nouvelles poussées : 0 ; leçons existantes consolidées et poussées : 858 ; blocages : P1 LOT_{n:03d}, dix positions non démontrées par le paquet consulté.
''')
        git('add', '--', f'ChatGPT_Codex/LOT_{n:03d}', 'ChatGPT_Codex/JOURNAL_NUIT.md')
        changed = git('diff', '--cached', '--name-only', '-z').split('\0')
        assert all(not x or x == 'ChatGPT_Codex/JOURNAL_NUIT.md' or x.startswith(f'ChatGPT_Codex/LOT_{n:03d}/') for x in changed)
        git('commit', '-q', '-m', f'LOT_{n:03d} : sources, paquet et blocage P1 audité')
        git('push', '-q', '-u', 'origin', 'HEAD')
        print(f'LOT_{n:03d} : branche poussée ; P1 non franchie ; 0 leçon nouvelle.', flush=True)


if __name__ == '__main__':
    main()
