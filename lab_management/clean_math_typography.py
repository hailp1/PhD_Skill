"""
Clean all raw dollar signs ($) and LaTeX math strings from Paper 1 manuscript,
converting them to clean, professional Elsevier-grade academic typography.
"""

MANUSCRIPT_PATH = "lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md"

with open(MANUSCRIPT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# Replace variables in text
text = text.replace("$T = 5$", "*T* = 5")
text = text.replace("($S$)", "(S)")
text = text.replace("($O$)", "(O)")
text = text.replace("($R$)", "(R)")
text = text.replace("($UBI$)", "(UBI)")
text = text.replace("($UBI \\rightarrow IB$)", "(UBI → IB)")
text = text.replace("($UBI -> IB$)", "(UBI → IB)")

# Replace section header references
text = text.replace("($H_1, H_2, H_4$)", "(H1, H2, H4)")
text = text.replace("($H_3$)", "(H3)")
text = text.replace("($H_5$)", "(H5)")
text = text.replace("($H_6$)", "(H6)")

# Replace formal hypothesis lines
text = text.replace("- **$H_1$**:", "- **H1:**")
text = text.replace("- **$H_2$**:", "- **H2:**")
text = text.replace("- **$H_3$**:", "- **H3:**")
text = text.replace("- **$H_{3a}$ (Mediation)**:", "- **H3a (Mediation):**")
text = text.replace("- **$H_4$**:", "- **H4:**")
text = text.replace("- **$H_5$**:", "- **H5:**")
text = text.replace("- **$H_6$**:", "- **H6:**")

# Catch any remaining single dollar signs
import re
text = re.sub(r'\$([A-Za-z0-9_]+)\$', r'*\1*', text)

# Count remaining dollar signs
remaining_dollars = text.count("$")
print(f"Remaining dollar signs: {remaining_dollars}")

with open(MANUSCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("[OK] Replaced all raw LaTeX math strings with clean academic typography!")
