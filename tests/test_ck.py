#!/usr/bin/env python3
"""Janus · tests/test_ck.py : données, schémas et contrôles du socle CK et de l'audit médical de niveau 1 (sans navigateur, quelques secondes).

Chaque contrôle doit réussir sur un jeu d'essai conforme et échouer quand sa règle est violée :
compilateur et schémas (G5), doses (G1), sources (G2), domaines (G3), Lyncée (G4), verbes (G6),
rouge (G7), justification (G8), budgets, schémas SVG des nerfs, rapport des fautes et accord de Vial sur une faute critique.
Le jeu d'essai est FICTIF (substance-test, sources d'exemple) et vit dans un dossier temporaire.
Sortie : une ligne par contrôle, puis le décompte ; code 1 au premier échec.
"""
import copy, json, os, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
T = os.path.join(ROOT, 'tools')
J = '2026-10-17'
APP = ('<!doctype html><html><head><title>t</title><style>.ck-win{color:#111}</style></head><body><p>Accueil</p><script>\n'
       'const TIP={"X1":{"c":["Le patient présente une dyspnée."],"s":"source"}};\n'
       'const NOT={};\nconst GES=[{"id":"neuro-nc","items":[]}];\n</script></body></html>')
SRC = [{'id': 'R1', 'titre': 'Recommandation fictive', 'org': 'Société suisse fictive', 'pays': 'CH',
        'type': 'ligne-directrice', 'url': 'https://www.swissneuro.ch/exemple'},
       {'id': 'G1918', 'titre': 'Anatomie fictive', 'org': 'Éditeur fictif', 'pays': 'US', 'type': 'anatomie',
        'url': 'https://commons.wikimedia.org/wiki/Exemple', 'licence': 'Domaine public'}]
REF = [{'id': 'R1', 'loc': '§ 1', 'lu_le': J}]
GLO = [{'id': 'dyspnee', 'type': 'signe', 'label': 'Dyspnée', 'flexions': ['dyspnées'],
        'def': 'La gêne respiratoire est ressentie par le patient au repos ou à l’effort.',
        'recherche': 'On interroge le patient sur la gêne et on compte la fréquence respiratoire.', 'src': REF},
       {'id': 'signe-exemple', 'type': 'syndrome', 'label': 'Syndrome exemple',
        'def': 'Ce syndrome fictif associe une dyspnée et une gêne au repos.', 'composantes': ['dyspnee'], 'src': REF}]
# Justification exigée par G8 (mécanisme, principe, pourquoi ce choix ; limites pour un moyen).
JX = {'mecanisme': 'La maladie fictive bloque la fonction du tissu.', 'principe': 'Le moyen fictif agit sur ce blocage.',
      'pourquoi_ce_choix': 'Il est disponible partout et plus simple que les autres.'}
SYN = [{'id': 'syn-ex', 'label': 'Syndrome exemple', 'module': 'neuro-nc', 'signes': ['dyspnee'],
        'a_demander': ['durée de la gêne'], 'hyp': ['hyp-ex'], 'src': REF}]
HYP = [{'id': 'hyp-ex', 'label': 'Hypothèse exemple', 'syn': ['syn-ex'], 'bloquant': False,
        'exam': {'lignes': [{'rang': 1, 'nom': 'Examen A', **JX, 'recherche': 'une anomalie', 'src': REF},
                            {'rang': 2, 'nom': 'Examen B', **JX, 'recherche': 'une cause rare', 'src': REF}]},
        'confirmation': 'Le diagnostic se confirme par l’examen A.',
        'pec': {'objectif': 'On rétablit la fonction.', 'mesures_generales': ['On protège la zone atteinte.'],
                'moyens_specifiques': [{'type': 'pharmaco', **JX, 'limites': 'Elle est contre-indiquée en cas d’allergie connue.',
                                        'texte': 'On donne la substance-test 10 mg/j par voie orale.',
                                        'dose_ref': 'substance-test-po', 'src': REF}]}, 'src': REF}]
NC = [{'id': 'nc07', 'nom': 'Nerf exemple', 'noyaux': ['noyau A'], 'trajet': ['segment A'], 'foramens': ['orifice A'],
       'territoires': ['territoire A'], 'vues': {'face': 'assets/nc/nc07-face.svg'}, 'tour': None,
       'lesions': [{'site': 1, 'niveau': 'niveau A', 'deficit': 'Le déficit touche la moitié du territoire.', 'syn': 'syn-ex',
                    'exam_orientant': 'Examen A', 'hyp': ['hyp-ex'], 'src': REF}]}]
