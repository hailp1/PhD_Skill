#!/usr/bin/env python3
"""
run_full_slr_from_dimensions.py
===============================
End-to-end reproducible PRISMA 2020, Bibliometric Co-occurrence (VOSviewer-compatible),
and Regex Lexical Salience pipeline operating strictly on:
  data/raw/dimensions_raw_export.csv (2,500 records exported 2026-11-28)

Outputs:
  - lab_projects/paper1a_osf_screening_log.csv (2,500-row auditable OSF ledger)
  - data/processed/dimensions_clean_included.csv (final included corpus)
  - lab_management/paper1a_real_stats.json (all exact statistics for Paper 1A)
  - lab_projects/figures/figure3_vosviewer_real_network.png (real co-occurrence map)
"""

import csv
import json
import math
import os
import re
from collections import Counter, defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW_CSV = os.path.join(WORKSPACE, "data", "raw", "dimensions_raw_export.csv")
OSF_LOG = os.path.join(WORKSPACE, "lab_projects", "paper1a_osf_screening_log.csv")
CLEAN_CSV = os.path.join(WORKSPACE, "data", "processed", "dimensions_clean_included.csv")
STATS_JSON = os.path.join(WORKSPACE, "lab_management", "paper1a_real_stats.json")
FIG3_PNG = os.path.join(WORKSPACE, "lab_projects", "figures", "figure3_vosviewer_real_network.png")

NON_JOURNAL_RE = re.compile(
    r"proceeding|conference|symposium|workshop|lecture notes|arxiv|ssrn|preprint|"
    r"zenodo|research square|chapter|book|studies in big data|studies in systems|"
    r"advances in economics|advances in social science|smart innovation|"
    r"highlights in business|communications in computer|ifip advances|"
    r"acm international|ieee international|procedia",
    re.I,
)
AI_RE = re.compile(
    r"artificial intelligence|\bAI\b|recommend|algorithm|personaliz|chatbot|conversational agent|generative",
    re.I,
)
IMP_RE = re.compile(r"impuls|unplanned|spontaneous|urge to buy", re.I)
ECOM_RE = re.compile(
    r"e-commerce|ecommerce|online shop|digital retail|electronic commerce|social commerce|"
    r"mobile commerce|live.?stream|livestream|online retail|online store|online consumer|"
    r"online purchase|online buy|shopping",
    re.I,
)
NON_RETAIL_RE = re.compile(
    r"clinical|patient|hospital|psychiatric|mental health|psychotherapy|cancer|diabetes|neurolog|mri|eeg|surgical|nursing",
    re.I,
)

# Curated domain concept dictionary for reproducible co-word network (4 theoretical clusters)
CONCEPT_TERMS = {
    # Cluster 1 (Red): Algorithmic Stimuli & System Architecture
    "artificial intelligence": (1, r"\bartificial intelligence\b|\bAI\b"),
    "recommendation system": (1, r"\brecommend(?:er|ation) system"),
    "personalized recommendation": (1, r"\bpersonaliz(?:ed|ation)\b"),
    "algorithmic curation": (1, r"\balgorithm(?:ic)?\b"),
    "live streaming": (1, r"\blive.?stream(?:ing)?\b"),
    "social commerce": (1, r"\bsocial commerce\b"),
    "chatbot / virtual agent": (1, r"\bchatbot|\bvirtual (?:AI )?streamer|\bconversational agent"),
    "novelty & serendipity": (1, r"\bnovelt|\bserendipit"),
    # Cluster 2 (Green): Cognitive Organism & E-Satisfaction
    "e-satisfaction": (2, r"\be-satisfaction\b|\bcustomer satisfaction\b|\bsatisfaction\b"),
    "trust": (2, r"\btrust\b"),
    "perceived value": (2, r"\bperceived value\b|\butilitarian"),
    "perceived usefulness": (2, r"\bperceived usefulness\b|\bease of use\b"),
    "cognitive fit / fluency": (2, r"\bcognitive\b|\bfluency\b|\binformation processing\b"),
    "S-O-R framework": (2, r"\bs-o-r\b|\bstimulus-organism-response\b"),
    # Cluster 3 (Blue): Affective Organism & Impulsive Response
    "online impulse buying": (3, r"\bonline impulse buying\b|\be-impulse\b"),
    "impulse buying": (3, r"\bimpulse buying\b|\bimpulsive buying\b"),
    "urge to buy impulsively": (3, r"\burge to buy\b"),
    "emotional arousal": (3, r"\barousal\b|\bemotion(?:al)?\b|\bpleasure\b"),
    "flow experience": (3, r"\bflow\b|\bimmersi"),
    "hedonic motivation": (3, r"\bhedonic\b"),
    "scarcity & urgency": (3, r"\bscarcit|\burgency\b|\bfear of missing out\b|\bfomo\b"),
    # Cluster 4 (Yellow): Dark Side, Reactance & Self-Control
    "privacy concerns": (4, r"\bprivacy\b|\bsurveillance\b"),
    "psychological reactance": (4, r"\breactance\b|\bintrusiv|\bskepticism\b"),
    "self-control": (4, r"\bself-control\b|\bself-regulation\b|\bself-regulatory\b"),
    "ego depletion / fatigue": (4, r"\bdepletion\b|\bfatigue\b|\bcognitive load\b"),
    "post-purchase regret": (4, r"\bregret\b|\bdissonance\b|\bproduct return"),
}

