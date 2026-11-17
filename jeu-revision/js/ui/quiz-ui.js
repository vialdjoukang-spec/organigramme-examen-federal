/**
 * Duels courts (vue « quiz ») : mode Fondamentaux (échelons 1–2 d’une spécialité)
 * et « Ronde » du jour (20 min, points faibles d’abord). Même confiance que le plateau.
 */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.quiz = (function () {
  const { h, $, mmss, reducedMotion } = JEU.dom;
  let S = null;   // { type, sp, file, i, q, choisi, reponse, t0, debut, bons, n, fin }
  let minuteur = null;

  function demarrer(type, sp) {
    const file = (type === "fondamentaux" ? JEU.quiz.fondamentaux(sp) : JEU.quiz.ronde()).map(JEU.quiz.instancier);
    S = { type, sp, file, i: 0, choisi: null, reponse: null, debut: JEU.horloge.now(), bons: 0, n: 0, fin: false };
    JEU.app.montrer("quiz", true);
    nouvelle();
    clearInterval(minuteur);
    if (type === "ronde") minuteur = setInterval(tic, 1000);
  }
  const restantMs = () => JEU.progression.RONDE_MS - (JEU.horloge.now() - S.debut);
  function tic() {
    if (!S || S.fin) return clearInterval(minuteur);
    const el = $("#ronde-chrono"); if (el) el.textContent = mmss(restantMs() / 1000);
    if (restantMs() <= 0 && !S.reponse) terminer("Les 20 minutes sont écoulées.");
  }
  function nouvelle() { S.q = S.file[S.i]; S.choisi = null; S.reponse = null; S.t0 = JEU.horloge.now(); render(); const b = $(".quiz-choix .choix"); if (b) b.focus(); }

  function render() {
    const root = $("#vue-quiz");
    if (!S) { root.replaceChildren(h("section", { class: "page" }, h("h1", {}, "Aucune série en cours."), h("button", { type: "button", class: "btn btn-primaire", onclick: () => demarrer("ronde") }, "Lancer la Ronde du jour"))); return; }
    const titre = S.type === "ronde" ? "Ronde du jour" : `Fondamentaux · ${JEU.registry.specialite(S.sp).nom}`;
    const tete = h("header", { class: "page-tete quiz-tete" },
      h("p", { class: "sur-titre" }, titre, S.q && !S.fin ? ` · question ${S.i + 1}/${S.file.length}` : ""),
      S.type === "ronde" ? h("p", { class: "ronde-chrono-bloc" }, "Temps restant ", h("span", { id: "ronde-chrono", class: "chrono", role: "timer" }, mmss(Math.max(0, restantMs()) / 1000))) : null);
    if (S.fin || !S.q) {
      root.replaceChildren(h("section", { class: "page quiz" }, tete,
        h("div", { class: "debrief debrief--ok", id: "quiz-fin" }, h("h3", {}, S.file.length ? "Série terminée." : "Rien à réviser pour l’instant."),
          h("p", {}, S.motif || (S.file.length ? `${S.bons} bonne(s) réponse(s) sur ${S.n}.` : "Joue un cas ou les fondamentaux : la Ronde se nourrit de tes coups.")),
          h("div", { class: "debrief-actions" },
            h("button", { type: "button", class: "btn btn-primaire", onclick: () => JEU.app.montrer("tableau") }, "Voir le tableau de bord"),
            h("button", { type: "button", class: "btn", onclick: () => JEU.app.montrer("parcours") }, "Retour au parcours")))));
      return;
    }
    const q = S.q, ech = JEU.progression.ECHELONS[q.ech - 1];
    const choisiTxt = S.choisi && q.choix.find(c => c.id === S.choisi).t;
    root.replaceChildren(h("section", { class: "page quiz", "aria-labelledby": "quiz-q" }, tete,
      h("div", { class: "quiz-carte" },
        h("p", { class: "phase" }, h("span", { class: "tag-phase" }, `Échelon ${ech[0]} · ${ech[1]}`), q.raison ? h("span", { class: "tag-raison" }, q.raison) : null),
        h("blockquote", { class: "quiz-enonce" }, q.enonce),
        h("h2", { id: "quiz-q", class: "quiz-question" }, q.question || "Choisis la bonne réponse."),
        h("div", { class: "quiz-choix", role: "group", "aria-label": "Réponses" }, q.choix.map((c, i) => {
          const etat = S.reponse ? (c.juste ? "juste" : c.id === S.reponse.choix ? "faux" : "") : (c.id === S.choisi ? "choisi" : "");
          return h("button", { type: "button", class: `choix choix--${etat}`, "data-choix": c.id, "aria-pressed": String(c.id === S.choisi), disabled: !!S.reponse,
            onclick: () => choisir(c.id) }, h("span", { class: "raccourci", "aria-hidden": "true" }, String(i + 1)), c.t);
        })),
        S.choisi && !S.reponse ? JEU.ui.confiance.panneau(`Réponse : ${choisiTxt}`, valider, () => { S.choisi = null; render(); }) : null,
        S.reponse ? retour() : null)));
  }
  function retour() {
    const q = S.q, ok = S.reponse.ok, cl = q.explication || {};
    const carte = JEU.registry.pathologie(q.pa).carte;
    return h("div", { id: "feedback", class: `feedback ${ok ? "feedback--bon" : "feedback--erreur"} ${reducedMotion() ? "" : "anim-joue"}`, role: "status", "aria-live": "polite" },
      h("span", { class: "feedback-tag" }, ok ? "Juste" : "Faux"),
      h("span", {}, ok ? "Tu relies ce constat à la bonne pathologie." : `La réponse attendue est : ${JEU.registry.pathologie(q.juste || q.pa).nom}.`, " ", cl.t ? h("em", {}, cl.t) : null),
      h("button", { type: "button", class: "btn btn-lien", onclick: () => JEU.ui.fiche.open(carte) }, "Ouvrir la fiche"),
      h("button", { type: "button", class: "btn btn-primaire", id: "btn-q-suivante", onclick: suivante }, S.i < S.file.length - 1 ? "Question suivante" : "Terminer"));
  }
  function choisir(id) { if (S.reponse) return; S.choisi = id; JEU.son.jouer("bip"); render(); const p = $("#confiance"); if (p) p.focus(); }
  function valider(conf) {
    if (!S.choisi || S.reponse) return;
    const q = S.q, c = q.choix.find(x => x.id === S.choisi), ok = !!c.juste;
    const carte = JEU.registry.pathologie(q.pa).carte;
    JEU.progression.enregistrer({ sp: q.sp, pa: q.pa, ech: q.ech, src: S.type === "ronde" ? "ronde" : "fond", q: q.id, carte, rep: c.id,
      v: ok ? "bon" : "erreur", g: ok ? null : "mineure", conf, ms: JEU.horloge.now() - S.t0, mode: S.type, fiche: carte });
    S.reponse = { ok, choix: c.id, conf }; S.n++; if (ok) S.bons++;
    JEU.son.jouer(ok ? "valide" : "alerte");
    render(); const b = $("#btn-q-suivante"); if (b) b.focus();
  }
  function suivante() {
    if (S.type === "ronde" && restantMs() <= 0) return terminer("Les 20 minutes sont écoulées.");
    if (S.i < S.file.length - 1) { S.i++; nouvelle(); } else terminer();
  }
  function terminer(motif) {
    S.fin = true; S.motif = motif ? `${motif} ${S.bons} bonne(s) réponse(s) sur ${S.n}.` : null; clearInterval(minuteur);
    if (S.type === "ronde") JEU.progression.enregistrerRonde({ n: S.n, bons: S.bons, dureeMs: JEU.horloge.now() - S.debut, complete: !motif || /écoulées/.test(motif) });
    render(); const b = $("#quiz-fin button"); if (b) b.focus();
  }
  function onKey(ev) {
    if (!S || S.fin || $("#fiche").open || document.body.dataset.vue !== "quiz" || ev.target.matches("input, textarea, select")) return;
    if (ev.key === "Escape" && S.choisi && !S.reponse) { S.choisi = null; return render(); }
    const conf = JEU.ui.confiance.touche(ev);
    if (conf && S.choisi && !S.reponse) { ev.preventDefault(); return valider(conf); }
    const n = parseInt(ev.key, 10);
    if (!S.reponse && n >= 1 && n <= S.q.choix.length) choisir(S.q.choix[n - 1].id);
  }
  function init() { document.addEventListener("keydown", onKey); render(); }
  return { init, demarrer, render, etat: () => S };
})();
