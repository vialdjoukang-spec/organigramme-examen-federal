#!/usr/bin/env python3
"""Relais GitHub → Codex cloud : contrôle120s, baux communs, réponse vérifiée, sans faux démarrage."""
import argparse
import datetime as dt
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import uuid

sys.path.insert(0, str(Path(__file__).resolve().parent))
import permanence as guard

CONFIG = 'tools/garde/codex_cloud_120.json'
BOT = 'chatgpt-codex-connector[bot]'
SETTINGS = 'https://chatgpt.com/codex/cloud/settings/environments'


class SharedStore(guard.Store):
    def read(self):
        state = super().read()
        if not isinstance(state, dict):
            raise ValueError('état partagé invalide')
        for field in ('agent', 'worker', 'demande'):
            if field not in state:
                continue
            lease = state[field]
            if (not isinstance(lease, dict) or not isinstance(lease.get('owner'), str)
                    or not lease['owner'] or type(lease.get('expires')) not in (int, float)
                    or not math.isfinite(lease['expires'])):
                raise ValueError('bail partagé invalide')
        cloud = state.get('codex_cloud', {})
        if not isinstance(cloud, dict):
            raise ValueError('état cloud invalide')
        for field in ('requested_at', 'reserved_at'):
            if field in cloud and (type(cloud[field]) not in (int, float)
                                   or not math.isfinite(cloud[field]) or cloud[field] < 0):
                raise ValueError('date cloud invalide')
        if 'request_id' in cloud and (type(cloud['request_id']) is not int or cloud['request_id'] < 1):
            raise ValueError('identifiant cloud invalide')
        return state


def api(path, body=None, human=False):
    env = dict(os.environ)
    if human:
        token = env.get('GH_TOKEN_CODEX')
        if not token:
            raise RuntimeError('jeton humain absent ; aucune notification de remplacement')
        env['GH_TOKEN'] = token
    cmd = ['gh', 'api', path]
    if body is not None:
        cmd += ['-X', 'POST', '--input', '-']
    result = subprocess.run(cmd, input=json.dumps(body) if body is not None else None,
                            env=env, capture_output=True, text=True, timeout=30)
    if result.returncode:
        raise RuntimeError('API GitHub indisponible ; état de livraison inconnu' if body else 'API GitHub indisponible')
    return json.loads(result.stdout)


def comments(pr):
    result = []
    # Pas de lecture limitée aux cent premiers commentaires d'un fil durable.
    for page in range(1, 6):
        rows = api(f'repos/{guard.REPO}/issues/{pr}/comments?per_page=100&page={page}')
        if not isinstance(rows, list):
            raise ValueError('commentaires invalides')
        result.extend(rows)
        if len(rows) < 100:
            return result
    raise RuntimeError('fil trop volumineux ; observation requise avant relance')


def timestamp(value):
    parsed = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('date sans fuseau')
    return parsed.timestamp()


def feedback(rows, cloud, cfg):
    """Un acquittement n'est jamais une preuve d'exécution ou une validation médicale."""
    requests = [c for c in rows if c.get('user', {}).get('login') == cfg['requester_login']
                and c.get('user', {}).get('type') == 'User'
                and '@codex' in c.get('body', '').lower()
                and '@codex review' not in c.get('body', '').lower()]
    latest = max(requests, key=lambda c: c['id'], default=None)
    # Réconciliation après crash/timeout du POST : la réservation n'est pas renvoyée aveuglément.
    if latest and latest['id'] >= cloud.get('request_id', 0):
        cloud.update(request_id=latest['id'], requested_at=timestamp(latest['created_at']),
                     request_url=latest.get('html_url'))
    if not cloud.get('request_id'):
        return
    replies = [c for c in rows if c.get('user', {}).get('login') == BOT
               and c.get('user', {}).get('type') == 'Bot'
               and c['id'] > cloud['request_id']
               and timestamp(c['created_at']) >= cloud['requested_at']]
    reply = max(replies, key=lambda c: c['id'], default=None)
    if reply:
        missing = 'create an environment for this repo' in reply.get('body', '').lower()
        cloud.update(reply_id=reply['id'], reply_url=reply.get('html_url'),
                     statut='environnement_cloud_manquant' if missing else 'reponse_connecteur_execution_non_prouvee')
        if missing:
            cloud['settings_url'] = SETTINGS
    cloud['execution_ia_prouvee'] = False


