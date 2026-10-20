"""Le mandat n'avance pas par un compteur, un lot proposé ou une preuve périmée."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.mandat import planifier as planner
from tools.garde import codex_cloud_120 as relay


class MandatTests(unittest.TestCase):
    def fixture(self, root):
        (root/'data/ck/mono').mkdir(parents=True)
        (root/'data/ck/mono/a.json').write_text('{}')
        ssps = [[c, c, c.split('.')[0]] for c in ('G1','S1.1','S1.2','S1.3','S2.1','F1.1','O1.1')]
        tip = {c: {'c':['Contenu ' + c] * 14} for c, _, _ in ssps}
        (root/'app_v2.html').write_text('\nconst SSP=' + json.dumps(ssps) + ';\nconst TIP=' + json.dumps(tip) + ';\n')
        occurrences = [dict(ssp=c, diagnostic_id=planner.mid(c+' DD '+str(i)), diagnostic=c+' DD '+str(i),
                            prototype_relecture=False) for c, _, _ in ssps for i in range(5 if c == 'G1' else 1)]
        with (root/'app_v2.html').open('a') as f:
            f.write('const NOT=' + json.dumps({c:[[x['diagnostic'] for x in occurrences if x['ssp']==c]] for c,_,_ in ssps})+';\n')
        (root/'data/ck/mono/a.json').write_text(json.dumps({x['diagnostic_id']:{'n':x['diagnostic']} for x in occurrences}))
        registry = dict(version=1, reservations=[], publications={}, audits_phases={}, applicabilite={}, gamma={})
        contract = json.loads((planner.ROOT/'tools/mandat/contrat.json').read_text())
        courses = dict(ssp_restant=list(tip), anomalies=[])
        return contract, registry, {'occurrences': occurrences}, courses

    def run_plan(self, root, values):
        contract, registry, coordination, courses = values
        with patch.object(planner, 'bilan', return_value=courses), patch.object(planner, 'audit_cours', return_value=True):
            return planner.construire(root, coordination, contract, registry)

    def test_initial_dispatch_is_s_only_and_two_courses_max(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root);r=self.run_plan(root,v)
            self.assertEqual((r['etape'],r['phase']),('ALPHA','S'))
            self.assertEqual([x['unites'] for x in r['prochains_lots']], [['S1.1','S1.2'],['S1.3','S2.1']])
            self.assertFalse(r['complet']);self.assertEqual(r['mesure']['alpha_publies'],0)

    def test_reservations_are_resumed_without_duplicate_dispatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root)
            v[1]['reservations']=[dict(etape='ALPHA',phase='S',agent='a',modele='gpt-6-sol',raisonnement='high',statut='en_audit',unites=['S1.1','S1.2'],branche='b')]
            r=self.run_plan(root,v)
            self.assertEqual(r['prochains_lots'][0]['action'],'reprendre_lot_reserve')
            self.assertEqual(len(r['prochains_lots']),1);self.assertFalse(r['anomalies'])
            v[1]['reservations'].append(dict(v[1]['reservations'][0],agent='b'))
            self.assertTrue(self.run_plan(root,v)['anomalies'])

    def test_wrong_phase_unknown_or_oversized_reservations_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root)
            for units, phase in [(['S1.1','S1.2','S1.3'],'S'),(['F1.1'],'F'),(['S999'],'S')]:
                v[1]['reservations']=[dict(etape='ALPHA',phase=phase,agent='a',statut='en_redaction',unites=units)]
                self.assertTrue(self.run_plan(root,v)['anomalies'])

    def test_publication_proof_requires_real_integrated_commit_and_file_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);self.fixture(root)
            def git(*args):return planner.git(root,*args).decode().strip()
            git('init','-q');git('config','user.email','audit@example.invalid');git('config','user.name','audit')
            git('add','.');git('commit','-qm','fixture');commit=git('rev-parse','HEAD')
            git('update-ref','refs/remotes/origin/main',commit)
            path=root/'proof.json';key='ALPHA:S1.1';digest=planner.empreinte(['Contenu S1.1']*14)
            sha=hashlib.sha256((root/'app_v2.html').read_bytes()).hexdigest()
            report=dict(statut='publication_verifiee',commit=commit,unites={key:digest},
                        verifie_le='2026-01-01T00:00:00Z',
                        workflow_pages='https://github.com/vialdjoukang-spec/organigramme-examen-federal/actions/runs/123',
                        fichiers=[dict(path='app_v2.html',url=planner.PAGES+'app_v2.html',http=200,
                                       sha256_attendu=sha,sha256_public=sha)])
            def write():
                path.write_text(json.dumps(report));return dict(rapport='proof.json',rapport_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
            self.assertTrue(planner.publie(root,write(),key,digest))
            original=copy.deepcopy(report)
            for mutation in ('commit','hash','url','unite','date','path'):
                report=copy.deepcopy(original)
                if mutation=='commit':report['commit']='a'*40
                if mutation=='hash':report['fichiers'][0].update(sha256_attendu='c'*64,sha256_public='c'*64)
                if mutation=='url':report['fichiers'][0]['url']='https://other.invalid/app_v2.html'
                if mutation=='unite':report['unites'][key]='d'*64
                if mutation=='date':report['verifie_le']='2999-01-01T00:00:00Z'
                if mutation=='path':report['fichiers'][0]['path']='../app_v2.html'
                expected=report['unites'][key]
                self.assertFalse(planner.publie(root,write(),key,expected),mutation)
            report=original;record=write();path.write_text('{}')
            self.assertFalse(planner.publie(root,record,key,digest))
            self.assertFalse(planner.publie(root,{'rapport':'../outside','rapport_sha256':'a'},key,digest))
            git('checkout','-qb','unmerged');(root/'new').write_text('x');git('add','.');git('commit','-qm','unmerged')
            report['commit']=git('rev-parse','HEAD')
            self.assertFalse(planner.publie(root,write(),key,digest))

    def test_external_tip_publication_requires_verified_asset_and_matching_shard(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.fixture(root)
            app = (root/'app_v2.html').read_text()
            a,b = planner.span(app,'TIP'); tip=json.loads(app[a:b])
            (root/'data/tip').mkdir(parents=True)
            for code,item in tip.items():
                (root/'data/tip'/f'{code}.json').write_text(json.dumps(item))
            (root/'assets/config').mkdir(parents=True)
            from tools.tip_data import TAG, render
            asset=root/'assets/config/tip.js';asset.write_text(render(tip))
            (root/'app_v2.html').write_text(TAG+'\n<script>'+app[:a-len('\nconst TIP=')]+app[b+1:]+'</script>')
            def git(*args):return planner.git(root,*args).decode().strip()
            git('init','-q');git('config','user.email','audit@example.invalid');git('config','user.name','audit')
            git('add','.');git('commit','-qm','asset TIP');commit=git('rev-parse','HEAD')
            git('update-ref','refs/remotes/origin/main',commit)
            key='ALPHA:S1.1';digest=planner.empreinte(tip['S1.1']['c'])
            def file(path):
                sha=hashlib.sha256((root/path).read_bytes()).hexdigest()
                return dict(path=path,url=planner.PAGES+path,http=200,sha256_attendu=sha,sha256_public=sha)
            report=dict(statut='publication_verifiee',commit=commit,unites={key:digest},
                        verifie_le='2026-01-01T00:00:00Z',
                        workflow_pages='https://github.com/vialdjoukang-spec/organigramme-examen-federal/actions/runs/123',
                        fichiers=[file('app_v2.html')])
            proof=root/'proof.json'
            def record():
                proof.write_text(json.dumps(report))
                return dict(rapport='proof.json',rapport_sha256=hashlib.sha256(proof.read_bytes()).hexdigest())
            self.assertFalse(planner.publie(root,record(),key,digest))
            report['fichiers'].append(file('assets/config/tip.js'))
            self.assertTrue(planner.publie(root,record(),key,digest))
            report['fichiers'][-1]['sha256_public']='0'*64
            self.assertFalse(planner.publie(root,record(),key,digest))
            # Des empreintes publiques exactes ne rendent pas exécutable un HTML cassé.
            good_app = (root/'app_v2.html').read_text()
            original_shard = (root/'data/tip/S1.1.json').read_text()
            for mutation in ('late', 'duplicate', 'comment', 'async', 'shard', 'asset'):
                with self.subTest(mutation=mutation):
                    (root/'app_v2.html').write_text(good_app)
                    (root/'data/tip/S1.1.json').write_text(original_shard)
                    asset.write_text(render(tip))
                    if mutation == 'late':
                        (root/'app_v2.html').write_text(good_app.replace(TAG, '') + TAG)
                    if mutation == 'duplicate':
                        (root/'app_v2.html').write_text(good_app + '<script>let TIP = {};</script>')
                    if mutation == 'comment':
                        (root/'app_v2.html').write_text(good_app.replace(TAG, '<!--'+TAG+'-->'))
                    if mutation == 'async':
                        (root/'app_v2.html').write_text(good_app.replace('<script src=', '<script async src='))
                    if mutation == 'shard':
                        value=json.loads(original_shard);value['c'][0]='Divergence'
                        (root/'data/tip/S1.1.json').write_text(json.dumps(value))
                    if mutation == 'asset':
                        asset.write_text('const invalid = {};')
                    git('add','.');git('commit','-qm',mutation)
                    report['commit']=git('rev-parse','HEAD')
                    git('update-ref','refs/remotes/origin/main',report['commit'])
                    report['fichiers']=[file('app_v2.html'),file('assets/config/tip.js')]
                    self.assertFalse(planner.publie(root,record(),key,digest))

    def test_review_publication_and_phase_audit_are_distinct_gates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root)
            with patch.object(planner,'publie',return_value=True):
                self.assertEqual(self.run_plan(root,v)['restant_phase'],4)
                v[3]['ssp_restant']=[]
                r=self.run_plan(root,v);self.assertEqual(r['phase'],'S');self.assertTrue(r['audit_phase_requis'])
                with patch.object(planner,'audit_phase',side_effect=lambda root, record, scope: all(k.startswith('ALPHA:S') for k in scope)):
                    self.assertEqual(self.run_plan(root,v)['phase'],'F')

    def test_betta_publication_requires_compiled_payload_matching_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);self.fixture(root)
            data=json.loads((root/'data/ck/mono/a.json').read_text())
            diagnostic=next(iter(data));key='BETTA:'+diagnostic;digest=planner.empreinte(data[diagnostic])
            asset=root/'assets/mono/mono-a.js';asset.parent.mkdir(parents=True)
            def git(*args):return planner.git(root,*args).decode().strip()
            git('init','-q');git('config','user.email','audit@example.invalid');git('config','user.name','audit')
            def publish(payload):
                asset.write_text('window.CK_MONO_A='+json.dumps(payload)+';')
                git('add','.');git('commit','-qm','compiled fixture');commit=git('rev-parse','HEAD')
                git('update-ref','refs/remotes/origin/main',commit)
                sha=hashlib.sha256(asset.read_bytes()).hexdigest()
                report=dict(statut='publication_verifiee',commit=commit,unites={key:digest},verifie_le='2026-01-01T00:00:00Z',
                    workflow_pages='https://github.com/vialdjoukang-spec/organigramme-examen-federal/actions/runs/123',
                    fichiers=[dict(path='assets/mono/mono-a.js',url=planner.PAGES+'assets/mono/mono-a.js',http=200,sha256_attendu=sha,sha256_public=sha)])
                p=root/'proof.json';p.write_text(json.dumps(report))
                return dict(rapport='proof.json',rapport_sha256=hashlib.sha256(p.read_bytes()).hexdigest())
            self.assertTrue(planner.publie(root,publish(data),key,digest))
            stale=copy.deepcopy(data);stale[diagnostic]['n']='ancienne compilation'
            self.assertFalse(planner.publie(root,publish(stale),key,digest))

    def test_current_mandate_takes_precedence_in_porte(self):
        from tools import porte
        state=dict(etape_courante=0,mission_exclusive=dict(priorite_courante=dict(id=planner.ID)))
        with patch.object(porte,'critere',side_effect=AssertionError('legacy gate must not run')):
            order=porte.ordre(state)
        self.assertIn('python3 tools/mandat/planifier.py',order)
        self.assertIn('BETTA seulement après ALPHA publiée',order)
        self.assertIn('audit documentaire et publication vérifiée',order)

    def test_betta_starts_at_g_and_three_differentials_max_after_all_alpha(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root);v[3]['ssp_restant']=[]
            with (patch.object(planner,'publie',side_effect=lambda root,record,key,digest:key.startswith('ALPHA:')),
                  patch.object(planner,'audit_phase',side_effect=lambda root,record,scope:all(k.startswith('ALPHA:') for k in scope))):
                r=self.run_plan(root,v)
                self.assertEqual((r['etape'],r['phase']),('BETTA','G1'))
                self.assertEqual([len(x['unites']) for x in r['prochains_lots']],[3,2])
                self.assertFalse(r['complet'])

    def test_no_differential_requires_applicability_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root);v[3]['ssp_restant']=[]
            v[2]['occurrences']=[x for x in v[2]['occurrences'] if x['ssp']!='G1']
            p=root/'app_v2.html';text=p.read_text();a,b=planner.span(text,'NOT');n=json.loads(text[a:b]);n['G1']=[[]];p.write_text(text[:a]+json.dumps(n)+text[b:])
            with patch.object(planner,'publie',return_value=True),patch.object(planner,'audit_phase',return_value=True):
                r=self.run_plan(root,v)
                self.assertEqual(r['phase'],'G1')
                self.assertEqual(r['prochains_lots'][0]['unites'],['G1:applicabilite'])

    def test_gamma_cannot_start_before_betta_and_uses_correct_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root);v[3]['ssp_restant']=[]
            with patch.object(planner,'publie',side_effect=lambda root,record,key,digest:not key.startswith('GAMMA:')),patch.object(planner,'audit_phase',return_value=True):
                self.assertEqual(self.run_plan(root,v)['etape'],'BETTA')
                for x in v[2]['occurrences']:x['prototype_relecture']=True
                r=self.run_plan(root,v)
                self.assertEqual((r['etape'],r['phase']),('GAMMA','organisation'))

    def test_reservation_errors_block_dispatch_and_duplicate_agent_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root)
            reservation=dict(etape='ALPHA',phase='S',agent='a',modele='gpt-6-sol',raisonnement='high',statut='en_redaction',unites=['S1.1'])
            for second in [dict(reservation,unites=['S1.2']),dict(reservation,agent='b',unites=['S1.2'],statut='unknown'),dict(reservation,agent='b',unites=['S1.2','S1.2'])]:
                v[1]['reservations']=[reservation,second]
                r=self.run_plan(root,v);self.assertTrue(r['anomalies']);self.assertFalse(r['prochains_lots'])

    def test_astra_and_scope_are_required_not_a_label_alone(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);p=root/'audit.json';scope={'ALPHA:S1.1':'a'*64}
            r=dict(verdict='favorable_documentaire',relecteur_independant='auditeur',auteur='auteur',modele='gpt-6-astra',lu_le='2026-01-01',perimetre_sha256=planner.empreinte(scope))
            def record():
                p.write_text(json.dumps(r));return dict(rapport='audit.json',rapport_sha256=hashlib.sha256(p.read_bytes()).hexdigest())
            self.assertTrue(planner.audit_phase(root,record(),scope))
            for field,value in [('modele','gpt-6-sol'),('lu_le','2999-01-01'),('relecteur_independant','auteur')]:
                old=r[field];r[field]=value;self.assertFalse(planner.audit_phase(root,record(),scope));r[field]=old
            self.assertFalse(planner.audit_phase(root,record(),{'ALPHA:S1.2':'a'*64}))
            self.assertFalse(planner.audit_phase(root,record(),{}))

    def test_gamma_scope_cannot_be_replaced_with_a_chosen_empty_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);self.fixture(root)
            (root/'assets/config').mkdir(parents=True);p=root/'assets/config/fonctions.js';p.write_text('function a(){}')
            first=planner.gamma_scope(root);self.assertIn('app_v2.html',first);self.assertIn('assets/config/fonctions.js',first)
            p.write_text('function b(){}');self.assertNotEqual(first,planner.gamma_scope(root))

    def test_complete_rejects_a_forged_summary_without_phases(self):
        report={'plan':{'mandat':{'id':planner.ID,'etape':'TERMINE','complet':True,'anomalies':[]}}}
        self.assertFalse(relay.guard.complete(report))

    def test_stale_or_truncated_coordination_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root);v[2]['occurrences'].pop()
            with self.assertRaisesRegex(ValueError,'Inventaire'):
                self.run_plan(root,v)

    def test_live_reservation_prevents_complete_even_when_all_proofs_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root);v[3]['ssp_restant']=[]
            for x in v[2]['occurrences']:x['prototype_relecture']=True
            with patch.object(planner,'publie',return_value=True),patch.object(planner,'audit_phase',return_value=True):
                r=self.run_plan(root,v);self.assertTrue(r['complet']);self.assertTrue(relay.guard.complete({'plan':{'mandat':r}}))
                v[1]['reservations']=[dict(etape='ALPHA',phase='S',agent='a',modele='gpt-6-sol',raisonnement='high',statut='en_redaction',unites=['S1.1'])]
                r=self.run_plan(root,v);self.assertFalse(r['complet']);self.assertTrue(r['anomalies'])

    def test_refresh_shallow_checkout_restores_old_publication_commits(self):
        from tools.garde import permanence
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/'source';source.mkdir()
            def git(*args):return planner.git(source,*args).decode().strip()
            git('init','-qb','main');git('config','user.email','audit@example.invalid');git('config','user.name','audit')
            (source/'file').write_text('old');git('add','.');git('commit','-qm','old');old=git('rev-parse','HEAD')
            (source/'file').write_text('new');git('add','.');git('commit','-qm','new');new=git('rev-parse','HEAD')
            shallow=root/'shallow';planner.git(root,'clone','-q','--depth','1',source.as_uri(),str(shallow))
            self.assertEqual(planner.git(shallow,'rev-parse','--is-shallow-repository').strip(),b'true')
            permanence.refresh_history(shallow)
            self.assertEqual(planner.git(shallow,'rev-parse','--is-shallow-repository').strip(),b'false')
            self.assertEqual(planner.git(shallow,'rev-parse','origin/main').decode().strip(),new)
            self.assertEqual(planner.git(shallow,'show',old+':file'),b'old')

    def test_local_review_date_is_bound_to_real_utc_instant_and_timezone(self):
        from datetime import datetime, timezone
        from zoneinfo import ZoneInfo
        now=datetime.now(timezone.utc)
        r=dict(lu_le=now.astimezone(ZoneInfo('Europe/Zurich')).date().isoformat(),
               audit_utc=now.isoformat(),fuseau_date_lecture='Europe/Zurich')
        self.assertTrue(planner.date_audit(r))
        r['audit_utc']='2999-01-01T00:00:00+00:00';self.assertFalse(planner.date_audit(r))
        r['audit_utc']=now.isoformat();r['lu_le']='2000-01-01';self.assertFalse(planner.date_audit(r))
        r['fuseau_date_lecture']='Unknown/Zone';self.assertFalse(planner.date_audit(r))

    def test_waiting_publication_does_not_consume_an_active_agent_slot(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root)
            v[1]['reservations']=[dict(etape='ALPHA',phase='S',agent='a'+str(i),branche='b'+str(i),modele='gpt-6-sol',raisonnement='high',statut=status,unites=[code])
                for i,(code,status) in enumerate([('S1.1','a_publier'),('S1.2','a_publier'),('S1.3','en_audit'),('S2.1','en_redaction')])]
            v[1]['reservations'][1]['branche']=v[1]['reservations'][0]['branche']
            r=self.run_plan(root,v);self.assertFalse(r['anomalies']);self.assertEqual(len(r['reservations_actives']),4)
            self.assertEqual(r['prochains_lots'][0]['travail_attendu'],'publier_et_verifier_sans_nouvelle_redaction')
            for row in v[1]['reservations']:row['statut']='en_redaction'
            r=self.run_plan(root,v);self.assertTrue(r['anomalies']);self.assertFalse(r['prochains_lots'])

    def test_models_and_limits_cannot_silently_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root);v[0]['redaction']['ssp_max_par_agent']=3
            with self.assertRaises(ValueError):self.run_plan(root,v)

    def test_relay_uses_mandate_and_preserves_old_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);v=self.fixture(root);m=self.run_plan(root,v)
            report={'plan':{'mandat':m},'mesure':{}}
            state={'mesure':m['mesure'].copy(),'dernier_progres':0}
            cfg={'request_cooldown_seconds':1800}
            self.assertEqual(relay.decision(state,report,1000,False,cfg),'demander_reprise')
            body=relay.prompt(report,'reservation')
            self.assertIn('Étape ALPHA, phase S',body);self.assertIn('S1.1',body)
            self.assertIn('BETTA seulement après ALPHA',body);self.assertNotIn('brouillon G2',body)
            m['anomalies']=['preuve périmée']
            self.assertEqual(relay.decision(state,report,1000,False,cfg),'preuves_mandat_invalides_sans_relance')
            self.assertFalse(relay.guard.complete(report))


if __name__=='__main__':unittest.main()
