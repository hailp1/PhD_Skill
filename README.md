# AI-Driven Personalized Recommendation Systems and Online Consumer Impulse Buying Behavior
*(Tác động của Hệ thống Đề xuất Cá nhân hóa Dựa trên AI đến Hành vi Mua Bốc đồng của Người Tiêu dùng Trực tuyến)*

<p align="center">
  <a href="https://osf.io/w2apx/"><img src="https://img.shields.io/badge/OSF%20Preregistration-10.17605%2FOSF.IO%2FW2APX-blue?style=for-the-badge&logo=osf" alt="OSF Preregistration"></a>
  <a href="https://www.sciencedirect.com/journal/journal-of-retailing-and-consumer-services"><img src="https://img.shields.io/badge/Target%20Journal-JRCS%20(Elsevier%20Q1%20--%20IF%2011.0)-darkgreen?style=for-the-badge" alt="Target Journal"></a>
  <a href="http://prisma-statement.org/"><img src="https://img.shields.io/badge/Protocol-PRISMA%202020%20Statement-emerald?style=for-the-badge" alt="PRISMA 2020"></a>
  <a href="https://www.vosviewer.com/"><img src="https://img.shields.io/badge/Bibliometrics-VOSviewer%20v1.6.20-red?style=for-the-badge" alt="VOSviewer"></a>
  <a href="https://github.com/hailp1/PhD_Skill/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-CC--BY%204.0-lightgrey?style=for-the-badge" alt="License"></a>
  <a href="https://hailp1.github.io/PhD_Skill/"><img src="https://img.shields.io/badge/Live%20Dashboard-GitHub%20Pages-purple?style=for-the-badge" alt="Live Demo"></a>
</p>

---

## 📖 OVERVIEW & EXECUTIVE SUMMARY

This repository hosts the complete, reproducible computational research ecosystem, empirical datasets, and interactive visualization platforms for the Ph.D. dissertation:

