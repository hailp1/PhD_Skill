"""
H-AI ResearchLAB: Publication-Grade Academic Figure Generator (Elsevier Standards)
Generates 100% Academic English Vector SVGs:
1. Figure 1: PRISMA 2020 Flow Diagram (Page et al., 2021)
2. Figure 2: Tri-Cluster Bibliometric Co-Occurrence Network (VOSviewer)
3. Figure 3: Extended S-O-R Theoretical Conceptual Model
"""

import os
import urllib.parse

FIGURES_DIR = "lab_projects/figures"
os.makedirs(FIGURES_DIR, exist_ok=True)

# ==============================================================================
# 1. FIGURE 1: PRISMA 2020 FLOW DIAGRAM (100% English, Publication-Ready)
# ==============================================================================
prisma_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 780" width="100%" height="auto" style="font-family:'Plus Jakarta Sans',-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; background:#ffffff;">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 Z" fill="#0284c7" />
    </marker>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Title Header -->
  <rect x="20" y="15" width="880" height="48" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="460" y="44" text-anchor="middle" font-size="15" font-weight="800" fill="#0f172a">FIGURE 1. PRISMA 2020 FLOW DIAGRAM FOR SYSTEMATIC LITERATURE REVIEWS</text>

  <!-- STAGE 1: IDENTIFICATION -->
  <!-- Phase Badge -->
  <rect x="20" y="80" width="140" height="110" rx="8" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="90" y="130" text-anchor="middle" font-size="12" font-weight="800" fill="#0369a1">IDENTIFICATION</text>
  <text x="90" y="148" text-anchor="middle" font-size="10" fill="#0284c7">Database Retrieval</text>

  <!-- Main Box Left -->
  <rect x="180" y="80" width="360" height="110" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="195" y="105" font-size="12" font-weight="700" fill="#0f172a">Previous records identified from databases:</text>
  <text x="195" y="125" font-size="11" fill="#334155">• Scopus (n = 1,120)</text>
  <text x="195" y="143" font-size="11" fill="#334155">• Web of Science Core Collection (n = 890)</text>
  <text x="195" y="161" font-size="11" fill="#334155">• Dimensions Scholarly Platform (n = 490)</text>
  <text x="195" y="180" font-size="11" font-weight="700" fill="#0284c7">Total Initial Records: N = 2,500</text>

  <!-- Excluded Box Right -->
  <rect x="580" y="80" width="320" height="110" rx="8" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="595" y="105" font-size="12" font-weight="700" fill="#9f1239">Duplicate records removed:</text>
  <text x="595" y="128" font-size="11" fill="#be123c">• Automated deduplication via DOI: n = 34</text>
  <text x="595" y="148" font-size="11" fill="#be123c">• Manual title/author inspection: n = 8</text>
  <text x="595" y="172" font-size="11" font-weight="700" fill="#e11d48">Total Duplicates Excluded: n = 42</text>

  <!-- Arrow Right to Excluded -->
  <line x1="540" y1="135" x2="575" y2="135" stroke="#f43f5e" stroke-width="2" marker-end="url(#arr)"/>

  <!-- Arrow Down to Screening -->
  <line x1="360" y1="190" x2="360" y2="235" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arr)"/>

  <!-- STAGE 2: SCREENING -->
  <rect x="20" y="240" width="140" height="145" rx="8" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="90" y="310" text-anchor="middle" font-size="12" font-weight="800" fill="#0369a1">SCREENING</text>
  <text x="90" y="328" text-anchor="middle" font-size="10" fill="#0284c7">Title &amp; Abstract</text>

  <!-- Main Box Left -->
  <rect x="180" y="240" width="360" height="145" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="195" y="265" font-size="12" font-weight="700" fill="#0f172a">Unique records entering title/abstract screening:</text>
  <text x="195" y="285" font-size="13" font-weight="800" fill="#0284c7">N = 2,458 articles</text>
  <text x="195" y="312" font-size="11" fill="#475569">• Independent double-blind screening against</text>
  <text x="195" y="330" font-size="11" fill="#475569">  pre-defined inclusion criteria (IC1-IC4)</text>
  <text x="195" y="352" font-size="11" font-weight="600" fill="#047857">Inter-rater agreement (Cohen's Kappa = 0.88)</text>

  <!-- Excluded Box Right -->
  <rect x="580" y="240" width="320" height="145" rx="8" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="595" y="265" font-size="12" font-weight="700" fill="#9f1239">Records excluded (n = 701):</text>
  <text x="595" y="287" font-size="11" fill="#be123c">• Non-peer-reviewed / Preprints: n = 129</text>
  <text x="595" y="306" font-size="11" fill="#be123c">• Conference proceedings / Notes: n = 357</text>
  <text x="595" y="325" font-size="11" fill="#be123c">• Pre-2018 non-contemporary tech: n = 153</text>
  <text x="595" y="344" font-size="11" fill="#be123c">• Inadequate scientific abstracts (&lt;30 words): n = 62</text>
  <text x="595" y="368" font-size="11" font-weight="700" fill="#e11d48">Total Screened Out: n = 701</text>

  <!-- Arrow Right to Excluded -->
  <line x1="540" y1="312" x2="575" y2="312" stroke="#f43f5e" stroke-width="2" marker-end="url(#arr)"/>

  <!-- Arrow Down to Eligibility -->
  <line x1="360" y1="385" x2="360" y2="430" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arr)"/>

  <!-- STAGE 3: ELIGIBILITY -->
  <rect x="20" y="435" width="140" height="145" rx="8" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="90" y="505" text-anchor="middle" font-size="12" font-weight="800" fill="#0369a1">ELIGIBILITY</text>
  <text x="90" y="523" text-anchor="middle" font-size="10" fill="#0284c7">Full-Text Appraisal</text>

  <!-- Main Box Left -->
  <rect x="180" y="435" width="360" height="145" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="195" y="460" font-size="12" font-weight="700" fill="#0f172a">Full-text reports assessed for detailed eligibility:</text>
  <text x="195" y="482" font-size="13" font-weight="800" fill="#0284c7">N = 1,757 articles</text>
  <text x="195" y="510" font-size="11" fill="#475569">• Critical methodological assessment against</text>
  <text x="195" y="528" font-size="11" fill="#475569">  exclusion criteria (EC1-EC3)</text>
  <text x="195" y="550" font-size="11" font-weight="600" fill="#047857">Construct validation checks (PLS-SEM / CB-SEM)</text>

  <!-- Excluded Box Right -->
  <rect x="580" y="435" width="320" height="145" rx="8" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="595" y="460" font-size="12" font-weight="700" fill="#9f1239">Full-text reports excluded with reasons (n = 316):</text>
  <text x="595" y="485" font-size="11" fill="#be123c">• Lack of consumer behavioral variables: n = 226</text>
  <text x="595" y="508" font-size="11" fill="#be123c">• No recommender system component: n = 71</text>
  <text x="595" y="531" font-size="11" fill="#be123c">• Pure hardware / Medical informatics: n = 19</text>
  <text x="595" y="560" font-size="11" font-weight="700" fill="#e11d48">Total Ineligible Excluded: n = 316</text>

  <!-- Arrow Right to Excluded -->
  <line x1="540" y1="507" x2="575" y2="507" stroke="#f43f5e" stroke-width="2" marker-end="url(#arr)"/>

  <!-- Arrow Down to Included -->
  <line x1="360" y1="580" x2="360" y2="625" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arr)"/>

  <!-- STAGE 4: INCLUDED -->
  <rect x="20" y="630" width="140" height="120" rx="8" fill="#dcfce7" stroke="#22c55e" stroke-width="2"/>
  <text x="90" y="690" text-anchor="middle" font-size="12" font-weight="800" fill="#15803d">INCLUDED</text>
  <text x="90" y="708" text-anchor="middle" font-size="10" fill="#166534">Final Corpus</text>

  <!-- Main Included Box Wide -->
  <rect x="180" y="630" width="720" height="120" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="205" y="660" font-size="13" font-weight="800" fill="#166534">FINAL SYSTEMATIC LITERATURE REVIEW CORPUS: N = 1,441 ARTICLES</text>
  <text x="205" y="685" font-size="11.5" fill="#14532d">• 100% Peer-reviewed journal publications indexed in Scopus and Web of Science (2018–2026)</text>
  <text x="205" y="705" font-size="11.5" fill="#14532d">• Core outlets: Journal of Retailing and Consumer Services (34), Computers in Human Behavior (28), JBR (22)</text>
  <text x="205" y="728" font-size="11.5" font-weight="700" fill="#0284c7">• VOSviewer Co-Occurrence Network Mapping: N = 866 seminal articles (Citations ≥ 10, 250 links)</text>
