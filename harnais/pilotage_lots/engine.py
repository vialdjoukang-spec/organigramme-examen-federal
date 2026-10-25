"""Portes déterministes V8. Ne rédige, n'audite et ne relance aucune IA."""
from copy import deepcopy
from datetime import datetime, timezone, timedelta
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import PurePosixPath
import json
import math
import re

ROLES = {'medical', 'linguistique'}
KEYS = ('A', 'B1', 'B2', 'B3', 'B4')
CAMPAIGN = 'inverse-226-001-v8'
LEDGER_PATH = 'harnais/pilotage_lots/etat.json'
CONTROL_BRANCH = 'pilotage/lots-inverses-v8'

def digest(data):
    return sha256(data).hexdigest()

def number(value):
    if not isinstance(value, str) or not re.fullmatch(r'LOT_\d{3}', value):
        raise ValueError('Identifiant de lot invalide')
    n = int(value[4:])
    if not 1 <= n <= 248:
        raise ValueError('Lot hors PROFILES')
    return n

def instant(value):
    if not isinstance(value, str):
        raise ValueError('Date non textuelle')
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('Date sans fuseau')
    return result

def validate_state(state):
    if not isinstance(state, dict) or type(state.get('schema_version')) is not int or state['schema_version'] != 1:
        raise ValueError('Schéma du registre invalide')
    if state.get('campaign') != CAMPAIGN or state.get('start') != 226 or state.get('end') != 1:
        raise ValueError('Périmètre de campagne invalide')
    if state.get('status') not in {'active', 'paused', 'quota_exhausted', 'finished'}:
        raise ValueError('État de campagne invalide')
    if type(state.get('stop_requested')) is not bool or type(state.get('revision')) is not int or state['revision'] < 0:
        raise ValueError('Arrêt ou révision invalide')
    jobs, protected = state.get('jobs'), state.get('protected_lots')
    if not isinstance(jobs, list) or not isinstance(protected, list):
        raise ValueError('Affectations ou réservations absentes')
    reserved = {number(x) for x in protected}
    seen, workers = set(), set()
    for job in jobs:
        n = number(job['lot'])
        if n > 226 or n in seen or n in reserved:
            raise ValueError('Lot dupliqué, réservé ou hors vague')
        seen.add(n)
        worker = job.get('worker')
        if not isinstance(worker, str) or not worker:
            raise ValueError('Responsable absent')
        if job.get('state') not in {'draft', 'review', 'blocked', 'completed'}:
            raise ValueError('État de lot invalide')
        if job['state'] != 'completed':
            if worker in workers:
                raise ValueError('Un agent ne peut porter deux lots actifs')
            workers.add(worker)
        if not isinstance(job.get('writers'), list) or worker not in job['writers'] or any(not isinstance(x, str) or not x for x in job['writers']):
            raise ValueError('Auteurs réels non déclarés')
        if job['state']=='completed' and not re.fullmatch('[0-9a-f]{40}',job.get('validated_head','')):
            raise ValueError('Clôture sans version vérifiée')
        if not isinstance(job.get('branch'), str) or not job['branch'].startswith(f'cursor/lot-{n:03d}-'):
            raise ValueError('Branche non propre au lot')
    return state

def expected_files(lot):
    number(lot)
    names = [f'{lot}_Appel_A_V8_Plan_et_Liste.html']
    names += [f'{lot}_Appel_B_V8_Partie_{i}_DX.{a}_a_DX.{b}.html'
              for i, (a, b) in enumerate(((1,2),(3,5),(6,7),(8,10)), 1)]
    return dict(zip(KEYS, names))

def own_path(lot, path):
    if not isinstance(path, str):
        raise ValueError('Chemin de preuve non textuel')
    p = PurePosixPath(path)
    directory = PurePosixPath('lot en cours de production') / lot
    if p.is_absolute() or '..' in p.parts or not p.is_relative_to(directory) or p == directory:
        raise ValueError('Preuve hors du lot')
    return str(p)

class Shape(HTMLParser):
    def __init__(self):
        super().__init__(); self.forbidden = []; self.ids = []; self.sections = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {'script', 'img', 'link', 'iframe', 'object', 'embed'} or 'title' in attrs:
            self.forbidden.append(tag)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
            if tag == 'section': self.sections.append(attrs['id'])

