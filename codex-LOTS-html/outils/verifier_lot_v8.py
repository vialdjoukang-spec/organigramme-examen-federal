#!/usr/bin/env python3
"""Vérification statique V8 complémentaire, sans modifier le harnais officiel.

Ne fournit ni note de qualité médicale, ni verdict visuel ou audit indépendant.
Usage : python3 codex-LOTS-html/outils/verifier_lot_v8.py codex-LOTS-html/LOT_018
"""
import base64
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from lxml import html

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'harnais'))
import taille_xy


def normaliser(s):
    return re.sub(r'\s+', ' ', s).strip()


def verifier(dossier):
    canon = re.findall(r'^DX\.(\d+) — (.+)$', (dossier / 'LISTE_DX_CANONIQUE.md').read_text(), re.M)
    attendu = ['LOT_018_Phase_A_V0.html'] + [f'LOT_018_Phase_B_V0_DX.{i}.html' for i in range(1, 11)]
    arbres = {p.name: html.document_fromstring(p.read_bytes()) for p in dossier.glob('*.html')}
    officiels = {}
    for path in (dossier / 'evidence').glob('AIPS_*.json'):
        evidence = json.loads(path.read_text())
        source = ROOT / evidence['source']
        officiels[path.stem] = normaliser(gzip.open(source, 'rt', encoding='utf-8').read())
    rapports = []
    for nom in attendu:
        if nom not in arbres:
            continue
        path = dossier / nom
        raw = path.read_bytes()
        source = raw.decode('utf-8')
        tree = arbres[nom]
        phase_a = '_Phase_A_' in nom
        num = None if phase_a else int(re.search(r'DX\.(\d+)', nom)[1])
        prefix = 'a' if phase_a else f'dx{num}'
        checks = []

        def check(name, ok, detail=None):
            checks.append({'controle': name, 'ok': bool(ok), 'detail': detail})

        ids = [e.get('id') for e in tree.xpath('//*[@id]')]
        doubles = [k for k, n in Counter(ids).items() if n > 1]
        check('identifiants_uniques', not doubles, doubles)
        cassés = []
        for a in tree.xpath('//a[@href]'):
            href = a.get('href')
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            cible = url.path or nom
            autre = arbres.get(unquote(cible))
            if autre is None or (url.fragment and not autre.xpath('//*[@id=$v]', v=unquote(url.fragment))):
                cassés.append(href)
        check('liens_locaux_et_interfichiers_resolus', not cassés, cassés)
        windows = {e.get('id'): e for e in tree.xpath('//*[@popover]')}
        buttons = tree.xpath('//button[@popovertarget]')
        check('cibles_fenetres_presentes', all(b.get('popovertarget') in windows for b in buttons))
        check('fermeture_explicite', all(e.xpath('.//button[@popovertarget=$id and @popovertargetaction="hide"]', id=k) for k, e in windows.items()))
        accessibles = set()
        liens = []
        for b in buttons:
            if b.get('popovertargetaction') == 'hide':
                continue
            parents = b.xpath('ancestor::*[@popover]')
            liens.append((parents[-1].get('id') if parents else None, b.get('popovertarget')))
        while True:
            suivants = accessibles | {dst for src, dst in liens if src is None or src in accessibles}
            if suivants == accessibles:
                break
            accessibles = suivants
        check('fenetres_atteignables_depuis_la_fiche', set(windows) <= accessibles, sorted(set(windows) - accessibles))
        sous = {k for k, e in windows.items() if 'sousf' in e.get('class', '').split()}
        check('sous_fenetres_declenchees_depuis_une_fenetre', all(any(src in windows and dst == k for src, dst in liens) for k in sous))
        sections = tree.xpath('//section[h2[starts-with(@id,$p)]]', p=prefix+'-p')
        check('quatorze_parties_ordonnees', [s.find('h2').get('id') for s in sections] == [f'{prefix}-p{i}' for i in range(1, 15)])
        check('un_paragraphe_par_partie', all(len(s.xpath('./p')) == 1 for s in sections))
        phrases = []
        for s in sections:
            ps = s.xpath('./p')
            if not ps:
                phrases.append(0)
                continue
            el = deepcopy(ps[0])
            for e in el.xpath('.//sup'):
                e.drop_tree()
            for e in el.xpath('.//abbr'):
                e.text = 'ABREVIATION'
                for enfant in list(e):
                    e.remove(enfant)
            txt = normaliser(el.text_content())
            phrases.append(len(re.findall(r'[.!?](?=\s|$)', txt)))
        check('deux_a_quatre_phrases_par_partie', all(2 <= n <= 4 for n in phrases), phrases)
        check('quatorze_questions_depliables', len(tree.xpath('//details[@class="quiz"]')) == 14)
        check('title_reserve_aux_abbreviations', all(e.tag == 'abbr' and e.get('title', '').strip() for e in tree.xpath('//*[@title]')))
        check('abbreviations_definies', all(e.get('title', '').strip() for e in tree.xpath('//abbr')))
        check('pas_espace_insecable', '\u00a0' not in source and '\u202f' not in source)
        interdits = tree.xpath('//script|//iframe|//link[@rel="stylesheet"]|//*[@src and not(starts-with(@src,"data:"))]|//@*[starts-with(name(),"on")]')
        css = '\n'.join(tree.xpath('//style/text()'))
        check('aucune_execution_ou_ressource_distante', not interdits and not re.search(r'@import|url\([\s\x22\x27]*https?://', css))
        used = {a.get('href')[1:] for a in tree.xpath('//sup[@class="s"]/a')}
        sourced = {li.get('id') for li in tree.xpath('//section[contains(concat(" ",@class," ")," sources ")]//li[@id]')}
        check('references_exposants_et_sources_bijectives', bool(used) and used == sourced and not re.search(r'\[S\d+\]', source), {'cites': sorted(used), 'sources': sorted(sourced)})
        check('sources_avec_url', all(e.xpath('./a[starts-with(@href,"http")]') for e in tree.xpath('//li[starts-with(@id,"s")]')))
        marker = 'LOT_018_Phase_A' if phase_a else f'LOT_018_Phase_B_DX.{num}'
        check('marque_fin', source.rstrip().endswith(f'<!-- FIN_FICHIER {marker} -->'))
        check('mention_clinique', 'Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.' in source)
        texte_lu = '\n'.join(tree.xpath('//body//text()[not(parent::script or parent::style)]'))
        check('pas_meta_production_dans_lecture', not re.search(r'\b(?:LOT|corpus|Phase [AB])\b', texte_lu))
        mesure = taille_xy.mesurer(source)
        check('texte_principal_sous_limite', mesure.x[1] <= (100_000 if phase_a else 9_000), mesure.x[1])
        check('taille_inscrite', len(tree.xpath('//*[@id="taille"]')) == 1 and 'T =' in tree.xpath('//*[@id="taille"]')[0].text_content())
        fonts = re.findall(r'data:font/woff2;base64,([^\x22]+)', css)
        try:
            decoded = [base64.b64decode(x.replace('\\\n', ''), validate=True) for x in fonts]
            expected = [(ROOT / f'codex-LOTS-html/outils/polices/atkinson-hyperlegible-latin-{w}-normal.woff2').read_bytes() for w in (400, 700)]
            check('polices_embarquees_identiques', decoded == expected)
        except ValueError as e:
            check('polices_embarquees_identiques', False, str(e))
        style_source = (ROOT / 'harnais/modele_lecon/style_lecon.css').read_text()
        check('style_officiel_repris', re.sub(r'\s+', '', style_source) in re.sub(r'\s+', '', css))
        inconnues = []
        quotes = tree.xpath('//blockquote/p')
        for block in quotes:
            q = normaliser(block.text_content().strip().removeprefix('« ').removesuffix(' »'))
            if not q or not any(q in original for original in officiels.values()):
                inconnues.append(q[:160])
        check('citations_aips_presentes_dans_fichiers_originaux', not inconnues, {'citations': len(quotes), 'non_retrouvees': inconnues})
        if not phase_a:
            titre = f'DX.{num} — {dict(canon).get(str(num), "ABSENT")}'
            check('titre_canonique_exact', f'<h2>{titre}</h2>' in source)
        else:
            noms = [normaliser(tr.xpath('./td[1]')[0].text_content()) for tr in tree.xpath('//tr[starts-with(normalize-space(td[1]),"DX.")]')]
            check('dix_diagnostics_canoniques_ordre_identique', noms == [f'DX.{n} — {s}' for n, s in canon])
        rapports.append({'fichier': nom, 'sha256': hashlib.sha256(raw).hexdigest(), 'octets': len(raw), 'texte_fiche_octets': mesure.x[1], 'texte_fenetres_octets': mesure.y[1], 'fenetres': len(windows), 'sous_fenetres': len(sous), 'citations_aips': len(quotes), 'controles': checks, 'statique_ok': all(c['ok'] for c in checks)})
    lot_ok = sorted(arbres) == sorted(attendu) and len(canon) == 10
    return {'lot': 'LOT_018', 'execute_le': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'portee': 'Vérifications statiques complémentaires V8 ; aucun score médical ni essai navigateur.', 'onze_fichiers_et_dix_diagnostics': lot_ok, 'statique_ok': lot_ok and all(r['statique_ok'] for r in rapports), 'fichiers': rapports, 'audit_independant_effectue': False, 'rendu_navigateur_verifie': False, 'rapports_officiels': 'Rapports bruts conservés ; leurs résultats ne sont pas remplacés par ce contrôle.'}


if __name__ == '__main__':
    resultat = verifier(Path(sys.argv[1]))
    print(json.dumps(resultat, ensure_ascii=False, indent=2))
    sys.exit(0 if resultat['statique_ok'] else 1)
