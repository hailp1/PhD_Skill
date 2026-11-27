# Decoding the Generative AI Recommendation-Impulse Buying Link: An Empirical Registered Protocol Testing Curvilinear Surveillance Reactance, Multiplicative Mediation, and Ego Depletion

---

## HIGHLIGHTS
- Tests a dynamic multiplicative S-O-R model for AI-driven impulse buying.
- Models inverted-U personalization effects on surveillance reactance.
- Examines cognitive fluency x emotional arousal interaction on buying urges.
- Evaluates ego depletion boundaries using G*Power N=450 and PLS-SEM.
- Proposes three-wave RI-CLPM to test post-purchase regret feedback.

---

## ABSTRACT
While generative artificial intelligence (AI) recommendation agents increasingly shape consumer discovery across digital retailing ecosystems, empirical models rarely capture the non-linear, interactive, and self-regulatory boundaries governing unplanned purchasing. Building directly on our expanded systematic corpus audit ($N = 1,016$ peer-reviewed studies plus $n = 28$ snowball-expanded records), this registered empirical protocol operationalizes and prepares to test a **Dynamic and Multiplicative Dual-Path Stimulus-Organism-Response (S-O-R) Model**. Specifically, we move beyond linear additive frameworks by hypothesizing an inverted-U curvilinear relationship between perceived personalization and in-session cognitive fluency/e-satisfaction ($H_1, H_8$), alongside a multiplicative interaction between cognitive comfort (permission structure) and emotional arousal (kinetic energy) in driving the urge to buy impulsively ($H_{5b}$). Furthermore, we model ego depletion as a self-regulatory boundary condition accelerating checkout execution ($H_7$) and propose a three-wave Random-Intercept Cross-Lagged Panel Model (RI-CLPM) to test whether depletion-induced impulse purchases trigger post-purchase regret that erodes future satisfaction ($H_9$). Sample size estimation via G*Power 3.1 ($N = 450$), Brislin back-translation of a 28-item validated survey instrument, Common Method Bias (CMB) remedies, and a Two-Stage PLS-SEM estimation strategy are fully specified prior to field data collection.

**Keywords**: Generative AI Recommendations; Online Impulse Buying; Inverted-U Personalization; Surveillance Reactance; Multiplicative Mediation; Ego Depletion; PLS-SEM; Registered Empirical Protocol.

---

## 1. INTRODUCTION

### 1.1. Research Motivation and Empirical Imperative
Digital retailing interfaces have transitioned from static product catalogs to dynamic, conversational AI recommendation agents capable of real-time preference adaptation (Guha et al., 2022; Huang & Ahmad, 2026; Pang et al., 2026). Although practitioner accounts frequently link predictive personalization to elevated conversion rates, empirical consumer psychology suggests that algorithmic nudging operates through complex cognitive and affective trade-offs (Chan et al., 2017; Zhang et al., 2021). Quantitative gap scanning across our expanded corpus ($N = 1,016$ studies) reveals that only 0.98% of extant studies test multiplicative cognitive-affective interactions, 2.17% evaluate curvilinear personalization thresholds, 4.53% model surveillance reactance, 2.95% employ longitudinal panel designs, and merely 0.79% incorporate ego depletion as a regulatory boundary (Akram et al., 2020; Kumaran & Shobhana, 2026).

To address these empirical blind spots without post-hoc theorizing, this study establishes a pre-registered empirical protocol designed to test nine formal hypotheses ($H_1$ through $H_9$, alongside mediation hypotheses $H_{4a}$, $H_{5a}$ and interaction hypothesis $H_{5b}$) in active digital retail settings. We examine how AI recommendation attributes simultaneously foster in-session cognitive fluency and hedonic arousal while risking endogenous privacy backlash when personalization crosses consumer comfort thresholds (Gallin & Portes, 2024; Xiao & Benbasat, 2018).

### 1.2. Research Questions and Multi-Perspective Design Rationale
This empirical investigation addresses three focused questions:
- **RQ1**: *Does perceived algorithmic personalization exhibit an inverted-U curvilinear effect on in-session cognitive fluency and e-satisfaction by endogenously triggering surveillance reactance beyond an optimal threshold?*
- **RQ2**: *Do e-satisfaction (permission structure) and emotional arousal (kinetic energy) interact multiplicatively to amplify the urge to buy impulsively?*
- **RQ3**: *To what extent does ego depletion strengthen the translation of impulsive urges into checkout behavior, and does post-purchase regret feed back to erode subsequent satisfaction?*

Synthesizing four orthogonal theoretical perspectives (Consumer Psychology, Information Systems Architecture, Self-Regulation Theory, and Algorithmic Ethics), our protocol enforces four structural upgrades over conventional S-O-R surveys:
- **Consumer Psychology & Dual-Path Affect**: Specify Multiplicative Interaction (ESAT x Arousal -> UBI) and resolve cold-start impulse buying via In-Session Cognitive Fluency.
- **Information Systems & Algorithmic Architecture**: Model Perceived Personalization (PP) with an Inverted-U curvilinear effect on Cognitive Fluency/E-Satisfaction, triggering endogenous Surveillance Reactance beyond the privacy threshold.
- **Self-Regulation, Cognitive Load & Ego Depletion**: Add Negative Recursive Feedback Loop (OIB under Ego Depletion -> Post-Purchase Regret -> Erodes Future E-Satisfaction) and hedge depletion via Cognitive Load Theory.
- **Generative AI Social Agency & Algorithmic Ethics (2024-2026)**: Explicitly contrast Gen 1.0 vs. Gen 2.0 AI Agency and formulate Tiered Ethical Friction (low-regret vs. high-regret cooling-off mechanisms).

### 1.3. Novelty Positioning Against Prior Literature
Table 1 contrasts this registered protocol against prevailing empirical paradigms in AI-mediated retail research, clarifying the incremental theoretical and methodological novelty of testing all five mechanisms simultaneously.

