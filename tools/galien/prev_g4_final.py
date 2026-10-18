#!/usr/bin/env python3
"""Relecture G4 du 18.10.2026 : Limper, BASEL IX, HAS 2019, ESGE 2019, ESC 2018.
Après extract NOT/TIP et replay des corrections antérieures ; inject TIP puis prev_build/ck_build.
Aucune dose et aucun chiffre de prévalence supplémentaire.
"""
import json
from pathlib import Path

def read(p):
    return json.loads(Path(p).read_text())

def save(p, d):
    Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')

n, t, p, sources = (read(x) for x in
    ('data/NOT.json', 'data/TIP.json', 'data/ck/prev.json', 'data/ck/src.json'))
p['G6']['cadre'] = p['G6']['cadre'].replace('suivi de 30 jours', 'suivi diagnostique d’un an (mortalité évaluée à 30 jours)')
for c in ('G6', 'F1.19'):
    for item in p[c]['items']:
        if item.get('src') in ('R-LIMPER-NJM-2011', 'R-BASELIX-JIM-2021'):
            item['date_lu'] = '2026-10-17'  # UTC ; 18.10.2026 en Europe/Zurich.

skin = n['G6'][0].index('Infection de la peau et des tissus mous (érysipèle, dermohypodermite)')
before = 'aucune dans la forme simple ; échographie ou IRM si un abcès ou une fasciite est suspecté.'
after = 'aucune dans la forme simple ; échographie si un abcès est suspecté. Si une fasciite est suspectée, l’IRM ne se discute qu’en cas de doute et ne doit jamais retarder la chirurgie urgente.'
assert before in t['G6']['d'][skin] or after in t['G6']['d'][skin]
t['G6']['d'][skin] = t['G6']['d'][skin].replace(before, after)

# L'ESC réserve la troponine à la suspicion ischémique : elle n'est pas un bilan systématique de syncope.
syncope = n['F1.19'][0].index('Syncope cardiaque structurelle aiguë (syndrome coronarien aigu, dissection aortique, tamponnade)')
before = 'ECG en 10 minutes, troponine, échocardiographie au lit, angio-TDM si dissection suspectée.'
after = 'ECG initial, échocardiographie si une cause structurelle est suspectée ; troponine si une ischémie est suspectée. L’imagerie d’une dissection suspectée reste À vérifier.'
assert before in t['F1.19']['d'][syncope] or after in t['F1.19']['d'][syncope]
t['F1.19']['d'][syncope] = t['F1.19']['d'][syncope].replace(before, after)

added = [
    dict(id='R-ESGE-CBDS-2019', titre='Endoscopic management of common bile duct stones: ESGE guideline (Endoscopy 2019;51:472–491)',
         org='European Society of Gastrointestinal Endoscopy', pays='DE', type='ligne-directrice',
         url='https://www.esge.com/assets/downloads/pdfs/guidelines/2019_a_0862_0346.pdf', annee=2019),
    dict(id='R-HAS-ICB-2019', titre='Prise en charge des infections cutanées bactériennes courantes, recommandations, février 2019',
         org='HAS, SPILF, Société française de dermatologie', pays='FR', type='ligne-directrice',
         url='https://www.sfdermato.org/media/pdf/recommandation/prise-en-charge-des-nfections-utanees-bacteriennes-courantes-ecommandations-4ed00f7fca94e917a4ddfc42f6a7cd8f.pdf', annee=2019),
    dict(id='R-ESC-SYNCOPE-2018', titre='2018 ESC Guidelines for the diagnosis and management of syncope (Eur Heart J 2018;39:1883–1948)',
         org='European Society of Cardiology', pays='FR', type='ligne-directrice',
         url='https://academic.oup.com/eurheartj/article/39/21/1883/4939241', annee=2018),
]
ids = {s['id'] for s in sources}
sources.extend(s for s in added if s['id'] not in ids)
for source in sources:
    if source['id'] == 'R-LIMPER-NJM-2011':
        source['url'] = 'https://njmonline.nl/getpdf.php?id=1033'
for c, note in [('G6', 'ESGE 2019 §4 et §8.1 ; HAS/SPILF/SFD 2019 §1.2, §1.8 et §2.3, lus le 18.10.2026'),
                ('F1.19', 'ESC 2018 §4.1.1 et messages clés 3–8, lus le 18.10.2026')]:
    if note not in t[c]['s']:
        t[c]['s'] += ' · ' + note
save('data/ck/prev.json', p)
save('data/TIP.json', t)
save('data/ck/src.json', sources)
print('G4 : relecture finale appliquée, doses inchangées.')
