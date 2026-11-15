#!/usr/bin/env python3
"""Écrit REFERENTIEL_EPIDEMIO_PROFILES.md (lisible sur téléphone : listes, pas de tableau large), groupé par LOT puis DX."""
import json, os, sys, collections
ICI = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(os.path.dirname(ICI), 'out')
dest = sys.argv[1] if len(sys.argv) > 1 else f'{OUT}/REFERENTIEL_EPIDEMIO_PROFILES.md'
mp = json.load(open(f'{OUT}/mapping.json'))
ssp = {x['lot']: x for x in json.load(open('/workspace/Leona__Brief_Redaction_LOTs_20261115/scripts/ssp_dx.json'))}
par = collections.defaultdict(list)
for r in mp:
    for c in r['cibles']:
        par[c.get('lot', 0)].append((c, r))
nonp = sum(r['classe_source'] == 'non_primaire' for r in mp)
L = ['# Référentiel épidémiologique PROFILES 2023 (Suisse)', '',
     'Origine : page « Audit Épidémiologique PROFILES 2023 (248 SSP) », capture du 15.11.2026, extraite par `parse_mht.py`.',
     f'Le référentiel compte {len(mp)} valeurs pour 194 entités ; les cartes affichent 82 prévalences, 49 incidences, 43 cas annuels et 47 parts de cohorte.',
     f'Une valeur marquée ✅ vient d\'un organisme suisse (OFS, ONEC, OFSP, Obsan, Swissnoso, Suva, Swisstransplant, Tox Info Suisse). '
     f'Une valeur marquée ⚠️ ({nonp}) vient du « Cours PROFILES », de la littérature ou d\'un organisme non officiel : cette source n\'est pas primaire, donc tu la vérifies avant usage.',
     'Le rédacteur place ces valeurs dans le point 2 Épidémiologie du DX indiqué, avec la source et l\'année.', '']
for lot in sorted(par):
    s = ssp.get(lot, {})
    L.append(f'## LOT {lot:03d} · {s.get("code","")} · {s.get("nom","")}')
    for c, r in sorted(par[lot], key=lambda x: (int(x[0]['lecon'][2:]) if x[0]['lecon'].startswith('DX') else 0, x[1]['n'])):
        m = '✅' if r['classe_source'] == 'officielle_suisse' else '⚠️'
        le = c['lecon'].replace('DX', 'DX.') if c['lecon'] != 'A' else 'Phase A'
        L.append(f'- {m} **{le} {r["entite"]}** ({c["code"]}) : {r["type_libelle"].lower()} **{r["valeur"]}** ; {r["population"]} ; {r["source"]}.')
    L.append('')
open(dest, 'w').write('\n'.join(L)); print(dest, len(L))
