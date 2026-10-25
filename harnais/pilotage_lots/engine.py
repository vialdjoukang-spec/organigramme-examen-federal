"""Contrôles de preuves V0, en lecture seule. Aucun audit clinique ni attribution."""
from datetime import datetime, timedelta
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import PurePosixPath
import json
import math
import re

from harnais.surveillance.watchdog import EXPECTED_VERSIONS, MODEL, REVISION, TOOLS


ROLES = ("medical", "linguistique", "visual")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def digest(raw):
    return sha256(raw).hexdigest()


def instant(value):
    if not isinstance(value, str):
        raise ValueError("Date absente")
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("Date sans fuseau")
    return result


def own_path(lot, value):
    if not isinstance(lot, str) or not re.fullmatch(r"LOT_\d{3}", lot) or not 1 <= int(lot[4:]) <= 248:
        raise ValueError("Lot hors PROFILES")
    if not isinstance(value, str):
        raise ValueError("Chemin absent")
    path = PurePosixPath(value)
    root = PurePosixPath("lot en cours de production") / lot
    if path.is_absolute() or ".." in path.parts or not path.is_relative_to(root) or path == root:
        raise ValueError("Chemin hors du lot")
    return str(path)


def validate_state(state):
    if not isinstance(state, dict) or state.get("schema_version") != 2 or state.get("prompt") != "V0":
        raise ValueError("Registre V0 attendu ; registre V8 refusé")
    if state.get("status") not in {"active", "paused", "blocked", "finished", "quota_exhausted"}:
        raise ValueError("État invalide")
    if type(state.get("stop_requested")) is not bool or state.get("automatic_assignment") is not False:
        raise ValueError("Arrêt explicite et attribution automatique interdite requis")
    jobs = state.get("jobs")
    if not isinstance(jobs, list):
        raise ValueError("Affectations absentes")
    lots, workers = set(), set()
    for job in jobs:
        if not isinstance(job, dict):
            raise ValueError("Affectation non structurée")
        lot, worker = job.get("lot"), job.get("worker")
        own_path(lot or "", "lot en cours de production/" + (lot or "") + "/DECISION_SEANCE.md")
        if lot in lots or not isinstance(worker, str) or not worker or worker in workers:
            raise ValueError("Lot dupliqué ou responsable affecté à plusieurs lots")
        lots.add(lot)
        workers.add(worker)
        if not isinstance(job.get("writers"), list) or worker not in job["writers"]:
            raise ValueError("Auteurs non déclarés")
        if any(not isinstance(x, str) or not x for x in job["writers"]):
            raise ValueError("Identité d'auteur invalide")
        if not isinstance(job.get("branch"), str) or not job["branch"]:
            raise ValueError("Branche absente")
    return state


def layout(session):
    lot = session["lot"]
    expected_a = f"{lot}_Phase_A_V0_SSP_et_10DD.html"
    phase_a, phase_b = session.get("phase_a"), session.get("phase_b")
    if not isinstance(phase_a, dict) or phase_a.get("name") != expected_a or phase_a.get("entities") != [{"code": "SSP", "id": "ssp"}]:
        raise ValueError("Nom ou entité de Phase A invalide")
    if not isinstance(phase_b, list) or not phase_b:
        raise ValueError("Découpage Phase B absent")
    covered = []
    for k, part in enumerate(phase_b, 1):
        a, b = part.get("start"), part.get("end")
        if type(a) is not int or type(b) is not int or not 1 <= a <= b <= 10:
            raise ValueError("Plage DX invalide")
        if part.get("name") != f"{lot}_Phase_B_V0_Partie_{k}_DX.{a}_a_DX.{b}.html":
            raise ValueError("Nom Phase B incompatible avec la décision")
        entities = [{"code": f"DX.{i}", "id": f"dx{i}"} for i in range(a, b + 1)]
        if part.get("entities") != entities:
            raise ValueError("Entités incompatibles avec la plage DX")
        covered.extend(range(a, b + 1))
    if covered != list(range(1, 11)):
        raise ValueError("DX.1–DX.10 non couverts dans l'ordre, sans trou ni chevauchement")
    return [("A", phase_a)] + [(f"B{k}", part) for k, part in enumerate(phase_b, 1)]


