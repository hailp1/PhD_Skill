#!/usr/bin/env python3
"""
run_full_slr_from_dimensions.py
===============================
End-to-end reproducible PRISMA 2020, Two-Tier Corpus (Broad Context N=1,152 + Core AI-Impulse),
Inductive Corpus-Extracted Co-Word Network (VOSviewer-compatible export),
Theory-Driven Concept Map (Appendix B), and Construct-Separated Lexical Audit
operating strictly on:
  data/raw/dimensions_raw_export.csv (2,500 records exported 2026-11-28)
"""

import csv
import hashlib
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
ORIG_EXPORT = os.path.join(WORKSPACE, "Dimensions-Publication-2026-11-28_08-40-19.csv")
OSF_LOG = os.path.join(WORKSPACE, "lab_projects", "paper1a_osf_screening_log.csv")
CLEAN_CSV = os.path.join(WORKSPACE, "data", "processed", "dimensions_clean_included.csv")
CORE_CSV = os.path.join(WORKSPACE, "data", "processed", "dimensions_core_ai_impulse.csv")
VOS_MAP = os.path.join(WORKSPACE, "data", "processed", "vosviewer_core_map.txt")
VOS_NET = os.path.join(WORKSPACE, "data", "processed", "vosviewer_core_network.txt")
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
AI_STRICT_RE = re.compile(
    r"\b(artificial intelligence|ai|recommender|recommendation|collaborative filtering|"
    r"deep learning|machine learning|algorithmic|personaliz\w+|generative ai|llm|chatbot|conversational agent)\b",
    re.I,
)
IMP_STRICT_RE = re.compile(
    r"\b(impulse buying|impulsive buying|impulse purchas\w*|spontaneous purchas\w*|unplanned purchas\w*|urge to buy)\b",
    re.I,
)
GENAI_RE = re.compile(r"\b(generative ai|genai|chatgpt|gpt-4|large language model|llm)\b", re.I)

IMP_BROAD_RE = re.compile(
    r"impuls|unplanned|spontaneous|urge to buy|compulsive|habit|buying behavior|purchase intention|purchasing behavior|consumer behavior|consumer decision",
    re.I,
)
ECOM_RE = re.compile(
    r"consumer|customer|shopper|buyer|purchas|buying|e-commerce|ecommerce|retail|shopping|social commerce|mobile commerce|live.?stream|livestream|marketplace|marketing|brand|digital platform|habit",
    re.I,
)
NON_RETAIL_RE = re.compile(
    r"cancer|tumor|surgical|chemotherapy|radiology|pathology|icu|sepsis|cardiac|stroke|epilepsy|alzheimer",
    re.I,
)

# Appendix B: Theory-Driven Concept Map (26 curated concepts)
CONCEPT_TERMS = {
    "artificial intelligence": (1, r"\bartificial intelligence\b|\bAI\b"),
    "recommendation system": (1, r"\brecommend(?:er|ation) system"),
    "personalized recommendation": (1, r"\bpersonaliz(?:ed|ation)\b"),
    "algorithmic curation": (1, r"\balgorithm(?:ic)?\b"),
    "live streaming": (1, r"\blive.?stream(?:ing)?\b"),
    "social commerce": (1, r"\bsocial commerce\b"),
    "chatbot / virtual agent": (1, r"\bchatbot|\bvirtual (?:AI )?streamer|\bconversational agent"),
    "novelty & serendipity": (1, r"\bnovelt|\bserendipit"),
    "e-satisfaction": (2, r"\be-satisfaction\b|\bcustomer satisfaction\b|\bsatisfaction\b"),
    "trust": (2, r"\btrust\b"),
    "perceived value": (2, r"\bperceived value\b|\butilitarian"),
    "perceived usefulness": (2, r"\bperceived usefulness\b|\bease of use\b"),
    "cognitive fit / fluency": (2, r"\bcognitive\b|\bfluency\b|\binformation processing\b"),
    "S-O-R framework": (2, r"\bs-o-r\b|\bstimulus-organism-response\b"),
    "online impulse buying": (3, r"\bonline impulse buying\b|\be-impulse\b"),
    "impulse buying": (3, r"\bimpulse buying\b|\bimpulsive buying\b"),
    "urge to buy impulsively": (3, r"\burge to buy\b"),
    "emotional arousal": (3, r"\barousal\b|\bemotion(?:al)?\b|\bpleasure\b"),
    "flow experience": (3, r"\bflow\b|\bimmersi"),
    "hedonic motivation": (3, r"\bhedonic\b"),
    "scarcity & urgency": (3, r"\bscarcit|\burgency\b|\bfear of missing out\b|\bfomo\b"),
    "privacy concerns": (4, r"\bprivacy\b|\bsurveillance\b"),
    "psychological reactance": (4, r"\breactance\b|\bintrusiv|\bskepticism\b"),
    "self-control": (4, r"\bself-control\b|\bself-regulation\b|\bself-regulatory\b"),
    "ego depletion / fatigue": (4, r"\bdepletion\b|\bfatigue\b|\bcognitive load\b"),
    "post-purchase regret": (4, r"\bregret\b|\bdissonance\b|\bproduct return"),
}

