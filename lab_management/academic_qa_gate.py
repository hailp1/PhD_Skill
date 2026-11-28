"""
H-AI ResearchLAB - CORE ACADEMIC QUALITY & INTEGRITY GATE (academic_qa_gate.py)
Automated Verification & Adversarial Auditing Harness for Scopus Q1 / Elsevier JRCS Submissions.
Enforces 0-Tolerance Anti-Hallucination, Agnostic PRISMA Searches, Metric Consistency, and Citation Integrity.
"""

import re
import os
import sys
import json

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MANUSCRIPT_PATH = os.path.join(WORKSPACE_DIR, "lab_projects", "PAPER_01_SLR_JRCS_MANUSCRIPT.md")
CORPUS_CSV = os.path.join(WORKSPACE_DIR, "data", "processed", "dimensions_clean_included.csv")

class AcademicQAGate:
    def __init__(self, manuscript_path=MANUSCRIPT_PATH, paper_type="slr"):
        self.manuscript_path = manuscript_path
        self.paper_type = paper_type.lower()
        self.text = ""
        self.red_flags = []
        self.warnings = []
        self.score = 100 # Starts at 100, deducted per error
        self.load_manuscript()

    def load_manuscript(self):
        if not os.path.exists(self.manuscript_path):
            self.red_flags.append(f"FATAL: Manuscript not found at {self.manuscript_path}")
            return
        with open(self.manuscript_path, "r", encoding="utf-8") as f:
            raw = f.read()
            # Strip base64 data to avoid false positive substring matches in binary image strings
            self.text = re.sub(r'data:image/[^"]+', '', raw)

    def audit_prisma_search_query(self):
        """Gate 1: Check for Confirmation Bias & Broken Syntax in Boolean Search (SLR only)."""
        if self.paper_type != "slr":
            print("[CHECK 1] Skipping PRISMA Boolean check (Empirical Protocol paper)...")
            return
        print("[CHECK 1] Auditing PRISMA Boolean Search Strategy...")
        # Check if search string contains circular variables
        search_match = re.search(r'(?:Boolean query|search string|Search Strategy)[^\n]*\n+```[^\n]*\n([\s\S]*?)```', self.text, re.IGNORECASE)
        search_text = search_match.group(1) if search_match else self.text[:5000]

        # 1. Circular logic check
        circular_terms = ["e-satisfaction", "online satisfaction", "S-O-R", "stimulus-organism-response"]
        for term in circular_terms:
            if re.search(r'\b' + re.escape(term) + r'\b', search_text, re.IGNORECASE):
                self.red_flags.append(f"CONFIRMATION BIAS: Boolean query contains predefined mediator/theory '{term}', causing tautological circular reasoning.")
                self.score -= 20

        # 2. Cut-off words check
        cut_words = [r'"smar\b', r'"impu\b', r'\bsmar"', r'\bimpu"']
        for cw in cut_words:
            if re.search(cw, search_text, re.IGNORECASE):
                self.red_flags.append(f"SYNTAX CORRUPTION: Broken/truncated keyword detected in Boolean query matching pattern '{cw}'.")
                self.score -= 10

    def audit_vosviewer_methodology(self):
        """Gate 2: Check for VOSviewer Metric Consistency & Graph Topology (SLR) or Brislin/G*Power (Empirical)."""
        if self.paper_type != "slr":
            print("[CHECK 2] Auditing Empirical Methodology (G*Power, Brislin & PLS-SEM)...")
            if not re.search(r'G\*Power|Brislin|PLS-SEM', self.text, re.IGNORECASE):
                self.red_flags.append("EMPIRICAL METHODOLOGY MISSING: Must specify G*Power, Brislin back-translation, or PLS-SEM protocol.")
                self.score -= 15
            return
        print("[CHECK 2] Auditing VOSviewer Terminology & Graph Logic...")
        # Check if co-word mentions citations threshold instead of occurrences
        if re.search(r'co-word[^\n]*threshold of [^\n]*citations', self.text, re.IGNORECASE):
            self.red_flags.append("METRIC ERROR: Co-word occurrence analysis incorrectly specifies 'citations' instead of 'occurrences'.")
            self.score -= 15

        # Check for disconnected graph contradiction (866 nodes vs 250 links without explanation)
        if re.search(r'866 nodes[^\n]*250[^\n]*links', self.text, re.IGNORECASE):
            self.warnings.append("GRAPH TOPOLOGY WARNING: 866 nodes with only 250 links implies a disconnected network. Must clarify units (e.g. top co-occurrence links or cluster components).")
            self.score -= 5

    def audit_hypotheses_vs_propositions(self):
        """Gate 3: Ensure SLR uses Propositions (P) while Empirical uses Hypotheses (H)."""
        print("[CHECK 3] Auditing Hypotheses vs. Propositions Standard...")
        if self.paper_type == "slr":
            h_pattern = re.findall(r'\bH[1-6][a-z]?\b\s*:', self.text)
            if h_pattern:
                self.red_flags.append(f"METHODOLOGY MISMATCH: Found {len(h_pattern)} Hypotheses (e.g. {h_pattern[:3]}). SLR/Conceptual paper must use Propositions (P1-P9) unless MASEM is conducted.")
                self.score -= 15
        else:
            h_found = re.findall(r'\bH[1-9][a-z]?\b', self.text)
            if len(h_found) < 4:
                self.red_flags.append("EMPIRICAL HYPOTHESES MISSING: Empirical paper must formulate explicit testable Hypotheses (H1-H9).")
                self.score -= 15

    def audit_citation_hallucinations_and_typos(self):
        """Gate 4: Check for Known Hallucinated Citations, Typos, and Mismatches."""
        print("[CHECK 4] Auditing Citation Integrity & Anti-Hallucination Gate...")
        
        # 1. Known mismatched citations
        mismatched = [
            ("Pillai", "Hospitality/COVID paper misattributed to e-commerce algorithms"),
            ("Ramsin", "Object-oriented software paper misattributed to collaborative filtering"),
            ("Blut", "Chatbot paper misattributed to 40%-60% impulse sales stats")
        ]
        for author, reason in mismatched:
            if re.search(r'\b' + author + r'\b', self.text, re.IGNORECASE):
                self.red_flags.append(f"CITATION RED FLAG: Author '{author}' detected ({reason}). Must be removed or replaced with authentic e-commerce literature.")
                self.score -= 20

        # 2. Known author typos, retracted/predatory leaks, & reviewer-flagged metadata hallucinations
        typos = [
            (r'\blice,?\s+D\.?\s*M\.?', "Tice, D. M."),
            (r'\bBenpasat\b', "Benbasat"),
            (r'\baftective\b', "affective"),
            (r'70/30\s+rule', "Unsubstantiated 70/30 heuristic"),
            (r'RETRACTED ARTICLE|retraction notice', "Retracted article cited in manuscript"),
            (r'\bZenodo\b|\bOALib\b|\bIJARSCT\b|\bIJRSI\b|World Journal of Advanced Research', "Non-peer-reviewed preprint or predatory outlet leaked into corpus"),
            (r'Xiao[^\n]{0,80}2007[^\n]{0,120}ACM Computing Surveys', "Xiao & Benbasat (2007) was published in MIS Quarterly 31(1), not ACM Computing Surveys"),
            (r'Guha[^\n]{0,120}2022[^\n]{0,120}Journal of the Academy of Marketing Science', "Guha et al. (2021) was published in Journal of Retailing 97(1), not JAMS 2022"),
            (r'Mariani[^\n]{0,80}Bontis[^\n]{0,40}2023', "Mariani, Perez-Vega, & Wirtz (2022) P&M 39(4), not Bontis 2023"),
            (r'Sundar[^\n]{0,80}2019[^\n]{0,120}Computers in Human Behavior', "Sundar & Kim (2019) was published at CHI '19, not CHB"),
            (r'Zheng[^\n]{0,100}2019[^\n]{0,120}social support and credibility', "Zheng et al. (2019) IJIM 48 is about hedonic/utilitarian browsing, not social support"),
            (r'\b100%\s+verified\b|\bgold\s+standard\b|\bexceptionally\s+high\b', "Remove self-praise / unsubstantiated boastful phrasing"),
            (r'Arousal\s*>\s*UBI', "Invalid math '>' notation for causal arrow; use '->' or equation format"),
        ]
        for pattern, correction in typos:
            if re.search(pattern, self.text, re.IGNORECASE):
                self.red_flags.append(f"TYPO / UNSUBSTANTIATED CLAIM: Detected pattern matching '{pattern}'. Correction/Removal required: {correction}.")
                self.score -= 10

        # 3. 5-pillar research agenda completeness
        agenda_match = re.search(r'5-pillar[^\n]*agenda([\s\S]*?)(?:5\.5|6\.|\Z)', self.text, re.IGNORECASE)
        if agenda_match:
            agenda_text = agenda_match.group(1)
            pillars = re.findall(r'(?:Pillar|Item|\d\.)\s*[A-Z]', agenda_text)
            if len(pillars) < 5:
                self.red_flags.append(f"COMPLETENESS ERROR: 5-pillar research agenda promised, but only {len(pillars)} pillars articulated.")
                self.score -= 10

    def audit_references_and_rendering(self):
        """Gate 5: Check Reference Depth (>=80), Zero Al-typos, Zero Em-dashes, Zero HTML Leaks."""
        print("[CHECK 5] Auditing Reference Depth, Formatting & HTML Render Safety...")
        # Check reference count (supports both clean APA paragraphs and legacy '- ' lines)
        min_refs = 80 if self.paper_type == "slr" else 25
        ref_section = re.search(r'## REFERENCES([\s\S]*)$', self.text)
        if ref_section:
            ref_lines = [l.strip() for l in ref_section.group(1).strip().split('\n') if l.strip() and not l.strip().startswith('#')]
            if len(ref_lines) < min_refs:
                self.red_flags.append(f"REFERENCE DEPTH DEFICIT: Found {len(ref_lines)} references. Requires >= {min_refs} verified references.")
                self.score -= 15

        # Check Al-Driven typo (case-sensitive)
        if re.search(r'\bAl-Driven\b|\bAl\s+Recommender', self.text):
            self.red_flags.append("TYPOGRAPHY ERROR: Case-sensitive 'Al-' (lowercase L) detected instead of 'AI-'.")
            self.score -= 10

        # Check em-dashes in body prose (exclude References section so verbatim published titles are preserved)
        body_prose = re.split(r'^##\s+REFERENCES\b', self.text, flags=re.MULTILINE)[0]
        em_dashes = len(re.findall(r'—', body_prose))
        if em_dashes > 0:
            self.red_flags.append(f"AI STYLE MARKER: Detected {em_dashes} em-dashes ('—') in manuscript body. Replace with scholarly commas/parentheses.")
            self.score -= 10

        # Check PRISMA 2020 Limitations presence for SLR
        if self.paper_type == "slr" and not re.search(r'^#{2,3}\s+.*Limitations\b', self.text, re.MULTILINE | re.IGNORECASE):
            self.red_flags.append("PRISMA 2020 DEFICIT: Missing dedicated Limitations subsection (Item 23c).")
            self.score -= 10

        # Check blank lines inside academic-figure-container (causes marked.js raw HTML leak)
        fig_blocks = re.findall(r'<div class="academic-figure-container"[\s\S]*?<\/div>\s*<\/div>', self.text)
        for idx, blk in enumerate(fig_blocks, 1):
            if '\n\n' in blk:
                self.red_flags.append(f"RENDERING LEAK: Figure/Table block #{idx} contains blank lines that break marked.js HTML parsing.")
                self.score -= 15

    def audit_two_way_citations(self):
        """Gate 6: Strict 1-to-1 Two-Way Citation Parity & Pure APA 7th Format."""
        print("[CHECK 6] Auditing Two-Way Citation Parity & APA 7th Format...")
        parts = re.split(r'^##\s+REFERENCES\b', self.text, flags=re.MULTILINE)
        if len(parts) < 2:
            self.red_flags.append("MISSING REFERENCES SECTION.")
            self.score -= 20
            return
        body, refs_sec = parts[0], parts[1]

        ref_lines = [l.strip() for l in refs_sec.strip().split('\n') if l.strip() and not l.strip().startswith('#')]
        uncited_refs = []
        bad_apa_refs = []
        for rl in ref_lines:
            # Check for raw semicolon author separator
            if ';' in rl.split('(')[0]:
                bad_apa_refs.append(rl[:60])
            # Extract first surname and year (including 2026a/2026b)
            m_year = re.search(r'\((\d{4}[a-z]?)\)', rl)
            if m_year:
                yr = m_year.group(1)
                first_word = re.sub(r'^[-\u2022]\s*', '', rl).split(',')[0].split()[0].strip()
                # Check if first_word and yr appear in body (both parenthetical and narrative forms)
                if not re.search(r'\b' + re.escape(first_word) + r'[^\n]{0,45}\b' + yr + r'\b', body):
                    uncited_refs.append(f"{first_word} ({yr})")

        if bad_apa_refs:
            self.red_flags.append(f"APA FORMAT ERROR: Found {len(bad_apa_refs)} references using semicolons ';' instead of APA 7th commas & '&' (e.g. {bad_apa_refs[0]}).")
            self.score -= 15
        if uncited_refs:
            self.red_flags.append(f"REFERENCE PADDING ERROR: Found {len(uncited_refs)} uncited references in References list (e.g. {uncited_refs[:5]}).")
            self.score -= 20

        # Live/Cached Crossref DOI, Retraction & Collision Gate
        try:
            from crossref_ref_auditor import audit_manuscript_dois
            doi_issues = audit_manuscript_dois(self.manuscript_path)
            if doi_issues:
                for di in doi_issues[:5]:
                    self.red_flags.append(f"CROSSREF GATE: {di}")
                self.score -= 20
        except Exception as e:
            self.warnings.append(f"Crossref DOI gate skipped: {e}")

    def run_full_audit(self):
        print("=" * 80)
        print("🔬 H-AI ResearchLAB | CORE ACADEMIC QUALITY AUDIT")
        print("=" * 80)
        self.audit_prisma_search_query()
        self.audit_vosviewer_methodology()
        self.audit_hypotheses_vs_propositions()
        self.audit_citation_hallucinations_and_typos()
        self.audit_references_and_rendering()
        self.audit_two_way_citations()

        self.score = max(0, self.score)
        print("\n" + "=" * 80)
        print(f"📊 OVERALL ACADEMIC QUALITY SCORE: {self.score}/100")
        print("=" * 80)

        if self.red_flags:
            print(f"\n❌ FOUND {len(self.red_flags)} RED FLAGS (REJECTED FOR Q1 SUBMISSION):")
            for idx, rf in enumerate(self.red_flags, 1):
                print(f"   [{idx}] {rf}")
        else:
            print("\n✅ ZERO RED FLAGS! Manuscript meets international academic integrity standards.")

        if self.warnings:
            print(f"\n⚠️ FOUND {len(self.warnings)} WARNINGS:")
            for idx, w in enumerate(self.warnings, 1):
                print(f"   [{idx}] {w}")

        return len(self.red_flags) == 0

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="H-AI Lab Academic QA Gate")
    parser.add_argument("--file", type=str, default=MANUSCRIPT_PATH, help="Path to manuscript")
    parser.add_argument("--type", type=str, default="slr", choices=["slr", "empirical"], help="Paper type")
    args = parser.parse_args()
    gate = AcademicQAGate(manuscript_path=args.file, paper_type=args.type)
    passed = gate.run_full_audit()
    sys.exit(0 if passed else 1)
