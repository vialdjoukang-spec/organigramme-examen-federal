#!/usr/bin/env python3
"""Corrections après relecture des 98 lignes contre 73 textes AIPS Refdata officiels.
Lancé dans chaque branche de dose ; conserve son sous-ensemble et ses extraits.
Ne donne aucune validation humaine et ne lève pas attente-vial.
"""
import hashlib
import json
from pathlib import Path
import re

path = Path('data/ck/doses_ch.json')
rows = json.loads(path.read_text())
patch = {
 'alteplase-iv-adulte-infarctus-90-min': {'duree': 'schéma de 90 minutes si le traitement commence dans les 6 heures suivant le début des symptômes'},
 'naloxone-iv-adulte-surdosage-opioide': {'intervalle': 'répéter toutes les 2 à 3 minutes ; sans amélioration après 10 mg, rechercher une cause non opioïde ; exceptions : buprénorphine et doses élevées d’opioïdes agonistes-antagonistes'},
 'enoxaparine-sc-adulte-tvp-ep': {'duree': 'environ 10 jours en moyenne ; relais par un antagoniste de la vitamine K avec chevauchement jusqu’à la zone thérapeutique'},
 'isoniazide-po-adulte-tuberculose': {'population': 'adulte ; enfant et nourrisson (de 0 à 3 mois : ajustement individuel des doses)'},
 'isoniazide-po-prophylaxie-tuberculose': {'intervalle': 'chaque jour ; pyridoxine 10 à 20 mg/j'},
 'rifampicine-po-prophylaxie-meningocoque': {'dose': 'plus de 12 ans et plus de 60 kg : 600 mg 2 fois par jour ; enfant dès 1 mois (ou moins de 60 kg) : 10 mg/kg 2 fois par jour, sans dépasser la dose adulte ; moins d’un mois : 5 mg/kg 2 fois par jour'},
 'pyrazinamide-po-tuberculose': {'dose': '25 (20 à 30) mg/kg/j, maximum 2 g/j ; enfant de 3 à 10 ans : 30 à 35 mg/kg/j, seulement en cas d’indication absolue ; insuffisance rénale : entretien réduit à 1000 mg/j'},
 'flucloxacilline-iv-adulte': {'population': 'adulte ; clairance < 10 ml/min : 1 g toutes les 8 à 12 heures ; anurie : maximum 1 g toutes les 12 heures ; enfant : jusqu’à 100 à 150 mg/kg/j, maximum 33 mg/kg par dose'},
 'co-amoxicilline-iv-enfant': {'population': 'enfant de 3 mois à environ 12 ans (40 kg) ; nouveau-né jusqu’à 3 mois ; utiliser uniquement les présentations pédiatriques 550 mg (500/50) ou 1100 mg (1000/100)'},
 'ceftriaxone-iv-enfant-meningite': {'population': 'de 15 jours à 12 ans ; contre-indiquée chez le prématuré jusqu’à 41 semaines post-menstruelles et chez le nouveau-né de 28 jours ou moins recevant ou devant recevoir du calcium IV', 'duree': 'méningocoque 4 jours ; Haemophilus influenzae 6 jours ; pneumocoque 7 jours ; perfusion d’au moins 30 minutes dès 50 mg/kg, 60 minutes chez le nouveau-né'},
 'immunoglobuline-anti-d': {'population': 'femme Rh(D) négatif ; prophylaxie postnatale si l’enfant est Rh(D) positif ; enfant et adolescent (transfusion) : même posologie'},
 'aspirine-po-adulte-infarctus': {'voie': 'PO avec une préparation à résorption rapide non gastro-résistante, ou IV avec une préparation adaptée'},
 'phytomenadione-iv-avk': {'dose': 'hémorragie grave sous phenprocoumone : 5 à 10 mg IV avec concentré de prothrombine ou plasma frais ; intervention urgente sous phenprocoumone : 10 mg IV avec complexe prothrombinique selon son information professionnelle ; acénocoumarol, hémorragie grave : 5 mg IV avec plasma frais ou concentré de prothrombine ; phenprocoumone, INR ≥ 9 : 10 mg IV ; INR < 9 : 2 à 5 mg PO ou IV'},
 'acide-zoledronique-iv-hypercalcemie': {'population': 'adulte et patient âgé ; métastases osseuses : clairance 50 à 60 ml/min, 3,5 mg ; 40 à 49 ml/min, 3,3 mg ; 30 à 39 ml/min, 3,0 mg ; inférieure à 30 ml/min : non recommandé'},
 'lanreotide-sc': {'dose': 'acromégalie et symptômes de TNE : initiale 60 mg tous les 28 jours, maximum 120 mg tous les 28 jours ; acromégalie stabilisée : 120 mg tous les 42 ou 56 jours ; TNE-GEP : 120 mg tous les 28 jours'},
 'chlorure-potassium-iv': {'dose': 'valeurs indicatives : apport quotidien maximal 400 mmol si K+ inférieur à 2,0 mmol/l, 200 mmol si K+ supérieur à 2,5 mmol/l ; concentration maximale dans le soluté 80 mmol/l (K+ inférieur à 2,0) ou 40 mmol/l (K+ supérieur à 2,5) ; vitesse de perfusion : À vérifier (AIPS, unité ambiguë dans le texte officiel)'},
 'dexamethasone-iv-adulte-oedeme-cerebral': {'dose': 'forme subaiguë ou chronique (tumeur, abcès, méningo-encéphalite) : 8 à 12 mg, puis 4 mg toutes les 6 heures ; formes aiguës traumatiques, hémorragiques ou ischémiques : indication À vérifier avant toute utilisation clinique'},
}
notes = {
 'obidoxime-iv-organophosphores': 'Ne dispense en aucun cas de l’atropine (AIPS).',
 'chlorure-potassium-iv': 'L’AIPS imprime « mmol/l heure » : aucune conversion supposée en mmol/heure. La vitesse reste À vérifier (AIPS).',
 'dexamethasone-iv-adulte-oedeme-cerebral': 'L’indication historique de l’AIPS ne vaut pas recommandation clinique : ESO/EANS 2025 PICO 5.1.6 déconseille les corticostéroïdes dans l’hémorragie intracérébrale spontanée aiguë hors essai.',
}
for row in rows:
    rid = row['id']
    row.update(patch.get(rid, {}))
    row['lu_le'] = '2026-10-17'  # UTC ; 18.10.2026 Europe/Zurich.
    row['lu_par'] = 'Galien'  # Rôle de relecture joué par Codex, pas validation d'un médecin.
    note = 'Extraits confrontés ligne par ligne aux textes AIPS officiels Refdata ; validation par un médecin non acquise.'
    if row.get('aips_publie', '').endswith('-01'):
        note += ' Le jour 01 de aips_publie est une normalisation du mois de aips_version ; le jour exact de publication n’est pas établi.'
    row['note'] = note + (' ' + notes[rid] if rid in notes else '')
    if rid == 'naloxone-iv-adulte-surdosage-opioide':
        row['note'] += ' Maintenir la surveillance : l’effet de certains opioïdes dépasse celui de la naloxone (AIPS).'
    if rid == 'aciclovir-iv-adulte':
        row['note'] += ' Durée clinique de l’encéphalite HSV À vérifier : l’AIPS indique 10 jours ; EAN/ESCMID 2026 §10 recommande au moins 14 jours et envisage une prolongation selon l’évolution. Source européenne relue le 17.10.2026 UTC : doi:10.1111/ene.70647.'
    if rid == 'bromocriptine-po':
        row['dose'] = row['dose'].replace('inhibition de la lactation :', 'inhibition de la lactation pour raisons médicales :')
    extra = None
    if rid == 'ceftriaxone-iv-enfant-meningite':
        extra = {'rubrique': 'Posologie/Mode d’emploi, populations particulières', 'texte': "Nourrissons, enfants en bas âge et enfants (de 15 jours à 12 ans)\nRocephin est contre-indiqué chez les nouveau-nés (≤28 jours) qui ont besoin (ou auront probablement besoin) d'un traitement par des solutions intraveineuses contenant du calcium, y compris les perfusions continues de solutions contentant du calcium, par ex. pour la nutrition parentérale, en raison du risque de formation de précipités de calcium-ceftriaxone (voir «Contre-indications»)."}
    if rid == 'immunoglobuline-anti-d':
        extra = {'rubrique': 'Indications/Possibilités d’emploi', 'texte': "b) Pour une prophylaxie postnatale lorsque le Rh(D) de la mère est négatif (D partiel y compris) et celui de l'enfant positif."}
    if extra and extra not in row['aips_extrait']:
        row['aips_extrait'].append(extra)