# Construct-separated lexical audit (no conflation of generic "moderating effect" or "privacy")
REGEX_AUDIT_DICT = [
    ("S-O-R Theoretical Framing", r"stimulus-organism-response|s-o-r|sor model|sor framework"),
    ("Privacy / Surveillance Mentions", r"\bprivacy\b|\bsurveillance\b"),
    ("Psychological Reactance / Manipulative Intent", r"\breactance\b|\bmanipulative intent\b|\bintrusiveness\b|\bcreepiness\b"),
    ("Curvilinear / Inverted-U / Threshold Effects", r"inverted-u|inverted u|curvilinear|threshold effect|quadratic|non-linear|nonlinear"),
    ("Cognitive-Affective Multiplicative Interaction", r"multiplicative|cognitive.?affective interaction|synergistic interaction"),
    ("Ego Depletion / Self-Regulatory Fatigue / Cognitive Load", r"ego depletion|rational depletion|self-regulatory|decision fatigue|cognitive load"),
    ("Post-Purchase Regret / Dissonance / Returns", r"post-purchase regret|cognitive dissonance|post-purchase dissonance|\bregret\b|product return"),
    ("Generative AI / LLM / Conversational Agents", r"\bgenerative ai\b|\bgenai\b|\bchatgpt\b|\blarge language model\b|\bllm\b|conversational agent"),
]

STOPWORDS = set(
    "the and of in to on for with that this by as is are was were from an a at be or it its their they we our "
    "using based study research paper findings results data analysis model effects effect impact role influence "
    "relationship between among through how toward towards via into during across within such than also can may "
    "will more most which who whom whose these those one two three four five first second third new high low "
    "different significant significantly positive positively negative negatively examine examines examined explore "
    "explores explored investigate investigates investigated propose proposes proposed demonstrate demonstrates "
    "suggest suggests reveal reveals provide provides contribute contributes understanding insights implications "
    "abstract purpose design methodology approach originality value practical social limitations".split()
)

BOILERPLATE_GRAMS = {
    "design methodology", "methodology approach", "design methodology approach",
    "practical implications", "originality value", "research limitations",
    "limitations implications", "social implications", "structural equation",
    "equation modeling", "structural equation modeling", "structural equation modelling",
    "equation modelling", "squares structural equation", "modeling pls-sem",
    "equation modeling pls-sem", "partial least", "least squares",
    "partial least squares", "least squares structural", "squares structural",
    "findings suggest", "results indicate", "results show", "present study",
    "current study", "future research", "empirical study", "quantitative study",
    "survey data", "questionnaire survey", "does not", "shape consumer",
    "driving impulse", "fear of missing", "missing out", "out fomo",
    "stimulus organism", "organism response", "systematic literature",
}

