---
name: phd-dissertation-writing
description: >-
  Use this skill when drafting, reviewing, or polishing chapters of a PhD dissertation or converting thesis chapters into Scopus/WoS journal articles in Marketing and Business Administration. It enforces the 5-chapter dissertation structure, rigorous academic discussion formatting, theoretical contributions, managerial implications, academic phrasing, and APA 7th presentation.
---

# PhD Dissertation Writing & Publication Skill (Marketing & Business Administration)

This skill guides the composition of a complete 5-chapter doctoral dissertation (Luận án Tiến sĩ) and supports formatting empirical findings for publication in top-tier peer-reviewed marketing and management journals.

## Quick Reference Resources
- Standard 5-Chapter Dissertation Structure: [dissertation_structure_template.md](./resources/dissertation_structure_template.md)
- Academic Phrasebank for Marketing: [academic_phrasebank_marketing.md](./resources/academic_phrasebank_marketing.md)
- Anti-AI & Academic Hedging Guide: [anti_ai_academic_hedging_guide.md](./references/anti_ai_academic_hedging_guide.md)
- Academic Tone Audit Script: [academic_tone_audit.py](./scripts/academic_tone_audit.py)
- Scopus/WoS Q1/Q2 Publication Strategy: [journal_publication_strategy.md](./references/journal_publication_strategy.md)

---

## Step-by-Step Procedure

### 1. Structure the Dissertation Across the 5 Canonical Chapters
Doctoral institutions in Vietnam and globally universally require the 5-chapter structure:
- **Chương 1: Tổng quan và Tính cấp thiết của Đề tài (Introduction & Rationale)**
- **Chương 2: Cơ sở Lý thuyết, Tổng quan Nghiên cứu & Giả thuyết (Theoretical Background & Hypotheses)**
- **Chương 3: Phương pháp Nghiên cứu (Research Methodology)**
- **Chương 4: Kết quả Nghiên cứu Thực nghiệm và Thảo luận (Empirical Findings & Academic Discussion)**
- **Chương 5: Đóng góp Mới, Hàm ý Quản trị, Hạn chế & Hướng Nghiên cứu Tiếp theo (Contributions, Implications & Limitations)**
- Detail-level breakdown available at [dissertation_structure_template.md](./resources/dissertation_structure_template.md).

### 2. Draft the "Discussion" Section (Chương 4) with Deep Criticality
The Discussion section differentiates a doctoral thesis from a master's thesis. It must NOT merely restate numbers:
- **Three-Pronged Discussion Formula**:
  1. *Factual Finding*: State whether the hypothesis was supported (Path coefficient $\beta$, $t$-value, $p$-value).
  2. *Dialogue with Prior Literature*: Compare with seminal studies. Does this finding corroborate (e.g., Wang et al., 2022) or contradict (e.g., Kim et al., 2024) earlier findings?
  3. *Theoretical Justification*: Explain *why* this relationship occurred in this specific context using the grounding theory (e.g., S-O-R or Cognitive Appraisal).

### 3. Articulate Theoretical & Managerial Contributions (Chương 5)
- **Theoretical Contributions (Đóng góp về mặt học thuật/lý thuyết)**:
  - Do not state obvious generalities. Explicitly state how the findings advance theory (e.g., *“This dissertation extends the Stimulus-Organism-Response (S-O-R) paradigm into conversational AI interactions by revealing that...”*).
  - Highlight the identification of novel boundary conditions or mediation paths.
- **Managerial / Practical Implications (Hàm ý quản trị thực tiễn)**:
  - Organize into actionable, operational recommendations for Marketing Directors, Product Managers, and Policy Makers.
  - Break down into Strategic Level (Tầm nhìn/Định vị) and Operational Level (Triển khai/Công cụ tiếp thị).

### 4. Polish Academic Prose & Enforce Academic Hedging (Anti-AI Protocol)
- Maintain formal scholarly tone: objective, hedged (avoiding unfounded absolute assertions like "proves 100%"), logically chained with cohesive transitional signposts.
- Utilize [academic_phrasebank_marketing.md](./resources/academic_phrasebank_marketing.md) for scholarly sentence templates.
- **Mandatory Anti-AI Check**:
  - Follow [anti_ai_academic_hedging_guide.md](./references/anti_ai_academic_hedging_guide.md) to eliminate clichés (*delve into, tapestry, testament to, beacon, bức tranh toàn cảnh, minh chứng hùng hồn...*).
  - Convert any absolute, boastful statements into disciplined academic hedging (*suggests, lends support to, within the boundary conditions of...*).
  - Run the automated audit script on your draft:
    ```bash
    python .agents/skills/phd-dissertation-writing/scripts/academic_tone_audit.py --file draft_chapter.md
    ```

### 5. Format Figures and Tables to APA 7th Standard
- **Tables**: Clean horizontal borders only (Top border, Header separator border, Bottom border; NO vertical lines).
- **Numbers**: Round path coefficients to 3 decimal places, $p$-values to 3 decimal places (e.g., $p < 0.001$, $p = 0.042$).
- Include table note explaining abbreviations (e.g., *Note: *** $p < 0.001$, ** $p < 0.01$, * $p < 0.05$*).
