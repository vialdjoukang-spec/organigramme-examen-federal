# Audit médical de niveau 2 · branche feat/ck-glossaire-lot01

**Auditeur** : Galien. **Auteur audité** : Hippocrate (unités glo-lot01a et glo-lot01b). **Date** : 17.10.2026, Europe/Zurich.

## Méthode

Galien a relu seulement le diff des deux unités et les signalements de niveau 1 (`tools/audit/niveau1.py`, Lyncée), région par région, à partir des listes de travail de `tools/audit/galien_region.py travail`. Chaque entrée a été confrontée au paragraphe exact de sa source, relu le 17.10.2026 (CEN, HUG, SFE, HAS). Trois automates ont travaillé : Neuro (76 entrées), TêteCou (13 entrées) et PeauPopulations (11 entrées) ; CœurThorax, AbdoPelvis et Locomoteur n’avaient aucune entrée dans ce lot.

## Résultat

Galien a relevé et corrigé 29 fautes : aucune critique, 3 majeures et 26 mineures. Chaque correction a son propre commit, et sa ligne de `qa/audit/fautes.jsonl` porte le hachage de ce commit ; le détail figure dans `qa/audit/RAPPORT_FAUTES.md`.

- Les trois fautes majeures concernent une alerte omise (l’apparition brutale d’une paralysie faciale, qui fait suspecter un AVC selon les HUG), un traitement écrit dans une entrée sémiologique (syndrome de Ramsay-Hunt) et une affirmation capitale non lue mais marquée « sourcé » (atteinte pupillaire du III, désormais « À vérifier »).
- Les fautes mineures forment trois familles : des faux synonymes en alias (11 alias retirés dans 10 entrées), des précisions de manœuvre inventées (durées, conditions, épreuves non lues) et des généralisations au-delà de la portée de la source.

## Points relevés sans correction

- L’orientation du syndrome méningé dit que la méningite et l’hémorragie méningée « imposent une prise en charge urgente ». La source citée ne le dit pas en ces termes, mais l’affirmation est exacte et capitale ; Galien la laisse et demande une source suisse ou européenne pour le lot 02.
- Lyncée découpe mal les éponymes à trait d’union (« signe de Argyll- ») ; une exclusion motivée le contourne, et Janus doit corriger le motif.
- Le nerf hypoglosse est exclu de Lyncée avec un motif : son infobulle viendra de nc.json (nerf XII) en phase NC-1.

## Ce que cet audit ne couvre pas

Galien n’a pas audité `data/ck/doses_ch.json`, qu’il a lui-même rédigé ; la contre-lecture de ces trois lignes et des deux doses « À vérifier » de `qa/posologies.md` revient à Asclépios.
