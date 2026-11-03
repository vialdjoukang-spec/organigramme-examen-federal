#!/usr/bin/env python3
"""Applique uniquement DX1-C1/C2. Contrôle mécanique, pas audit médical indépendant."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path

BASELINE = '1b935e9bd07319f8c8d3157b191c9b4039628fa477bea78b864a559cbb5c9b49'
CHANGES = [
    (
        'DX1-C1',
        'Pas plus de 6 à la fois ; plus de 8 dans la journée est généralement inutile, et 12 constitue un plafond exceptionnel transitoire, non un objectif. Un besoin croissant impose une réévaluation.',
        'Pas plus de 6 inhalations à la fois. Le total quotidien comprend les prises d’entretien et de secours : plus de 8 inhalations par jour n’est généralement pas nécessaire ; exceptionnellement et de manière transitoire, ce total peut atteindre 12 inhalations par jour. Un besoin croissant ou une mauvaise réponse impose une réévaluation ; une aggravation rapide nécessite une consultation urgente.'
    ),
    (
        'DX1-C2',
        'Enseigner le rinçage buccal après entretien et la technique.',
        'Enseigner la technique et le rinçage de la bouche à l’eau après chaque utilisation, conformément à l’AIPS de Symbicort.'
    )
]

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def patched(raw: bytes) -> bytes:
    if sha(raw) != BASELINE:
        raise ValueError('Source différente du brouillon audité : comparaison et réconciliation obligatoires.')
    text = raw.decode('utf-8')
    for label, old, new in CHANGES:
        if text.count(old) != 1 or new in text:
            raise ValueError(f'{label}: précondition de remplacement non satisfaite')
        text = text.replace(old, new, 1)
    return text.encode('utf-8')

def check(original: bytes, final: bytes) -> dict:
    before, after = json.loads(original), json.loads(final)
    checks: dict[str, bool] = {}
    checks['baseline_sha256'] = sha(original) == BASELINE
    checks['application_exacte_2_remplacements'] = final == patched(original)
    checks['titre_inchange'] = before['titre'] == after['titre']
    checks['sources_inchangees'] = before['sources'] == after['sources']
    checks['quiz_inchange'] = before['quiz'] == after['quiz']
    checks['14_questions'] = len(after['quiz']) == 14
    checks['13_sections_contenu_avant_section_quiz'] = [s['numero'] for s in after['sections']] == list(range(1,14))
    checks['12_sections_autres_inchangees'] = all(a == b for a,b in zip(before['sections'], after['sections']) if a['numero'] != 11)
    a11 = next(s for s in before['sections'] if s['numero'] == 11)
    b11 = next(s for s in after['sections'] if s['numero'] == 11)
    checks['section11_main_et_refs_inchanges'] = all(a11[k] == b11[k] for k in ('numero','main','refs'))
    checks['total_entretien_secours_explicite'] = 'Le total quotidien comprend les prises d’entretien et de secours' in b11['detail_html']
    checks['rinçage_apres_chaque_utilisation'] = 'après chaque utilisation' in b11['detail_html']
    checks['deux_formulations_anciennes_absentes'] = all(old not in b11['detail_html'] for _,old,_ in CHANGES)
    restored = copy.deepcopy(after)
    restored['sections'][10] = copy.deepcopy(before['sections'][10])
    checks['objet_entier_hors_section11_identique'] = restored == before
    inverse = final.decode('utf-8')
    for _,old,new in CHANGES:
        inverse = inverse.replace(new, old, 1)
    checks['reversibilite_binaire_exacte'] = inverse.encode('utf-8') == original
    checks['5_sources_ids_uniques'] = len({s['id'] for s in after['sources']}) == len(after['sources']) == 5
    ids = {s['id'] for s in after['sources']}
    checks['references_resolues'] = all(set(s['refs']) <= ids for s in after['sections'] + after['quiz'])
    if not all(checks.values()):
        raise ValueError(json.dumps(checks, ensure_ascii=False))
    return {
        'nature': 'Contrôle mécanique ciblé des deux corrections ; ni audit médical distinct ni validation HTML',
        'baseline_sha256': sha(original),
        'final_sha256': sha(final),
        'final_git_blob_sha1': hashlib.sha1(b'blob '+str(len(final)).encode()+b'\0'+final).hexdigest(),
        'octets_avant': len(original), 'octets_apres': len(final),
        'checks': checks, 'controles_reussis': sum(checks.values()), 'controles_total': len(checks),
        'controle_navigateur': False, 'harnais_global_execute': False,
        'audit_distinct_apres_correction': False, 'validation_clinique_humaine': False,
        'statut': 'corrections_ciblees_appliquees_candidat_non_promu'
    }

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('sortie', type=Path)
    parser.add_argument('--rapport', type=Path, required=True)
    args = parser.parse_args()
    raw = args.source.read_bytes()
    final = patched(raw)
    report = check(raw, final)
    args.sortie.parent.mkdir(parents=True, exist_ok=True)
    args.rapport.parent.mkdir(parents=True, exist_ok=True)
    args.sortie.write_bytes(final)
    args.rapport.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
