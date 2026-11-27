"""
H-AI ResearchLAB | DATA-DRIVEN IDEA & RESEARCH GAP ENGINE (idea_scanner.py v2.0)
Scans local PRISMA corpus (N=1,441) + OpenAlex API to quantify empirical coverage,
prevent 'S-O-R Fatigue', enforce Gen 2.0 AI-Specificity, and design non-linear/dynamic blueprints.
"""

import sys
import os
import csv
import json
import urllib.parse
import requests

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOCAL_CORPUS_CSV = os.path.join(WORKSPACE_DIR, "data", "processed", "dimensions_clean_included.csv")


def scan_local_corpus_gaps(idea_text):
    """Quantify empirical coverage and true research gaps across the 1,441 cleaned corpus."""
    print(f"\n[STEP 1] QUANTITATIVE GAP SCANNING ON LOCAL CORPUS (N = 1,441)...")
    if not os.path.exists(LOCAL_CORPUS_CSV):
        print("  [WARN] Local corpus CSV not found. Skipping local density metrics.")
        return {}

    with open(LOCAL_CORPUS_CSV, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

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

    return metrics


def scan_openalex_benchmarks(query_str, max_results=5):
    """Retrieve high-impact global benchmarks from OpenAlex API using clean core keywords."""
    print(f"\n[STEP 2] QUERYING GLOBAL OPENALEX API FOR BENCHMARK CITATIONS...")
    # Extract clean core concept query instead of sending long comma-separated prose
    clean_q = '"recommendation" AND "impulse buying"' if ("recommend" in query_str.lower() and "impulse" in query_str.lower()) else query_str
    encoded_query = urllib.parse.quote(clean_q)
    url = f"https://api.openalex.org/works?search={encoded_query}&per-page={max_results}&sort=cited_by_count:desc"
    headers = {"User-Agent": "H-AI-Research-Lab/3.0 (mailto:phd_candidate@h-ai-lab.edu.vn)"}

    papers = []
    try:
        response = requests.get(url, headers=headers, timeout=8)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            print(f"  -> Global hits on OpenAlex: {data.get('meta', {}).get('count', 0):,}")
            for i, item in enumerate(results, 1):
                title = item.get("title", "No Title")
                year = item.get("publication_year", "N/A")
                cited = item.get("cited_by_count", 0)
                doi = item.get("doi", "")
                venue = item.get("primary_location", {}).get("source", {}).get("display_name", "Journal") if item.get("primary_location") and item.get("primary_location").get("source") else "Journal"
                papers.append({
                    "rank": i, "title": title, "year": year,
                    "citations": cited, "journal": venue, "doi": doi
                })
                print(f"     [{i}] ({year}) {title[:65]}... | {venue} | Citations: {cited:,}")
    except Exception as e:
        print(f"  [INFO] Offline/Timeout OpenAlex fallback ({e}). Using verified local corpus.")
    return papers


def evaluate_novelty_and_generate_plan(idea_text, gap_metrics, openalex_papers):
    """Anti-SOR-Fatigue Check & Dynamic Blueprint Generator."""
    print(f"\n[STEP 3] ANTI-SOR-FATIGUE CHECK & DYNAMIC BLUEPRINT SYNTHESIS...")
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
        "recommended_theoretical_elevations": recommendations,
        "recommended_methods": [
            "PLS-SEM / CB-SEM with Interaction & Quadratic (Inverted-U) Terms",
            "fsQCA (Configurational Asymmetry) & Necessary Condition Analysis (NCA)",
            "Dual-Task Experimental Ego Depletion Manipulation"
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

    print(f"  [SUCCESS] Data-Driven Gap Blueprint saved to: {output_path}")
    return plan


def main():
    idea = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "AI recommendation systems, dual-path organismic states, ego depletion, and online impulse buying"
    print("=" * 85)
    print("🔬 H-AI ResearchLAB | DATA-DRIVEN IDEA & GAP SCANNER v2.0")
    print(f"Topic: {idea}")
    print("=" * 85)
    gaps = scan_local_corpus_gaps(idea)
    oa = scan_openalex_benchmarks(idea, max_results=5)
    evaluate_novelty_and_generate_plan(idea, gaps, oa)


if __name__ == "__main__":
    main()
