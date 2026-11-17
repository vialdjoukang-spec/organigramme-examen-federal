/** Petits utilitaires DOM sans dépendance. */
window.JEU = window.JEU || {};
JEU.dom = (function () {
  /** h("div", {class:"x", onclick: fn}, enfant1, "texte", ...) */
  function h(tag, attrs, ...kids) {
    const el = document.createElement(tag);
    Object.entries(attrs || {}).forEach(([k, v]) => {
      if (v === null || v === undefined || v === false) return;
      if (k.startsWith("on") && typeof v === "function") el.addEventListener(k.slice(2), v);
      else if (k === "class") el.className = v;
      else if (k === "html") el.innerHTML = v;
      else el.setAttribute(k, v === true ? "" : v);
    });
    kids.flat(Infinity).forEach(k => { if (k !== null && k !== undefined && k !== false) el.append(k.nodeType ? k : document.createTextNode(String(k))); });
    return el;
  }
  const $ = (sel, root = document) => root.querySelector(sel);
  const reducedMotion = () => window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  /** Rejoue une classe d’animation (shake, glow…). */
  function pulse(el, cls) {
    if (!el) return;
    el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls);
    el.addEventListener("animationend", () => el.classList.remove(cls), { once: true });
  }
  const dateFr = iso => new Date(iso).toLocaleString("fr-CH", { dateStyle: "short", timeStyle: "short" });
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
  const mmss = s => { const n = Math.max(0, Math.round(s)); return `${String(Math.floor(n / 60)).padStart(2, "0")}:${String(n % 60).padStart(2, "0")}`; };
  const pct = x => x === null || x === undefined ? "—" : `${Math.round(x * 100)} %`;
  return { h, $, $$, reducedMotion, pulse, dateFr, mmss, pct };
})();
