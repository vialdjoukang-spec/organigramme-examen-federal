# Audit indépendant — mandat t498u — v3

## Verdict
**Prêt comme référentiel documentaire condensé, après corrections. Pas validé pour un usage clinique, juridique ou d'examen.** La fidélité documentaire contrôlée ne constitue pas une garantie médicale, ni une vérification des sources externes.

Périmètre : seul PDF de 38 pages, 867 251 octets, SHA-256 `b2a4434d2bf60ec4a93548b6c4151305c93617f23ab07ab7901fd365bb312833`. Les quatre pièces initiales restent hors périmètre, non relues par cet audit. Aucun accès GitHub ni dossier privé ; source et livraison_v2 intactes. Aucun appel HTTP.

## Défauts réels de la v2 et corrections
1. **Dermatologie, ligne 14 (pages 7–8)** : « SSDV / SGDV » avait glissé dans la spécialité et « HUG SMPR & » dans la liste Top 5. Cause : une ligne PDF traversant deux cellules était affectée entière par son centre. Réaffectation par centre de chaque caractère ; contrôle visuel de la page 7. La comparaison du producteur à sa propre extraction « 45/45 identiques » était vraie sur son intermédiaire, mais ne détectait pas ce défaut.
2. **Registre des libellés** : les grands rectangles englobants capturaient des caractères voisins (ex. « d'immuno ssai.ch/fr »). Registre reconstruit pour les 458 annotations à partir des QuadPoints et centres des caractères, avec fragments et coordonnées.
3. **Nuances de condensation** : rétabli « Ne pas débuter de dialyse chronique » (la v2 omettait « débuter »), et « 4 affirmations à juger chacune vraie ou fausse » pour K-prime. Ce sont des corrections de fidélité à la source, pas de nouvelles recommandations.
4. Corrigé l'identifiant interne resté « v1 ».
5. Dédupliqué les cibles répétées : références Markdown standard en §5. Les libellés qui répétaient une URL deviennent « accès »/« URL » ; leur libellé original et chaque transformation sont au registre. Réversibilité exacte vérifiée.

## Les liens coupés sont-ils complets ?
**Oui.** La v2 avait déjà les trois adresses intégrales ; son rapport « fragments préservés » était trop faible et ambigu. L'audit indépendant recolle les cellules sources aux coupures et confirme :
- p35–36 : `https://www.medix-romandie.ch/fr/medecins/guidelines-medix-suisse-acces-libre/`
- p33–34 : `https://www.unisante.ch/fr/consultations-medicales/professionnels-sante/recommandations-eviprev/tableau-eviprev`
- p36–37 : `https://www.fedlex.admin.ch/eli/cc/2008/832/fr`
Le quatrième cas, InfoVac, n'est pas une coupure de page : le texte `https://www.infovac.ch` et la cible `https://www.infovac.ch/` sont distincts et préservés. Rien n'a été inventé à partir des domaines affichés sans protocole. Les cibles query/fragment et les artefacts `%5Bspan_...` déjà présents dans le PDF restent littéraux, même suspects ou morts.

## Résultats contrôlés
| Contrôle | Résultat |
|---|---|
| Annotations PDF | 458/458 ; 223 URIs uniques ; zéro manquante |
| URLs complètes affichées, après recollage des cellules | 84 uniques ; toutes présentes dans le Markdown final |
| Liens Markdown | 497 occurrences → 238 définitions exactes ; aucun identifiant non résolu |
| Associations libellé/cible | 458 contrôlées géométriquement ; ponctuation périphérique tolérée ; abréviations URL réversibles |
| Tableau spécialités | 45 lignes × 5 cellules = 225 ; zéro différence après retrait des balises et normalisation des espaces |
| Architecture | §2.1–2.5 ; §3.1–3.3 (6, 8, 6 ressources) ; 52 citations ordonnées |
| Citations | 52 titres/URLs comparés indépendamment aux pages 37–38 ; zéro écart normalisé |
| Corpus | Aucun nouveau contenu clinique ; affirmations attribuées à la source |

La conformité des cellules est textuelle normalisée, non une validation de leur exactitude scientifique. Les paragraphes et tableaux reformulés du §2 ont été confrontés à la source ; les deux nuances ci-dessus ont été corrigées. Ce contrôle ne prouve pas mathématiquement une équivalence sémantique universelle.

## Utilité et économie : jugement honnête
Le résultat est utile : un index structuré de ressources, lisible sans PDF, avec les cibles auparavant cachées rendues exploitables. La condensation reste **conservatrice**, pas un résumé radical : les 45 lignes et toutes les ressources expliquent l'essentiel du volume.
- Markdown v2 : 106 979 octets ; Markdown v3 : **91,229 octets** (UTF-8).
- La seule factorisation des liens économise **15,959 octets / 14.89 %** par rapport à la version corrigée à liens en ligne (107,188 octets), sans perte vérifiée par aller-retour exact.
- Le texte brut extrait du PDF fait 96 894 octets. Le « ~20 % » de la v2 compare du NEO sans nouvelles cibles à du texte source dont les URLs visibles subsistent : c'est un proxy, pas une mesure de jetons ni de coût. Ne pas le présenter comme économie financière ou réduction comparable du contenu utile.
- Aucun compteur de jetons, tarif, coût d'inférence ou temps de lecture humain mesuré. Aucune économie d'argent démontrée.

## Lecture efficace
Lire `INDEX.md`, puis le Markdown principal uniquement. Résoudre ses références `[Rnnn]` via le §5. Ne charger le registre JSON (preuve détaillée, volumineuse) qu'en audit ou recherche de provenance. Pour diminuer encore le coût, sélectionner la spécialité/sous-section requise et ses références, au lieu d'injecter tout le document dans chaque requête.

## Reproduction et limites
- Audit source complet : `venv/bin/python audit_independant_v3/auditer_corriger.py` depuis le dossier racine de cette livraison ; dépend de PyMuPDF et du chemin local du PDF. Il recrée les trois fichiers de contenu/registre/résultats en v3 uniquement. Puis `python3 audit_independant_v3/finaliser.py` pour rapports, manifeste et ZIP.
- Vérification portable du paquet : `python3 VERIFIER_PAQUET.py` dans `livraison_v3` ; aucun réseau/dépendance externe. Ne remplace pas la comparaison PDF.
- Preuves locales : `audit_independant_v3/tables_independantes.json`, `paragraphes_independants.json`, `page07.png` et `AUDIT_INDEPENDANT_MACHINE.json`.
- Pas de validation externe des dates, recommandations, modalités d'examen, portée juridique, provenance des affirmations ou disponibilité des sites. Les incohérences internes de la source (>40 / >60 stratégies, 11 / 12 stations, références 2026) restent attribuées et non arbitrées.
- Deux clones GitHub exacts **non réalisés par cet audit** : le parent effectue cette étape autorisée par le mandat. Aucun fichier existant écrasé hors du nouveau dossier v3.

SHA-256 du Markdown final : `bb554439e65d45af25b101b64c85291308094ebd9d368b6ea892a722c71b067c`.
