#!/usr/bin/env python3
"""Conversion mécanique préparatoire. Défaut: contrôle seul; --render explicite.
Compléments: --sources 1:chemin.json (répétable), objets {sources: [{id,titre|title,url}]}.
Aucun appel réseau, modification du formatter partagé ou source Phase A.
"""
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import re
import tempfile
from html import escape
from pathlib import Path

LOT = Path(__file__).resolve().parents[1]
CITATION = re.compile(r'\[((?:[A-Z]+\d+)[^\]\n]*)\]')
IDENT = re.compile(r'([A-Z]+)(\d+)(?:\s*[–—-]\s*([A-Z]*)(\d+))?')
SECTION = re.compile(r'^## (\d+)\. (.+)$', re.M)
QUESTION = re.compile(r'^\s*(\d+)\. \*\*(.+?)\*\*\s*(.*)$', re.M)


def references(text):
    found = []
    for citation in CITATION.finditer(text):
        # La partie après ; est une qualification pédagogique conservée au rendu.
        ids = citation[1]
        for match in IDENT.finditer(ids):
            prefix, start, endprefix, end = match.groups()
            if end and endprefix and endprefix != prefix:
                raise ValueError('Plage de références ambiguë: ' + match[0])
            first, last = int(start), int(end or start)
            if last < first:
                raise ValueError('Plage de références inversée: ' + match[0])
            found.extend(f'{prefix}{i}' for i in range(first, last + 1))
    return list(dict.fromkeys(found))


def input_paths(n):
    if n in (5, 10):
        return LOT / f"_travail/DX{n}_REDACTION_0858.md", LOT / f"evidence/DX{n}_0858.json"
    if n in (3, 4, 8, 9):
        return LOT / f"_travail/DX{n}_REDACTION_0506.md", LOT / f"evidence/DX{n}_0506.json"
    if n in (2, 7):
        return LOT / f"_travail/DX{n}_REDACTION_0427.md", LOT / f"evidence/DX{n}_0427.json"
    return LOT / f"_travail/DX{n}_REDACTION_0240.md", LOT / f"evidence/dx{n}_0240.json"


def read_sources(n, extras):
    rows = {}
    paths = [input_paths(n)[1], *extras]
    for path in paths:
        document = json.loads(path.read_text())
        for row in document['sources']:
            ident = row['id']
            if ident in rows and row != rows[ident]:
                raise ValueError(f'Référence {ident} redéfinie dans {path}; harmoniser les preuves')
            if not (row.get('titre') or row.get('title')) or not re.match(r'https?://', row.get('url', '')):
                raise ValueError(f'Source incomplète {ident} dans {path}')
            rows[ident] = row
    return rows, paths


def parse(n, extras):
    path = input_paths(n)[0]
    text = path.read_text()
    headings = list(SECTION.finditer(text))
    if [int(h[1]) for h in headings] != list(range(1, 15)):
        raise ValueError(f'DX.{n}: exactement 14 sections numérotées 1–14 requises')
    parts = []
    for i, h in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        parts.append((h[2], text[h.end():end].strip()))
    # Les références brutes et journaux restent dans le Markdown de preuve uniquement.
    last = parts[-1][1]
    appendix = re.search(r'^(?:#{2,3} |Sources et passages\s*:|Sources détaillées,|Sources, portée effectivement lue,)', last, re.M)
    quiz_text = last[:appendix.start()] if appendix else last
    questions = list(QUESTION.finditer(quiz_text))
    if [int(q[1]) for q in questions] != list(range(1, 15)):
        raise ValueError(f'DX.{n}: exactement 14 questions numérotées 1–14 requises')
    rows, paths = read_sources(n, extras)
    used = references(text)
    missing = sorted(set(used) - rows.keys())
    if missing:
        raise ValueError(f'DX.{n}: références sans preuve: {missing}')
    first_line = text.splitlines()[0]
    title = re.sub(r'^# .*?DX\.\s*' + str(n) + r'\s*[—–-]?\s*', '', first_line)
    return dict(n=n, title=title, parts=parts, preamble=text[len(first_line):headings[0].start()].strip(),
                rows=rows, used=used, questions=questions, quiz_text=quiz_text,
                appendix=last[appendix.start():] if appendix else '',
                paths=[path, *paths])


