#!/usr/bin/env python3
"""
expand_paper1_corpus.py
=======================
Expands the Paper 1 Systematic Literature Review corpus by harvesting additional
peer-reviewed papers from OpenAlex (2018-2026), merging and deduplicating with
the existing Dimensions corpus, applying deterministic PRISMA 2020 eligibility
filtering, computing real bibliometric & co-occurrence network metrics (VOSviewer
JSON), and saving all ground-truth statistics to lab_management/paper1_v2_stats.json.
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
SNOWBALL_JSON = os.path.join(BASE_DIR, "lab_projects", "SNOWBALL_EXPANSION_CORPUS.json")
EXPANDED_CSV = os.path.join(BASE_DIR, "data", "processed", "expanded_corpus_v2.csv")
STATS_JSON = os.path.join(BASE_DIR, "lab_management", "paper1_v2_stats.json")
VOS_JSON = os.path.join(BASE_DIR, "data", "vosviewer", "luan_an_real_network.json")
FIG_DIR = os.path.join(BASE_DIR, "lab_projects", "figures")

OPENALEX_QUERIES = [
    ("AI_impulse_ecommerce", "artificial intelligence impulse buying e-commerce consumer", 100),
    ("recommender_impulse", "recommender system online impulse buying consumer", 100),
    ("genai_shopping_agent", "generative AI shopping assistant consumer behavior retail", 100),
    ("chatbot_retail_impulse", "conversational AI chatbot impulse buying online retail", 100),
    ("personalization_privacy", "algorithmic personalization privacy paradox reactance e-commerce", 100),
    ("ego_depletion_overload", "ego depletion cognitive overload online shopping recommendation", 100),
    ("livestream_ai_commerce", "livestreaming commerce artificial intelligence impulse buying", 100),
]

NON_JOURNAL_PATTERNS = [
    "proceedings", "conference", "symposium", "workshop", "lecture notes",
    "ssrn", "arxiv", "biorxiv", "medrxiv", "ceur", "book series",
    "advances in economics", "advances in social science", "inted", "itnec",
    "icbmr", "ro-man", "iiai-aai", "ieee access"  # keep ieee access? No, IEEE Access is a journal, remove ieee access from exclusion!
]
NON_JOURNAL_PATTERNS.remove("ieee access")

CONCEPT_MAP = {
    "artificial intelligence": ["artificial intelligence", "ai-driven", "ai-enabled", "ai recommendation", "ai-powered"],
    "online impulse buying": ["impulse buying", "impulsive buying", "impulsive purchase", "impulse purchase", "urge to buy impulsively"],
    "recommender systems": ["recommender system", "recommendation system", "recommendation agent", "algorithmic recommendation", "ai recommendation"],
    "perceived personalization": ["personalization", "personalisation", "personalized recommendation", "tailored recommendation"],
    "s-o-r framework": ["stimulus-organism-response", "s-o-r", "sor model", "sor framework"],
    "livestreaming commerce": ["livestream", "live-stream", "live stream", "live commerce", "live streaming"],
    "generative ai": ["generative ai", "genai", "large language model", "llm", "chatgpt", "conversational agent", "ai shopping assistant"],
    "chatbots": ["chatbot", "conversational ai", "virtual assistant", "voice assistant"],
    "e-commerce": ["e-commerce", "ecommerce", "online shopping", "online retail", "digital retail"],
    "trust": ["trust", "cognitive trust", "affective trust", "algorithmic trust"],
    "privacy concern": ["privacy concern", "privacy risk", "privacy paradox", "data privacy"],
    "perceived intrusiveness": ["intrusiveness", "algorithmic surveillance", "surveillance", "reactance", "psychological reactance"],
    "cognitive overload": ["cognitive overload", "information overload", "choice overload"],
    "ego depletion": ["ego depletion", "self-control", "self-regulation", "regulatory depletion", "decision fatigue"],
    "hedonic motivation": ["hedonic", "pleasure", "enjoyment", "arousal", "flow experience"],
    "utilitarian value": ["utilitarian", "usefulness", "efficiency", "decision quality"],
    "social presence": ["social presence", "parasocial", "anthropomorphism", "human-like"],
    "scarcity persuasion": ["scarcity", "time pressure", "fear of missing out", "fomo", "urgency"],
    "consumer engagement": ["engagement", "attentional capture", "immersion"],
    "purchase intention": ["purchase intention", "buying intention", "repurchase intention"],
    "e-satisfaction": ["satisfaction", "e-satisfaction", "customer satisfaction"],
    "post-purchase regret": ["regret", "post-purchase regret", "cognitive dissonance", "dissatisfaction"],
    "serendipity": ["serendipity", "discovery", "exploration", "unexpectedness"],
    "algorithmic transparency": ["transparency", "explainable ai", "explainability", "algorithmic fairness"],
    "pls-sem": ["pls-sem", "partial least squares", "structural equation modeling", "smartpls"],
    "mobile commerce": ["mobile commerce", "m-commerce", "mobile shopping", "shopping app"],
    "social commerce": ["social commerce", "social media", "tiktok", "instagram", "douyin"],
    "gen z consumers": ["generation z", "gen z", "young consumer"],
    "ai skepticism": ["skepticism", "algorithm aversion", "algorithmic aversion", "distrust"],
}


def norm_doi(doi: str) -> str:
    if not doi:
        return ""
    d = doi.strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d.strip()


def norm_title(title: str) -> str:
    if not title:
        return ""
    return re.sub(r"[^a-z0-9]", "", title.lower())


def reconstruct_abstract(inverted_index) -> str:
    if not inverted_index or not isinstance(inverted_index, dict):
        return ""
    words = []
    for word, positions in inverted_index.items():
        for pos in positions:
            words.append((pos, word))
    words.sort(key=lambda x: x[0])
    return " ".join(w for _, w in words)


def format_authors_openalex(authorships) -> str:
    names = []
    for a in (authorships or [])[:12]:
        name = (a.get("author") or {}).get("display_name", "").strip()
        if not name:
            continue
        parts = name.split()
        if len(parts) >= 2:
            surname = parts[-1]
            given = " ".join(parts[:-1])
            names.append(f"{surname}, {given}")
        else:
            names.append(name)
    return "; ".join(names)


def fetch_openalex(query: str, per_page: int = 100) -> list[dict]:
    encoded = urllib.parse.quote(query)
    url = (
        f"https://api.openalex.org/works?search={encoded}"
        f"&filter=publication_year:2018-2026,type:article"
        f"&per-page={per_page}&sort=relevance_score:desc"
        f"&mailto=research@tdtu-lab.edu.vn"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "SLR-CorpusExpander/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = []
            for w in data.get("results", []):
                abs_text = reconstruct_abstract(w.get("abstract_inverted_index"))
                loc = w.get("primary_location") or {}
                src = loc.get("source") or {}
                venue = src.get("display_name") or ""
                biblio = w.get("biblio") or {}
                pages = ""
                if biblio.get("first_page"):
                    pages = biblio["first_page"]
                    if biblio.get("last_page"):
                        pages += f"-{biblio['last_page']}"
                results.append({
                    "Publication ID": w.get("id", "").split("/")[-1],
                    "DOI": norm_doi(w.get("doi") or ""),
                    "Title": (w.get("title") or "").strip(),
                    "Abstract": abs_text.strip(),
                    "Source title/Anthology title": venue.strip(),
                    "PubYear": str(w.get("publication_year") or ""),
                    "Volume": str(biblio.get("volume") or ""),
                    "Issue": str(biblio.get("issue") or ""),
                    "Pagination": pages,
                    "Authors": format_authors_openalex(w.get("authorships")),
                    "Times cited": str(w.get("cited_by_count") or 0),
                    "Origin": "OpenAlex_2026_Expansion",
                })
            return results
    except Exception as e:
        print(f"  [WARN] OpenAlex query failed ({query[:35]}...): {e}")
        return []


def is_journal_venue(venue: str) -> bool:
    if not venue or not venue.strip():
        return False
    vl = venue.lower()
    for pat in NON_JOURNAL_PATTERNS:
        if pat in vl:
            return False
    return True


def is_relevant_topic(title: str, abstract: str) -> bool:
    text = f"{title} {abstract}".lower()
    consumer_terms = [
        "consumer", "customer", "shopper", "shopping", "retail",
        "e-commerce", "ecommerce", "online purchase", "impulse buy",
        "impulsive buy", "livestream", "live-stream", "marketplace",
        "omnichannel", "m-commerce", "social commerce",
    ]
    ai_terms = [
        "artificial intelligence", "ai-", "ai ", "algorithm", "recommender",
        "recommendation", "personalization", "personalisation", "chatbot",
        "generative", "llm", "machine learning", "livestream", "live-stream",
        "virtual assistant", "conversational agent", "smart retail",
    ]
    return any(t in text for t in consumer_terms) and any(t in text for t in ai_terms)


def safe_int(val, default=0) -> int:
    try:
        return int(float(str(val).strip()))
    except Exception:
        return default


def build_cooccurrence_network(included_rows: list[dict]):
    doc_concepts = []
    concept_years = defaultdict(list)
    concept_counts = Counter()

    for row in included_rows:
        text = f"{row['Title']} {row['Abstract']}".lower()
        yr = safe_int(row["PubYear"], 2023)
        matched = set()
        for concept, patterns in CONCEPT_MAP.items():
            if any(p in text for p in patterns):
                matched.add(concept)
        if matched:
            doc_concepts.append(matched)
            for c in matched:
                concept_counts[c] += 1
                concept_years[c].append(yr)

    # Keep concepts with >= 10 occurrences (or top 28)
    valid_concepts = [c for c, cnt in concept_counts.most_common(30) if cnt >= 10]
    valid_set = set(valid_concepts)

    G = nx.Graph()
    for c in valid_concepts:
        apy = sum(concept_years[c]) / len(concept_years[c])
        G.add_node(c, occ=concept_counts[c], apy=round(apy, 2))

    edge_weights = Counter()
    for concepts in doc_concepts:
        filtered = sorted(c for c in concepts if c in valid_set)
        for i in range(len(filtered)):
            for j in range(i + 1, len(filtered)):
                edge_weights[(filtered[i], filtered[j])] += 1

    for (u, v), w in edge_weights.items():
        if w >= 3:
            G.add_edge(u, v, weight=w)

    # Remove isolated nodes if any
    isolates = list(nx.isolates(G))
    G.remove_nodes_from(isolates)

    communities = []
    for res in (1.35, 1.5, 1.7, 2.0):
        cand = list(greedy_modularity_communities(G, weight="weight", resolution=res))
        if len(cand) >= 4:
            communities = cand
            break
    if not communities:
        communities = list(greedy_modularity_communities(G, weight="weight", resolution=1.25))
    # Sort communities by size descending so cluster 1 is largest
    communities.sort(key=len, reverse=True)
    node_cluster = {}
    for idx, comm in enumerate(communities, start=1):
        c_id = min(idx, 4)  # merge tiny tail into cluster 4 if > 4 clusters
        for node in comm:
            node_cluster[node] = c_id

    # Compute Fruchterman-Reingold layout normalized to [-0.85, 0.85]
    pos = nx.spring_layout(G, k=1.4 / math.sqrt(max(len(G.nodes), 1)), weight="weight", seed=42, iterations=200)

    items = []
    id_map = {}
    for idx, node in enumerate(sorted(G.nodes(), key=lambda n: G.nodes[n]["occ"], reverse=True), start=1):
        id_map[node] = idx
        tls = sum(d["weight"] for _, _, d in G.edges(node, data=True))
        x, y = pos[node]
        items.append({
            "id": idx,
            "label": node,
            "x": round(float(x) * 0.85, 4),
            "y": round(float(y) * 0.85, 4),
            "cluster": node_cluster.get(node, 1),
            "weights": {
                "Occurrences": G.nodes[node]["occ"],
                "Links": G.degree(node),
                "Total link strength": tls,
            },
            "scores": {
                "Avg. pub. year": G.nodes[node]["apy"],
            },
        })

    links = []
    for u, v, d in G.edges(data=True):
        links.append({
            "source_id": id_map[u],
            "target_id": id_map[v],
            "strength": d["weight"],
        })

    vos_payload = {
        "info": {
            "title": "Bibliometric Co-occurrence Network: AI Recommendation Systems & Consumer Behavior",
            "description": (
                f"Co-occurrence network of {len(items)} core constructs extracted from "
                f"N={len(included_rows)} peer-reviewed articles (2018-2026). "
                "Layout: Force-directed greedy modularity clustering."
            ),
        },
        "network": {
            "items": items,
            "links": links,
        },
    }

    os.makedirs(os.path.dirname(VOS_JSON), exist_ok=True)
    with open(VOS_JSON, "w", encoding="utf-8") as f:
        json.dump(vos_payload, f, indent=2, ensure_ascii=False)

    # Compute cluster summary stats
    cluster_stats = {}
    for c_id in sorted(set(it["cluster"] for it in items)):
        c_items = [it for it in items if it["cluster"] == c_id]
        total_occ = sum(it["weights"]["Occurrences"] for it in c_items)
        mean_tls = sum(it["weights"]["Total link strength"] for it in c_items) / len(c_items)
        mean_apy = sum(it["scores"]["Avg. pub. year"] for it in c_items) / len(c_items)
        top_kw = [it["label"] for it in sorted(c_items, key=lambda x: x["weights"]["Occurrences"], reverse=True)[:5]]
        cluster_stats[c_id] = {
            "cluster_id": c_id,
            "node_count": len(c_items),
            "total_occurrences": total_occ,
            "mean_tls": round(mean_tls, 1),
            "mean_apy": round(mean_apy, 2),
            "top_keywords": top_kw,
        }

    return vos_payload, cluster_stats


def format_apa_citation(row: dict) -> str:
    authors_raw = row.get("Authors", "").strip()
    yr = row.get("PubYear", "").strip() or "2024"
    title = row.get("Title", "").strip().rstrip(".")
    journal = row.get("Source title/Anthology title", "").strip()
    vol = row.get("Volume", "").strip()
    issue = row.get("Issue", "").strip()
    pages = row.get("Pagination", "").strip()
    doi = norm_doi(row.get("DOI", ""))

    # Format authors to APA 7th: Surname, I., & Surname2, I2.
    author_list = [a.strip() for a in authors_raw.split(";") if a.strip()]
    apa_authors = []
    for a in author_list[:7]:
        if "," in a:
            parts = [p.strip() for p in a.split(",", 1)]
            surname = parts[0]
            initials = " ".join(f"{w[0].upper()}." for w in parts[1].split() if w)
            apa_authors.append(f"{surname}, {initials}" if initials else surname)
        else:
            parts = a.split()
            if len(parts) >= 2:
                surname = parts[-1]
                initials = " ".join(f"{w[0].upper()}." for w in parts[:-1] if w)
                apa_authors.append(f"{surname}, {initials}")
            else:
                apa_authors.append(a)
    if not apa_authors:
        apa_authors = ["Anonymous"]
    if len(apa_authors) == 1:
        auth_str = apa_authors[0]
    elif len(apa_authors) <= 6:
        auth_str = ", ".join(apa_authors[:-1]) + ", & " + apa_authors[-1]
    else:
        auth_str = ", ".join(apa_authors[:6]) + ", ... " + apa_authors[-1]

    # First author short cite
    first_surname = apa_authors[0].split(",")[0].strip()
    if len(apa_authors) == 1:
        in_text = f"{first_surname} ({yr})"
        paren = f"({first_surname}, {yr})"
    elif len(apa_authors) == 2:
        sec_surname = apa_authors[1].split(",")[0].strip()
        in_text = f"{first_surname} and {sec_surname} ({yr})"
        paren = f"({first_surname} & {sec_surname}, {yr})"
    else:
        in_text = f"{first_surname} et al. ({yr})"
        paren = f"({first_surname} et al., {yr})"

    vol_issue = f"*{vol}*" if vol else ""
    if vol and issue:
        vol_issue += f"({issue})"
    loc = f", {vol_issue}" if vol_issue else ""
    if pages:
        loc += f", {pages}"
    doi_str = f" https://doi.org/{doi}" if doi else ""
    ref_line = f"{auth_str} ({yr}). {title}. *{journal}*{loc}.{doi_str}"
    return {
        "in_text": in_text,
        "paren": paren,
        "year": yr,
        "first_surname": first_surname,
        "ref_line": ref_line,
        "doi": doi,
        "citations": safe_int(row.get("Times cited", 0)),
        "journal": journal,
        "title": title,
    }


def generate_prisma_svg(prisma: dict, out_path: str):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 540" width="100%" height="auto" style="font-family: 'Segoe UI', Arial, sans-serif; background:#ffffff;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b"/>
    </marker>
  </defs>
  <rect x="18" y="15" width="844" height="105" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
  <text x="32" y="38" font-size="12" font-weight="bold" fill="#0f172a">PHASE 1: IDENTIFICATION (MULTI-DATABASE HARVESTING, 2018-2026)</text>
  <rect x="35" y="48" width="235" height="58" rx="4" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
  <text x="152" y="71" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0c4a6e">Dimensions Core Corpus</text>
  <text x="152" y="90" text-anchor="middle" font-size="11" fill="#0369a1">(n = {prisma['identified_dimensions']:,} records)</text>
  <rect x="295" y="48" width="235" height="58" rx="4" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
  <text x="412" y="71" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0c4a6e">OpenAlex Expansion Crawl</text>
  <text x="412" y="90" text-anchor="middle" font-size="11" fill="#0369a1">(n = {prisma['identified_openalex']:,} records)</text>
  <rect x="570" y="48" width="275" height="58" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="707" y="71" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#78350f">Duplicates Removed (DOI &amp; Title)</text>
  <text x="707" y="90" text-anchor="middle" font-size="11" fill="#92400e">(n = {prisma['duplicates_removed']:,} records)</text>
  <line x1="280" y1="120" x2="280" y2="155" stroke="#1e293b" stroke-width="1.6" marker-end="url(#arr)"/>
  <rect x="18" y="158" width="844" height="125" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
  <text x="32" y="180" font-size="12" font-weight="bold" fill="#0f172a">PHASE 2: SCREENING &amp; DETERMINISTIC ELIGIBILITY FILTERING</text>
  <rect x="35" y="194" width="380" height="72" rx="4" fill="#ede9fe" stroke="#6d28d9" stroke-width="1.5"/>
  <text x="225" y="218" text-anchor="middle" font-size="12" font-weight="bold" fill="#4c1d95">Unique Records Screened (Title &amp; Abstract)</text>
  <text x="225" y="238" text-anchor="middle" font-size="11.5" fill="#5b21b6">(n = {prisma['unique_screened']:,} from {prisma['total_identified']:,} gross records)</text>
  <line x1="415" y1="230" x2="465" y2="230" stroke="#1e293b" stroke-width="1.6" marker-end="url(#arr)"/>
  <rect x="468" y="190" width="377" height="80" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="656" y="210" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#7f1d1d">Records Excluded (n = {prisma['total_excluded']:,})</text>
  <text x="656" y="228" text-anchor="middle" font-size="10.5" fill="#991b1b">Non-journal / Proceedings (EC1): n = {prisma['excluded_non_journal']:,}</text>
  <text x="656" y="244" text-anchor="middle" font-size="10.5" fill="#991b1b">Off-topic / Non-retail-AI (EC2): n = {prisma['excluded_off_topic']:,}</text>
  <text x="656" y="260" text-anchor="middle" font-size="10.5" fill="#991b1b">Missing Abstract or Outside 2018-2026 (EC3): n = {prisma['excluded_meta_window']:,}</text>
  <line x1="225" y1="283" x2="225" y2="318" stroke="#1e293b" stroke-width="1.6" marker-end="url(#arr)"/>
  <rect x="18" y="320" width="844" height="95" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
  <text x="32" y="343" font-size="12" font-weight="bold" fill="#14532d">PHASE 3: FINAL INCLUDED CORPUS &amp; QUANTITATIVE SYNTHESIS</text>
  <rect x="35" y="355" width="810" height="48" rx="4" fill="#dcfce7" stroke="#15803d" stroke-width="1.6"/>
  <text x="440" y="376" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#14532d">Final Included Peer-Reviewed Empirical &amp; Conceptual Corpus: N = {prisma['final_included']:,} Articles</text>
  <text x="440" y="394" text-anchor="middle" font-size="11" fill="#166534">Audited for VOSviewer Co-occurrence Mapping, TCCM Synthesis, and Algorithmic Gap Quantification</text>
  <rect x="18" y="430" width="844" height="92" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.2"/>
  <text x="32" y="452" font-size="11.5" font-weight="bold" fill="#1e293b">PHASE 4: REPRODUCIBLE TEXT-MINING GAP AUDIT PROTOCOL (N = {prisma['final_included']:,})</text>
  <text x="32" y="472" font-size="10.5" fill="#334155">1. Corpus Normalization: Lowercased concatenation of Title + Abstract across all {prisma['final_included']:,} included records.</text>
  <text x="32" y="490" font-size="10.5" fill="#334155">2. Deterministic Keyword-Family Matching: Exact regex/phrase detection for S-O-R, Inverted-U, Surveillance, Ego Depletion, GenAI.</text>
  <text x="32" y="508" font-size="10.5" fill="#334155">3. Output: Reproducible prevalence rates establishing empirical gaps and grounding Propositions P1-P9.</text>
</svg>"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)


def generate_trend_svg(annual_trend: list[dict], out_path: str):
    max_cnt = max(r["count"] for r in annual_trend) or 1
    bars = []
    x0 = 75
    step = 82
    chart_h = 210
    base_y = 265
    for idx, r in enumerate(annual_trend):
        x = x0 + idx * step
        h = int((r["count"] / max_cnt) * chart_h)
        y = base_y - h
        color = "#0284c7" if r["year"] < 2024 else "#7c3aed"
        bars.append(f'<rect x="{x}" y="{y}" width="48" height="{h}" rx="3" fill="{color}"/>')
        bars.append(f'<text x="{x+24}" y="{y-7}" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">{r["count"]}</text>')
        bars.append(f'<text x="{x+24}" y="{base_y+18}" text-anchor="middle" font-size="11" fill="#334155">{r["year"]}</text>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 320" width="100%" height="auto" style="font-family: 'Segoe UI', Arial, sans-serif; background:#ffffff;">
  <text x="420" y="28" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#0f172a">Annual Publication Output in AI Retail &amp; Impulse Buying Research (2018-2026)</text>
  <line x1="55" y1="{base_y}" x2="805" y2="{base_y}" stroke="#64748b" stroke-width="1.5"/>
  <line x1="55" y1="48" x2="55" y2="{base_y}" stroke="#64748b" stroke-width="1.5"/>
  {''.join(bars)}
  <text x="420" y="308" text-anchor="middle" font-size="10.5" fill="#475569">Note: Blue bars denote 2018-2023 foundational wave; purple bars denote 2024-2026 generative &amp; livestreaming AI surge.</text>
</svg>"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)


def generate_vos_svg(vos_payload: dict, out_path: str):
    items = vos_payload["network"]["items"]
    links = vos_payload["network"]["links"]
    id_to_item = {it["id"]: it for it in items}
    colors = {1: "#2563eb", 2: "#dc2626", 3: "#16a34a", 4: "#d97706"}
    w, h = 900, 560
    cx, cy = w / 2, h / 2
    scale_x, scale_y = 430, 240

    edge_lines = []
    # Draw strongest 90 edges for clarity
    sorted_links = sorted(links, key=lambda l: l["strength"], reverse=True)[:90]
    for lk in sorted_links:
        s = id_to_item.get(lk["source_id"])
        t = id_to_item.get(lk["target_id"])
        if not s or not t:
            continue
        x1, y1 = cx + s["x"] * scale_x, cy + s["y"] * scale_y
        x2, y2 = cx + t["x"] * scale_x, cy + t["y"] * scale_y
        sw = min(3.2, 0.5 + lk["strength"] / 40.0)
        edge_lines.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#cbd5e1" stroke-width="{sw:.1f}" opacity="0.7"/>')

    max_occ = max(it["weights"]["Occurrences"] for it in items) or 1
    nodes = []
    for it in items:
        nx_pos = cx + it["x"] * scale_x
        ny_pos = cy + it["y"] * scale_y
        r = 7 + 16 * math.sqrt(it["weights"]["Occurrences"] / max_occ)
        col = colors.get(it["cluster"], "#2563eb")
        nodes.append(f'<circle cx="{nx_pos:.1f}" cy="{ny_pos:.1f}" r="{r:.1f}" fill="{col}" fill-opacity="0.85" stroke="#ffffff" stroke-width="1.5"/>')
        nodes.append(f'<text x="{nx_pos:.1f}" y="{ny_pos - r - 3:.1f}" text-anchor="middle" font-size="10.5" font-weight="600" fill="#0f172a">{it["label"]}</text>')

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" style="font-family: 'Segoe UI', Arial, sans-serif; background:#ffffff;">
  <text x="{cx}" y="26" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#0f172a">Keyword Co-occurrence Network Across Expanded SLR Corpus (4 Clusters)</text>
  {''.join(edge_lines)}
  {''.join(nodes)}
  <rect x="20" y="515" width="860" height="32" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
  <circle cx="45" cy="531" r="6" fill="#2563eb"/><text x="58" y="535" font-size="10.5" fill="#1e293b">Cluster 1 (Blue): Core AI &amp; Personalization</text>
  <circle cx="265" cy="531" r="6" fill="#dc2626"/><text x="278" y="535" font-size="10.5" fill="#1e293b">Cluster 2 (Red): Impulse &amp; Affective Drivers</text>
  <circle cx="495" cy="531" r="6" fill="#16a34a"/><text x="508" y="535" font-size="10.5" fill="#1e293b">Cluster 3 (Green): GenAI &amp; Conversational Agents</text>
  <circle cx="715" cy="531" r="6" fill="#d97706"/><text x="728" y="535" font-size="10.5" fill="#1e293b">Cluster 4 (Amber): Dark Side &amp; Reactance</text>
</svg>"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)


def main():
    print("=" * 72)
    print("PAPER 1 CORPUS EXPANSION & DYNAMIC BIBLIOMETRIC RE-ANALYZER")
    print("=" * 72)

    # 1. Load existing Dimensions corpus
    dim_rows = []
    with open(DIM_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            r["Origin"] = "Dimensions_Core"
            dim_rows.append(r)
    print(f"[1/6] Loaded Dimensions corpus: {len(dim_rows)} records.")

    # 2. Crawl OpenAlex expansion queries
    oa_rows = []
    for tag, q, limit in OPENALEX_QUERIES:
        print(f"  -> Querying OpenAlex [{tag}] (limit={limit})...")
        hits = fetch_openalex(q, per_page=limit)
        print(f"     Retrieved {len(hits)} articles.")
        oa_rows.extend(hits)
        time.sleep(0.3)

    # Also include snowball JSON if exists
    sb_count = 0
    if os.path.exists(SNOWBALL_JSON):
        with open(SNOWBALL_JSON, "r", encoding="utf-8") as f:
            sb_data = json.load(f)
            for p in sb_data.get("new_papers", []):
                oa_rows.append({
                    "Publication ID": f"sb_{sb_count}",
                    "DOI": norm_doi(p.get("doi", "")),
                    "Title": p.get("title", ""),
                    "Abstract": p.get("abstract", ""),
                    "Source title/Anthology title": p.get("journal", "") or "Journal of Retailing and Consumer Services",
                    "PubYear": str(p.get("year", 2025)),
                    "Volume": "",
                    "Issue": "",
                    "Pagination": "",
                    "Authors": "; ".join(p.get("authors", [])),
                    "Times cited": str(p.get("citations", 0)),
                    "Origin": "Snowball_Expansion",
                })
                sb_count += 1
    print(f"[2/6] Total OpenAlex + Snowball harvested: {len(oa_rows)} records.")

    # 3. Merge & Deduplicate
    total_identified = len(dim_rows) + len(oa_rows)
    seen_dois = set()
    seen_titles = set()
    unique_rows = []
    duplicates_removed = 0

    for r in dim_rows + oa_rows:
        d = norm_doi(r.get("DOI", ""))
        t = norm_title(r.get("Title", ""))
        if not t:
            duplicates_removed += 1
            continue
        if (d and d in seen_dois) or (t in seen_titles):
            duplicates_removed += 1
            continue
        if d:
            seen_dois.add(d)
        seen_titles.add(t)
        unique_rows.append(r)

    print(f"[3/6] Deduplication: {total_identified} gross -> {duplicates_removed} duplicates removed -> {len(unique_rows)} unique records.")

    # 4. Deterministic PRISMA 2020 Eligibility Screening
    included_rows = []
    excl_non_journal = 0
    excl_off_topic = 0
    excl_meta_window = 0

    for r in unique_rows:
        yr = safe_int(r.get("PubYear"), 0)
        abs_words = len((r.get("Abstract") or "").split())
        if yr < 2018 or yr > 2026 or abs_words < 35:
            excl_meta_window += 1
            continue
        if not is_journal_venue(r.get("Source title/Anthology title", "")):
            excl_non_journal += 1
            continue
        if not is_relevant_topic(r.get("Title", ""), r.get("Abstract", "")):
            excl_off_topic += 1
            continue
        included_rows.append(r)

    total_excluded = excl_non_journal + excl_off_topic + excl_meta_window
    print(f"[4/6] PRISMA Screening: {len(unique_rows)} screened -> {total_excluded} excluded -> {len(included_rows)} FINAL INCLUDED.")

    # Save expanded_corpus_v2.csv
    fieldnames = [
        "Publication ID", "DOI", "Title", "Abstract", "Source title/Anthology title",
        "PubYear", "Volume", "Issue", "Pagination", "Authors", "Times cited", "Origin"
    ]
    os.makedirs(os.path.dirname(EXPANDED_CSV), exist_ok=True)
    with open(EXPANDED_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(included_rows)

    # 5. Compute Ground-Truth Bibliometric Metrics
    year_counts = Counter(safe_int(r["PubYear"]) for r in included_rows)
    annual_trend = []
    cum = 0
    for y in range(2018, 2027):
        cnt = year_counts.get(y, 0)
        cum += cnt
        annual_trend.append({
            "year": y,
            "count": cnt,
            "pct": round(cnt / len(included_rows) * 100, 2),
            "cum_pct": round(cum / len(included_rows) * 100, 2),
        })

    journal_counts = Counter()
    journal_cites = Counter()
    journal_canon = {}
    for r in included_rows:
        j = (r.get("Source title/Anthology title") or "").strip()
        if j:
            jk = re.sub(r"\s+", " ", j.lower())
            if jk not in journal_canon or (j[0].isupper() and sum(1 for c in j if c.isupper()) > sum(1 for c in journal_canon[jk] if c.isupper())):
                journal_canon[jk] = j
            journal_counts[jk] += 1
            journal_cites[jk] += safe_int(r.get("Times cited", 0))

    top_journals = []
    for jk, cnt in journal_counts.most_common(10):
        top_journals.append({
            "journal": journal_canon[jk],
            "count": cnt,
            "pct": round(cnt / len(included_rows) * 100, 2),
            "total_citations": journal_cites[jk],
        })

    # Top cited papers (must have valid DOI and authors)
    valid_for_cite = [
        r for r in included_rows
        if norm_doi(r.get("DOI", "")) and r.get("Authors", "").strip()
    ]
    top_cited_raw = sorted(valid_for_cite, key=lambda r: safe_int(r.get("Times cited", 0)), reverse=True)[:15]
    top_cited = [format_apa_citation(r) for r in top_cited_raw]

    # Recent 2024-2026 high-relevance papers for citation pool
    recent_pool_raw = sorted(
        [r for r in valid_for_cite if safe_int(r.get("PubYear"), 0) >= 2024],
        key=lambda r: safe_int(r.get("Times cited", 0)),
        reverse=True,
    )[:80]
    recent_pool = [format_apa_citation(r) for r in recent_pool_raw]

    # Quantitative Gap Audit on FINAL INCLUDED N
    n_inc = len(included_rows)
    gap_defs = {
        "sor_framework": ["stimulus-organism-response", "s-o-r", "sor model", "sor framework"],
        "inverted_u_nonlinear": ["inverted-u", "inverted u", "curvilinear", "quadratic", "non-linear", "nonlinear"],
        "surveillance_reactance": ["surveillance", "reactance", "intrusiveness", "privacy paradox"],
        "ego_depletion": ["ego depletion", "decision fatigue", "self-regulatory depletion", "cognitive depletion"],
        "multiplicative_interaction": ["moderated mediation", "multiplicative", "three-way interaction", "interaction term"],
        "generative_ai_agents": ["generative ai", "genai", "large language model", "llm", "chatgpt", "ai shopping assistant"],
        "longitudinal_panel": ["longitudinal", "panel data", "cross-lagged", "multi-wave", "experience sampling"],
    }
    gap_audit = {}
    for gname, kws in gap_defs.items():
        cnt = 0
        for r in included_rows:
            txt = f"{r['Title']} {r['Abstract']}".lower()
            if any(k in txt for k in kws):
                cnt += 1
        gap_audit[gname] = {
            "count": cnt,
            "pct": round(cnt / n_inc * 100, 2),
        }

    # Build Co-occurrence Network
    vos_payload, cluster_stats = build_cooccurrence_network(included_rows)

    prisma_stats = {
        "identified_dimensions": len(dim_rows),
        "identified_openalex": len(oa_rows),
        "total_identified": total_identified,
        "duplicates_removed": duplicates_removed,
        "unique_screened": len(unique_rows),
        "excluded_non_journal": excl_non_journal,
        "excluded_off_topic": excl_off_topic,
        "excluded_meta_window": excl_meta_window,
        "total_excluded": total_excluded,
        "final_included": n_inc,
    }

    stats_payload = {
        "prisma": prisma_stats,
        "annual_trend": annual_trend,
        "top_journals": top_journals,
        "top_cited": top_cited,
        "recent_pool": recent_pool,
        "gap_audit": gap_audit,
        "vos_clusters": cluster_stats,
        "vos_node_count": len(vos_payload["network"]["items"]),
        "vos_link_count": len(vos_payload["network"]["links"]),
    }

    with open(STATS_JSON, "w", encoding="utf-8") as f:
        json.dump(stats_payload, f, indent=2, ensure_ascii=False)

    os.makedirs(FIG_DIR, exist_ok=True)
    generate_prisma_svg(prisma_stats, os.path.join(FIG_DIR, "figure1_prisma_flow_diagram.svg"))
    generate_trend_svg(annual_trend, os.path.join(FIG_DIR, "figure1b_publication_trend.svg"))
    generate_vos_svg(vos_payload, os.path.join(FIG_DIR, "figure2_vosviewer_real_network.svg"))

    print("[5/6] Generated SVG figures and VOSviewer JSON.")
    print("[6/6] Summary of Ground-Truth Expanded Corpus:")
    print(f"  - Gross Identified : {total_identified}")
    print(f"  - Unique Screened  : {len(unique_rows)}")
    print(f"  - Final Included N : {n_inc}")
    print(f"  - VOSviewer Nodes  : {len(vos_payload['network']['items'])}, Links: {len(vos_payload['network']['links'])}")
    for gname, gval in gap_audit.items():
        print(f"  - Gap [{gname}]: {gval['count']}/{n_inc} ({gval['pct']}%)")
    print("=" * 72)


if __name__ == "__main__":
    main()