def technical(data, key):
    text = data.decode('utf-8'); parser = Shape(); parser.feed(text)
    reasons = []
    if not 90_000 <= len(data) <= 200_000: reasons.append('Taille hors90–200Ko')
    if not text.lstrip().lower().startswith('<!doctype html>') or not re.search(r'</html>\s*<!-- FIN_FICHIER [^>]+ -->\s*$', text):
        reasons.append('HTML5 complet ou marque de fin absent')
    if parser.forbidden or len(parser.ids) != len(set(parser.ids)): reasons.append('Élément interdit ou identifiant dupliqué')
    if max(map(len, text.splitlines()), default=0) > 3000: reasons.append('Ligne supérieure à3000caractères')
    if key != 'A':
        wanted = {'B1':(1,2),'B2':(3,4,5),'B3':(6,7),'B4':(8,9,10)}[key]
        dx_sections=[x for x in parser.sections if re.fullmatch(r'dx\d+-p\d+',x)]
        if len(dx_sections)!=14*len(wanted): reasons.append('Cadence ou nombre de points incorrect')
        for dx in wanted:
            if not all(f'dx{dx}-p{n}' in parser.sections for n in range(1,15)):
                reasons.append(f'DX{dx}:14points non retrouvés')
    return reasons

def attestation(api, head, lot, record, basis, writers, role, now):
    if not isinstance(record, dict): raise ValueError('Attestation absente')
    if record.get('file_sha256') != basis: raise ValueError('Attestation sur une autre version')
    if role in ROLES:
        actor = record.get('auditor_id')
        if not isinstance(actor, str) or not actor or actor in writers:
            raise ValueError('Audit non indépendant de ses auteurs')
        score = record.get('score')
        if type(score) not in (int,float) or not math.isfinite(score) or not 90 <= score <= 100:
            raise ValueError('Score inférieur90 ou invalide')
        if record.get('role') != role or type(record.get('critical_count')) is not int or record['critical_count'] != 0 or record.get('full_read') is not True:
            raise ValueError('Audit incomplet ou critique restant')
        if role == 'medical' and record.get('critical_sources_read') is not True:
            raise ValueError('Sources critiques non attestées lues')
    elif role == 'visual':
        if record.get('width_px') != 390 or record.get('performed') is not True or record.get('authorized_environment') is not True:
            raise ValueError('Contrôle visuel390 autorisé non attesté')
    elif role == 'delivery':
        if record.get('verified') is not True or record.get('destination') != 'Drive Finaux':
            raise ValueError('Livraison finale non vérifiée')
        if not isinstance(record.get('remote_file_id'), str) or not record['remote_file_id']:
            raise ValueError('Reçu de livraison absent')
    checked = instant(record.get('checked_at'))
    if checked > now + timedelta(seconds=120): raise ValueError('Attestation future')
    path = own_path(lot, record.get('report_path'))
    raw = api.file(path, head)
    if not re.fullmatch('[0-9a-f]{64}', record.get('report_sha256','')) or digest(raw) != record['report_sha256']:
        raise ValueError('Rapport absent ou empreinte différente')

