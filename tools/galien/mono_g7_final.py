#!/usr/bin/env python3
"""Audit partiel G7/G8 : exclure les chiffres non CH/UE et les doses non encore auditées.
La décision HOPE/décès reste suspendue pour Vial ; ce script ne la valide pas.
"""
import json
from pathlib import Path

replacements = {
 'arret-hypothermique-ht-iv-lt-24-c-ou-signes-vitaux-absents': {'pha': "Adrénaline et adaptation de la posologie à l'hypothermie : À vérifier (AIPS)."},
 'hyperthyroidie-thyrotoxicose': {'pha': "Antithyroïdien de synthèse ; carbimazole et β-bloquant symptomatique : doses À vérifier (AIPS)."},
 'hypothermie-septique': {'pha': "Antibiothérapie et noradrénaline si choc : posologies À vérifier (AIPS).", 'mes': "Prélever les hémocultures ; administrer prudemment les cristalloïdes ; volume et débit À vérifier (AIPS)."},
 'hypothermie-toxique': {'pha': "Naloxone si intoxication par opioïde : dose et intervalle À vérifier (AIPS)."},
 'mastocytose-systemique-anaphylaxie': {'pha': "Adrénaline intramusculaire en première intention de l'anaphylaxie ; dose et répétition À vérifier (AIPS)."},
 'flush-a-l-alcool-aldh2': {'epi': "Prévalence et sex-ratio : À vérifier (source CH/UE).", 'phy': "Le déficit enzymatique ralentit l'élimination de l'acétaldéhyde ; les valeurs quantitatives restent À vérifier (source CH/UE).", 'exp': "Questionnaire et examens complémentaires : À vérifier (source CH/UE).", 'mes': "Informer sur les risques liés à l'alcool ; leur quantification et les indications d'endoscopie restent À vérifier (source CH/UE).", 'src': "À vérifier (source CH/UE) : la référence PLoS Med 2009 ne satisfait pas la restriction géographique du projet."},
 'menopause': {'epi': "Fréquence et durée des symptômes vasomoteurs en Suisse ou en Europe : À vérifier (source CH/UE) ; sex-ratio : sans objet."},
 'hypothermie-secondaire-endocrinienne': {'epi': "Fréquence et mortalité : À vérifier (source CH/UE)."},
}
seen = set()
for path in Path('data/ck/mono').glob('*.json'):
    data = json.loads(path.read_text())
    changed = False
    for key, values in replacements.items():
        if key in data:
            data[key].update(values)
            if key == 'menopause':
                data[key]['src'] = data[key]['src'].split(' · Duration of menopausal')[0]
            if key == 'hypothermie-secondaire-endocrinienne':
                data[key]['src'] = data[key]['src'].split(' · Myxedema Coma')[0]
            if key in list(replacements)[:5]:
                data[key]['src'] = data[key]['src'].split(' · AIPS ')[0]
            seen.add(key)
            changed = True
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=1)+'\n')
assert seen == set(replacements), set(replacements)-seen
print('G7/G8 : doses non auditées et chiffres hors cadre retirés ; décision HOPE suspendue.')