<div class="academic-figure-container" style="margin: 1.5rem 0; overflow-x: auto;">
<div style="font-weight: 700; font-size: 0.98rem; color: #0f172a; margin-bottom: 0.5rem; text-align: left;">Table 1: Novelty Positioning Matrix Comparing Prior Empirical Streams and the Current Protocol</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.84rem; text-align: left; background: #ffffff; border-top: 2.5px solid #0f172a; border-bottom: 2.5px solid #0f172a;">
<thead>
<tr style="border-bottom: 1.5px solid #cbd5e1; background: #f8fafc;">
<th style="padding: 9px 12px; font-weight: 800; color: #0f172a;">Analytical Dimension</th>
<th style="padding: 9px 12px; font-weight: 800; color: #0f172a;">Prevailing Linear S-O-R Stream</th>
<th style="padding: 9px 12px; font-weight: 800; color: #0f172a;">Current Registered Protocol (Paper 2)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 12px;">Personalization Effect</td><td style="padding: 8px 12px;">Assumes monotonic linear benefit on trust and satisfaction</td><td style="padding: 8px 12px;">Tests inverted-U quadratic threshold ($PP^2$, $H_1$) and endogenous reactance ($H_8$)</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9; background: #fdfdfd;"><td style="padding: 8px 12px;">Cognitive-Affective Integration</td><td style="padding: 8px 12px;">Models cognitive and affective mediators as independent additive paths</td><td style="padding: 8px 12px;">Tests multiplicative interaction ($ESAT \times AROUSAL$, $H_{5b}$)</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 12px;">Self-Regulatory Boundary</td><td style="padding: 8px 12px;">Treats impulse urge-to-buy conversion as static across sessions</td><td style="padding: 8px 12px;">Models Ego Depletion ($H_7$) as an executive-control amplifier</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9; background: #fdfdfd;"><td style="padding: 8px 12px;">Temporal Causality</td><td style="padding: 8px 12px;">Single-wave cross-sectional survey (high CMB risk)</td><td style="padding: 8px 12px;">Three-wave 14-day lagged panel with RI-CLPM regret feedback ($H_9$)</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 12px;">Managerial Prescription</td><td style="padding: 8px 12px;">Maximize algorithmic persuasion and click-through velocity</td><td style="padding: 8px 12px;">Calibrates Tiered Ethical Friction to protect long-term CLV</td></tr>
</tbody>
</table>
<div style="font-size: 0.78rem; color: #64748b; margin-top: 0.5rem; text-align: left;"><em>Note</em>: Contrasts prevailing linear S-O-R empirical studies against the current pre-registered multi-wave protocol.</div>
</div>

---

## 2. THEORETICAL BACKGROUND AND HYPOTHESES DEVELOPMENT

Figure 1 illustrates the hypothesized structural architecture linking AI recommendation stimuli, dual organismic states, endogenous surveillance reactance, ego depletion, and three-wave post-purchase regret feedback.