path.write_text(json.dumps(rows, ensure_ascii=False, indent=1)+'\n')

# Enregistrer chaque information professionnelle citée, sans inventer sa date exacte.
p = Path('data/ck/src.json')
sources = json.loads(p.read_text())
urls = {s['url'] for s in sources}
for row in rows:
    if row['url_texte'] in urls:
        continue
    auth = re.search(r'authNr=(\d+)', row['url']).group(1)
    sources.append(dict(id='AIPS-'+auth+'-'+hashlib.sha256(row['url_texte'].encode()).hexdigest()[:8],
        titre=row['produit_ch']+' — information professionnelle, '+row['aips_version'],
        org='Swissmedic / Fondation Refdata', pays='CH', type='information-professionnelle',
        url=row['url_texte'], annee=int(row['aips_publie'][:4]),
        note='Texte officiel relu le 17.10.2026 UTC ; version exprimée au mois, date exacte de publication non vérifiée.'))
    urls.add(row['url_texte'])
p.write_text(json.dumps(sources, ensure_ascii=False, indent=1)+'\n')
for ident, title, org, country, url, year in [
    ('R-EAN-ESCMID-ENCEPH-2026', 'Diagnosis and Management of Infectious Encephalitis in Adults: Guidelines From EAN and ESCMID', 'European Academy of Neurology et European Society of Clinical Microbiology and Infectious Diseases', 'CH', 'https://doi.org/10.1111/ene.70647', 2026),
    ('R-ESO-EANS-ICH-2025', 'ESO and EANS guideline on stroke due to spontaneous intracerebral haemorrhage', 'European Stroke Organisation et European Association of Neurosurgical Societies', 'CH', 'https://doi.org/10.1177/23969873251340815', 2025),
]:
    if not any(s['url'] == url for s in sources):
        sources.append(dict(id=ident, titre=title, org=org, pays=country,
                            type='ligne-directrice', url=url, annee=year,
                            note='Section clinique pertinente relue le 17.10.2026 UTC ; ne remplace pas la dose AIPS.'))
p.write_text(json.dumps(sources, ensure_ascii=False, indent=1)+'\n')
print(f'{len(rows)} lignes relues ; corrections de contexte appliquées, aucune validation humaine déclarée.')
