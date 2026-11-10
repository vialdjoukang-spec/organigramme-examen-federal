# Décision de séance — LOT_052 — 2026-11-10

Ordre écrit de Vial, médecin et propriétaire du dépôt, du 2026-11-10 : détruire le contenu de `Grokbot/LOT_052` et le refaire selon `PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md`, avec les images en paire brut / annotée de la version µ6 du 10.11.2026. Cet ordre prime, pour ce lot, sur les consignes plus anciennes du dépôt.

Branche imposée : `grok/refonte-lot-052`, prise sur `main` au commit `f5e8d76e4`. Pas de pull request, pas de fusion, pas d'auto-merge. Bitunder audite puis décide.

Collision lue, non modifiée : `origin/claude/lot-052` (autre dossier) et `origin/grok/lot-052-bande` (ancienne version d'environ 10 Ko). `outils/mere.py` n'a pas été lancé, parce qu'il écrit dans `outils/`.

Porte : la liste est écrite et hashée. `controle3.py` est vert sur la Phase A seule. Cela ne vaut ni audit indépendant, ni porte P3, ni porte P4. Deux fichiers sur onze seulement : la Phase A est livrée, DX.1 suit dans le commit suivant de cette même session, DX.2 à DX.10 attendent le feu vert explicite de Bitunder.

Définition retenue : il n'existe pas, dans les textes lus, de définition d'une société savante mondiale en une phrase pour « douleur abdominale ». La définition opératoire est celle de Sinz, Schmied et Ukegjini, Forum Médical Suisse, 2021, responsabilité scientifique Ukegjini, hôpital cantonal de Saint-Gall. Les bornes de durée viennent des Hôpitaux universitaires de Genève (aigu : moins de 7 jours, colloque du 11 octobre 2017 ; chronique : au moins 3 mois, stratégie 2023).

Image de Phase A : le cliché libre qui sépare la perforation (E2). Un cliché d'ischémie mésentérique (E1) sans légende déjà imprimée et sous licence libre n'a pas été obtenu. La latéralité « sous le diaphragme gauche » est celle de la description Commons ; le cours ne la recalcule pas.

Doses : seules les informations professionnelles ouvertes (Dafalgan oral 47503, Dafalgan intraveineux 66702, Algifor Liquid Caps 400, 65372). Aucun milligramme d'antibiotique, de métamizole ou de morphine.

## Correction de la Phase A — 2026-11-10, soir

Ordre de Vial (« Tu dois corriger ») : la Phase A est réécrite par Grok Bot lui-même, sans délégation, selon `CHARTE_VIAL_10.11.26.md` et `PROMPT_LOTS_Lo_10.11.26.claude.md`. Cette section remplace les décisions ci-dessus sur la liste, la définition, les images et les doses.

- Liste : celle de `LISTE_DX_CANONIQUE.md` déjà poussée sur la branche (commit af1c771c0, fréquence au cabinet, série HUG la plus récente), sans MICI ni hémorragie digestive. La Phase A la reprend telle quelle et y ajoute les rangs E du cours : E1 = GEU rompue, AAA rompu, ischémie mésentérique, occlusion ou hernie étranglée, infarctus inférieur ; E2 = perforation, angiocholite ; E3 = urgence chirurgicale sans choc (appendicite, pancréatite, diverticulite).
- Définition : HUG, colloque de médecine de premier recours du 11.10.2017 (moins de 7 jours) ; douleur chronique : HUG 2023 (au moins 3 mois) ; douleur : IASP, définition révisée.
- Sources suisses d'abord : RMS 2010 et 2006 (deux articles), HUG 2017 et 2023, smarter medicine (Société suisse de chirurgie), Forum Médical Suisse 2021 ; Börner 2025 en second. Extraits mot pour mot dans `_travail/evidence/`, indexés dans `_travail/PA/paquet.json`.
- Doses : Dafalgan® 47503, Dafalgan® i.v. 66702, Novalgin® 16950, Algifor® 65372, toutes depuis l'information professionnelle. Aucune dose d'opiacé ni d'antibiotique.
- Images : paire brute / annotée sur le cliché de Bill Rhodes ; cliché Cerevisae corrigé (repère 1 sur la clarté, 2 sur le L, 3 sur l'air libre et non sur l'estomac) et présenté comme déjà annoté par l'auteur.
- Phase B : DX.1 (douleur non spécifique) et DX.2 (gastroentérite) ont été réécrits sur la branche par un autre passage et ne sont pas touchés ici. DX.3 à DX.10 sont restaurés depuis `origin/main` (anciennes versions, ancienne liste) et restent à refaire.
- Toujours pas d'audit indépendant (Θ2-P3) : le rédacteur ne s'audite pas lui-même.

## Passage fix052b — 2026-11-10

- Rangs E : exactement ceux de `LISTE_DX_CANONIQUE.md`. Le rang E3 disparaît ; « hospitalisation sans rang E » le remplace (appendicite, cholécystite simple, pancréatite, diverticulite compliquée). La pancréatite est une hospitalisation médicale, pas une urgence chirurgicale.
- Occlusion et hernie étranglée : porte E1, conduite unique « transfert immédiat en ambulance médicalisée, à jeun », après palpation des orifices herniaires (RMS 2010, HUG 2017).
- GEU : β-HCG positive avec douleur → urgences de gynécologie sans délai, échographie ; ambulance médicalisée si instable (HUG, plaintes gynécologiques, 30.10.2018 ; RMS 2010).
- 144 nommé d'après la page CHUV « Appeler le 144 ». Buscopan® non ajouté : le seul extrait (HUG 2023) le cite pour la douleur chronique.
- Hinchey : RMS 2009 (stades I à IV) et RMS 2021 (Hinchey modifiée, abstention d'antibiotique dans la forme simple sans facteur de risque).
- Embryologie : limites d'après TeachMeAnatomy (artère mésentérique supérieure) ; règle clinique d'après Sinz 2021. StatPearls (NBK545247) bloque la lecture automatique.
- Images : fiche 1 = échographie axiale d'AAA, Mikael Häggström, CC0, sans échelle donc sans diamètre ; fiche 2 = Rhodes. Attribution complète dans chaque légende.
- La question finale garde la formulation imposée par le prompt de Lo (ligne 24), qui contient « fenêtres » ; c'est la seule occurrence.

## Passage fix052c — 2026-11-10

- E1 = hernie étranglée ou occlusion avec signes d'ischémie (défense, lactates, syndrome inflammatoire ; HUG 2017, diapositives 8 et 14). L'occlusion simple est une urgence chirurgicale hospitalisée le jour même, sans rang E (RMS 2010, texte et figure 2).
- AAA : seuil d'après Ponti et coll., RMS 2012 (valeurs normales de 1,4 à 3 cm), et Righini, RMS 2004 (AAA > 3 cm ; mesurer aussi le chenal persistant). Aucune source ESC n'est citée. L'image mesurée de l'auteur ne porte aucune valeur : aucun diamètre n'est lu sur l'image.
- GEU : l'image CC0 « Blob sign of ectopic pregnancy » porte les légendes anglaises de l'auteur ; aucune version sans légende n'existe. Elle est présentée comme original légendé, puis annotée en français.
- GEU, conduite : β-HCG positive → urgences de gynécologie (HUG 2018, fidèle à l'extrait) ; en choc, GEU rompue = urgence vitale, ambulance médicalisée (RMS 2010, extraits 16 et 17).
- Morphine : dose de l'AIPS Morphin HCl Sintetica (Swissmedic 51039, mars 2024), avec la mise en garde de la notice sur le syndrome abdominal aigu d'étiologie inconnue. LAMal : aucun extrait, rien n'est ajouté.
- Durées en chiffres quand l'extrait les écrit en chiffres. « 6 heures » s'appuie sur RMS 2006 (Gonzalez et coll., tableau 3). La néphropathie au contraste garde « trois à sept jours », car seul Sinz 2021 la soutient, en lettres, et `controle3.py` exige le chiffre dans l'extrait.
- `images/0fa3bad94e3ca02b.png` est conservée : DX.1 l'utilise.

## Passage fix052d — 2026-11-10

- Opiacés : la phrase « l'effet antalgique justifie à lui seul la prescription » est retirée. La restriction de l'AIPS 51039 est citée mot pour mot, puis la douleur forte du ventre aigu est posée comme la nécessité absolue (RMS 2006, extrait 16, cité entre guillemets). Le grade B reste, car il figure dans l'extrait 18 de la même source.
- Délai : « sans délai, aux urgences » remplace « le jour même » partout (P3, P4, P5, P6, P10, P13, en-tête).
- GEU : rang « E1 si rupture ou choc » dans le badge, le tableau P4 et la fiche 2. Le fichier DX.9 n'est pas modifié.
- Masse pulsatile : E1 seulement si elle est douloureuse (HUG 2017, douleurs vives). L'anévrisme indolore n'ouvre pas la porte E1.
- Biologie : CRP < 10 mg/l et lipase 13–60 U/l d'après les intervalles du CHUV (état au 16.10.2024). Pour les lactates, le document renvoie au fichier des examens : le cours renvoie aux valeurs du laboratoire.
- 11.A : urgentiste dans les 10 minutes et chirurgien dans les 60 minutes (Boerner 2025), antibiotique dans l'heure en choc septique (Sinz 2021).
- DX.2 : aucune source ne chiffre sa part isolée ; le cours garde « 80 % causes médicales, sans part isolée ».
- La règle « la série la plus récente tranche » est présentée comme règle de lecture du cours, pas comme phrase d'une source.
- Néphropathie au contraste : « se normalise ensuite en moins d'une semaine », sans chiffre, car l'extrait écrit la durée en lettres.

## Passage fix052e — 2026-11-10

- Aucune citation mot pour mot dans le corps du texte : la définition de l'anévrisme, la restriction de la morphine et l'effet des opiacés sont reformulés. La nuance « uniquement en cas de nécessité absolue » est gardée (6 mots, sous le seuil de 8).
- Délais d'arrivée (10 et 60 minutes) au seul point 11.A ; la fenêtre Urgence garde un rappel bref (priorité ESI 1 ou 2). L'antibiotique dans l'heure n'apparaît plus qu'au point 11.B ; la question d'examen correspondante est remplacée par le Novalgin® en choc (AIPS 16950).
- Dose intraveineuse de la morphine : au seul tableau des antalgiques.
- Points clés : la ligne « orifices herniaires, ECG, β-HCG » est retirée (déjà au point 6, dans la fenêtre Urgence et au point 14).
- Lactates : aucun extrait de valeur normale ; la phrase est retirée.
- `verif.py` compte de nouveau les citations entre guillemets dans le contrôle des 8 mots.