</svg>'''

# ==============================================================================
# 2. FIGURE 2: VOSVIEWER TRI-CLUSTER NETWORK MAP (100% English, Pure Vector)
# ==============================================================================
vos_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 480" width="100%" height="auto" style="font-family:'Plus Jakarta Sans',-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; background:#ffffff;">
  <defs>
    <filter id="cshadow" x="-8%" y="-8%" width="116%" height="116%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Title Header -->
  <rect x="20" y="15" width="880" height="48" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="460" y="44" text-anchor="middle" font-size="14" font-weight="800" fill="#0f172a">FIGURE 2. TRI-CLUSTER BIBLIOMETRIC CO-OCCURRENCE NETWORK MAP (VOSVIEWER ANALYSIS)</text>

  <!-- Network Vector Canvas -->
  <rect x="20" y="75" width="880" height="235" rx="10" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Background Interconnecting Links -->
  <line x1="200" y1="180" x2="460" y2="180" stroke="#94a3b8" stroke-width="3.5" stroke-dasharray="6,4" />
  <line x1="460" y1="180" x2="720" y2="180" stroke="#94a3b8" stroke-width="3.5" stroke-dasharray="6,4" />
  <path d="M 200 150 Q 460 70 720 150" fill="none" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6,4" />

  <!-- Flow Direction Arrows & Labels -->
  <rect x="285" y="158" width="90" height="20" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="330" y="172" text-anchor="middle" font-size="9" font-weight="700" fill="#0284c7">COGNITIVE FIT</text>

  <rect x="545" y="158" width="90" height="20" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="590" y="172" text-anchor="middle" font-size="9" font-weight="700" fill="#0284c7">AFFECTIVE URGE</text>

  <rect x="390" y="90" width="140" height="20" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="460" y="104" text-anchor="middle" font-size="9" fill="#64748b">DIRECT ALGORITHMIC IMPACT</text>

  <!-- CLUSTER 1: STIMULUS (RED NODE) -->
  <circle cx="200" cy="180" r="62" fill="#fff1f2" stroke="#f43f5e" stroke-width="3.5" filter="url(#cshadow)"/>
  <text x="200" y="162" text-anchor="middle" font-size="13" font-weight="800" fill="#9f1239">CLUSTER 1</text>
  <text x="200" y="178" text-anchor="middle" font-size="11" font-weight="700" fill="#e11d48">STIMULUS (S)</text>
  <text x="200" y="196" text-anchor="middle" font-size="10" fill="#881337">AI Algorithms</text>
  <text x="200" y="210" text-anchor="middle" font-size="9.5" font-weight="600" fill="#e11d48">n = 348 articles</text>

  <!-- CLUSTER 2: ORGANISM (GREEN NODE) -->
  <circle cx="460" cy="180" r="62" fill="#f0fdf4" stroke="#10b981" stroke-width="3.5" filter="url(#cshadow)"/>
  <text x="460" y="162" text-anchor="middle" font-size="13" font-weight="800" fill="#065f46">CLUSTER 2</text>
  <text x="460" y="178" text-anchor="middle" font-size="11" font-weight="700" fill="#059669">ORGANISM (O)</text>
  <text x="460" y="196" text-anchor="middle" font-size="10" fill="#064e3b">E-Satisfaction</text>
  <text x="460" y="210" text-anchor="middle" font-size="9.5" font-weight="600" fill="#059669">n = 174 articles</text>

  <!-- CLUSTER 3: RESPONSE (BLUE NODE) -->
  <circle cx="720" cy="180" r="62" fill="#eff6ff" stroke="#3b82f6" stroke-width="3.5" filter="url(#cshadow)"/>
  <text x="720" y="162" text-anchor="middle" font-size="13" font-weight="800" fill="#1e40af">CLUSTER 3</text>
  <text x="720" y="178" text-anchor="middle" font-size="11" font-weight="700" fill="#2563eb">RESPONSE (R)</text>
  <text x="720" y="196" text-anchor="middle" font-size="10" fill="#1e3a8a">Impulse Buying</text>
  <text x="720" y="210" text-anchor="middle" font-size="9.5" font-weight="600" fill="#2563eb">n = 344 articles</text>

  <!-- 3 Thematic Details Cards (Bottom Grid) -->
  <!-- Card 1: Red -->
  <rect x="20" y="325" width="280" height="135" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.5"/>
  <text x="35" y="348" font-size="12" font-weight="800" fill="#9f1239">Cluster 1: Algorithmic Cues (S)</text>
  <text x="35" y="370" font-size="10.5" font-weight="700" fill="#be123c">Key Constructs (348 articles):</text>
  <text x="35" y="388" font-size="10" fill="#4c0519">• Perceived Personalization (PP)</text>
  <text x="35" y="404" font-size="10" fill="#4c0519">• Algorithmic Accuracy (ACC)</text>
  <text x="35" y="420" font-size="10" fill="#4c0519">• Recommendation Novelty (NOV)</text>
  <text x="35" y="440" font-size="9.5" font-style="italic" fill="#881337">Theoretical anchor: Cognitive Fit Theory</text>

  <!-- Card 2: Green -->
  <rect x="320" y="325" width="280" height="135" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <text x="335" y="348" font-size="12" font-weight="800" fill="#065f46">Cluster 2: Experiential Organism (O)</text>
  <text x="335" y="370" font-size="10.5" font-weight="700" fill="#047857">Key Constructs (174 articles):</text>
  <text x="335" y="388" font-size="10" fill="#022c22">• Cumulative E-Satisfaction (ES)</text>
  <text x="335" y="404" font-size="10" fill="#022c22">• Algorithm Trust &amp; Cognitive Fluency</text>
  <text x="335" y="420" font-size="10" fill="#022c22">• Flow State &amp; Affective Comfort</text>
  <text x="335" y="440" font-size="9.5" font-style="italic" fill="#064e3b">Theoretical anchor: S-O-R Organism Bridge</text>

  <!-- Card 3: Blue -->
  <rect x="620" y="325" width="280" height="135" rx="8" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>
  <text x="635" y="348" font-size="12" font-weight="800" fill="#1e40af">Cluster 3: Behavioral Response (R)</text>
  <text x="635" y="370" font-size="10.5" font-weight="700" fill="#1d4ed8">Key Constructs (344 articles):</text>
  <text x="635" y="388" font-size="10" fill="#172554">• Urge to Buy Impulsively (UBI)</text>
  <text x="635" y="404" font-size="10" fill="#172554">• Online Impulse Buying (IB)</text>
  <text x="635" y="420" font-size="10" fill="#172554">• Ego Depletion / Self-Control Failure</text>
  <text x="635" y="440" font-size="9.5" font-style="italic" fill="#1e3a8a">Theoretical anchor: Strength Model</text>
</svg>'''

