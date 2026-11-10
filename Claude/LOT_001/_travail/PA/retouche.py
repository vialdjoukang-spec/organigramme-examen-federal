#!/usr/bin/env python3
"""Résout les marqueurs [[DROPk]] (phrases non vérifiables) : remplacement sourcé à la main ou suppression."""
import re, glob, json, sys
D = 'Claude/LOT_001/_travail/PA/'
perdus = open(D + 'HELP_perdus.txt').read().split('\n')
def c(*ids): return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
REP = [
 ("Une sudation focale, bilatérale, idiopathique", "Une sudation focale, bilatérale, idiopathique et gênante."),
 ("318 cas déclarés en 2024, soit 3,5/100 000", "318 cas déclarés en 2024, soit 3,5 pour 100 000 habitants" + c('wad7cf6-26')),
 ("La ménopause naturelle survient vers 51 ans", "La ménopause naturelle survient en moyenne à l'âge de 51 ans" + c('w223dbe-2')),
 ("Chaque dénominateur diffère", "Chaque dénominateur diffère, donc la lecture classe les diagnostics différentiels sans fusionner ces chiffres."),
 ("Électrocardiogramme (ECG) 12 dérivations", "Électrocardiogramme (ECG) et troponine sériée"),
 ("Traitement oncohématologique selon", "Traitement oncohématologique spécialisé"),
 ("Prise en charge spécialisée et chirurgie", "Prise en charge spécialisée et chirurgie"),
 ("Traitement étiologique qui réduit", "Traitement étiologique qui réduit la production ou le tissu fonctionnel"),
 ("Le fézolinétant (VEOZA®, n° 69232)", "Le fézolinétant (VEOZA®) antagonise le récepteur NK3 ; la dose recommandée est de 45 mg une fois par jour" + c('aips-69232-2') + " ; ses contre-indications figurent au point 11.B."),
 ("Cas déclarés en 2024 : 318", "Cas déclarés en 2024 : 318, soit 3,5 pour 100 000" + c('wad7cf6-26')),
 ("Le médecin hospitalise ; en choc", "Le médecin hospitalise le patient."),
 ("La clinique tranche (4 des 7", "La clinique tranche ; le test de Minor cartographie la zone."),
 ("Les métanéphrines libres tranchent ; au-delà", "Les métanéphrines libres tranchent ; l'imagerie localise ensuite la tumeur."),
 ("Le pouls bat régulièrement entre 60", "Le pouls bat régulièrement et les mains restent stables."),
 ("Une tachycardie > 100/min", "Une tachycardie, un pouls irrégulier ou un tremblement fin nouveau font demander glycémie, ECG ou bilan thyroïdien selon le contexte."),
 ("7.6 Adrénergique par accès (DX.10)", "7.6 Adrénergique par accès (DX.10)"),
 ("7.8 Sudoral local, déficitaire ou qualitatif", "7.8 Sudoral local, déficitaire ou qualitatif (DX.4)"),
 ("Il note une échelle de 0 à 10", "Il note une échelle d'intensité au suivi."),
 ("La clinique (anamnèse et examen) sert de référence", "La clinique (anamnèse et examen) sert de référence."),
 ("Aucun débit universel n'existe", "Aucun débit universel n'existe."),
 ("Objectif de correction > 4,0", "Si la glycémie reste inférieure à 4 mmol/L après l'apport de glucides, le médecin corrige à nouveau" + c('w04c5a2-4')),
 ("TSH basse → test réflexe fT4", "Si la TSH est basse, le test réflexe mesure la fT4 (référence adulte 12,0–22,0 pmol/L)" + c('w064a12-4') + " et la T3 libre (3,1–6,8 pmol/L)" + c('w9962bf-3')),
 ("LUKS adulte : leucocytes", "Valeurs adultes du laboratoire de Lucerne : leucocytes 3,7–9,2 G/L, hémoglobine 118–152 g/L chez la femme et 134–170 g/L chez l'homme, thrombocytes 150–380 G/L" + c('w53ba8a-3') + ", CRP < 5 mg/L" + c('w21f59e-3')),
 ("Cytopénie, anémie ou CRP à 20", "Une cytopénie, une anémie ou une CRP élevée sont des signaux non spécifiques."),
 ("Métanéphrines urinaires de 24 h", "Métanéphrines urinaires collectées sur la journée entière"),
 ("Métanéphrines libres plasmatiques après", "Métanéphrines libres plasmatiques prélevées en décubitus, à jeun, sans effort, sur glace"),
 ("Un PPGL sécrétant devient très improbable", "Un PPGL sécrétant devient très improbable."),
 ("Un seul métabolite > limite", "Un seul métabolite à peine au-dessus de la limite"),
 ("Un métabolite > 2 fois la limite", "Un métabolite très élevé ou plusieurs métabolites élevés"),
 ("Probabilité qui justifie la localisation", "Probabilité qui justifie la localisation."),
 ("Le document de l'Inselspital", "Le laboratoire de l'Inselspital applique l'algorithme de l'ESC à 0 et 1 heure pour la troponine T" + c('w318537-85') + "."),
 ("Exclusion biologique : valeur initiale", "Pour l'exclusion biologique, il retient une valeur initiale < 5 ng/L chez un patient douloureux depuis plus de 3 h, ou < 12 ng/L avec une variation à 1 h < 3 ng/L" + c('w318537-85') + "."),
 ("Forte probabilité : valeur initiale", "Pour la forte probabilité, il retient une valeur initiale ≥ 52 ng/L ou une variation à 1 h ≥ 5 ng/L" + c('w318537-85') + "."),
 ("6. 🚩 E5", "🚩 E5 : risque d'acquisition du VIH ou primo-infection compatible"),
 ("7. 🚩 E6", "🚩 E6 : adénopathie ou masse avec symptômes généraux"),
 ("8. 🚩 E7", "🚩 E7 : accès de céphalées, palpitations et sueurs ou risque de PPGL"),
 ("→ le médecin dose les métanéphrines", "→ le médecin dose les métanéphrines ; une valeur nettement au-dessus de la limite fait demander la localisation."),
 ("Des bouffées avec cycles modifiés après 45", "Des bouffées avec cycles modifiés"),
 ("Il pose un diagnostic clinique → DX.5", "Il pose un diagnostic clinique → DX.5 ; devant des signes atypiques, il revient à la recherche des causes graves."),
 ("La DDG décrit des séances initiales", "La DDG décrit des séances de 20-30 minutes plusieurs fois par semaine" + c('w8deb59-34') + "."),
 ("La notice Saalio", "La notice de l'appareil Saalio contre-indique le traitement chez les porteurs d'un stimulateur cardiaque ou d'un défibrillateur implanté, ainsi que pendant la grossesse et l'allaitement" + c('wb20388-24') + "."),
 ("Symptômes vasomoteurs de la ménopause : 45 mg", "Symptômes vasomoteurs de la ménopause : 45 mg une fois par jour ; dose maximale 45 mg par jour" + c('aips-69232-2')),
 ("Protocole HUG du 02.09.2022", "Le protocole HUG corrige avec 15 g de glucides si la glycémie est inférieure à 4 mmol/L et avec 30 g si elle est inférieure à 2,5 mmol/L (aliments courants, pas des doses AIPS)" + c('w04c5a2-2', 'w04c5a2-3')),
 ("Recontrôle après 20–30 min", "Il refait une glycémie 20 à 30 minutes après l'apport ; si elle reste inférieure à 4 mmol/L, il corrige à nouveau avec 15 à 30 g de glucides" + c('w04c5a2-3')),
 ("Réponse attendue dans les 10 min", "Réponse attendue dans les 10 minutes" + c('aips-31489-5') + " ; phéochromocytome exclu"),
 ("Aucune dose adulte ou vésicale", "Aucune dose adulte ou vésicale n'est transposée."),
 ("Un HDSS de 4 ne prouve", "Un score HDSS élevé ne prouve pas qu'une technique est remboursée."),
 ("Chaque réponse s'appuie sur les points", "Chaque réponse s'appuie sur les points précédents."),
 ("Non, elle en reçoit 50", "Non, elle en reçoit 50" + c('aips-52433-51')),
 ("Il reçoit 0,5 mg SC ou IM", "Il reçoit 0,5 mg par voie sous-cutanée ou intramusculaire" + c('aips-31489-4')),
 ("L'AIPS prévoit 0,5 mg sous 25 kg", "L'AIPS prévoit 0,5 mg chez l'enfant de moins de 25 kg ou de moins de 6 à 8 ans" + c('aips-31489-4')),
 ("L'information professionnelle (IP) suisse lue le", "L'information professionnelle suisse limite l'indication à l'adulte" + c('aips-69243-1')),
]
def rep(k):
    p = perdus[k]
    for pre, new in REP:
        if p.startswith(pre): return new
    return ''
if __name__ == '__main__':
    non = set()
    for f in sorted(glob.glob(D + 'fragments/p*.html')):
        t = open(f).read()
        def sub(m):
            return rep(int(m.group(1)))
        t = re.sub(r'\[\[DROP(\d+)\]\]', sub, t)
        t = re.sub(r'<td([^>]*)>\s*</td>', r'<td\1>—</td>', t)
        t = re.sub(r'<li>\s*</li>', '', t)
        t = re.sub(r'<div class="p">\s*</div>\n?', '', t)
        open(f, 'w').write(t)
