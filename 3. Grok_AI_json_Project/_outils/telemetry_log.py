#!/usr/bin/env python3
"""TELEMETRY_LOG.PY — Lock-safe live telemetry CLI for M_LIVE & Extreme Medical Auditors.

Pure Python 3.13 stdlib only. Thread/process-safe on Windows (msvcrt.locking) and POSIX (fcntl.flock)
with atomic temp-file + fsync + os.replace writes for telemetry_live.json and telemetry_live.js.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import errno
import html as html_lib
import json
import os
import random
import re
import sys
import tempfile
import time
import unicodedata
import uuid

if os.name == "nt":
    import msvcrt
else:
    import fcntl

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

DEFAULT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

T0_ISO = "2026-11-20T15:52:08Z"
T0_DT = datetime(2026, 11, 20, 15, 52, 8, tzinfo=timezone.utc)
T0_EPOCH_MS = int(T0_DT.timestamp() * 1000)

SSP_ORDER = ("SSP_248", "SSP_247", "SSP_246", "SSP_245")
MILESTONE_ORDER = ("M_LIVE", "M1", "E2E", "M2", "M3", "M4", "M5", "M6")

CANONICAL_TYPES = (
    "posologie",
    "seuil_clinique",
    "mecanisme_biologique",
    "recommandation_suisse",
    "contre_indication",
    "infobulle_why",
    "source_reference",
    "autre",
)

CANONICAL_SEVERITIES = ("critique", "majeure", "mineure")
CANONICAL_STATUSES = ("started", "in_progress", "done", "error")
CANONICAL_PHASES = (
    "init",
    "survey",
    "impl",
    "condense",
    "canvas",
    "why",
    "audit_med",
    "verify",
    "assemble",
    "e2e",
    "report",
)

TYPE_ALIASES = {
    "posologie": "posologie",
    "dose": "posologie",
    "dosage": "posologie",
    "poso": "posologie",
    "seuil_clinique": "seuil_clinique",
    "seuil": "seuil_clinique",
    "seuils": "seuil_clinique",
    "threshold": "seuil_clinique",
    "mecanisme_biologique": "mecanisme_biologique",
    "mecanisme": "mecanisme_biologique",
    "mechanism": "mecanisme_biologique",
    "physiopathologie": "mecanisme_biologique",
    "pharmacologie": "mecanisme_biologique",
    "recommandation_suisse": "recommandation_suisse",
    "recommandations_suisses": "recommandation_suisse",
    "suisse": "recommandation_suisse",
    "swiss": "recommandation_suisse",
    "guideline": "recommandation_suisse",
    "contre_indication": "contre_indication",
    "contre_indications": "contre_indication",
    "contraindication": "contre_indication",
    "ci": "contre_indication",
    "infobulle_why": "infobulle_why",
    "why": "infobulle_why",
    "infobulle": "infobulle_why",
    "tooltip": "infobulle_why",
    "source_reference": "source_reference",
    "source": "source_reference",
    "reference": "source_reference",
    "ref": "source_reference",
    "biblio": "source_reference",
    "autre": "autre",
    "other": "autre",
}

SEVERITY_ALIASES = {
    "critique": "critique",
    "critical": "critique",
    "crit": "critique",
    "high": "critique",
    "majeure": "majeure",
    "majeur": "majeure",
    "major": "majeure",
    "medium": "majeure",
    "moderate": "majeure",
    "mineure": "mineure",
    "mineur": "mineure",
    "minor": "mineure",
    "low": "mineure",
}

STATUS_ALIASES = {
    "started": "started",
    "start": "started",
    "begin": "started",
    "in_progress": "in_progress",
    "inprogress": "in_progress",
    "running": "in_progress",
    "active": "in_progress",
    "working": "in_progress",
    "wip": "in_progress",
    "done": "done",
    "completed": "done",
    "complete": "done",
    "pass": "done",
    "passed": "done",
    "ok": "done",
    "finished": "done",
    "error": "error",
    "err": "error",
    "fail": "error",
    "failed": "error",
    "blocked": "error",
    "ko": "error",
}

PHASE_ALIASES = {
    "audit": "audit_med",
    "audit_medical": "audit_med",
    "audit_med": "audit_med",
    "test": "e2e",
    "tests": "e2e",
    "e2e": "e2e",
    "condensation": "condense",
    "condense": "condense",
}

SSP_META = {
    "SSP_245": {"lot": 245, "code": "O7.23", "nom": "Suspicion de maladie rare", "circuit": "MONOGRAPHIQUE"},
    "SSP_246": {"lot": 246, "code": "O7.24", "nom": "Patients vulnérables", "circuit": "NON_MONOGRAPHIQUE"},
    "SSP_247": {"lot": 247, "code": "O7.25", "nom": "Demande de conseil génétique", "circuit": "NON_MONOGRAPHIQUE"},
    "SSP_248": {"lot": 248, "code": "O7.26", "nom": "Intoxication, empoisonnement", "circuit": "MONOGRAPHIQUE"},
}

FALLBACK_COURSES: dict[str, list[tuple[str, str]]] = {
    "SSP_245": [
        ("LOT_245_Phase_A_V0.html", "Suspicion de maladie rare — Vue d'ensemble et filière suisse kosek"),
        ("LOT_245_Phase_B_V0_DX.1.html", "Errance diagnostique devant symptômes multisystémiques chroniques inexpliqués"),
        ("LOT_245_Phase_B_V0_DX.2.html", "Suspicion de maladie auto-inflammatoire ou fièvre récurrente (FMF, TRAPS)"),
        ("LOT_245_Phase_B_V0_DX.3.html", "Suspicion de maladie héréditaire du tissu conjonctif (Marfan, Ehlers-Danlos)"),
        ("LOT_245_Phase_B_V0_DX.4.html", "Suspicion de maladie métabolique héréditaire (Fabry, Wilson, Pompe)"),
        ("LOT_245_Phase_B_V0_DX.5.html", "Suspicion de déficit immunitaire primitif chez l'adulte ou l'enfant"),
        ("LOT_245_Phase_B_V0_DX.6.html", "Suspicion de neuropathie ou myopathie héréditaire (Charcot-Marie-Tooth, myotonie)"),
        ("LOT_245_Phase_B_V0_DX.7.html", "Suspicion de vascularite rare ou maladie systémique orpheline (Behçet, Takayasu, IgG4)"),
        ("LOT_245_Phase_B_V0_DX.8.html", "Suspicion de sclérose latérale amyotrophique (SLA) ou maladie neurodégénérative rare"),
        ("LOT_245_Phase_B_V0_DX.9.html", "Suspicion de mastocytose systémique ou angio-œdème héréditaire"),
        ("LOT_245_Phase_B_V0_DX.10.html", "Suspicion de porphyrie aiguë intermittente"),
        ("LOT_245_Phase_B_V0_DX.11.html", "Crise d'angio-œdème héréditaire laryngé résistant aux corticoïdes"),
        ("LOT_245_Phase_B_V0_DX.12.html", "Crise neuroviscérale aiguë de porphyrie aiguë intermittente"),
        ("LOT_245_Phase_B_V0_DX.13.html", "Décompensation métabolique aiguë (hyperammoniémie) sur maladie métabolique rare"),
        ("LOT_245_Phase_B_V0_DX.14.html", "Dissection aortique aiguë sur syndrome de Marfan ou Loeys-Dietz"),
        ("LOT_245_Phase_B_V0_DX.15.html", "Insuffisance hépatique aiguë ou crise hémolytique de maladie de Wilson"),
        ("LOT_245_Phase_B_V0_DX.16.html", "Crise myasthénique ou défaillance respiratoire inaugurale d'une maladie neuromusculaire"),
    ],
    "SSP_246": [
        ("LOT_246_Phase_A_V0.html", "Patients vulnérables — Vue d'ensemble et principes suisses"),
        ("LOT_246_Phase_B_V0_DX.1.html", "Sujet âgé polymorbide, fragile et isolé"),
        ("LOT_246_Phase_B_V0_DX.2.html", "Patient en situation de précarité socio-économique ou sans-abri"),
        ("LOT_246_Phase_B_V0_DX.3.html", "Patient avec trouble psychique sévère ou addiction (accès limité aux soins)"),
        ("LOT_246_Phase_B_V0_DX.4.html", "Patient présentant une déficience intellectuelle ou trouble du spectre de l'autisme"),
        ("LOT_246_Phase_B_V0_DX.5.html", "Patient victime de violence domestique ou maltraitance"),
        ("LOT_246_Phase_B_V0_DX.6.html", "Patient en situation de migration précaire ou sans-papiers (accès LAMal)"),
        ("LOT_246_Phase_B_V0_DX.7.html", "Enfant ou adolescent exposé à une négligence ou conflit familial grave"),
        ("LOT_246_Phase_B_V0_DX.8.html", "Patient en soins palliatifs à domicile avec épuisement des proches aidants"),
        ("LOT_246_Phase_B_V0_DX.9.html", "Patient atteint de handicap sensoriel (surdité, cécité) nécessitant adaptation"),
        ("LOT_246_Phase_B_V0_DX.10.html", "Personne détenue ou sous mesure privative de liberté"),
        ("LOT_246_Phase_B_V0_DX.11.html", "Violence domestique aiguë avec danger vital immédiat ou traumatisme"),
        ("LOT_246_Phase_B_V0_DX.12.html", "Maltraitance infantile aiguë ou syndrome du bébé secoué"),
        ("LOT_246_Phase_B_V0_DX.13.html", "Hypothermie, déshydratation sévère ou gelures chez personne sans-abri"),
        ("LOT_246_Phase_B_V0_DX.14.html", "Crise suicidaire aiguë chez patient isolé ou vulnérable"),
        ("LOT_246_Phase_B_V0_DX.15.html", "Abus financier ou négligence grave nécessitant signalement à l'APEA"),
        ("LOT_246_Phase_B_V0_DX.16.html", "Overdose aux opioïdes ou sevrage sévère (delirium tremens) chez patient marginalisé"),
    ],
    "SSP_247": [
        ("LOT_247_Phase_A_V0.html", "Demande de conseil génétique — Orientation générale & LAGH"),
        ("LOT_247_Phase_B_V0_DX.1.html", "Conseil génétique en oncogénétique (BRCA1/2, syndrome de Lynch)"),
        ("LOT_247_Phase_B_V0_DX.2.html", "Conseil génétique prénatal (âge maternel, DPNI, antécédents familiaux)"),
        ("LOT_247_Phase_B_V0_DX.3.html", "Conseil génétique préconceptionnel (consanguinité, porteur sain)"),
        ("LOT_247_Phase_B_V0_DX.4.html", "Conseil génétique pour cardiopathie héréditaire (CMH, QT long, Brugada)"),
        ("LOT_247_Phase_B_V0_DX.5.html", "Conseil génétique pour hypercholestérolémie familiale ou hémochromatose"),
        ("LOT_247_Phase_B_V0_DX.6.html", "Conseil génétique pour maladie neurologique héréditaire (Huntington, SLA familiale)"),
        ("LOT_247_Phase_B_V0_DX.7.html", "Conseil génétique pédiatrique devant retard de développement ou malformation"),
        ("LOT_247_Phase_B_V0_DX.8.html", "Interprétation d'une variante de signification incertaine (VUS) ou découverte fortuite"),
        ("LOT_247_Phase_B_V0_DX.9.html", "Cadre légal suisse du conseil génétique (LAGH : consentement, droit de ne pas savoir)"),
        ("LOT_247_Phase_B_V0_DX.10.html", "Diagnostic préimplantatoire (DPI) selon la LPMA en Suisse"),
        ("LOT_247_Phase_B_V0_DX.11.html", "Diagnostic prénatal urgent d'anomalie fœtale sévère"),
        ("LOT_247_Phase_B_V0_DX.12.html", "Syncope ou mort subite familiale suspecte de canalopathie héréditaire"),
        ("LOT_247_Phase_B_V0_DX.13.html", "Résultat oncogénétique urgent modifiant une décision chirurgicale immédiate"),
        ("LOT_247_Phase_B_V0_DX.14.html", "Dépistage néonatal positif urgent (mucoviscidose, PCU, SMA)"),
        ("LOT_247_Phase_B_V0_DX.15.html", "Détresse psychologique majeure ou culpabilité parentale après annonce génétique"),
    ],
    "SSP_248": [
        ("LOT_248_Phase_A_V0.html", "Intoxication, empoisonnement : vue d’ensemble"),
        ("LOT_248_Phase_B_V0_DX.1.html", "Intoxication éthylique aiguë"),
        ("LOT_248_Phase_B_V0_DX.2.html", "Intoxication médicamenteuse volontaire aux benzodiazépines ou Z-drugs"),
        ("LOT_248_Phase_B_V0_DX.3.html", "Intoxication au paracétamol (volontaire ou surdosage thérapeutique)"),
        ("LOT_248_Phase_B_V0_DX.4.html", "Intoxication aux opioïdes (morphine, héroïne, méthadone, fentanyl)"),
        ("LOT_248_Phase_B_V0_DX.5.html", "Intoxication au monoxyde de carbone (CO)"),
        ("LOT_248_Phase_B_V0_DX.6.html", "Intoxication aux antidépresseurs (tricycliques, ISRS) ou lithium"),
        ("LOT_248_Phase_B_V0_DX.7.html", "Intoxication domestique accidentelle de l'enfant (produits ménagers, piles boutons)"),
        ("LOT_248_Phase_B_V0_DX.8.html", "Intoxication aux drogues stimulantes (cocaïne, amphétamines, MDMA, GHB)"),
        ("LOT_248_Phase_B_V0_DX.9.html", "Intoxication alimentaire bactérienne ou par toxines (S. aureus, B. cereus)"),
        ("LOT_248_Phase_B_V0_DX.10.html", "Intoxication aux champignons vénéneux (Amanite phalloïde) ou plantes toxiques"),
        ("LOT_248_Phase_B_V0_DX.11.html", "Intoxication aux pesticides organophosphorés ou méthanol/éthylène glycol"),
        ("LOT_248_Phase_B_V0_DX.12.html", "Arrêt respiratoire ou coma profond sur surdosage d'opioïdes"),
        ("LOT_248_Phase_B_V0_DX.13.html", "Hépatite fulminante au paracétamol"),
        ("LOT_248_Phase_B_V0_DX.14.html", "État de mal convulsif ou arythmie ventriculaire sur antidépresseurs tricycliques"),
        ("LOT_248_Phase_B_V0_DX.15.html", "Acidose métabolique sévère à trou anionique élevé sur méthanol ou éthylène glycol"),
        ("LOT_248_Phase_B_V0_DX.16.html", "Brûlure caustique œsophagogastrique aiguë par ingestion d'acide ou de base"),
        ("LOT_248_Phase_B_V0_DX.17.html", "Syndrome cholinergique aigu avec détresse respiratoire (organophosphorés)"),
        ("LOT_248_Phase_B_V0_DX.18.html", "Encéphalopathie aiguë ou coma oxycarboné nécessitant oxygénothérapie hyperbare"),
    ],
}


def strip_accents_token(text: str) -> str:
    norm = unicodedata.normalize("NFKD", text.strip())
    ascii_only = "".join(ch for ch in norm if not unicodedata.combining(ch))
    return re.sub(r"[\s\-]+", "_", ascii_only.lower()).strip("_")


def parse_iso_utc(ts_str: str | None) -> datetime:
    if not ts_str:
        return datetime.now(timezone.utc)
    raw = ts_str.strip()
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(raw)
    except ValueError as exc:
        raise ValueError(f"Horodatage ISO invalide: {ts_str!r}") from exc
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def format_iso_ms(dt: datetime) -> str:
    utc = dt.astimezone(timezone.utc)
    ms = utc.microsecond // 1000
    return utc.strftime("%Y-%m-%dT%H:%M:%S.") + f"{ms:03d}Z"


def compute_t_sec(dt: datetime) -> float:
    return round(max(0.0, (dt.astimezone(timezone.utc) - T0_DT).total_seconds()), 3)


def normalize_ssp(raw: str) -> str:
    val = (raw or "").strip()
    if not val:
        raise ValueError("--ssp ne peut pas être vide")
    up = val.upper().replace("-", "_")
    if up in ("245", "SSP245", "SSP_245"):
        return "SSP_245"
    if up in ("246", "SSP246", "SSP_246"):
        return "SSP_246"
    if up in ("247", "SSP247", "SSP_247"):
        return "SSP_247"
    if up in ("248", "SSP248", "SSP_248"):
        return "SSP_248"
    if up in ("SHARED", "E2E", "ALL", "M_LIVE", "M1", "M2", "M3", "M4", "M5", "M6"):
        return up
    if re.match(r"^SSP_\d{3}(?:\.\.\d{3})?$", up):
        return up
    return up


def normalize_course(raw: str) -> str:
    val = (raw or "").strip()
    if not val or val.lower() == "all":
        return "all"
    return os.path.basename(val.replace("\\", "/"))


def normalize_phase(raw: str) -> str:
    tok = strip_accents_token(raw or "")
    if not tok:
        raise ValueError("--phase ne peut pas être vide")
    return PHASE_ALIASES.get(tok, tok)


def normalize_status(raw: str) -> str:
    tok = strip_accents_token(raw or "")
    mapped = STATUS_ALIASES.get(tok, tok)
    if mapped not in CANONICAL_STATUSES:
        raise ValueError(
            f"--status invalide: {raw!r}. Valeurs acceptées: {', '.join(CANONICAL_STATUSES)}"
        )
    return mapped


def normalize_type(raw: str) -> str:
    tok = strip_accents_token(raw or "")
    mapped = TYPE_ALIASES.get(tok, tok)
    if mapped not in CANONICAL_TYPES:
        raise ValueError(
            f"--type invalide: {raw!r}. Valeurs acceptées: {', '.join(CANONICAL_TYPES)}"
        )
    return mapped


def normalize_severity(raw: str) -> str:
    tok = strip_accents_token(raw or "")
    mapped = SEVERITY_ALIASES.get(tok, tok)
    if mapped not in CANONICAL_SEVERITIES:
        raise ValueError(
            f"--severity invalide: {raw!r}. Valeurs acceptées: {', '.join(CANONICAL_SEVERITIES)}"
        )
    return mapped


def normalize_section(raw: str) -> str:
    val = (raw or "").strip()
    if not val:
        raise ValueError("--section ne peut pas être vide")
    tok = strip_accents_token(val)
    m = re.match(r"^(?:p|partie_?)(\d{1,2})$", tok)
    if m:
        num = int(m.group(1))
        if 1 <= num <= 14:
            return f"p{num}"
    if tok in ("fm_canvas", "canvas", "algo", "algorithme"):
        return "canvas"
    if tok in ("fenetre", "fen", "modale", "modal"):
        return "modal"
    if "source" in tok or tok == "refs":
        return "sources"
    return tok


def infer_milestone(explicit: str | None, ssp: str, phase: str, agent: str) -> str:
    if explicit and explicit.strip():
        return explicit.strip().upper()
    if ssp == "E2E" or phase == "e2e":
        return "E2E"
    if ssp == "SSP_248":
        return "M2"
    if ssp == "SSP_247":
        return "M3"
    if ssp == "SSP_246":
        return "M4"
    if ssp == "SSP_245":
        return "M5"
    if phase == "report":
        return "M6"
    if ssp == "SHARED":
        if "live" in agent.lower() or "m_live" in agent.lower():
            return "M_LIVE"
        return "M1"
    if ssp == "ALL":
        return "M6" if phase == "report" else "M_LIVE"
    return ""


class TelemetryLock:
    """Persistent byte-range lock on _outils/telemetry.lock (never unlinked)."""

    def __init__(self, lock_path: str, timeout: float = 30.0):
        self.lock_path = lock_path
        self.timeout = max(1.0, float(timeout))
        self.fd: int | None = None

    def __enter__(self) -> TelemetryLock:
        os.makedirs(os.path.dirname(os.path.abspath(self.lock_path)), exist_ok=True)
        deadline = time.monotonic() + self.timeout
        attempt = 0

        while True:
            try:
                self.fd = os.open(self.lock_path, os.O_CREAT | os.O_RDWR)
                break
            except OSError as exc:
                if time.monotonic() >= deadline:
                    raise TimeoutError(f"Impossible d'ouvrir le verrou {self.lock_path}: {exc}") from exc
                time.sleep(0.015 + random.uniform(0.0, 0.02))

        try:
            if os.fstat(self.fd).st_size == 0:
                os.write(self.fd, b"0")
        except OSError:
            pass

        while True:
            try:
                if os.name == "nt":
                    os.lseek(self.fd, 0, os.SEEK_SET)
                    msvcrt.locking(self.fd, msvcrt.LK_NBLCK, 1)
                else:
                    fcntl.flock(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return self
            except OSError as exc:
                if time.monotonic() >= deadline:
                    try:
                        os.close(self.fd)
                    finally:
                        self.fd = None
                    raise TimeoutError(
                        f"Timeout verrou ({self.timeout}s) sur {self.lock_path}: {exc}"
                    ) from exc
                delay = min(0.15, 0.01 * (1.25 ** min(attempt, 15))) + random.uniform(0.0, 0.02)
                attempt += 1
                time.sleep(delay)

    def __exit__(self, exc_type, exc, tb) -> None:
        if self.fd is not None:
            try:
                if os.name == "nt":
                    os.lseek(self.fd, 0, os.SEEK_SET)
                    msvcrt.locking(self.fd, msvcrt.LK_UNLCK, 1)
                else:
                    fcntl.flock(self.fd, fcntl.LOCK_UN)
            finally:
                os.close(self.fd)
                self.fd = None


def atomic_write_text(path: str, content: str, retries: int = 25) -> None:
    parent = os.path.dirname(os.path.abspath(path))
    os.makedirs(parent, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(prefix=f".{os.path.basename(path)}.", suffix=".tmp", dir=parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())
        for attempt in range(retries):
            try:
                os.replace(tmp_path, path)
                return
            except (PermissionError, OSError) as exc:
                winerr = getattr(exc, "winerror", None)
                transient = (
                    isinstance(exc, PermissionError)
                    or winerr in (5, 32)
                    or exc.errno in (errno.EACCES, errno.EPERM, errno.EBUSY)
                )
                if not transient or attempt == retries - 1:
                    raise
                delay = min(0.25, 0.012 * (1.25 ** attempt)) + random.uniform(0.002, 0.015)
                time.sleep(delay)
    finally:
        if os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except OSError:
                pass


def clean_course_title(raw_html: str, code: str, order: int) -> str:
    m = re.search(r"<title>(.*?)</title>", raw_html, re.S | re.I) or re.search(
        r"<h2[^>]*>(.*?)</h2>", raw_html, re.S | re.I
    )
    txt = html_lib.unescape(re.sub(r"<[^>]+>", "", m.group(1))) if m else ""
    txt = re.sub(
        r"LOT[ _]?\d{3}|Phase[ _]?[AB]|\bV0\b|DX\.?\s?\d+|Le[çc]on\s?\d+|"
        + re.escape(code)
        + r"|\(\s*\)",
        "",
        txt,
    )
    txt = re.sub(r"^[\s—–·:,|-]+|[\s—–·:,|-]+$", "", txt).strip()
    return txt or f"Partie {order}"


def course_sort_key(filename: str) -> tuple[int, int, str]:
    if "_Phase_A_" in filename:
        return (0, 0, filename)
    m = re.search(r"_DX\.(\d+)\.html$", filename)
    if m:
        return (1, int(m.group(1)), filename)
    return (2, 999, filename)


def discover_courses(base_dir: str) -> list[dict]:
    cat_path = os.path.join(base_dir, "_outils", "catalogue_248.json")
    cat_data = None
    if os.path.isfile(cat_path):
        try:
            with open(cat_path, encoding="utf-8") as f:
                cat_data = json.load(f)
        except Exception:
            cat_data = None

    catalog: list[dict] = []
    for ssp in SSP_ORDER:
        meta = dict(SSP_META[ssp])
        lot = meta["lot"]
        if isinstance(cat_data, list) and len(cat_data) >= lot:
            entry = cat_data[lot - 1]
            meta["code"] = entry.get("code", meta["code"])
            meta["nom"] = entry.get("nom", meta["nom"])
            meta["circuit"] = entry.get("circuit", meta["circuit"])

        src_dir = os.path.join(base_dir, ssp, "_sources")
        if not os.path.isdir(src_dir):
            src_dir = os.path.join(base_dir, ssp)

        html_files: list[str] = []
        if os.path.isdir(src_dir):
            html_files = sorted(
                (
                    fn
                    for fn in os.listdir(src_dir)
                    if fn.startswith(f"LOT_{lot:03d}_") and fn.endswith(".html")
                ),
                key=course_sort_key,
            )

        if html_files:
            for fn in html_files:
                _, order, _ = course_sort_key(fn)
                label = "Ch.0" if order == 0 else f"DX.{order}"
                fp = os.path.join(src_dir, fn)
                try:
                    with open(fp, encoding="utf-8", errors="replace") as f:
                        raw_html = f.read(8192)
                    title = clean_course_title(raw_html, meta["code"], order)
                except OSError:
                    title = f"{meta['nom']} ({label})"
                catalog.append(
                    {
                        "key": f"{ssp}/{fn}",
                        "ssp": ssp,
                        "code": meta["code"],
                        "course": fn,
                        "order": order,
                        "label": label,
                        "title": title,
                    }
                )
        else:
            for fn, title in FALLBACK_COURSES[ssp]:
                _, order, _ = course_sort_key(fn)
                label = "Ch.0" if order == 0 else f"DX.{order}"
                catalog.append(
                    {
                        "key": f"{ssp}/{fn}",
                        "ssp": ssp,
                        "code": meta["code"],
                        "course": fn,
                        "order": order,
                        "label": label,
                        "title": title,
                    }
                )
    return catalog


def append_jsonl(events_path: str, record: dict) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(events_path)), exist_ok=True)
    line = json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
    with open(events_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(line)
        f.flush()
        os.fsync(f.fileno())


def read_events_jsonl(events_path: str) -> tuple[list[dict], int]:
    records: list[dict] = []
    corrupt_count = 0
    if not os.path.isfile(events_path):
        return records, corrupt_count
    with open(events_path, encoding="utf-8", errors="replace") as f:
        for lineno, raw_line in enumerate(f, start=1):
            stripped = raw_line.strip()
            if not stripped:
                continue
            try:
                obj = json.loads(stripped)
                if not isinstance(obj, dict):
                    raise ValueError("Ligne JSONL non-objet")
                records.append(obj)
            except Exception as exc:
                corrupt_count += 1
                sys.stderr.write(
                    f"[telemetry_log] ATTENTION ligne corrompue ignorée ({events_path}:{lineno}): {exc}\n"
                )
    return records, corrupt_count


def build_state(base_dir: str, records: list[dict], corrupt_count: int) -> dict:
    catalog = discover_courses(base_dir)
    courses: dict[str, dict] = {}
    course_lookup_by_name: dict[str, str] = {}

    for item in catalog:
        key = item["key"]
        courses[key] = {
            "key": key,
            "ssp": item["ssp"],
            "code": item["code"],
            "course": item["course"],
            "order": item["order"],
            "label": item["label"],
            "title": item["title"],
            "status": "pending",
            "phase": "pending",
            "audit_status": "pending",
            "last_agent": "",
            "last_ts": "",
            "last_t_sec": None,
            "last_detail": "",
            "fix_count": 0,
            "fixes_by_type": {t: 0 for t in CANONICAL_TYPES},
            "fixes_by_severity": {s: 0 for s in CANONICAL_SEVERITIES},
        }
        course_lookup_by_name[item["course"]] = key

    def sort_key(idx_rec: tuple[int, dict]) -> tuple[float, int, int]:
        idx, rec = idx_rec
        t_val = rec.get("t_sec")
        if not isinstance(t_val, (int, float)):
            try:
                t_val = compute_t_sec(parse_iso_utc(rec.get("ts")))
            except Exception:
                t_val = 0.0
        seq_val = rec.get("seq")
        seq_int = int(seq_val) if isinstance(seq_val, int) else idx
        return (float(t_val), seq_int, idx)

    ordered_records = [rec for _, rec in sorted(enumerate(records), key=sort_key)]

    milestones: dict[str, dict] = {
        m: {"status": "pending", "last_t_sec": None, "last_detail": "", "events_count": 0}
        for m in MILESTONE_ORDER
    }
    agents: dict[str, dict] = {}
    by_type: dict[str, int] = {t: 0 for t in CANONICAL_TYPES}
    by_severity: dict[str, int] = {s: 0 for s in CANONICAL_SEVERITIES}
    by_section: Counter[str] = Counter()
    ssp_fixes: dict[str, dict] = {
        ssp: {
            "ssp": ssp,
            "code": SSP_META[ssp]["code"],
            "nom": SSP_META[ssp]["nom"],
            "courses_total": sum(1 for c in courses.values() if c["ssp"] == ssp),
            "courses_done": 0,
            "courses_in_progress": 0,
            "courses_error": 0,
            "courses_pending": 0,
            "courses_audited": 0,
            "courses_with_fixes": 0,
            "fixes": 0,
            "by_type": {t: 0 for t in CANONICAL_TYPES},
            "by_severity": {s: 0 for s in CANONICAL_SEVERITIES},
            "last_phase": "pending",
            "last_status": "pending",
            "last_t_sec": None,
        }
        for ssp in SSP_ORDER
    }

    curve: list[dict] = []
    fixes: list[dict] = []
    timeline: list[dict] = []
    lifecycle_events = 0
    fix_events = 0
    last_event_ts = T0_ISO
    last_t_sec = 0.0

    for seq_idx, rec in enumerate(ordered_records, start=1):
        kind = str(rec.get("kind") or "event").lower()
        ts = str(rec.get("ts") or T0_ISO)
        t_sec = rec.get("t_sec")
        if not isinstance(t_sec, (int, float)):
            try:
                t_sec = compute_t_sec(parse_iso_utc(ts))
            except Exception:
                t_sec = 0.0
        t_sec = round(max(0.0, float(t_sec)), 3)

        agent = str(rec.get("agent") or "unknown")
        ssp = str(rec.get("ssp") or "SHARED")
        course = normalize_course(str(rec.get("course") or "all"))
        phase = str(rec.get("phase") or ("audit_med" if kind == "fix" else "impl"))
        status = str(rec.get("status") or ("done" if kind == "fix" else "in_progress"))
        milestone = str(rec.get("milestone") or infer_milestone(None, ssp, phase, agent))
        detail = str(rec.get("detail") or "")

        if t_sec >= last_t_sec:
            last_t_sec = t_sec
            last_event_ts = ts

        if milestone in milestones:
            milestones[milestone]["status"] = status
            milestones[milestone]["last_t_sec"] = t_sec
            milestones[milestone]["last_detail"] = detail
            milestones[milestone]["events_count"] += 1

        ag = agents.setdefault(
            agent,
            {
                "agent": agent,
                "last_ts": ts,
                "last_t_sec": t_sec,
                "milestone": milestone,
                "ssp": ssp,
                "course": course,
                "phase": phase,
                "status": status,
                "detail": detail,
                "events_count": 0,
                "fixes_count": 0,
            },
        )
        ag["last_ts"] = ts
        ag["last_t_sec"] = t_sec
        if milestone:
            ag["milestone"] = milestone
        ag["ssp"] = ssp
        ag["course"] = course
        ag["phase"] = phase
        ag["status"] = status
        ag["detail"] = detail
        ag["events_count"] += 1

        course_key = None
        if course != "all":
            candidate = f"{ssp}/{course}"
            if candidate in courses:
                course_key = candidate
            elif course in course_lookup_by_name:
                course_key = course_lookup_by_name[course]

        if kind == "fix":
            fix_events += 1
            ag["fixes_count"] += 1
            n_val = fix_events
            section = str(rec.get("section") or "p1")
            ftype = str(rec.get("type") or "autre")
            if ftype not in by_type:
                ftype = "autre"
            sev = str(rec.get("severity") or "mineure")
            if sev not in by_severity:
                sev = "mineure"
            source = str(rec.get("source") or "")
            before = str(rec.get("before") or "")
            after = str(rec.get("after") or "")

            by_type[ftype] += 1
            by_severity[sev] += 1
            by_section[section] += 1

            if ssp in ssp_fixes:
                ssp_fixes[ssp]["fixes"] += 1
                ssp_fixes[ssp]["by_type"][ftype] += 1
                ssp_fixes[ssp]["by_severity"][sev] += 1

            if course_key and course_key in courses:
                c_obj = courses[course_key]
                c_obj["fix_count"] += 1
                c_obj["fixes_by_type"][ftype] += 1
                c_obj["fixes_by_severity"][sev] += 1
                c_obj["last_agent"] = agent
                c_obj["last_ts"] = ts
                c_obj["last_t_sec"] = t_sec
                c_obj["last_detail"] = detail
                if c_obj["audit_status"] == "pending":
                    c_obj["audit_status"] = "in_progress"
                if c_obj["status"] == "pending":
                    c_obj["status"] = "in_progress"
                    c_obj["phase"] = "audit_med"

            curve_pt = {
                "n": n_val,
                "t_sec": t_sec,
                "ts": ts,
                "ssp": ssp,
                "course": course,
                "section": section,
                "type": ftype,
                "severity": sev,
                "agent": agent,
                "source": source,
                "detail": detail,
            }
            curve.append(curve_pt)

            fix_rec = {
                "id": str(rec.get("id") or f"fix-{n_val}"),
                "seq": int(rec.get("seq") or seq_idx),
                **curve_pt,
                "milestone": milestone,
                "before": before,
                "after": after,
            }
            fixes.append(fix_rec)
            timeline.append(
                {
                    "kind": "fix",
                    "seq": fix_rec["seq"],
                    "n": n_val,
                    "t_sec": t_sec,
                    "ts": ts,
                    "agent": agent,
                    "milestone": milestone,
                    "ssp": ssp,
                    "course": course,
                    "section": section,
                    "type": ftype,
                    "severity": sev,
                    "source": source,
                    "before": before,
                    "after": after,
                    "detail": detail,
                }
            )
        else:
            lifecycle_events += 1
            if ssp in ssp_fixes:
                ssp_fixes[ssp]["last_phase"] = phase
                ssp_fixes[ssp]["last_status"] = status
                ssp_fixes[ssp]["last_t_sec"] = t_sec
            if course_key and course_key in courses:
                c_obj = courses[course_key]
                c_obj["status"] = status
                c_obj["phase"] = phase
                c_obj["last_agent"] = agent
                c_obj["last_ts"] = ts
                c_obj["last_t_sec"] = t_sec
                c_obj["last_detail"] = detail
                if phase == "audit_med":
                    c_obj["audit_status"] = status
            timeline.append(
                {
                    "kind": "event",
                    "seq": int(rec.get("seq") or seq_idx),
                    "t_sec": t_sec,
                    "ts": ts,
                    "agent": agent,
                    "milestone": milestone,
                    "ssp": ssp,
                    "course": course,
                    "phase": phase,
                    "status": status,
                    "detail": detail,
                }
            )

    courses_done = sum(1 for c in courses.values() if c["status"] == "done")
    courses_in_progress = sum(1 for c in courses.values() if c["status"] in ("started", "in_progress"))
    courses_error = sum(1 for c in courses.values() if c["status"] == "error")
    courses_pending = sum(1 for c in courses.values() if c["status"] == "pending")
    courses_audited = sum(1 for c in courses.values() if c["audit_status"] == "done")
    courses_with_fixes = sum(1 for c in courses.values() if c["fix_count"] > 0)
    total_courses = len(courses)
    total_fixes = len(fixes)

    for ssp in SSP_ORDER:
        sc = [c for c in courses.values() if c["ssp"] == ssp]
        s_info = ssp_fixes[ssp]
        s_info["courses_done"] = sum(1 for c in sc if c["status"] == "done")
        s_info["courses_in_progress"] = sum(1 for c in sc if c["status"] in ("started", "in_progress"))
        s_info["courses_error"] = sum(1 for c in sc if c["status"] == "error")
        s_info["courses_pending"] = sum(1 for c in sc if c["status"] == "pending")
        s_info["courses_audited"] = sum(1 for c in sc if c["audit_status"] == "done")
        s_info["courses_with_fixes"] = sum(1 for c in sc if c["fix_count"] > 0)

    recent_events = list(reversed(timeline[-200:]))

    return {
        "schema_version": "1.0",
        "generated_at": format_iso_ms(datetime.now(timezone.utc)),
        "t0": T0_ISO,
        "t0_epoch_ms": T0_EPOCH_MS,
        "last_event_ts": last_event_ts,
        "last_t_sec": round(last_t_sec, 3),
        "integrity": {
            "total_events": len(ordered_records),
            "lifecycle_events": lifecycle_events,
            "fix_events": fix_events,
            "corrupt_lines_skipped": corrupt_count,
        },
        "summary": {
            "total_ssps": len(SSP_ORDER),
            "total_courses": total_courses,
            "courses_done": courses_done,
            "courses_in_progress": courses_in_progress,
            "courses_error": courses_error,
            "courses_pending": courses_pending,
            "courses_audited": courses_audited,
            "courses_with_fixes": courses_with_fixes,
            "pct_courses_affected": round((courses_with_fixes / total_courses) * 100.0, 2) if total_courses else 0.0,
            "total_fixes": total_fixes,
            "penetration_rate_per_course": round(total_fixes / total_courses, 3) if total_courses else 0.0,
            "penetration_rate_audited_courses": round(total_fixes / courses_audited, 3) if courses_audited else 0.0,
            "by_type": by_type,
            "by_severity": by_severity,
            "by_section": dict(sorted(by_section.items())),
            "by_ssp": ssp_fixes,
        },
        "milestones": milestones,
        "agents": agents,
        "courses": courses,
        "curve": curve,
        "fixes": fixes,
        "recent_events": recent_events,
    }


def write_live_outputs(outils_dir: str, state: dict) -> None:
    live_json_path = os.path.join(outils_dir, "telemetry_live.json")
    live_js_path = os.path.join(outils_dir, "telemetry_live.js")

    json_text = json.dumps(state, ensure_ascii=False, indent=2) + "\n"
    atomic_write_text(live_json_path, json_text)

    compact_json = json.dumps(state, ensure_ascii=False, separators=(",", ":"))
    safe_js = (
        compact_json.replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
        .replace("</", "<\\/")
    )
    js_text = f"window.__TELEMETRY_LIVE__ = {safe_js};\n"
    atomic_write_text(live_js_path, js_text)


def rebuild_under_lock(base_dir: str) -> dict:
    outils_dir = os.path.join(base_dir, "_outils")
    events_path = os.path.join(outils_dir, "telemetry_events.jsonl")
    records, corrupt_count = read_events_jsonl(events_path)
    state = build_state(base_dir, records, corrupt_count)
    write_live_outputs(outils_dir, state)
    return state


def make_baseline_events(init_dt: datetime) -> list[dict]:
    init_iso = format_iso_ms(init_dt)
    init_t = compute_t_sec(init_dt)
    seeds = [
        {
            "id": "seed-001",
            "seq": 1,
            "kind": "event",
            "ts": "2026-11-20T15:52:08.000Z",
            "t_sec": 0.0,
            "agent": "orchestrator",
            "milestone": "INIT",
            "ssp": "ALL",
            "course": "all",
            "phase": "init",
            "status": "started",
            "detail": "Lancement initial de la mission SSP_245–248 (69 cours).",
        },
        {
            "id": "seed-002",
            "seq": 2,
            "kind": "event",
            "ts": "2026-11-20T15:57:57.000Z",
            "t_sec": 349.0,
            "agent": "teamwork_explorer_survey_1",
            "milestone": "M1",
            "ssp": "SHARED",
            "course": "all",
            "phase": "survey",
            "status": "done",
            "detail": "Survey 1 terminé : moteur UI/infobulles Why & baseline E2E.",
        },
        {
            "id": "seed-003",
            "seq": 3,
            "kind": "event",
            "ts": "2026-11-20T15:59:25.000Z",
            "t_sec": 437.0,
            "agent": "teamwork_explorer_survey_2",
            "milestone": "M2",
            "ssp": "SSP_248",
            "course": "all",
            "phase": "survey",
            "status": "done",
            "detail": "Survey 2 terminé : plan de condensation SSP_248 & notions < 60%.",
        },
        {
            "id": "seed-004",
            "seq": 4,
            "kind": "event",
            "ts": "2026-11-20T15:59:34.000Z",
            "t_sec": 446.0,
            "agent": "teamwork_explorer_survey_3",
            "milestone": "M3",
            "ssp": "SSP_245..247",
            "course": "all",
            "phase": "survey",
            "status": "done",
            "detail": "Survey 3 terminé : couverture SSP_245–247 & plans Canvas Obsidian.",
        },
        {
            "id": "seed-005",
            "seq": 5,
            "kind": "event",
            "ts": "2026-11-20T16:00:00.000Z",
            "t_sec": 472.0,
            "agent": "sub_orch_m1",
            "milestone": "M1",
            "ssp": "SHARED",
            "course": "all",
            "phase": "impl",
            "status": "in_progress",
            "detail": "Implémentation du moteur frontend partagé (forme.css, forme.js, gabarit) démarrée.",
        },
        {
            "id": "seed-006",
            "seq": 6,
            "kind": "event",
            "ts": "2026-11-20T16:00:00.000Z",
            "t_sec": 472.0,
            "agent": "e2e_track",
            "milestone": "E2E",
            "ssp": "E2E",
            "course": "all",
            "phase": "verify",
            "status": "in_progress",
            "detail": "Construction de la suite de tests E2E démarrée.",
        },
        {
            "id": "seed-007",
            "seq": 7,
            "kind": "event",
            "ts": "2026-11-20T16:08:16.000Z",
            "t_sec": 968.0,
            "agent": "orchestrator",
            "milestone": "INIT",
            "ssp": "ALL",
            "course": "all",
            "phase": "init",
            "status": "in_progress",
            "detail": "Directive prioritaire : Auditeurs Médicaux Extrêmes & Télémétrie Live Orthonormée activés.",
        },
        {
            "id": "seed-008",
            "seq": 8,
            "kind": "event",
            "ts": init_iso,
            "t_sec": init_t,
            "agent": "m_live",
            "milestone": "M_LIVE",
            "ssp": "SHARED",
            "course": "all",
            "phase": "impl",
            "status": "in_progress",
            "detail": "Télémétrie live initialisée avec catalogue des 69 cours (SSP_245–248).",
        },
    ]
    return seeds


def md_escape(text: str) -> str:
    return (text or "").replace("\r", " ").replace("\n", " ").replace("|", "\\|").strip()


def generate_markdown_report(state: dict) -> str:
    summary = state["summary"]
    total_courses = summary["total_courses"]
    total_fixes = summary["total_fixes"]
    by_sev = summary["by_severity"]
    by_type = summary["by_type"]
    by_section = summary["by_section"]
    by_ssp = summary["by_ssp"]
    fixes = state["fixes"]
    courses = list(state["courses"].values())

    lines: list[str] = []
    lines.append("# Rapport Statistique sur la Pénétration Erratique — SSP_245–248")
    lines.append("")
    lines.append(f"- **Généré le (UTC)** : `{state['generated_at']}`")
    lines.append(f"- **Origine temporelle (`t₀`)** : `{state['t0']}`")
    lines.append(f"- **Dernier événement (`t_sec`)** : `+{state['last_t_sec']} s` (`{state['last_event_ts']}`)")
    lines.append(f"- **Intégrité du journal** : `{state['integrity']['total_events']}` entrées (`{state['integrity']['corrupt_lines_skipped']}` ligne(s) corrompue(s) ignorée(s))")
    lines.append("")

    lines.append("## 1. Synthèse exécutive & KPIs")
    lines.append("")
    lines.append("| Indicateur | Valeur |")
    lines.append("|---|---|")
    lines.append(f"| Nombre total de cours | **{total_courses}** (SSP_245: 17, SSP_246: 17, SSP_247: 16, SSP_248: 19) |")
    lines.append(f"| Cours audités (`audit_med = done`) | **{summary['courses_audited']} / {total_courses}** |")
    lines.append(f"| Cours touchés (≥ 1 correction) | **{summary['courses_with_fixes']} / {total_courses}** ({summary['pct_courses_affected']:.2f} %) |")
    lines.append(f"| Total des erreurs corrigées (`N_erreurs_corrigées`) | **{total_fixes}** |")
    lines.append(f"| Taux de pénétration global (fixes / 69 cours) | **{summary['penetration_rate_per_course']:.3f}** |")
    lines.append(f"| Taux sur cours audités (fixes / cours audités) | **{summary['penetration_rate_audited_courses']:.3f}** |")
    lines.append(
        f"| Répartition par sévérité | Critique : **{by_sev['critique']}** · Majeure : **{by_sev['majeure']}** · Mineure : **{by_sev['mineure']}** |"
    )
    lines.append("")

    lines.append("## 2. Ventilation par SSP (`SSP_245`–`SSP_248`)")
    lines.append("")
    lines.append("| SSP | Code | Intitulé | Cours | Audités | Touchés | Fixes | Taux / cours | Critique | Majeure | Mineure |")
    lines.append("|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for ssp in SSP_ORDER:
        s = by_ssp[ssp]
        rate = (s["fixes"] / s["courses_total"]) if s["courses_total"] else 0.0
        sev = s["by_severity"]
        lines.append(
            f"| `{ssp}` | `{s['code']}` | {md_escape(s['nom'])} | {s['courses_total']} | {s['courses_audited']} | {s['courses_with_fixes']} | **{s['fixes']}** | {rate:.3f} | {sev['critique']} | {sev['majeure']} | {sev['mineure']} |"
        )
    lines.append("")

    lines.append("## 3. Typologie des erreurs corrigées (8 types canoniques)")
    lines.append("")
    lines.append("| Type d'erreur | Effectif | Part (%) | Critique | Majeure | Mineure |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for ftype in CANONICAL_TYPES:
        cnt = by_type.get(ftype, 0)
        pct = (cnt / total_fixes * 100.0) if total_fixes else 0.0
        c_crit = sum(1 for fx in fixes if fx["type"] == ftype and fx["severity"] == "critique")
        c_maj = sum(1 for fx in fixes if fx["type"] == ftype and fx["severity"] == "majeure")
        c_min = sum(1 for fx in fixes if fx["type"] == ftype and fx["severity"] == "mineure")
        lines.append(f"| `{ftype}` | **{cnt}** | {pct:.1f} % | {c_crit} | {c_maj} | {c_min} |")
    lines.append("")

    lines.append("## 4. Densité par section clinique")
    lines.append("")
    if by_section:
        lines.append("| Section | Corrections |")
        lines.append("|---|---:|")
        for sec, cnt in sorted(by_section.items(), key=lambda kv: (-kv[1], kv[0])):
            lines.append(f"| `{sec}` | {cnt} |")
    else:
        lines.append("_Aucune correction enregistrée pour le moment._")
    lines.append("")

    lines.append("## 5. Classement par cours")
    lines.append("")
    touched = [c for c in courses if c["fix_count"] > 0]
    touched.sort(key=lambda c: (-c["fix_count"], -c["fixes_by_severity"]["critique"], c["ssp"], c["order"]))
    if touched:
        lines.append("| SSP | Cours | Titre | Total fixes | Critique | Majeure | Mineure | Statut audit |")
        lines.append("|---|---|---|---:|---:|---:|---:|---|")
        for c in touched:
            sev = c["fixes_by_severity"]
            lines.append(
                f"| `{c['ssp']}` | `{c['course']}` | {md_escape(c['title'])} | **{c['fix_count']}** | {sev['critique']} | {sev['majeure']} | {sev['mineure']} | `{c['audit_status']}` |"
            )
    else:
        lines.append("_Aucun cours n'a encore reçu de correction._")
    lines.append("")
    clean_audited = [c for c in courses if c["audit_status"] == "done" and c["fix_count"] == 0]
    lines.append(f"**Cours audités avec 0 erreur détectée ({len(clean_audited)})** : " + (
        ", ".join(f"`{c['key']}`" for c in clean_audited) if clean_audited else "_aucun à ce stade_"
    ))
    lines.append("")

    lines.append("## 6. Registre détaillé des corrections")
    lines.append("")
    if fixes:
        lines.append("| # | t (s) | SSP | Cours | Section | Type | Sévérité | Agent | Source | Avant | Après | Justification |")
        lines.append("|---:|---:|---|---|---|---|---|---|---|---|---|---|")
        for fx in fixes:
            lines.append(
                f"| {fx['n']} | {fx['t_sec']:.3f} | `{fx['ssp']}` | `{fx['course']}` | `{fx['section']}` | `{fx['type']}` | `{fx['severity']}` | `{md_escape(fx['agent'])}` | {md_escape(fx['source'])} | {md_escape(fx['before'])} | {md_escape(fx['after'])} | {md_escape(fx['detail'])} |"
            )
    else:
        lines.append("_Aucune correction enregistrée dans `_outils/telemetry_events.jsonl`._")
    lines.append("")

    return "\n".join(lines)


def cmd_init(args: argparse.Namespace, base_dir: str, lock_timeout: float) -> int:
    outils_dir = os.path.join(base_dir, "_outils")
    lock_path = os.path.join(outils_dir, "telemetry.lock")
    events_path = os.path.join(outils_dir, "telemetry_events.jsonl")

    init_dt = parse_iso_utc(args.ts)
    with TelemetryLock(lock_path, timeout=lock_timeout):
        if os.path.isfile(events_path) and os.path.getsize(events_path) > 0 and not args.force:
            state = rebuild_under_lock(base_dir)
            print(
                json.dumps(
                    {
                        "status": "preserved_existing",
                        "events_path": events_path,
                        "total_events": state["integrity"]["total_events"],
                        "total_fixes": state["summary"]["total_fixes"],
                        "total_courses": state["summary"]["total_courses"],
                    },
                    ensure_ascii=False,
                )
            )
            return 0

        seeds = make_baseline_events(init_dt)
        content = "".join(json.dumps(ev, ensure_ascii=False, separators=(",", ":")) + "\n" for ev in seeds)
        atomic_write_text(events_path, content)
        state = rebuild_under_lock(base_dir)
        print(
            json.dumps(
                {
                    "status": "initialized",
                    "events_path": events_path,
                    "total_events": state["integrity"]["total_events"],
                    "total_fixes": state["summary"]["total_fixes"],
                    "total_courses": state["summary"]["total_courses"],
                },
                ensure_ascii=False,
            )
        )
        return 0


def cmd_event(args: argparse.Namespace, base_dir: str, lock_timeout: float) -> int:
    agent = (args.agent or "").strip()
    detail = (args.detail or "").strip()
    if not agent:
        raise ValueError("--agent ne peut pas être vide")
    if not detail:
        raise ValueError("--detail ne peut pas être vide")

    ssp = normalize_ssp(args.ssp)
    course = normalize_course(args.course)
    phase = normalize_phase(args.phase)
    status = normalize_status(args.status)
    milestone = infer_milestone(args.milestone, ssp, phase, agent)
    dt = parse_iso_utc(args.ts)

    outils_dir = os.path.join(base_dir, "_outils")
    lock_path = os.path.join(outils_dir, "telemetry.lock")
    events_path = os.path.join(outils_dir, "telemetry_events.jsonl")

    with TelemetryLock(lock_path, timeout=lock_timeout):
        existing_records, _ = read_events_jsonl(events_path)
        seq = len(existing_records) + 1
        rec = {
            "id": f"evt-{uuid.uuid4().hex[:12]}",
            "seq": seq,
            "kind": "event",
            "ts": format_iso_ms(dt),
            "t_sec": compute_t_sec(dt),
            "agent": agent,
            "milestone": milestone,
            "ssp": ssp,
            "course": course,
            "phase": phase,
            "status": status,
            "detail": detail,
        }
        append_jsonl(events_path, rec)
        state = rebuild_under_lock(base_dir)

    print(
        json.dumps(
            {
                "status": "ok",
                "kind": "event",
                "t_sec": rec["t_sec"],
                "total_events": state["integrity"]["total_events"],
                "total_fixes": state["summary"]["total_fixes"],
            },
            ensure_ascii=False,
        )
    )
    return 0


def cmd_fix(args: argparse.Namespace, base_dir: str, lock_timeout: float) -> int:
    required_vals = {
        "--agent": args.agent,
        "--ssp": args.ssp,
        "--course": args.course,
        "--section": args.section,
        "--type": args.type,
        "--severity": args.severity,
        "--source": args.source,
        "--before": args.before,
        "--after": args.after,
        "--detail": args.detail,
    }
    for flag, val in required_vals.items():
        if not val or not val.strip():
            raise ValueError(f"{flag} est obligatoire et ne peut pas être vide")

    agent = args.agent.strip()
    ssp = normalize_ssp(args.ssp)
    course = normalize_course(args.course)
    section = normalize_section(args.section)
    ftype = normalize_type(args.type)
    severity = normalize_severity(args.severity)
    source = args.source.strip()
    before = args.before.strip()
    after = args.after.strip()
    detail = args.detail.strip()
    milestone = infer_milestone(args.milestone, ssp, "audit_med", agent)
    dt = parse_iso_utc(args.ts)

    outils_dir = os.path.join(base_dir, "_outils")
    lock_path = os.path.join(outils_dir, "telemetry.lock")
    events_path = os.path.join(outils_dir, "telemetry_events.jsonl")

    with TelemetryLock(lock_path, timeout=lock_timeout):
        existing_records, _ = read_events_jsonl(events_path)
        seq = len(existing_records) + 1
        rec = {
            "id": f"fix-{uuid.uuid4().hex[:12]}",
            "seq": seq,
            "kind": "fix",
            "ts": format_iso_ms(dt),
            "t_sec": compute_t_sec(dt),
            "agent": agent,
            "milestone": milestone,
            "ssp": ssp,
            "course": course,
            "phase": "audit_med",
            "status": "in_progress",
            "section": section,
            "type": ftype,
            "severity": severity,
            "source": source,
            "before": before,
            "after": after,
            "detail": detail,
        }
        append_jsonl(events_path, rec)
        state = rebuild_under_lock(base_dir)

    print(
        json.dumps(
            {
                "status": "ok",
                "kind": "fix",
                "n": state["summary"]["total_fixes"],
                "t_sec": rec["t_sec"],
                "type": ftype,
                "severity": severity,
                "total_events": state["integrity"]["total_events"],
            },
            ensure_ascii=False,
        )
    )
    return 0


def cmd_rebuild(args: argparse.Namespace, base_dir: str, lock_timeout: float) -> int:
    outils_dir = os.path.join(base_dir, "_outils")
    lock_path = os.path.join(outils_dir, "telemetry.lock")
    with TelemetryLock(lock_path, timeout=lock_timeout):
        state = rebuild_under_lock(base_dir)
    print(
        json.dumps(
            {
                "status": "rebuilt",
                "total_events": state["integrity"]["total_events"],
                "total_fixes": state["summary"]["total_fixes"],
                "corrupt_lines_skipped": state["integrity"]["corrupt_lines_skipped"],
                "total_courses": state["summary"]["total_courses"],
            },
            ensure_ascii=False,
        )
    )
    return 0


def cmd_report(args: argparse.Namespace, base_dir: str, lock_timeout: float) -> int:
    outils_dir = os.path.join(base_dir, "_outils")
    lock_path = os.path.join(outils_dir, "telemetry.lock")
    out_arg = args.out or "RAPPORT_PENETRATION_ERRATIQUE.md"
    out_path = out_arg if os.path.isabs(out_arg) else os.path.join(base_dir, out_arg)

    with TelemetryLock(lock_path, timeout=lock_timeout):
        events_path = os.path.join(outils_dir, "telemetry_events.jsonl")
        records, corrupt_count = read_events_jsonl(events_path)
        state = build_state(base_dir, records, corrupt_count)
    md = generate_markdown_report(state)
    atomic_write_text(out_path, md)
    print(
        json.dumps(
            {
                "status": "report_written",
                "out_path": out_path,
                "total_fixes": state["summary"]["total_fixes"],
                "courses_with_fixes": state["summary"]["courses_with_fixes"],
            },
            ensure_ascii=False,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    sub_common = argparse.ArgumentParser(add_help=False)
    sub_common.add_argument(
        "--base-dir",
        default=argparse.SUPPRESS,
        help="Répertoire racine du projet (par défaut : parent de _outils/).",
    )
    sub_common.add_argument(
        "--lock-timeout",
        type=float,
        default=argparse.SUPPRESS,
        help="Timeout d'acquisition du verrou en secondes (défaut : 30.0).",
    )

    parser = argparse.ArgumentParser(
        description="CLI de télémétrie temps réel verrouillée pour M_LIVE et Auditeurs Médicaux Extrêmes."
    )
    parser.add_argument(
        "--base-dir",
        default=DEFAULT_BASE_DIR,
        help="Répertoire racine du projet (par défaut : parent de _outils/).",
    )
    parser.add_argument(
        "--lock-timeout",
        type=float,
        default=30.0,
        help="Timeout d'acquisition du verrou en secondes (défaut : 30.0).",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", parents=[sub_common], help="Initialise la télémétrie (idempotent).")
    p_init.add_argument("--force", action="store_true", help="Réinitialise même si telemetry_events.jsonl existe.")
    p_init.add_argument("--ts", default=None, help="Horodatage ISO UTC optionnel de l'initialisation.")

    p_evt = sub.add_parser("event", parents=[sub_common], help="Enregistre un événement de cycle de vie.")
    p_evt.add_argument("--agent", required=True, help="Identifiant de l'agent.")
    p_evt.add_argument("--ssp", required=True, help="Portée SSP_245..248, SHARED, E2E ou ALL.")
    p_evt.add_argument("--course", default="all", help="Fichier du cours ou 'all'.")
    p_evt.add_argument("--phase", required=True, help="Phase (survey, impl, condense, canvas, why, audit_med, verify, assemble, e2e, report).")
    p_evt.add_argument("--status", required=True, help="Statut (started, in_progress, done, error).")
    p_evt.add_argument("--detail", required=True, help="Description de l'événement.")
    p_evt.add_argument("--milestone", default=None, help="Jalon explicite optionnel (M_LIVE, M1..M6, E2E).")
    p_evt.add_argument("--ts", default=None, help="Horodatage ISO UTC optionnel.")

    p_fix = sub.add_parser("fix", parents=[sub_common], help="Enregistre une correction médicale horodatée.")
    p_fix.add_argument("--agent", required=True, help="Identifiant de l'auditeur médical.")
    p_fix.add_argument("--ssp", required=True, help="SSP (SSP_245..248).")
    p_fix.add_argument("--course", required=True, help="Nom de fichier du cours (LOT_nnn_...html).")
    p_fix.add_argument("--section", required=True, help="Section (p1..p14, canvas, modal, sources).")
    p_fix.add_argument("--type", required=True, help="Type canonique (8 types).")
    p_fix.add_argument("--severity", required=True, help="Sévérité (critique, majeure, mineure).")
    p_fix.add_argument("--source", required=True, help="Source médicale vérifiée.")
    p_fix.add_argument("--before", required=True, help="Résumé avant correction.")
    p_fix.add_argument("--after", required=True, help="Résumé après correction.")
    p_fix.add_argument("--detail", required=True, help="Justification médicale.")
    p_fix.add_argument("--milestone", default=None, help="Jalon explicite optionnel.")
    p_fix.add_argument("--ts", default=None, help="Horodatage ISO UTC optionnel.")

    sub.add_parser("rebuild", parents=[sub_common], help="Reconstruit telemetry_live.{json,js} depuis le JSONL.")

    p_rep = sub.add_parser("report", parents=[sub_common], help="Génère le rapport statistique Markdown.")
    p_rep.add_argument("--out", default="RAPPORT_PENETRATION_ERRATIQUE.md", help="Chemin du rapport Markdown.")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    base_dir = os.path.abspath(args.base_dir)
    lock_timeout = float(args.lock_timeout)

    try:
        if args.command == "init":
            return cmd_init(args, base_dir, lock_timeout)
        if args.command == "event":
            return cmd_event(args, base_dir, lock_timeout)
        if args.command == "fix":
            return cmd_fix(args, base_dir, lock_timeout)
        if args.command == "rebuild":
            return cmd_rebuild(args, base_dir, lock_timeout)
        if args.command == "report":
            return cmd_report(args, base_dir, lock_timeout)
        parser.error(f"Sous-commande inconnue: {args.command}")
        return 2
    except ValueError as exc:
        sys.stderr.write(f"[telemetry_log] Erreur de validation: {exc}\n")
        return 2
    except TimeoutError as exc:
        sys.stderr.write(f"[telemetry_log] Erreur de verrouillage: {exc}\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
