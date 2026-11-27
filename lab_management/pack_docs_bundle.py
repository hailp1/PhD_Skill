"""
H-AI ResearchLAB - DYNAMIC BUNDLE PACKAGER (pack_docs_bundle.py)
Enforces Automated Quality Gate Auditing before Packaging Manuscripts into Web Viewers.
"""

import json
import os
import sys

# Add current directory and tone audit script directory to path
sys.path.append(os.path.dirname(__file__))
WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(WORKSPACE, ".agents", "skills", "phd-dissertation-writing", "scripts"))

from academic_qa_gate import AcademicQAGate
from academic_tone_audit import audit_academic_text

def audit_paper_status(fpath, ptype):
    if not os.path.exists(fpath):
        return "Chưa Khởi Tạo"
    g = AcademicQAGate(fpath, paper_type=ptype)
    g.run_full_audit()
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        t_res = audit_academic_text(f.read())
    t_score = t_res["naturalness_score"]
    print(f"\n[TONE GATE - {ptype.upper()}] Academic Naturalness Score: {t_score}/100 (Em-dashes: {t_res['em_dash_count']})")
    if len(g.red_flags) == 0 and g.score >= 90 and t_score >= 80:
        return f"Hoàn Thiện 100% (QA: {g.score}/100 | Tone: {t_score}/100)"
    return f"Cần Chỉnh Sửa (QA: {g.score}/100 | Tone: {t_score}/100 | Flags: {len(g.red_flags)})"

MANUSCRIPT_FILE = os.path.join(WORKSPACE, "lab_projects", "PAPER_01_SLR_JRCS_MANUSCRIPT.md")
PAPER2_FILE = os.path.join(WORKSPACE, "lab_projects", "PAPER_02_EMPIRICAL_CHB_MANUSCRIPT.md")

paper1_status = audit_paper_status(MANUSCRIPT_FILE, "slr")
paper2_status = audit_paper_status(PAPER2_FILE, "empirical")

print(f"\n[PACKAGER] Dynamic Status for Paper 1: {paper1_status}")
print(f"[PACKAGER] Dynamic Status for Paper 2: {paper2_status}")

docs_to_pack = {
    'paper1': (
        'lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md',
        'Paper 01: SLR & Bibliometrics (JRCS Q1)',
        'JRCS Q1 (IF: 11.0)',
        paper1_status
    ),
    'paper2': (
        'lab_projects/PAPER_02_EMPIRICAL_CHB_MANUSCRIPT.md',
        'Paper 02: Empirical Protocol (CHB Q1)',
        'CHB Q1 (IF: 9.0)',
        paper2_status
    ),
    'plan': (
        'lab_projects/AUTOMATED_PAPER_WRITING_PLAN.md',
        'Kế Hoạch Bài Báo Mới (IMRAD Blueprint)',
        'H-AI Engine',
        'Scopus Q1 Plan'
    ),
    'survey': (
        'docs/survey_instrument.md',
        'Paper 2: Bảng Hỏi Khảo Sát Thực Nghiệm',
        'N = 450 (Likert 7)',
        '28 Items'
    ),
    'proposal': (
        'docs/proposal_detailed.md',
        'Đề Cương Nghiên Cứu Tiến Sĩ Chi Tiết',
        'TDTU Ph.D.',
        'Đề Cương Chuẩn'
    ),
    'baumeister': (
        'lab_projects/parsed_markdown/baumeister_2002.md',
        'Toàn Văn: Baumeister (2002) - Ego Depletion',
        'JCR FT50',
        'Lý Thuyết Nền'
    ),
    'shanahan': (
        'lab_projects/parsed_markdown/shanahan_2019.md',
        'Toàn Văn: Shanahan (2019) - Thang Đo PP',
        'JRCS Q1',
        'Thang Đo Gốc'
    ),
    'beatty': (
        'lab_projects/parsed_markdown/beatty_1998.md',
        'Toàn Văn: Beatty & Ferrell (1998) - Thang Đo UBI',
        'J. Retailing Q1',
        'Thang Đo Gốc'
    ),
    'verhagen': (
        'lab_projects/parsed_markdown/verhagen_2011.md',
        'Toàn Văn: Verhagen & van Dolen (2011) - Khung S-O-R',
        'I&M Q1',
        'Khung Lý Thuyết'
    )
}

bundle = {}
for k, (fpath, title, tag, status) in docs_to_pack.items():
    full_path = os.path.join(WORKSPACE, fpath.replace("/", os.sep))
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
            bundle[k] = {
                'title': title,
                'tag': tag,
                'status': status,
                'path': fpath,
                'markdown': md_text
            }
        print(f"Packed {k}: {len(md_text):,} chars")

bundle_json_path = os.path.join(WORKSPACE, 'lab_projects', 'DOCUMENTS_BUNDLE.json')
with open(bundle_json_path, 'w', encoding='utf-8') as f:
    json.dump(bundle, f, ensure_ascii=False, indent=2)

# Also generate DOCS_INLINE.js for instant 0ms offline reader
js_content = "window.INLINE_DOCS_BUNDLE = " + json.dumps(bundle, ensure_ascii=False, indent=2) + ";\n"
inline_js_path = os.path.join(WORKSPACE, 'lab_projects', 'DOCS_INLINE.js')
with open(inline_js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

# If web directory exists, copy there too
import shutil
web_target_dir = os.path.join(WORKSPACE, 'web', 'lab_projects')
if os.path.exists(web_target_dir):
    shutil.copy(bundle_json_path, os.path.join(web_target_dir, 'DOCUMENTS_BUNDLE.json'))
    shutil.copy(inline_js_path, os.path.join(web_target_dir, 'DOCS_INLINE.js'))

web_root_dir = os.path.join(WORKSPACE, 'web')
if os.path.exists(web_root_dir):
    shutil.copy(bundle_json_path, os.path.join(web_root_dir, 'DOCUMENTS_BUNDLE.json'))
    shutil.copy(inline_js_path, os.path.join(web_root_dir, 'DOCS_INLINE.js'))

print("[SUCCESS] Packaged DOCUMENTS_BUNDLE.json and DOCS_INLINE.js with dynamic QA Gate status verification!")
