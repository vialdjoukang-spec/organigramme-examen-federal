#!/usr/bin/env python3
"""Calculateur multi-secteur : python3 tools/prevalences/jauges.py [--distant].

Les numérateurs cliniques proviennent exclusivement de data/ck/prev.json.
Une recherche ou un extrait candidat n'augmente jamais la couverture clinique.
"""
import argparse
from datetime import datetime, timezone
import html
import json
import math
from pathlib import Path
import subprocess
import sys
from zoneinfo import ZoneInfo
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.prevalences.moteur import ROOT, DEFAULT_STATE, CONFIG, atomic_json, catalog, expected_protocol


def valid_published(item, task, sources, today):
    if not isinstance(item, dict): return False
    if item.get('nom') != task['diagnostic'] or type(item.get('prev_pct')) not in (int, float): return False
    if not math.isfinite(item['prev_pct']) or not 0 < item['prev_pct'] <= 100 or item.get('statut') == 'À vérifier': return False
    date = item.get('date_lu', '')
    try: datetime.strptime(date, '%Y-%m-%d')
    except (ValueError, TypeError): return False
    return date <= today and isinstance(item.get('src'), str) and item['src'] in sources and isinstance(item.get('loc'), str) and bool(item['loc'].strip())


def measure(root=ROOT, states=None):
    ssps, tasks = catalog(root); original_states = states or {}; states = {}; loading_errors = []
    for category, state in original_states.items():
        if not isinstance(state, dict) or not isinstance(state.get('tasks'), dict):
            loading_errors.append({'categorie': category, 'motif': 'État non objet ou tâches invalides'})
        else: states[category] = state
    prev = json.loads((root / 'data/ck/prev.json').read_text())
    sources = {s['id'] for s in json.loads((root / 'data/ck/src.json').read_text())}
    today = datetime.now(timezone.utc).date().isoformat()
    report = {'version': 1, 'maj': datetime.now(timezone.utc).isoformat(timespec='seconds'),
              'definitions': {'tentes': 'Au moins un fournisseur a été interrogé (un échec reste visible).',
                              'recherches_abouties': 'Toutes les requêtes du protocole ont répondu ; cela ne prouve pas l’exhaustivité documentaire.',
                              'avec_candidats': 'Au moins un extrait chiffré associé lexicalement au diagnostic est conservé, relu ou à relire.',
                              'chiffres_sources': 'Chiffres publiés avec libellé, source, date et emplacement ; ce contrôle de structure ne vaut pas validation de médecin.'},
              'categories': {}, 'secteurs': {}, 'erreurs_chargement': loading_errors}
    for field, groups in [('categories', CONFIG['categories']), ('secteurs', list(dict.fromkeys(s[2] for s in ssps)))]:
        for group in groups:
            selected = [t for t in tasks if t['categorie' if field == 'categories' else 'secteur'] == group]
            selected_ssps = [s for s in ssps if (s[0][0] if field == 'categories' else s[2]) == group]
            metrics = dict(total=len(selected), ssp=len(selected_ssps), ssp_sans_dd=sum(not any(t['ssp'] == s[0] for t in selected) for s in selected_ssps),
                           tentes=0, recherches_abouties=0, partiels=0, erreurs=0, avec_candidats=0, candidats=0,
                           chiffres_sources=0, a_verifier=0, sans_chiffre=0, audits_statistiques=0, corrections_arithmetiques=0,
                           etats_obsoletes=0, valeurs_proposees=0, relectures_agent=0, derniere_recherche=None)
            for t in selected:
                state = states.get(t['categorie'], {})
                row = state.get('tasks', {}).get(t['key'], {})
                if row and row.get('fingerprint') != t['fingerprint']:
                    metrics['etats_obsoletes'] += 1; row = {}
                has_queries = bool(row.get('queries'))
                metrics['tentes'] += has_queries
                expected = expected_protocol()
                actual = [(q.get('provider'), q.get('id')) for q in row.get('queries', [])]
                complete = row.get('statut') == 'recherchee' and set(actual) == expected and len(actual) == len(expected) and all(q.get('ok') is True for q in row.get('queries', []))
                metrics['recherches_abouties'] += complete
                metrics['partiels'] += has_queries and any(q.get('ok') is True for q in row['queries']) and not complete
                metrics['erreurs'] += has_queries and not any(q.get('ok') is True for q in row['queries'])
                candidates = row.get('candidates', [])
                metrics['avec_candidats'] += bool(candidates); metrics['candidats'] += len(candidates)
                from tools.prevalences.relance_agent import review_completed
                metrics['relectures_agent'] += sum(review_completed(c) for c in candidates)
                metrics['valeurs_proposees'] += row.get('selection',{}).get('retenu') is not None
                metrics['audits_statistiques'] += sum(isinstance(c.get('audit'), dict) for c in candidates)
                metrics['corrections_arithmetiques'] += sum(len(c.get('audit', {}).get('corrections', [])) for c in candidates)
                if row.get('date_recherche'):
                    metrics['derniere_recherche'] = max(metrics['derniere_recherche'] or '', row['date_recherche'])
                item = next((i for i in prev.get(t['ssp'], {}).get('items', []) if i.get('i') == t['i']), {})
                ok = valid_published(item, t, sources, today)
                metrics['chiffres_sources'] += ok
                metrics['a_verifier'] += not ok and item.get('statut') == 'À vérifier'
                metrics['sans_chiffre'] += not ok
            metrics['progression'] = {k: round(100 * metrics[k] / metrics['total'], 2) if metrics['total'] else 0
                                      for k in ('tentes', 'recherches_abouties', 'avec_candidats', 'chiffres_sources')}
            report[field][group] = metrics
    summed = ['total', 'ssp', 'ssp_sans_dd', 'tentes', 'recherches_abouties', 'partiels', 'erreurs', 'avec_candidats', 'candidats', 'chiffres_sources', 'a_verifier', 'sans_chiffre', 'audits_statistiques', 'corrections_arithmetiques', 'etats_obsoletes', 'valeurs_proposees', 'relectures_agent']
    report['total'] = {k: sum(c[k] for c in report['categories'].values()) for k in summed}
    return report