CANONICAL_MAP = {
    "missing out fomo": "fear of missing out (fomo)",
    "stimulus organism response": "s-o-r framework",
    "systematic literature review": "systematic review",
    "literature review": "systematic review",
    "online survey": "survey methodology",
    "ai recommendations": "ai recommendation",
    "algorithmic recommendations": "ai recommendation",
    "impulsive purchases": "impulse purchase",
    "impulsive buying": "impulse buying",
    "impulse buying behavior": "impulse buying",
    "impulsive buying behavior": "impulse buying",
    "impulse buying behaviour": "impulse buying",
    "impulsive buying behaviour": "impulse buying",
    "buying behavior": "consumer buying behavior",
    "buying behaviour": "consumer buying behavior",
    "purchasing behavior": "consumer buying behavior",
    "purchasing behaviour": "consumer buying behavior",
    "purchase behavior": "consumer buying behavior",
    "purchase behaviour": "consumer buying behavior",
    "artificial intelligence ai": "artificial intelligence",
    "intelligence ai": "artificial intelligence",
    "e-commerce platforms": "e-commerce",
    "e-commerce platform": "e-commerce",
    "online shopping": "online shopping",
    "personalized recommendations": "personalized recommendation",
    "personalized product": "personalized recommendation",
    "recommendation systems": "recommendation system",
    "recommender systems": "recommendation system",
    "recommender system": "recommendation system",
    "recommendation algorithms": "recommendation algorithm",
    "live-streaming": "live streaming",
    "livestream shopping": "live streaming",
    "live streaming commerce": "live streaming",
    "live streaming e-commerce": "live streaming",
    "short video": "short-video platforms",
    "short-video": "short-video platforms",
    "impulse purchases": "impulse purchase",
    "impulsive purchasing": "impulse purchase",
    "impulse purchasing": "impulse purchase",
    "urge to buy": "urge to buy impulsively",
    "buy impulsively": "urge to buy impulsively",
    "consumer behavior": "consumer behavior",
    "consumer behaviour": "consumer behavior",
    "perceived enjoyment": "perceived enjoyment",
    "emotional arousal": "emotional arousal",
    "social presence": "social presence",
    "social commerce": "social commerce",
    "social media": "social media",
    "social proof": "social proof",
    "consumer trust": "trust",
    "dark patterns": "dark patterns",
    "dark pattern": "dark patterns",
    "purchase intention": "purchase intention",
    "buying intention": "purchase intention",
    "impulsive buying intention": "impulse buying",
    "impulse buying intention": "impulse buying",
    "online impulse": "online impulse buying",
}


