"""
H-AI ResearchLAB | DATA-DRIVEN IDEA, GAP & SNOWBALL KEYWORD EXPANDER (idea_scanner.py v3.0)
1. Scans final included corpus (N=866) to quantify empirical coverage & gaps.
2. Queries OpenAlex API Round 1 for global high-impact benchmarks.
3. Snowball Keyword Expander: Automatically formulates targeted niche Boolean queries
   from detected gaps (<5% coverage), crawls Round 2 papers from OpenAlex, deduplicates
   against local corpus, and extracts emerging keywords for VOSviewer & ideation.
"""

import sys
import os
import csv
import json
import re
import urllib.parse
import requests
from collections import Counter

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOCAL_CORPUS_CSV = os.path.join(WORKSPACE_DIR, "data", "processed", "dimensions_clean_included.csv")

# Gap-to-Snowball Keyword Expansion Dictionary
GAP_EXPANSION_MAP = {
    "ego_depletion": {
        "query": '("ego depletion" OR "self-regulatory depletion" OR "decision fatigue") AND ("impulse buying" OR "impulsive purchase")',
        "seed_keywords": ["ego depletion", "cognitive load", "decision fatigue", "self-control failure"]
    },
    "surveillance_reactance": {
        "query": '("algorithmic surveillance" OR "psychological reactance" OR "dark patterns") AND ("personalization" OR "recommender")',
        "seed_keywords": ["algorithmic surveillance", "psychological reactance", "privacy fatigue", "dark patterns"]
    },
    "inverted_u_nonlinear": {
        "query": '("inverted-U" OR "curvilinear" OR "threshold effect") AND ("personalization" OR "recommendation") AND "privacy"',
        "seed_keywords": ["inverted-U effect", "curvilinear personalization", "privacy threshold"]
    },
    "multiplicative_interaction": {
        "query": '("interaction effect" OR "moderated mediation") AND ("e-satisfaction" OR "cognitive") AND ("arousal" OR "impulse buying")',
        "seed_keywords": ["cognitive-affective interaction", "moderated mediation", "permission structure"]
    },
    "post_purchase_regret": {
        "query": '("post-purchase regret" OR "cognitive dissonance") AND ("impulse buying" OR "e-commerce") AND ("satisfaction" OR "return")',
        "seed_keywords": ["post-purchase regret", "cognitive dissonance", "product returns", "CLV erosion"]
    },
    "genai_conversational": {
        "query": '("generative AI" OR "conversational agent" OR "LLM") AND ("recommendation" OR "shopping") AND "impulse"',
        "seed_keywords": ["generative AI", "conversational commerce", "anthropomorphism", "social agency"]
    }
}


def scan_local_corpus_gaps(idea_text):
    """Quantify empirical coverage and true research gaps strictly across the N = 866 final included corpus."""
    print(f"\n[STEP 1] QUANTITATIVE GAP SCANNING ON FINAL INCLUDED CORPUS (N = 866)...")
    if not os.path.exists(LOCAL_CORPUS_CSV):
        print("  [WARN] Local corpus CSV not found. Skipping local density metrics.")
        return {}, set(), set()

    with open(LOCAL_CORPUS_CSV, "r", encoding="utf-8") as f:
        all_rows = list(csv.DictReader(f))

    existing_dois = {str(r.get("DOI", "")).strip().lower() for r in all_rows if r.get("DOI")}
    existing_titles = {re.sub(r'\W+', ' ', str(r.get("Title", "")).lower()).strip() for r in all_rows if r.get("Title")}

    def rel_score(r):
        t = (str(r.get("Title", "")) + " " + str(r.get("Abstract", ""))).lower()
        return sum(1 for k in ["impulse", "impulsive", "recommend", "personaliz", "algorithm", "ai ", "artificial intelligence", "e-commerce", "online shopping", "retail", "consumer", "livestream", "live stream", "satisfaction"] if k in t)

    rows = sorted(all_rows, key=lambda r: (-rel_score(r), -int(str(r.get("PubYear", "0") or 0))))[:866]
    total = len(rows)

    counts = {
        "sor_framework": 0,
        "genai_conversational": 0,
        "ego_depletion": 0,
        "surveillance_reactance": 0,
        "post_purchase_regret": 0,
        "inverted_u_nonlinear": 0,
        "multiplicative_interaction": 0,
    }

    for r in rows:
        txt = (str(r.get("Title", "")) + " " + str(r.get("Abstract", ""))).lower()
        if "s-o-r" in txt or "stimulus-organism-response" in txt or "stimulus organism response" in txt:
            counts["sor_framework"] += 1
        if any(k in txt for k in ["generative ai", "chatgpt", "llm", "large language model", "conversational ai", "chatbot"]):
            counts["genai_conversational"] += 1
        if "ego depletion" in txt or "self-regulatory" in txt or "decision fatigue" in txt:
            counts["ego_depletion"] += 1
        if any(k in txt for k in ["surveillance", "reactance", "dark pattern", "creepiness", "privacy fatigue"]):
            counts["surveillance_reactance"] += 1
        if any(k in txt for k in ["regret", "remorse", "dissonance", "product return"]):
            counts["post_purchase_regret"] += 1
        if any(k in txt for k in ["inverted-u", "inverted u", "curvilinear", "nonlinear", "non-linear", "threshold effect"]):
            counts["inverted_u_nonlinear"] += 1
        if any(k in txt for k in ["interaction effect", "multiplicative", "moderated mediation"]):
            counts["multiplicative_interaction"] += 1

    metrics = {k: {"count": v, "pct": round((v / total) * 100, 2) if total else 0} for k, v in counts.items()}
    print(f"  -> Corpus Analyzed: {total:,} unique records.")
    for k, m in metrics.items():
        print(f"     - {k:28s}: {m['count']:4d} papers ({m['pct']:5.2f}%)")

    return metrics, existing_dois, existing_titles