class Markdown:
    """Sous-ensemble explicite: paragraphes, titres, listes, tableaux, gras, liens, code.
    Le HTML source est conservé; aucune interprétation/réécriture clinique.
    """
    def __init__(self, numbers):
        self.numbers = numbers

    def inline(self, text):
        tokens = []
        def token(value):
            tokens.append(value)
            return f'\x00{len(tokens)-1}\x00'
        text = re.sub(r'</?[A-Za-z][A-Za-z0-9]*(?:\s+[^<>]*)?\s*/?>', lambda m: token(m[0]), text)
        text = escape(text, quote=False)
        def citation(match):
            def linked(ident):
                ids = references('[' + ident[0] + ']')
                return ','.join(f'<a href="#s{self.numbers[x]}">{x}</a>' for x in ids)
            return token('<sup class="s">[' + IDENT.sub(linked, match[1]) + ']</sup>')
        text = CITATION.sub(citation, text)
        text = re.sub(r'`([^`]+)`', lambda m: token('<code>' + m[1] + '</code>'), text)
        text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',
                      lambda m: token('<a href="' + escape(m[2], quote=True) + '">' + m[1] + '</a>'), text)
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
        while re.search(r'\x00\d+\x00', text):
            text = re.sub(r'\x00(\d+)\x00', lambda m: tokens[int(m[1])], text)
        return text

    def blocks(self, text):
        lines, out, i = text.splitlines(), [], 0
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                i += 1
                continue
            if line.startswith('```') or line.startswith('~~~'):
                raise ValueError('Bloc de code non pris en charge: conversion explicite nécessaire')
            if line.startswith('|'):
                rows = []
                while i < len(lines) and lines[i].startswith('|'):
                    rows.append([x.strip() for x in lines[i].strip().strip('|').split('|')]); i += 1
                if len(rows) < 2 or not all(re.fullmatch(r':?-+:?', x) for x in rows[1]):
                    raise ValueError('Table Markdown sans séparateur reconnu')
                if any(len(row) != len(rows[0]) for row in rows[2:]):
                    raise ValueError('Table Markdown non rectangulaire')
                out.append('<div class="tw"><table><thead><tr>' + ''.join('<th scope="col">' + self.inline(c) + '</th>' for c in rows[0]) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + self.inline(c) + '</td>' for c in row) + '</tr>' for row in rows[2:]) + '</tbody></table></div>')
                continue
            h = re.match(r'^(#{1,6}) (.*)', line)
            if h:
                out.append('<h3>' + self.inline(h[2]) + '</h3>'); i += 1; continue
            item = re.match(r'^(?:\d+\. |[-*] )(.*)', line)
            if item:
                tag = 'ol' if line[0].isdigit() else 'ul'
                values = []
                while i < len(lines):
                    item = re.match(r'^(?:\d+\. |[-*] )(.*)', lines[i])
                    if not item: break
                    values.append('<li>' + self.inline(item[1]) + '</li>'); i += 1
                out.append(f'<{tag}>' + ''.join(values) + f'</{tag}>'); continue
            paragraph = [line]; i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r'^(?:#|\||\d+\. |[-*] )', lines[i]):
                paragraph.append(lines[i]); i += 1
            out.append('<p>' + self.inline('\n'.join(paragraph)) + '</p>')
        return '\n'.join(out)


def clinical_scope(data):
    """Conserver le périmètre clinique verbatim, sans métadonnées de production."""
    preamble = data['preamble']
    if data['n'] == 8:
        return '**Monographie préparatoire ; ne constitue pas un protocole thérapeutique exhaustif.**\n\nPopulation adulte, principalement membre inférieur. Grossesse et pédiatrie nécessitent un parcours distinct. Les posologies présentées concernent uniquement l’apixaban, d’après la notice suisse citée.'
    if data['n'] in (2, 3, 4, 5, 7, 9, 10):
        return '**Monographie préparatoire ; ne constitue pas un protocole thérapeutique exhaustif.**\n\nPopulation adulte. Pédiatrie et grossesse nécessitent un parcours distinct. Aucune posologie médicamenteuse proposée.'
    marker = 'Le champ principal est ' if data['n'] == 1 else 'Le titre canonique est conservé ; '
    if marker not in preamble:
        raise ValueError(f"DX.{data['n']}: préambule changé, périmètre clinique à revoir")
    scope = marker + preamble.split(marker, 1)[1]
    if data['n'] == 6:
        scope = scope.split('Cette version préparatoire', 1)[0].strip()
    scope = scope.replace('Aucun HTML produit.', '').strip()
    return '**Monographie préparatoire ; ne constitue pas un protocole thérapeutique exhaustif.**\n\n' + scope


