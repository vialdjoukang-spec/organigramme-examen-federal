// Extrait tout le texte affiché (cartes + cas) pour le contrôle de reprise textuelle (tests/check_overlap.py).
const { charger } = require("../tools/charger");
const J = charger(); const out = []; const skip = ["url", "id", "lu_le", "titre", "editeur", "portee"];
const walk = (o, k) => { if (typeof o === "string") { if (!skip.includes(k)) out.push(o); } else if (o && typeof o === "object") for (const kk in o) walk(o[kk], kk); };
walk(J.specialites); console.log(out.join("\n"));
