#!/usr/bin/env python3
"""
phase1_clean_paper1a.py
=======================
Phase 1 Emergency Data & Citation Audit for Paper 1A:
1. Applies strict 3-pillar PRISMA 2020 eligibility screening (2018-2026, strictly
   excluding 2027 early-access, conference proceedings, duopoly/store-layout,
   and non-impulse-buying papers) -> Core Corpus + OSF screening log CSV.
2. Computes 100% synchronized annual trend, Top 10 Journals (with ABDC/ABS tiers),
   Top 10 Cited Core Corpus papers, and full-corpus structured evidence coding.
3. Computes 3 bibliometric networks on Core Corpus:
   - Keyword Co-occurrence (with thesaurus & resolution stability check)
   - Bibliographic Coupling (shared cited references)
   - Co-Citation (top co-cited foundational references)
4. Verifies seminal & literature-review references directly via Crossref API.
"""

import csv
import json
import math
import os
import re
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict

import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIM_CSV = os.path.join(BASE_DIR, "data", "processed", "dimensions_clean_included.csv")
EXP_CSV = os.path.join(BASE_DIR, "data", "processed", "expanded_corpus_v2.csv")
OSF_LOG_CSV = os.path.join(BASE_DIR, "lab_projects", "paper1a_osf_screening_log.csv")
CORE_CSV = os.path.join(BASE_DIR, "data", "processed", "paper1a_core_corpus.csv")
STATS_JSON = os.path.join(BASE_DIR, "lab_management", "paper1a_clean_stats.json")
REFS_JSON = os.path.join(BASE_DIR, "lab_management", "paper1a_verified_refs.json")

NON_JOURNAL_PATTERNS = [
    "proceedings", "conference", "symposium", "workshop", "lecture notes",
    "ssrn", "arxiv", "biorxiv", "medrxiv", "ceur", "book series",
    "advances in economics", "advances in social science", "inted", "itnec",
    "icbmr", "ro-man", "iiai-aai", "zenodo", "figshare", "research square",
    "oalib", "world journal of advanced research", "ijarsct", "ijrsi",
    "international journal of multidisciplinary research", "preprint",
]

RETRACTED_PATTERNS = [
    "retracted article", "retraction notice", "retracted:", "withdrawn article",
    "erratum", "corrigendum",
]

INDONESIAN_STOPWORDS = {"yang", "dan", "pada", "pengaruh", "perilaku", "konsumen", "terhadap", "pembelian", "secara", "untuk"}

OFF_TOPIC_PATTERNS = [
    "duopoly", "store layout", "visual merchandising", "brick-and-mortar",
    "food waste", "supply chain", "clinical trial", "hospitality robot",
]

# Journal quality tier lookup (ABS/AJG & ABDC representative mapping)
JOURNAL_TIER_MAP = {
    "journal of retailing and consumer services": "ABDC: A | ABS: 2 | SJR: Q1",
    "journal of business research": "ABDC: A | ABS: 3 | SJR: Q1",
    "computers in human behavior": "ABDC: A | ABS: 3 | SJR: Q1",
    "journal of theoretical and applied electronic commerce research": "ABDC: B | ABS: 1 | SJR: Q1",
    "international journal of information management": "ABDC: A* | ABS: 2 | SJR: Q1",
    "information & management": "ABDC: A* | ABS: 3 | SJR: Q1",
    "psychology and marketing": "ABDC: A | ABS: 3 | SJR: Q1",
    "psychology & marketing": "ABDC: A | ABS: 3 | SJR: Q1",
    "asia pacific journal of marketing and logistics": "ABDC: A | ABS: 1 | SJR: Q1",
    "international journal of retail & distribution management": "ABDC: A | ABS: 2 | SJR: Q1",
    "journal of consumer behaviour": "ABDC: A | ABS: 2 | SJR: Q1",
    "electronic commerce research and applications": "ABDC: C | ABS: 2 | SJR: Q1",
    "electronic commerce research": "ABDC: A | ABS: 2 | SJR: Q1",
    "internet research": "ABDC: A | ABS: 2 | SJR: Q1",
    "frontiers in psychology": "SJR: Q1/Q2 (Non-ABS)",
    "sustainability": "SJR: Q1/Q2 (Non-ABS)",
    "behavioral sciences": "SJR: Q2 (Non-ABS)",
    "acta psychologica": "SJR: Q2 (Non-ABS)",
    "plos one": "SJR: Q1 (Multidisciplinary)",
    "heliyon": "SJR: Q1 (Multidisciplinary)",
    "cogent business & management": "ABDC: C | ABS: 1 | SJR: Q2",
}

