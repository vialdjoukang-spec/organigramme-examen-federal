/**
 * Sons synthétisés (Web Audio API) : aucun fichier, aucune licence.
 * bip (moniteur), valide, alerte, victoire, etoile. Bouton muet mémorisé.
 * Par défaut : muet si l’utilisateur préfère le mouvement réduit. Le contexte audio
 * ne se crée qu’après un geste de l’utilisateur (règle des navigateurs).
 */
window.JEU = window.JEU || {};
JEU.son = (function () {
  const KEY = "revmed.son";
  let ctx = null;
  const trace = [];            // sons demandés (contrôlés par les tests)
  function prefere() {
    try { const v = localStorage.getItem(KEY); if (v !== null) return v === "on"; } catch (e) { /* */ }
    return !(window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches);
  }
  let actif = prefere();
  function setActif(v) { actif = !!v; try { localStorage.setItem(KEY, actif ? "on" : "off"); } catch (e) { /* */ } }
  function audio() {
    if (!ctx) { const A = window.AudioContext || window.webkitAudioContext; if (!A) return null; ctx = new A(); }
    if (ctx.state === "suspended") ctx.resume();
    return ctx;
  }
  function note(f, t0, dur, type = "sine", gain = 0.08) {
    const a = audio(); if (!a) return;
    const o = a.createOscillator(), g = a.createGain();
    o.type = type; o.frequency.value = f;
    const t = a.currentTime + t0;
    g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(gain, t + 0.01); g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    o.connect(g).connect(a.destination); o.start(t); o.stop(t + dur + 0.02);
  }
  const SONS = {
    bip: () => note(1000, 0, 0.09, "sine", 0.05),
    valide: () => { note(660, 0, 0.12, "triangle"); note(880, 0.09, 0.16, "triangle"); },
    alerte: () => { note(440, 0, 0.16, "square", 0.04); note(330, 0.16, 0.22, "square", 0.04); },
    victoire: () => [523, 659, 784, 1047].forEach((f, i) => note(f, i * 0.11, 0.22, "triangle")),
    etoile: () => note(1319, 0, 0.15, "sine", 0.05)
  };
  function jouer(nom) {
    trace.push({ nom, joue: actif });
    if (!actif || !SONS[nom]) return false;
    try { SONS[nom](); } catch (e) { return false; }
    return true;
  }
  return { jouer, actif: () => actif, setActif, trace, SONS: Object.keys(SONS) };
})();