LOC = [{'module': 'neuro-nc', 'A': ['syn-ex'], 'B': ['hyp-ex']}]
DOS = [{'id': 'substance-test-po', 'substance': 'substance-test', 'produit_ch': 'Produit fictif', 'dose': '10 mg/j pendant 5 jours',
        'voie': 'p.o.', 'population': 'adulte', 'aips_rubrique': 'Posologie/Mode d’emploi',
        'url': 'https://www.swissmedicinfo.ch/exemple', 'lu_le': J, 'lu_par': 'Galien'}]
SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><g id="trait"/><g id="nerf"/><g id="legendes"/></svg>')
CRED = [{'fichier': 'nc07-face.svg', 'source': 'Exemple', 'auteur': 'Auteur', 'licence': 'Domaine public',
         'url': 'https://commons.wikimedia.org/wiki/Exemple', 'derive': True, 'licence_derivee': 'CC BY-SA 4.0'}]
BASE = {'src': SRC, 'glo': GLO, 'syn': SYN, 'hyp': HYP, 'nc': NC, 'loc': LOC, 'doses_ch': DOS}


def run(script, *args, env=None, cwd=None):
    p = subprocess.run([PY, os.path.join(T, script), *args], capture_output=True, text=True, cwd=cwd,
                       env={**os.environ, **(env or {})})
    return p.returncode, p.stdout + p.stderr