<div class="academic-figure-container" style="text-align:center; margin: 20px 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 490" width="100%" height="auto" style="font-family: 'Segoe UI', Arial, sans-serif; background:#ffffff;">
<defs>
<marker id="p2b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#1d4ed8"/></marker>
<marker id="p2r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626"/></marker>
<marker id="p2g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#0f766e"/></marker>
<marker id="p2p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#7c3aed"/></marker>
</defs>
<text x="460" y="24" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#0f172a">Figure 1: Hypothesized Dynamic and Multiplicative S-O-R Structural Model (H1-H9)</text>
<rect x="20" y="50" width="205" height="350" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.4"/>
<text x="122" y="72" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#1e3a8a">STIMULI (AI ATTRIBUTES)</text>
<rect x="34" y="90" width="177" height="72" rx="5" fill="#ffffff" stroke="#2563eb" stroke-width="1.3"/>
<text x="122" y="114" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e40af">Perceived Personalization (PP)</text>
<text x="122" y="132" text-anchor="middle" font-size="10" fill="#1d4ed8">H1: Inverted-U (PP^2)</text>
<text x="122" y="148" text-anchor="middle" font-size="10" fill="#dc2626">H8: Triggers Reactance</text>
<rect x="34" y="182" width="177" height="66" rx="5" fill="#ffffff" stroke="#2563eb" stroke-width="1.3"/>
<text x="122" y="208" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e40af">Recommendation Accuracy</text>
<text x="122" y="227" text-anchor="middle" font-size="10" fill="#1d4ed8">(ACC) -&gt; H2 (+)</text>
<rect x="34" y="268" width="177" height="66" rx="5" fill="#ffffff" stroke="#2563eb" stroke-width="1.3"/>
<text x="122" y="294" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e40af">Novelty &amp; Serendipity</text>
<text x="122" y="313" text-anchor="middle" font-size="10" fill="#dc2626">(NOV) -&gt; H3 (+)</text>
<rect x="255" y="50" width="365" height="350" rx="8" fill="#fefce8" stroke="#ca8a04" stroke-width="1.4"/>
<text x="437" y="72" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#713f12">ORGANISM (DUAL-PATH &amp; REACTANCE)</text>
<rect x="275" y="90" width="325" height="68" rx="5" fill="#ffffff" stroke="#0284c7" stroke-width="1.4"/>
<text x="437" y="114" text-anchor="middle" font-size="11" font-weight="bold" fill="#0369a1">Cognitive Fluency &amp; E-Satisfaction (ESAT)</text>
<text x="437" y="134" text-anchor="middle" font-size="10" fill="#334155">Permission Structure (H4, H4a)</text>
<rect x="275" y="178" width="325" height="62" rx="5" fill="#fff7ed" stroke="#ea580c" stroke-width="1.4"/>
<text x="437" y="203" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#9a3412">H5b: Multiplicative Interaction</text>
<text x="437" y="222" text-anchor="middle" font-size="10" fill="#c2410c">(ESAT x Emotional Arousal -&gt; UBI)</text>
<rect x="275" y="258" width="325" height="68" rx="5" fill="#ffffff" stroke="#dc2626" stroke-width="1.4"/>
<text x="437" y="282" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">Emotional Arousal (AROUSAL)</text>
<text x="437" y="302" text-anchor="middle" font-size="10" fill="#334155">Visceral Kinetic Energy (H5, H5a)</text>
<rect x="275" y="340" width="325" height="48" rx="5" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.3"/>
<text x="437" y="362" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#7f1d1d">Surveillance Reactance (REACT)</text>
<text x="437" y="378" text-anchor="middle" font-size="9.5" fill="#991b1b">H8 (-): Attenuates ESAT Beyond Privacy Threshold</text>
<rect x="650" y="50" width="250" height="350" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.4"/>
<text x="775" y="72" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#14532d">RESPONSE &amp; BOUNDARY</text>
<rect x="670" y="95" width="210" height="64" rx="5" fill="#ffffff" stroke="#15803d" stroke-width="1.4"/>
<text x="775" y="120" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">Urge to Buy Impulsively (UBI)</text>
<text x="775" y="139" text-anchor="middle" font-size="10" fill="#334155">Proximal Cognitive-Affective Trigger</text>
<rect x="670" y="190" width="210" height="62" rx="5" fill="#f0fdfa" stroke="#0f766e" stroke-width="1.4"/>
<text x="775" y="214" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#115e59">H7 Moderator: Ego Depletion</text>
<text x="775" y="233" text-anchor="middle" font-size="10" fill="#134e4a">(EGO) Accelerates UBI -&gt; OIB</text>
<rect x="670" y="276" width="210" height="62" rx="5" fill="#ffffff" stroke="#15803d" stroke-width="1.4"/>
<text x="775" y="300" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">Online Impulse Buying (OIB)</text>
<text x="775" y="319" text-anchor="middle" font-size="10" fill="#334155">H6 (+): Unplanned Checkout</text>
<rect x="670" y="348" width="210" height="44" rx="5" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.3"/>
<text x="775" y="368" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#5b21b6">Post-Purchase Regret (W1-&gt;W3)</text>
<text x="775" y="383" text-anchor="middle" font-size="9.5" fill="#6d28d9">H9: RI-CLPM Cross-Lagged Erosion</text>
<line x1="211" y1="120" x2="273" y2="120" stroke="#1d4ed8" stroke-width="1.8" marker-end="url(#p2b)"/>
<line x1="211" y1="215" x2="273" y2="138" stroke="#1d4ed8" stroke-width="1.7" marker-end="url(#p2b)"/>
<line x1="211" y1="145" x2="273" y2="360" stroke="#dc2626" stroke-width="1.6" stroke-dasharray="4,3" marker-end="url(#p2r)"/>
<line x1="211" y1="300" x2="273" y2="292" stroke="#dc2626" stroke-width="1.8" marker-end="url(#p2r)"/>
<line x1="600" y1="122" x2="668" y2="122" stroke="#1d4ed8" stroke-width="1.8" marker-end="url(#p2b)"/>
<line x1="600" y1="208" x2="668" y2="136" stroke="#ea580c" stroke-width="1.8" marker-end="url(#p2r)"/>
<line x1="600" y1="286" x2="668" y2="148" stroke="#dc2626" stroke-width="1.8" marker-end="url(#p2r)"/>
<line x1="775" y1="159" x2="775" y2="274" stroke="#0f766e" stroke-width="1.8" marker-end="url(#p2g)"/>
<line x1="775" y1="338" x2="775" y2="346" stroke="#7c3aed" stroke-width="1.6" marker-end="url(#p2p)"/>
<path d="M 775 392 L 775 445 L 437 445 L 437 158" fill="none" stroke="#7c3aed" stroke-width="1.7" stroke-dasharray="6,4" marker-end="url(#p2p)"/>
<text x="560" y="466" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#6d28d9">H9 (-) Three-Wave RI-CLPM Feedback: Depletion-Induced OIB &amp; Regret Erode Future ESAT</text>
</svg>
<div class="figure-caption"><strong>Figure 1:</strong> Hypothesized Dynamic and Multiplicative S-O-R Structural Model ($H_1$ through $H_9$).</div>
</div>

### 2.1. Dual-Path S-O-R Foundations and Curvilinear Personalization (H1, H2, H8)
Grounded in the Stimulus-Organism-Response (S-O-R) paradigm (Mehrabian & Russell, 1974; Jacoby, 2002) and Cognitive Fit Theory (Vessey, 1991), **Perceived Personalization (PP)** reduces information search friction, enabling immediate in-session cognitive fluency and **E-Satisfaction (ESAT)** even in cold-start discovery sessions (Oliver, 1980, 1993; Shanahan et al., 2019; Spreng et al., 1996). However, drawing on Psychological Reactance Theory (Brehm, 1966) and agent bias research (Komiak & Benbasat, 2006; Xiao & Benbasat, 2007, 2018), hyper-personalization beyond an acceptable privacy boundary evokes perceived algorithmic surveillance and reactance (Lau et al., 2026). Simultaneously, **Perceived Recommendation Accuracy (ACC)** reinforces functional expectancy confirmation (Al-Natour et al., 2011). We therefore hypothesize:
- **H1**: *Perceived personalization exhibits an inverted-U curvilinear relationship with in-session cognitive fluency and e-satisfaction.*
- **H2**: *Perceived recommendation accuracy positively influences e-satisfaction.*
- **H8**: *Excessive perceived personalization positively triggers algorithmic surveillance reactance, which negatively attenuates e-satisfaction.*

### 2.2. Recommendation Novelty and Affective Arousal (H3)
Whereas accuracy satisfies utilitarian expectations, **Recommendation Novelty and Serendipity (NOV)** introduces unexpected hedonic discovery (Zhang et al., 2021; Lin, 2026). Consistent with environmental psychology (Eroglu et al., 2001; Verhagen & van Dolen, 2011), novel and visually salient recommendations elevate **Emotional Arousal (AROUSAL)** during active browsing (Ampadu et al., 2022; Miao et al., 2021). Thus:
- **H3**: *Recommendation novelty and serendipity positively influence consumer emotional arousal.*

