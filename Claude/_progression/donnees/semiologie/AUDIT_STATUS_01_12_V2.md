# Audit médical V2 — fiches Status S-01 à S-12 (contre-vérification, 14.11.2026)

Méthode : j'ai lu `CORRECTIONS_STATUS_01_12.md`, puis j'ai relu par script (json.load) tous les champs visés dans les 12 JSON. J'ai vérifié que chaque `image.fichier` existe dans `img/` et que la liste `syndromes_lies` concorde avec les syndromes cités. J'ai aussi regardé l'image S-11 recadrée.

## 1. Critiques et majeurs du premier audit

| Fiche | Défaut V1 | Constat V2 | Statut |
|---|---|---|---|
| S-05 | Image d'un détenu de Guantánamo | Le fichier n'est plus dans `img/`, et aucun JSON ne le cite. Le champ passe en `a_fournir` (« main droite et œil droit… pouce sur le sourcil »). | Corrigé |
| S-12 | Image NEJM (tête de Méduse) | Le fichier n'est plus dans `img/` ; le champ passe en `a_fournir` (licence libre relue). | Corrigé |
| S-03 | Image Schamroth illisible (mineur) | Le fichier est absent ; le champ passe en `a_fournir` (fenêtre visible puis absente). | Corrigé |
| S-01 | Seuil de PA | Normal : « pas d'HTA si < 140/90 ; 120–139/70–89 = PA élevée (ESC 2024, À vérifier ; SSH non lue) ». Le `positif_si` est cohérent. | Corrigé |
| S-04 | Ganglion épitrochléen | « 3 cm au-dessus de l'épicondyle médial, sillon entre biceps et triceps ». L'ajout du nerf ulnaire est exact. | Corrigé |
| S-08 | Palpation carotidienne | « tiers inférieur du cou, à hauteur du cricoïde… loin du sinus carotidien ». | Corrigé |
| S-08 | Lobe thyroïdien | « entre la trachée et le bord antérieur du SCM, en refoulant légèrement ce muscle ». | Corrigé |
| S-11 | « Consigne MEBEKO » pour les seins | Requalifiée en « déduction » dans `duree.cs` et dans `a_nommer_sans_faire[0]`. | Corrigé |
| S-11 | Visage visible | L'image est recadrée sous le menton : aucun trait du visage n'apparaît (contrôle visuel). La légende est exacte. Le choix entre figurante habillée et fenêtre occultante reste une décision de Vial. | Corrigé |

**Valeurs JAMA reprises.** Elles sont conformes aux résumés PubMed lus en V1 et portent l'étiquette « source américaine — résumé lu » :

| Source | Valeurs reprises |
|---|---|
| Bagai 2006 | 6,1 / 0,03 ; Weber 1,6 / 0,70 ; Rinne 2,7–62 / 0,01–0,85 |
| Roy 2007 | 3,3 / 0,03 |
| Trowbridge 2003 | 2,8 (IC 0,8–8,6) |
| Lederle 1999 | LR+ 12 ; sensibilité 76 % pour un AAA ≥ 5 cm |
| Metlay 1997 | aucun signe isolé ne confirme une pneumonie |
| Ebell 2016 | valeurs inchangées et exactes |
| Wagner 1996 | psoas qualitatif |

Williams, Grover, Siminoski et Naylor restent marqués « non lu ». C'est honnête.

## 2. Défauts nouveaux ou résiduels (aucun critique, aucun majeur)

| Grav. | Fiche, champ | Ancien → Nouveau |
|---|---|---|
| Mineur | S-12 `version_cs.a_nommer_sans_faire[1]` | « …orifices herniaires : à nommer si l'examen exige d'invaginer le scrotum (déduction) : à nommer, en particulier devant une occlusion ou une douleur de l'aine. » → « …orifices herniaires : à nommer si l'examen exige d'invaginer le scrotum (déduction), en particulier devant une occlusion ou une douleur de l'aine. » (doublon « à nommer », syntaxe cassée) |
| Mineur | S-11 `examen_complet[Palpation].gestes[1].anomalies[1].signifie` | « hyperprolactinémie (médicament, prolactinome), hypothyroïdie » → « hyperprolactinémie (médicament, prolactinome), hypothyroïdie (SY-51) » (SY-51 figure dans `syndromes_lies` sans être cité ; le script le confirme) |
| Mineur | S-09 `version_cs.a_dire[0]` | Retirer « (chez le BPCO somnolent, chercher une hypercapnie, SY-31) » de la phrase à dire. L'ajouter dans `pieges` : « Chez un BPCO somnolent, oublier l'hypercapnie (SY-31) : la SpO2 ne la révèle pas. » (une consigne n'a pas sa place dans une phrase dite au patient) |

Aucune autre erreur nouvelle n'a été trouvée dans les champs modifiés. Les gestes ajoutés sont exacts : Ishihara et désaturation du rouge (S-05), largeur aortique et flot (S-12), cholestéatome (S-06), scorbut (S-02). Les 20 images citées existent toutes dans `img/`. Les 12 JSON sont valides.

## 3. Restes hors périmètre bloquant
- Licences Commons des 20 images conservées : je ne les ai pas revérifiées moi-même, car l'API a répondu HTTP 429 en V1. Le correcteur déclare une lecture au téléchargement.
- Non lues : SSH, SSI Pharyngitis 2023, GESKES, GLIM. Ces sources sont signalées « À vérifier » dans les fiches.

## 4. Verdict
**audit-ok.** Les 2 critiques et les 6 majeurs sont corrigés sans erreur nouvelle de gravité supérieure à mineure. Les 3 mineurs du § 2 peuvent s'appliquer sans nouvel audit.

## Clôture
Les 3 mineurs du § 2 ont été appliqués mot pour mot (S-12, S-11, S-09). **audit-ok** confirmé pour S-01 à S-12.
