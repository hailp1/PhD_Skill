# AI-Driven Personalized Recommendation Systems and Online Consumer Impulse Buying Behavior: A Systematic Literature Review and Bibliometric Network Analysis

**Target Journal:** Journal of Retailing and Consumer Services (Elsevier)  
**Article Type:** Review Article (Systematic Literature Review, Multi-Method Bibliometric Analysis, and Evidence-Based Research Agenda)  
**Submission Protocol:** Blinded Manuscript for Double-Blind Peer Review

---

## HIGHLIGHTS

* Synthesizes 179 peer-reviewed articles (2018-2026) at the AI-impulse buying intersection.
* Combines keyword co-occurrence, bibliographic coupling, and co-citation mapping.
* Provides full-corpus evidence coding and ABDC/ABS/SJR outlet stratification.
* Separates immediate cognitive fluency, relational trust, and post-purchase satisfaction.
* Outlines a testable future agenda on privacy reactance and post-purchase regret.

---

## ABSTRACT

Algorithmic recommendation systems and conversational shopping agents increasingly mediate product discovery in digital retail, yet empirical research linking artificial intelligence (AI) stimuli to online impulse buying remains fragmented across disciplines. Following PRISMA 2020 reporting principles and the Theories-Contexts-Characteristics-Methods (TCCM) framework, this study conducts a systematic literature review and multi-method bibliometric analysis of 179 peer-reviewed journal articles published between January 2018 and November 2026 (with early-access 2027 records excluded). Screening 1,780 unique records harvested across Dimensions and OpenAlex against a three-pillar Boolean intersection (AI/recommendation systems, online impulse buying, and digital retail), we establish a transparent, OSF-ready screening log and code the entire 179-article core corpus. Keyword co-occurrence analysis (20 thesaurus-standardized concepts across 3 to 5 clusters depending on resolution), bibliographic coupling (73 coupled articles, 817 shared-reference links), and co-citation mapping reveal heavy reliance on cross-sectional Stimulus-Organism-Response (S-O-R) surveys (26.82%) and livestreaming contexts (39.66%). Conversely, privacy reactance (0.56%), non-linear personalization thresholds (0.56%), cognitive-affective interactions (1.68%), and longitudinal designs (4.47%) remain scarce. Synthesizing these empirical gaps alongside foundational self-regulation, privacy-paradox, and dark-pattern scholarship, we formulate an evidence-based future research agenda comprising seven testable propositions (P1-P7) and discuss design and regulatory implications.

**Keywords:** Systematic literature review; Bibliometric analysis; AI recommendation systems; Online impulse buying; Personalization-privacy paradox; Self-regulation; S-O-R framework

---

## 1. INTRODUCTION

### 1.1. Research Background and Scope

Digital commerce has shifted from keyword-driven search toward algorithmically curated discovery, where predictive recommender systems and conversational shopping assistants dynamically shape consideration sets (Xiao and Benbasat (2007); Guha et al. (2021); Germonprez et al. (2011)). In consumer psychology and retailing, understanding how algorithmic cues convert browsing into unplanned purchases requires bridging information systems design with affective and self-regulatory theory (Beatty and Elizabeth Ferrell (1998); Rook and Fisher (1995); Chan et al. (2017); Zheng et al. (2019)). Prior conceptual accounts note that AI functionalities can lower search friction while simultaneously introducing persuasive nudges and algorithmic friction (Dwivedi et al. (2021); Mariani et al. (2022)). Recent empirical studies across livestreaming and social commerce, including Beikverdi et al. (2023), Zhang et al. (2020), Luo et al. (2024), and Huang et al. (2024), illustrate rapid practitioner adoption of real-time recommendation feeds, while Feng et al. (2024), Gong and Jiang (2023), Liu et al. (2020), and Xia et al. (2024) highlight growing scholarly interest in mobile and AI-assisted impulse consumption.

### 1.2. Positioning Relative to Prior Reviews and Research Questions

Existing reviews have examined general online impulse buying (Chan et al. (2017)), AI applications in marketing and consumer research (Mariani et al. (2022); Guha et al. (2021)), and early recommendation agent adoption (Xiao and Benbasat (2007)). However, no prior review has simultaneously isolated the strict three-pillar intersection of AI/algorithmic personalization, online impulse buying, and digital retail across 2018-2026 while combining full-corpus evidence coding with multi-method bibliometric mapping (keyword co-occurrence, bibliographic coupling, and co-citation). Recent studies on recursive temporal S-O-R feedback (Tobon and Abril (2025)) and synthetic urgency backfire (Siva Bala Kumaran and Shobhana (2026)) underscore the need to consolidate empirical evidence before proposing new theoretical extensions. Accordingly, this review addresses four research questions:
1. **RQ1:** What are the publication trajectory, outlet quality distribution (ABDC/ABS/SJR), and citation structure of the 179-article core corpus from 2018 to 2026?
2. **RQ2:** What intellectual clusters and research fronts emerge across keyword co-occurrence, bibliographic coupling, and co-citation networks?
3. **RQ3:** Across full-corpus TCCM evidence coding, which theoretical mechanisms, contexts, and methods are well supported, mixed, or empirically under-explored?
4. **RQ4:** What falsifiable propositions and empirical designs should guide future research on curvilinear personalization, cognitive-affective interactions, self-control strain, and post-purchase regret?

---

## 2. METHODOLOGY

### 2.1. Three-Pillar Search Strategy and Database Adaptation

Following PRISMA 2020 reporting guidelines (Page et al. (2021)) and the TCCM review protocol (Paul and Rosado-Serrano (2019); Stewart and Yap (2020)), we executed an iterative search across Dimensions and OpenAlex covering January 2018 through November 2026 (final search completed November 2026). To ensure transparency, our search logic operationalizes a **three-pillar Boolean intersection** combining (1) AI and algorithmic recommendation stimuli, (2) impulse buying outcomes, and (3) online retail and commerce contexts. Because query syntax differs across bibliographic engines (for example, `TITLE-ABS-KEY` in Scopus vs. `TS=` in Web of Science vs. full-text/abstract indexing in Dimensions and OpenAlex), the standardized conceptual Boolean query is documented below:

```text
TITLE-ABS-KEY (
  ("artificial intelligence" OR "recommender system*" OR "recommendation agent*"
   OR "algorithmic personalization" OR "generative AI" OR "conversational AI"
   OR "chatbot*" OR "livestream* commerce")
  AND
  ("impulse buying" OR "impulsive purchase" OR "urge to buy impulsively"
   OR "impulse shopping")
  AND
  ("e-commerce" OR "online shopping" OR "online retail" OR "social commerce"
   OR "mobile commerce" OR "digital retail")
)
```

### 2.2. Eligibility Criteria, Deduplication, and OSF-Ready Screening Audit

Merging Dimensions and OpenAlex harvests yielded 2,457 gross records. Automated normalization of Digital Object Identifiers (DOIs) and punctuation-stripped titles removed 677 duplicates, leaving 1,780 unique records for eligibility screening. Rather than relying on broad AI-marketing proxies, we enforced four deterministic rules:
* **IC1 (Time Window & Language):** Peer-reviewed journal articles published in English between January 2018 and November 2026 (indexed 2027 early-access records were explicitly excluded).
* **EC1 (Non-Journal Outlets):** Conference proceedings, workshops, book chapters, and unrefereed preprints were excluded ($n = 50$).
* **EC2 (Off-Topic & Missing Three-Pillar Intersection):** Articles focusing on analytical duopoly pricing, physical brick-and-mortar store layouts, or lacking empirical/conceptual focus on *both* AI/algorithmic cues and online impulse buying were excluded ($n = 1,539$, comprising 45 off-topic studies and 1,494 studies missing one or more Boolean pillars).
* **EC3 (Window & Metadata Completeness):** Records outside 2018-2026 (including 2027 early-access items) or lacking sufficient abstract text (< 35 words) were excluded ($n = 12$).

These criteria retained a focused **Core Corpus of $N = 179$ peer-reviewed journal articles**. To ensure full auditability and address reproducibility standards, the complete 1,780-row decision ledger (`paper1a_osf_screening_log.csv`) documenting every included and excluded DOI and exclusion code is archived in the project repository for Open Science Framework (OSF) deposit. Figure 1 summarizes the PRISMA 2020 selection flow.