def decision(state, report, now, busy, cfg):
    plan = report.get('plan', {})
    mandate = plan.get('mandat')
    if mandate is not None:
        if (mandate.get('id') != 'modifications_1_ck_2_cs'
                or mandate.get('etape') not in ('ALPHA', 'BETTA', 'GAMMA', 'TERMINE')):
            return 'mission_modifiee_sans_relance'
        if mandate.get('anomalies'):
            return 'preuves_mandat_invalides_sans_relance'
        status = guard.policy(state, report, now, busy)
        if status == 'termine':
            return 'mandat_termine_preuves_verifiees'
        if status in ('occupe', 'progression'):
            return 'occupe_ou_progression'
        cloud = state.setdefault('codex_cloud', {})
        last = max(cloud.get('requested_at', 0), cloud.get('reserved_at', 0))
        if last and now - last < cfg['request_cooldown_seconds']:
            return cloud.get('statut', 'demande_en_attente_execution_non_prouvee')
        if not mandate.get('prochains_lots') and not mandate.get('audit_phase_requis'):
            return 'mandat_sans_lot_reprise_a_verifier'
        return 'demander_reprise'
    if not (plan.get('priorite_cours_ssp') is True
            and plan.get('diagnostics_differentiels_suspendus') is True
            and plan.get('mission_exclusive') == guard.MISSION):
        return 'mission_modifiee_sans_relance'
    if plan.get('anomalies_cours'):
        return 'preuves_cours_invalides_sans_relance'
    if guard.policy(state, report, now, busy) in ('occupe', 'progression'):
        return 'occupe_ou_progression'
    cloud = state.setdefault('codex_cloud', {})
    # Temporisation persistante distincte des passages120s : évite les sessions cumulées.
    last = max(cloud.get('requested_at', 0), cloud.get('reserved_at', 0))
    if last and now - last < cfg['request_cooldown_seconds']:
        return cloud.get('statut', 'demande_en_attente_execution_non_prouvee')
    if not plan.get('prochain_lot9'):
        return 'jalon_cours_sans_lot_dd_toujours_suspendus'
    return 'demander_reprise'


def prompt(report, reservation):
    mandate = report['plan'].get('mandat')
    if mandate is not None:
        lots = '; '.join(', '.join(lot['unites']) +
                        (' [état ' + lot['statut'] + ' : ' + lot['travail_attendu'] + ']' if lot.get('statut') else '') +
                        (' [branche ' + lot['branche'] + ']' if lot.get('branche') else '')
                        for lot in mandate['prochains_lots'])
        action = 'Termine le contre-audit de phase.' if mandate['audit_phase_requis'] else 'Lots : ' + lots + '.'
        return (f'@codex Reprends le mandat autorisé de Vial : Modification_1_CK puis Modification_2_CS. '
                f'Étape {mandate["etape"]}, phase {mandate["phase"]}. {action} '
                'Lis AGENTS.md et docs/MODIFICATIONS-1-CK-2-CS.md puis exécute python3 tools/mandat/planifier.py. '
                'Reprends les branches réservées avant toute nouvelle rédaction ; compare leurs données à main. '
                'ALPHA : S puis F puis O, 14 parties de cours, deux SSP au plus par agent. '
                'BETTA seulement après ALPHA publiée et auditée : G puis S puis F puis O, '
                'un SSP à la fois, trois différentiels au plus par agent, six rubriques adaptées si nécessaire. '
                'GAMMA seulement après BETTA : organisation CS puis couleurs puis fond et forme. '
                'Rédacteurs GPT-6 raisonnement élevé, audits indépendants Astra ; noter les modèles réellement disponibles. '
                'Ne pas confondre lots proposés et agents lancés. Déclare le bail réel de 180 s du responsable avec '
                'permanence.py --github-state --agent <identifiant-unique> --lease-seconds 180 ; '
                'ne le renouvelle que pendant le travail réel. Sources CH/Europe et AIPS, '
                'corrections puis CI exacte verte, fusion protégée, vérification Pages, registre à jour. '
                'Aucun compteur de structure ne vaut audit ou publication. '
                f'<!-- relais-cloud-120:{reservation} -->')
    ssp = report['plan']['prochain_lot9'][0]['ssp']
    return (f'@codex Reprends le travail autorisé de Vial sur main, cours SSP uniquement : prochain {ssp}. '
            'Lis AGENTS.md, PROCHAINE_ACTION.md et docs/PROMPT-DIRECTEUR-ACADEMIQUE.md. '
            'Les diagnostics différentiels sont suspendus ; ne reprends pas le lot G2 DD. '
            'Préserve les14parties spécifiques, numérotation, sous-parties, concision, sources et clic sans survol. '
            'Reprends une PR de cours active avant de créer un autre lot. Le brouillon G2 est sur '
            'feat/forme-cours-g2, docs/preparations/cours-G2/ : le comparer à main actuel avant intégration. '
            'Déclare ton bail réel de 180 s avec permanence.py --github-state --agent <identifiant-unique> '
            '--lease-seconds 180, renouvelle pendant le travail réel seulement. '
            'Contre-audit indépendant, CI exacte verte, fusion protégée, vérification Pages puis lot suivant. '
            'Un commentaire ou un compteur ne prouve aucune validation médicale. '
            f'<!-- relais-cloud-120:{reservation} -->')


