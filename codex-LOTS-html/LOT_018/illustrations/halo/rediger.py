"""Schéma original : lecture du halo temporal, trois vues conservées en JSON."""
import importlib.util
import json
from pathlib import Path

D = Path(__file__).resolve().parent
BASE = D.parents[2]
loader = importlib.util.spec_from_file_location('dessinateur', BASE / 'outils/dessinateur/dessinateur.py')
draw = importlib.util.module_from_spec(loader)
loader.loader.exec_module(draw)

def shape(tag, **attrs):
    return {'tag': tag, 'attrs': {k.replace('_', '-'): v for k, v in attrs.items()}}

def circle(radius, fill):
    return shape('ellipse', cx=360, cy=160, rx=radius, ry=radius, fill=fill)

def contour(d):
    return [shape('path', d=d, fill='none', stroke='#142633', stroke_width=7),
            shape('path', d=d, fill='none', stroke='#ffed69', stroke_width=3, stroke_dasharray='8 6')]

def leader(x1, y1, x2, y2):
    return shape('line', x1=x1, y1=y1, x2=x2, y2=y2, stroke='#142633', stroke_width=2)

def label(x, y, name, definition):
    return {'xy': [x, y], 'nom': name, 'definition': definition}

background = shape('rect', x=100, y=20, width=520, height=280, fill='#b8c3cb', rx=12)
spec = {
    'id': 'i018-halo-temporal',
    'titre': 'Artère temporale : comprendre le halo dans deux plans',
    'auteur': 'Codex — dessin original, CC BY 4.0 ; aucun cliché échographique reproduit',
    'source_medicale': 'https://www.lecofer.org/item-cours-1-16-0.php',
    'acces_le': '2026-10-31',
    'vues': [
        {
            'titre': '1. Coupe transversale de référence',
            'formes': [background, circle(88, '#e8edf0'), circle(76, '#d85b38'), leader(205, 65, 297, 100)],
            'reperes': [
                label(360, 160, 'Lumière artérielle', 'Centre orange : convention de remplissage Doppler, sans mesure de débit.'),
                label(205, 65, 'Paroi fine de référence', 'Anneau clair schématique ; son épaisseur dessinée ne définit pas un seuil normal.')
            ],
            'explication': 'Cette vue sert de comparaison anatomique. Les couleurs sont conventionnelles. Il ne s’agit ni d’une acquisition en mode B ni d’un Doppler réel.'
        },
        {
            'titre': '2. Coupe transversale : épaississement pariétal',
            'formes': [background, circle(110, '#253441'), circle(65, '#d85b38')]
                + contour('M245 160 a115 115 0 1 0 230 0 a115 115 0 1 0 -230 0')
                + [leader(535, 60, 430, 95)],
            'reperes': [
                label(360, 160, 'Lumière centrale', 'Le centre reste distinct de la paroi. Sa couleur représente un signal Doppler conventionnel.'),
                label(535, 60, 'Halo pariétal', 'L’anneau sombre figure une paroi épaissie, homogène et hypoéchogène. Les pointillés en délimitent le bord externe.')
            ],
            'explication': 'Le halo appartient à la paroi, pas au tissu autour du vaisseau. Un aspect évocateur doit être interprété avec la clinique et distingué notamment de l’athérome par un opérateur entraîné.'
        },
        {
            'titre': '3. Coupe longitudinale du segment représenté',
            'formes': [background,
                shape('rect', x=125, y=50, width=470, height=220, fill='#253441'),
                shape('rect', x=125, y=95, width=470, height=130, fill='#d85b38')]
                + contour('M125 50 H595 V95 H125 Z')
                + contour('M125 225 H595 V270 H125 Z')
                + [leader(60, 73, 260, 73), leader(660, 247, 460, 247)],
            'reperes': [
                label(360, 160, 'Lumière longitudinale', 'Couloir orange central, bordé par les deux parois du segment.'),
                label(60, 73, 'Paroi superficielle épaissie', 'Bande sombre du haut : représentation longitudinale de la même paroi inflammatoire.'),
                label(660, 247, 'Paroi profonde épaissie', 'Bande sombre du bas : l’autre bord de la paroi coupée dans son axe. Les deux contours encadrent les bandes représentées.')
            ],
            'explication': 'Vérifier l’anomalie dans les deux plans. Le dessin ne décrit pas l’étendue réelle de la maladie. Une échographie négative ne suffit pas à exclure une ACG lorsque la suspicion clinique reste forte ; poursuivre le bilan spécialisé.'
        }
    ]
}
(D / 'temporal.json').write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n')
caption = (' <a href="https://catalogue.chuv.ch/miajour/comptes-rendus/fiche/mia_review_141/avant-la-biopsie-evaluer-lechodoppler-des-arteres-temporales-pour-le-diagnostic-de-larterite-a-cellules-geantes">CHUV : interprétation dans la démarche diagnostique</a>.'
           ' <a href="https://creativecommons.org/licenses/by/4.0/">Licence du dessin : CC BY 4.0</a>.')
(D / 'temporal.html').write_text(draw.render(spec).replace('</figcaption>', caption + '</figcaption>'))
print('Trois vues générées ; inspection visuelle à effectuer.')