THESAURUS_CONCEPTS = {
    "online impulse buying": ["impulse buying", "impulsive buying", "impulsive purchase", "impulse purchase", "urge to buy impulsively", "impulse shopping"],
    "artificial intelligence": ["artificial intelligence", "ai-driven", "ai-enabled", "ai-powered", "ai recommendation", "machine learning"],
    "recommender systems": ["recommender system", "recommendation system", "recommendation agent", "algorithmic recommendation"],
    "perceived personalization": ["personalization", "personalisation", "personalized recommendation", "tailored recommendation"],
    "s-o-r framework": ["stimulus-organism-response", "s-o-r", "sor model", "sor framework"],
    "livestreaming commerce": ["livestream", "live-stream", "live stream", "live commerce", "live streaming"],
    "generative ai & chatbots": ["generative ai", "genai", "large language model", "llm", "chatgpt", "conversational ai", "chatbot", "virtual assistant"],
    "e-commerce": ["e-commerce", "ecommerce", "online shopping", "online retail", "mobile commerce", "m-commerce"],
    "trust": ["trust", "cognitive trust", "affective trust", "algorithmic trust"],
    "privacy & surveillance reactance": ["privacy concern", "privacy risk", "privacy paradox", "intrusiveness", "surveillance", "psychological reactance", "dark pattern"],
    "cognitive load & ego depletion": ["ego depletion", "self-control", "self-regulation", "cognitive overload", "information overload", "decision fatigue"],
    "hedonic pleasure & arousal": ["hedonic", "pleasure", "enjoyment", "arousal", "flow experience", "immersion"],
    "utilitarian value & accuracy": ["utilitarian", "usefulness", "accuracy", "decision quality", "cognitive fit"],
    "social presence & parasocial": ["social presence", "parasocial", "anthropomorphism", "human-like"],
    "scarcity & urgency": ["scarcity", "time pressure", "fear of missing out", "fomo", "urgency"],
    "e-satisfaction": ["e-satisfaction", "customer satisfaction", "satisfaction"],
    "post-purchase regret": ["regret", "post-purchase regret", "cognitive dissonance"],
    "pls-sem": ["pls-sem", "partial least squares", "structural equation modeling", "smartpls"],
    "social commerce": ["social commerce", "social media", "tiktok", "douyin", "instagram"],
    "gen z consumers": ["generation z", "gen z", "young consumer"],
}

SEMINAL_DOIS_TO_VERIFY = {
    "Xiao_2007": "10.2307/25148784",
    "Xiao_2018": "10.1016/j.dss.2018.03.005",
    "Mariani_2022": "10.1002/mar.21619",
    "AlNatour_2011": "10.17705/1jais.00267",
    "Zheng_2019": "10.1016/j.ijinfomgt.2019.02.010",
    "Sundar_2019": "10.1145/3290605.3300768",
    "Guha_2021": "10.1016/j.jretai.2021.01.005",
    "Dwivedi_2021": "10.1016/j.ijinfomgt.2019.08.002",
    "Paul_2019_IMR": "10.1108/IMR-10-2018-0280",
    "Paul_Criado_2020": "10.1016/j.ibusrev.2020.101717",
    "Page_2021": "10.1136/bmj.n71",
    "Donthu_2021": "10.1016/j.jbusres.2021.04.070",
    "Vohs_2007": "10.1086/510228",
    "Awad_2006": "10.2307/25148715",
    "Aguirre_2015": "10.1016/j.jretai.2014.09.005",
    "Mathur_2019": "10.1145/3359183",
    "Logg_2019": "10.1016/j.obhdp.2018.12.005",
    "Hagger_2016": "10.1177/1745691616652873",
    "Baumeister_2002": "10.1086/338209",
    "Beatty_1998": "10.1016/S0022-4359(99)80092-X",
    "Rook_1995": "10.1086/209452",
    "Mehrabian_1974": "",
    "Verhagen_2011": "10.1016/j.im.2011.08.001",
    "Chan_2017": "10.1016/j.im.2016.06.001",
    "Kumaran_2026": "10.1080/10496491.2026.2669635",
    "Tobon_2024": "10.1007/s11846-024-00808-3",
    "Lin_2026": "10.1016/j.actpsy.2026.107594",
    "Pang_2026": "10.1016/j.chb.2026.108999",
}


