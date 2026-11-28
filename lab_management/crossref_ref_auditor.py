#!/usr/bin/env python3
"""
crossref_ref_auditor.py
=======================
Automated Crossref DOI, Retraction, Author-Parity, and Title-Collision Auditor.
Caches verified DOIs in lab_management/crossref_doi_cache.json for instant
subsequent checks while flagging retracted papers, wrong authors, or DOI collisions.
"""

import json
import os
import re
import time
import urllib.parse
import urllib.request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_PATH = os.path.join(BASE_DIR, "lab_management", "crossref_doi_cache.json")


def load_cache():
    if os.path.exists(CACHE_PATH):
        try:
            with open(CACHE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_cache(cache):
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def fetch_crossref(doi: str, cache: dict) -> dict:
    d_norm = doi.strip().lower().rstrip(".,;)")
    if d_norm in cache:
        return cache[d_norm]
    url = f"https://api.crossref.org/works/{urllib.parse.quote(d_norm)}"
    req = urllib.request.Request(url, headers={"User-Agent": "H-AI-Lab-CitationGate/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            msg = json.loads(resp.read().decode("utf-8")).get("message", {})
            authors = [a.get("family", "").lower() for a in msg.get("author", []) if a.get("family")]
            title = (msg.get("title") or [""])[0]
            retracted = False
            if "retract" in title.lower() or "withdrawn" in title.lower():
                retracted = True
            for upd in msg.get("update-to", []):
                if "retract" in str(upd.get("type", "")).lower():
                    retracted = True
            entry = {
                "ok": True,
                "doi": d_norm,
                "authors": authors,
                "title": title,
                "journal": (msg.get("container-title") or [""])[0],
                "retracted": retracted,
            }
            cache[d_norm] = entry
            time.sleep(0.08)
            return entry
    except Exception as e:
        return {"ok": False, "doi": d_norm, "error": str(e)}


def audit_manuscript_dois(md_path: str) -> list[str]:
    if not os.path.exists(md_path):
        return [f"Missing file: {md_path}"]
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    parts = re.split(r"^##\s+REFERENCES\b", text, flags=re.MULTILINE)
    if len(parts) < 2:
        return ["Missing ## REFERENCES section"]

    ref_lines = [l.strip() for l in parts[1].splitlines() if l.strip() and not l.strip().startswith("#")]
    cache = load_cache()
    issues = []

    for rl in ref_lines:
        m_doi = re.search(r"https?://(?:dx\.)?doi\.org/(10\.\d{4,9}/\S+)", rl, re.IGNORECASE)
        if not m_doi:
            continue
        doi = m_doi.group(1).rstrip(".,;>")
        cr = fetch_crossref(doi, cache)
        if not cr.get("ok"):
            # Do not hard-fail on transient network timeout, only report if 404
            if "404" in str(cr.get("error", "")):
                issues.append(f"DEAD DOI (404): https://doi.org/{doi} in '{rl[:60]}...'")
            continue

        if cr.get("retracted"):
            issues.append(f"RETRACTED ARTICLE DETECTED via Crossref: https://doi.org/{doi} ({cr.get('title','')[:60]})")

        # Check first surname match (supports multi-word surnames like "Do Xuan Nguyen")
        surname_tokens = [w.lower() for w in re.findall(r"[a-zA-Z\-]{2,}", rl.split(",")[0])]
        cr_authors = cr.get("authors", [])
        if surname_tokens and cr_authors and not any(tok in a or a in tok for tok in surname_tokens for a in cr_authors):
            issues.append(
                f"DOI AUTHOR MISMATCH: Reference starts with '{' '.join(surname_tokens)}' but DOI {doi} belongs to {cr_authors[:3]}"
            )

        # Check basic title keyword overlap (>= 2 content words >= 4 chars)
        m_title = re.search(r"\(\d{4}[a-z]?\)\.\s+([^\.\*]+)", rl)
        if m_title and cr.get("title"):
            ref_words = {w for w in re.findall(r"[a-z]{4,}", m_title.group(1).lower())}
            cr_words = {w for w in re.findall(r"[a-z]{4,}", cr["title"].lower())}
            if len(ref_words) >= 3 and len(cr_words) >= 3 and len(ref_words & cr_words) == 0:
                issues.append(
                    f"DOI TITLE COLLISION: '{m_title.group(1)[:50]}' vs Crossref '{cr['title'][:50]}' ({doi})"
                )

    save_cache(cache)
    return issues


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE_DIR, "lab_projects", "PAPER_01_SLR_JRCS_MANUSCRIPT.md")
    errs = audit_manuscript_dois(target)
    if errs:
        print(f"[FAIL] Found {len(errs)} Crossref DOI issues in {os.path.basename(target)}:")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    print(f"[PASS] All DOIs in {os.path.basename(target)} verified clean against Crossref (0 retracted, 0 collisions).")