<div class="academic-figure-container" style="text-align:center; margin: 20px 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="auto" style="font-family: 'Segoe UI', Arial, sans-serif; background:#ffffff;">
<defs><marker id="ar1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b"/></marker></defs>
<rect x="20" y="15" width="840" height="92" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="34" y="36" font-size="11.5" font-weight="bold" fill="#0f172a">PHASE 1: IDENTIFICATION (DIMENSIONS CORE + OPENALEX EXPANSION, 2018-2026)</text>
<rect x="34" y="46" width="385" height="50" rx="4" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.4"/>
<text x="226" y="68" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0c4a6e">Gross Identified Records: n = 2,457</text>
<text x="226" y="85" text-anchor="middle" font-size="10" fill="#0369a1">Three-Pillar Boolean Intersection (AI/Rec + Impulse Buying + Online Retail)</text>
<rect x="455" y="46" width="390" height="50" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.4"/>
<text x="650" y="68" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#78350f">Duplicates Removed (DOI &amp; Title): n = 677</text>
<text x="650" y="85" text-anchor="middle" font-size="10" fill="#92400e">Automated Normalization &amp; Cross-Database Deduplication</text>
<line x1="226" y1="107" x2="226" y2="142" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar1)"/>
<rect x="20" y="145" width="840" height="145" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="34" y="167" font-size="11.5" font-weight="bold" fill="#0f172a">PHASE 2: DETERMINISTIC SCREENING &amp; ELIGIBILITY AUDIT (OSF LOGGED)</text>
<rect x="34" y="182" width="360" height="90" rx="4" fill="#ede9fe" stroke="#6d28d9" stroke-width="1.4"/>
<text x="214" y="218" text-anchor="middle" font-size="12" font-weight="bold" fill="#4c1d95">Unique Records Screened</text>
<text x="214" y="238" text-anchor="middle" font-size="11.5" fill="#5b21b6">n = 1,780 Records</text>
<line x1="394" y1="227" x2="438" y2="227" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar1)"/>
<rect x="440" y="178" width="405" height="98" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.4"/>
<text x="642" y="198" text-anchor="middle" font-size="11" font-weight="bold" fill="#7f1d1d">Excluded Records (n = 1,601)</text>
<text x="642" y="216" text-anchor="middle" font-size="10" fill="#991b1b">EC1 Non-Journal / Proceedings: n = 50</text>
<text x="642" y="233" text-anchor="middle" font-size="10" fill="#991b1b">EC2 Off-Topic (Duopoly / Store Layout): n = 45</text>
<text x="642" y="250" text-anchor="middle" font-size="10" fill="#991b1b">EC2 Missing 3-Pillar Intersection (No Impulse Measure): n = 1,494</text>
<text x="642" y="267" text-anchor="middle" font-size="10" fill="#991b1b">EC3 Outside 2018-2026 (incl. 2027) / Short Abstract: n = 12</text>
<line x1="214" y1="290" x2="214" y2="325" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar1)"/>
<rect x="20" y="328" width="840" height="110" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
<text x="34" y="350" font-size="11.5" font-weight="bold" fill="#14532d">PHASE 3: FINAL CORE CORPUS &amp; MULTI-METHOD SYNTHESIS</text>
<rect x="34" y="362" width="810" height="60" rx="4" fill="#dcfce7" stroke="#15803d" stroke-width="1.5"/>
<text x="439" y="387" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#14532d">Final Included Core Corpus: N = 179 Peer-Reviewed Journal Articles (2018-2026)</text>
<text x="439" y="407" text-anchor="middle" font-size="10.5" fill="#166534">Full-Corpus Evidence Coding + Keyword Co-Occurrence + Bibliographic Coupling + Co-Citation</text>
</svg>
<div class="figure-caption"><strong>Figure 1:</strong> PRISMA 2020 Selection Flow and Deterministic Three-Pillar Screening Audit ($N = 179$ Core Corpus).</div>
</div>

### 2.3. Full-Corpus Coding and Multi-Method Bibliometric Protocol

Unlike prior reviews that rely on keyword frequency counts alone, we coded all 179 included articles across theoretical lenses, retail contexts, empirical methods, and tested structural mechanisms using a standardized codebook. For science mapping (Donthu et al. (2021)), we applied three complementary bibliometric techniques on the 179-article core corpus:
1. **Keyword Co-occurrence with Thesaurus Standardization:** Synonymous variants (for example, *impulse buying*, *impulsive buying*, and *urge to buy impulsively*) were merged via a 20-concept thesaurus (minimum threshold = 5 occurrences, edge weight $\ge 3$). Cluster stability was evaluated across modularity resolution parameters (`1.0` yielding 3 macro-clusters vs. `1.25` yielding 5 sub-clusters).
2. **Bibliographic Coupling:** Articles sharing $\ge 3$ cited references in their bibliography were linked to identify active research fronts (73 coupled articles, 817 edges, 4 clusters).
3. **Co-Citation Analysis:** Shared reference DOIs across all 179 bibliographies were aggregated to identify the foundational intellectual anchors of the field.

---

## 3. RESULTS: PERFORMANCE, BIBLIOMETRIC MAPPING, AND EVIDENCE SYNTHESIS

### 3.1. Publication Trajectory and Outlet Quality Stratification

As shown in Table 1 and Figure 2, core output grew from 1 article in 2018 to 84 articles in 2026 (with 2024-2026 accounting for 86.59% of the 179-article corpus). Notably, this post-2024 acceleration coincides with commercial deployment of livestreaming recommendation feeds and conversational AI, though raw growth also partly reflects broader expansion in open-access multidisciplinary publishing.

<div class="academic-figure-container" style="text-align:center; margin: 20px 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 305" width="100%" height="auto" style="font-family: 'Segoe UI', Arial, sans-serif; background:#ffffff;">
<text x="420" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Annual Publication Output in Core AI-Impulse Buying Corpus (2018-2026, 2027 Excluded)</text>
<line x1="55" y1="250" x2="800" y2="250" stroke="#64748b" stroke-width="1.5"/>
<line x1="55" y1="45" x2="55" y2="250" stroke="#64748b" stroke-width="1.5"/>
<rect x="75" y="250" width="46" height="0" rx="3" fill="#0284c7"/><text x="98" y="244" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">0</text><text x="98" y="268" text-anchor="middle" font-size="11" fill="#334155">2018</text><rect x="157" y="250" width="46" height="0" rx="3" fill="#0284c7"/><text x="180" y="244" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">0</text><text x="180" y="268" text-anchor="middle" font-size="11" fill="#334155">2019</text><rect x="239" y="241" width="46" height="9" rx="3" fill="#0284c7"/><text x="262" y="235" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">4</text><text x="262" y="268" text-anchor="middle" font-size="11" fill="#334155">2020</text><rect x="321" y="250" width="46" height="0" rx="3" fill="#0284c7"/><text x="344" y="244" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">0</text><text x="344" y="268" text-anchor="middle" font-size="11" fill="#334155">2021</text><rect x="403" y="237" width="46" height="13" rx="3" fill="#0284c7"/><text x="426" y="231" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">6</text><text x="426" y="268" text-anchor="middle" font-size="11" fill="#334155">2022</text><rect x="485" y="218" width="46" height="32" rx="3" fill="#0284c7"/><text x="508" y="212" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">14</text><text x="508" y="268" text-anchor="middle" font-size="11" fill="#334155">2023</text><rect x="567" y="206" width="46" height="44" rx="3" fill="#7c3aed"/><text x="590" y="200" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">19</text><text x="590" y="268" text-anchor="middle" font-size="11" fill="#334155">2024</text><rect x="649" y="130" width="46" height="120" rx="3" fill="#7c3aed"/><text x="672" y="124" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">52</text><text x="672" y="268" text-anchor="middle" font-size="11" fill="#334155">2025</text><rect x="731" y="55" width="46" height="195" rx="3" fill="#7c3aed"/><text x="754" y="49" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">84</text><text x="754" y="268" text-anchor="middle" font-size="11" fill="#334155">2026</text>
<text x="420" y="292" text-anchor="middle" font-size="10" fill="#475569">Note: Blue bars (2018-2023) represent early algorithmic adoption; purple bars (2024-2026) reflect livestreaming and GenAI expansion.</text>
</svg>
<div class="figure-caption"><strong>Figure 2:</strong> Annual Publication Distribution Across the Core Corpus (2018-2026, $N = 179$).</div>
</div>

**Table 1: Annual Publication Output in the Core Corpus (2018-2026, $N = 179$)**

