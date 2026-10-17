---
name: ssp-chaine-clinique
description: >-
  Lis ce skill avant d’écrire un contenu de la partie CK : geste, sémiologie,
  exploration par hypothèse, puis prise en charge, selon un gabarit fixe et des
  sources suisses ou européennes.
---
# But
Ce skill rend la partie CK concise, complète et identique d’un module à l’autre.
# Déclencheur
Tu l’appliques à toute entrée de `data/ck/syn.json`, `data/ck/hyp.json` ou `data/ck/nc.json`.
# Étapes
1. Geste (A) : temps, manœuvre ou test spécial, repris de GES ; chaque signe, syndrome ou terme spécialisé employé relève de ssp-signe-infobulle (glossaire imbriqué).
2. Sémiologie : signes et syndromes à rechercher, symptômes complémentaires à demander, orientation exploratoire et diagnostique.
3. Exploration, pour chaque hypothèse 1 à n : examen de référence dans ce contexte et ce qu’il recherche ; à défaut, 1re intention (pourquoi, en une phrase ; précautions), 2e intention, 3e si utile, chacune avec ce qu’elle recherche en quelques mots, et l’alternative en situation particulière (grossesse, insuffisance rénale, pacemaker, enfant).
4. Prise en charge si le diagnostic est confirmé : 1. objectif ; 2. mesures générales ; 3. moyens spécifiques (pharmacologiques, interventionnels, rééducation, suivi).
5. Sources : une société savante suisse d’abord (SSN, SSC, SSI, SSMI, Swiss Stroke Society…), sinon européenne (EAN, ESO, ESC, ERS, EULAR…), sinon une ligne directrice nationale européenne (DGN/AWMF, HAS) ; chaque élément porte `src` et `lu_le`. Sinon : « À vérifier ».
6. Toute dose relève de ssp-posologie-suisse ; une dose non lue dans l’AIPS reste « À vérifier », même si une ligne directrice la cite.
7. L’urgence vitale est la seule information en rouge.
# Interdits
Pas de source nord-américaine pour la prise en charge, pas de phrase nominale, pas de « gold standard » affirmé sans source qui le désigne comme tel.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