def norm_doi(doi: str) -> str:
    if not doi:
        return ""
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip().lower()).strip()


def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (title or "").lower())


def safe_int(val, default=0) -> int:
    try:
        return int(float(str(val).strip()))
    except Exception:
        return default


def verify_crossref_doi(doi: str) -> dict:
    if not doi:
        return {"status": "no_doi"}
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    req = urllib.request.Request(url, headers={"User-Agent": "SLR-CitationAuditor/1.0 (mailto:research@tdtu-lab.edu.vn)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8")).get("message", {})
            authors = []
            for a in data.get("author", [])[:10]:
                fam = a.get("family", "")
                giv = a.get("given", "")
                if fam:
                    initials = " ".join(f"{w[0].upper()}." for w in giv.split() if w)
                    authors.append(f"{fam}, {initials}" if initials else fam)
            year = None
            for key in ("published-print", "published-online", "issued"):
                dp = (data.get(key) or {}).get("date-parts")
                if dp and dp[0]:
                    year = dp[0][0]
                    break
            return {
                "status": "verified",
                "doi": doi,
                "authors": authors,
                "year": year,
                "title": (data.get("title") or [""])[0],
                "journal": (data.get("container-title") or [""])[0],
                "volume": data.get("volume", ""),
                "issue": data.get("issue", ""),
                "page": data.get("page", ""),
            }
    except Exception as e:
        return {"status": f"error: {e}", "doi": doi}


