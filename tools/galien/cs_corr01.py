"""Galien · corrections de niveau 2 des 5 stations CS pilotes (PR #40), 17.10.2026. Rejouable sur data/cs/stations.json."""
import json, sys
P = 'data/cs/stations.json'
S = json.load(open(P))
st = {s['ssp']: s for s in S}
# G6 : la réponse à l'antipyrétique ne trie pas la gravité ; seule la réévaluation sans fièvre compte.
g = next(i for i in st['G6']['grille']['management'] if i['t'].startswith('Il utilise la réponse au paracétamol'))
g['t'] = 'Il réévalue l’enfant une fois la fièvre baissée, en particulier la fréquence cardiaque et le comportement, sans tirer de la seule baisse de la fièvre une conclusion sur la gravité.'
g['pourquoi'] = 'Une tachycardie ou une léthargie qui persistent quand la fièvre a baissé restent des signes d’alarme, alors que la baisse de la fièvre sous antipyrétique se voit aussi dans les infections graves et ne permet donc pas de les écarter.'
st['G6']['a_verifier'].append('Galien (17.10.2026) : l’affirmation que la réponse à l’antipyrétique ne distingue pas une infection grave d’une infection bénigne reste à relire dans une source suisse ou européenne (le merkblatt du Kinderspital Zürich, rubrique Antipyretika, la nuance-t-il ?).')
# S2.5 : STEMI inférieur sans dérivations droites ni prudence avec les dérivés nitrés.
m = st['S2.5']['grille']['management']
if not any('V4R' in i['t'] for i in m):
    k = next(n for n, i in enumerate(m) if i['t'].startswith('Il reconnaît le sus-décalage'))
    m.insert(k + 1, {'t': 'Devant un infarctus inférieur, il fait enregistrer les dérivations droites (V3R et V4R) à la recherche d’une extension au ventricule droit, et il évite alors les dérivés nitrés.',
                     'pts': 1, 'pourquoi': 'Le ventricule droit infarci dépend de sa précharge : un dérivé nitré, qui la réduit, peut provoquer une hypotension sévère.',
                     'hyp': ['sca'], 'src': [{'id': 'R-ESC-SCA', 'loc': '§ 3.2 (dérivations supplémentaires), tel que repris dans la chaîne hyp|sca', 'lu_le': '2026-10-17'}]})
    st['S2.5']['a_verifier'].append('Galien (17.10.2026) : la recommandation des dérivations V3R et V4R dans l’infarctus inférieur et la prudence avec les dérivés nitrés restent à relire dans le texte intégral de l’ESC 2023.')
open(P, 'w').write(json.dumps(S, ensure_ascii=False, indent=1))
print('2 corrections CS appliquées')
