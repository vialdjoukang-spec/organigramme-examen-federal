#!/usr/bin/env python3
"""Galien · audit G4 prévalence (G6 fièvre, F1.19 syncope), 17.10.2026. Rejouable : extract NOT/TIP, ce script, inject, prev_build.
Chiffres vérifiés : Limper 2011 (Neth J Med 69:124-8, Résultats et tableau 2, n = 213) et BASEL IX (J Intern Med 2021,
Résultats : 665, 439, 252, 138 et 159 diagnostics adjugés, soit 1653 ; l'article donne 15,2 % pour 252, donc sur 1653).
1. F1.19, majeure (linguistique et structure) : les 8 fenêtres de différentiel affichaient chaque valeur sous l'intitulé suivant
   (« Examen déterminant : Bénigne », « Terrain : ECG, Holter », intitulé final vide) ; les intitulés sont remis en face de leur valeur.
2. F1.19, majeure : les syncopes cardiaques structurelles aiguës (SCA, dissection aortique, tamponnade) manquaient.
3. G6, majeure : l'angiocholite (3/213, 1,4 %, tableau 2) et les infections de la peau et des tissus mous (12/213, 5,6 %, Résultats) manquaient.
"""
import json, re
N = json.load(open('data/NOT.json')); T = json.load(open('data/TIP.json')); P = json.load(open('data/ck/prev.json'))
OLD = ['Signe distinctif', 'Urgence', 'Examen déterminant', 'Terrain', 'Prise en charge — but · moyens', '']
NEW = ['Mécanisme', 'Signe distinctif', 'Urgence', 'Examen déterminant', 'Terrain', 'Prise en charge — but · moyens']
for k, d in enumerate(T['F1.19']['d']):
    labs = re.findall(r'• <b>([^<]*)</b> :', d)
    if labs == OLD:
        it = iter(NEW)
        T['F1.19']['d'][k] = re.sub(r'• <b>[^<]*</b> :', lambda m: '• <b>' + next(it) + '</b> :', d)
def add(c, nom, d, item, vd=None):
    if nom not in N[c][0]:
        N[c][0].append(nom); T[c]['d'].append(d)
        if 'v' in T[c] and len(T[c]['v']['d']) == len(T[c]['d']) - 1: T[c]['v']['d'].append(vd or ['complété', []])
    i = N[c][0].index(nom); assert len(T[c]['d']) == len(N[c][0])
    it = P[c]['items']
    if not any(e['i'] == i for e in it):
        e = dict(i=i, nom=nom, **item)
        if e.get('rang') is None: e['rang'] = max(x['rang'] for x in it) + 1
        it.append(e)
NOMS = 'Syncope cardiaque structurelle aiguë (syndrome coronarien aigu, dissection aortique, tamponnade)'
for e in P['F1.19']['items']:
    if e['rang'] >= 6: e['rang'] += 1
add('F1.19', NOMS,
    '<b style="color:var(--bad)">À ne pas manquer.</b><br>'
    "• <b>Mécanisme</b> : Chute brutale du débit cardiaque par ischémie, obstacle ou compression du cœur.<br>"
    "• <b>Signe distinctif</b> : Syncope avec douleur thoracique, dorsale ou dyspnée, asymétrie tensionnelle, turgescence jugulaire.<br>"
    "• <b>Urgence</b> : URGENCE.<br>"
    "• <b>Examen déterminant</b> : ECG en 10 minutes, troponine, échocardiographie au lit, angio-TDM si dissection suspectée.<br>"
    "• <b>Terrain</b> : Sujet âgé, hypertension, cardiopathie connue.<br>"
    "• <b>Prise en charge — but · moyens</b> : Surveillance monitorée et traitement de la cause ; but : prévenir la mort subite.<br>",
    dict(prev_pct=None, type='consultation', rang=6, statut='À vérifier',
         note="Elle fait partie des syncopes cardiaques (252 sur 1653, soit 15,2 %) de BASEL IX, qui ne détaille pas leurs causes ; "
              "la ligne directrice ESC 2018 de la syncope range l'ischémie aiguë, la dissection aortique et la tamponnade parmi les syncopes cardiaques. Aucune fréquence propre n'est encore sourcée."))
if 'syncope' not in T['F1.19']['s'].lower():
    T['F1.19']['s'] = (T['F1.19']['s'] + ' · ' if T['F1.19']['s'] else '') + 'ESC 2018 — Guidelines for the diagnosis and management of syncope'
LOC2, LOCR = 'Tableau 2 (Bacterial infections, Cholangitis n = 3)', 'Résultats, § Infections (skin infections, 12 patients)'
add('G6', 'Angiocholite aiguë',
    "<b style=\"color:var(--bad)\">À ne pas manquer.</b>\n• <b>Clinique</b> : fièvre avec frissons, ictère et douleur de l'hypocondre droit (triade de Charcot), souvent sur lithiase connue.\n"
    "• <b>Biologie</b> : cholestase (phosphatases alcalines, gamma-GT, bilirubine), syndrome inflammatoire ; hémocultures avant l'antibiotique.\n"
    "• <b>Imagerie</b> : échographie abdominale (dilatation des voies biliaires), puis cholangio-IRM ou échoendoscopie selon la probabilité.\n"
    "• <b>Ce qui confirme</b> : obstacle biliaire avec infection ; l'urgence tient au sepsis.\n"
    "• <b>Prise en charge</b> : antibiothérapie et drainage biliaire endoscopique (CPRE), en urgence si la forme est grave.",
    dict(prev_pct=1.4, type='consultation', src='R-LIMPER-NJM-2011', loc=LOC2, date_lu='2026-10-17',
         note='3 patients sur 213 avaient une angiocholite (K. pneumoniae 2 fois, E. faecalis 1 fois dans les hémocultures).'))
add('G6', 'Infection de la peau et des tissus mous (érysipèle, dermohypodermite)',
    "• <b>Clinique</b> : placard inflammatoire chaud, douloureux, à bords nets (érysipèle) ou diffus, souvent d'une jambe, avec porte d'entrée (intertrigo, plaie).\n"
    "• <b>Biologie</b> : syndrome inflammatoire ; hémocultures si la fièvre est élevée ou si le patient est fragile.\n"
    "• <b>Imagerie</b> : aucune dans la forme simple ; échographie ou IRM si un abcès ou une fasciite est suspecté.\n"
    "• <b>Ce qui confirme</b> : le diagnostic est clinique.\n"
    "• <b>Prise en charge</b> : antibiothérapie active sur le streptocoque, traitement de la porte d'entrée ; chirurgie en urgence si une fasciite nécrosante est suspectée (douleur disproportionnée, nécrose, choc).",
    dict(prev_pct=5.6, type='consultation', src='R-LIMPER-NJM-2011', loc=LOCR, date_lu='2026-10-17',
         note="12 patients sur 213 avaient une infection cutanée selon les Résultats ; le tableau 2 n'en compte que 3, ceux dont l'hémoculture isolait S. pyogenes."))
P['F1.19']['cadre'] = P['F1.19']['cadre'].rstrip('.') + " ; les pourcentages de l'article se rapportent aux 1653 diagnostics adjugés"
json.dump(N, open('data/NOT.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(T, open('data/TIP.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(P, open('data/ck/prev.json', 'w'), ensure_ascii=False, indent=1)
print('G4 corrigé')
