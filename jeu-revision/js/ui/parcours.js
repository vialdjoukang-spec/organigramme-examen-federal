/**
 * Carte du parcours : une salle par spécialité, groupées par lot (PLAN_PRODUCTION.md).
 * Chaque salle montre son cycle : Fondamentaux → Consultation → Urgence → Cas final.
 * Déblocage : 2 étoiles de moyenne sur la spécialité précédente, ou mode Entraînement.
 * Une étape sans contenu ne bloque pas la suivante ; le cas final s’ouvre après les étapes jouables.
 */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.parcours = (function () {
  const { h, $, pct } = JEU.dom;
  const KEY = "revmed.entrainement";
  const entrainement = () => { try { return localStorage.getItem(KEY) === "1"; } catch (e) { return false; } };
  const setEntrainement = v => { try { localStorage.setItem(KEY, v ? "1" : "0"); } catch (e) { /* */ } };

  /** Meilleures étoiles par cas, hors examen blanc. */
  function meilleures() {
    const m = {};
    JEU.progression.get().parties.forEach(p => { if (p.mode !== "examen") m[p.cas] = Math.max(m[p.cas] || 0, p.etoiles || 0); });
    return m;
  }
  function moyenne(casL) { const m = meilleures(); return casL.length ? casL.reduce((a, k) => a + (m[k.id] || 0), 0) / casL.length : null; }

  function cycle(spId) {
    const qF = JEU.quiz.fondamentaux(spId).length;
    const stF = (() => { const L = JEU.progression.get().coups.filter(c => c.sp === spId && c.ech && c.ech <= 2 && c.v); const b = L.filter(c => c.v === "bon").length; return L.length >= Math.min(5, qF) && L.length && b / L.length >= 0.7; })();
    const etape = (mode) => { const L = JEU.registry.casDe(spId, mode); const moy = moyenne(L); return { n: L.length, cas: L, moyenne: moy, reussi: L.length > 0 && moy >= 2 }; };
    const C = { fondamentaux: { n: qF, reussi: stF }, consultation: etape("consultation"), urgence: etape("urgence"), final: etape("final") };
    const prets = ["fondamentaux", "consultation", "urgence"].every(k => !C[k].n || C[k].reussi);
    C.final.ouvert = entrainement() || prets;
    return C;
  }
  /** État de chaque salle : ouverte, verrouillée ou en préparation. */
  function etats() {
    const ordre = JEU.registry.ordreParcours();
    let precedente = null;
    return ordre.map(s => {
      const sp = JEU.registry.specialite(s.id);
      let etat = "preparation";
      if (sp) {
        const casL = JEU.registry.casDe(s.id);
        if (!precedente || entrainement()) etat = "ouverte";
        else etat = (moyenne(JEU.registry.casDe(precedente)) || 0) >= 2 ? "ouverte" : "verrouillee";
        precedente = casL.length ? s.id : precedente;
      }
      return Object.assign({ etat, donnees: sp || null }, s);
    });
  }

  function render() {
    const root = $("#vue-parcours");
    const E = etats();
    const g = JEU.progression.grade(JEU.registry.pathologies());
    const casExamen = JEU.registry.tousLesCas().filter(k => k.mode !== "consultation");
    root.replaceChildren(h("section", { class: "page parcours", "aria-labelledby": "parcours-titre" },
      h("header", { class: "page-tete" },
        h("p", { class: "sur-titre" }, "Internat · Parcours"),
        h("h1", { id: "parcours-titre" }, "Fais le tour des services."),
        h("p", {}, `Grade : `, h("strong", { id: "grade" }, g.grade), ` · ${g.n}/${g.total} pathologies maîtrisées (${pct(g.part)}).`,
          g.suivant ? ` Prochain grade : ${g.suivant.grade} à ${Math.round(g.suivant.seuil * 100)} %.` : ""),
        h("label", { class: "interrupteur" }, h("input", { type: "checkbox", id: "chk-entrainement", checked: entrainement() || null,
          onchange: ev => { setEntrainement(ev.target.checked); render(); } }), " Mode Entraînement : toutes les salles ouvertes, sans chronomètre.")),
      h("div", { class: "lots" }, JEU.parcours.map(lot => h("section", { class: "lot", "aria-labelledby": `lot-${lot.id}` },
        h("h2", { id: `lot-${lot.id}`, class: "bloc-titre" }, `Lot ${lot.id} · ${lot.nom}`),
        h("ol", { class: "salles" }, lot.specialites.map(s => salle(E.find(x => x.id === s.id))))))),
      h("section", { class: "examen-blanc", "aria-labelledby": "eb-titre" },
        h("h2", { id: "eb-titre" }, "Examen blanc PROFILES"),
        h("p", {}, "Il mêle les cas de toutes les spécialités, sous chronomètre, et les note comme à l’examen. Structure prête ; le contenu arrive avec les lots."),
        h("button", { type: "button", class: "btn", id: "btn-examen-blanc", disabled: casExamen.length ? null : true,
          onclick: () => JEU.ui.board.demarrerExamen(casExamen.map(k => k.id)) }, `Lancer la démonstration (${casExamen.length} cas)`))));
  }

  function salle(s) {
    if (!s.donnees) return h("li", { class: "salle salle--preparation", "data-specialite": s.id },
      h("span", { class: "salle-nom" }, s.nom), h("span", { class: "salle-etat" }, "En préparation"));
    const C = cycle(s.id), ouverte = s.etat === "ouverte";
    const pas = (cle, titre, n, reussi, action, ouvert = true) => h("li", { class: `pas ${reussi ? "pas--reussi" : ""} ${!n ? "pas--vide" : ""}`, "data-pas": cle },
      h("span", { class: "pas-titre" }, titre),
      h("span", { class: "pas-info" }, !n ? "à produire" : reussi ? "réussi" : `${n} ${cle === "fondamentaux" ? "question(s)" : "cas"}`),
      n && ouverte && ouvert ? action : null);
    const boutonsCas = L => h("span", { class: "pas-actions" }, L.map(k => h("button", { type: "button", class: "btn btn-petit", "data-cas": k.id, onclick: () => JEU.ui.board.demarrer(k.id) }, k.titre)));
    return h("li", { class: `salle salle--${s.etat}`, "data-specialite": s.id },
      h("div", { class: "salle-tete" }, h("span", { class: "salle-nom" }, s.nom),
        h("span", { class: "salle-etat" }, ouverte ? "Ouverte" : "Verrouillée · 2 étoiles de moyenne sur la salle précédente")),
      h("ol", { class: "cycle", "aria-label": `Cycle ${s.nom}` },
        pas("fondamentaux", "1 · Fondamentaux", C.fondamentaux.n, C.fondamentaux.reussi,
          h("button", { type: "button", class: "btn btn-petit", id: `btn-fond-${s.id}`, onclick: () => JEU.ui.quiz.demarrer("fondamentaux", s.id) }, "Jouer")),
        pas("consultation", "2 · Consultation", C.consultation.n, C.consultation.reussi, boutonsCas(C.consultation.cas)),
        pas("urgence", "3 · Urgence", C.urgence.n, C.urgence.reussi, boutonsCas(C.urgence.cas)),
        pas("final", "4 · Cas final", C.final.n, C.final.reussi, boutonsCas(C.final.cas), C.final.ouvert)));
  }
  return { render, entrainement, etats, cycle, moyenne };
})();
