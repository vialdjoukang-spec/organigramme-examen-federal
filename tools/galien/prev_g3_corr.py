#!/usr/bin/env python3
"""Galien · audit G3 prévalence (S3.1 douleur abdominale aiguë), 17.10.2026. Rejouable : extract NOT/TIP, ce script, inject, prev_build.
Les 7 chiffres d'Asclépios sont exacts (OPTIMA, BMJ 2009, tableau 1, n = 1021). Fautes majeures : la liste omettait la
2e cause chiffrée (diverticulite aiguë, 118, 11,6 %), la catégorie la plus fréquente après l'appendicite (douleur abdominale
non spécifique, 183, 17,9 %) et les urgences gynécologiques (27, 2,6 %). Elles sont ajoutées en fin de liste (index 9 à 11).
"""
import json
C = 'S3.1'
L = 'Tableau 1 (Final diagnoses assigned by expert panel)'
ADD = [
 ('Diverticulite aiguë', 11.6, '118 patients sur 1021 avaient une diverticulite aiguë, 2e diagnostic de l’étude.',
  "• <b>Ce que c’est</b> : Inflammation d’un diverticule du côlon, le plus souvent sigmoïdien<br>"
  "• <b>Ce qui l’évoque</b> : Douleur de la fosse iliaque gauche, fièvre, défense localisée, sujet de plus de 50 ans<br>"
  "• <b>Examen clé</b> : Tomodensitométrie avec injection, qui confirme le diagnostic et recherche un abcès ou une perforation<br>"
  "• <b>Conduite</b> : Forme simple : traitement ambulatoire possible ; abcès ou perforation : hospitalisation, drainage ou chirurgie<br>"
  "• <b>Piège</b> : Une diverticulite du côlon droit ou d’un sigmoïde long, qui pend à droite, mime une appendicite<br>"),
 ('Douleur abdominale non spécifique', 17.9, '183 patients sur 1021 n’avaient aucune cause retrouvée à 6 mois ; c’est le diagnostic non urgent le plus fréquent de l’étude.',
  "• <b>Ce que c’est</b> : Douleur sans cause retrouvée après l’examen clinique, la biologie et l’imagerie : c’est un diagnostic d’exclusion<br>"
  "• <b>Ce qui l’évoque</b> : Constantes normales, examen rassurant, biologie sans syndrome inflammatoire<br>"
  "• <b>Examen clé</b> : Aucun examen ne le confirme ; on le retient seulement après avoir écarté les urgences<br>"
  "• <b>Conduite</b> : Antalgie, consignes écrites de reconsultation et réévaluation si la douleur persiste<br>"
  "• <b>Piège</b> : Le retenir sur la seule clinique : dans la grande étude néerlandaise des urgences, l’évaluation clinique seule manquait 12 % des urgences<br>"),
 ('Urgence gynécologique (torsion d’annexe, infection génitale haute, kyste ovarien rompu)', 2.6,
  '27 des 1021 patients avaient une urgence gynécologique : torsion d’annexe, infection génitale haute, kyste ovarien hémorragique ou rompu.',
  '<b style="color:var(--bad)">À ne pas manquer.</b><br>'
  "• <b>Ce que c’est</b> : Torsion d’annexe, infection génitale haute, kyste ovarien hémorragique ou rompu<br>"
  "• <b>Ce qui l’évoque</b> : Douleur pelvienne brutale avec nausées (torsion), fièvre et leucorrhées (infection)<br>"
  "• <b>Examen clé</b> : β-hCG d’abord, puis échographie pelvienne endovaginale<br>"
  "• <b>Conduite</b> : Torsion : cœlioscopie en urgence pour conserver l’ovaire ; infection : antibiothérapie<br>"
  "• <b>Piège</b> : Oublier la β-hCG, alors qu’une grossesse extra-utérine se présente de la même façon<br>"),
]
N = json.load(open('data/NOT.json')); T = json.load(open('data/TIP.json')); P = json.load(open('data/ck/prev.json'))
it = P[C]['items']
for nom, pct, note, d in ADD:
    if nom not in N[C][0]:
        N[C][0].append(nom); T[C]['d'].append(d)
    i = N[C][0].index(nom)
    if not any(e['i'] == i for e in it):
        it.append({'i': i, 'nom': nom, 'prev_pct': pct, 'type': 'consultation', 'src': 'R-OPTIMA-BMJ-2009', 'loc': L,
                   'date_lu': '2026-10-17', 'rang': max(e['rang'] for e in it) + 1, 'note': note})
assert len(T[C]['d']) == len(N[C][0])
for s in (' · ESCP 2020 — European Society of Coloproctology guidelines for the management of diverticular disease of the colon',
          ' · Laméris et al. — Imaging strategies for detection of urgent conditions in patients with acute abdominal pain, BMJ 2009'):
    if s not in T[C]['s']: T[C]['s'] += s
for e in it:
    if e['nom'] == 'Appendicite aiguë':
        e['note'] = '284 patients sur 1021 avaient une appendicite aiguë, le diagnostic le plus fréquent de l’étude.'
json.dump(N, open('data/NOT.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(T, open('data/TIP.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(P, open('data/ck/prev.json', 'w'), ensure_ascii=False, indent=1)
print('G3 corrigé')