def bar(n, total, width=20):
    count = int(width * n / total) if total else 0
    return '█' * count + '░' * (width-count) + f' {100*n/total if total else 0:5.1f} % ({n}/{total})'


def console(report, sectors=False):
    lines = ['Prévalences · recherche et chiffres sourcés', '']
    rows = report['secteurs'] if sectors else report['categories']
    for name, m in rows.items():
        lines += [f"{name} · {m['ssp']} SSP · {m['ssp_sans_dd']} sans différentiel",
                  f"  Recherche aboutie {bar(m['recherches_abouties'], m['total'])}",
                  f"  Chiffres sourcés   {bar(m['chiffres_sources'], m['total'])}",
                  f"  Tentés : {m['tentes']} · extraits : {m['candidats']}, relus : {m['relectures_agent']} · partiels : {m['partiels']} · erreurs : {m['erreurs']} · propositions : {m['valeurs_proposees']}"]
    t = report['total']
    lines += ['', f"TOTAL chiffres sourcés {bar(t['chiffres_sources'], t['total'])}",
              f"{t['ssp_sans_dd']}/{t['ssp']} SSP sans différentiel : leur contenu reste à rédiger.",
              'Les candidats ne comptent pas comme chiffres vérifiés.']
    return '\n'.join(lines)