* **Dissertation Title**: *AI-Driven Personalized Recommendation Systems and Online Consumer Impulse Buying Behavior: The Mediating Role of Cumulative E-Satisfaction and the Boundary Condition of Ego Depletion*
* **Researcher**: **Le Phuc Hai (Lê Phúc Hải)** | Ph.D. Candidate in Marketing & Business Administration
* **Institution**: **Ton Duc Thang University (TDTU)**, Ho Chi Minh City, Vietnam
* **OSF Study Protocol**: Registered under code **`w2apx`** ([https://osf.io/w2apx/](https://osf.io/w2apx/))
* **Target Venue for Paper 1**: *Journal of Retailing and Consumer Services* (Elsevier, CiteScore: 19.3, Impact Factor: 11.0, ABS 3*, Scopus Q1)

---

## 🔬 THREE PILLARS OF EMPIRICAL RIGOR

```
┌───────────────────────────────────────┐
│     Stage 1: Systematic Review        │  ---> N = 2,500 initial records (Scopus/WoS/Dimensions)
│        (PRISMA 2020 Protocol)         │  ---> N = 1,441 core studies included post-screening
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│     Stage 2: Bibliometric Network     │  ---> Fractional counting, Modularity-based clustering
│      (VOSviewer Software v1.6.20)     │  ---> 4 Thematic Clusters, 28 key nodes, 250 links
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│    Stage 3: Conceptual S-O-R Model    │  ---> Stimulus (PP, ACC, NOV) -> Organism (ES) -> Response (UBI -> IB)
│    (Baumeister Ego Depletion Theory)  │  ---> 6 Hypotheses (H1-H6) with moderation & serial mediation
└───────────────────────────────────────┘
```

---

## 📊 CORE SCIENTIFIC ARTIFACTS & FIGURES

### 1. PRISMA 2020 Flow Diagram (Screening Trajectory)
*Identifies the systematic selection funnel from 2,500 raw bibliographic citations down to 1,441 high-impact peer-reviewed studies.*
* **Vector Asset**: [lab_projects/figures/figure1_prisma_flow_diagram.svg](lab_projects/figures/figure1_prisma_flow_diagram.svg)

### 2. Empirical VOSviewer Co-Occurrence Network Map
*Direct WebGL capture from VOSviewer Online displaying 4 clusters, 28 high-frequency constructs, and 250 co-occurrence link paths.*
* **High-Res Asset**: [lab_projects/figures/figure2_vosviewer_real_network.png](lab_projects/figures/figure2_vosviewer_real_network.png)
* **Interactive Live Web App**: [Click to open VOSviewer directly on Port 8600](http://localhost:8600/?json=data/luan_an_real_network.json)

### 3. Integrative Conceptual Framework (S-O-R & Ego Depletion)
*Synthesizes algorithmic cues into internal cognitive-affective evaluations and behavioral checkout enactment.*
* **Vector Asset**: [lab_projects/figures/figure3_theoretical_sor_model.svg](lab_projects/figures/figure3_theoretical_sor_model.svg)

---

## 🏛️ REPOSITORY ARCHITECTURE

```text
khoahoc/
├── .github/workflows/                 # CI/CD: Automated deployment to GitHub Pages
│   └── deploy-pages.yml               # Deploys web/ dashboard on every git push
│
├── .agents/skills/                    # Ph.D. Internal AI Research Advisory Skills Suite
│   ├── phd-research-proposal/         # Gap identification, RQs, theoretical frameworks
│   ├── phd-literature-review/         # PRISMA 2020, citation verification, matrix synthesis
│   ├── phd-methodology-design/        # Back-translation, construct operationalization, scales
│   ├── phd-data-analysis/             # PLS-SEM/CB-SEM, Common Method Bias (CMB) control
│   └── phd-dissertation-writing/      # 5-chapter dissertation drafting & anti-AI tone audit
│
├── data/                              # Research Data Management (FAIR Principles)
│   ├── raw/                           # Raw bibliographic datasets (Dimensions, Scopus, WoS)
│   ├── processed/                     # Clean corpus (N = 1,441 core studies, 100% DOI-verified)
│   └── vosviewer/                     # Coordinate maps and network files for VOSviewer
│       └── luan_an_real_network.json  # 28 nodes, 250 links, 4 clusters
│
├── lab_projects/                      # Manuscript Drafting & Production Assets
│   ├── figures/                       # Vector SVGs & 300 DPI publication graphics
│   ├── PAPER_01_SLR_JRCS_MANUSCRIPT.md# 100% Academic English submission manuscript
│   └── MASTER_LITERATURE_LIBRARY.bib  # Master BibTeX reference bibliography
│
├── lab_management/                    # Computational Automation & Verification Pipeline
│   ├── capture_vosviewer_screenshot.py# Automated Headless Chrome WebGL snapshot engine
│   ├── generate_academic_figures.py   # Publication-grade vector figure generator
│   └── update_pdf_engine.py           # A4 PDF layout engine with anti-slicing rules
│
├── web/                               # Interactive HTML5/SPA Science Dashboard (GitHub Pages)
│   ├── index.html                     # Unified research command dashboard
│   ├── interactive_science_map.html   # Canvas VOSviewer with 300 DPI & SVG export
│   └── XEM_BAN_THAO_BAI_BAO.html      # High-fidelity Elsevier A4 manuscript reader
│
├── CITATION.cff                       # Citation metadata for automatic GitHub citing
├── GEMINI.md                          # Doctoral dissertation advisory system rules
├── start_vosviewer_online.bat         # 1-click launcher for VOSviewer Online (Port 8600)
└── README.md                          # Master repository documentation
```

---

## 🚀 HOW TO REPRODUCE THIS RESEARCH

### Step 1: Clone the Repository
```bash
git clone https://github.com/hailp1/PhD_Skill.git
cd PhD_Skill
```

### Step 2: Launch the Interactive Science Dashboard
* Double-click `start_vosviewer_online.bat` to launch local VOSviewer Online (Port 8600).
* Open `XEM_BAN_THAO_BAI_BAO.html` in your browser to inspect the full-text manuscript, vector flowcharts, and 1-click A4 PDF export.

### Step 3: Verify Scholarly Citations (Anti-Hallucination Gate)
Run the automated Crossref API verification tool to validate DOI integrity across all cited publications:
```bash
python .agents/skills/phd-literature-review/scripts/citation_verifier.py
```

---

## 📜 CITATION & ATTRIBUTION

If you utilize this protocol, empirical network map, or conceptual framework in your research, please cite:

```bibtex
@misc{le2026aidriven,
  author       = {Le, Phuc Hai},
  title        = {AI-Driven Personalized Recommendation Systems and Online Consumer Impulse Buying Behavior: A Systematic Literature Review and Bibliometric Network Analysis},
  year         = {2026},
  publisher    = {Open Science Framework (OSF)},
  doi          = {10.17605/OSF.IO/W2APX},
  url          = {https://osf.io/w2apx/},
  note         = {Ph.D. Dissertation Research, Ton Duc Thang University (TDTU)}
}
```

---

## ⚖️ LICENSE
* **Academic Manuscript, Figures & Datasets**: Licensed under [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
* **Software Scripts & Pipeline Automation**: Licensed under the [MIT License](LICENSE).
