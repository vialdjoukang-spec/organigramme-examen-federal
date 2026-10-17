#!/usr/bin/env python3
"""Janus · génère tools/audit/verbes_conjugues.txt.gz, la liste des formes verbales conjuguées
utilisée par le contrôle G6 (phrase sans verbe).

Source préférée (plan, section 9) : Lexique 3.83 (CC BY-SA 4.0), si le fichier
.cache/lexique/Lexique383.tsv existe (cache local, jamais versionné) : formes VER/AUX dont
infover contient ind, sub, cnd ou imp. Le 17.10.2026, lexique.org ne livrait pas le fichier
depuis le box (HTTP 200 sans corps, puis 503) ; la liste versionnée vient donc du conjugueur
ci-dessous, appliqué aux lemmes de tools/audit/verbes_lemmes.txt (lemmes VERB/AUX relevés par
spaCy fr_core_news_sm dans TIP, NOT et GES, 2 occurrences au moins) et à une table d'irréguliers.
Participes et infinitifs sont exclus : ils ne sont pas conjugués.
"""
import gzip, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
# Mots-outils jamais comptés comme verbes, même si un lemme fautif les engendrait.
MOTS_OUTILS = set('le la les l de des du un une et ou en au aux ce ces cet cette sa son ses se sur par pour dans avec sans '
                  'sous entre mais donc car ni ne pas plus très que qui quoi dont où il elle ils elles on nous vous leur leurs '
                  'lui me te mon ma mes ton ta tes notre nos votre vos y si tout tous toute toutes'.split())
P = ('je', 'tu', 'il', 'nous', 'vous', 'ils')


def er(v):
    r = v[:-2]
    alt = {r}
    if r.endswith('c'):
        alt.add(r[:-1] + 'ç')
    if r.endswith('g'):
        alt.add(r + 'e')
    for a, b in (('é', 'è'), ('e', 'è')):  # céder → cède, lever → lève
        i = r.rfind(a)
        if i >= 0:
            alt.add(r[:i] + b + r[i + 1:])
    if r.endswith(('el', 'et')):
        alt.add(r + r[-1])
    if r.endswith('y'):
        alt.add(r[:-1] + 'i')
    f = set()
    for s in alt:
        f |= {s + x for x in ('e', 'es', 'ent', 'ons', 'ez', 'ais', 'ait', 'ions', 'iez', 'aient', 'ai', 'as', 'a',
                              'âmes', 'âtes', 'èrent', 'ât', 'asse', 'assent')}
        f |= {s + 'er' + x for x in ('ai', 'as', 'a', 'ons', 'ez', 'ont', 'ais', 'ait', 'ions', 'iez', 'aient')}
        f |= {s + 'er' + x for x in ('ai', 'as', 'a', 'ons', 'ez', 'ont', 'ais', 'ait', 'ions', 'iez', 'aient')}
        f |= {s + 'èr' + x for x in ('ai', 'a', 'ont', 'ait', 'aient')}
    return f


def ir2(v):  # finir
    r = v[:-2]
    return {r + x for x in ('is', 'it', 'issons', 'issez', 'issent', 'issais', 'issait', 'issions', 'issiez',
                            'issaient', 'isse', 'isses', 'irent', 'ît', 'irai', 'iras', 'ira', 'irons', 'irez',
                            'iront', 'irais', 'irait', 'irions', 'iriez', 'iraient')}


def gen(pres, imp, fut, ps='i', subj=None):
    """pres = (sg1, sg3, pl1 radical, pl3) ; imp = radical d'imparfait ; fut = radical de futur."""
    s1, s3, p1, p3 = pres
    f = {s1, s1[:-1] + 's' if s1.endswith('x') else s1, s3, p1 + 'ons', p1 + 'ez', p3}
    f |= {imp + x for x in ('ais', 'ait', 'ions', 'iez', 'aient')}
    f |= {fut + x for x in ('ai', 'as', 'a', 'ons', 'ez', 'ont', 'ais', 'ait', 'ions', 'iez', 'aient')}
    sb = subj or p3[:-3]
    f |= {sb + x for x in ('e', 'es', 'ent')} | {imp + x for x in ('ions', 'iez')}
    return {x for x in f if x}