def page(report):
    def group_table(rows):
        out = []
        for name, m in rows.items():
            cells = [f'<th scope="row">{html.escape(name)}</th>', f"<td>{m['ssp']}</td>", f"<td>{m['total']}</td>"]
            for field in ('recherches_abouties', 'chiffres_sources'):
                label = f"{name} : {m[field]} sur {m['total']}"
                cells.append(f'<td><progress aria-label="{label}" max="{max(1,m["total"])}" value="{m[field]}"></progress><br>{m[field]}/{m["total"]} · {m["progression"][field]:g} %</td>')
            cells += [f"<td>{m['candidats']}</td>", f"<td>{m['partiels']} / {m['erreurs']}</td>", f"<td>{m['ssp_sans_dd']}</td>", f"<td>{m['audits_statistiques']} / {m['corrections_arithmetiques']}</td>"]
            out.append('<tr>'+''.join(cells)+'</tr>')
        return '<div class="scroll"><table><thead><tr><th>Groupe</th><th>SSP</th><th>Diagnostics</th><th>Recherche aboutie</th><th>Chiffres sourcés</th><th>Candidats</th><th>Partiels / erreurs</th><th>SSP sans DD</th><th>Contrôles / corrections</th></tr></thead><tbody>'+''.join(out)+'</tbody></table></div>'
    local_date = datetime.fromisoformat(report['maj']).astimezone(ZoneInfo('Europe/Zurich')).strftime('%d.%m.%Y à %H:%M · Europe/Zurich')
    content = group_table(report['categories']) + '<h2>Les 19 secteurs</h2>' + group_table(report['secteurs'])
    definitions = ''.join('<dt>'+html.escape(k)+'</dt><dd>'+html.escape(v)+'</dd>' for k,v in report['definitions'].items())
    t = report['total']
    return f'''<!doctype html>
<html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="refresh" content="300">
<title>Prévalences · jauges par catégorie et secteur</title>
<style>body{{font:17px/1.5 system-ui;background:#fbfbf8;color:#17212b;margin:0}}main{{max-width:1200px;margin:auto;padding:24px}}a{{color:#17469a}}.scroll{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;background:white}}th,td{{padding:12px;text-align:left;border:1px solid #d3d8dc}}progress{{max-width:160px;width:100%;accent-color:#1e608c}}dt{{font-weight:700}}dd{{margin-bottom:12px}}.meta{{color:#424d56}}</style>
<main><h1>Prévalences · recherche et chiffres sourcés</h1>
<p>{t['chiffres_sources']}/{t['total']} diagnostics ont un chiffre sourcé publié. {t['candidats']} extraits sont conservés : {t['relectures_agent']} relus et {t['candidats']-t['relectures_agent']} à relire.</p>
<p class="meta">Calcul : {html.escape(local_date)}. Actualisation de la page toutes les 5 minutes ; une recherche planifiée peut être retardée.</p>
<p><a href="./app_v2.html">Application</a> · <a href="./progres.html">Autres jauges</a> · <a href="./prevalences.json">Données des jauges</a> · <a href="./prevalences-erreurs.pdf">Synthèse PDF des erreurs</a> · <a href="./prevalences-erreurs.json">Registre des contrôles</a> · <a href="https://github.com/vialdjoukang-spec/organigramme-examen-federal/tree/automates/prevalences">Recherches, erreurs et audit statistique</a></p>
<h2>Les quatre catégories</h2>{content}<p>Les propositions retenues par le contrôle statistique restent des candidats ; elles ne sont jamais additionnées aux chiffres cliniques publiés.</p><h2>Lecture des jauges</h2><dl>{definitions}</dl>
<p>{t['ssp_sans_dd']} SSP sans différentiel restent à rédiger. Les chiffres candidats, la progression des recherches et la validation clinique sont des mesures distinctes.</p></main></html>'''


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state-dir', default=str(DEFAULT_STATE)); p.add_argument('--distant', action='store_true', help='lit la branche de suivi après fetch, sans changer de branche')
    p.add_argument('--json', action='store_true'); p.add_argument('--secteurs', action='store_true'); p.add_argument('--output', help='dossier des sorties jauges.json/html et README.md')
    args = p.parse_args(argv); states = {}
    if args.distant:
        subprocess.run(['git','-C',str(ROOT),'fetch','origin','automates/prevalences:refs/remotes/origin/automates/prevalences'], check=True, stdout=subprocess.DEVNULL)
        for c in CONFIG['categories']:
            r = subprocess.run(['git','-C',str(ROOT),'show',f'origin/automates/prevalences:{c}.json'],capture_output=True,text=True)
            if r.returncode == 0: states[c] = json.loads(r.stdout)
    else:
        for c in CONFIG['categories']:
            path = Path(args.state_dir) / f'{c}.json'
            if path.exists(): states[c] = json.loads(path.read_text())
    from tools.prevalences.auditeur import audit_state
    from tools.prevalences.selection import selectionner
    from tools.prevalences.moteur import load_registry
    # La jauge est le point central : réappliquer audit et sélection en lecture
    # de l'instantané ; les écritures de candidats restent dans les automates.
    for category, state in list(states.items()):
        if not isinstance(state,dict) or not isinstance(state.get('tasks'),dict): continue
        state, _ = audit_state(state)
        for row in state['tasks'].values():
            if isinstance(row,dict): row['selection'] = selectionner(row.get('candidates',[]),load_registry())
        states[category] = state
    report = measure(states=states)
    from tools.prevalences.rapport import centraliser, ecrire_pdf
    code_errors = json.loads((ROOT/'audit/PREVALENCES_ERREURS_CODE.json').read_text())
    previous_file = Path(args.output)/'erreurs.json' if args.output else Path(args.state_dir)/'erreurs.json'
    previous = json.loads(previous_file.read_text()) if previous_file.exists() else None
    if not isinstance(previous,dict): previous = None
    errors = centraliser(states,code_errors,previous)
    errors['maj'] = report['maj']
    report['controle_statistique'] = errors['synthese']
    report['selections'] = {category: {key: row.get('selection',{}) for key,row in state.get('tasks',{}).items() if isinstance(row,dict)} for category,state in states.items() if isinstance(state,dict)}
    if args.output:
        out = Path(args.output); out.mkdir(parents=True,exist_ok=True)
        atomic_json(out/'erreurs.json',errors)
        ecrire_pdf(out/'erreurs.pdf',report,errors)
        atomic_json(out/'jauges.json',report); (out/'jauges.html').write_text(page(report),encoding='utf-8')
        (out/'README.md').write_text('# Suivi automatique des prévalences\n\n'+console(report)+'\n\nJauges publiques : https://vialdjoukang-spec.github.io/organigramme-examen-federal/prevalences.html\n\nLes fichiers G.json, S.json, F.json et O.json conservent les requêtes, erreurs, candidats et audits. Aucune écriture de données cliniques par les robots.\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=1) if args.json else console(report,args.secteurs))
    return 0


if __name__ == '__main__': raise SystemExit(main())
