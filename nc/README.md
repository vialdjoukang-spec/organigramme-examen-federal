# nc/ · données des schémas de nerfs crâniens

- `sources.yml` : registre des sources (titre, auteur, URL, licence vérifiée et date).
- `annot/<nerf>.yml` : annotations au format d’Ariane, chacune sourcée ; une position ne vient que d’un objet nommé du modèle.
- `trait/<nerf>-<vue>.svg/.json` : trait et ancres produits par `tools/dedale/freestyle.py` (modèle Z-Anatomy) ou `trace.py` (Gray 1918).

Licence : les fichiers de `trait/` et les vues de `assets/nc/` sont des œuvres dérivées publiées sous CC BY-SA 4.0
(https://creativecommons.org/licenses/by-sa/4.0/) : Z-Anatomy (G. Kervyn, M. Zielinski, CC BY-SA 4.0), d’après BodyParts3D
(DBCLS, CC BY-SA 2.1 JP) et Cranial Nerves and Foramina (University of Dundee, CAHID, CC BY 4.0) ; plan d’après Gray 1918 (domaine public).
Aucun fichier source du modèle n’est versionné.