class Fixture:
    def __init__(self):
        self.d = tempfile.mkdtemp(prefix='ck-')
        os.makedirs(os.path.join(self.d, 'data', 'ck'))
        shutil.copytree(os.path.join(ROOT, 'data', 'ck', 'schema'), os.path.join(self.d, 'data', 'ck', 'schema'))
        os.makedirs(os.path.join(self.d, 'qa', 'audit'))
        os.makedirs(os.path.join(self.d, 'assets', 'nc'))
        shutil.copy(os.path.join(ROOT, 'qa', 'domaines.yml'), os.path.join(self.d, 'qa'))
        open(os.path.join(self.d, 'qa', 'termes_exclus.txt'), 'w').write('# vide\n')
        self.app(APP)
        open(os.path.join(self.d, 'assets', 'nc', 'nc07-face.svg'), 'w').write(SVG)
        json.dump(CRED, open(os.path.join(self.d, 'assets', 'nc', 'credits.json'), 'w'))
        self.data = copy.deepcopy(BASE)
        self.save()
        run('audit/niveau1.py', '--racine', self.d, '--init-doses')
        run('lyncee.py', '--racine', self.d, '--init')
        run('ck_build.py', '--racine', self.d)
        open(os.path.join(self.d, 'qa', 'audit', 'fautes.jsonl'), 'w').write('')
        run('audit/rapport_fautes.py', '--racine', self.d)

    def app(self, html):
        open(os.path.join(self.d, 'app_v2.html'), 'w', encoding='utf-8').write(html)

    def save(self):
        for k, v in self.data.items():
            json.dump(v, open(os.path.join(self.d, 'data', 'ck', k + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    def gate(self, g):
        return run('audit/niveau1.py', '--racine', self.d, '--only', g)[0]

    def close(self):
        shutil.rmtree(self.d, ignore_errors=True)


R = {}


def case(name, fn):
    f = Fixture()
    try:
        R[name] = bool(fn(f))
    except Exception as e:  # un test qui plante échoue
        R[name] = False
        print('  exception', name, type(e).__name__, e)
    finally:
        f.close()


def mut(f, fn, g):
    fn(f.data)
    f.save()
    return f.gate(g) == 1


# Socle : le jeu conforme passe partout.
case('socle_jeu_conforme_passe_G1_a_G8', lambda f: run('audit/niveau1.py', '--racine', f.d)[0] == 0)
case('socle_ck_build_check_a_jour', lambda f: run('ck_build.py', '--racine', f.d, '--check')[0] == 0)
case('socle_ck_build_perime_echoue', lambda f: (f.data['glo'][0].update(label='Dyspnée modifiée'), f.save(),
                                               run('ck_build.py', '--racine', f.d, '--check')[0] == 1)[-1])
case('socle_sortie_compacte_window_CK', lambda f: open(os.path.join(f.d, 'assets', 'ck', 'glo-index.js'), encoding='utf-8').read()
     .split('\n')[1].startswith('window.CK_GLO_INDEX={') and os.path.exists(os.path.join(f.d, 'assets', 'ck', 'glo-d.js')))
case('socle_alétheia_passe', lambda f: run('aletheia.py', '--racine', f.d)[0] == 0)
# G1 doses
case('G1_dose_sans_dose_ref_echoue', lambda f: mut(f, lambda d: d['hyp'][0]['pec']['moyens_specifiques'][0].pop('dose_ref'), 'G1'))
case('G1_dose_absente_de_la_ligne_echoue', lambda f: mut(f, lambda d: d['hyp'][0]['pec']['moyens_specifiques'][0].update(
    texte='On donne la substance-test 20 mg/j par voie orale.'), 'G1'))
case('G1_dose_a_verifier_passe', lambda f: not mut(f, lambda d: d['hyp'][0]['pec']['moyens_specifiques'][0].update(
    dose_ref=None, statut='À vérifier'), 'G1'))
case('G1_concentration_n_est_pas_une_dose', lambda f: not mut(f, lambda d: d['glo'][1].update(
    orientation='Une glycémie de 11 mmol/L oriente vers un trouble glycémique.'), 'G1'))
case('G1_dose_nouvelle_dans_TIP_echoue', lambda f: (f.app(APP.replace('une dyspnée.', 'une dyspnée ; on donne 5 mg/kg.')), f.gate('G1') == 1)[-1])
case('G1_dose_nouvelle_TIP_a_verifier_passe', lambda f: (f.app(APP.replace('une dyspnée.', 'une dyspnée ; 5 mg/kg (À vérifier).')), f.gate('G1') == 0)[-1])
case('G1_ligne_hors_AIPS_echoue', lambda f: mut(f, lambda d: d['doses_ch'][0].update(url='https://www.exemple.com/x'), 'G1'))
# G2 sources
case('G2_sans_source_echoue', lambda f: mut(f, lambda d: d['glo'][0].pop('src'), 'G2'))
case('G2_a_verifier_passe', lambda f: not mut(f, lambda d: (d['glo'][0].pop('src'), d['glo'][0].update(statut='À vérifier')), 'G2'))
case('G2_date_future_echoue', lambda f: mut(f, lambda d: d['syn'][0].update(src=[{'id': 'R1', 'lu_le': '2099-01-01'}]), 'G2'))
case('G2_ligne_imbriquee_sans_source_echoue', lambda f: mut(f, lambda d: d['hyp'][0]['exam']['lignes'][1].pop('src'), 'G2'))
# G3 domaines
case('G3_domaine_hors_liste_echoue', lambda f: mut(f, lambda d: d['src'][0].update(url='https://www.exemple-nord-americain.org/x'), 'G3'))
case('G3_editeur_hors_europe_echoue', lambda f: mut(f, lambda d: d['src'][0].update(url='https://doi.org/10.1/x', pays='US'), 'G3'))
case('G3_anatomie_commons_passe', lambda f: f.gate('G3') == 0)
case('G3_anatomie_reservee_au_type_anatomie', lambda f: mut(f, lambda d: d['src'][0].update(url='https://commons.wikimedia.org/x'), 'G3'))
# G4 Lyncée
case('G4_terme_nouveau_non_defini_echoue', lambda f: (f.app(APP.replace('une dyspnée.', 'une dyspnée et une hépatomégalie.')), f.gate('G4') == 1)[-1])
case('G4_terme_dans_une_definition_echoue', lambda f: mut(f, lambda d: d['glo'][0].update(**{'def': 'La gêne respiratoire accompagne parfois une cyanose des lèvres.'}), 'G4'))
case('G4_terme_defini_passe', lambda f: (f.app(APP.replace('une dyspnée.', 'une dyspnée et une hépatomégalie.')),
                                       f.data['glo'].append({'id': 'hepatomegalie', 'type': 'signe', 'label': 'Hépatomégalie',
                                                             'def': 'Le foie déborde le rebord costal à la palpation.', 'recherche': 'On palpe le foie.', 'src': REF}),
                                       f.save(), f.gate('G4') == 0)[-1])
case('G4_exclusion_sans_motif_echoue', lambda f: (open(os.path.join(f.d, 'qa', 'termes_exclus.txt'), 'a').write('hépatomégalie\n'), f.gate('G4') == 1)[-1])
case('G4_renvoi_glo_inexistant_echoue', lambda f: (f.app(APP.replace('<p>Accueil</p>', '<p data-t="glo|inconnu">Accueil</p>')), f.gate('G4') == 1)[-1])
case('G4_auto_reference_echoue', lambda f: mut(f, lambda d: d['glo'][0].update(**{'def': 'La dyspnée est une gêne que le patient ressent.'}), 'G4'))
case('G4_paire_circulaire_echoue', lambda f: mut(f, lambda d: d['glo'].extend([
    {'id': 'terme-a', 'type': 'terme', 'label': 'Terme alpha', 'def': 'Il correspond au terme bêta, sans plus.', 'voir': ['terme-b'], 'src': REF},
    {'id': 'terme-b', 'type': 'terme', 'label': 'Terme bêta', 'def': 'Il correspond au terme alpha, sans plus.', 'voir': ['terme-a'], 'src': REF}]), 'G4'))


def _baseline_grows(f):
    b = os.path.join(f.d, 'qa', 'termes-baseline.json')
    subprocess.run(['git', 'init', '-q'], cwd=f.d)
    subprocess.run(['git', '-c', 'user.email=t@t', '-c', 'user.name=t', 'add', '-A'], cwd=f.d)
    subprocess.run(['git', '-c', 'user.email=t@t', '-c', 'user.name=t', 'commit', '-qm', 'base'], cwd=f.d)
    x = json.load(open(b))
    x['termes'].append('hepatomegalie')
    json.dump(x, open(b, 'w'))
    f.app(APP.replace('une dyspnée.', 'une dyspnée et une hépatomégalie.'))
    return run('lyncee.py', '--racine', f.d, '--diff', 'HEAD')[0] == 1 and run('lyncee.py', '--racine', f.d)[0] == 0


case('G4_reference_ne_peut_que_baisser', _baseline_grows)
case('G4_update_resserre_sans_ajouter', lambda f: (f.data['glo'].append({'id': 'patient', 'type': 'terme', 'label': 'Patient',
                                                                         'def': 'La personne reçoit les soins.', 'src': REF}), f.save(),
                                                 run('lyncee.py', '--racine', f.d, '--update')[0] == 0)[-1])
# G5 chaîne
case('G5_reference_et_lignes_ensemble_echoue', lambda f: mut(f, lambda d: d['hyp'][0]['exam'].update(
    reference={'nom': 'Examen R', 'recherche': 'la cause', 'src': REF}), 'G5'))
case('G5_sans_deuxieme_intention_echoue', lambda f: mut(f, lambda d: d['hyp'][0]['exam']['lignes'].pop(), 'G5'))
case('G5_premiere_intention_sans_pourquoi_ce_choix_echoue', lambda f: mut(f, lambda d: d['hyp'][0]['exam']['lignes'][0].pop('pourquoi_ce_choix'), 'G5'))
case('G5_sans_objectif_echoue', lambda f: mut(f, lambda d: d['hyp'][0]['pec'].pop('objectif'), 'G5'))
case('G5_renvoi_croise_inexistant_echoue', lambda f: mut(f, lambda d: d['syn'][0]['signes'].append('absent'), 'G5'))
case('G5_module_hors_GES_echoue', lambda f: mut(f, lambda d: d['loc'][0].update(module='module-inconnu'), 'G5'))
case('G5_lesion_incomplete_echoue', lambda f: mut(f, lambda d: d['nc'][0]['lesions'][0].pop('exam_orientant'), 'G5'))
case('G5_signe_sans_recherche_echoue', lambda f: mut(f, lambda d: d['glo'][0].pop('recherche'), 'G5'))
case('G5_reference_seule_passe', lambda f: not mut(f, lambda d: d['hyp'][0].update(exam={'reference': {'nom': 'Examen R', **JX, 'recherche': 'la cause', 'src': REF}}), 'G5'))
# G6 verbes
case('G6_phrase_nominale_echoue', lambda f: mut(f, lambda d: d['hyp'][0]['pec'].update(objectif='Restauration rapide de la fonction motrice.'), 'G6'))
case('G6_elision_verbale_passe', lambda f: not mut(f, lambda d: d['hyp'][0]['pec'].update(objectif='La fonction s’améliore en quelques jours.'), 'G6'))
case('G6_libelle_court_exempte', lambda f: not mut(f, lambda d: d['hyp'][0].update(label='Atteinte motrice périphérique aiguë'), 'G6'))
# G7 rouge
case('G7_rouge_en_ligne_non_bloquant_echoue', lambda f: mut(f, lambda d: d['hyp'][0].update(
    confirmation='Le diagnostic <span style="color:#c00">se confirme</span> par l’examen A.'), 'G7'))
case('G7_urg_sur_bloquant_passe', lambda f: not mut(f, lambda d: d['hyp'][0].update(
    bloquant=True, confirmation='Le diagnostic <span class="urg">se confirme</span> en urgence.'), 'G7'))
case('G7_css_ck_rouge_echoue', lambda f: (f.app(APP.replace('.ck-win{color:#111}', '.ck-win{color:#c0392b}')), f.gate('G7') == 1)[-1])
case('G7_css_ck_urg_passe', lambda f: (f.app(APP.replace('.ck-win{color:#111}', '.ck-win .urg{color:var(--bad)}')), f.gate('G7') == 0)[-1])
# G8 justification
H0 = lambda d: d['hyp'][0]
case('G8_jeu_conforme_passe', lambda f: f.gate('G8') == 0)
case('G8_examen_sans_mecanisme_echoue', lambda f: mut(f, lambda d: H0(d)['exam']['lignes'][1].pop('mecanisme'), 'G8'))
case('G8_examen_principe_vide_echoue', lambda f: mut(f, lambda d: H0(d)['exam']['lignes'][0].update(principe='  '), 'G8'))
case('G8_reference_sans_pourquoi_ce_choix_echoue', lambda f: mut(f, lambda d: H0(d).update(exam={'reference': {
    'nom': 'Examen R', 'mecanisme': JX['mecanisme'], 'principe': JX['principe'], 'recherche': 'la cause', 'src': REF}}), 'G8'))
case('G8_moyen_sans_limites_echoue', lambda f: mut(f, lambda d: H0(d)['pec']['moyens_specifiques'][0].pop('limites'), 'G8'))
case('G8_moyen_principe_recopie_echoue', lambda f: mut(f, lambda d: H0(d)['pec']['moyens_specifiques'][0].update(
    principe=JX['mecanisme']), 'G8'))
case('G8_champ_trop_court_echoue', lambda f: mut(f, lambda d: H0(d)['pec']['moyens_specifiques'][0].update(pourquoi_ce_choix='Efficace.'), 'G8'))
case('G8_ancien_champ_pourquoi_echoue', lambda f: mut(f, lambda d: H0(d)['exam']['lignes'][0].update(pourquoi='Il est disponible partout.'), 'G8'))
case('G8_a_verifier_admis', lambda f: not mut(f, lambda d: H0(d)['pec']['moyens_specifiques'][0].update(
    limites='Les contre-indications restent À vérifier dans une source suisse.'), 'G8'))
# Vue liée depuis un syndrome (voie motrice) : nerf absent = erreur ; vue non livrée = avertissement seul.
case('G5_syn_vue_nerf_absent_echoue', lambda f: mut(f, lambda d: d['syn'][0].update(vues=['nc|nc08|voie_motrice']), 'G5'))
case('G5_syn_vue_non_livree_avertit', lambda f: (f.data['syn'][0].update(vues=['nc|nc07|voie_motrice']), f.save(),
                                               (lambda r: r[0] == 0 and 'pas encore livrée' in r[1])(run('ck_build.py', '--racine', f.d)))[-1])
case('G5_syn_vue_inconnue_echoue', lambda f: mut(f, lambda d: d['syn'][0].update(vues=['nc|nc07|dessus']), 'G5'))
# Artefact
case('artefact_audit_flags_ecrit', lambda f: (mut(f, lambda d: d['glo'][0].pop('src'), 'G2'),
                                             run('audit/niveau1.py', '--racine', f.d, '--sortie', os.path.join(f.d, 'qa', 'audit-flags.json')),
                                             json.load(open(os.path.join(f.d, 'qa', 'audit-flags.json')))[0]['controle'] == 'G2'
                                             and json.load(open(os.path.join(f.d, 'qa', 'audit-flags.json')))[0]['ligne'] > 0)[-1])


# Rapport des fautes
def _faute(f, grav, accord=None):
    x = {'unite': 'nc07', 'element': 'hyp|hyp-ex', 'region': 'neuro', 'champ': 'pec.objectif', 'faute': 'Faute fictive de test.',
         'correction': 'Correction fictive de test.', 'source': 'R1 § 1', 'lu_le': J, 'gravite': grav, 'commit': 'abc1234', 'date': J}
    if accord:
        x['accord_vial'] = accord
    open(os.path.join(f.d, 'qa', 'audit', 'fautes.jsonl'), 'a').write(json.dumps(x, ensure_ascii=False) + '\n')


case('fautes_rapport_perime_echoue', lambda f: (_faute(f, 'mineure'), run('audit/rapport_fautes.py', '--racine', f.d, '--check')[0] == 1)[-1])
case('fautes_critique_sans_accord_bloque', lambda f: (_faute(f, 'critique'), run('audit/rapport_fautes.py', '--racine', f.d),
                                                    run('audit/rapport_fautes.py', '--racine', f.d, '--check')[0] == 1)[-1])
case('fautes_critique_avec_accord_passe_et_en_tete', lambda f: (_faute(f, 'mineure'), _faute(f, 'critique', J), run('audit/rapport_fautes.py', '--racine', f.d),
                                                              run('audit/rapport_fautes.py', '--racine', f.d, '--check')[0] == 0,
                                                              open(os.path.join(f.d, 'qa', 'audit', 'RAPPORT_FAUTES.md'), encoding='utf-8').read()
                                                              .find('Fautes critiques') < open(os.path.join(f.d, 'qa', 'audit', 'RAPPORT_FAUTES.md'), encoding='utf-8').read().find('## nc07'))[-2:] == (True, True))
case('fautes_ligne_invalide_echoue', lambda f: (open(os.path.join(f.d, 'qa', 'audit', 'fautes.jsonl'), 'a').write('{"unite":"x"}\n'),
                                              run('audit/rapport_fautes.py', '--racine', f.d)[0] == 1)[-1])
# Budgets et SVG
case('budget_assets_ck_depasse_echoue', lambda f: run('budget.py', env={'BUDGET_ROOT': f.d, 'CK_MAX_BYTES': '10'})[0] == 1)
case('budget_svg_depasse_echoue', lambda f: run('budget.py', env={'BUDGET_ROOT': f.d, 'SVG_MAX_BYTES': '10'})[0] == 1)
case('budget_assets_nc_depasse_echoue', lambda f: run('budget.py', env={'BUDGET_ROOT': f.d, 'NC_MAX_BYTES': '10'})[0] == 1)
case('budget_conforme_passe', lambda f: run('budget.py', env={'BUDGET_ROOT': f.d})[0] == 0)
case('svg_conforme_passe', lambda f: run('nc_svg_check.py', '--racine', f.d)[0] == 0)
case('svg_couche_absente_echoue', lambda f: (open(os.path.join(f.d, 'assets', 'nc', 'nc07-face.svg'), 'w').write(SVG.replace('<g id="nerf"/>', '')),
                                           run('nc_svg_check.py', '--racine', f.d)[0] == 1)[-1])
case('svg_sans_credit_echoue', lambda f: (json.dump([], open(os.path.join(f.d, 'assets', 'nc', 'credits.json'), 'w')),
                                        run('nc_svg_check.py', '--racine', f.d)[0] == 1)[-1])
case('svg_ressource_externe_echoue', lambda f: (open(os.path.join(f.d, 'assets', 'nc', 'nc07-face.svg'), 'w').write(
    SVG.replace('<g id="trait"/>', '<g id="trait"><image href="https://exemple.org/a.png"/></g>')), run('nc_svg_check.py', '--racine', f.d)[0] == 1)[-1])
# Dépôt réel : données vides mais conformes, sorties à jour.
R['depot_ck_build_a_jour'] = run('ck_build.py', '--check')[0] == 0
R['depot_niveau1_reussit'] = run('audit/niveau1.py')[0] == 0
R['depot_rapport_fautes_a_jour'] = run('audit/rapport_fautes.py', '--check')[0] == 0

for k, v in R.items():
    print(('ok    ' if v else 'ÉCHEC ') + k)
print(f'Socle CK et audit : {sum(R.values())}/{len(R)}.')
sys.exit(0 if all(R.values()) else 1)