### 2.3. Multiplicative Organismic Interaction and Impulsive Urges (H4, H4a, H5, H5a, H5b)
Consumer impulse literature distinguishes cognitive trust from visceral desire (Beatty & Ferrell, 1998; Rook & Fisher, 1995). We posit that **E-Satisfaction** functions as a cognitive permission structure that disarms analytical vigilance ($H_4, H_{4a}$), while **Emotional Arousal** supplies visceral kinetic energy ($H_5, H_{5a}$) (Do Xuan Nguyen & Nguyen, 2026; Zhu et al., 2023). Crucially, rather than operating purely additively, these two states interact multiplicatively to maximize the **Urge to Buy Impulsively (UBI)**:
- **H4**: *E-satisfaction positively influences the urge to buy impulsively.*
- **H4a**: *E-satisfaction mediates the curvilinear relationship between perceived personalization/accuracy and the urge to buy impulsively.*
- **H5**: *Emotional arousal positively influences the urge to buy impulsively.*
- **H5a**: *Emotional arousal mediates the positive relationship between recommendation novelty and the urge to buy impulsively.*
- **H5b**: *E-satisfaction and emotional arousal interact multiplicatively to amplify the urge to buy impulsively, such that urges peak when both states are simultaneously high.*

### 2.4. Checkout Execution, Ego Depletion, and Recursive Regret Feedback (H6, H7, H9)
Felt impulsive urges serve as the proximate antecedent to **Online Impulse Buying Behavior (OIB)** (Badgaiyan & Verma, 2015; Zheng et al., 2019). Grounded in the Strength Model of Self-Control (Baumeister, 2002; Baumeister et al., 2007) and Cognitive Load Theory (Sweller, 1988), consumers experiencing **Ego Depletion (EGO)** lack executive inhibition to override urges, even accounting for replication debates regarding contextual cognitive fatigue (Hagger et al., 2016; Kulal et al., 2026). Over repeated cycles, however, depletion-induced impulse purchases generate **Post-Purchase Regret**, eroding subsequent satisfaction (Tobon & Abril, 2024):
- **H6**: *The urge to buy impulsively positively influences online impulse buying behavior.*
- **H7**: *Ego depletion positively moderates the relationship between the urge to buy impulsively and online impulse buying behavior.*
- **H9**: *Depletion-induced online impulse buying increases post-purchase regret, which negatively predicts future e-satisfaction across sequential shopping waves.*

---

## 3. RESEARCH METHODOLOGY (PRE-DATA REGISTERED PROTOCOL)

### 3.1. Target Sample Size, G*Power Calculation, and Sampling Strategy
**[STATUS: PENDING FIELD SURVEY COLLECTION | ZERO FABRICATED DATA REPORTED]**  
To ensure robust statistical power for detecting small-to-medium quadratic ($PP^2$) and multiplicative interaction ($ESAT \times Arousal$) effects in PLS-SEM, a priori power analysis was conducted using **G*Power 3.1** (Faul et al., 2009). Setting a conservative effect size ($f^2 = 0.05$), $\alpha = 0.05$, statistical power $(1 - \beta) = 0.95$, and up to 6 structural predictors per endogenous construct yields a minimum required sample of $N = 368$. Accounting for an anticipated 18% invalid/attention-check failure and cross-wave attrition buffer, we establish a target sample of **$N = 450$ active e-commerce consumers** recruited across three longitudinal survey waves ($t_1, t_2, t_3$, spaced 14 days apart) to enable RI-CLPM testing of $H_9$. Figure 2 plots the statistical power trajectory across sample sizes.

<div class="academic-figure-container" style="text-align:center; margin: 20px 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 300" width="100%" height="auto" style="font-family: 'Segoe UI', Arial, sans-serif; background:#ffffff;">
<text x="420" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Figure 2: A Priori G*Power 3.1 Statistical Power Curve (f^2 = 0.05, alpha = 0.05, 6 Predictors)</text>
<line x1="90" y1="240" x2="790" y2="240" stroke="#64748b" stroke-width="1.5"/>
<line x1="90" y1="45" x2="90" y2="240" stroke="#64748b" stroke-width="1.5"/>
<line x1="90" y1="54.8" x2="780" y2="54.8" stroke="#16a34a" stroke-width="1.3" stroke-dasharray="5,4"/>
<text x="775" y="49.8" text-anchor="end" font-size="10" font-weight="bold" fill="#15803d">Target Power (1 - beta) = 0.95</text>
<rect x="603.0" y="45" width="157.0" height="195" fill="#dcfce7" fill-opacity="0.45"/>
<text x="681.5" y="228" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#166534">18% Attrition Buffer</text>
<polyline fill="none" stroke="#0284c7" stroke-width="2.5" points="90.0,169.8 185.7,136.6 281.4,107.4 377.1,84.0 472.9,68.4 568.6,58.6 603.0,54.8 664.3,51.8 760.0,48.5"/>
<circle cx="90.0" cy="169.8" r="4" fill="#0284c7" stroke="#ffffff" stroke-width="1.2"/><text x="90.0" y="159.8" text-anchor="middle" font-size="10" font-weight="bold" fill="#0284c7">N=100 (0.36)</text><circle cx="185.7" cy="136.6" r="4" fill="#0284c7" stroke="#ffffff" stroke-width="1.2"/><circle cx="281.4" cy="107.4" r="4" fill="#0284c7" stroke="#ffffff" stroke-width="1.2"/><text x="281.4" y="97.4" text-anchor="middle" font-size="10" font-weight="bold" fill="#0284c7">N=200 (0.68)</text><circle cx="377.1" cy="84.0" r="4" fill="#0284c7" stroke="#ffffff" stroke-width="1.2"/><circle cx="472.9" cy="68.4" r="4" fill="#0284c7" stroke="#ffffff" stroke-width="1.2"/><text x="472.9" y="58.4" text-anchor="middle" font-size="10" font-weight="bold" fill="#0284c7">N=300 (0.88)</text><circle cx="568.6" cy="58.6" r="4" fill="#0284c7" stroke="#ffffff" stroke-width="1.2"/><circle cx="603.0" cy="54.8" r="5.5" fill="#dc2626" stroke="#ffffff" stroke-width="1.2"/><text x="603.0" y="44.8" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">N=368 (0.95)</text><circle cx="664.3" cy="51.8" r="4" fill="#0284c7" stroke="#ffffff" stroke-width="1.2"/><circle cx="760.0" cy="48.5" r="5.5" fill="#dc2626" stroke="#ffffff" stroke-width="1.2"/><text x="760.0" y="38.5" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">N=450 (0.98)</text>
<text x="420" y="275" text-anchor="middle" font-size="10.5" fill="#334155">Sample Size (N): Minimum Required N = 368 (Power = 0.95) | Target Field Recruitment N = 450 (Power = 0.98)</text>
</svg>
<div class="figure-caption"><strong>Figure 2:</strong> A Priori G*Power 3.1 Statistical Power Curve ($f^2 = 0.05, \alpha = 0.05$, Target $N = 450$).</div>
</div>