def extract_inductive_cooccurrence(docs, min_df=4):
    """Inductively extract frequent 2- and 3-grams from Title+Abstract, normalize variants, and cluster by greedy modularity."""
    term_docs = defaultdict(set)
    term_years = defaultdict(list)

    for idx, r in enumerate(docs):
        txt = ((r.get("Title") or "") + " " + (r.get("Abstract") or "")).lower()
        txt = re.sub(r"[^a-z0-9\-\s]", " ", txt)
        tokens = [t for t in txt.split() if len(t) > 1]
        yr = int(r["PubYear"])
        doc_terms = set()
        for n in (2, 3):
            for i in range(len(tokens) - n + 1):
                gram = tokens[i : i + n]
                if gram[0] in STOPWORDS or gram[-1] in STOPWORDS:
                    continue
                if any(w.isdigit() for w in gram):
                    continue
                raw = " ".join(gram)
                if raw in BOILERPLATE_GRAMS:
                    continue
                canon = CANONICAL_MAP.get(raw, raw)
                if canon in BOILERPLATE_GRAMS:
                    continue
                doc_terms.add(canon)
        for t in doc_terms:
            term_docs[t].add(idx)
            term_years[t].append(yr)

    active = sorted([t for t, d in term_docs.items() if len(d) >= min_df], key=lambda t: len(term_docs[t]), reverse=True)
    # Build co-occurrence edges
    edges = {}
    tls = Counter()
    adj = defaultdict(dict)
    total_w = 0
    for i, t1 in enumerate(active):
        for t2 in active[i + 1 :]:
            w = len(term_docs[t1] & term_docs[t2])
            if w > 0:
                edges[(t1, t2)] = w
                tls[t1] += w
                tls[t2] += w
                adj[t1][t2] = w
                adj[t2][t1] = w
                total_w += w

    # Greedy modularity clustering (pure Python)
    comm = {t: i for i, t in enumerate(active)}
    m2 = 2.0 * max(total_w, 1)
    deg = {t: sum(adj[t].values()) for t in active}
    improved = True
    while improved:
        improved = False
        for t in active:
            cur_c = comm[t]
            c_weights = defaultdict(float)
            for nb, w in adj[t].items():
                c_weights[comm[nb]] += w
            tot_c = defaultdict(float)
            for node, c in comm.items():
                tot_c[c] += deg[node]
            best_c = cur_c
            best_gain = 0.0
            k_i = deg[t]
            for cand_c, k_in in c_weights.items():
                if cand_c == cur_c:
                    continue
                gain = k_in - (tot_c[cand_c] * k_i) / m2
                cur_in = c_weights.get(cur_c, 0.0)
                cur_tot = tot_c[cur_c] - k_i
                cur_gain = cur_in - (cur_tot * k_i) / m2
                if gain - cur_gain > 1e-6 and (gain - cur_gain) > best_gain:
                    best_gain = gain - cur_gain
                    best_c = cand_c
            if best_c != cur_c:
                comm[t] = best_c
                improved = True

    # Renumber communities 1..K ordered by total occurrences
    comm_groups = defaultdict(list)
    for t, c in comm.items():
        comm_groups[c].append(t)
    ordered_groups = sorted(comm_groups.values(), key=lambda g: sum(len(term_docs[t]) for t in g), reverse=True)

    node_cluster = {}
    cluster_stats = {}
    for cid, grp in enumerate(ordered_groups, start=1):
        for t in grp:
            node_cluster[t] = cid
        all_yrs = [y for t in grp for y in term_years[t]]
        apy = round(sum(all_yrs) / len(all_yrs), 2) if all_yrs else 0.0
        top_t = sorted(grp, key=lambda t: len(term_docs[t]), reverse=True)[:5]
        cluster_stats[str(cid)] = {
            "terms_count": len(grp),
            "occurrences": sum(len(term_docs[t]) for t in grp),
            "tls": sum(tls[t] for t in grp),
            "apy": apy,
            "top_terms": [
                {"term": t, "occ": len(term_docs[t]), "tls": tls[t], "apy": round(sum(term_years[t]) / len(term_years[t]), 2)}
                for t in top_t
            ],
        }

    # Export VOSviewer-compatible map & network files
    id_map = {t: i + 1 for i, t in enumerate(active)}
    with open(VOS_MAP, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["id", "label", "cluster", "weight<Occurrences>", "weight<Total link strength>", "score<Avg. pub. year>"])
        for t in active:
            apy_t = round(sum(term_years[t]) / len(term_years[t]), 2)
            w.writerow([id_map[t], t, node_cluster[t], len(term_docs[t]), tls[t], apy_t])
    with open(VOS_NET, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        for (t1, t2), weight in edges.items():
            w.writerow([id_map[t1], id_map[t2], weight])

    return active, term_docs, term_years, edges, tls, node_cluster, cluster_stats


def main():
    sha256_target = ORIG_EXPORT if os.path.exists(ORIG_EXPORT) else RAW_CSV
    sha256 = hashlib.sha256(open(sha256_target, "rb").read()).hexdigest()

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
            log_rows.append([pub_id, doi, yr_str, source, title, cited, "EXCLUDE", "EC3_NON_RETAIL", "Clinical/medical domain unrelated to consumer behavior"])
            continue

        if not (IMP_BROAD_RE.search(txt) and ECOM_RE.search(txt)):
            counts["EXCLUDE_EC2_OFF_TOPIC"] += 1
            log_rows.append([pub_id, doi, yr_str, source, title, cited, "EXCLUDE", "EC2_OFF_TOPIC", "Missing impulse/habit/buying + consumer/commerce nexus in T/A"])
            continue

        is_core = bool(AI_STRICT_RE.search(txt) and IMP_STRICT_RE.search(txt))
        tier = "CORE_AI_IMPULSE" if is_core else "BROAD_CONTEXT"
        counts["INCLUDE"] += 1
        log_rows.append([pub_id, doi, yr_str, source, title, cited, "INCLUDE", tier, "Meets Title/Abstract screening criteria (2018-2026)"])
        included.append(r)

    os.makedirs(os.path.dirname(OSF_LOG), exist_ok=True)
    with open(OSF_LOG, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Publication_ID", "DOI", "PubYear", "Source_Title", "Title", "Times_Cited", "Screening_Decision", "Corpus_Tier_Or_Exclusion", "Reason"])
        w.writerows(log_rows)

    os.makedirs(os.path.dirname(CLEAN_CSV), exist_ok=True)
    if included:
        with open(CLEAN_CSV, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(included[0].keys()))
            w.writeheader()
            w.writerows(included)

    core_docs = [r for r in included if AI_STRICT_RE.search(f"{r.get('Title','')} {r.get('Abstract','')}") and IMP_STRICT_RE.search(f"{r.get('Title','')} {r.get('Abstract','')}")]
    if core_docs:
        with open(CORE_CSV, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(core_docs[0].keys()))
            w.writeheader()
            w.writerows(core_docs)

    n_inc = len(included)
    n_core = len(core_docs)
    n_ta_ai = sum(1 for r in included if AI_STRICT_RE.search(f"{r.get('Title','')} {r.get('Abstract','')}"))
    n_ta_imp = sum(1 for r in included if IMP_STRICT_RE.search(f"{r.get('Title','')} {r.get('Abstract','')}"))
    n_ta_genai = sum(1 for r in included if GENAI_RE.search(f"{r.get('Title','')} {r.get('Abstract','')}"))

    yr_counts = Counter(int(r["PubYear"]) for r in included)
    core_yr_counts = Counter(int(r["PubYear"]) for r in core_docs)
    phases = {
        "phase1_2018_2020": sum(yr_counts[y] for y in (2018, 2019, 2020)),
        "phase2_2021_2023": sum(yr_counts[y] for y in (2021, 2022, 2023)),
        "phase3_2024_2026": sum(yr_counts[y] for y in (2024, 2025, 2026)),
    }
    core_phases = {
        "phase1_2018_2020": sum(core_yr_counts[y] for y in (2018, 2019, 2020)),
        "phase2_2021_2023": sum(core_yr_counts[y] for y in (2021, 2022, 2023)),
        "phase3_2024_2026": sum(core_yr_counts[y] for y in (2024, 2025, 2026)),
    }

    top_journals = Counter((r.get("Source title/Anthology title") or "").strip() for r in included).most_common(10)
    core_top_journals = Counter((r.get("Source title/Anthology title") or "").strip() for r in core_docs).most_common(10)
    country_counts = Counter()
    for r in included:
        raw_c = (r.get("Authors Affiliations - Country of Research organization") or "").strip()
        if raw_c:
            for c_name in set(x.strip() for x in raw_c.split(";") if x.strip()):
                country_counts[c_name] += 1
    top_countries = country_counts.most_common(12)

    top_cited_core = sorted(core_docs, key=lambda x: int(x.get("Times cited") or 0), reverse=True)[:10]
    top_cited_broad = sorted(included, key=lambda x: int(x.get("Times cited") or 0), reverse=True)[:10]

    # 1. Inductive corpus-extracted co-occurrence network on Core Corpus (min_df=5)
    active_ind, ind_docs, ind_yrs, ind_edges, ind_tls, ind_clust, ind_cstats = extract_inductive_cooccurrence(core_docs, min_df=5)

    # 2. Theory-Driven Concept Map (26 curated concepts on Broad N=1,152 for Appendix B)
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

    theory_cstats = {}
    for cl in (1, 2, 3, 4):
        cl_terms = [t for t in active_terms if CONCEPT_TERMS[t][0] == cl]
        all_yrs = [y for t in cl_terms for y in term_years[t]]
        theory_cstats[str(cl)] = {
            "terms_count": len(cl_terms),
            "occurrences": sum(len(term_docs[t]) for t in cl_terms),
            "tls": sum(tls[t] for t in cl_terms),
            "apy": round(sum(all_yrs) / len(all_yrs), 2) if all_yrs else 0.0,
            "top_terms": [
                {"term": t, "occ": len(term_docs[t]), "tls": tls[t], "apy": round(sum(term_years[t]) / len(term_years[t]), 2)}
                for t in sorted(cl_terms, key=lambda t: len(term_docs[t]), reverse=True)[:4]
            ],
        }

    # Draw Figure 3: Inductive Core Corpus Co-Occurrence Network
    os.makedirs(os.path.dirname(FIG3_PNG), exist_ok=True)
    fig, ax = plt.subplots(figsize=(12, 7.2), dpi=220)
    ax.set_facecolor("#fafafa")
    palette = {1: "#e11d48", 2: "#16a34a", 3: "#2563eb", 4: "#d97706", 5: "#7c3aed", 6: "#0891b2"}
    n_cl = len(ind_cstats)
    centers = {}
    for cid in range(1, n_cl + 1):
        ang = 2 * math.pi * (cid - 1) / max(n_cl, 1)
        centers[cid] = (0.58 * math.cos(ang), 0.48 * math.sin(ang))

    pos = {}
    for cid in range(1, n_cl + 1):
        cl_terms = sorted([t for t in active_ind if ind_clust[t] == cid], key=lambda t: len(ind_docs[t]), reverse=True)
        cx, cy = centers[cid]
        for k, t in enumerate(cl_terms):
            ang = (2 * math.pi * k) / max(len(cl_terms), 1)
            rad = 0.06 if k == 0 else 0.22 + 0.05 * (k % 2)
            pos[t] = (cx + rad * math.cos(ang), cy + rad * math.sin(ang))

    max_w = max(ind_edges.values()) if ind_edges else 1
    for (t1, t2), w in ind_edges.items():
        if w >= 2:
            x1, y1 = pos[t1]
            x2, y2 = pos[t2]
            ax.plot([x1, x2], [y1, y2], color="#94a3b8", alpha=min(0.65, 0.14 + 0.5 * (w / max_w)), linewidth=0.6 + 2.2 * (w / max_w), zorder=1)

    for t in active_ind:
        x, y = pos[t]
        cid = ind_clust[t]
        occ = len(ind_docs[t])
        sz = 160 + occ * 22
        ax.scatter([x], [y], s=sz, color=palette.get(cid, "#475569"), edgecolors="#ffffff", linewidths=1.8, alpha=0.92, zorder=3)
        ax.text(x, y + 0.04, f"{t} ({occ})", fontsize=7.6, fontweight="bold", ha="center", va="bottom", color="#0f172a", zorder=4,
                bbox=dict(boxstyle="round,pad=0.18", facecolor="#ffffff", edgecolor="none", alpha=0.80))

    legend_handles = [
        mpatches.Patch(color=palette.get(int(cid), "#475569"), label=f"Cluster {cid} ({len(ind_cstats[cid]['top_terms'])} top terms, APY {ind_cstats[cid]['apy']})")
        for cid in sorted(ind_cstats.keys(), key=int)
    ]
    ax.legend(handles=legend_handles, loc="lower center", bbox_to_anchor=(0.5, -0.11), ncol=2, frameon=True, fontsize=8.5)
    ax.set_title(f"Inductive Co-Occurrence Network of Core AI-Impulse Corpus (n = {n_core}, DF >= 5, Modularity Clustering)", fontsize=11.5, fontweight="bold", pad=12, color="#0f172a")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_edgecolor("#cbd5e1")
    plt.tight_layout()
    plt.savefig(FIG3_PNG, dpi=220, bbox_inches="tight")
    plt.close(fig)

    # Construct-separated Regex Lexical Audit (both Core and Broad)
    regex_results = []
    for label, pat in REGEX_AUDIT_DICT:
        rx = re.compile(pat, re.I)
        n_broad = sum(1 for r in included if rx.search(f"{r.get('Title', '')} {r.get('Abstract', '')}"))
        n_c = sum(1 for r in core_docs if rx.search(f"{r.get('Title', '')} {r.get('Abstract', '')}"))
        regex_results.append({
            "category": label,
            "pattern": pat,
            "broad_count": n_broad,
            "broad_pct": round((n_broad / n_inc) * 100, 2) if n_inc else 0.0,
            "core_count": n_c,
            "core_pct": round((n_c / n_core) * 100, 2) if n_core else 0.0,
        })

    def fmt_authors(raw_auth):
        parts = [a.strip() for a in (raw_auth or "").split(";") if a.strip()]
        surnames = [p.split(",")[0].strip() for p in parts]
        if len(surnames) == 1:
            return surnames[0]
        if len(surnames) == 2:
            return f"{surnames[0]} & {surnames[1]}"
        return f"{surnames[0]} et al."

    stats = {
        "export_date": "2026-11-28",
        "source_file": "Dimensions-Publication-2026-11-28_08-40-19.csv",
        "sha256": sha256,
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
            "final_included_broad": n_inc,
            "final_included_core": n_core,
            "ta_ai_only": n_ta_ai,
            "ta_impulse_only": n_ta_imp,
            "ta_genai_llm": n_ta_genai,
        },
        "yearly_counts": {str(y): yr_counts[y] for y in range(2018, 2027)},
        "core_yearly_counts": {str(y): core_yr_counts[y] for y in range(2018, 2027)},
        "phases": phases,
        "core_phases": core_phases,
        "top_journals": [{"journal": j, "count": c, "pct": round(c / n_inc * 100, 1)} for j, c in top_journals],
        "core_top_journals": [{"journal": j, "count": c, "pct": round(c / n_core * 100, 1)} for j, c in core_top_journals],
        "total_countries": len(country_counts),
        "top_countries": [{"country": cn, "count": c, "pct": round(c / n_inc * 100, 1)} for cn, c in top_countries],
        "top_cited_core": [
            {
                "authors": fmt_authors(r.get("Authors")),
                "year": r.get("PubYear"),
                "journal": r.get("Source title/Anthology title"),
                "title": r.get("Title"),
                "doi": r.get("DOI"),
                "citations": int(r.get("Times cited") or 0),
            }
            for r in top_cited_core
        ],
        "top_cited_broad": [
            {
                "authors": fmt_authors(r.get("Authors")),
                "year": r.get("PubYear"),
                "journal": r.get("Source title/Anthology title"),
                "title": r.get("Title"),
                "doi": r.get("DOI"),
                "citations": int(r.get("Times cited") or 0),
            }
            for r in top_cited_broad
        ],
        "inductive_network": {
            "corpus_n": n_core,
            "min_df": 5,
            "active_terms": len(active_ind),
            "edges": len(ind_edges),
            "clusters": ind_cstats,
        },
        "theory_concept_map": {
            "active_terms": len(active_terms),
            "edges": len(edge_weights),
            "clusters": theory_cstats,
        },
        "regex_audit": regex_results,
    }
    with open(STATS_JSON, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    print(json.dumps({
        "sha256": sha256,
        "broad": n_inc,
        "core": n_core,
        "ta_genai": n_ta_genai,
        "inductive_terms": len(active_ind),
        "inductive_edges": len(ind_edges),
        "inductive_clusters": ind_cstats,
        "regex_audit": regex_results,
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
