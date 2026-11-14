# Corrections des fiches Status S-01 à S-12 (suite de AUDIT_STATUS_01_12.md, 14.11.2026)

J'ai appliqué les patchs à S-01…S-12.json, puis validé chaque fichier par json.load. Bilan : 20 images réelles conservées et présentes dans img/, 25 champs « a_fournir ». Aucun patch n'a été refusé ; deux patchs ont été adaptés, et la raison est donnée.

## Critiques (2/2 appliqués)
| Fiche | Patch | Statut |
|---|---|---|
| S-05 | Image du détenu de Guantánamo (`S-05_ophtalmoscopie.jpg`) | **Appliqué** : fichier supprimé ; le champ passe en `a_fournir` avec la description de l'auditeur. Je n'ai pas cherché d'image de remplacement, car l'API Commons répond HTTP 429. |
| S-12 | Image NEJM (`S-12_caput_medusae.jpg`) | **Appliqué** : fichier supprimé ; le champ passe en `a_fournir` (Commons CC BY/PD ou Europe PMC CC BY relue). |

## Majeurs (6/6 appliqués)
| Fiche | Patch | Statut |
|---|---|---|
| S-01 | Seuils de PA : « pas d'HTA si < 140/90 » ; 120–139/70–89 = « PA élevée » (ESC 2024) | **Appliqué**, dans le normal et le « positif si » de la manœuvre. |
| S-04 | Ganglion épitrochléen : 3 cm au-dessus de l'épicondyle médial, sillon bicipito-tricipital | **Appliqué** ; j'ai ajouté que le nerf ulnaire passe en arrière de l'épicondyle. |
| S-08 | Palpation carotidienne au niveau du cricoïde, loin du sinus carotidien | **Appliqué**. |
| S-08 | Lobe thyroïdien entre la trachée et le bord antérieur du SCM | **Appliqué**. |
| S-11 | « consigne MEBEKO » → déduction (Infotext : « Intimbereich », les seins n'y sont pas nommés) | **Appliqué**, dans duree.cs et a_nommer_sans_faire. |
| S-11 | Légende du visage et image | **Appliqué** : image recadrée sous le menton (bande supérieure de 95 px retirée de la miniature 500 px), puis contrôlée à l'œil : aucun trait du visage n'est visible. La légende est corrigée. L'avis § 3 (préférer une figurante habillée, fenêtre occultante) **reste une décision de Vial**. |

## Mineurs
| Fiche | Patchs | Statut |
|---|---|---|
| S-01 | Hypoglycémie de niveau 2 ; « sepsis à haut risque » ; 3 mesures, moyenne des 2 dernières ; légende de l'image PA ; SY-35 et SY-67 ajoutés | Appliqués |
| S-02 | Critère GLIM 2019 ; scorbut ; renvoi « détail en S-03 » ; SY-51 retiré ; GESKES ajouté avant ESPEN | Appliqués |
| S-03 | Gale et dermatose dans le prurit ; légende des pétéchies sans mention du PTI ; image de Schamroth | Appliqués : l'image Schamroth est passée en `a_fournir` et le fichier `S-03_schamroth.jpg` est supprimé (fenêtre illisible ; aucune autre image recherchée, à cause de l'API 429). |
| S-04 | Seuil épitrochléen > 0,5 cm « À vérifier » ; SY-63 et SY-79 retirés | Appliqués |
| S-05 | Nystagmus inhibé par la fixation ; VI microvasculaire ; sympathomimétiques ; échelle de Monoyer ; « fixe l'œil ouvert » ; geste Ishihara + désaturation du rouge ajouté ; fausse source européenne supprimée | Appliqués |
| S-05 | Anisocorie peu visible | **Adapté** : j'ai corrigé la légende (« différence discrète, mieux visible dans la pénombre ») au lieu de remplacer l'image, l'API Commons étant indisponible. |
| S-06 | LR de Weber, Rinne et voix chuchotée (Bagai 2006, source américaine, résumé lu) ; cholestéatome ; source Bagai à la place de la fausse source européenne ; SY-4 et SY-14 cités dans la cible ; légende de l'otoscopie | Appliqués |
| S-07 | ESCMID 2012 (résumé lu) et SSI non lue ; Ebell étiqueté ; ajustement McIsaac dans a_dire | Appliqués ; j'ai aussi ajouté ESCMID 2012 dans les sources. |
| S-08 | Auscultation du creux sus-claviculaire à l'angle de la mandibule ; SY-15 retiré | Appliqués |
| S-09 | Excursion ≈ 3–5 cm « À vérifier » ; Metlay 1997 ; légende (omoplate) ; SY-24 ajouté | Appliqués |
| S-09 | SY-31 : « retirer ou citer » | **Adapté** : je l'ai gardé et cité dans a_dire (hypercapnie du BPCO somnolent). |
| S-10 | Pouls paradoxal (Roy 2007) ; légende de la jugulaire externe ; ESC HF 2021 + mise à jour 2023 | Appliqués |
| S-11 | Tumeur testiculaire (gynécomastie) ; hypothyroïdie (galactorrhée) ; SY-65 retiré | Appliqués ; j'ai ajouté SY-51, désormais cité. |
| S-12 | Murphy LR+ 2,8 (Trowbridge, résumé lu) ; psoas (Wagner, résumé lu) ; Blumberg « sur la zone suspecte » ; geste « largeur de l'aorte » (Lederle 1999) ; technique du flot ajoutée à la matité déclive mobile ; formulation herniaire/génitale corrigée ; SY-39 retiré | Appliqués ; sources Trowbridge, Wagner et Lederle mises à jour. |

## Restes « À vérifier »
- Licences Commons des images conservées : relues par l'API le 14.11.2026, au moment de leur téléchargement. L'auditeur n'a pas pu les revérifier, car l'API lui a répondu HTTP 429.
- Les sources suivantes ne sont pas lues : position de la Société suisse d'hypertension, SSI Pharyngitis 2023, GESKES, GLIM.
- Les articles JAMA non cités par l'auditeur restent marqués « non lu » : Siminoski, Williams, Grover, Naylor.
