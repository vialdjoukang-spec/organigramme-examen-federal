/**
 * Questions sur l’échelle à 7 échelons (PROGRESSION.md § 1) et construction de la « Ronde ».
 * Deux sources de questions :
 *  1. questions rédigées (spécialité.questions, validées par le schéma) ;
 *  2. questions automatiques : une affirmation sourcée d’une rubrique devient
 *     « À quelle pathologie se rattache ce constat ? ». Les affirmations ambiguës
 *     (présentes dans plusieurs fiches, qui nomment une autre pathologie, ou marquées
 *     « quiz: false » par l’auteur car valables pour plusieurs pathologies) sont écartées.
 */
window.JEU = window.JEU || {};
JEU.alea = JEU.alea || Math.random;
JEU.quiz = (function () {
  /** Rubrique → échelon. Les fondamentaux valent 2 (mécanisme) sauf « echelon: 1 ». */
  const ECH = { fondamentaux: 2, demarche: 3, differentiels: 4, exploration: 5, diagnostic: 6, priseEnCharge: 7, suivi: 7 };
  const norm = s => s.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  const melanger = a => { const b = [...a]; for (let i = b.length - 1; i > 0; i--) { const j = Math.floor(JEU.alea() * (i + 1)); [b[i], b[j]] = [b[j], b[i]]; } return b; };

  function noms(p) {
    const c = JEU.registry.card(p.carte) || {};
    return [p.nom, c.nom, c.court].filter(Boolean);
  }
  const motRe = m => new RegExp(`(?<![\\p{L}\\p{N}])${m.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}(?![\\p{L}\\p{N}])`, "giu");
  /** Masque le nom de la pathologie (mot entier) pour ne pas donner la réponse. */
  function masquer(t, mots) { let x = t; mots.forEach(m => { x = x.replace(motRe(m), "[…]"); }); return x; }
  const nomme = (t, mots) => mots.some(m => motRe(norm(m)).test(norm(t)));

  let cache = null;
  function construire() {
    const qs = [];
    JEU.specialites.forEach(sp => {
      const P = sp.pathologies.filter(p => JEU.registry.card(p.carte));
      const compte = {};
      P.forEach(p => Object.values(JEU.registry.card(p.carte).rubriques).flat().forEach(cl => { compte[cl.t] = (compte[cl.t] || 0) + 1; }));
      P.forEach(p => {
        const c = JEU.registry.card(p.carte);
        const autres = P.filter(x => x.id !== p.id);
        Object.entries(ECH).forEach(([rub, e0]) => (c.rubriques[rub] || []).forEach((cl, i) => {
          if (cl.na || cl.quiz === false || !cl.s.length || /À vérifier/.test(cl.t) || compte[cl.t] > 1) return;
          const enonce = masquer(cl.t, noms(p));
          if (autres.some(a => nomme(enonce, noms(a)))) return;
          qs.push({ id: `auto:${p.id}:${rub}:${i}`, auto: true, sp: sp.id, pa: p.id, ech: cl.echelon || e0, rub,
            enonce, question: "À quelle pathologie se rattache ce constat ?", juste: p.id,
            candidats: P.map(x => x.id), explication: cl });
        }));
      });
      (sp.questions || []).forEach(q => qs.push(Object.assign({ sp: sp.id, pa: q.pathologie, ech: q.echelon, redigee: true }, q)));
    });
    cache = qs; return qs;
  }
  const toutes = () => cache || construire();
  const pour = (pa, ech) => toutes().filter(q => q.pa === pa && q.ech === ech);

  /** Prépare une question jouable : 4 choix au plus, ordre aléatoire. */
  function instancier(q) {
    if (q.redigee) return Object.assign({}, q, { choix: melanger(q.choix.map((c, i) => ({ id: "c" + i, t: c.t, juste: !!c.juste }))) });
    const autres = melanger(q.candidats.filter(id => id !== q.juste)).slice(0, 3);
    const choix = melanger([q.juste, ...autres]).map(id => ({ id, t: JEU.registry.pathologie(id).nom, juste: id === q.juste }));
    return Object.assign({}, q, { choix });
  }
  /** Mode Fondamentaux : échelons 1 et 2 d’une spécialité. */
  const fondamentaux = sp => melanger(toutes().filter(q => q.sp === sp && q.ech <= 2));

  /**
   * Ronde du jour (20 min) : angles morts, puis cartes Leitner dues (boîte basse d’abord),
   * puis cases faibles de la carte de chaleur, puis échelons jamais vus.
   */
  function ronde() {
    const vu = new Set(), file = [];
    const ajoute = (pa, ech, raison) => {
      const k = `${pa}|${ech}`; if (vu.has(k)) return;
      const L = pour(pa, ech); if (!L.length) return;
      vu.add(k); file.push(Object.assign({ raison }, L[Math.floor(JEU.alea() * L.length)]));
    };
    const P = JEU.progression;
    P.dues().forEach(x => ajoute(x.pa, x.ech, x.angleMort ? "Angle mort" : x.rappel ? "Rappel J+30" : `Leitner · boîte ${x.boite}`));
    const ch = P.chaleur();
    const faibles = Object.entries(ch).filter(([, v]) => v.precision < P.SEUIL_FAIBLE).sort((a, b) => a[1].precision - b[1].precision);
    faibles.forEach(([k]) => { const [sp, ech] = k.split("|"); toutes().filter(q => q.sp === sp && q.ech === +ech).forEach(q => ajoute(q.pa, q.ech, "Case faible")); });
    const it = P.items();
    melanger(toutes()).forEach(q => { if (!it[`${q.pa}|${q.ech}`]) ajoute(q.pa, q.ech, "Nouveau"); });
    return file;
  }
  /** Échelons sans aucune question pour une pathologie (rapport de couverture). */
  function echelonsVides(pa) { return [1, 2, 3, 4, 5, 6, 7].filter(e => !pour(pa, e).length); }

  return { ECH, toutes, pour, instancier, fondamentaux, ronde, echelonsVides, reset: () => { cache = null; } };
})();