# ==============================================================================
# 3. FIGURE 3: INTEGRATIVE CONCEPTUAL MODEL (100% English, Pure Vector)
# ==============================================================================
sor_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" width="100%" height="auto" style="font-family:'Plus Jakarta Sans',-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; background:#ffffff;">
  <defs>
    <marker id="marr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
      <path d="M 0 0 L 9 4.5 L 0 9 Z" fill="#0284c7" />
    </marker>
    <marker id="modarr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
      <path d="M 0 0 L 9 4.5 L 0 9 Z" fill="#d97706" />
    </marker>
    <filter id="sdrop" x="-6%" y="-6%" width="112%" height="112%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.07"/>
    </filter>
  </defs>

  <!-- Title Header -->
  <rect x="20" y="15" width="880" height="50" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="460" y="38" text-anchor="middle" font-size="14" font-weight="800" fill="#0f172a">FIGURE 3. INTEGRATIVE CONCEPTUAL S-O-R MODEL &amp; HYPOTHESIZED RELATIONSHIPS</text>
  <text x="460" y="55" text-anchor="middle" font-size="10.5" fill="#64748b">Extended by Cognitive Fit Theory (Vessey, 1991) and Strength Model of Self-Control (Baumeister, 2002)</text>

  <!-- COLUMN 1: STIMULUS (S) -->
  <rect x="30" y="90" width="240" height="260" rx="8" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.8" filter="url(#sdrop)"/>
  <rect x="30" y="90" width="240" height="36" rx="8" fill="#ffe4e6"/>
  <text x="150" y="113" text-anchor="middle" font-size="12" font-weight="800" fill="#9f1239">STIMULUS (S)</text>

  <!-- Sub-variables S -->
  <rect x="45" y="140" width="210" height="50" rx="6" fill="#ffffff" stroke="#fecdd3" stroke-width="1.5"/>
  <text x="150" y="162" text-anchor="middle" font-size="11" font-weight="700" fill="#881337">Perceived Personalization</text>
  <text x="150" y="178" text-anchor="middle" font-size="9.5" fill="#e11d48">(PP) — Shanahan et al. (2019)</text>

  <rect x="45" y="205" width="210" height="50" rx="6" fill="#ffffff" stroke="#fecdd3" stroke-width="1.5"/>
  <text x="150" y="227" text-anchor="middle" font-size="11" font-weight="700" fill="#881337">Perceived Accuracy</text>
  <text x="150" y="243" text-anchor="middle" font-size="9.5" fill="#e11d48">(ACC) — Al-Natour et al. (2011)</text>

  <rect x="45" y="270" width="210" height="50" rx="6" fill="#ffffff" stroke="#fecdd3" stroke-width="1.5"/>
  <text x="150" y="292" text-anchor="middle" font-size="11" font-weight="700" fill="#881337">Recommendation Novelty</text>
  <text x="150" y="308" text-anchor="middle" font-size="9.5" fill="#e11d48">(NOV) — Zhang et al. (2021)</text>

  <!-- COLUMN 2: ORGANISM (O) -->
  <rect x="350" y="130" width="220" height="180" rx="8" fill="#f0fdf4" stroke="#10b981" stroke-width="2" filter="url(#sdrop)"/>
  <rect x="350" y="130" width="220" height="36" rx="8" fill="#dcfce7"/>
  <text x="460" y="153" text-anchor="middle" font-size="12" font-weight="800" fill="#065f46">ORGANISM (O): MEDIATOR</text>

  <rect x="365" y="185" width="190" height="90" rx="6" fill="#ffffff" stroke="#a7f3d0" stroke-width="1.5"/>
  <text x="460" y="218" text-anchor="middle" font-size="12" font-weight="800" fill="#065f46">CUMULATIVE</text>
  <text x="460" y="236" text-anchor="middle" font-size="12" font-weight="800" fill="#065f46">E-SATISFACTION</text>
  <text x="460" y="255" text-anchor="middle" font-size="10" fill="#059669">(ES) — Oliver (1980)</text>

  <!-- COLUMN 3: RESPONSE (R) -->
  <rect x="650" y="90" width="240" height="260" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8" filter="url(#sdrop)"/>
  <rect x="650" y="90" width="240" height="36" rx="8" fill="#dbeafe"/>
  <text x="770" y="113" text-anchor="middle" font-size="12" font-weight="800" fill="#1e40af">RESPONSE (R): OUTCOMES</text>

  <!-- Response Sub-variables -->
  <rect x="665" y="145" width="210" height="60" rx="6" fill="#ffffff" stroke="#bfdbfe" stroke-width="1.5"/>
  <text x="770" y="172" text-anchor="middle" font-size="11.5" font-weight="800" fill="#1e3a8a">Urge to Buy Impulsively</text>
  <text x="770" y="190" text-anchor="middle" font-size="9.5" fill="#2563eb">(UBI) — Beatty &amp; Ferrell (1998)</text>

  <!-- Arrow UBI -> IB -->
  <line x1="770" y1="205" x2="770" y2="245" stroke="#0284c7" stroke-width="2.5" marker-end="url(#marr)"/>
  <rect x="780" y="215" width="55" height="18" rx="4" fill="#e0f2fe"/>
  <text x="807" y="228" text-anchor="middle" font-size="9.5" font-weight="800" fill="#0369a1">H5 (+)</text>

  <rect x="665" y="255" width="210" height="60" rx="6" fill="#ffffff" stroke="#93c5fd" stroke-width="2"/>
  <text x="770" y="282" text-anchor="middle" font-size="11.5" font-weight="800" fill="#1e40af">Online Impulse Buying</text>
  <text x="770" y="300" text-anchor="middle" font-size="9.5" fill="#2563eb">(IB) — Rook &amp; Fisher (1995)</text>

  <!-- Hypotheses Structural Arrows S -> O -->
  <!-- H1: PP -> ES -->
  <line x1="255" y1="165" x2="345" y2="210" stroke="#0284c7" stroke-width="2" marker-end="url(#marr)"/>
  <rect x="275" y="170" width="50" height="18" rx="4" fill="#e0f2fe"/>
  <text x="300" y="183" text-anchor="middle" font-size="9" font-weight="800" fill="#0369a1">H1 (+)</text>

  <!-- H2: ACC -> ES -->
  <line x1="255" y1="230" x2="345" y2="230" stroke="#0284c7" stroke-width="2" marker-end="url(#marr)"/>
  <rect x="275" y="221" width="50" height="18" rx="4" fill="#e0f2fe"/>
  <text x="300" y="234" text-anchor="middle" font-size="9" font-weight="800" fill="#0369a1">H2 (+)</text>

  <!-- H4: NOV -> ES -->
  <line x1="255" y1="295" x2="345" y2="250" stroke="#0284c7" stroke-width="2" marker-end="url(#marr)"/>
  <rect x="275" y="280" width="50" height="18" rx="4" fill="#e0f2fe"/>
  <text x="300" y="293" text-anchor="middle" font-size="9" font-weight="800" fill="#0369a1">H4 (+)</text>

  <!-- Hypothesis Structural Arrow O -> R (H3: ES -> UBI) -->
  <line x1="570" y1="200" x2="655" y2="180" stroke="#0284c7" stroke-width="2.5" marker-end="url(#marr)"/>
  <rect x="585" y="175" width="50" height="18" rx="4" fill="#e0f2fe"/>
  <text x="610" y="188" text-anchor="middle" font-size="9" font-weight="800" fill="#0369a1">H3 (+)</text>

  <!-- MODERATOR (BOTTOM BOX) -->
  <rect x="330" y="380" width="300" height="110" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6,4" filter="url(#sdrop)"/>
  <rect x="330" y="380" width="300" height="28" rx="8" fill="#fef3c7"/>
  <text x="480" y="399" text-anchor="middle" font-size="10.5" font-weight="800" fill="#b45309">PSYCHOLOGICAL MODERATOR (H6)</text>

  <text x="480" y="428" text-anchor="middle" font-size="12" font-weight="800" fill="#92400e">Ego Depletion (EGO)</text>
  <text x="480" y="446" text-anchor="middle" font-size="10" fill="#b45309">Self-Regulatory Resource Depletion</text>
  <text x="480" y="465" text-anchor="middle" font-size="9.5" font-style="italic" fill="#78350f">Baumeister (2002) Strength Model</text>

  <!-- Moderator Arrow (Dashed) to UBI -> IB link -->
  <path d="M 630 435 L 770 435 L 770 240" fill="none" stroke="#d97706" stroke-width="2.5" stroke-dasharray="5,4" marker-end="url(#modarr)"/>
  <rect x="710" y="420" width="55" height="18" rx="4" fill="#fef3c7"/>
  <text x="737" y="433" text-anchor="middle" font-size="9.5" font-weight="800" fill="#92400e">H6 (+)</text>
</svg>'''

# Save individual SVG files
with open(os.path.join(FIGURES_DIR, "figure1_prisma_flow_diagram.svg"), "w", encoding="utf-8") as f:
    f.write(prisma_svg)
with open(os.path.join(FIGURES_DIR, "figure2_vosviewer_clusters.svg"), "w", encoding="utf-8") as f:
    f.write(vos_svg)
with open(os.path.join(FIGURES_DIR, "figure3_theoretical_sor_model.svg"), "w", encoding="utf-8") as f:
    f.write(sor_svg)

print(f"[SUCCESS] Generated 3 publication-grade vector SVGs in {FIGURES_DIR}/")