def ir3(v):  # partir, dormir, sentir, servir, sortir, mentir
    r = v[:-2]
    return gen((r[:-1] + 's', r[:-1] + 't', r, r + 'ent'), r, v[:-1] + 'r') | {r + 'it', r + 'irent'}


def vrir(v):  # ouvrir, couvrir, offrir, souffrir
    r = v[:-2]
    return er(r + 'er') - {r + 'er' + x for x in ('ai', 'as', 'a')} | gen((r + 'e', r + 'e', r, r + 'ent'), r, v + '') | {r + 'it', r + 'irent'}


def re_reg(v):  # attendre, répondre, perdre, rompre
    r = v[:-2]
    return gen((r + 's', r if r.endswith(('d', 'p')) else r + 't', r, r + 'ent'), r, r + 'r') | {r + 'it', r + 'irent', r + 't'}


def uire(v):  # conduire, réduire, produire
    r = v[:-2]
    return gen((r + 's', r + 't', r + 's', r + 'sent'), r + 's', v[:-1]) | {r + 'sit', r + 'sirent'}


def indre(v):  # craindre, atteindre, joindre, peindre
    r = v[:-4]
    return gen((r + 'ns', r + 'nt', r + 'gn', r + 'gnent'), r + 'gn', v[:-1]) | {r + 'gnit', r + 'gnirent'}


def aitre(v):  # connaître, paraître
    r = v[:-4]
    return gen((r + 'is', r + 'ît', r + 'iss', r + 'issent'), r + 'iss', v[:-1]) | {r[:-1] + 'ut', r[:-1] + 'urent', r + 'it'}


def cevoir(v):
    r = v[:-6]
    return gen((r + 'çois', r + 'çoit', r + 'cev', r + 'çoivent'), r + 'cev', r + 'cevr', subj=r + 'çoiv') | {r + 'çut', r + 'çurent'}