| Year | Article Count | Share (%) | Cumulative Share (%) |
| :--- | :---: | :---: | :---: |
| 2018 | 0 | 0.00% | 0.00% |
| 2019 | 0 | 0.00% | 0.00% |
| 2020 | 4 | 2.23% | 2.23% |
| 2021 | 0 | 0.00% | 2.23% |
| 2022 | 6 | 3.35% | 5.59% |
| 2023 | 14 | 7.82% | 13.41% |
| 2024 | 19 | 10.61% | 24.02% |
| 2025 | 52 | 29.05% | 53.07% |
| 2026 | 84 | 46.93% | 100.00% |

Table 2 reports the leading publication outlets alongside their ABDC, ABS/AJG, and SJR quality classifications. *Journal of Theoretical and Applied Electronic Commerce Research* (11 articles), *Frontiers in Psychology* (6 articles), and *Journal of Retailing and Consumer Services* (5 articles, 261 citations) lead the distribution. Because multidisciplinary open-access outlets account for a notable share of recent volume, sensitivity inspection confirms that ABDC-A/ABS 2-3* journals (*Journal of Retailing and Consumer Services*, *Asia Pacific Journal of Marketing and Logistics*, *Computers in Human Behavior*) disproportionately anchor foundational S-O-R and experimental studies, including Ngo et al. (2025), Arachchi and Samarasinghe (2023), Gao and Liang (2025), Miranda et al. (2024), and Huu et al. (2023) and Saad and Choura (2022), Gallin and Portes (2024), Zhang and Zhang (2024), Zhu et al. (2023), and Gong et al. (2024).

**Table 2: Top 10 Publishing Outlets with Quality Tier Stratification ($N = 179$)**

| Rank | Journal Title | Articles | Share (%) | Citations | Quality Tier (ABDC / ABS / SJR) |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | Journal of Theoretical and Applied Electronic Commerce Research | 11 | 6.15% | 98 | ABDC: B | ABS: 1 | SJR: Q1 |
| 2 | Frontiers in Psychology | 6 | 3.35% | 335 | SJR: Q1/Q2 (Non-ABS) |
| 3 | Journal of Retailing and Consumer Services | 5 | 2.79% | 261 | ABDC: A | ABS: 2 | SJR: Q1 |
| 4 | International Review of Management and Marketing | 3 | 1.68% | 4 | SJR Indexed |
| 5 | Sustainability | 3 | 1.68% | 182 | SJR: Q1/Q2 (Non-ABS) |
| 6 | Asia Pacific Journal of Marketing and Logistics | 3 | 1.68% | 77 | ABDC: A | ABS: 1 | SJR: Q1 |
| 7 | Zenodo (CERN European Organization for Nuclear Research) | 3 | 1.68% | 2 | SJR Indexed |
| 8 | Acta Psychologica | 2 | 1.12% | 57 | SJR: Q2 (Non-ABS) |
| 9 | Behavioral Sciences | 2 | 1.12% | 2 | SJR: Q2 (Non-ABS) |
| 10 | Young Consumers | 2 | 1.12% | 64 | SJR Indexed |

Table 3 lists the six most-cited empirical articles strictly within the 179-article core corpus (excluding general AI-marketing conceptual reviews that do not measure impulse buying). Empirical citation leadership is concentrated in livestreaming and social-commerce impulse studies.

**Table 3: Top Cited Empirical Studies Strictly Within the Core Corpus ($N = 179$)**

| Rank | Study | Title (Abbreviated) | Journal | Citations |
| :---: | :--- | :--- | :--- | :---: |
| 1 | Huo et al. (2023) | Why do consumers buy impulsively during live streaming? A deep learning-... | Journal of Business Research | 240 |
| 2 | Chen et al. (2022) | Exploring Factors Affecting Consumer’s Impulse Buying Behavior in Live-S... | SAGE Open | 168 |
| 3 | Abdelsalam et al. (2020) | Research on the Impact of Marketing Strategy on Consumers’ Impulsive Pur... | Frontiers in Psychology | 164 |
| 4 | Zhang et al. (2023) | Understanding Online Impulse Buying Behavior in Social Commerce: A Syste... | IEEE Access | 108 |
| 5 | Yang et al. (2022) | How Do Virtual AI Streamers Influence Viewers’ Livestream Shopping Behav... | Information Systems Frontiers | 106 |
| 6 | Ampadu et al. (2022) | Effects of Interface Design and Live Atmosphere on Consumers’ Impulse-Bu... | Sustainability | 100 |

### 3.2. Multi-Method Bibliometric Structure

Across the three bibliometric layers, inductive clustering reveals converging yet distinct structural patterns:
* **Keyword Co-Occurrence Structure:** At resolution `1.0`, the 20 standardized concepts partition into 3 stable macro-clusters: (1) livestreaming commerce, S-O-R, and hedonic arousal; (2) algorithmic personalization, trust, and utilitarian accuracy; and (3) emerging generative AI, scarcity, and self-regulation constructs. Increasing resolution to `1.25` splits the third cluster into 5 finer sub-themes, separating conversational AI agents from privacy and ego-depletion constructs.
* **Bibliographic Coupling Fronts (73 articles, 817 links, 4 clusters):** Coupling analysis confirms four active research fronts sharing common reference bases: livestreaming presenter-algorithm interaction (Adyantari et al. (2025), Amin (2025), and Pham et al. (2024)), personalized recommender trust and serendipity (Xin et al. (2025), Firdausiah et al. (2023), and Kathuria and Bakshi (2024)), social-commerce scarcity and FoMO (Kinasih and Wuryandari (2023), Azizah and Indrawati (2022), and Do Xuan Nguyen and Nguyen (2026)), and nascent AI-driven cognitive load and regret (Liu et al. (2024), Putra et al. (2025), and Song (2023)).
* **Co-Citation Anchors:** Co-citation counts across the core bibliographies confirm that empirical studies overwhelmingly build upon environmental psychology (Mehrabian and Russell (1974)), classic impulse-buying precursors (Rook and Fisher (1995); Beatty and Elizabeth Ferrell (1998)), online store atmospheric S-O-R models (Verhagen and van Dolen (2011)), and recommendation novelty (Beukeboom and Pollmann (2021)).

### 3.3. Full-Corpus Evidence Coding and TCCM Synthesis

Moving beyond selective narrative examples, Table 4 summarizes quantitative evidence coding across **all 179 articles** in the core corpus. While S-O-R (26.82%) and PLS-SEM (26.26%) dominate, critical mechanisms remain severely under-tested: privacy reactance (0.56%), non-linear inverted-U thresholds (0.56%), cognitive-affective interactions (1.68%), and longitudinal panel designs (4.47%).

**Table 4: Full-Corpus TCCM and Relational Evidence Synthesis ($N = 179$)**

| Dimension / Mechanism | Core Corpus Count | Share (%) | Representative Core Studies | Synthesis & Gap Assessment |
| :--- | :---: | :---: | :--- | :--- |
| **S-O-R Theoretical Lens** | 48 | 26.82% | George and Rupa (2025), Ali et al. (2025), Sholihah et al. (2025), Prasetia et al. (2025) | Dominant paradigm; mostly linear additive paths |
| **Livestreaming & Social Commerce** | 71 | 39.66% | Shamim and Misra (2025), Moghddam et al. (2025), Zhang et al. (2026) | Primary empirical setting; heavy China/Asia concentration |
| **PLS-SEM Cross-Sectional Surveys** | 47 | 26.26% | Wang et al. (2024), Wang et al. (2026), Nimisha and Pandey (2025), Pei et al. (2025) | High reliance on single-wave self-reports; limited causality |
| **Experimental Designs** | 20 | 11.17% | Aishwariya and Vidya (2025), Dang and Hoang (2025), Widjaja et al. (2025) | Growing use for chatbot/scarcity manipulation |
| **Self-Regulation / Ego Depletion** | 15 | 8.38% | Wang et al. (2025), Rafdinal et al. (2025), Parihar (2025) | Emerging; rarely accounts for depletion replication debates |
| **GenAI & Conversational Agents** | 11 | 6.15% | Lestari and Dalimunthe (2023), Anoop and Rahman (2025), Abu and Huaqiang (2025) | Rapidly growing; lacks systematic comparison vs. static filtering |
| **Post-Purchase Regret** | 10 | 5.59% | Tobon and Abril (2025); Siva Bala Kumaran and Shobhana (2026) | Mixed findings; rarely linked dynamically to future trust |
| **Longitudinal / Panel Designs** | 8 | 4.47% | Tobon and Abril (2025) | Severe deficit blocking causal feedback testing |
| **Multiplicative Interaction** | 3 | 1.68% | Lin (2026) | Almost absent; additive mediation assumed without testing |
| **Privacy Reactance & Inverted-U** | 1 | 0.56% | Siva Bala Kumaran and Shobhana (2026) | Critical empirical blind spot in impulse buying literature |

