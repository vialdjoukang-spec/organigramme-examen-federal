#!/usr/bin/env python3
"""Suivi couplé 8/9, sans écriture clinique ni validation automatique."""
import argparse
from collections import Counter
from datetime import date, datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.prevalences.moteur import ROOT, DEFAULT_STATE, atomic_json, catalog
from tools.prevalences.jauges import valid_published
from tools.mono_build import mid, REQ, prototype_ready, load_ssp

CONFIG = json.loads(Path(__file__).with_name('config.json').read_text())

def empreinte(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def texte(value): return isinstance(value, str) and bool(value.strip())

def date_valide(value):
    try: return isinstance(value, str) and date.fromisoformat(value) <= date.today()
    except ValueError: return False

def attestation(record, value, root, sources, fingerprint=None):
    if not isinstance(record, dict): return False
    if record.get('statut') != 'revue_documentaire' or record.get('validation_clinique') is not False: return False
    if record.get('sha256') != empreinte(value) or not date_valide(record.get('date_lu')): return False
    if fingerprint is not None and record.get('fingerprint') != fingerprint: return False
    ids = record.get('sources')
    if not isinstance(ids, list) or not ids or any(not isinstance(x,str) or x not in sources for x in ids): return False
    path = record.get('rapport')
    if not texte(path): return False
    target = (root / path).resolve()
    if not target.is_relative_to(root.resolve()) or not target.is_file(): return False
    return record.get('rapport_sha256') == hashlib.sha256(target.read_bytes()).hexdigest()

def relecture_prototype(record, value, root, sources):
    return (isinstance(record, dict) and record.get('chronologie_relue') is True
            and attestation(record, value, root, sources))

def calculer(root=ROOT, states=None, ledger=None, config=None):
    config = config or CONFIG; ledger = ledger or {}; states_provided = states is not None; states = states or {}
    ssps, tasks = catalog(root)
    sources = {s['id']:s for s in json.loads((root/'data/ck/src.json').read_text())}
    fiches_ssp = load_ssp(root) or {}
    ssp_prototypes = [s[0] for s in ssps if prototype_ready(fiches_ssp.get(s[0], {}))]
    ssp_revues = [c for c in ssp_prototypes
                  if relecture_prototype(ledger.get('ssp', {}).get(c), fiches_ssp[c], root, sources)]
    prev = json.loads((root/'data/ck/prev.json').read_text()); monos = {}; duplicates = []
    for path in sorted((root/'data/ck/mono').glob('*.json')):
        for key, value in json.loads(path.read_text()).items():
            if key in monos: duplicates.append(key)
            monos[key] = value
    occurrences=[]; seen=set(); mono_metrics={}
    for task in tasks:
        key = task['key']; diagnostic = mid(task['diagnostic']); mono = monos.get(diagnostic, {})
        structure = isinstance(mono, dict) and all(texte(mono.get(k)) for k in REQ) and mid(mono.get('n','')) == diagnostic
        reserves = [k for k,v in mono.items() if k not in ('n','src','lu') and isinstance(v,str) and re.search(r'à\s+vérifier',v,re.I)] if isinstance(mono,dict) else []
        mono_read = structure and attestation(ledger.get('monographies',{}).get(diagnostic),mono,root,sources)
        raw_items = prev.get(task['ssp'],{}).get('items',[])
        items = [v for v in raw_items if type(v.get('i')) is int and v['i']==task['i']]
        item = items[0] if len(items)==1 else {}
        published = valid_published(item,task,sources,date.today().isoformat())
        prev_read = published and attestation(ledger.get('prevalences',{}).get(key),item,root,sources,task['fingerprint'])
        unique = key not in seen; seen.add(key)
        mr = ledger.get('monographies',{}).get(diagnostic,{})
        pr = ledger.get('prevalences',{}).get(key,{})
        ready = bool(unique and diagnostic not in duplicates and structure and mono_read and not reserves and published and prev_read
                     and mr.get('reserves_levees') is True and pr.get('reserves_levees') is True
                     and pr.get('applicable_au_dd_dans_ce_cadre') is True
                     and pr.get('population_cible') == task['title_ssp'])
        prototype = isinstance(mono,dict) and structure and prototype_ready(mono)
        prototype_read = prototype and relecture_prototype(mr, mono, root, sources)
        row = dict(task,diagnostic_id=diagnostic,mono_structure=bool(structure),mono_relecture=bool(mono_read),mono_reserves=reserves,
                   prototype_structure=bool(prototype),prototype_relecture=bool(prototype_read),
                   prevalence_publiee=bool(published),prevalence_relecture=bool(prev_read),couple_documente=ready)
        occurrences.append(row); mono_metrics[diagnostic]={'structure':bool(structure),'relecture':bool(mono_read),'reserves':bool(reserves),
                                                         'prototype_structure':bool(prototype),'prototype_relecture':bool(prototype_read)}
    empty=[s[0] for s in ssps if not any(t['ssp']==s[0] for t in tasks)]
    total=len(occurrences); paired=sum(t['couple_documente'] for t in occurrences)
    mono_total=len(mono_metrics)
    metrics={'occurrences':total,'diagnostics_uniques':mono_total,'monographies_structure':sum(m['structure'] for m in mono_metrics.values()),
             'prototype_structure':sum(m['prototype_structure'] for m in mono_metrics.values()),
             'prototype_relecture':sum(m['prototype_relecture'] for m in mono_metrics.values()),
             'monographies_relues':sum(m['relecture'] for m in mono_metrics.values()),'monographies_avec_reserves':sum(m['reserves'] for m in mono_metrics.values()),
             'prevalences_publiees':sum(t['prevalence_publiee'] for t in occurrences),'prevalences_relues':sum(t['prevalence_relecture'] for t in occurrences),
             'couples_documentes':paired,'ssp_sans_dd':empty,'doublons_monographies':duplicates,
             'maturite_documentaire_complete':bool(total and paired==total and not empty and not duplicates and len(seen)==total)}
    metrics.update(ssp_total=len(ssps),ssp_prototype_structure=len(ssp_prototypes),ssp_prototype_relecture=len(ssp_revues))
    metrics.update(chronologie_structures=metrics['prototype_structure'],chronologie_relectures=metrics['prototype_relecture'],
                   ssp_chronologie_structures=len(ssp_prototypes),ssp_chronologie_relectures=len(ssp_revues))
    ordered=sorted(occurrences,key=lambda t:(t['ssp']!=config['ssp_prioritaire'],))
    next_mono=[]; selected=set()
    for t in ordered:
        if not t['mono_structure'] and t['diagnostic_id'] not in selected:
            next_mono.append({'diagnostic_id':t['diagnostic_id'],'diagnostic':t['diagnostic'],'ssp':t['ssp']});selected.add(t['diagnostic_id'])
        if len(next_mono)>=config['taille_lot_monographies']: break
    maturation=[]; already=set()
    for t in ordered:
        if t['mono_structure'] and (not t['mono_relecture'] or t['mono_reserves']
                or ledger.get('monographies',{}).get(t['diagnostic_id'],{}).get('reserves_levees') is not True) and t['diagnostic_id'] not in already:
            maturation.append({'diagnostic_id':t['diagnostic_id'],'diagnostic':t['diagnostic'],'ssp':t['ssp'],
                               'action':'compléter les réserves ou inscrire la relecture actuelle'})
            already.add(t['diagnostic_id'])
    if not next_mono:
        next_mono=maturation[:config['taille_lot_monographies']]
        selected={t['diagnostic_id'] for t in next_mono}
    crisis = config.get('mission_exclusive') == 'infobulles_prototype6'
    if crisis:
        metrics['maturite_documentaire_complete'] = bool(metrics['maturite_documentaire_complete']
            and metrics['prototype_relecture'] == mono_total)
        # An existing legacy monograph is still due. Preserve catalogue order
        # within G1 and then the remaining SSP; do not skip to missing G10 work.
        maturation=[]; selected=set()
        for t in ordered:
            if t['diagnostic_id'] in selected or t['prototype_relecture']:
                continue
            maturation.append({'diagnostic_id':t['diagnostic_id'],'diagnostic':t['diagnostic'],'ssp':t['ssp'],
                               'action':('relecture documentaire du prototype actuel' if t['prototype_structure']
                                         else 'réviser selon les six rubriques, puis contrelecture indépendante')})
            selected.add(t['diagnostic_id'])
        next_mono=maturation[:config['taille_lot_monographies']]
        selected={t['diagnostic_id'] for t in next_mono}
    priority=[t['key'] for t in ordered if t['diagnostic_id'] in selected and not t['prevalence_relecture']]
    priority += [t['key'] for t in ordered if t['ssp']==config['ssp_prioritaire'] and not t['prevalence_relecture'] and t['key'] not in priority]
    from tools.prevalences.relance_agent import review_completed
    queue=0; stale=0; anomalies=[]
    if states_provided:
        anomalies += [f'État absent : {c}' for c in 'GSFO' if c not in states]
    for category,state in states.items():
        current={t['key']:t for t in tasks if t['categorie']==category}
        if not isinstance(state,dict) or not isinstance(state.get('tasks'),dict):
            anomalies.append(f'État invalide : {category}');continue
        for key,row in state['tasks'].items():
            if not isinstance(row,dict) or not isinstance(row.get('candidates',[]),list):
                anomalies.append(f'Tâche invalide : {category}/{key}');continue
            if key not in current or row.get('fingerprint')!=current[key]['fingerprint']: stale+=1;continue
            for c in row.get('candidates',[]):
                if not isinstance(c,dict):anomalies.append(f'Candidat invalide : {category}/{key}');continue
                queue+=c.get('statut')=='candidat_a_relire' and not review_completed(c)
    if anomalies:metrics['maturite_documentaire_complete']=False
    plan={'etape_prioritaire':9,'etape_associee':8,'prochain_lot9':next_mono,'priorites8':priority,'file_maturation9':maturation,
          'file_maturation8':[t['key'] for t in ordered if t['prevalence_publiee'] and not t['prevalence_relecture']],
          'file_relecture':queue,'etats_obsoletes':stale,'anomalies_etat':anomalies,'etat_recherche_fiable':bool(states_provided and not anomalies),
          'limite_recherche':config['lot_recherche_file_chargee'] if queue>=config['seuil_file_relecture'] else config['lot_recherche_normal'],
          'intervalle_recherche_minutes':config['intervalle_recherche_minutes']}
    if crisis:
        plan.update(mission_exclusive='infobulles_prototype6',recherche_automatique_suspendue=True,
                    perimetre_monographies='diagnostics_differentiels',prochaines_fiches_ssp=[],
                    action_recherche='rechercher manuellement les sources nécessaires au lot courant uniquement')
    return {'version':1,'protocole':{'version':2,'rubriques':6,'chronologie_obligatoire':True},'maj':datetime.now(timezone.utc).isoformat(timespec='seconds'),'mesure':metrics,'plan':plan,'occurrences':occurrences,
            'reserve':'Couverture structurelle et relecture documentaire distinctes. Registre lié aux empreintes initialisé sur le dernier lot ; les audits historiques ne sont pas tous migrés. Aucun accord clinique humain ni achèvement déduit d’un chiffre arrondi.'}

def page(report):
    m=report['mesure'];p=report['plan'];esc=lambda v:html.escape(str(v))
    rows=[('Monographies structurées',m['monographies_structure'],m['diagnostics_uniques']),('Relectures monographiques inscrites au registre couplé',m['monographies_relues'],m['diagnostics_uniques']),
          ('Prévalences publiées avec source',m['prevalences_publiees'],m['occurrences']),('Relectures de prévalences inscrites au registre couplé',m['prevalences_relues'],m['occurrences']),('Occurrences documentées sur les deux volets',m['couples_documentes'],m['occurrences'])]
    if p.get('mission_exclusive') == 'infobulles_prototype6':
        rows=[('Prototypes six rubriques avec chronologies (hors validation clinique)',m['prototype_structure'],m['diagnostics_uniques']),
              ('Prototypes avec relecture documentaire actuelle',m['prototype_relecture'],m['diagnostics_uniques'])]
    bars=''.join(f'<tr><td>{esc(label)}</td><td><progress value="{n}" max="{max(1,total)}"></progress> {n}/{total}</td></tr>' for label,n,total in rows)
    todo=''.join(f'<li>{esc(x["ssp"])} : {esc(x["diagnostic"])}</li>' for x in p['prochain_lot9'])
    recherche=(esc(p['action_recherche'])+'. Recherches automatiques transversales suspendues.'
               if p.get('recherche_automatique_suspendue') else
               'File documentaire : '+str(p['file_relecture'])+' extraits. Recherche régulée : '+str(p['limite_recherche'])+' diagnostic(s) par catégorie, au plus toutes les '+str(p['intervalle_recherche_minutes'])+' minutes.')
    titre='Diagnostics différentiels · prototype six rubriques' if p.get('mission_exclusive') == 'infobulles_prototype6' else 'Étapes 8 et 9 · suivi commun'
    return '<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>'+titre+'</title><style>body{font:18px system-ui;max-width:960px;margin:auto;padding:24px;color:#182c40;background:#f5f7fa}td{padding:12px}progress{max-width:40vw}a{color:#0057a3}</style><h1>'+titre+'</h1><p>'+esc(report['maj'])+'</p><table>'+bars+'</table><p>'+esc(report['reserve'])+'</p><h2>Lot prioritaire</h2><ol>'+todo+'</ol><p>'+recherche+'</p><p>SSP sans différentiel : '+str(len(m['ssp_sans_dd']))+'. Leur absence empêche une maturité globale.</p><p><a href="prevalences.html">Prévalences</a> · <a href="prevalences-erreurs.pdf">Rapport des erreurs</a> · <a href="coordination.json">Détail vérifiable</a></p></html>'

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--state-dir',type=Path,default=DEFAULT_STATE);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    states={c:json.loads((args.state_dir/f'{c}.json').read_text()) for c in 'GSFO' if (args.state_dir/f'{c}.json').exists()}
    ledger_path=Path(__file__).with_name('relectures.json');ledger=json.loads(ledger_path.read_text()) if ledger_path.exists() else {}
    report=calculer(states=states,ledger=ledger);args.output.mkdir(parents=True,exist_ok=True)
    atomic_json(args.output/'coordination.json',report);atomic_json(args.output/'priorites.json',report['plan']);(args.output/'coordination.html').write_text(page(report))
    print(json.dumps({'mesure':report['mesure'],'plan':report['plan']},ensure_ascii=False))
if __name__=='__main__':main()
