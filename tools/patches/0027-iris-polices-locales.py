import os, sys
# Patch 0027 · Iris · 17.10.2026 · CLS de l'accueil instable sur la CI (0,06 à 0,17 selon l'exécution, « visuel » rouge
# sur les demandes de fusion des monographies, qui ne touchent pas app_v2.html).
# Cause : Inter, Fraunces et JetBrains Mono venaient du CDN Google (font-display:swap). Sur le runner, qui n'a pas ces
# polices, la première peinture se fait en DejaVu Sans ; quand Inter arrive, le texte du bandeau #bak se replie
# sur une ligne de plus (+17 px) et les onglets et le calendrier descendent : layout-shift de 0,134, présent ou non
# selon que la police arrive avant ou après la première peinture. Reproduit à l'identique (0,1697) sans les polices
# système de la box (FONTCONFIG_FILE). Correctif : les mêmes fichiers woff2 (mêmes versions, mêmes plages unicode)
# sont servis depuis assets/fonts/ (licence OFL jointe), les sous-ensembles latins préchargés : la police est prête
# avant la première peinture, en file:// comme sur Pages, et l'application ne dépend plus d'un tiers. Rendu inchangé.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()
A = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;'
     '0,9..144,700;1,9..144,600&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">')
assert s.count(A) == 1, 'Ancrage absent ou répété : lien Google Fonts'
P = ''.join(f'<link rel="preload" href="assets/fonts/{n}-latin.woff2" as="font" type="font/woff2" crossorigin>'
            for n in ('inter', 'fraunces', 'fraunces-italic', 'jetbrainsmono'))
s = s.replace(A, P + '<link rel="stylesheet" href="assets/fonts/fonts.css">')
open(p, 'w', encoding='utf-8').write(s)
print('0027 appliqué')
