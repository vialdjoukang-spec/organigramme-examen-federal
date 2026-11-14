# LOT 3 — sexe et silhouettes — 14.11.2026

Branche `cursor/interface-didactique-ffbc`. Trente id. `validate.py --only` : 30 partiels, 0 erreur, 0 complet.

Sexe lu dans `caption_source` seulement : male, female, woman, women, girl, boy, homme, femme, garçon, ou la suite « year-old man » / « yo man ». « year old man » sans trait d'union, « man » seul, « Man erkennt », et les titres de fichier « 68jm » ou « 61W » ne comptent pas. Les deux sexes dans la même légende donneraient « À vérifier ».

Un complet exige les deux côtés M ou les deux F, le même plan et la même séquence, un contour d'au moins 8 sommets distincts non rectangulaire relu sur l'overlay, et une `definition_source` qui n'est pas « À vérifier ». Aucun id ne réunit tout cela.

## Un côté sexé

| id | côté | sexe | légende | blocage |
| --- | --- | --- | --- | --- |
| IMG-167 | normale | M | « 21 year old male » (légende Commons complète, coupe 45) | pathologie sans mot de sexe ; temps nativ / artériel / portal ≠ scanner injecté dont la phase n'est pas nommée |
| IMG-168 | normale | M | même sujet, coupe 52 | pathologie « Metastasenleber bei Mammakarzinom » sans mot de sexe ; phase portale ≠ phase non nommée |
| IMG-169 | pathologie | M | « 10-year-old male », kyste CE3b, panneau A (Alshoabi 2023, CC BY 4.0) | foie normal sans mot de sexe |
| IMG-172 | pathologie | M | « 54-year-old male », Doppler du tronc porte, panneau a (Marra 2022, CC BY 4.0) | Doppler normal sans mot de sexe ; Budd-Chiari absent |
| IMG-228 | pathologie | F | « 76 year old woman », rein hyperéchogène (Häggström, CC0) | rein normal sagittal sans mot de sexe ; obstacle non illustré |
| IMG-235 | pathologie | F | « 78 year old woman » | aorte normale sans mot de sexe ; rupture absente |

Recherches Commons et Open-i (CC0, domaine public, CC BY, CC BY-SA) : pas de normale du même sexe, du même plan et de la même séquence pour ces six-là. Les clichés Häggström « year old man » (cholécystite, lithiase, foie normal, épididymite) restent « À vérifier ».

## Les deux côtés sans sexe établi

Normale présente, légendes muettes : IMG-170, IMG-171, IMG-176, IMG-177, IMG-229, IMG-230, IMG-231, IMG-243, IMG-244.

Normale absente (recherche libre sans paire de même sexe) : IMG-142, IMG-143, IMG-144, IMG-145, IMG-148, IMG-149, IMG-150, IMG-152, IMG-162, IMG-163, IMG-173, IMG-174, IMG-178, IMG-179, IMG-181.

## Contours

Les polygones d'au plus 6 sommets ont été redessinés (≥ 8 sommets distincts) et relus sur `progression/captures-interface/lot3/IMG-*.png`. IMG-229, IMG-149, IMG-150, IMG-152, IMG-163, IMG-170, IMG-171, IMG-179 avaient déjà une silhouette ≥ 8 sommets, relue, laissée en place.

## Adulte — règle du 14.11.2026 10:48

Le même sexe n'est exigé que pour le bassin, le sein et les organes génitaux. Ailleurs, adulte des deux côtés suffit. Silhouettes non redessinées.

`adulte` = oui si la légende donne un âge ≥ 18 ou le mot adulte, ou si un signe de maturité est visible (os sans cartilage de croissance, calibre aortique adulte). Sinon les deux champs valent « À vérifier ». Un rein de 9,34 cm recoupe une taille d'adolescent : IMG-228, IMG-230 et IMG-231 normales restent « À vérifier ».

Complet : IMG-235 (78 ans et lumière aortique 1,88 cm, coupe relue). IMG-167 et IMG-168 sont adultes des deux côtés mais restent partiels (phase différente, définition non sourcée).