### 3.2. Survey Instrument Design and Brislin Back-Translation Protocol
All measurement scales employ a 7-point Likert format (`1 = Strongly Disagree` to `7 = Strongly Agree`) adapted from validated Q1 literature and translated into Vietnamese using **Brislin's (1970) back-translation protocol** with two independent bilingual marketing scholars and qualitative Content Validity Index (CVI $\ge 0.80$) expert screening. Table 2 summarizes the 28-item core operationalization alongside attention-check safeguards.

<div class="academic-figure-container" style="margin: 2rem 0; overflow-x: auto;">
<div style="font-weight: 700; font-size: 1rem; color: #0f172a; margin-bottom: 0.5rem; text-align: left;">Table 2: Construct Operationalization and Validated Scale Sources (28-Item Core Instrument)</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.84rem; text-align: left; background: #ffffff; border-top: 2.5px solid #0f172a; border-bottom: 2.5px solid #0f172a;">
<thead>
<tr style="border-bottom: 1.5px solid #cbd5e1; background: #f8fafc;">
<th style="padding: 9px 12px; font-weight: 800; color: #0f172a;">Construct (Code)</th>
<th style="padding: 9px 12px; font-weight: 800; color: #0f172a; text-align: center;">Items</th>
<th style="padding: 9px 12px; font-weight: 800; color: #0f172a;">Role in Model</th>
<th style="padding: 9px 12px; font-weight: 800; color: #0f172a;">Primary Adapted Source(s)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 12px;">Perceived Personalization (PP)</td><td style="padding: 8px 12px; text-align: center;">4</td><td style="padding: 8px 12px;">Stimulus (Quadratic $PP^2$)</td><td style="padding: 8px 12px;">Shanahan et al. (2019)</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9; background: #fdfdfd;"><td style="padding: 8px 12px;">Recommendation Accuracy (ACC)</td><td style="padding: 8px 12px; text-align: center;">3</td><td style="padding: 8px 12px;">Stimulus</td><td style="padding: 8px 12px;">Al-Natour et al. (2011)</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 12px;">Novelty &amp; Serendipity (NOV)</td><td style="padding: 8px 12px; text-align: center;">3</td><td style="padding: 8px 12px;">Stimulus</td><td style="padding: 8px 12px;">Zhang et al. (2021)</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9; background: #fdfdfd;"><td style="padding: 8px 12px;">E-Satisfaction (ESAT)</td><td style="padding: 8px 12px; text-align: center;">4</td><td style="padding: 8px 12px;">Cognitive Mediator</td><td style="padding: 8px 12px;">Oliver (1980); Spreng et al. (1996)</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 12px;">Emotional Arousal (AROUSAL)</td><td style="padding: 8px 12px; text-align: center;">3</td><td style="padding: 8px 12px;">Affective Mediator</td><td style="padding: 8px 12px;">Mehrabian &amp; Russell (1974); Verhagen &amp; van Dolen (2011)</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9; background: #fdfdfd;"><td style="padding: 8px 12px;">Urge to Buy Impulsively (UBI)</td><td style="padding: 8px 12px; text-align: center;">3</td><td style="padding: 8px 12px;">Proximal Response</td><td style="padding: 8px 12px;">Beatty &amp; Ferrell (1998)</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 12px;">Online Impulse Buying (OIB)</td><td style="padding: 8px 12px; text-align: center;">4</td><td style="padding: 8px 12px;">Behavioral Outcome</td><td style="padding: 8px 12px;">Rook &amp; Fisher (1995); Zheng et al. (2019)</td></tr>
<tr style="border-bottom: 1px solid #f1f5f9; background: #fdfdfd;"><td style="padding: 8px 12px;">Ego Depletion &amp; Reactance (EGO/REACT)</td><td style="padding: 8px 12px; text-align: center;">4</td><td style="padding: 8px 12px;">Boundary Moderators</td><td style="padding: 8px 12px;">Baumeister et al. (2007); Xiao &amp; Benbasat (2018)</td></tr>
</tbody>
</table>
<div style="font-size: 0.78rem; color: #64748b; margin-top: 0.5rem; text-align: left;"><em>Note</em>: Plus 2 embedded attention-check items and 3 screening questions. Pre-validated via Brislin (1970) back-translation.</div>
</div>

### 3.3. Statistical Analysis and Common Method Bias (CMB) Protocol
Figure 3 outlines the three-wave data collection schedule and multi-stage analytical workflow designed to separate within-person dynamics from stable trait variance while guarding against Common Method Bias (Podsakoff et al., 2003).

