# Essai de débit, avant la passe de production

Ces fichiers ne sont pas la production du LOT. Ils mesurent Gemma 4 (`gemma4:e4b-it-qat`) sur cette machine, le 9 novembre 2026.

- Trois phrases libres : 12,15 jetons par seconde, `think` vide.
- Point 1, première formulation du prompt : 925 octets, 11,3 tok/s, arrêt spontané.
- Point 1, deuxième formulation : 1531 octets, 11,7 tok/s.
- Point 2, formulation « huit paragraphes » : 4230 octets, 11,5 tok/s. Défaut observé : 89 % arrondi en « quatre-vingt-dix ». Le prompt figé interdit cet arrondi. La passe de production est la première écriture avec ce prompt figé ; elle n'est pas une correction de ces essais.