def render(data):
    # Instance de module propre par DX: aucune mutation du module partagé sur disque.
    spec = importlib.util.spec_from_file_location('formatter_dx', LOT / '_travail/format_lecon.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = data['rows']
    numbers = {ident: i for i, ident in enumerate(rows, 1)}
    module.S = [(f"{ident} — {r.get('titre') or r.get('title')}" +
                 ''.join(f' ; {k}: {r[k]}' for k in ('version', 'date', 'lecture', 'passages', 'limite', 'limites', 'portee_lue', 'date_publication', 'date_source', 'reserve_fraicheur', 'date_consultation', 'date_lecture', 'read_date') if r.get(k)), r['url']) for ident, r in rows.items()]
    module.T = [title for title, _ in data['parts']]
    md = Markdown(numbers)
    canonical = re.search(r'^DX\.' + str(data['n']) + r' — (.+)$', (LOT / 'LISTE_DX_CANONIQUE.md').read_text(), re.M)
    if not canonical: raise ValueError('Intitulé canonique absent')
    lesson = module.Lesson(canonical[1], data['n'])
    for i, (title, body) in enumerate(data['parts'], 1):
        if i == 14:
            qs = data['questions']; quiz = data['quiz_text']; details = []
            for j, q in enumerate(qs):
                end = qs[j+1].start() if j+1 < len(qs) else len(quiz)
                answer = q[3] + quiz[q.end():end]
                details.append('<details class="quiz"><summary>' + md.inline(q[2]) + '</summary>' + md.blocks(answer.strip()) + '</details>')
            detail = '\n'.join(details)
        else:
            detail = md.blocks(body)
        if i == 1: detail = md.blocks(clinical_scope(data)) + detail
        refs = tuple(numbers[x] for x in references(body))
        # Titre cliquable = aucune paraphrase susceptible de modifier le sens.
        lesson.add('{' + escape(title) + '}', detail, refs)
    cache_dir = LOT / '_travail/_cache'
    cache_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='dx-render-', dir=cache_dir) as temporary:
        module.D = Path(temporary)
        with contextlib.redirect_stdout(io.StringIO()): lesson.write()
        name = f"LOT_133_Phase_B_V0_DX.{data['n']}.html"
        raw = (module.D / name).read_text()
    old_status = 'couverture documentaire et iconographie incomplètes ; liste différentielle proposée, non gelée.'
    if raw.count(old_status) != 1:
        raise ValueError('Bannière du formatter modifiée : adaptation locale à revoir')
    raw = raw.replace(old_status, 'liste pédagogique figée ; monographie préparatoire ; illustrations absentes.')
    # Fiche de base: de <main> à la première fenêtre; bibliographie/annexes hors base.
    base = raw.split('<main>', 1)[1].split('<div id="dx', 1)[0]
    base_bytes = len(base.encode())
    if base_bytes > 9000: raise ValueError(f'Fiche de base {base_bytes} octets > 9000')
    if len(re.findall(r'<details class="quiz">', raw)) != 14: raise ValueError('Rendu: 14 questions requises')
    if len(re.findall(r'<h2 id="dx\d+-p\d+"', raw)) != 14: raise ValueError('Rendu: 14 parties requises')
    targets = set(re.findall(r'id="(s\d+)"', raw))
    if set(re.findall(r'href="#(s\d+)"', raw)) - targets: raise ValueError('Référence HTML sans cible')
    return name, raw, base_bytes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dx', nargs='+', type=int, choices=tuple(range(1, 11)), default=[1, 6])
    parser.add_argument('--sources', action='append', default=[], metavar='DX:JSON')
    parser.add_argument('--render', action='store_true', help='Écrire les HTML après autorisation root')
    args = parser.parse_args()
    extras = {n: [] for n in tuple(range(1, 11))}
    for value in args.sources:
        n, path = value.split(':', 1); extras[int(n)].append(Path(path).resolve())
    inputs = [p for n in args.dx for p in [*input_paths(n), *extras[n]]]
    snapshots = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    documents = [parse(n, extras[n]) for n in args.dx]
    outputs = [render(d) for d in documents] if args.render else []
    for path, digest in snapshots.items():
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest: raise ValueError(f'Entrée modifiée pendant le contrôle: {path}')
    for name, raw, base_bytes in outputs:
        (LOT / name).write_text(raw)
        print(f'{name}: fiche base {base_bytes} octets; préparatoire, audit clinique restant')
    for d in documents:
        print(f"DX.{d['n']}: 14 parties, 14 questions; {len(d['used'])} références citées résolues; " + ('rendu écrit' if args.render else 'contrôle seul, aucun HTML produit'))


if __name__ == '__main__':
    main()
