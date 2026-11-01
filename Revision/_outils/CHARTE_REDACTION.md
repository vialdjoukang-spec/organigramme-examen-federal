# Charte de rédaction — QCM Type A (Revision · examen fédéral CH)

*Grand Maître Professeur Bitunder · v1.0 · 1er novembre 2026 (Europe/Zurich, UTC+1).*
*Sources : guide IML Berne (R. Krebs, MC‑Anleitung), Exigences MEBEKO/OFSP 2026, `STRATEGIE_QCM_EXAMEN_CH.md`. Gabarit de référence : G01 v2.*

---

## 1. Voix du professeur
- Français suisse soigné, phrases courtes, registre de confrère à confrère. On emploie le **vouvoiement** dans le feedback.
- Le ton est exigeant et bienveillant : on nomme l'erreur sans humilier (« Réflexe tentant, mais… »).
- On ne délaie pas : une idée par phrase, et le verbe d'action en tête dans la perle (« Mesurer… », « Ne jamais… sans… »).
- On utilise le vocabulaire suisse (EMS, médecin de famille, cabinet, Swissmedic, compendium, LAMal) et les unités SI, avec mmHg pour la PA.
- Les abréviations sont courantes (ECG, CRP, TSH) ; on développe les autres à la première occurrence.

## 2. Anatomie d'un item Type A
| Élément | Règle |
|---|---|
| **Stem** | Vignette brève ordonnée : âge et sexe → lieu (cabinet / urgences / EMS / hôpital) → motif → durée → anamnèse → status (constantes chiffrées) → examens → éventuellement évolution. 2–5 phrases. Valeurs normales fournies si elles sont non triviales. |
| **Question** | Une seule phrase, positive de préférence : « Quel est le diagnostic le plus probable ? », « l'examen le plus approprié », « la prochaine étape », « le traitement de première intention ». |
| **Options** | 5 options (A–E), **homogènes** (une seule dimension : DX *ou* examen *ou* traitement), plausibles, de longueur comparable, sans ponctuation finale. |
| **Clé** | Une seule réponse juste ou meilleure, défendable par une source. |
| **Métadonnées** | `id`, `lot`, `ssp`, `bloc`, `dx`, `dx_cibles`, `niveau`, `specialite`, `type`, `polarite`, `blueprint{tache,setting}`, `media`, `qualite`, `historique`. |

## 3. Règles IML anti‑indices (obligatoires)
1. **Test de couverture** : en cachant les options, un expert doit pouvoir formuler la réponse.
2. Pas de « toutes / aucune des réponses ci‑dessus ».
3. Pas de *cue* : la bonne réponse ne doit pas être la plus longue ni la plus nuancée. Pas de mot du stem répété dans la clé. Pas de convergence ni de paire de contraires.
4. Pas de « toujours / jamais / uniquement » dans les options.
5. **Pas de question piège de forme** : pas de double négation. Le Type A négatif (« la moins appropriée ») reste ≤ 5 %, avec la négation **en gras**.
6. Pas de trivia (dates, éponymes, pourcentages isolés sans conséquence clinique).
7. Chaque item est **autonome** : il ne dépend pas d'une autre question (sauf dans une séquence, au Temps 2).