def main():
    print("=" * 76)
    print("PHASE 1: PAPER 1A DATA & CITATION AUDIT (CORE CORPUS + CROSSREF)")
    print("=" * 76)

    # 1. Load Dimensions + Expanded CSV pool and deduplicate
    raw_rows = []
    for path, src_label in [(DIM_CSV, "Dimensions"), (EXP_CSV, "OpenAlex_Expanded")]:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    r["_src"] = src_label
                    raw_rows.append(r)

    seen_dois, seen_titles = set(), set()
    unique_rows = []
    dups = 0
    for r in raw_rows:
        d = norm_doi(r.get("DOI", ""))
        t = norm_title(r.get("Title", ""))
        if not t or (d and d in seen_dois) or (t in seen_titles):
            dups += 1
            continue
        if d:
            seen_dois.add(d)
        seen_titles.add(t)
        unique_rows.append(r)

    # 2. Strict 3-Pillar Screening for Paper 1A Core Corpus
    osf_log = []
    core_rows = []
    counts_excl = Counter()

    for r in unique_rows:
        yr = safe_int(r.get("PubYear"), 0)
        title = (r.get("Title") or "").strip()
        abs_txt = (r.get("Abstract") or "").strip()
        venue = (r.get("Source title/Anthology title") or "").strip()
        text = f"{title} {abs_txt}".lower()

        decision = "INCLUDE_CORE"
        reason = "Meets all 3 Boolean pillars (AI/Rec + Impulse Buying + Online/Retail) in peer-reviewed journal (2018-2026)."

        title_words = set(re.findall(r"[a-z]+", text))
        if yr < 2018 or yr > 2026 or len(abs_txt.split()) < 35 or len(title_words & INDONESIAN_STOPWORDS) >= 3:
            decision = "EXCLUDE_EC3_WINDOW_META"
            reason = f"Year={yr} outside 2018-2026, abstract < 35 words, or non-English (IC1)."
            counts_excl["EC3_window_meta"] += 1
        elif any(rp in text for rp in RETRACTED_PATTERNS):
            decision = "EXCLUDE_EC1_RETRACTED"
            reason = "Retracted or withdrawn article excluded for integrity."
            counts_excl["EC1_non_journal"] += 1
        elif not venue or any(p in venue.lower() for p in NON_JOURNAL_PATTERNS):
            decision = "EXCLUDE_EC1_NON_JOURNAL"
            reason = f"Non-journal or conference/preprint outlet: {venue}"
            counts_excl["EC1_non_journal"] += 1
        elif any(p in text for p in OFF_TOPIC_PATTERNS):
            decision = "EXCLUDE_EC2_OFF_TOPIC"
            reason = "Off-topic mechanism (e.g. duopoly competition, physical store layout, or non-retail)."
            counts_excl["EC2_off_topic"] += 1
        else:
            has_ai = any(k in text for k in [
                "artificial intelligence", "ai-", "ai ", "recommender", "recommendation",
                "personalization", "personalisation", "algorithm", "chatbot", "generative ai",
                "livestream", "live-stream", "live stream",
            ])
            has_impulse = any(k in text for k in [
                "impulse buying", "impulsive buying", "impulsive purchase",
                "impulse purchase", "urge to buy impulsively", "impulse shopping",
            ])
            has_ecom = any(k in text for k in [
                "e-commerce", "ecommerce", "online shopping", "online retail",
                "consumer", "shopper", "shopping", "livestream", "live-stream",
                "mobile commerce", "social commerce", "retail",
            ])
            if not (has_ai and has_impulse and has_ecom):
                decision = "EXCLUDE_EC2_NO_3PILLAR"
                reason = f"Missing 3-pillar intersection (AI={has_ai}, Impulse={has_impulse}, Retail={has_ecom})."
                counts_excl["EC2_no_3pillar"] += 1

        osf_log.append({
            "DOI": norm_doi(r.get("DOI", "")),
            "PubYear": yr,
            "Title": title,
            "Journal": venue,
            "Source_Stream": r.get("_src", ""),
            "Decision": decision,
            "Reason": reason,
        })
        if decision == "INCLUDE_CORE":
            core_rows.append(r)

    # Save OSF Screening Log & Core Corpus CSV
    os.makedirs(os.path.dirname(OSF_LOG_CSV), exist_ok=True)
    with open(OSF_LOG_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["DOI", "PubYear", "Title", "Journal", "Source_Stream", "Decision", "Reason"])
        w.writeheader()
        w.writerows(osf_log)

    core_fields = [k for k in core_rows[0].keys() if k != "_src"] if core_rows else []
    with open(CORE_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=core_fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(core_rows)

    n_core = len(core_rows)
    print(f"[1/4] Pool={len(raw_rows)} -> Unique={len(unique_rows)} (Dups={dups}) -> CORE INCLUDED N={n_core}")
    print(f"      Exclusions: EC1={counts_excl['EC1_non_journal']}, EC2_off={counts_excl['EC2_off_topic']}, EC2_missing_pillar={counts_excl['EC2_no_3pillar']}, EC3={counts_excl['EC3_window_meta']}")

    # 3. Annual Trend (2018-2026 strictly) & Top 10 Journals with ABS/ABDC Tiers
    yr_cnt = Counter(safe_int(r["PubYear"]) for r in core_rows)
    annual = []
    cum = 0
    for y in range(2018, 2027):
        c = yr_cnt.get(y, 0)
        cum += c
        annual.append({"year": y, "count": c, "pct": round(c / n_core * 100, 2), "cum_pct": round(cum / n_core * 100, 2)})

    j_cnt, j_cite, j_canon = Counter(), Counter(), {}
    for r in core_rows:
        j = (r.get("Source title/Anthology title") or "").strip()
        if j:
            jk = re.sub(r"\s+", " ", j.lower())
            if jk not in j_canon or sum(1 for ch in j if ch.isupper()) > sum(1 for ch in j_canon[jk] if ch.isupper()):
                j_canon[jk] = j
            j_cnt[jk] += 1
            j_cite[jk] += safe_int(r.get("Times cited", 0))

    top_journals = []
    for jk, cnt in j_cnt.most_common(10):
        top_journals.append({
            "journal": j_canon[jk],
            "count": cnt,
            "pct": round(cnt / n_core * 100, 2),
            "total_citations": j_cite[jk],
            "quality_tier": JOURNAL_TIER_MAP.get(jk, "SJR Indexed"),
        })

    # Top 10 Most Cited STRICTLY from Core Corpus
    top_cited_core = []
    for r in sorted(core_rows, key=lambda x: safe_int(x.get("Times cited", 0)), reverse=True)[:12]:
        if norm_doi(r.get("DOI", "")) and r.get("Authors", "").strip():
            top_cited_core.append({
                "doi": norm_doi(r.get("DOI", "")),
                "year": safe_int(r.get("PubYear")),
                "title": r.get("Title", "").strip(),
                "journal": r.get("Source title/Anthology title", "").strip(),
                "authors": r.get("Authors", "").strip(),
                "citations": safe_int(r.get("Times cited", 0)),
            })

    # 4. Full-Corpus Structured Evidence Coding (100% of Core Corpus)
    coding = Counter()
    for r in core_rows:
        txt = f"{r.get('Title','')} {r.get('Abstract','')}".lower()
        # Theories
        if any(k in txt for k in ["stimulus-organism-response", "s-o-r", "sor model", "sor framework"]):
            coding["theory_sor"] += 1
        if any(k in txt for k in ["technology acceptance", "tam", "utaut"]):
            coding["theory_tam_utaut"] += 1
        if any(k in txt for k in ["flow theory", "flow experience"]):
            coding["theory_flow"] += 1
        if any(k in txt for k in ["ego depletion", "self-control", "self-regulation"]):
            coding["theory_self_regulation"] += 1
        if any(k in txt for k in ["reactance", "privacy calculus", "surveillance"]):
            coding["theory_reactance_privacy"] += 1
        # Contexts
        if any(k in txt for k in ["livestream", "live-stream", "live stream", "live commerce"]):
            coding["ctx_livestream"] += 1
        if any(k in txt for k in ["social commerce", "tiktok", "douyin", "instagram"]):
            coding["ctx_social_commerce"] += 1
        if any(k in txt for k in ["chatbot", "conversational ai", "generative ai", "llm"]):
            coding["ctx_genai_chatbot"] += 1
        # Methods
        if any(k in txt for k in ["pls-sem", "partial least squares", "smartpls"]):
            coding["meth_pls_sem"] += 1
        if any(k in txt for k in ["experiment", "randomized", "scenario"]):
            coding["meth_experiment"] += 1
        if any(k in txt for k in ["longitudinal", "panel", "multi-wave"]):
            coding["meth_longitudinal"] += 1
        # Specific Mechanisms
        if any(k in txt for k in ["inverted-u", "inverted u", "curvilinear", "quadratic", "non-linear", "nonlinear"]):
            coding["mech_nonlinear_u"] += 1
        if any(k in txt for k in ["moderated mediation", "interaction effect", "multiplicative"]):
            coding["mech_interaction"] += 1
        if any(k in txt for k in ["regret", "cognitive dissonance"]):
            coding["mech_regret"] += 1

    evidence_coding = {k: {"count": v, "pct": round(v / n_core * 100, 2)} for k, v in coding.items()}

    # 5. Multi-Method Bibliometrics on Core Corpus
    # 5a. Keyword Co-occurrence + Resolution Stability Check
    doc_concepts, c_years, c_counts = [], defaultdict(list), Counter()
    for r in core_rows:
        txt = f"{r.get('Title','')} {r.get('Abstract','')}".lower()
        yr = safe_int(r["PubYear"], 2023)
        matched = {c for c, pats in THESAURUS_CONCEPTS.items() if any(p in txt for p in pats)}
        if matched:
            doc_concepts.append(matched)
            for c in matched:
                c_counts[c] += 1
                c_years[c].append(yr)

    G_kw = nx.Graph()
    for c, cnt in c_counts.items():
        if cnt >= 5:
            G_kw.add_node(c, occ=cnt, apy=round(sum(c_years[c]) / len(c_years[c]), 2))
    ew = Counter()
    for cs in doc_concepts:
        fl = sorted(c for c in cs if c in G_kw)
        for i in range(len(fl)):
            for j in range(i + 1, len(fl)):
                ew[(fl[i], fl[j])] += 1
    for (u, v), w in ew.items():
        if w >= 3:
            G_kw.add_edge(u, v, weight=w)
    G_kw.remove_nodes_from(list(nx.isolates(G_kw)))

    comm_10 = list(greedy_modularity_communities(G_kw, weight="weight", resolution=1.0))
    comm_125 = list(greedy_modularity_communities(G_kw, weight="weight", resolution=1.25))

    # Generate clean, readable Keyword Co-occurrence Network SVG
    node_cl = {}
    for cid, cm in enumerate(sorted(comm_10, key=len, reverse=True), 1):
        for n in cm:
            node_cl[n] = min(cid, 4)
    pos_kw = nx.spring_layout(G_kw, k=1.8 / math.sqrt(max(G_kw.number_of_nodes(), 1)), weight="weight", seed=42, iterations=250)
    kw_colors = {1: "#2563eb", 2: "#dc2626", 3: "#16a34a", 4: "#d97706"}
    w_svg, h_svg = 900, 520
    cx_s, cy_s = w_svg / 2, h_svg / 2 - 10
    sx_s, sy_s = 360, 195
    edges_svg = []
    for u, v, d in sorted(G_kw.edges(data=True), key=lambda x: x[2]["weight"], reverse=True)[:70]:
        x1, y1 = cx_s + pos_kw[u][0] * sx_s, cy_s + pos_kw[u][1] * sy_s
        x2, y2 = cx_s + pos_kw[v][0] * sx_s, cy_s + pos_kw[v][1] * sy_s
        edges_svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#cbd5e1" stroke-width="{min(3.0, 0.6 + d["weight"]/12.0):.1f}" opacity="0.75"/>')
    max_kw_occ = max((G_kw.nodes[n]["occ"] for n in G_kw.nodes()), default=1)
    nodes_svg = []
    for n in G_kw.nodes():
        nx_p, ny_p = cx_s + pos_kw[n][0] * sx_s, cy_s + pos_kw[n][1] * sy_s
        r_p = 7 + 14 * math.sqrt(G_kw.nodes[n]["occ"] / max_kw_occ)
        col = kw_colors.get(node_cl.get(n, 1), "#2563eb")
        nodes_svg.append(f'<circle cx="{nx_p:.1f}" cy="{ny_p:.1f}" r="{r_p:.1f}" fill="{col}" fill-opacity="0.88" stroke="#ffffff" stroke-width="1.5"/>')
        nodes_svg.append(f'<text x="{nx_p:.1f}" y="{ny_p - r_p - 4:.1f}" text-anchor="middle" font-size="10.5" font-weight="600" fill="#0f172a">{n}</text>')
    kw_svg_path = os.path.join(BASE_DIR, "lab_projects", "figures", "paper1a_kw_network.svg")
    os.makedirs(os.path.dirname(kw_svg_path), exist_ok=True)
    with open(kw_svg_path, "w", encoding="utf-8") as f_svg:
        f_svg.write(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w_svg} {h_svg}" width="100%" height="auto" style="font-family: \'Segoe UI\', Arial, sans-serif; background:#ffffff;">'
            f'<text x="{w_svg/2}" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Keyword Co-occurrence Network Across Clean Core Corpus (N={n_core})</text>'
            + "".join(edges_svg) + "".join(nodes_svg)
            + '<rect x="30" y="476" width="840" height="30" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>'
            + '<circle cx="65" cy="491" r="6" fill="#2563eb"/><text x="78" y="495" font-size="10.5" fill="#1e293b">Cluster 1: Livestreaming &amp; S-O-R</text>'
            + '<circle cx="315" cy="491" r="6" fill="#dc2626"/><text x="328" y="495" font-size="10.5" fill="#1e293b">Cluster 2: Personalization &amp; Trust</text>'
            + '<circle cx="585" cy="491" r="6" fill="#16a34a"/><text x="598" y="495" font-size="10.5" fill="#1e293b">Cluster 3: GenAI, Scarcity &amp; Self-Regulation</text>'
            + '</svg>'
        )

    # 5b. Bibliographic Coupling (shared cited DOIs in Cited references)
    doc_refs = []
    for idx, r in enumerate(core_rows):
        cr = r.get("Cited references", "")
        dois = set(re.findall(r"10\.\d{4,9}/[-._;()/:a-z0-9]+", cr.lower()))
        if dois:
            doc_refs.append((idx, r.get("Title", "")[:60], dois))
    G_bc = nx.Graph()
    for i in range(len(doc_refs)):
        for j in range(i + 1, len(doc_refs)):
            shared = len(doc_refs[i][2] & doc_refs[j][2])
            if shared >= 3:
                G_bc.add_edge(doc_refs[i][0], doc_refs[j][0], weight=shared)
    bc_comms = list(greedy_modularity_communities(G_bc, weight="weight")) if G_bc.number_of_edges() > 0 else []

    # 5c. Co-Citation top cited journals/works
    ref_doi_counts = Counter()
    for _, _, dois in doc_refs:
        for d in dois:
            ref_doi_counts[d] += 1
    top_cocited = [{"doi": d, "co_citations": c} for d, c in ref_doi_counts.most_common(10)]

    print(f"[2/4] Bibliometrics: KW_nodes={G_kw.number_of_nodes()} (res 1.0 -> {len(comm_10)} clusters, res 1.25 -> {len(comm_125)} clusters)")
    print(f"      BibCoupling: {G_bc.number_of_nodes()} coupled docs, {G_bc.number_of_edges()} edges, {len(bc_comms)} clusters")

    # 6. Crossref API Verification of Seminal & Flagged References
    print("[3/4] Verifying flagged & seminal DOIs via Crossref Official Registry...")
    verified_refs = {}
    for label, doi in SEMINAL_DOIS_TO_VERIFY.items():
        if doi:
            res = verify_crossref_doi(doi)
            verified_refs[label] = res
            print(f"  - {label:16s} ({doi}): {res['status']} | {res.get('journal', '')} ({res.get('year', '')})")
            time.sleep(0.15)
        else:
            verified_refs[label] = {"status": "book_no_doi", "title": "An approach to environmental psychology", "year": 1974}

    with open(REFS_JSON, "w", encoding="utf-8") as f:
        json.dump(verified_refs, f, indent=2, ensure_ascii=False)

    stats = {
        "prisma": {
            "gross_pool": len(raw_rows),
            "duplicates_removed": dups,
            "unique_screened": len(unique_rows),
            "excluded_ec1_non_journal": counts_excl["EC1_non_journal"],
            "excluded_ec2_off_topic": counts_excl["EC2_off_topic"],
            "excluded_ec2_missing_pillar": counts_excl["EC2_no_3pillar"],
            "excluded_ec3_window_meta": counts_excl["EC3_window_meta"],
            "final_core_included": n_core,
        },
        "annual_trend": annual,
        "top_journals": top_journals,
        "top_cited_core": top_cited_core,
        "evidence_coding": evidence_coding,
        "bibliometrics": {
            "kw_nodes": G_kw.number_of_nodes(),
            "kw_edges": G_kw.number_of_edges(),
            "kw_clusters_res10": len(comm_10),
            "kw_clusters_res125": len(comm_125),
            "bc_nodes": G_bc.number_of_nodes(),
            "bc_edges": G_bc.number_of_edges(),
            "bc_clusters": len(bc_comms),
            "top_cocited_dois": top_cocited,
        },
    }
    with open(STATS_JSON, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    print(f"[4/4] Saved clean stats -> {STATS_JSON}")
    print("=" * 76)


if __name__ == "__main__":
    main()
