# Corrections après audit — fiches Status S-13 à S-24 (14.11.2026)

Ce document répond à `AUDIT_STATUS_13_24.md`. Les 12 JSON passent `json.load`, puis `generer_status.py` a régénéré `STATUS.html` (35 fiches, 0 illisible).

## Majeurs (2/2 appliqués)

| Fiche | Correction |
|---|---|
| S-17 | **Schober remis dans le bon sens.** Le test d'origine utilise deux repères : la jonction lombo-sacrée et un point 10 cm au-dessus. Le normal est une augmentation ≥ 5 cm, soit 10 → ≥ 15 cm. La variante modifiée (Macrae-Wright) ajoute un repère 5 cm au-dessous de la jonction ; son normal est ≥ 20 cm (À vérifier). Le nom, la technique, le seuil de positivité, le normal du geste et le texte de l'anomalie sont corrigés. |
| S-13 | **Photo génitale retirée.** Le fichier `img/S-13_hernie_inguinale_debout.jpg` est supprimé. Le champ image devient `a_fournir` : hernie franche photographiée debout, organes génitaux couverts. |

## Retraits de prudence (demandés par le coordinateur)

- **S-17, test d'Adams.** Le sujet de la photo SOSORT est probablement mineur et son consentement n'est pas documenté. Le fichier `img/S-17_adams_scoliose.jpg` est supprimé. Le champ image devient `a_fournir` : adulte consentant, en sous-vêtements.
- **S-24, `Elevated_JVP1.jpg`.** La licence a été revérifiée le 14.11.2026 par l'API Commons : CC BY-SA 3.0, « Own work » de James Heilman, MD, avec la mention « Consent of person in picture obtained ». La miniature thumb a été téléchargée sans erreur. **L'image est conservée.**

## Mineurs (24/24 appliqués)

### S-13
- La lampe est retirée du matériel.

### S-14
- L'image de l'hydrocèle est marquée `"occulter": true`. Sa légende signale la fenêtre occultante et le consentement non documenté.
- La varicocèle droite, récente ou qui ne s'affaisse pas couché, oriente vers une compression de la veine rénale ou cave → échographie.

### S-16
- Le renvoi « voir S-11/S-12 » devient « voir S-12 ».
- L'image du col est marquée `"occulter": true`, avec la mention « fenêtre occultante ».

### S-17
- Bragard : « flexion dorsale du pied ».
- La technique du Spurling est décrite.
- La photo d'Adams est retirée (voir plus haut).

### S-18
- La capsulite rétractile et l'omarthrose sont reliées à SY-59.
- La nuque est examinée en premier dans `a_dire[0]`, et la mention contradictoire est retirée de `a_dire[4]`.
- La Duale Reihe passe avant Hegedus.

### S-19
- « Hypoalgésie à la piqûre » (RV 3,1 ; IC 2,0–5,1) remplace « hypoesthésie ». L'amyotrophie thénar et le monofilament sont signalés comme peu utiles.
- La technique du Finkelstein est décrite.
- Une anomalie « syndrome des loges » est ajoutée (SY-61).
- La Duale Reihe passe avant D'Arcy.

### S-20
- Thomas : le flessum concerne la hanche **controlatérale**.
- Le geste FABER (Patrick) est ajouté, pour distinguer hanche et sacro-iliaque.
- La mention « aucune source suisse » quitte les sources et passe dans `valeur`.

### S-21
- Lachman : le tibia est tiré « fermement, sans à-coup », pour éviter le faux négatif.
- Les critères de la règle d'Ottawa du genou sont détaillés (source canadienne, À vérifier).

### S-22
- Installation : « le test des 4 pas fait partie de la règle d'Ottawa ».
- SY-61 est cité (syndrome des loges après fracture).

### S-23
- Normal de l'IPS : 1,00–1,40 ; la zone 0,91–0,99 est limite (À vérifier).
- Aorte : LR+ 12, sensibilité 76 % si l'anévrisme mesure ≥ 5 cm (Lederle, JAMA 1999, source américaine). La source est ajoutée.
- ESC 2024 est cité dans l'original : Eur Heart J 2024;45:3538-3700.

### S-24
- Nom de la manœuvre : « voir aussi S-10 ».
- La légende de la photo précise qu'il s'agit probablement de la jugulaire externe, et que la licence a été revérifiée.
- Wells : version de 1997 à 3 niveaux, sans antécédent de TVP ; version de 2003 à 2 niveaux, avec antécédent de TVP.
- CEAP est étiqueté « source américaine (American Venous Forum) » et placé après la Duale Reihe.

## Reste à faire

- `generer_status.py` ne lit pas encore la clé `"occulter"` (S-14, S-16). Une fenêtre occultante reste à coder ; la décision revient à Vial.
- Images à fournir (S-13, S-17 Adams, etc.) : séance photo avec figurants consentants, sous CC BY 4.0.
