---
name: phd-data-analysis
description: >-
  Use this skill when analyzing empirical research data, testing measurement models, evaluating structural equation models (PLS-SEM or CB-SEM), conducting mediation/moderation analyses, or checking for Common Method Bias (CMB) in Marketing and Business Administration dissertations. It includes Python automation scripts and step-by-step reporting guidelines following Hair et al. (2019, 2022).
---

# PhD Quantitative Data Analysis & SEM Skill (Marketing & Business Administration)

This skill directs the statistical analysis and reporting for empirical doctoral dissertations in Marketing and Business Administration, adhering to rigorous reporting standards for PLS-SEM (SmartPLS, semopy) and CB-SEM (AMOS, lavaan).

## Quick Reference Resources
- Python Data Analysis Script: [research_data_toolkit.py](./scripts/research_data_toolkit.py)
- SEM Analysis & Reporting Guide: [sem_analysis_guide.md](./references/sem_analysis_guide.md)

---

## Step-by-Step Procedure

### 1. Data Cleaning and Preliminary Screening
- **Missing Values**: Ensure listwise or pairwise deletion, or use Expectation-Maximization / Mean Imputation if missingness $< 5\%$.
- **Outliers**: Screen univariate outliers ($z$-scores beyond $\pm 3.29$) and multivariate outliers (Mahalanobis distance $D^2$, $p < 0.001$).
- **Univariate & Multivariate Normality**:
  - Check Skewness (threshold: $|\text{Skew}| < 2.0$) and Kurtosis (threshold: $|\text{Kurt}| < 7.0$) per Kline (2016).
  - If data deviates strongly from multivariate normality, **PLS-SEM** is strongly preferred over CB-SEM (Hair et al., 2019).
- Run automated screening via Python:
  ```bash
  python .agents/skills/phd-data-analysis/scripts/research_data_toolkit.py --file your_data.csv --task descriptive
  ```

### 2. Common Method Bias (CMB) Assessment
Because survey respondents self-report both independent and dependent variables in cross-sectional research, CMB must be rigorously ruled out:
- **Harman's Single Factor Test**:
  - Run unrotated Principal Component Analysis on all perceptual items.
  - The first unrotated factor must account for **less than 50% of the total variance** (Podsakoff et al., 2003).
  - Run automated check:
    ```bash
    python .agents/skills/phd-data-analysis/scripts/research_data_toolkit.py --file your_data.csv --task harman
    ```
- **Full Collinearity Assessment (PLS-SEM)**:
  - Check Variance Inflation Factor (VIF) for all latent constructs. VIF values should be $\le 3.3$ (Kock, 2015).

### 3. Measurement Model Evaluation (Outer Model)
Report the 3 pillars of measurement quality:
1. **Indicator Reliability**: Outer loadings $\ge 0.708$ (items between 0.40 and 0.708 should only be deleted if removal increases Composite Reliability or AVE above thresholds).
2. **Internal Consistency Reliability**:
   - Cronbach's Alpha ($\alpha \ge 0.70$)
   - Composite Reliability ($\text{CR} \ge 0.70$)
3. **Convergent Validity**:
   - Average Variance Extracted ($\text{AVE} \ge 0.50$)
4. **Discriminant Validity**:
   - **HTMT Criterion (Heterotrait-Monotrait Ratio)**: Must be $< 0.85$ (conservative threshold) or $< 0.90$ (liberal threshold) (Henseler et al., 2015).
   - **Fornell-Larcker Criterion**: The square root of AVE for each construct must exceed its correlations with any other construct.

### 4. Structural Model Evaluation (Inner Model & Hypotheses Testing)
1. **Collinearity of Structural Model**: Lateral VIFs must be $< 3.0$ (or $< 5.0$).
2. **Coefficient of Determination ($R^2$)**:
   - $R^2 \ge 0.75$: Substantial
   - $R^2 \ge 0.50$: Moderate
   - $R^2 \ge 0.25$: Weak
3. **Effect Size ($f^2$)**:
   - $f^2 \ge 0.02$: Small
   - $f^2 \ge 0.15$: Medium
   - $f^2 \ge 0.35$: Large
4. **Significance of Path Coefficients ($\beta$)**:
   - Run Bootstrapping with $5,000$ to $10,000$ subsamples.
   - Report $\beta$, standard error, $t$-statistic ($t > 1.96$ for $p < 0.05$; $t > 2.58$ for $p < 0.01$), and 95% Bias-Corrected Confidence Intervals (CI must not include zero).

### 5. Advanced Mechanism Testing
- **Mediation Analysis (Indirect Effects)**:
  - Calculate indirect path $a \times b$ via Preacher & Hayes bootstrapping.
  - If indirect effect is significant and direct effect $c'$ is not significant $\rightarrow$ **Full mediation**.
  - If both indirect and direct effects are significant and have the same sign $\rightarrow$ **Complementary partial mediation**.
  - If opposite sign $\rightarrow$ **Competitive partial mediation**.
- **Moderation Analysis (Interaction Effects)**:
  - Standardize variables (z-scores) before creating product terms.
  - Plot simple slope analysis (low moderator $-1\text{SD}$, mean, high moderator $+1\text{SD}$).