IRR = {
    'être': {'suis', 'es', 'est', 'sommes', 'êtes', 'sont', 'étais', 'était', 'étions', 'étiez', 'étaient', 'serai',
             'seras', 'sera', 'serons', 'serez', 'seront', 'serais', 'serait', 'serions', 'seriez', 'seraient', 'sois',
             'soit', 'soyons', 'soyez', 'soient', 'fus', 'fut', 'fûmes', 'furent', 'fût', 'fussent'},
    'avoir': {'ai', 'as', 'a', 'avons', 'avez', 'ont', 'avais', 'avait', 'avions', 'aviez', 'avaient', 'aurai', 'auras',
              'aura', 'aurons', 'aurez', 'auront', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient', 'aie', 'aies',
              'ait', 'ayons', 'ayez', 'aient', 'eus', 'eut', 'eurent', 'eût'},
    'aller': gen(('vais', 'va', 'all', 'vont'), 'all', 'ir', subj='aill') | {'vas', 'alla', 'allèrent', 'va'},
    'faire': gen(('fais', 'fait', 'fais', 'font'), 'fais', 'fer', subj='fass') | {'faites', 'fit', 'firent'},
    'dire': gen(('dis', 'dit', 'dis', 'disent'), 'dis', 'dir') | {'dites', 'dirent'},
    'pouvoir': gen(('peux', 'peut', 'pouv', 'peuvent'), 'pouv', 'pourr', subj='puiss') | {'puis', 'put', 'purent'},
    'devoir': gen(('dois', 'doit', 'dev', 'doivent'), 'dev', 'devr', subj='doiv') | {'dut', 'durent'},
    'vouloir': gen(('veux', 'veut', 'voul', 'veulent'), 'voul', 'voudr', subj='veuill') | {'voulut'},
    'savoir': gen(('sais', 'sait', 'sav', 'savent'), 'sav', 'saur', subj='sach') | {'sut', 'surent'},
    'falloir': {'faut', 'fallait', 'faudra', 'faudrait', 'faille', 'fallut'},
    'valoir': gen(('vaux', 'vaut', 'val', 'valent'), 'val', 'vaudr', subj='vaill') | {'valut'},
    'voir': gen(('vois', 'voit', 'voy', 'voient'), 'voy', 'verr', subj='voi') | {'vit', 'virent'},
    'prévoir': gen(('prévois', 'prévoit', 'prévoy', 'prévoient'), 'prévoy', 'prévoir', subj='prévoi') | {'prévit'},
    'croire': gen(('crois', 'croit', 'croy', 'croient'), 'croy', 'croir', subj='croi') | {'crut'},
    'boire': gen(('bois', 'boit', 'buv', 'boivent'), 'buv', 'boir', subj='boiv') | {'but'},
    'vivre': gen(('vis', 'vit', 'viv', 'vivent'), 'viv', 'vivr') | {'vécut'},
    'suivre': gen(('suis', 'suit', 'suiv', 'suivent'), 'suiv', 'suivr') | {'suivit', 'suivirent'},
    'lire': gen(('lis', 'lit', 'lis', 'lisent'), 'lis', 'lir') | {'lut'},
    'écrire': gen(('écris', 'écrit', 'écriv', 'écrivent'), 'écriv', 'écrir') | {'écrivit'},
    'mettre': gen(('mets', 'met', 'mett', 'mettent'), 'mett', 'mettr') | {'mit', 'mirent'},
    'prendre': gen(('prends', 'prend', 'pren', 'prennent'), 'pren', 'prendr', subj='prenn') | {'prit', 'prirent'},
    'venir': gen(('viens', 'vient', 'ven', 'viennent'), 'ven', 'viendr', subj='vienn') | {'vint', 'vinrent'},
    'tenir': gen(('tiens', 'tient', 'ten', 'tiennent'), 'ten', 'tiendr', subj='tienn') | {'tint', 'tinrent'},
    'courir': gen(('cours', 'court', 'cour', 'courent'), 'cour', 'courr') | {'courut'},
    'mourir': gen(('meurs', 'meurt', 'mour', 'meurent'), 'mour', 'mourr') | {'mourut'},
    'acquérir': gen(('acquiers', 'acquiert', 'acquér', 'acquièrent'), 'acquér', 'acquerr') | {'acquit'},
    'naître': gen(('nais', 'naît', 'naiss', 'naissent'), 'naiss', 'naîtr') | {'naquit'},
    'plaire': gen(('plais', 'plaît', 'plais', 'plaisent'), 'plais', 'plair') | {'plut'},
    'rire': gen(('ris', 'rit', 'ri', 'rient'), 'ri', 'rir'),
    'fuir': gen(('fuis', 'fuit', 'fuy', 'fuient'), 'fuy', 'fuir', subj='fui'),
    'asseoir': gen(('assieds', 'assied', 'assey', 'asseyent'), 'assey', 'assiér'),
    'résoudre': gen(('résous', 'résout', 'résolv', 'résolvent'), 'résolv', 'résoudr') | {'résolut'},
    'vaincre': gen(('vaincs', 'vainc', 'vainqu', 'vainquent'), 'vainqu', 'vaincr'),
    'battre': gen(('bats', 'bat', 'batt', 'battent'), 'batt', 'battr'),
    'extraire': gen(('extrais', 'extrait', 'extray', 'extraient'), 'extray', 'extrair', subj='extrai'),
    'suffire': gen(('suffis', 'suffit', 'suffis', 'suffisent'), 'suffis', 'suffir') | {'suffit'},
    'interdire': gen(('interdis', 'interdit', 'interdis', 'interdisent'), 'interdis', 'interdir'),
    'conclure': gen(('conclus', 'conclut', 'conclu', 'concluent'), 'conclu', 'conclur'),
    'inclure': gen(('inclus', 'inclut', 'inclu', 'incluent'), 'inclu', 'inclur'),
    'exclure': gen(('exclus', 'exclut', 'exclu', 'excluent'), 'exclu', 'exclur'),
    'coudre': gen(('couds', 'coud', 'cous', 'cousent'), 'cous', 'coudr'),
}
PREF = {'venir': 'venir', 'tenir': 'tenir', 'prendre': 'prendre', 'mettre': 'mettre', 'faire': 'faire',
        'voir': 'voir', 'suivre': 'suivre', 'écrire': 'écrire', 'courir': 'courir', 'battre': 'battre',
        'dire': 'dire', 'traire': 'extraire', 'crire': 'écrire', 'soudre': 'résoudre', 'vivre': 'vivre', 'naître': 'naître', 'quérir': 'acquérir'}