def read_session(reader, head, job):
    lot = job["lot"]
    md = reader.file(own_path(lot, job["decision_path"]), head)
    raw = reader.file(own_path(lot, job["session_path"]), head)
    if digest(md) != job["decision_sha256"] or digest(raw) != job["session_sha256"]:
        raise ValueError("Décision de séance modifiée ou non liée à cette version")
    session = json.loads(raw)
    if not isinstance(session, dict):
        raise ValueError("Décision non structurée")
    if session.get("schema_version") != 1 or session.get("prompt") != "V0" or session.get("lot") != lot:
        raise ValueError("Décision V0 d'un autre lot ou schéma invalide")
    if session.get("worker") != job["worker"] or session.get("branch") != job["branch"] or session.get("writers") != job["writers"]:
        raise ValueError("Attribution différente de la décision")
    authority = session.get("authority", {})
    if authority.get("mode") not in {"direct", "delegated"} or not authority.get("instruction") or not authority.get("decided_by"):
        raise ValueError("Fondement de l'autorisation absent")
    if session.get("decision_sha256") != digest(md):
        raise ValueError("La décision lisible et sa transcription divergent")
    layout(session)
    return session


def verify_harness(reader, head, job, now):
    raw = reader.file(own_path(job["lot"], job["runtime_path"]), head)
    if digest(raw) != job["runtime_sha256"]:
        raise ValueError("Preuve runtime modifiée")
    proof = json.loads(raw)
    if not isinstance(proof, dict) or type(proof.get("schema_version")) is not int or proof["schema_version"] != 1 or proof.get("agent") != job["worker"] or proof.get("complete") is not True:
        raise ValueError("Harnais individuel non vert")
    age = (now - instant(proof.get("tested_at"))).total_seconds()
    if not -120 <= age <= 3600:
        raise ValueError("Test runtime périmé ou futur")
    tests = proof.get("tests", {})
    if not isinstance(tests, dict) or any(not isinstance(tests.get(tool), dict) or tests[tool].get("ok") is not True for tool in TOOLS):
        raise ValueError("Trois tests fonctionnels non démontrés")
    versions = proof.get("versions")
    if not isinstance(versions, dict) or any(versions.get(k) != v for k, v in EXPECTED_VERSIONS.items()):
        raise ValueError("Versions runtime non canoniques ou absentes")
    if not isinstance(proof.get("run_id"), str) or not proof["run_id"].strip():
        raise ValueError("Identifiant du test runtime absent")
    chunks = tests["chonkie"].get("chunks")
    if type(chunks) is not int or chunks < 2 or tests["chonkie"].get("exact_reconstruction") is not True:
        raise ValueError("Découpage réel et reconstruction Chonkie non démontrés")
    cached = tests["gptcache"]
    if cached.get("mode") != "exact-match" or cached.get("write_read") is not True or cached.get("distinct_key_miss") is not True:
        raise ValueError("Cache exact non démontré")
    compressed = tests["llmlingua"]
    before, after = compressed.get("origin_tokens"), compressed.get("compressed_tokens")
    if compressed.get("model") != MODEL or compressed.get("revision") != REVISION or type(before) is not int or type(after) is not int or not 0 < after < before:
        raise ValueError("Compression réelle canonique non démontrée")
    if proof.get("medical_source_compressed") is not False:
        raise ValueError("Absence de compression médicale non attestée")