---

## 4. EVIDENCE-BASED FUTURE RESEARCH AGENDA

To translate the quantitative gaps in Table 4 into falsifiable empirical inquiry, Figure 3 synthesizes an **Evidence-Based Future Research Agenda** (Propositions P1-P7). Rather than presenting untested conceptual claims as established findings, each proposition below specifies construct definitions, competing theoretical predictions, boundary conditions, and empirical falsification criteria, while integrating foundational privacy-paradox (Awad and Krishnan (2006); Aguirre et al. (2015)), dark-pattern (Mathur et al. (2019)), and algorithm-aversion (Logg et al. (2019)) scholarship.

<div class="academic-figure-container" style="text-align:center; margin: 20px 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 460" width="100%" height="auto" style="font-family: 'Segoe UI', Arial, sans-serif; background:#ffffff;">
<defs><marker id="agb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#1d4ed8"/></marker>
<marker id="agr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626"/></marker>
<marker id="agp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#7c3aed"/></marker></defs>
<text x="460" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Evidence-Based Future Research Agenda: Separable Organismic Paths and Measurable Dark-Side Nodes</text>
<rect x="20" y="45" width="210" height="330" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.4"/>
<text x="125" y="67" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#1e3a8a">STIMULI (S)</text>
<rect x="34" y="85" width="182" height="72" rx="5" fill="#ffffff" stroke="#2563eb" stroke-width="1.3"/>
<text x="125" y="109" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e40af">Algorithmic Personalization</text>
<text x="125" y="126" text-anchor="middle" font-size="9.5" fill="#334155">P1: Inverted-U Curve</text>
<text x="125" y="142" text-anchor="middle" font-size="9.5" fill="#1d4ed8">Moderated by Privacy &amp; Control</text>
<rect x="34" y="175" width="182" height="72" rx="5" fill="#ffffff" stroke="#2563eb" stroke-width="1.3"/>
<text x="125" y="199" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e40af">Novelty &amp; Conversational</text>
<text x="125" y="216" text-anchor="middle" font-size="9.5" fill="#334155">AI Interactivity (P2)</text>
<text x="125" y="232" text-anchor="middle" font-size="9.5" fill="#1d4ed8">Social Presence &amp; Serendipity</text>
<rect x="34" y="265" width="182" height="72" rx="5" fill="#ffffff" stroke="#2563eb" stroke-width="1.3"/>
<text x="125" y="289" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#1e40af">Choice Velocity &amp; Scarcity</text>
<text x="125" y="306" text-anchor="middle" font-size="9.5" fill="#334155">P3: Cognitive Load /</text>
<text x="125" y="322" text-anchor="middle" font-size="9.5" fill="#dc2626">Opportunity-Cost Strain</text>
<rect x="260" y="45" width="370" height="330" rx="8" fill="#fefce8" stroke="#ca8a04" stroke-width="1.4"/>
<text x="445" y="67" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#713f12">SEPARABLE ORGANISMIC NODES (O)</text>
<rect x="278" y="82" width="160" height="66" rx="5" fill="#ffffff" stroke="#0284c7" stroke-width="1.3"/>
<text x="358" y="106" text-anchor="middle" font-size="10" font-weight="bold" fill="#0369a1">In-Session Fluency</text>
<text x="358" y="123" text-anchor="middle" font-size="9.5" fill="#334155">(Immediate Ease)</text>
<rect x="454" y="82" width="160" height="66" rx="5" fill="#ffffff" stroke="#0284c7" stroke-width="1.3"/>
<text x="534" y="106" text-anchor="middle" font-size="10" font-weight="bold" fill="#0369a1">Algorithmic Trust</text>
<text x="534" y="123" text-anchor="middle" font-size="9.5" fill="#334155">(Relational Belief)</text>
<rect x="278" y="166" width="336" height="58" rx="5" fill="#ffffff" stroke="#dc2626" stroke-width="1.3"/>
<text x="446" y="190" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#991b1b">Affective Arousal &amp; Synergistic Interaction (P5b)</text>
<text x="446" y="208" text-anchor="middle" font-size="9.5" fill="#334155">Tests Synergistic (b3 &gt; 0) vs. Hot/Cool Override (b3 &lt; 0)</text>
<rect x="278" y="242" width="336" height="54" rx="5" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.3"/>
<text x="446" y="264" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#7f1d1d">Surveillance Reactance (Measurable Mediator)</text>
<text x="446" y="281" text-anchor="middle" font-size="9.5" fill="#991b1b">P1b: Mediates Negative Tail of Inverted-U Personalization</text>
<rect x="278" y="308" width="336" height="54" rx="5" fill="#f0fdfa" stroke="#0f766e" stroke-width="1.3"/>
<text x="446" y="330" text-anchor="middle" font-size="10" font-weight="bold" fill="#115e59">Candidate Self-Control Strain (P6)</text>
<text x="446" y="347" text-anchor="middle" font-size="9.5" fill="#134e4a">Cognitive Load / Opportunity-Cost / Depletion Debate</text>
<rect x="660" y="45" width="240" height="330" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.4"/>
<text x="780" y="67" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#14532d">RESPONSES &amp; POST-PURCHASE (R)</text>
<rect x="678" y="88" width="204" height="60" rx="5" fill="#ffffff" stroke="#15803d" stroke-width="1.3"/>
<text x="780" y="114" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#166534">Urge to Buy Impulsively (UBI)</text>
<text x="780" y="132" text-anchor="middle" font-size="9.5" fill="#334155">Immediate Behavioral Impulse</text>
<rect x="678" y="170" width="204" height="60" rx="5" fill="#ffffff" stroke="#15803d" stroke-width="1.3"/>
<text x="780" y="196" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#166534">Online Impulse Buying (OIB)</text>
<text x="780" y="214" text-anchor="middle" font-size="9.5" fill="#334155">Unplanned Checkout &amp; Returns</text>
<rect x="678" y="255" width="204" height="96" rx="5" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.4"/>
<text x="780" y="282" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#5b21b6">Post-Purchase Satisfaction</text>
<text x="780" y="300" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#5b21b6">vs. Regret (Measurable Node)</text>
<text x="780" y="322" text-anchor="middle" font-size="9.5" fill="#6d28d9">P7: Dynamic ESM / Log Feedback</text>
<line x1="216" y1="115" x2="276" y2="115" stroke="#1d4ed8" stroke-width="1.7" marker-end="url(#agb)"/>
<line x1="216" y1="140" x2="276" y2="266" stroke="#dc2626" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#agr)"/>
<line x1="216" y1="210" x2="276" y2="195" stroke="#dc2626" stroke-width="1.7" marker-end="url(#agr)"/>
<line x1="216" y1="300" x2="276" y2="332" stroke="#1d4ed8" stroke-width="1.6" marker-end="url(#agb)"/>
<line x1="614" y1="115" x2="676" y2="115" stroke="#1d4ed8" stroke-width="1.7" marker-end="url(#agb)"/>
<line x1="614" y1="195" x2="676" y2="128" stroke="#dc2626" stroke-width="1.7" marker-end="url(#agr)"/>
<line x1="780" y1="148" x2="780" y2="168" stroke="#1d4ed8" stroke-width="1.7" marker-end="url(#agb)"/>
<line x1="780" y1="230" x2="780" y2="253" stroke="#7c3aed" stroke-width="1.7" marker-end="url(#agp)"/>
<path d="M 780 351 L 780 418 L 534 418 L 534 150" fill="none" stroke="#7c3aed" stroke-width="1.7" stroke-dasharray="6,4" marker-end="url(#agp)"/>
<text x="480" y="438" text-anchor="middle" font-size="10" font-weight="bold" fill="#6d28d9">P7 Recursive Feedback: Post-Purchase Regret Updates Future Algorithmic Trust &amp; Reactance Thresholds (ESM / Platform Logs)</text>
</svg>
<div class="figure-caption"><strong>Figure 3:</strong> Evidence-Based Future Research Agenda Separating Fluency, Trust, and Post-Purchase Regret Nodes (Propositions P1-P7).</div>
</div>

### 4.1. Curvilinear Personalization and Measurable Surveillance Reactance (P1, P1b)

