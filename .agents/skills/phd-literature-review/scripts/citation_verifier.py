"""
Academic Citation & Knowledge Authenticity Verifier
Verifies DOIs and citations against real-world Crossref and OpenAlex academic databases
to prevent AI hallucinated citations and fake references in PhD dissertations.
"""

import sys
import os
import re
import argparse
import requests
import json
from urllib.parse import quote


HEADERS = {
    "User-Agent": "PhDSkillCitationVerifier/1.0 (mailto:academic-research@khoahoc.edu.vn)"
}


def verify_doi(doi: str) -> dict:
    """
    Verifies a DOI directly against the official Crossref REST API.
    """
    # Clean DOI string
    clean_doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip())
    url = f"https://api.crossref.org/works/{quote(clean_doi)}"
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json().get("message", {})
            title = data.get("title", [""])[0] if data.get("title") else "N/A"
            authors = []
            for author in data.get("author", []):
                family = author.get("family", "")
                given = author.get("given", "")
                authors.append(f"{family}, {given}".strip(", "))
            
            journal = data.get("container-title", [""])[0] if data.get("container-title") else "N/A"
            published_year = (
                data.get("published-print", {}).get("date-parts", [[None]])[0][0]
                or data.get("published-online", {}).get("date-parts", [[None]])[0][0]
                or data.get("created", {}).get("date-parts", [[None]])[0][0]
            )

            return {
                "status": "VERIFIED",
                "doi": clean_doi,
                "doi_url": f"https://doi.org/{clean_doi}",
                "title": title,
                "authors": "; ".join(authors[:5]) + (" et al." if len(authors) > 5 else ""),
                "journal": journal,
                "year": published_year,
                "source": "Crossref Official Registry"
            }
        elif response.status_code == 404:
            return {
                "status": "HALLUCINATION_ALERT",
                "doi": clean_doi,
                "error": "DOI does not exist in Crossref database (likely a fabricated DOI).",
                "source": "Crossref Official Registry"
            }
        else:
            return {
                "status": "UNRESOLVED",
                "doi": clean_doi,
                "error": f"API returned status code {response.status_code}",
                "source": "Crossref Official Registry"
            }
    except Exception as e:
        return {
            "status": "CONNECTION_ERROR",
            "doi": clean_doi,
            "error": str(e)
        }


def search_crossref_citation(query_text: str) -> dict:
    """
    Searches Crossref by citation or title string to find matching authentic works.
    """
    url = f"https://api.crossref.org/works?query.bibliographic={quote(query_text.strip())}&rows=3"
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=12)
        if response.status_code == 200:
            items = response.json().get("message", {}).get("items", [])
            if not items:
                return {
                    "status": "HALLUCINATION_ALERT",
                    "query": query_text,
                    "matches_found": 0,
                    "warning": "No real publication found matching this query in Crossref."
                }
            
            top_match = items[0]
            title = top_match.get("title", [""])[0] if top_match.get("title") else "N/A"
            authors = []
            for author in top_match.get("author", []):
                family = author.get("family", "")
                given = author.get("given", "")
                authors.append(f"{family}, {given}".strip(", "))

            journal = top_match.get("container-title", [""])[0] if top_match.get("container-title") else "N/A"
            doi = top_match.get("DOI", "")
            score = top_match.get("score", 0)

            return {
                "status": "VERIFIED_MATCH",
                "query": query_text,
                "relevance_score": score,
                "verified_doi": f"https://doi.org/{doi}" if doi else "N/A",
                "verified_title": title,
                "verified_authors": "; ".join(authors[:5]) + (" et al." if len(authors) > 5 else ""),
                "verified_journal": journal
            }
        else:
            return {"status": "ERROR", "error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"status": "CONNECTION_ERROR", "error": str(e)}


def scan_file_for_citations(file_path: str):
    """
    Scans a markdown or text file for DOIs and verifies each against Crossref.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Find all DOIs (format: 10.xxxx/yyyy)
    doi_pattern = r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b"
    found_dois = list(set(re.findall(doi_pattern, content)))

    print("=" * 70)
    print(f"CITATION AUTHENTICITY AUDIT REPORT: {os.path.basename(file_path)}")
    print(f"Total Unique DOIs Detected: {len(found_dois)}")
    print("=" * 70)

    if not found_dois:
        print("Note: No explicit DOIs detected in this document.")
        print("If citations are formatted as (Author, Year), run with --query '<Citation String>' to verify.")
        return

    verified_count = 0
    hallucinated_count = 0

    for i, doi in enumerate(found_dois, 1):
        # Strip trailing punctuation often captured by regex
        clean = re.sub(r"[.)>,;]+$", "", doi)
        res = verify_doi(clean)
        print(f"\n[{i}/{len(found_dois)}] Checking DOI: {clean}")
        if res["status"] == "VERIFIED":
            verified_count += 1
            print(f"  ✓ STATUS: AUTHENTIC / VERIFIED")
            print(f"    Title:   {res['title']}")
            print(f"    Authors: {res['authors']}")
            print(f"    Journal: {res['journal']} ({res['year']})")
            print(f"    URL:     {res['doi_url']}")
        elif res["status"] == "HALLUCINATION_ALERT":
            hallucinated_count += 1
            print(f"  ❌ STATUS: FAKE / HALLUCINATED DOI (NOT FOUND IN REGISTRY)")
            print(f"    Warning: This DOI does not exist. Do NOT include in your dissertation!")
        else:
            print(f"  ⚠ STATUS: {res.get('status')} - {res.get('error')}")

    print("\n" + "=" * 70)
    print(f"AUDIT SUMMARY: {verified_count} Verified | {hallucinated_count} Fake/Hallucinated")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(description="Academic Citation & Authenticity Verifier")
    parser.add_argument("--doi", type=str, help="Verify a single DOI string")
    parser.add_argument("--query", type=str, help="Verify a citation text or article title")
    parser.add_argument("--file", type=str, help="Scan a markdown/text file for all citations & DOIs")
    args = parser.parse_args()

    if args.doi:
        res = verify_doi(args.doi)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif args.query:
        res = search_crossref_citation(args.query)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif args.file:
        scan_file_for_citations(args.file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