def evaluate_lot(api, job, now):
    lot = job['lot']; directory = 'lot en cours de production/' + lot
    head = api.head(job['branch'])  # Toutes les lectures suivantes utilisent cette version fixe.
    result = {'lot':lot, 'branch':job['branch'], 'head':head, 'complete':False, 'files':{}, 'next_action':None}
    actions = []
    entries = {}
    try:
        package = json.loads(api.file(directory+'/VALIDATION_V8.json', head))
        if not isinstance(package, dict) or package.get('schema_version') != 1 or not isinstance(package.get('files'), dict):
            raise ValueError('Dossier de validation mal structuré')
    except FileNotFoundError:
        package = {'files':{}}
    except (TypeError, ValueError) as exc:
        result['next_action'] = {'action':'repair_validation_record','reason':str(exc)}
        return result
    for key, name in expected_files(lot).items():
        path = directory + '/' + name
        try: raw = api.file(path, head)
        except FileNotFoundError:
            result['files'][key] = {'state':'missing'}
            actions.append({'action':'write','file':key})
            continue
        basis = digest(raw); problems = technical(raw, key)
        result['files'][key] = {'sha256':basis,'bytes':len(raw),'technical_reserves':problems,'gates':{}}
        if problems:
            actions.append({'action':'repair_html','file':key,'reason':'; '.join(problems)})
            continue
        entry = package['files'].get(key, {})
        if not isinstance(entry, dict): entry = {}
        entries[key] = entry
        for role in ('medical','linguistique','visual'):
            try:
                attestation(api, head, lot, entry.get(role), basis, job['writers'], role, now)
                result['files'][key]['gates'][role] = True
            except (ValueError,TypeError,KeyError,FileNotFoundError) as exc:
                result['files'][key]['gates'][role] = False
                # Les audits et corrections restent utiles avant une QA externe indisponible.
                actions.append({'action':{'medical':'audit_or_correct','linguistique':'audit_or_correct','visual':'await_authorized_visual_proof'}[role], 'file':key,'role':role,'reason':str(exc)})
    prerequisites = all(x.get('gates') and len(x['gates'])==3 and all(x['gates'].values()) for x in result['files'].values())
    if prerequisites:
        latest = max(instant(entries[k][r]['checked_at']) for k in KEYS for r in ('medical','linguistique','visual'))
        for key in KEYS:
            record=entries[key].get('delivery')
            try:
                attestation(api,head,lot,record,result['files'][key]['sha256'],job['writers'],'delivery',now)
                if instant(record['checked_at']) < latest: raise ValueError('Livraison antérieure aux validations complètes')
                result['files'][key]['gates']['delivery']=True
            except (ValueError,TypeError,KeyError,FileNotFoundError) as exc:
                result['files'][key]['gates']['delivery']=False
                actions.append({'action':'verify_final_delivery','file':key,'reason':str(exc)})
    priorities={'write':0,'repair_html':1,'audit_or_correct':2,'await_authorized_visual_proof':3,'verify_final_delivery':4}
    result['next_action']=min(actions,key=lambda x:priorities[x['action']]) if actions else None
    result['complete'] = prerequisites and all(x['gates'].get('delivery') is True for x in result['files'].values())
    return result

def acquire(state, owner, token, now):
    validate_state(state)
    if state['stop_requested'] or state['status'] != 'active': raise ValueError('Campagne arrêtée ou quota bloquant')
    if not isinstance(owner,str) or not owner or not isinstance(token,str) or len(token)<16: raise ValueError('Bail sans identité réelle')
    old = state.get('lease')
    if old is not None:
        if not isinstance(old,dict): raise ValueError('Bail mal structuré')
        expiry = instant(old['expires_at'])
        if expiry > now and (old.get('owner'),old.get('token')) != (owner,token):
            raise ValueError('Une autre session porte le bail')
        if expiry > now+timedelta(minutes=20): raise ValueError('Bail anormalement prolongé')
    result=deepcopy(state);result['revision']+=1
    result['lease']={'owner':owner,'token':token,'expires_at':(now+timedelta(minutes=20)).isoformat()}
    return result  # À publier par commit enfant + update_ref(expected_sha), jamais force.

def advance(state, owner, token, worker, evaluations, reservations, now):
    result=acquire(state,owner,token,now)
    if not isinstance(reservations,dict) or reservations.get('complete') is not True or not isinstance(reservations.get('lots'),list):
        raise ValueError('Inventaire distant incomplet: aucune nouvelle affectation')
    elapsed=(now-instant(reservations['checked_at'])).total_seconds()
    if not -120 <= elapsed <= 300: raise ValueError('Inventaire des réservations périmé')
    current=[j for j in result['jobs'] if j['worker']==worker and j['state']!='completed']
    if len(current)!=1: raise ValueError('Responsable sans lot courant unique')
    job=current[0]; evaluation=evaluations.get(job['lot'])
    if not evaluation or evaluation.get('complete') is not True or evaluation.get('lot')!=job['lot'] or evaluation.get('branch')!=job['branch'] or not re.fullmatch('[0-9a-f]{40}',evaluation.get('head','')):
        raise ValueError('Lot courant non complet: aucun passage au suivant')
    job['state']='completed';job['validated_head']=evaluation['head']
    used={number(j['lot']) for j in result['jobs']} | {number(x) for x in result['protected_lots']} | {number(x) for x in reservations['lots']}
    candidate=next((n for n in range(226,0,-1) if n not in used),None)
    if candidate is not None:
        result['jobs'].append({'lot':f'LOT_{candidate:03d}','worker':worker,'writers':[worker],
          'branch':f'cursor/lot-{candidate:03d}-v8-auto','state':'draft','pr':None})
    elif all(j['state']=='completed' for j in result['jobs']):
        # Des lots réservés à d'autres vagues ne sont jamais déclarés terminés par cette campagne.
        result['status']='paused';result['pause_reason']='Aucun lot libre; réservations conservées.'
    validate_state(result)
    return result
