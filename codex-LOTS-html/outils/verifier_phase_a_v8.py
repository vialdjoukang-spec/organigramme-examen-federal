#!/usr/bin/env python3
"""Contrôles statiques complémentaires : ne remplace aucun audit obligatoire.

Usage : python3 codex-LOTS-html/outils/verifier_phase_a_v8.py <Phase_A.html>
Dépendance de lecture : lxml. Aucune exécution de navigateur ou validation médicale.
"""
import base64
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

from lxml import html

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'harnais'))
import taille_xy


def verifier(path):
    raw = path.read_bytes()
    source = raw.decode('utf-8')
    tree = html.document_fromstring(source)
    checks = []

    def check(name, ok, detail=None):
        checks.append({'controle': name, 'ok': bool(ok), 'detail': detail})

    ids = [e.get('id') for e in tree.xpath('//*[@id]')]
    duplicates = [k for k, n in Counter(ids).items() if n > 1]
    check('identifiants_uniques', not duplicates, duplicates)
    broken = [a.get('href') for a in tree.xpath('//a[starts-with(@href,"#")]')
              if a.get('href')[1:] not in ids]
    check('ancres_locales_resolues', not broken, broken)
    windows = {e.get('id'): e for e in tree.xpath('//*[@popover]')}
    buttons = tree.xpath('//button[@popovertarget]')
    check('cibles_fenetres_presentes', all(b.get('popovertarget') in windows for b in buttons))
    check('fermeture_explicite', all(e.xpath('.//button[@popovertarget=$id and @popovertargetaction="hide"]', id=k)
                                    for k, e in windows.items()))
    invokers = {b.get('popovertarget') for b in buttons if b.get('popovertargetaction') != 'hide'}
    check('fenetres_accessibles_par_bouton', set(windows) <= invokers)
    headings = tree.xpath('//h2[starts-with(@id,"a-p")]')
    check('quatorze_parties', [h.get('id') for h in headings] == [f'a-p{i}' for i in range(1, 15)])
    check('paragraphes_des_parties', all(h.getparent().tag == 'section' and len(h.getparent().xpath('./p')) == 1 for h in headings))
    check('dix_diagnostics_comparatifs', len(tree.xpath('//tr[starts-with(normalize-space(td[1]),"DX.")]')) == 10)
    check('title_reserve_aux_abbreviations', all(e.tag == 'abbr' and e.get('title').strip() for e in tree.xpath('//*[@title]')))
    check('abbreviations_definies', all(e.get('title', '').strip() for e in tree.xpath('//abbr')))
    check('aucune_execution_ou_ressource_distante', not tree.xpath('//script|//iframe|//link[@rel="stylesheet"]|//*[@src and not(starts-with(@src,"data:"))]'))
    check('references_en_exposant', bool(tree.xpath('//sup[@class="s"]/a')) and '[S1]' not in source)
    check('huit_sources_identifiees', all(f's{i}' in ids for i in range(1, 9)))
    check('marque_fin', source.rstrip().endswith('<!-- FIN_FICHIER LOT_018_Phase_A -->'))
    check('mention_clinique', 'Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.' in source)
    measure = taille_xy.mesurer(source)
    check('texte_fiche_100_ko_max', measure.x[1] <= 100_000, measure.x[1])
    css = '\n'.join(tree.xpath('//style/text()'))
    encoded_fonts = re.findall(r'data:font/woff2;base64,([^"]+)', css)
    decoded_fonts = [base64.b64decode(x.replace('\\\n', ''), validate=True) for x in encoded_fonts]
    expected_fonts = [(ROOT / f'codex-LOTS-html/outils/polices/atkinson-hyperlegible-latin-{w}-normal.woff2').read_bytes() for w in (400, 700)]
    check('polices_embarquees_identiques_aux_fichiers', decoded_fonts == expected_fonts)
    originals = []
    for path_aips in (path.parent / 'evidence').glob('AIPS_*.json'):
        originals.extend(json.loads(path_aips.read_text())['sections'].values())
    unknown_quotes = []
    for block in tree.xpath('//blockquote/p'):
        quote = block.text_content().strip().removeprefix('« ').removesuffix(' »')
        if not any(quote in original for original in originals):
            unknown_quotes.append(quote[:140])
    check('citations_aips_identiques_aux_extraits', not unknown_quotes, unknown_quotes)
    return {
        'fichier': str(path), 'sha256': hashlib.sha256(raw).hexdigest(),
        'execute_le': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'portee': 'Structure et intégrité statiques seulement ; aucun audit médical, aucune validation visuelle.',
        'octets': len(raw), 'texte_fiche_octets': measure.x[1], 'texte_fenetres_octets': measure.y[1],
        'fenetres': len(windows), 'questions': len(tree.xpath('//details[@class="quiz"]')),
        'controles': checks, 'statique_ok': all(c['ok'] for c in checks),
        'rendu_navigateur': {'statut': 'non_verifie', 'motif': 'Chromium : net::ERR_BLOCKED_BY_ADMINISTRATOR pour file:// ; aucune tentative de contournement.'},
    }


if __name__ == '__main__':
    report = verifier(Path(sys.argv[1]))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if report['statique_ok'] else 1)