def query_openalex(query_str, max_results=5):
    """Helper to query OpenAlex API cleanly."""
    encoded_query = urllib.parse.quote(query_str)
    url = f"https://api.openalex.org/works?search={encoded_query}&per-page={max_results}&sort=cited_by_count:desc"
    headers = {"User-Agent": "H-AI-Research-Lab/3.0 (mailto:phd_candidate@h-ai-lab.edu.vn)"}

    papers = []
    total_hits = 0
    try:
        response = requests.get(url, headers=headers, timeout=8)
        if response.status_code == 200:
            data = response.json()
            total_hits = data.get("meta", {}).get("count", 0)
            for i, item in enumerate(data.get("results", []), 1):
                title = item.get("title", "No Title") or "No Title"
                year = item.get("publication_year", "N/A")
                cited = item.get("cited_by_count", 0)
                raw_doi = item.get("doi", "") or ""
                clean_doi = raw_doi.replace("https://doi.org/", "").strip().lower()
                venue = item.get("primary_location", {}).get("source", {}).get("display_name", "Journal") if item.get("primary_location") and item.get("primary_location").get("source") else "Journal"
                concepts = [c.get("display_name", "") for c in item.get("concepts", [])[:5] if c.get("display_name")]
                papers.append({
                    "rank": i, "title": title, "year": year,
                    "citations": cited, "journal": venue, "doi": clean_doi,
                    "concepts": concepts
                })
    except Exception:
        pass
    return total_hits, papers


def scan_openalex_benchmarks(query_str, max_results=5):
    """Retrieve high-impact global benchmarks from OpenAlex API using clean core keywords."""
    print(f"\n[STEP 2] QUERYING GLOBAL OPENALEX API FOR BENCHMARK CITATIONS...")
    clean_q = '"recommendation" AND "impulse buying"' if ("recommend" in query_str.lower() and "impulse" in query_str.lower()) else query_str
    total_hits, papers = query_openalex(clean_q, max_results=max_results)
    print(f"  -> Global hits on OpenAlex: {total_hits:,}")
    for p in papers:
        print(f"     [{p['rank']}] ({p['year']}) {p['title'][:65]}... | {p['journal']} | Citations: {p['citations']:,}")
    return papers


def snowball_expand_and_crawl(gap_metrics, existing_dois, existing_titles, threshold_pct=5.0):
    """
    Snowball Keyword Expander:
    1. Detects under-researched constructs (< threshold_pct in N=866).
    2. Formulates targeted Boolean expansion queries.
    3. Executes Round-2 OpenAlex snowball crawl and deduplicates against local corpus.
    4. Extracts emerging keywords for VOSviewer & future paper ideation.
    """
    print(f"\n[STEP 3] SNOWBALL KEYWORD EXPANDER (GAP THRESHOLD < {threshold_pct}%)...")
    expanded_queries = []
    snowball_papers = []
    emerging_concept_counter = Counter()
    seen_snowball_dois = set(existing_dois)
    seen_snowball_titles = set(existing_titles)

    for gap_key, stats in gap_metrics.items():
        if stats["pct"] < threshold_pct and gap_key in GAP_EXPANSION_MAP:
            exp = GAP_EXPANSION_MAP[gap_key]
            q = exp["query"]
            expanded_queries.append({"gap": gap_key, "coverage_pct": stats["pct"], "expanded_query": q, "seed_keywords": exp["seed_keywords"]})
            print(f"  -> Expanding Gap [{gap_key} ({stats['pct']}%)] -> Query: {q}")

            hits, raw_papers = query_openalex(q, max_results=6)
            added = 0
            for p in raw_papers:
                norm_title = re.sub(r'\W+', ' ', p["title"].lower()).strip()
                if (p["doi"] and p["doi"] in seen_snowball_dois) or (norm_title in seen_snowball_titles):
                    continue
                if p["doi"]:
                    seen_snowball_dois.add(p["doi"])
                seen_snowball_titles.add(norm_title)
                p["source_gap"] = gap_key
                snowball_papers.append(p)
                for c in p.get("concepts", []):
                    emerging_concept_counter[c] += 1
                added += 1
            print(f"     * OpenAlex Hits: {hits:,} | Net New Deduplicated Snowball Papers Added: {added}")

    top_emerging_keywords = [kw for kw, _ in emerging_concept_counter.most_common(15)]
    snowball_output = {
        "expanded_queries": expanded_queries,
        "net_new_papers_count": len(snowball_papers),
        "top_emerging_keywords": top_emerging_keywords,
        "snowball_papers": snowball_papers
    }

    snowball_path = os.path.join(WORKSPACE_DIR, "lab_projects", "SNOWBALL_EXPANSION_CORPUS.json")
    with open(snowball_path, "w", encoding="utf-8") as f:
        json.dump(snowball_output, f, ensure_ascii=False, indent=2)

    print(f"  [SUCCESS] Snowball Expansion complete: {len(snowball_papers)} net-new papers & {len(top_emerging_keywords)} emerging keywords saved to {snowball_path}")
    return snowball_output


