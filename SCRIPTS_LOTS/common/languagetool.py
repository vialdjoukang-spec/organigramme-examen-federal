"""Client LanguageTool ÉCONOME pour l'API publique (https://api.languagetool.org/v2/check).
Contraintes publiques : ~20 req/min/IP (pointe), 75 Ko/min, 20 Ko/requête, POST seulement ; les CGU déconseillent
l'automatisation. Conception : regroupement par section, cache par empreinte, budget partagé par les deux agents
(10 req/min, 60 Ko/min) via un seau à verrou de fichier, recul sur 429, jamais bloquant (« NON VÉRIFIÉ »)."""
import hashlib, re, json, sqlite3, time, urllib.parse, urllib.request, urllib.error
from pathlib import Path
from token_bucket import SeauPartage

class LanguageTool:
    def __init__(self, cfg):
        self.c = cfg["languagetool"]; self.ua = cfg["user_agent"]
        self.seau = SeauPartage(Path(cfg["shared_state_dir"]) / "languagetool", "lt_public",
                                self.c["budget_req_per_min"] / 60.0, max(1, self.c["budget_req_per_min"] // 2),
                                self.c["budget_bytes_per_min"] / 60.0, self.c["max_bytes_per_request"] * 1.2)
        Path(cfg["cache_dir"]).mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(Path(cfg["cache_dir"]) / "languagetool.sqlite"), timeout=30)
        self.db.execute("create table if not exists lt(h text primary key, t real, res text)")
        self.appels = 0

    @staticmethod
    def decouper(texte, maxi):
        """Blocs ≤ maxi octets, coupés aux frontières de phrase."""
        blocs, cour = [], ""
        for ph in re.split(r"(?<=[.!?…])\s+", texte.replace("\n", " ")):
            ph = ph.strip()
            if not ph: continue
            ph += " "
            if len((cour + ph).encode()) > maxi and cour:
                blocs.append(cour.strip()); cour = ""
            while len(ph.encode()) > maxi:
                blocs.append(ph[: maxi // 2]); ph = ph[maxi // 2:]
            cour += ph
        if cour.strip(): blocs.append(cour.strip())
        return blocs

    def verifier(self, texte):
        """Retourne {'statut': 'ok'|'NON VÉRIFIÉ', 'correspondances': [...], 'raison': ...}. Ne bloque jamais, ne lève jamais."""
        try:
            return self._verifier(texte)
        except Exception as e:      # toute panne interne devient « NON VÉRIFIÉ » : la relecture continue
            return {"statut": "NON VÉRIFIÉ", "raison": f"erreur interne {type(e).__name__}", "correspondances": []}

    def _verifier(self, texte):
        if not self.c.get("enabled", True):
            return {"statut": "NON VÉRIFIÉ", "raison": "LanguageTool désactivé", "correspondances": []}
        res, raison = [], None
        for bloc in self.decouper(texte, self.c["max_bytes_per_request"]):
            h = hashlib.sha256((self.c["language"] + "\0" + bloc).encode()).hexdigest()
            r = self.db.execute("select res from lt where h=?", (h,)).fetchone()
            if r:
                res.extend(json.loads(r[0])); continue
            if self.appels >= self.c["max_requests_per_pass"]:
                raison = "budget du passage atteint (reporté au passage suivant)"; break
            if not self.seau.prendre(octets=len(bloc.encode()), attente_max=2):
                raison = "budget partagé de 10 req/min épuisé ou recul en cours"; break
            try:
                self.appels += 1
                data = urllib.parse.urlencode({"text": bloc, "language": self.c["language"], "level": "default"}).encode()
                req = urllib.request.Request(self.c["url"], data=data, method="POST",
                                             headers={"User-Agent": self.ua, "Accept": "application/json"})
                with urllib.request.urlopen(req, timeout=self.c["timeout_s"]) as rep:
                    doc = json.loads(rep.read())
                self.seau.succes()
                m = [{"message": x.get("message"), "regle": x.get("rule", {}).get("id"), "categorie": x.get("rule", {}).get("category", {}).get("id"),
                      "contexte": x.get("context", {}).get("text", "")[:120], "suggestions": [s["value"] for s in x.get("replacements", [])[:2]]}
                     for x in doc.get("matches", [])]
                self.db.execute("insert or replace into lt values(?,?,?)", (h, time.time(), json.dumps(m, ensure_ascii=False))); self.db.commit()
                res.extend(m)
            except urllib.error.HTTPError as e:
                if e.code in (429, 503):
                    ra = e.headers.get("Retry-After"); self.seau.reculer(int(ra) if ra and ra.isdigit() else None)
                raison = f"HTTP {e.code}"; break
            except Exception as e:
                raison = f"{type(e).__name__}"; break
        return {"statut": "ok" if raison is None else "NON VÉRIFIÉ", "raison": raison, "correspondances": res}