Prior personalization-privacy paradox research demonstrates that covert or overly specific targeting triggers perceived vulnerability and reactance (Awad and Krishnan (2006); Aguirre et al. (2015); Xiao and Benbasat (2018)). In our core corpus, however, only 0.56% of impulse-buying studies model privacy reactance. Merging curvilinear personalization with explicit reactance mediation yields two falsifiable propositions:
* **Proposition 1 (P1):** Perceived algorithmic personalization exerts an inverted-U effect on **in-session cognitive fluency** (defined as immediate perceived ease of processing recommendation feeds), moderated by consumer privacy concern, algorithmic transparency, and perceived user control.
* **Proposition 1b (P1b):** **Surveillance reactance** (measured explicitly as perceived intrusive monitoring and autonomy threat) mediates the downward tail of the inverted-U personalization curve, reducing both in-session fluency and relational **algorithmic trust**.

### 4.2. Conversational AI Agency and Choice Velocity (P2, P3)

Rather than treating Generation 1.0 and 2.0 AI solely as chronological labels, future studies should operationalize continuous system parameters: conversational interactivity, anthropomorphic social cues, and response latency (Sundar and Kim (2019); Logg et al. (2019); Pang et al. (2026)).
* **Proposition 2 (P2):** Higher conversational interactivity and social presence in AI shopping assistants amplify affective arousal more strongly than static item-based carousels, conditional on user algorithm appreciation vs. aversion.
* **Proposition 3 (P3):** High-velocity algorithmic scarcity cues and recommendation choice volume elevate cognitive load, taxing executive deliberation during prolonged browsing sessions.

### 4.3. Separating Fluency, Trust, and Synergistic Interaction (P4, P5b)

To resolve conceptual conflation between immediate ease and cumulative satisfaction, future models should separate **in-session cognitive fluency** (first-visit cold-start mechanism) from **relational trust** (cross-session credibility) and **post-purchase satisfaction**. Furthermore, dual-process self-regulation literature suggests two competing predictions for how cognition and affect combine: a *hot/cool override hypothesis* (visceral arousal overrides cognitive evaluation, implying a negative interaction $b_3 < 0$) versus a *synergistic permission hypothesis* (cognitive fluency disarms analytical vigilance when arousal is high, implying a positive interaction $b_3 > 0$).
* **Proposition 4 (P4):** In-session cognitive fluency and algorithmic trust exert distinct positive effects on the urge to buy impulsively (UBI), with fluency dominating novel cold-start sessions and trust dominating repeat platform visits.
* **Proposition 5b (P5b):** In-session fluency/trust and affective arousal interact to shape UBI ($UBI = b_1 \text{Fluency} + b_2 \text{Arousal} + b_3 (\text{Fluency} \times \text{Arousal})$); future experiments should explicitly adjudicate between synergistic amplification ($b_3 > 0$) and hot/cool override ($b_3 < 0$).

### 4.4. Candidate Self-Control Strain and Dynamic Regret Feedback (P6, P7)

Self-control failure and ego depletion have long been linked to impulsive spending (Baumeister (2002); Vohs and Faber (2007); Kaya et al. (2020)), with Vohs and Faber (2007) showing that resource depletion elevates both impulsive urges and buying volume. However, large-scale multilab replication efforts (Hagger et al. (2016)) report mixed effect sizes for classic ego-depletion tasks, prompting process and opportunity-cost reformulations. Future retail studies should therefore treat self-regulatory strain as a candidate mechanism tested via behavioral or cognitive-load manipulations rather than assuming universal trait depletion. Similarly, building on emerging temporal feedback studies (Tobon and Abril (2025); Siva Bala Kumaran and Shobhana (2026)), post-purchase regret should be modeled as an explicit measurable node using experience sampling (ESM) or platform return/refund logs rather than relying solely on 3-wave panel surveys.
* **Proposition 6 (P6):** Cognitive load and situational self-regulatory strain strengthen both the arousal-to-UBI link and the UBI-to-checkout link, an effect that should be cross-validated against opportunity-cost motivation controls.
* **Proposition 7 (P7):** When depletion-linked impulse purchases generate post-purchase regret (captured via ESM or product-return behavior), regret recursively lowers subsequent algorithmic trust and shifts the consumer's personalization-reactance threshold leftward in future sessions.

Table 5 maps every proposition in this agenda directly to its empirical status in the 179-article core corpus.

**Table 5: Proposition-to-Corpus Evidence Mapping ($N = 179$)**

| Proposition | Core Construct / Relationship | Corpus Support Status | Recommended Empirical Test |
| :--- | :--- | :--- | :--- |
| **P1 & P1b** | Inverted-U Personalization $\rightarrow$ Surveillance Reactance | Under-tested (0.56% / 0.56%) | Quadratic SEM / Polynomial RSA + privacy moderators |
| **P2 & P3** | Conversational AI & Scarcity $\rightarrow$ Arousal / Load | Growing (6.15%) | Randomized 2x2 lab/field experiments (Vineesh A R (2026), Monisha and Chellamuthu (2026)) |
| **P4 & P5b** | Fluency/Trust $\times$ Arousal $\rightarrow$ UBI | Unresolved (1.68%) | Latent Moderated Structural Equations (LMS) |
| **P6** | Self-Control Strain (Ego Depletion / Load) | Mixed (8.38%) | Dual-task cognitive load experiments (Trinh and Nguyen (2025), Zheng et al. (2025)) |
| **P7** | Regret $\rightarrow$ Future Trust & Reactance Shift | Nascent (4.47% longitudinal) | Experience Sampling (ESM) + platform return logs (Xilai et al. (2026), Cui (2026)) |

---

## 5. MANAGERIAL PROPOSITIONS, LIMITATIONS, AND CONCLUSION

### 5.1. Testable Design and Regulatory Propositions for Retail Platforms

While aggressive dark-pattern urgency and hyper-granular retargeting can lift short-term conversion, behavioral economics and legal scholarship warn that manipulative choice architectures erode consumer welfare and invite regulatory scrutiny (Mathur et al. (2019)). Under emerging governance frameworks such as the European Union Digital Services Act (DSA) and U.S. Federal Trade Commission (FTC) dark-pattern enforcement, platforms face growing tension between short-term gross merchandise value incentives and long-term trust preservation. Rather than prescribing unproven heuristics, we propose **calibrated ethical friction** (such as transparent recommendation explanations, optional cooling-off confirmations for high-regret discretionary baskets, and user-adjustable personalization controls) as testable interface interventions whose impact on net return rates and customer retention should be evaluated via randomized A/B field trials before platform-wide deployment.

### 5.2. Limitations and Methodological Safeguards

In accordance with PRISMA 2020 Item 23c (Page et al. (2021)), four limitations bound this review. First, excluding conference proceedings (`EC1`, $n = 50$) ensured peer-reviewed journal consistency across the 179-article core corpus, yet necessarily omitted computer-science recommender venues (such as ACM RecSys, SIGIR, and CHI) where algorithmic architectures often debut. Second, our full-corpus evidence coding relied on structured title and abstract fields alongside bibliographic metadata; studies reporting interaction or quadratic terms solely within supplementary tables may be conservatively undercounted. Third, restricting inclusion to English-language outlets may underrepresent non-English regional studies of livestreaming commerce. Fourth, because the 179-article corpus spans heterogeneous survey, experimental, and conceptual designs without uniform correlation matrices, statistical meta-analysis (MASEM) was not feasible; once experimental replication accumulates around P1, P5b, and P7, future meta-analytic structural equation modeling will be warranted.

### 5.3. Conclusion

By enforcing strict three-pillar eligibility screening ($N = 179$), archiving a transparent OSF screening log, verifying every foundational reference via Crossref, and triangulating three bibliometric methods with full-corpus evidence coding, this review establishes a reliable empirical baseline for AI-mediated impulse buying research. Separating immediate cognitive fluency from relational trust, elevating surveillance reactance and post-purchase regret to measurable constructs, and adjudicating competing interaction hypotheses offer a rigorous roadmap for next-generation digital retailing scholarship.

---

## REFERENCES