def evaluate_novelty_and_generate_plan(idea_text, gap_metrics, openalex_papers, snowball_data):
    """Anti-SOR-Fatigue Check & Dynamic Blueprint Generator."""
    print(f"\n[STEP 4] ANTI-SOR-FATIGUE CHECK & DYNAMIC BLUEPRINT SYNTHESIS...")
    recommendations = []

    if gap_metrics.get("inverted_u_nonlinear", {}).get("pct", 0) < 2.0:
        recommendations.append("Incorporate Curvilinear (Inverted-U) threshold modeling for personalization-privacy reactance.")
    if gap_metrics.get("post_purchase_regret", {}).get("pct", 0) < 5.0:
        recommendations.append("Add Negative Recursive Feedback Loop (Post-Purchase Regret -> Erodes Future E-Satisfaction).")
    if gap_metrics.get("ego_depletion", {}).get("pct", 0) < 5.0:
        recommendations.append("Test Ego Depletion & Cognitive Load as boundary conditions (hedged against replication debates).")
    if gap_metrics.get("genai_conversational", {}).get("pct", 0) < 10.0:
        recommendations.append("Differentiate Gen 2.0 Conversational Social Agency from Gen 1.0 Collaborative Filtering.")

    recommendations.append("Model Multiplicative Interaction (Permission Structure x Kinetic Energy) instead of additive-only S-O-R.")

    plan = {
        "idea_input": idea_text,
        "anti_sor_fatigue_protocol": "ACTIVE (Dynamic, Non-Linear, Multiplicative & Recursive Modeling)",
        "quantitative_corpus_gaps": gap_metrics,
        "snowball_expansion_summary": {
            "queries_executed": len(snowball_data.get("expanded_queries", [])),
            "net_new_papers_harvested": snowball_data.get("net_new_papers_count", 0),
            "top_emerging_keywords": snowball_data.get("top_emerging_keywords", [])
        },
        "recommended_theoretical_elevations": recommendations,
        "recommended_methods": [
            "PLS-SEM / CB-SEM with Interaction & Quadratic (Inverted-U) Terms",
            "fsQCA (Configurational Asymmetry) & Necessary Condition Analysis (NCA)",
            "Cross-Lagged Panel Modeling (RI-CLPM) for Recursive Regret Loops"
        ],
        "target_journals": [
            "Journal of Retailing and Consumer Services (Elsevier, Q1, IF: 11.0)",
            "Journal of Business Research (Elsevier, Q1, IF: 10.5)",
            "Computers in Human Behavior (Elsevier, Q1, IF: 9.0)"
        ],
        "openalex_benchmarks": openalex_papers
    }

    output_path = os.path.join(WORKSPACE_DIR, "lab_projects", "NEW_IDEA_PAPER_PLAN.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)

    print(f"  [SUCCESS] Data-Driven Gap & Snowball Blueprint saved to: {output_path}")
    return plan


def main():
    idea = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "AI recommendation systems, dual-path organismic states, ego depletion, and online impulse buying"
    print("=" * 85)
    print("🔬 H-AI ResearchLAB | DATA-DRIVEN IDEA, GAP & SNOWBALL EXPANDER v3.0")
    print(f"Topic: {idea}")
    print("=" * 85)
    gaps, existing_dois, existing_titles = scan_local_corpus_gaps(idea)
    oa = scan_openalex_benchmarks(idea, max_results=5)
    snowball_data = snowball_expand_and_crawl(gaps, existing_dois, existing_titles, threshold_pct=5.0)
    evaluate_novelty_and_generate_plan(idea, gaps, oa, snowball_data)


if __name__ == "__main__":
    main()
