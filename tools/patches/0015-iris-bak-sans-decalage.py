import os, sys
# Patch 0015 · Iris · 17.10.2026 · CLS de l'accueil sur la CI (0,437 > 0,192 depuis #24/#28).
# Cause : le bandeau de sauvegarde #bak est peint vide (≈102 px), puis bakShow(), exécuté à la fin d'un script
# devenu plus long, y écrit l'avertissement « jamais exportée » (≈170 px) après la première peinture : tout
# le panneau du calendrier descend (source n° 1 des layout-shift). Correctif : l'état initial du bandeau
# (classe warn et texte du premier lancement) est écrit dans le HTML ; bakShow() le remplace à l'identique
# pour un premier lancement. De même, le bouton #sv-fb (masqué dans le HTML) n'était démasqué par svFileBtn()
# qu'à la fin du script, ce qui rétrécissait le texte voisin : un court script en ligne, placé juste après le
# bouton, applique le même test (showSaveFilePicker) avant la première peinture. Enfin, #kpis (en-tête) était
# vide (0 px) jusqu'au rendu des 6 indicateurs (66 px) : il reçoit dans le HTML les 6 mêmes cartes, valeurs « – »,
# que le rendu remplace à géométrie identique (même grille auto-fit, mêmes libellés). Les réglages d'affichage
# (#d-gv, #d-fv vides, curseurs à leur milieu) reçoivent leurs valeurs par défaut de applyDisp() (50 %, 100 %). Seuils et référence inchangés.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

T = ('Votre progression vit seulement dans ce navigateur, et vous ne l’avez encore jamais exportée. '
     'Exportez-la chaque semaine, car Safari peut effacer ce stockage après sept jours sans visite.')
assert s.count(T) == 1, 'Texte du premier lancement absent de bakShow'
rep('<div class="bak" id="bak" role="region" aria-label="Sauvegarde de la progression"><p id="bak-t" role="status"></p>',
    '<div class="bak warn" id="bak" role="region" aria-label="Sauvegarde de la progression"><p id="bak-t" role="status">' + T + '</p>')

rep('<button class="b" id="sv-fb" type="button" hidden>Activer un fichier de sauvegarde automatique</button>',
    '<button class="b" id="sv-fb" type="button" hidden>Activer un fichier de sauvegarde automatique</button>'
    "<script>document.getElementById('sv-fb').hidden=typeof window.showSaveFilePicker!=='function'</script>")

K = [['SSP couverts (CK lu)'], ['couverture'], ['temps de lecture'], ['séances accomplies'], ['moyenne/jour (14 j)'], ['jours avant le CK']]
rep('<div class="kpis" id="kpis"></div>',
    '<div class="kpis" id="kpis">' + ''.join('<div class="kpi"><b>–</b><span>' + k[0] + '</span></div>' for k in K) + '</div>')

rep('id="d-gilt" min="0" max="100" step="5" tabindex="-1" aria-label="Fond doré (réglage retiré)"> <b id="d-gv"></b>',
    'id="d-gilt" min="0" max="100" step="5" value="50" tabindex="-1" aria-label="Fond doré (réglage retiré)"> <b id="d-gv">50 %</b>')
rep('<input type="range" id="d-fs" min="90" max="130" step="5"> <b id="d-fv"></b>',
    '<input type="range" id="d-fs" min="90" max="130" step="5" value="100"> <b id="d-fv">100 %</b>')

open(p, 'w', encoding='utf-8').write(s)
print('0015 appliqué')