<div class="academic-figure-container" style="text-align:center; margin: 20px 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 240" width="100%" height="auto" style="font-family: 'Segoe UI', Arial, sans-serif; background:#ffffff;">
<defs><marker id="p2f" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b"/></marker></defs>
<text x="450" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">Figure 3: Three-Wave Longitudinal Survey Design and Two-Stage PLS-SEM + RI-CLPM Workflow</text>
<rect x="20" y="45" width="195" height="145" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
<text x="117" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">Wave 1 (Day 0, N=450)</text>
<text x="117" y="90" text-anchor="middle" font-size="10" fill="#334155">AI Stimuli (PP, ACC, NOV)</text>
<text x="117" y="108" text-anchor="middle" font-size="10" fill="#334155">Baseline ESAT &amp; AROUSAL</text>
<text x="117" y="126" text-anchor="middle" font-size="10" fill="#334155">Brislin 28-Item Instrument</text>
<text x="117" y="144" text-anchor="middle" font-size="10" fill="#0284c7">Attention Checks + Screening</text>
<line x1="215" y1="117" x2="245" y2="117" stroke="#1e293b" stroke-width="1.6" marker-end="url(#p2f)"/>
<rect x="247" y="45" width="195" height="145" rx="6" fill="#fefce8" stroke="#ca8a04" stroke-width="1.4"/>
<text x="344" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#713f12">Wave 2 (Day 14)</text>
<text x="344" y="90" text-anchor="middle" font-size="10" fill="#334155">Ego Depletion (EGO)</text>
<text x="344" y="108" text-anchor="middle" font-size="10" fill="#334155">Surveillance Reactance</text>
<text x="344" y="126" text-anchor="middle" font-size="10" fill="#334155">UBI &amp; Impulse Checkout (OIB)</text>
<text x="344" y="144" text-anchor="middle" font-size="10" fill="#b45309">Temporal Separation vs. CMB</text>
<line x1="442" y1="117" x2="472" y2="117" stroke="#1e293b" stroke-width="1.6" marker-end="url(#p2f)"/>
<rect x="474" y="45" width="195" height="145" rx="6" fill="#faf5ff" stroke="#7c3aed" stroke-width="1.4"/>
<text x="571" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">Wave 3 (Day 28)</text>
<text x="571" y="90" text-anchor="middle" font-size="10" fill="#334155">Post-Purchase Regret</text>
<text x="571" y="108" text-anchor="middle" font-size="10" fill="#334155">Follow-Up E-Satisfaction</text>
<text x="571" y="126" text-anchor="middle" font-size="10" fill="#334155">Shifted Privacy Threshold</text>
<text x="571" y="144" text-anchor="middle" font-size="10" fill="#7c3aed">Tests H9 Within-Person Lag</text>
<line x1="669" y1="117" x2="699" y2="117" stroke="#1e293b" stroke-width="1.6" marker-end="url(#p2f)"/>
<rect x="701" y="45" width="179" height="145" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.4"/>
<text x="790" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#14532d">Estimation Pipeline</text>
<text x="790" y="90" text-anchor="middle" font-size="10" fill="#334155">1. Kline + Full VIF (&lt;= 3.3)</text>
<text x="790" y="108" text-anchor="middle" font-size="10" fill="#334155">2. Outer Loadings &amp; HTMT</text>
<text x="790" y="126" text-anchor="middle" font-size="10" fill="#334155">3. PLS-SEM (PP^2 &amp; ESATxAR)</text>
<text x="790" y="144" text-anchor="middle" font-size="10" fill="#15803d">4. 3-Wave RI-CLPM (H9)</text>
<text x="450" y="218" text-anchor="middle" font-size="10" fill="#475569">Note: 14-day temporal lags mitigate Common Method Bias (Podsakoff et al., 2003) and isolate within-person regret carryover.</text>
</svg>
<div class="figure-caption"><strong>Figure 3:</strong> Three-Wave Longitudinal Survey Design ($t_1, t_2, t_3$) and Two-Stage PLS-SEM + RI-CLPM Workflow.</div>
</div>

Following Hair et al. (2019, 2022), data analysis will proceed in three strict stages once field collection ($N = 450$) concludes:
1. **Data Cleaning and Common Method Bias Control**: Screening straight-lining responses, checking Kline (2016) univariate normality ($|\text{Skewness}| < 3.0, |\text{Kurtosis}| < 10.0$), and executing both Harman's single-factor test ($< 50\%$ variance) and Kock's (2015) Full Collinearity VIF assessment ($\text{VIF} \le 3.3$).
2. **Measurement Model Assessment**: Evaluating outer loadings ($\ge 0.708$), Cronbach's $\alpha$ and Composite Reliability ($\rho_c \ge 0.70$), Average Variance Extracted ($\text{AVE} \ge 0.50$), and Heterotrait-Monotrait Ratio ($\text{HTMT} < 0.85$).
3. **Structural Model, Quadratic, and RI-CLPM Estimation**: Assessing $H_1-H_8$ via **Two-Stage PLS-SEM** with 10,000 bootstrap subsamples, explicitly incorporating the quadratic term ($PP^2$) for $H_1$ and orthogonalized product indicator ($ESAT \times AROUSAL$) for $H_{5b}$, followed by three-wave RI-CLPM to isolate within-person regret feedback ($H_9$).

---

## 4. EXPECTED THEORETICAL AND METHODOLOGICAL CONTRIBUTIONS

### 4.1. Expected Theoretical Contributions
Upon empirical execution, this study delivers three distinct theoretical advances for human-computer interaction and consumer psychology. First, by testing quadratic personalization thresholds ($H_1$) alongside endogenous surveillance reactance ($H_8$), the study reconciles contradictory findings in personalization literature, demonstrating precisely how identical AI recommendation feeds shift from fluency enhancers to psychological reactance triggers (Shamim & Misra, 2025; Xiao & Benbasat, 2018). Second, by specifying a multiplicative cognitive-affective interaction ($H_{5b}$), the model moves beyond additive S-O-R assumptions (Mehrabian & Russell, 1974), showing that cognitive e-satisfaction acts as a permission gate that unlocks visceral arousal into impulsive urges. Third, by integrating ego depletion ($H_7$) with cross-lagged post-purchase regret ($H_9$), the framework bridges micro-level executive self-control theory (Baumeister, 2002) with longitudinal platform equity dynamics.