Abdelsalam, S., Salim, N., Alias, R. A., & Husain, O. (2020). Understanding Online Impulse Buying Behavior in Social Commerce: A Systematic Literature Review. *IEEE Access*, *8*, 89041-89058. https://doi.org/10.1109/access.2020.2993671
Abu, B., & Huaqiang, W. (2025). The Role of Algorithmic Ad Personalization in Driving Impulse Buying Behavior: Mediating Effects of Perceived Value and Moderating Personality Traits. *OALib*, *12*(08), 1-18. https://doi.org/10.4236/oalib.1113822
Adyantari, A., Nugraha, A. P., & Dharomesz, V. Y. (2025). Impulsive Buying Behavior in Live Streaming Shopping Mechanism: Do Fear of Missing Out Matter?. *Review of Management and Entrepreneurship*, *9*(1), 32-49. https://doi.org/10.37715/rme.v9i1.5125
Aguirre, E., Mahr, D., Grewal, D., de Ruyter, K., & Wetzels, M. (2015). Unraveling the Personalization Paradox: The Effect of Information Collection and Trust-Building Strategies on Online Advertisement Effectiveness. *Journal of Retailing*, *91*(1), 34-49. https://doi.org/10.1016/j.jretai.2014.09.005
Aishwariya, S., & Vidya, M. (2025). AI-Powered Personalization and Impulsive Buying: An S-O-R Model Approach to Post-Purchase Emotions in Fashion E-Commerce. *Journal of Management and Science*, *15*(2), 74-78. https://doi.org/10.26524/jms15.23
Ali, F., Janjua, Q. R., & Maqsood, H. (2025). The Rise of Live-Streaming E-Commerce: Analyzing Consumer Purchase Behavior and Brand Trust in Real-Time Shopping Events. *Journal of Management & Social Science*, *2*(1), 430-447. https://doi.org/10.63075/q0evzn78
Amin, A. (2025). Artificial intelligence in social media: a catalyst for impulse buying behavior?. *Young Consumers*, *26*(5), 765-785. https://doi.org/10.1108/yc-10-2024-2297
Ampadu, S., Jiang, Y., Debrah, E., Antwi, C. O., Amankwa, E., Gyamfi, S. A., ... Amoako, R. (2022). Online personalized recommended product quality and e-impulse buying: A conditional mediation analysis. *Journal of Retailing and Consumer Services*, *64*, 102789. https://doi.org/10.1016/j.jretconser.2021.102789
Anoop, T., & Rahman, Z. (2025). From brick and mortar to omnichannel: a mixed-method exploration of impulse buying research. *Journal of Consumer Marketing*, *42*(7), 963-979. https://doi.org/10.1108/jcm-01-2025-7538
Arachchi, H. D. M., & Samarasinghe, G. (2023). Impulse Purchase Intention in an AI-mediated Retail Environment: Extending the TAM with Attitudes Towards Technology and Innovativeness. *Global Business Review*. https://doi.org/10.1177/09721509231197721
Awad, N. F., & Krishnan, M. S. (2006). The Personalization Privacy Paradox: An Empirical Evaluation of Information Transparency and the Willingness to be Profiled Online for Personalization1. *MIS Quarterly*, *30*(1), 13-28. https://doi.org/10.2307/25148715
Azizah, I. N., & Indrawati, I. (2022). THE INFLUENCES OF FLASH SALE PROMOTION ON SHOPPING ENJOYMENT AND IMPULSE BUYING OF SHOPEE CONSUMERS INDONESIA. *Jurnal Ilmiah Manajemen Ekonomi & Akuntansi (MEA)*, *6*(3), 2055-2072. https://doi.org/10.31955/mea.v6i3.2394
Baumeister, R. F. (2002). Yielding to Temptation: Self‐Control Failure, Impulsive Purchasing, and Consumer Behavior. *Journal of Consumer Research*, *28*(4), 670-676. https://doi.org/10.1086/338209
Beatty, S. E., & Elizabeth Ferrell, M. (1998). Impulse buying: Modeling its precursors. *Journal of Retailing*, *74*(2), 169-191. https://doi.org/10.1016/S0022-4359(99)80092-X
Beikverdi, L., Sipilä, J., & Tarkiainen, A. (2023). Post‐purchase effects of impulse buying: A review and research agenda. *Journal of Consumer Behaviour*, *23*(3), 1512-1527. https://doi.org/10.1002/cb.2287
Beukeboom, C. J., & Pollmann, M. (2021). Partner phubbing: Why using your phone during interactions with your partner can be detrimental for your relationship. *Computers in Human Behavior*, *124*, 106932. https://doi.org/10.1016/j.chb.2021.106932
Chan, T. K., Cheung, C. M., & Lee, Z. W. (2017). The state of online impulse-buying research: A literature analysis. *Information & Management*, *54*(2), 204-217. https://doi.org/10.1016/j.im.2016.06.001
Chen, B., Wang, L., Rasool, H., & Wang, J. (2022). Research on the Impact of Marketing Strategy on Consumers’ Impulsive Purchase Behavior in Livestreaming E-commerce. *Frontiers in Psychology*, *13*, 905531-905531. https://doi.org/10.3389/fpsyg.2022.905531
Cui, N. (2026). Explaining and predicting consumer decision-making in E-commerce using an intelligent hybrid framework for impulsive and planned purchase behavior. *Scientific Reports*, *16*(1), 17040. https://doi.org/10.1038/s41598-026-47284-1
Dang, H. P., & Hoang, V. T. (2025). The Role of Streamer Characteristics and Social Presence in Driving Impulsive Buying Behavior: A Study in Live Commerce with Self-Efficacy as a Moderator. *Journal of Promotion Management*, *31*(6), 913-932. https://doi.org/10.1080/10496491.2025.2528749
Do Xuan Nguyen, T., & Nguyen, K. M. (2026). Demystifying how emotional and cognitive resonance to AI-driven content consistency sparks customer engagement and impulse buying in short-video E-commerce. *Journal of Retailing and Consumer Services*, *89*, 104646. https://doi.org/10.1016/j.jretconser.2025.104646
Donthu, N., Kumar, S., Mukherjee, D., Pandey, N., & Lim, W. M. (2021). How to conduct a bibliometric analysis: An overview and guidelines. *Journal of Business Research*, *133*, 285-296. https://doi.org/10.1016/j.jbusres.2021.04.070
Dwivedi, Y. K., Hughes, L., Ismagilova, E., Aarts, G., Coombs, C., Crick, T., ... Eirug, A. (2021). Artificial Intelligence (AI): Multidisciplinary perspectives on emerging challenges, opportunities, and agenda for research, practice and policy. *International Journal of Information Management*, *57*, 101994. https://doi.org/10.1016/j.ijinfomgt.2019.08.002
Feng, Z., Al Mamun, A., Masukujjaman, M., Wu, M., & Yang, Q. (2024). Impulse buying behavior during livestreaming: Moderating effects of scarcity persuasion and price perception. *Heliyon*, *10*(7), e28347. https://doi.org/10.1016/j.heliyon.2024.e28347
Firdausiah, R. A., Putra, B. N., & Salsabila, R. (2023). Impulsive Buying in Live Tiktok Shop: Exploring The Role of Telepresence, Enjoyment and Trust Among Generation Z. *JKBM (JURNAL KONSEP BISNIS DAN MANAJEMEN)*, *10*(1), 56-70. https://doi.org/10.31289/jkbm.v10i1.10456
Gallin, S., & Portes, A. (2024). Online shopping: How can algorithm performance expectancy enhance impulse buying?. *Journal of Retailing and Consumer Services*, *81*, 103988. https://doi.org/10.1016/j.jretconser.2024.103988
Gao, Y., & Liang, J. (2025). The Impact of AI-Powered Try-On Technology on Online Consumers’ Impulsive Buying Intention: The Moderating Role of Brand Trust. *Sustainability*, *17*(7), 2789. https://doi.org/10.3390/su17072789
George, A. M., & Rupa, R. S. (2025). Swipe, click, regret: an opinion on persuasive e-commerce and consumer autonomy. *Frontiers in Artificial Intelligence*, *8*, 1684841-1684841. https://doi.org/10.3389/frai.2025.1684841
Germonprez, M., Hovorka, D., & Gal, U. (2011). Secondary Design: A Case of Behavioral Design Science Research. *Journal of the Association for Information Systems*, *12*(10), 662-683. https://doi.org/10.17705/1jais.00278
Gong, X. Y., Yee, C. L., Lee, S. Y., Cao, E. Y., & Saif, A. N. M. (2024). Knowledge mapping of impulsive buying behavior research: a visual analysis using CiteSpace. *Humanities and Social Sciences Communications*, *11*(1), 967. https://doi.org/10.1057/s41599-024-03473-9
Gong, X., & Jiang, X. (2023). Understanding consumer impulse buying in livestreaming commerce: The product involvement perspective. *Frontiers in Psychology*, *14*, 1104349-1104349. https://doi.org/10.3389/fpsyg.2023.1104349
Guha, A., Grewal, D., Kopalle, P. K., Haenlein, M., Schneider, M. J., Jung, H., ... Hawkins, G. (2021). How artificial intelligence will affect the future of retailing. *Journal of Retailing*, *97*(1), 28-41. https://doi.org/10.1016/j.jretai.2021.01.005
Hagger, M. S., Chatzisarantis, N. L. D., Alberts, H., Anggono, C. O., Batailler, C., Birt, A. R., ... Bruyneel, S. (2016). A Multilab Preregistered Replication of the Ego-Depletion Effect. *Perspectives on Psychological Science*, *11*(4), 546-573. https://doi.org/10.1177/1745691616652873
Huang, Q., Dastane, O., Cham, T., & Cheah, J. (2024). Is ‘she’ more impulsive (to pleasure) than ‘him’ during livestream e-commerce shopping?. *Journal of Retailing and Consumer Services*, *78*, 103707. https://doi.org/10.1016/j.jretconser.2024.103707
Huo, C., Wang, X., Sadiq, M. W., & Pang, M. (2023). Exploring Factors Affecting Consumer’s Impulse Buying Behavior in Live-Streaming Shopping: An Interactive Research Based Upon SOR Model. *SAGE Open*, *13*(2). https://doi.org/10.1177/21582440231172678
Huu, K. N., Le, A. N., & Dong, P. N. (2023). A moderating – mediating model of the urge to buy impulsively in social commerce live-streaming. *Electronic Commerce Research and Applications*, *60*, 101286. https://doi.org/10.1016/j.elerap.2023.101286
Kathuria, A., & Bakshi, A. (2024). Influence of promotional factors on online impulse buying: exploring the mediating role of impulse buying tendency. *Current Psychology*, *43*(44), 34035-34051. https://doi.org/10.1007/s12144-024-06911-8
Kaya, B., Abubakar, A. M., Behravesh, E., Yildiz, H., & Mert, I. S. (2020). Antecedents of innovative performance: Findings from PLS-SEM and fuzzy sets (fsQCA). *Journal of Business Research*, *114*, 278-289. https://doi.org/10.1016/j.jbusres.2020.04.016
Kinasih, M. P., & Wuryandari, N. E. R. (2023). PENGARUH PRICE DISCOUNT, PRODUCT KNOWLEDGE, DAN TIME PRESSURE TERHADAP IMPULSE BUYING PADA FITUR SHOPEE LIVE. *Jurnal Ilmiah Multidisiplin*, *2*(05), 88-101. https://doi.org/10.56127/jukim.v2i05.940
Lestari, I., & Dalimunthe, H. (2023). Relationship of Online Promotions and Discounts on Impulse Buying: A Case Study of Matahari Binjai Supermall Consumers. *International Journal of Finance Economics and Business*, *2*(4), 322-328. https://doi.org/10.56225/ijfeb.v2i4.286
Lin, X. (2026). From scrolling to spending: Psychological mechanisms of AI-driven impulse buying in live-stream shopping. *Acta Psychologica*, *269*, 107594. https://doi.org/10.1016/j.actpsy.2026.107594
Liu, Y., Chang, X., Yang, S., Li, Z., & Wu, Y. (2024). “Pets make you spend more!” Impact of pet ownership on consumer purchase decisions. *Journal of Business Research*, *183*, 114838. https://doi.org/10.1016/j.jbusres.2024.114838
Liu, Y., Li, Q., Edu, T., Jozsa, L., & Negricea, I. C. (2020). Mobile shopping platform characteristics as consumer behavior determinants. *Asia Pacific Journal of Marketing and Logistics*, *32*(7), 1565-1587. https://doi.org/10.1108/apjml-05-2019-0308
Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes*, *151*, 90-103. https://doi.org/10.1016/j.obhdp.2018.12.005
Luo, X., Cheah, J., Lim, X., Ramayah, T., & Dwivedi, Y. K. (2024). Inducing shoppers’ impulsive buying tendency in live-streaming: integrating signaling theory with social exchange theory. *Internet Research*, *35*(1), 318-348. https://doi.org/10.1108/intr-04-2023-0260
Mariani, M. M., Perez‐Vega, R., & Wirtz, J. (2022). AI in marketing, consumer research and psychology: A systematic literature review and research agenda. *Psychology & Marketing*, *39*(4), 755-776. https://doi.org/10.1002/mar.21619
Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M., ... Narayanan, A. (2019). Dark Patterns at Scale. *Proceedings of the ACM on Human-Computer Interaction*, *3*(CSCW), 1-32. https://doi.org/10.1145/3359183
Mehrabian, A., & Russell, J. A. (1974). *An approach to environmental psychology*. MIT Press.
Miranda, S., Borges‐Tiago, M. T., Tiago, F., & Tu, X. (2024). To buy or not to buy? The impulse buying dilemma in livestream shopping. *Psychology and Marketing*, *41*(5), 989-1005. https://doi.org/10.1002/mar.21967
Moghddam, H. A., Mortimer, G., Ahmadi, H., & Sharif-Nia, H. (2025). How livestream engagement inspires tourist purchasing behaviour: A multi-study approach. *International Journal of Information Management*, *83*, 102903. https://doi.org/10.1016/j.ijinfomgt.2025.102903
Monisha, L., & Chellamuthu, S. (2026). How Does Perceived Social Presence Drive Impulse Buying Online? The Mediating Role of Flow Experience and Consumer Trust. *International Review of Management and Marketing*, *16*(2), 384-395. https://doi.org/10.32479/irmm.22091
Ngo, T. T. A., Nguyen, H. L. T., Mai, H. T. A., & Nguyen, H. P. (2025). Key determinants of online impulse buying behavior: A study from TikTok Shop users in Vietnam. *Acta Psychologica*, *260*, 105593-105593. https://doi.org/10.1016/j.actpsy.2025.105593
Nimisha, S. S., & Pandey, A. C. (2025). Ai-Driven Personalization Cues: Unraveling Consumer Impulsive Buying in E-Commerce. *Economic Sciences.*, *21*(02(S) August), 201-215. https://doi.org/10.69889/arkq5j81
Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... Brennan, S. E. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*, n71. https://doi.org/10.1136/bmj.n71
Pang, H., Wang, Y., Sun, M., & Wang, R. (2026). How artificial intelligence functionalities boost consumer benefit and impulse shopping? The significant role of responsive communication and conversational communication. *Computers in Human Behavior*, *181*, 108999. https://doi.org/10.1016/j.chb.2026.108999
Parihar, N. (2025). Consumer Behavior in Online Retailing: Factors, Trends and Implications in India. *International journal of research and scientific innovation*, *XII*(VI), 972-977. https://doi.org/10.51244/ijrsi.2025.12060077
Paul, J., & Rosado-Serrano, A. (2019). Gradual Internationalization vs Born-Global/International new venture models. *International Marketing Review*, *36*(6), 830-858. https://doi.org/10.1108/IMR-10-2018-0280
Pei, Y., Zhu, J., & Cao, J. (2025). Intergenerational Differences in Impulse Purchasing in Live E-Commerce: A Multi-Dimensional Mechanism of the ASEAN Cross-Border Market. *Journal of theoretical and applied electronic commerce research*, *20*(4), 268-268. https://doi.org/10.3390/jtaer20040268
Pham, A. D., Nguyen, H. N., Le, T. T., Nguyen, H. K., Khuat, H. T., Phan, H. T., ... Vu, H. T. (2024). Young consumers’ impulse buying tendency on social media: an empirical analysis in Vietnam in light of the LST theoretical perspective. *Young Consumers*, *27*(2), 185-206. https://doi.org/10.1108/yc-07-2023-1785
Prasetia, A. R., Hurriyati, R., & Dirgantari, P. D. (2025). The Effect of Live-Stream E-Branding on Impulse Buying Behavior with Parasocial Interaction as a Mediating Variable on Shopee Live. *Commercium Journal of Business and Management*, *4*(1), 41-60. https://doi.org/10.61978/commercium.v4i1.1176
Putra, A. A. J., Forijati, & Subagyo (2025). The influence of financial literacy, hedonism lifestyle, paylater, impulse buying through risk perception. *Multidisciplinary Science Journal*, *8*(5), 2026325-2026325. https://doi.org/10.31893/multiscience.2026325
Rafdinal, W., Hardiyanto, N., & Juniarti, C. (2025). Introducing the cognitive impulse model: a cognitive framework for impulse buying behavior in flash sale live streaming. *International Journal of Quality and Service Sciences*, *17*(4), 425-449. https://doi.org/10.1108/ijqss-07-2025-0161
Rook, D. W., & Fisher, R. J. (1995). Normative Influences on Impulsive Buying Behavior. *Journal of Consumer Research*, *22*(3), 305. https://doi.org/10.1086/209452
Saad, S. B., & Choura, F. (2022). Towards better interaction between salespeople and consumers: the role of virtual recommendation agent. *European Journal of Marketing*, *57*(3), 858-903. https://doi.org/10.1108/ejm-11-2021-0892
Shamim, K., & Misra, S. C. (2025). Leveraging AI to drive online impulse buying: a SOBC perspective. *International Journal of Retail & Distribution Management*, *53*(10-11), 1040-1056. https://doi.org/10.1108/ijrdm-07-2024-0334
Sholihah, D. R., Fathoni, M. A., Wulansari, A. S., Ananda, M. M., & Amalina, S. N. (2025). Understanding how intrinsic motivation influences female modest fashion online impulse buying: the mediating role of trust and attitude. *Journal of Islamic Marketing*, *16*(12), 3736-3758. https://doi.org/10.1108/jima-08-2024-0332
Siva Bala Kumaran, M., & Shobhana, N. (2026). The Persuasive Backfire of Generative AI: How Synthetic Urgency Fuels Impulse-Regret Responses and Return Intention in E-Commerce. *Journal of Promotion Management*, *32*(3), 307-321. https://doi.org/10.1080/10496491.2026.2669635
Song, M. (2023). The Impact of Algorithmic Product Recommendation on Consumers' Impulse Purchase Intention. *Frontiers in Business Economics and Management*, *11*(3), 107-111. https://doi.org/10.54097/fbem.v11i3.13197
Stewart, C. R., & Yap, S. (2020). Low literacy, policy and consumer vulnerability: Are we really doing enough?. *International Journal of Consumer Studies*, *44*(4), 343-352. https://doi.org/10.1111/ijcs.12569
Sundar, S. S., & Kim, J. (2019). Machine Heuristic. *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems*, 1-9. https://doi.org/10.1145/3290605.3300768
Tobon, S., & Abril, C. (2025). Game on: curbing impulse buying and returns in apparel e-tailers. *Review of Managerial Science*, *19*(6), 1783-1817. https://doi.org/10.1007/s11846-024-00808-3
Trinh, L. N., & Nguyen, T. V. (2025). Online Impulse Buying Behavior Among University Students: An Empirical Study at East Asia University of Technology. *World Journal of Advanced Research and Reviews*, *27*(1), 2388-2400. https://doi.org/10.30574/wjarr.2025.27.1.2749
Verhagen, T., & van Dolen, W. (2011). The influence of online store beliefs on consumer online impulse buying: A model and empirical application. *Information & Management*, *48*(8), 320-327. https://doi.org/10.1016/j.im.2011.08.001
Vineesh A R, M. R. K. R. R. S. (2026). Role of AI Recommendation on Consumer Behavior. *International Journal of Advanced Research in Science Communication and Technology*, 743. https://doi.org/10.48175/ijarsct-30755
Vohs, K. D., & Faber, R. J. (2007). Spent Resources: Self‐Regulatory Resource Availability Affects Impulse Buying. *Journal of Consumer Research*, *33*(4), 537-547. https://doi.org/10.1086/510228
Wang, L., Jing, Z., Li, H., Li, C., & Su, Y. (2025). The Influence of AI-Driven Personalization in Social Media Marketing on Consumer Purchase Decisions and Behavior. *International Journal of Accounting and Economics Studies*, *12*(5), 438-444. https://doi.org/10.14419/dcggbj32
Wang, L., Zhang, G., & Jiang, D. (2024). Encountering Product Information: How Flashes of Insight Improve Your Decisions on E-Commerce Platforms. *Journal of Theoretical and Applied Electronic Commerce Research*, *19*(3), 2180-2197. https://doi.org/10.3390/jtaer19030106
Wang, M., Zhang, W., & Li, Y. (2026). Narrative strategies in live-streaming commerce: host storytelling, immersion, and impulse buying. *Frontiers in Psychology*, *17*, 1746938-1746938. https://doi.org/10.3389/fpsyg.2026.1746938
Widjaja, A., Benjaminsz, C. A., Susanto, D. F., & Hendriana, E. (2025). Distinguishing the Effects of a Social Presence on Impulsive Buying Behavior Based on live-Streaming Shopping Platforms. *Journal of Organizational Computing and Electronic Commerce*, *36*(1), 31-61. https://doi.org/10.1080/10919392.2025.2529068
Xia, Y. X., Chae, S. W., & Xiang, Y. C. (2024). How social and media cues induce live streaming impulse buying? SOR model perspective. *Frontiers in Psychology*, *15*, 1379992. https://doi.org/10.3389/fpsyg.2024.1379992
Xiao, B., & Benbasat, I. (2007). E-Commerce Product Recommendation Agents: Use, Characteristics, and Impact1. *MIS Quarterly*, *31*(1), 137-209. https://doi.org/10.2307/25148784
Xiao, B., & Benbasat, I. (2018). An empirical examination of the influence of biased personalized product recommendations on consumers' decision making outcomes. *Decision Support Systems*, *110*, 46-57. https://doi.org/10.1016/j.dss.2018.03.005
Xilai, Q., Bashir, T., Naseem, A., Gul, R. F., & Sadiq, B. (2026). A dual-process psychological model of impulse buying in digital commerce: evidence from livestream and marketplace contexts. *Frontiers in Psychology*, *17*, 1774474. https://doi.org/10.3389/fpsyg.2026.1774474
Xin, M., Jian, L., Liu, W., & Bao, Y. (2025). Exploring the Effect of Live Streaming Atmospheric Cues on Consumer Impulse Buying: A Flow Experience Perspective. *Journal of Theoretical and Applied Electronic Commerce Research*, *20*(2), 149. https://doi.org/10.3390/jtaer20020149
Yang, J., Cao, C., Ye, C., & Shi, Y. (2022). Effects of Interface Design and Live Atmosphere on Consumers’ Impulse-Buying Behaviour from the Perspective of Human–Computer Interaction. *Sustainability*, *14*(12), 7110-7110. https://doi.org/10.3390/su14127110
Zhang, W., Leng, X., & Liu, S. (2020). RETRACTED ARTICLE: Research on mobile impulse purchase intention in the perspective of system users during COVID-19. *Personal and Ubiquitous Computing*, *27*(3), 665-673. https://doi.org/10.1007/s00779-020-01460-w
Zhang, X., & Zhang, S. (2024). Investigating impulse purchases in live streaming e-commerce: A perspective of match-ups. *Technological Forecasting and Social Change*, *205*, 123513. https://doi.org/10.1016/j.techfore.2024.123513
Zhang, X., Shi, Y., Li, T. (., Guan, Y., & Cui, X. (2023). How Do Virtual AI Streamers Influence Viewers’ Livestream Shopping Behavior? The Effects of Persuasive Factors and the Mediating Role of Arousal. *Information Systems Frontiers*, *26*(5), 1803-1834. https://doi.org/10.1007/s10796-023-10425-2
Zhang, Y., Fu, S., & Yan, X. (2026). From rational depletion to impulsive decision: A multi-information source perspective in social livestreaming e-commerce. *Journal of Retailing and Consumer Services*, *88*, 104518. https://doi.org/10.1016/j.jretconser.2025.104518
Zheng, L., Xiao, Z., & Zhang, W. (2025). The Impact of Negative Bullet Comments on Audiences’ Impulse Buying Intention in Fashion Livestreaming. *Journal of theoretical and applied electronic commerce research*, *21*(1), 1-1. https://doi.org/10.3390/jtaer21010001
Zheng, X., Men, J., Yang, F., & Gong, X. (2019). Understanding impulse buying in mobile commerce: An investigation into hedonic and utilitarian browsing. *International Journal of Information Management*, *48*, 151-160. https://doi.org/10.1016/j.ijinfomgt.2019.02.010
Zhu, Y., Shi, H., Bin Azam Hashmi, H., & Wu, Q. (2023). Bridging artificial intelligence-based services and online impulse buying in E-retailing context. *Electronic Commerce Research and Applications*, *62*, 101333. https://doi.org/10.1016/j.elerap.2023.101333
