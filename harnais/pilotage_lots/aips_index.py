#!/usr/bin/env python3
"""Inventorie l'index AIPS Medina ; ne télécharge et ne valide aucune prescription."""
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
from zipfile import ZipFile

NS = {"a": "https://simisinfo.refdata.ch/MedicinalDocuments/1.0/"}


def inventory(path, query="", language="fr", kind="SmPC"):
    raw = Path(path).read_bytes()
    types, languages, hosts = Counter(), Counter(), Counter()
    matches, bundles, documents = [], 0, 0
    with ZipFile(path) as archive:
        xml = [x for x in archive.infolist() if x.filename.lower().endswith(".xml")]
        if len(xml) != 1 or xml[0].file_size > 64_000_000:
            raise ValueError("Un index XML unique de moins de 64 Mo est attendu")
        with archive.open(xml[0]) as source:
            generated = None
            for event, node in ET.iterparse(source, events=("start", "end")):
                if generated is None and event == "start":
                    generated = node.attrib.get("generatedOn")
                if event != "end" or node.tag != "{" + NS["a"] + "}MedicinalDocumentsBundle":
                    continue
                bundles += 1
                doc_kind = node.findtext("a:Type", default="", namespaces=NS)
                types[doc_kind] += 1
                authorizations = [x.text for x in node.findall("a:RegulatedAuthorization/a:Identifier", NS)]
                for doc in node.findall("a:AttachedDocument", NS):
                    documents += 1
                    lang = doc.findtext("a:Language", default="", namespaces=NS)
                    title = doc.findtext("a:Description", default="", namespaces=NS)
                    languages[lang] += 1
                    references = []
                    for reference in doc.findall("a:DocumentReference", NS):
                        url = reference.findtext("a:Url", default="", namespaces=NS)
                        hosts[urlparse(url).hostname or ""] += 1
                        references.append({"content_type": reference.findtext("a:ContentType", default="", namespaces=NS), "url": url})
                    if query and query.casefold() in title.casefold() and lang == language and doc_kind == kind:
                        matches.append({"title": title, "type": doc_kind, "language": lang,
                                        "authorization_identifiers_as_read": authorizations,
                                        "document_start": doc.findtext("a:Period/a:Start", default="", namespaces=NS),
                                        "references": references, "professional_information_read": False})
                node.clear()
    return {"archive_bytes": len(raw), "archive_sha256": sha256(raw).hexdigest(), "generated_on": generated,
            "bundles": bundles, "attached_documents": documents, "bundle_types": dict(types),
            "document_languages": dict(languages), "reference_hosts": dict(hosts), "matches": matches,
            "embedded_monograph_text": False, "clinical_validation": False,
            "scope": "Index de références ; un numéro est lu dans RegulatedAuthorization, jamais déduit d'une URL."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("--query", default="")
    parser.add_argument("--language", default="fr", choices=("fr", "de", "it", "en"))
    parser.add_argument("--type", default="SmPC", choices=("SmPC", "PIL", "PL"))
    args = parser.parse_args()
    print(json.dumps(inventory(args.archive, args.query, args.language, args.type), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