### 4.2. Methodological Innovations
Methodologically, this protocol addresses two chronic weaknesses in digital retail survey research. First, separating stimuli ($t_1$), organismic states and impulse checkout ($t_2$), and post-purchase regret ($t_3$) across 14-day intervals provides procedural temporal separation against Common Method Bias (Podsakoff et al., 2003). Second, pairing Two-Stage PLS-SEM (Hair et al., 2019, 2022) for non-linear quadratic and multiplicative terms with a three-wave Random-Intercept Cross-Lagged Panel Model (RI-CLPM) decomposes stable between-person impulsivity traits from true within-person regret carryover ($H_9$).

---

## 5. MANAGERIAL IMPLICATIONS AND PRE-REGISTRATION SAFEGUARDS

### 5.1. Managerial Implications: Implementing Tiered Ethical Friction
For e-commerce product managers and algorithmic architects, the proposed model warns against optimizing single-session conversion by exploiting consumer ego depletion. Instead, platforms should adopt **Tiered Ethical Friction**: for low-regret routine replenishment categories, AI agents can maintain high-fluency one-click recommendations; conversely, when real-time behavioral telemetry detects elevated session velocity, late-night browsing, or high-ticket discretionary baskets indicative of ego depletion, interfaces should introduce calibrated friction, such as transparent recommendation rationales, brief cart cooling-off prompts, and granular privacy controls, to preserve long-term Customer Lifetime Value (CLV) and curb product return rates (Tobon & Abril, 2024).

### 5.2. Pre-Registration Safeguards and Anticipated Limitations
Three methodological boundaries are explicitly acknowledged prior to data collection. First, cross-wave panel attrition between $t_1$ and $t_3$ could bias longitudinal estimates; our G*Power recruitment buffer ($N = 450$ vs. $N = 368$ minimum) and matched incentive scheduling are designed to preserve $\ge 82\%$ retention. Second, self-reported ego depletion measures capture subjective cognitive fatigue rather than physiological depletion; future multi-method extensions may pair survey waves with clickstream latency telemetry. Third, sampling active Vietnamese digital shoppers provides strong internal validity in a rapidly expanding Southeast Asian mobile commerce market, though cross-cultural replication will be required to generalize exact privacy inflection points.

---

## REFERENCES
Akram, U., Kaleem Khan, M., Tanveer, Y., et al. (2020). How website quality and perceived value trigger impulse buying in digital flash sales: The role of ego depletion. *Journal of Business Research*, 114, 289-302.

Al-Natour, S., Benbasat, I., & Cenfetelli, R. (2011). The adoption of online shopping assistants: Perceived similarity, familiarity, and competence. *Journal of the Association for Information Systems*, 12(11), 762-787.

Ampadu, S., Jiang, Y., Debrah, E., Antwi, C. O., Amankwa, E., Gyamfi, S. A., & Amoako, R. (2022). Online personalized recommended product quality and e-impulse buying: A conditional mediation analysis. *Journal of Retailing and Consumer Services*, 64, 102789. https://doi.org/10.1016/j.jretconser.2021.102789

Badgaiyan, A. J., & Verma, A. (2015). Does urge to buy impulsively differ from impulsive buying behaviour? Assessing the impact of dispositional factors. *Journal of Retailing and Consumer Services*, 22, 145-157.

Baumeister, R. F. (2002). Yielding to temptation: Self-control failure, impulsive purchasing, and consumer behavior. *Journal of Consumer Research*, 28(4), 670-676.

Baumeister, R. F., Vohs, K. D., & Tice, D. M. (2007). The strength model of self-control. *Current Directions in Psychological Science*, 16(6), 351-355.

Beatty, S. E., & Ferrell, M. E. (1998). Impulse buying: Modeling its precursors. *Journal of Retailing*, 74(2), 169-191.

Brehm, J. W. (1966). *A theory of psychological reactance*. Academic Press.

Brislin, R. W. (1970). Back-translation for cross-cultural research. *Journal of Cross-Cultural Psychology*, 1(3), 185-216.

Chan, T. K., Cheung, C. M., & Lee, Z. W. (2017). The state of online impulse-buying research: A literature analysis. *Information & Management*, 54(2), 204-217.

Do Xuan Nguyen, T., & Nguyen, K. P. N. (2026). Demystifying how emotional and cognitive resonance to AI-driven recommendations drives impulse buying. *Journal of Retailing and Consumer Services*, 89, 104646. https://doi.org/10.1016/j.jretconser.2025.104646

Eroglu, S. A., Machleit, K. A., & Davis, L. M. (2001). Atmospheric qualities of online retailing: A conceptual model and implications. *Journal of Business Research*, 54(2), 177-184.

Faul, F., Erdfelder, E., Buchner, A., & Lang, A. G. (2009). Statistical power analyses using G*Power 3.1: Tests for correlation and regression analyses. *Behavior Research Methods*, 41(4), 1149-1160.

Gallin, S., & Portes, A. (2024). Online shopping: How can algorithm performance expectancy enhance impulse buying? *Journal of Retailing and Consumer Services*, 81, 103988. https://doi.org/10.1016/j.jretconser.2024.103988

Guha, A., Grewal, D., Kopalle, P. K., et al. (2022). How artificial intelligence will transform the future of retailing and customer journeys. *Journal of the Academy of Marketing Science*, 49(1), 219-241.

Hagger, M. S., Chatzisarantis, N. L., Alberts, H., et al. (2016). A multilab preregistered replication of the ego-depletion effect. *Perspectives on Psychological Science*, 11(4), 546-573.