def tick(store, owner, report, rows, cfg, now, busy, wall=time.time, allowed=lambda:True):
    state = store.read()
    if state.get('worker', {}).get('owner') != owner or not guard.live(state['worker'], now):
        raise RuntimeError('bail de veille perdu')
    cloud = state.setdefault('codex_cloud', {})
    feedback(rows, cloud, cfg)
    action = decision(state, report, now, busy, cfg)
    cloud.update(dernier_controle=now, action=action, interval_seconds=120)
    if not allowed():
        return 'arrete_avant_reservation'
    if action == 'demander_reprise':
        cloud.update(reserved_at=now, reservation=uuid.uuid4().hex,
                     statut='livraison_en_attente_non_prouvee', execution_ia_prouvee=False)
        state['demande'] = {'owner':owner, 'expires':now + cfg['request_cooldown_seconds'],
                            'statut':'demande_non_execution_prouvee'}
    # Réserver avant POST ; un conflit interdit tout envoi.
    store.write(state)
    if action == 'demander_reprise':
        identity = api('user', human=True)
        if identity.get('type') != 'User' or identity.get('login') != cfg['requester_login']:
            raise RuntimeError('identité humaine autorisée non confirmée ; aucune notification')
        # Relire après les accès réseau pour préserver un agent arrivé entre-temps.
        current = store.read()
        if (not allowed()
                or current.get('codex_cloud', {}).get('reservation') != cloud['reservation']
                or current.get('worker', {}).get('owner') != owner
                or not guard.live(current.get('worker'), wall())
                or guard.live(current.get('agent'), wall())
                or (guard.live(current.get('demande'), wall()) and current['demande'].get('owner') != owner)):
            return 'reprise_deja_prise_en_charge'
        sent = api(f"repos/{guard.REPO}/issues/{cfg['pilot_pr']}/comments",
                   {'body':prompt(report, cloud['reservation'])}, human=True)
        # Ne jamais écraser l'acquittement éventuel de l'agent ou un concurrent.
        current = store.read()
        c = current.setdefault('codex_cloud', {})
        if c.get('reservation') != cloud['reservation']:
            raise RuntimeError('réservation remplacée après envoi ; livraison à réconcilier')
        c.update(request_id=sent['id'], requested_at=timestamp(sent['created_at']),
                 request_url=sent.get('html_url'), statut='demande_transmise_execution_non_prouvee')
        store.write(current)
    return action


def slots(window, clock=time.monotonic, sleeper=time.sleep, stop=lambda: False):
    start = clock()
    for index in range(window // 120 + 1):
        due = start + index * 120
        while clock() < due:
            if stop():
                return
            sleeper(min(25, due-clock()))
        if stop():
            return
        # Si un passage est trop lent, sauter les échéances périmées, pas de rafale.
        if index and clock() - due >= 120:
            continue
        yield index


def worker(args):
    owner = 'cloud120-' + uuid.uuid4().hex
    store = SharedStore(args.state_dir, remote=True)
    deadline = time.monotonic() + args.window
    def allowed():
        return not (args.state_dir/'STOP').exists() and (args.window == 0 or time.monotonic() < deadline)
    with guard.lock(args.state_dir):
        try:
            for index in slots(args.window, stop=lambda:(args.state_dir/'STOP').exists()):
                root = None
                try:
                    root = guard.snapshot(args.state_dir, True)
                    cfg = json.loads((root/CONFIG).read_text())
                    if cfg.get('enabled') is not True:
                        guard.log('cloud120_arrete_configuration'); return
                    if cfg.get('interval_seconds') != 120 or cfg.get('request_cooldown_seconds', 0) < 1800:
                        raise ValueError('configuration de cadence invalide')
                    guard.claim(store, owner, time.time(), 180)
                    output = root/'.etat_local/coordination'
                    output.mkdir(parents=True, exist_ok=True)
                    report = guard.report_for(root, output)
                    rows = comments(cfg['pilot_pr'])
                    # Inconnu => exception sans notification ; pas de faux « libre ».
                    busy = guard.busy_now()
                    action = tick(store, owner, report, rows, cfg, time.time(), busy, allowed=allowed)
                    guard.log('cloud120_passage', numero=index, action=action, execution_ia_prouvee=False)
                finally:
                    if root is not None:
                        shutil.rmtree(root, ignore_errors=True)
            guard.log('cloud120_fenetre_terminee', tache_terminee=False)
        finally:
            guard.release(store, owner)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state-dir', type=Path, default=guard.ROOT/'.etat_local/cloud120')
    parser.add_argument('--window', type=int, default=1200)
    args = parser.parse_args()
    if not 0 <= args.window <= 1200:
        parser.error('fenêtre attendue entre0et1200secondes')
    try:
        worker(args)
    except (RuntimeError, ValueError, KeyError, TypeError, OSError, subprocess.SubprocessError) as error:
        guard.log('cloud120_interrompu', type=type(error).__name__, execution_ia_prouvee=False,
                  detail='voir les baux et la configuration ; aucun secret journalisé')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