## 4. Pièges classiques à entraîner (bloc « Pièges & alarmes »)
- **Fausse réassurance** : examen normal qui ne clôt pas (p. ex. glycémie normale, ETT rassurante à tort, troponine précoce négative).
- **Attribution prématurée** (« c'est la ménopause », « c'est l'anxiété ») avant d'avoir exclu l'organique grave.
- **Ordre des gestes** : le geste corrigible en minutes passe avant le bilan (glycémie avant ECG chez le diabétique confus).
- **Contre‑indications et interactions** : bêtabloquant seul dans un phéochromocytome, thiamine avant glucose chez l'alcoolique, glucagon inefficace dans certaines situations.
- **Faux positifs** et interférences de dosage (médicaments, régime, stress).
- **Red flags** du SSP : chaque drapeau rouge du LOT est testé au moins une fois.

## 5. Couverture DD (contrat SSP)
- Avant de rédiger, on extrait la **liste DD** du LOT (Phase A + DX.1…n) et on construit la matrice DD × tâche (mechanisms / assessment / management).
- **Chaque DD ≥ 2 items EX où il est la cible** (premier `DX.n` du champ `dx`), vérifié par `couverture_dd.py` (code retour 1 tant qu'il reste un gap). Les DX cités ensuite (« DX.3 vs DX.7 ») comptent comme discrimination croisée. Les distracteurs sont **des DD réels du même LOT** dès que possible.
- Volume : pas de plancher artificiel ; **plafond souple 80–100 questions par SSP**. Mieux vaut 2 EX solides par DD qu'un trivia de plus.
- Faits médicaux : **uniquement le LOT audité** `repo/LOT_Claude_Finaux/LOT_0NN/` (Phase A, Phase B DX.n §), lien d'ancre vérifié par le build.
- La répartition des blocs se cale sur G01 : Raisonner ≈ 1/3, Discriminer ≈ 1/2, Pièges & alarmes ≈ 1/6.
- Répartition des niveaux : **EX 55–60 %**, **AP ≈ 25 %**, **SPE 15–20 %** (chaque SPE étiquetée par spécialité).
- Clés équilibrées A–E (± 1), jamais 3 clés identiques d'affilée.
- Blueprint : les 3 tâches et ≥ 3 settings sont représentés.

## 6. Niveaux et couleurs
| Niveau | Couleur | Définition |
|---|---|---|
| **EX** (examen) | noir #1a1a1a | Réflexe attendu de tout candidat à l'examen fédéral. |
| **AP** (approfondissement) | bleu #0B5A8C (texte en bleu) | Mécanisme ou nuance qui fait comprendre le pourquoi (chaîne anat → tt). |
| **SPE** (spécialiste) | violet #6B2D8B + badge `SPE · spécialité` | Décision de deuxième ligne ; bouton 🔥. |

## 7. Feedback 💡 — 4 blocs, fermé par défaut
1. **Clé + pourquoi c'est juste**, en suivant la chaîne **anatomie → physiologie → physiopathologie → clinique → traitement** (on sélectionne les maillons utiles).
2. **Pourquoi chaque autre option est fausse** : une ligne par distracteur, avec le DD visé (« = E5, thyrotoxicose »).
3. **Perle clinique** : le réflexe à emporter. Les **probabilités, LR, sensibilités et spécificités en rouge #C8102E**.
4. **Source** : libellé + ancre vers la leçon du LOT (`source_lecon.href`), puis la référence suisse.

**UX non négociable** : aucun `<details open>`. Le feedback n'apparaît qu'au clic 💡 ou en **mode révision** (avec confirmation, non mémorisé). Un choix d'option marque juste/faux mais n'ouvre jamais le commentaire. Le PDF montre les questions sans réponses, avec le corrigé en annexe.

## 8. Sources
- **Suisses d'abord** : OFSP/BAG, Swissmedic, compendium.ch, SSMI/SGAIM, mediX, recommandations HUG / CHUV / USZ / Insel, sociétés suisses de spécialité.
- Ensuite : ESC, ESMO, EASL, NICE, UpToDate, etc., avec la date.
- **Jamais** d'item IML (copyright) ni de question copiée d'une banque commerciale.
- Un fait sans source dans le LOT ni source suisse ou internationale vérifiable est **retiré**.

## 9. Images et médias — interdiction d'inventer
- **Aucune image inventée, générée ni « illustrative »** dans une question (ECG, radiographie, dermatologie, frottis…).
- On n'utilise un média que s'il **existe réellement dans la leçon** du LOT (avec la source), et on le référence dans `media`. Sinon, `media: null` et pas de bouton 🖼.
- On décrit en texte ce que l'image montrerait (« ECG : sus‑décalage ST de V1 à V4 »).

## 10. Format de livraison — HTML prioritaire
1. **HTML autonome hors ligne** (template `_outils/templates/_ssp_reflexe.html` + `_ssp_script.js`). Police **Atkinson Hyperlegible** intégrée (`_fonts.css`), **fond bleu ciel pâle**, rouge #C8102E réservé aux probabilités et alarmes, filtres Tous / EX / AP / SPE, scores par niveau, par bloc et par spécialité, tableau 🔥.
2. **JSON** versionné (source de vérité), généré par `_bank_GXX.py`.
3. **PDF** en second (questions puis corrigé en annexe).
4. **CHANGELOG.md** par SSP.
5. Ensuite : `python3 _outils/scripts/couverture_dd.py GNN` puis `python3 _outils/scripts/etat_lieux.py` (et `resume_jour.py --write`, qui appelle etat_lieux.py).

## 11. Checklist IML par item (champ `qualite.checklist_iml`)
`couverture` · `homogene` · `sans_cue` · `sans_trivia`. Les quatre doivent être à `true` pour obtenir `revue_auto`.

## 12. Outillage (voir README.md)
`init_ssp.py G3` (canevas `_bank_G03.py` + checklist DD + CHANGELOG) → rédaction → `build_ssp.py <dossier>` (contrôles bloquants : 5 options, une clé, niveau/spécialité, « pourquoi » par distracteur, doublons ; **clés stables** : une question publiée garde sa lettre) → `couverture_dd.py` → `etat_lieux.py`.