Hair, J. F., Risher, J. J., Sarstedt, M., & Ringle, C. M. (2019). When to use and how to report the results of PLS-SEM. *European Business Review*, 31(1), 2-24.

Hair, J. F., Hult, G. T. M., Ringle, C. M., & Sarstedt, M. (2022). *A primer on partial least squares structural equation modeling (PLS-SEM)* (3rd ed.). Sage.

Huang, J., & Ahmad, W. (2026). Mechanism of AI chatbot anthropomorphism on consumer impulse buying in live streaming scenarios based on SOR framework. *PLOS ONE*, 21, e0357787. https://doi.org/10.1371/journal.pone.0357787

Jacoby, J. (2002). Stimulus-organism-response reconsidered: An evolutionary step in modeling (consumer) behavior. *Journal of Consumer Psychology*, 12(1), 51-57.

Kline, R. B. (2016). *Principles and practice of structural equation modeling* (4th ed.). Guilford Press.

Kock, N. (2015). Common method bias in PLS-SEM: A full collinearity assessment approach. *International Journal of e-Collaboration*, 11(4), 1-10.

Komiak, S. X., & Benbasat, I. (2006). The effects of personalization and familiarity on trust and adoption of recommendation agents. *MIS Quarterly*, 30(4), 941-960.

Kulal, A., Irfana, S., Rahiman, H. U., et al. (2026). From AI Persuasion to Impulse-Compulsive Buying: The Mediating Role of Impulsivity and Ego Depletion. *International Journal of Consumer Studies*, 50, e70249. https://doi.org/10.1111/ijcs.70249

Kumaran, M. S. B., & Shobhana, N. (2026). The Persuasive Backfire of Generative AI: How Synthetic Urgency Triggers Reactance. *Journal of Promotion Management*, 32, 307-321. https://doi.org/10.1080/10496491.2026.2669635

Lau, M. M., Hui, R. T., Ng, P. M. L., & Mak, M. S. Y. (2026). Triggered to buy? The role of negative emotions and user awareness of others in driving impulse purchases in AI live streaming. *Online Information Review*, 1-16. https://doi.org/10.1108/oir-07-2025-0490

Lin, X. (2026). From scrolling to spending: Psychological mechanisms of AI-driven impulse buying. *Acta Psychologica*, 269, 107594. https://doi.org/10.1016/j.actpsy.2026.107594

Mehrabian, A., & Russell, J. A. (1974). *An approach to environmental psychology*. MIT Press.

Miao, M., Jalees, T., Zaman, S. I., et al. (2021). The influence of digital atmospherics and AI personalization on urge to buy impulsively. *Journal of Retailing and Consumer Services*, 63, 102715.

Oliver, R. L. (1980). A cognitive model of the antecedents and consequences of satisfaction decisions. *Journal of Marketing Research*, 17(4), 460-469.

Oliver, R. L. (1993). Cognitive, affective, and attribute bases of the satisfaction response. *Journal of Consumer Research*, 20(3), 418-430.

Pang, H., Wang, Y., Sun, M., & Wang, R. (2026). How artificial intelligence functionalities boost consumer benefit and impulse shopping? *Computers in Human Behavior*, 181, 108999. https://doi.org/10.1016/j.chb.2026.108999

Podsakoff, P. M., MacKenzie, S. B., Lee, J. Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research: A critical review of the literature and recommended remedies. *Journal of Applied Psychology*, 88(5), 879-903.

Rook, D. W., & Fisher, R. J. (1995). Normative influences on impulsive buying behavior. *Journal of Consumer Research*, 22(3), 305-313.

Shamim, K., & Misra, S. C. (2025). Leveraging AI to drive online impulse buying: a SOBC perspective. *International Journal of Retail & Distribution Management*, 53, 1040-1056. https://doi.org/10.1108/ijrdm-07-2024-0334

Shanahan, T., Tran, T. P., & Taylor, E. C. (2019). Getting personal: How perceived personalization enhances online customer engagement and purchase intention. *Journal of Retailing and Consumer Services*, 47, 57-65.

Spreng, R. A., MacKenzie, S. B., & Olshavsky, R. W. (1996). A reexamination of the determinants of consumer satisfaction. *Journal of Marketing*, 60(3), 15-32.

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257-285.

Tobon, S., & Abril, C. (2024). Game on: curbing impulse buying and returns in apparel e-tailers. *Review of Managerial Science*, 19, 1783-1817. https://doi.org/10.1007/s11846-024-00808-3

Verhagen, T., & van Dolen, W. (2011). The influence of online store beliefs on consumer impulsive buying: A model and empirical application. *Information & Management*, 48(8), 320-327.

Vessey, I. (1991). Cognitive fit: A theory-based analysis of the graphs versus tables literature. *Decision Sciences*, 22(2), 219-240.

Xiao, B., & Benbasat, I. (2007). E-commerce product recommendation agents: Use, characteristics, and impact. *ACM Computing Surveys*, 39(4), 1-47.

Xiao, B., & Benbasat, I. (2018). An empirical examination of the influence of biased recommendation agents on users' decision making. *Information Systems Research*, 29(4), 931-952.

Zhang, K. Z., Xu, H., Zhao, S., & Yu, Y. (2021). The impact of recommendation novelty and serendipity on impulse buying. *Computers in Human Behavior*, 124, 106932.

Zheng, X., Men, J., Yang, F., & Gong, X. (2019). Understanding impulse buying in mobile commerce: An investigation into hedonic and utilitarian browsing. *International Journal of Information Management*, 48, 151-160.

Zhu, P., Liu, Z., Li, X., Jiang, X., & Zhu, M. X. (2023). The influences of livestreaming on online purchase intention: examining platform characteristics and consumer psychology. *Industrial Management & Data Systems*, 123, 862-885. https://doi.org/10.1108/imds-07-2022-0430