def forms_of(v):
    if v in IRR:
        return IRR[v]
    if v.endswith('cevoir'):
        return cevoir(v)
    for base, model in PREF.items():  # survenir, maintenir, comprendre, admettre, défaire, revoir…
        if v.endswith(base) and v != base:
            pre = v[:-len(base)]
            mdl = IRR[model]
            if model in ('extraire', 'acquérir', 'écrire', 'résoudre'):
                stem = model[:-len(base)]
                return {pre + f[len(stem):] for f in mdl if f.startswith(stem)}
            return {pre + f for f in mdl}
    if v.endswith('cevoir'):
        return cevoir(v)
    if v.endswith('er'):
        return er(v)
    if v.endswith(('vrir', 'frir')):
        return vrir(v)
    if v.endswith(('partir', 'sortir', 'sentir', 'dormir', 'servir', 'mentir')):
        return ir3(v) | ir2(v)
    if v.endswith('ir'):
        return ir2(v)
    if v.endswith('uire'):
        return uire(v)
    if v.endswith(('aindre', 'eindre', 'oindre')):
        return indre(v)
    if v.endswith('aître'):
        return aitre(v)
    if v.endswith(('dre', 'pre')):
        return re_reg(v)
    return set()


def lexique(path):
    out = set()
    with open(path, encoding='utf-8') as f:
        head = f.readline().rstrip('\n').split('\t')
        i_o, i_c, i_v = head.index('ortho'), head.index('cgram'), head.index('infover')
        for l in f:
            c = l.rstrip('\n').split('\t')
            if c[i_c] in ('VER', 'AUX') and any(t in c[i_v] for t in ('ind:', 'sub:', 'cnd:', 'imp:')):
                out.add(c[i_o])
    return out


def main():
    lx = os.path.join(ROOT, '.cache', 'lexique', 'Lexique383.tsv')
    if os.path.exists(lx):
        forms, src = lexique(lx), 'Lexique 3.83 (CC BY-SA 4.0)'
    else:
        lemmes = {l.strip() for l in open(os.path.join(HERE, 'verbes_lemmes.txt'), encoding='utf-8')
                  if len(l.strip()) >= 4 and not l.startswith('#')}
        lemmes |= set(IRR)
        forms = set()
        for v in sorted(lemmes):
            forms |= forms_of(v)
        src = f'conjugueur interne, {len(lemmes)} lemmes'
    forms = sorted(f for f in forms if f.isalpha() and f not in MOTS_OUTILS)
    out = os.path.join(HERE, 'verbes_conjugues.txt.gz')
    with gzip.GzipFile(out, 'wb', mtime=0) as g:  # mtime=0 : sortie reproductible
        g.write(('# ' + src + '\n' + '\n'.join(forms) + '\n').encode('utf-8'))
    print(f'{len(forms)} formes conjuguées ({src}) → {os.path.relpath(out, ROOT)}')


if __name__ == '__main__':
    sys.exit(main())