REGEX_AUDIT_DICT = [
    ("S-O-R Framing Mentions", r"stimulus-organism-response|s-o-r|sor model|sor framework"),
    ("Regret / Dissonance / Return Mentions", r"post-purchase regret|cognitive dissonance|regret|product return"),
    ("Interaction / Moderated Mediation Mentions", r"interaction effect|multiplicative|moderated mediation|moderating effect"),
    ("Curvilinear / Threshold Mentions", r"inverted-u|inverted u|curvilinear|threshold effect|quadratic|non-linear|nonlinear"),
    ("Privacy / Reactance / Dark-Pattern Mentions", r"privacy|surveillance|reactance|dark pattern"),
    ("Ego Depletion / Cognitive Load Mentions", r"ego depletion|self-regulatory|decision fatigue|cognitive load"),
]


def main():
    with open(RAW_CSV, encoding="utf-8-sig") as f:
        disclaimer = f.readline().strip()
        raw_rows = list(csv.DictReader(f))

    n_raw = len(raw_rows)
    seen_doi = set()
    dup_count = 0
    log_rows = []
    included = []
    counts = Counter()

    for r in raw_rows:
        doi = (r.get("DOI") or "").strip().lower()
        pub_id = (r.get("Publication ID") or "").strip()
        title = (r.get("Title") or "").strip()
        abstract = (r.get("Abstract") or "").strip()
        source = (r.get("Source title/Anthology title") or "").strip()
        yr_str = (r.get("PubYear") or "").strip()
        yr = int(yr_str) if yr_str.isdigit() else 0
        cited = int(r.get("Times cited") or 0) if str(r.get("Times cited") or "").isdigit() else 0

        if doi and doi in seen_doi:
            dup_count += 1
            counts["EXCLUDE_DUPLICATE"] += 1
            log_rows.append([pub_id, doi, yr_str, source, title, cited, "EXCLUDE", "EC4_DUPLICATE", "Duplicate DOI"])
            continue
        if doi:
            seen_doi.add(doi)

        if not (2018 <= yr <= 2026):
            counts["EXCLUDE_IC1_WINDOW"] += 1
            log_rows.append([pub_id, doi, yr_str, source, title, cited, "EXCLUDE", "IC1_OUT_OF_WINDOW", f"Year {yr_str} outside 2018-2026"])
            continue

        if NON_JOURNAL_RE.search(source) or not source:
            counts["EXCLUDE_EC1_NON_JOURNAL"] += 1
            log_rows.append([pub_id, doi, yr_str, source, title, cited, "EXCLUDE", "EC1_NON_JOURNAL", "Conference/book series/preprint or missing venue"])
            continue

        if not abstract:
            counts["EXCLUDE_NO_ABSTRACT"] += 1
            log_rows.append([pub_id, doi, yr_str, source, title, cited, "EXCLUDE", "EC2_NO_ABSTRACT", "Missing abstract for Title/Abstract screening"])
            continue

        if "RETRACTED" in title.upper():
            counts["EXCLUDE_EC1_RETRACTED"] += 1
            log_rows.append([pub_id, doi, yr_str, source, title, cited, "EXCLUDE", "EC1_RETRACTED", "Retracted publication"])
            continue

        txt = f"{title} {abstract}"
        if NON_RETAIL_RE.search(txt):
            counts["EXCLUDE_EC3_NON_RETAIL"] += 1
            log_rows.append([pub_id, doi, yr_str, source, title, cited, "EXCLUDE", "EC3_NON_RETAIL", "Clinical/medical non-retail context"])
            continue

        if not (AI_RE.search(txt) and IMP_RE.search(txt) and ECOM_RE.search(txt)):
            counts["EXCLUDE_EC2_OFF_TOPIC"] += 1
            log_rows.append([pub_id, doi, yr_str, source, title, cited, "EXCLUDE", "EC2_OFF_TOPIC", "Missing concurrent AI/recommender + impulse + digital commerce nexus in T/A"])
            continue

        counts["INCLUDE"] += 1
        log_rows.append([pub_id, doi, yr_str, source, title, cited, "INCLUDE", "INCLUDED_SYNTHESIS", "Meets IC1-IC4 peer-reviewed journal criteria (2018-2026)"])
        included.append(r)

    # Write OSF screening log
    os.makedirs(os.path.dirname(OSF_LOG), exist_ok=True)
    with open(OSF_LOG, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Publication_ID", "DOI", "PubYear", "Source_Title", "Title", "Times_Cited", "Screening_Decision", "Exclusion_Code", "Reason"])
        w.writerows(log_rows)

    # Write clean included CSV
    os.makedirs(os.path.dirname(CLEAN_CSV), exist_ok=True)
    if included:
        with open(CLEAN_CSV, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(included[0].keys()))
            w.writeheader()
            w.writerows(included)

    n_inc = len(included)
    yr_counts = Counter(int(r["PubYear"]) for r in included)
    phases = {
        "phase1_2018_2020": sum(yr_counts[y] for y in (2018, 2019, 2020)),
        "phase2_2021_2023": sum(yr_counts[y] for y in (2021, 2022, 2023)),
        "phase3_2024_2026": sum(yr_counts[y] for y in (2024, 2025, 2026)),
    }
    top_journals = Counter((r.get("Source title/Anthology title") or "").strip() for r in included).most_common(10)
    top_cited = sorted(included, key=lambda x: int(x.get("Times cited") or 0), reverse=True)[:10]

    # Co-occurrence network (full counting, T >= 3)
    term_docs = defaultdict(set)
    term_years = defaultdict(list)
    compiled_terms = {k: (cl, re.compile(pat, re.I)) for k, (cl, pat) in CONCEPT_TERMS.items()}
    for idx, r in enumerate(included):
        txt = f"{r.get('Title', '')} {r.get('Abstract', '')}"
        yr = int(r["PubYear"])
        for term, (cl, rx) in compiled_terms.items():
            if rx.search(txt):
                term_docs[term].add(idx)
                term_years[term].append(yr)

    active_terms = [t for t, docs in term_docs.items() if len(docs) >= 3]
    edge_weights = {}
    tls = Counter()
    for i, t1 in enumerate(active_terms):
        for t2 in active_terms[i + 1 :]:
            w = len(term_docs[t1] & term_docs[t2])
            if w > 0:
                edge_weights[(t1, t2)] = w
                tls[t1] += w
                tls[t2] += w

    cluster_stats = {}
    for cl in (1, 2, 3, 4):
        cl_terms = [t for t in active_terms if CONCEPT_TERMS[t][0] == cl]
        cl_occ = sum(len(term_docs[t]) for t in cl_terms)
        cl_tls = sum(tls[t] for t in cl_terms)
        all_yrs = [y for t in cl_terms for y in term_years[t]]
        cl_apy = round(sum(all_yrs) / len(all_yrs), 2) if all_yrs else 0.0
        top_t = sorted(cl_terms, key=lambda t: len(term_docs[t]), reverse=True)[:4]
        cluster_stats[str(cl)] = {
            "terms_count": len(cl_terms),
            "occurrences": cl_occ,
            "tls": cl_tls,
            "apy": cl_apy,
            "top_terms": [
                {"term": t, "occ": len(term_docs[t]), "tls": tls[t], "apy": round(sum(term_years[t]) / len(term_years[t]), 2)}
                for t in top_t
            ],
        }

    # Draw real co-occurrence network PNG (Figure 3)
    os.makedirs(os.path.dirname(FIG3_PNG), exist_ok=True)
    fig, ax = plt.subplots(figsize=(12, 7.2), dpi=220)
    ax.set_facecolor("#fafafa")
    cluster_colors = {1: "#e11d48", 2: "#16a34a", 3: "#2563eb", 4: "#d97706"}
    cluster_centers = {1: (-0.65, 0.35), 2: (0.05, 0.55), 3: (0.65, -0.15), 4: (-0.35, -0.55)}
    pos = {}
    for cl in (1, 2, 3, 4):
        cl_terms = sorted([t for t in active_terms if CONCEPT_TERMS[t][0] == cl], key=lambda t: len(term_docs[t]), reverse=True)
        cx, cy = cluster_centers[cl]
        for k, t in enumerate(cl_terms):
            ang = (2 * math.pi * k) / max(len(cl_terms), 1)
            rad = 0.08 if k == 0 else 0.24 + 0.04 * (k % 2)
            pos[t] = (cx + rad * math.cos(ang), cy + rad * math.sin(ang))

    max_w = max(edge_weights.values()) if edge_weights else 1
    for (t1, t2), w in edge_weights.items():
        if w >= 2:
            x1, y1 = pos[t1]
            x2, y2 = pos[t2]
            ax.plot([x1, x2], [y1, y2], color="#94a3b8", alpha=min(0.65, 0.12 + 0.5 * (w / max_w)), linewidth=0.5 + 2.2 * (w / max_w), zorder=1)

    for t in active_terms:
        x, y = pos[t]
        cl = CONCEPT_TERMS[t][0]
        occ = len(term_docs[t])
        sz = 140 + occ * 18
        ax.scatter([x], [y], s=sz, color=cluster_colors[cl], edgecolors="#ffffff", linewidths=1.8, alpha=0.92, zorder=3)
        ax.text(x, y + 0.045, f"{t} ({occ})", fontsize=7.8, fontweight="bold", ha="center", va="bottom", color="#0f172a", zorder=4,
                bbox=dict(boxstyle="round,pad=0.18", facecolor="#ffffff", edgecolor="none", alpha=0.78))

    legend_handles = [
        mpatches.Patch(color="#e11d48", label=f"Cluster 1: Algorithmic Stimuli (APY {cluster_stats['1']['apy']})"),
        mpatches.Patch(color="#16a34a", label=f"Cluster 2: Cognitive Organism & ESAT (APY {cluster_stats['2']['apy']})"),
        mpatches.Patch(color="#2563eb", label=f"Cluster 3: Affective Organism & Impulse (APY {cluster_stats['3']['apy']})"),
        mpatches.Patch(color="#d97706", label=f"Cluster 4: Dark Side, Privacy & Depletion (APY {cluster_stats['4']['apy']})"),
    ]
    ax.legend(handles=legend_handles, loc="lower center", bbox_to_anchor=(0.5, -0.11), ncol=2, frameon=True, fontsize=8.5)
    ax.set_title(f"Co-Occurrence Network Map of Included Dimensions Corpus (N = {n_inc}, T >= 3, Full Counting)", fontsize=11.5, fontweight="bold", pad=12, color="#0f172a")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_edgecolor("#cbd5e1")
    plt.tight_layout()
    plt.savefig(FIG3_PNG, dpi=220, bbox_inches="tight")
    plt.close(fig)

    # Regex lexical salience audit
    regex_results = []
    for label, pat in REGEX_AUDIT_DICT:
        rx = re.compile(pat, re.I)
        n_match = sum(1 for r in included if rx.search(f"{r.get('Title', '')} {r.get('Abstract', '')}"))
        regex_results.append({
            "category": label,
            "pattern": pat,
            "count": n_match,
            "pct": round((n_match / n_inc) * 100, 2) if n_inc else 0.0,
        })

    stats = {
        "export_date": "2026-11-28",
        "source_file": "Dimensions-Publication-2026-11-28_08-12-01.csv",
        "prisma": {
            "raw_identified": n_raw,
            "duplicates_removed": dup_count,
            "unique_records": n_raw - dup_count,
            "excluded_ic1_window": counts["EXCLUDE_IC1_WINDOW"],
            "excluded_ec1_non_journal": counts["EXCLUDE_EC1_NON_JOURNAL"],
            "excluded_no_abstract_retracted": counts["EXCLUDE_NO_ABSTRACT"] + counts["EXCLUDE_EC1_RETRACTED"],
            "no_abstract": counts["EXCLUDE_NO_ABSTRACT"],
            "retracted": counts["EXCLUDE_EC1_RETRACTED"],
            "eligible_ta_screened": n_raw - dup_count - counts["EXCLUDE_IC1_WINDOW"] - counts["EXCLUDE_EC1_NON_JOURNAL"] - counts["EXCLUDE_NO_ABSTRACT"] - counts["EXCLUDE_EC1_RETRACTED"],
            "excluded_ec3_non_retail": counts["EXCLUDE_EC3_NON_RETAIL"],
            "excluded_ec2_off_topic": counts["EXCLUDE_EC2_OFF_TOPIC"],
            "final_included": n_inc,
        },
        "yearly_counts": {str(y): yr_counts[y] for y in range(2018, 2027)},
        "phases": phases,
        "top_journals": [{"journal": j, "count": c, "pct": round(c / n_inc * 100, 1)} for j, c in top_journals],
        "top_cited": [
            {
                "authors": (r.get("Authors") or "").split(";")[0].split(",")[0].strip() + (" et al." if ";" in (r.get("Authors") or "") else ""),
                "year": r.get("PubYear"),
                "journal": r.get("Source title/Anthology title"),
                "title": r.get("Title"),
                "doi": r.get("DOI"),
                "citations": int(r.get("Times cited") or 0),
                "volume": r.get("Volume"),
                "issue": r.get("Issue"),
                "pagination": r.get("Pagination"),
            }
            for r in top_cited
        ],
        "vosviewer": {
            "active_terms": len(active_terms),
            "edges": len(edge_weights),
            "clusters": cluster_stats,
        },
        "regex_audit": regex_results,
    }
    with open(STATS_JSON, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    print(json.dumps(stats, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
