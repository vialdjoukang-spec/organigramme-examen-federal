# Journal · Veilles et automates · Argos

Chaque entrée porte une date (Europe/Zurich), une décision et les sources lues. Aucune donnée personnelle n’entre dans ce journal public.

- Le chantier démarre à sa phase (plan v2, section 3) ; aucune entrée pour l’instant.

## 17.10.2026 · Phase 1 · Ve1 et Ve2 (Argos)
- J’ai lu les robots.txt le 17.10.2026 : celui de www.bag.admin.ch autorise tout (`Disallow:` vide) ; healthreg-online.admin.ch renvoie sa page d’application au lieu d’un robots.txt, si bien qu’aucune règle n’interdit l’accès. Le script relit robots.txt avant chaque requête.
- Ve1 lit les deux pages OFSP (examen et inscription) et garde les titres et les liens de la zone `<main>` ; un nouveau lien PDF portant « 2027 » est signalé dans le ticket. Le workflow tourne chaque jour, mais le script ne lit les pages que le lundi, et chaque jour du 1.12 au 31.03, comme le plan l’exige.
- Ve2 rend le portail healthreg avec Playwright et garde les dates et les titres ; le premier rendu affiche la période du 15 décembre 2026 au 31 mars 2027.
- Écart au squelette : main est protégée, si bien que veille/etat.json s’enregistre sur la branche non protégée `veille-etat`. Parade aux 60 jours : chaque workflow se réactive lui-même par l’API (`PUT …/enable`) pendant la première semaine du mois et à chaque lancement manuel ; Janus vérifie au bout d’un mois que cette parade suffit.
- J’ai vérifié en local qu’une modification simulée produit un ticket, et qu’une page inchangée n’en produit aucun ; deux échecs consécutifs ouvrent un ticket d’échec, et un échec ne produit jamais de faux changement.