class Shape(HTMLParser):
    """Délimite les monographies et mesure leur texte, fenêtres incluses."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.nodes, self.ids, self.errors = [], [], [], []
        self.declaration, self.html_closed = False, False

    def handle_decl(self, decl):
        self.declaration = decl.lower() == "doctype html"

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        parent = self.stack[-1] if self.stack else None
        node = {"tag": tag, "attrs": attrs, "parent": parent, "text": [], "closed": tag in VOID}
        self.nodes.append(node)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag in {"script", "img", "link", "iframe", "object", "embed", "svg", "image"} or "title" in attrs:
            self.errors.append("Élément ou attribut interdit")
        for name, value in attrs.items():
            if name.startswith("on") or name == "srcdoc":
                self.errors.append("Code actif dans un attribut HTML")
            if name in {"href", "src", "action", "formaction", "xlink:href"} and re.match(r"(?:javascript|vbscript|data):", re.sub(r"[\x00-\x20]", "", value or ""), re.I):
                self.errors.append("URL active ou incorporée interdite")
            if name == "style" and re.search(r"@import|url\s*\(|expression\s*\(", value or "", re.I):
                self.errors.append("Ressource ou code CSS interdit")
        if tag == "table" and not (parent and parent["tag"] == "div" and "overflow-x:auto" in parent["attrs"].get("style", "").replace(" ", "")):
            self.errors.append("Tableau non enveloppé")
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_data(self, text):
        if any(n["tag"] == "style" for n in self.stack) and re.search(r"@import|url\s*\(|expression\s*\(", text, re.I):
            self.errors.append("Ressource ou code CSS interdit")
        if any(n["tag"] in {"style", "script"} for n in self.stack):
            return
        for node in self.stack:
            node["text"].append(text)

    def handle_endtag(self, tag):
        if tag in VOID:
            self.errors.append("Fermeture d'une balise vide")
        elif not self.stack or self.stack[-1]["tag"] != tag:
            self.errors.append("Balises non équilibrées")
        else:
            self.stack.pop()["closed"] = True
            if tag == "html":
                self.html_closed = True


def text_of(node):
    return " ".join(" ".join(node["text"]).split())


def inside(node, root):
    parent = node["parent"]
    while parent is not None:
        if parent is root:
            return True
        parent = parent["parent"]
    return False


def technical(raw, spec):
    text = raw.decode("utf-8")
    parser = Shape()
    parser.feed(text)
    errors = list(parser.errors)
    marker = re.escape(spec["name"].removesuffix(".html"))
    if parser.stack or not parser.declaration or not parser.html_closed or not re.search(r"</html>\s*<!-- FIN_FICHIER " + marker + r" -->\s*$", text):
        errors.append("HTML5 incomplet ou marque de fin absente")
    if len(parser.ids) != len(set(parser.ids)):
        errors.append("Identifiant dupliqué")
    if max(map(len, text.splitlines()), default=0) > 3000:
        errors.append("Ligne supérieure à 3000 caractères")
    measurements = {}
    entity_ids = [n["attrs"].get("id") for n in parser.nodes if re.fullmatch(r"ssp|dx\d+", n["attrs"].get("id") or "")]
    if entity_ids != [entity["id"] for entity in spec["entities"]]:
        errors.append("Entités monographiques étrangères ou désordonnées")
    for entity in spec["entities"]:
        roots = [n for n in parser.nodes if n["attrs"].get("id") == entity["id"]]
        if len(roots) != 1 or roots[0]["tag"] != "details" or "open" not in roots[0]["attrs"]:
            errors.append(entity["code"] + ": monographie details open absente")
            continue
        root = roots[0]
        children = [n for n in parser.nodes if inside(n, root)]
        content_bytes = len(text_of(root).encode("utf-8"))
        measurements[entity["code"]] = content_bytes
        if not 150_000 <= content_bytes <= 200_000:
            errors.append(entity["code"] + ": contenu propre hors 150–200 Ko")
        points = [n["attrs"].get("id") for n in children if n["tag"] == "section"]
        if points != [f"{entity['id']}-p{i}" for i in range(1, 15)]:
            errors.append(entity["code"] + ": quatorze points absents, désordonnés ou mal délimités")
        if any(n["tag"] == "style" for n in children):
            errors.append(entity["code"] + ": CSS dans le contenu monographique")
    return errors, measurements, parser


def attestation(reader, head, job, record, basis, role, now):
    if not isinstance(record, dict) or record.get("file_sha256") != basis:
        raise ValueError("Audit absent ou portant sur une autre version")
    if role in {"medical", "linguistique"}:
        actor, score = record.get("auditor_id"), record.get("score")
        if not isinstance(actor, str) or not actor or actor in job["writers"]:
            raise ValueError("Audit non indépendant")
        if type(score) not in (int, float) or not math.isfinite(score) or not 90 <= score <= 100:
            raise ValueError("Score inférieur à 90 ou invalide")
        if record.get("role") != role or type(record.get("critical_count")) is not int or record["critical_count"] != 0 or record.get("full_read") is not True:
            raise ValueError("Audit incomplet ou critique restant")
        if record.get("final_question") != "oui":
            raise ValueError("Question finale sans oui : validation bloquée")
        if role == "medical" and record.get("critical_sources_read") is not True:
            raise ValueError("Sources critiques non lues")
        if record.get("v0_line_by_line_complete") is not True or record.get("condensation_preserves_clinical_data") is not True:
            raise ValueError("Contrôle V0 ligne à ligne ou conservation des données non attesté")
    elif role == "visual":
        if record.get("width_px") != 390 or record.get("performed") is not True or record.get("authorized_environment") is not True:
            raise ValueError("QA390 autorisée non démontrée")
    elif role == "delivery":
        if record.get("verified") is not True or record.get("destination") != "Drive Finaux" or record.get("mime_type") != "text/html" or not record.get("remote_file_id") or record.get("remote_sha256") != basis:
            raise ValueError("Livraison HTML et identité des octets non démontrées")
    else:
        raise ValueError("Rôle inconnu")
    checked = instant(record.get("checked_at"))
    if checked > now + timedelta(seconds=120):
        raise ValueError("Attestation future")
    report = reader.file(own_path(job["lot"], record.get("report_path")), head)
    if digest(report) != record.get("report_sha256"):
        raise ValueError("Empreinte du rapport différente")
    return checked


def canonical(reader, head, job, a_sha, validated_at):
    root = "lot en cours de production/" + job["lot"] + "/"
    raw = reader.file(root + "LISTE_DX_CANONIQUE.md", head).decode("utf-8")
    blocks = re.findall(r"```json\s*\n(.*?)\n```", raw, re.S)
    if len(blocks) != 1:
        raise ValueError("Liste canonique machine absente ou ambiguë")
    data = json.loads(blocks[0])
    if data.get("phase_a_sha256") != a_sha or instant(data.get("frozen_at")) < validated_at:
        raise ValueError("Gel non lié à la Phase A validée")
    dx = data.get("diagnoses")
    if not isinstance(dx, list) or [x.get("code") for x in dx] != [f"DX.{i}" for i in range(1, 11)]:
        raise ValueError("Liste canonique incomplète ou désordonnée")
    names = [x.get("name") for x in dx]
    if any(not isinstance(x, str) or not x.strip() for x in names) or len(set(names)) != 10:
        raise ValueError("Noms canoniques absents ou dupliqués")
    corrections = reader.file(root + "CORRECTIONS_AUDIT.md", head)
    if digest(corrections) != data.get("corrections_sha256"):
        raise ValueError("Corrections d'audit modifiées sans réalignement")
    return data


def evaluate_lot(reader, job, now):
    """Évalue un instantané fixe, sans produire ni déclarer un audit réel."""
    head = reader.head(job["branch"])
    result = {"lot": job["lot"], "branch": job["branch"], "head": head,
              "validated": False, "delivered": False, "clinical_validation": False,
              "decision_ready": False, "harness_ready": False,
              "files": {}, "next_action": None}

    def blocked(action, reason, file=None):
        result["next_action"] = {"action": action, "reason": str(reason)}
        if file:
            result["next_action"]["file"] = file
        return result

    try:
        session = read_session(reader, head, job)
        result["decision_ready"] = True
    except (ValueError, KeyError, TypeError, FileNotFoundError) as exc:
        return blocked("repair_session_decision", exc)
    try:
        verify_harness(reader, head, job, now)
        result["harness_ready"] = True
    except (ValueError, KeyError, TypeError, FileNotFoundError) as exc:
        return blocked("restore_individual_harness", exc)
    root = "lot en cours de production/" + job["lot"] + "/"
    try:
        package = json.loads(reader.file(root + "VALIDATION_V0.json", head))
        if not isinstance(package, dict) or package.get("schema_version") != 1 or not isinstance(package.get("files"), dict):
            raise ValueError("Dossier de validation invalide")
    except FileNotFoundError:
        package = {"files": {}}
    except (ValueError, TypeError) as exc:
        return blocked("repair_validation_record", exc)
    validated_a_at, frozen, parsers, audit_times = None, None, {}, []
    for key, spec in layout(session):
        if key != "A" and frozen is None:
            raise AssertionError("Phase B sans gel")
        try:
            raw = reader.file(root + spec["name"], head)
        except FileNotFoundError:
            return blocked("write_phase_a" if key == "A" else "write_phase_b", "Fichier absent", key)
        try:
            errors, sizes, parser = technical(raw, spec)
        except (UnicodeError, ValueError) as exc:
            return blocked("repair_html", exc, key)
        basis = digest(raw)
        result["files"][key] = {"sha256": basis, "bytes": len(raw), "entity_content_bytes": sizes, "technical_reserves": errors, "gates": {}}
        if errors:
            other = [e for e in errors if "contenu propre hors" not in e]
            if not other and any(size < 150_000 for size in sizes.values()):
                return blocked("complete_exhaustive_draft", "; ".join(errors), key)
            if not other and any(size > 200_000 for size in sizes.values()):
                return blocked("condense_preserving_data", "; ".join(errors), key)
            return blocked("repair_html", "; ".join(errors), key)
        entry = package["files"].get(key, {})
        if not isinstance(entry, dict):
            return blocked("repair_validation_record", "Entrée de fichier invalide", key)
        if key != "A":
            try:
                started = instant(entry.get("production_started_at"))
                if started < instant(frozen["frozen_at"]) or started > now + timedelta(seconds=120):
                    raise ValueError("Phase B commencée avant le gel ou dans le futur")
                for entity in spec["entities"]:
                    node = next(n for n in parser.nodes if n["attrs"].get("id") == entity["id"])
                    summaries = [n for n in parser.nodes if n["tag"] == "summary" and n["parent"] is node]
                    name = frozen["diagnoses"][int(entity["code"][3:]) - 1]["name"]
                    if len(summaries) != 1 or text_of(summaries[0]) != entity["code"] + " — " + name:
                        raise ValueError("Divergence critique du nom ou numéro canonique")
            except (ValueError, KeyError, TypeError, StopIteration) as exc:
                return blocked("realign_phase_b", exc, key)
        times, failures = [], []
        for role in ROLES:
            try:
                record = entry.get(role)
                checked = attestation(reader, head, job, record, basis, role, now)
                if role != "visual":
                    entities = record.get("entities", {})
                    wanted = {e["code"] for e in spec["entities"]}
                    if not isinstance(entities, dict) or set(entities) != wanted:
                        raise ValueError("Grille individuelle absente pour une monographie")
                    for grade in entities.values():
                        score = grade.get("score")
                        if type(score) not in (int, float) or not math.isfinite(score) or not 90 <= score <= 100 or type(grade.get("critical_count")) is not int or grade["critical_count"] != 0 or grade.get("final_question") != "oui":
                            raise ValueError("Une monographie échoue malgré la moyenne du fichier")
                if key != "A" and checked < started:
                    raise ValueError("Audit antérieur à la production du fichier")
                times.append(checked)
                result["files"][key]["gates"][role] = True
            except (ValueError, KeyError, TypeError, FileNotFoundError) as exc:
                result["files"][key]["gates"][role] = False
                failures.append((role, str(exc)))
        if failures:
            role, reason = next((x for x in failures if x[0] != "visual"), failures[0])
            return blocked("await_authorized_visual_proof" if role == "visual" else "audit_or_correct", role + ": " + reason, key)
        audit_times.extend(times)
        parsers[key] = parser
        if key == "A":
            validated_a_at = max(times)
            try:
                frozen = canonical(reader, head, job, basis, validated_a_at)
                if instant(frozen["frozen_at"]) > now + timedelta(seconds=120):
                    raise ValueError("Gel daté dans le futur")
                found = [(n["attrs"].get("data-dx"), n["attrs"].get("data-name"), text_of(n)) for n in parser.nodes if "data-dx" in n["attrs"]]
                expected = [(x["code"], x["name"], x["code"] + " — " + x["name"]) for x in frozen["diagnoses"]]
                if found != expected:
                    raise ValueError("Liste canonique différente de la liste affichée en Phase A")
            except (ValueError, KeyError, TypeError, FileNotFoundError) as exc:
                return blocked("freeze_or_reaudit_phase_a", exc, "A")
    result["validated"] = True
    last_audit = max(audit_times)
    for key in result["files"]:
        try:
            record = package["files"][key].get("delivery")
            checked = attestation(reader, head, job, record, result["files"][key]["sha256"], "delivery", now)
            if type(record.get("remote_bytes")) is not int or record["remote_bytes"] != result["files"][key]["bytes"]:
                raise ValueError("Taille distante différente des octets figés")
            if checked < last_audit:
                raise ValueError("Livraison antérieure à la validation du lot complet")
            result["files"][key]["gates"]["delivery"] = True
        except (ValueError, KeyError, TypeError, FileNotFoundError) as exc:
            return blocked("verify_final_delivery", exc, key)
    result["delivered"] = True
    return result


def advance(*args, **kwargs):
    raise ValueError("Aucune attribution automatique : nouvelle décision de séance obligatoire")
