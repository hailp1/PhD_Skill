---
name: phd-methodology-design
description: >-
  Use this skill when designing research methodology, operationalizing constructs, developing/adapting measurement scales, calculating sample size, or creating survey questionnaires for a PhD dissertation in Marketing and Business Administration. It covers research philosophy, qualitative expert panels, back-translation protocols, sampling techniques (G*Power, Hair et al.), and survey instrument design.
---

# PhD Research Methodology & Scale Design Skill (Marketing & Business Administration)

This skill provides comprehensive guidance for designing a rigorous, empirically defensible research methodology for doctoral dissertations in Marketing and Business Administration.

## Quick Reference Resources
- Scale Development & Adaptation Protocol: [scale_development_protocol.md](./resources/scale_development_protocol.md)
- Sample Size Calculation Guidelines: [sample_size_guidelines.md](./resources/sample_size_guidelines.md)
- Survey Questionnaire Template: [survey_questionnaire_template.md](./resources/survey_questionnaire_template.md)

---

## Step-by-Step Procedure

### 1. Articulate Research Philosophy & Design
- **Research Paradigm**:
  - *Positivism (Thực chứng)*: Standard for quantitative survey/experiment research testing deductive hypotheses.
  - *Interpretivism/Constructivism (Diễn giải)*: Appropriate for qualitative, inductive grounded theory studies.
  - *Pragmatism (Thực dụng)*: Standard for mixed-methods research (Qual $\rightarrow$ Quan).
- **Research Design Type**:
  - *Sequential Exploratory Mixed-Methods*: Qualitative study (depth interviews/focus groups) to contextualize constructs $\rightarrow$ Large-scale Quantitative survey to test hypotheses.
  - *Cross-Sectional Survey vs Experimental Design (2x2 factorial)*: Choose based on whether causal manipulation is required.

### 2. Operationalize Constructs & Adapt Scales
Never create scales from scratch if validated instruments exist in high-impact literature (JM, JAMS, JCR, JBR):
- **Scale Identification**: Select scales with proven reliability (Cronbach's $\alpha > 0.80$) and convergent validity from Q1 journals.
- **Scale Type**: Standardize on 5-point or 7-point Likert scales (1 = Strongly Disagree to 5/7 = Strongly Agree). 7-point scales provide greater variance for structural equation modeling.
- **Translation & Contextual Adaptation**:
  - Step 1: Forward translation (English $\rightarrow$ Vietnamese) by subject-matter bilingual researchers.
  - Step 2: Backward translation (Vietnamese $\rightarrow$ English) by an independent translator.
  - Step 3: Synthesis and reconciliation of semantic discrepancies.
  - Follow [scale_development_protocol.md](./resources/scale_development_protocol.md).

### 3. Qualitative Validation (Expert Panel & Pilot Testing)
- **Expert Review Panel**: Conduct semi-structured discussions with 5–8 experts (academic professors and industry marketing directors) to assess face validity and content validity.
- **Pilot Study**: Administer the preliminary questionnaire to a pilot sample of $N = 50 - 100$ respondents.
  - Check item clarity, completion time, and preliminary Cronbach's $\alpha$ (delete items with item-total correlation $< 0.30$).

### 4. Determine Sampling Strategy & Sample Size
- **Sampling Strategy**:
  - *Probability Sampling*: Simple random, stratified (ideal, but often difficult in B2C/B2B consumer surveys).
  - *Non-Probability Sampling*: Purposive (chọn mẫu có mục đích) combined with quota sampling (định ngạch theo độ tuổi/khu vực) or snowball sampling. Include rigorous screening questions.
- **Sample Size Determination**:
  - *Statistical Power via G\*Power*: Calculate required sample based on effect size ($f^2 = 0.15$), $\alpha = 0.05$, and power ($1 - \beta = 0.80 - 0.95$).
  - *Hair et al. Rule of Thumb*: 10 times the maximum number of structural paths directed at an endogenous construct (minimum 200–400 for SEM).
  - *Observation-to-Item Ratio*: Minimum 5:1 (preferably 10:1) ratio of respondents per survey item. For a 40-item scale, minimum valid $N = 400$.
  - Consult [sample_size_guidelines.md](./resources/sample_size_guidelines.md) for formulas and tables.

### 5. Structure the Survey Instrument (Questionnaire)
Structure following [survey_questionnaire_template.md](./resources/survey_questionnaire_template.md):
- **Section 1**: Introduction, research ethics, confidentiality guarantee, consent.
- **Section 2**: Screening questions (e.g., "Have you purchased online via AI recommendations in the last 3 months?").
- **Section 3**: Core construct measurement items (randomized item order within blocks to mitigate common method bias).
- **Section 4**: Demographic and classification variables (placed at the end to minimize cognitive fatigue).
