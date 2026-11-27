"""
H-AI ResearchLAB - REGISTRY-DRIVEN BUNDLE PACKAGER (pack_docs_bundle.py v3.0)
Reads active manuscripts dynamically from RESEARCH_PROJECTS_PIPELINE.json,
audits each via AcademicQAGate + AcademicToneAudit, updates scores back into
the registry, and packages all documents for offline/web readers.
"""

import json
import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(__file__))
WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(WORKSPACE, ".agents", "skills", "phd-dissertation-writing", "scripts"))

from academic_qa_gate import AcademicQAGate
from academic_tone_audit import audit_academic_text

PIPELINE_FILE = os.path.join(WORKSPACE, "lab_management", "RESEARCH_PROJECTS_PIPELINE.json")


def audit_paper_status(fpath, ptype):
    if not os.path.exists(fpath):
        return "Chưa Khởi Tạo", None, None
    g = AcademicQAGate(fpath, paper_type=ptype)
    g.run_full_audit()
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        t_res = audit_academic_text(f.read())
    t_score = t_res["naturalness_score"]
    print(f"\n[TONE GATE - {ptype.upper()}] Academic Naturalness Score: {t_score}/100 (Em-dashes: {t_res['em_dash_count']})")
    if len(g.red_flags) == 0 and g.score >= 90 and t_score >= 80:
        return f"Hoàn Thiện 100% (QA: {g.score}/100 | Tone: {t_score}/100)", g.score, t_score
    return f"Cần Chỉnh Sửa (QA: {g.score}/100 | Tone: {t_score}/100 | Flags: {len(g.red_flags)})", g.score, t_score


def main():
    with open(PIPELINE_FILE, "r", encoding="utf-8") as f:
        pipeline = json.load(f)

    docs_to_pack = {}
    for proj in pipeline.get("projects", []):
        rel_path = proj.get("manuscript_file")
        if not rel_path:
            continue
        abs_path = os.path.join(WORKSPACE, rel_path)
        if not os.path.exists(abs_path):
            continue

        ptype = proj.get("paper_type", "slr")
        status_str, qa_s, tone_s = audit_paper_status(abs_path, ptype)
        proj["last_qa_score"] = qa_s
        proj["last_tone_score"] = tone_s
        if qa_s is not None and qa_s >= 90 and tone_s is not None and tone_s >= 80:
            proj["progress_percent"] = 100
            proj["status"] = "completed_ready_for_submission"

        pack_key = proj.get("pack_key", proj["id"].lower())
        docs_to_pack[pack_key] = (
            rel_path,
            proj.get("reader_title", proj.get("title_en")),
            proj.get("reader_tag", proj.get("target_journal")),
            status_str,
        )
        print(f"[PACKAGER] {proj['id']} -> {status_str}")

    pipeline["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    with open(PIPELINE_FILE, "w", encoding="utf-8") as f:
        json.dump(pipeline, f, ensure_ascii=False, indent=2)

    # Static reference & supporting documents
    supporting_docs = {
        "plan": ("lab_projects/AUTOMATED_PAPER_WRITING_PLAN.md", "Kế Hoạch Bài Báo Mới (IMRAD Blueprint)", "H-AI Engine", "Scopus Q1 Plan"),
        "survey": ("docs/survey_instrument.md", "Paper 2: Bảng Hỏi Khảo Sát Thực Nghiệm", "N = 450 (Likert 7)", "28 Items"),
        "proposal": ("docs/proposal_detailed.md", "Đề Cương Nghiên Cứu Tiến Sĩ Chi Tiết", "TDTU Ph.D.", "Đề Cương Chuẩn"),
        "baumeister": ("lab_projects/parsed_markdown/baumeister_2002.md", "Toàn Văn: Baumeister (2002) - Ego Depletion", "JCR FT50", "Lý Thuyết Nền"),
        "shanahan": ("lab_projects/parsed_markdown/shanahan_2019.md", "Toàn Văn: Shanahan (2019) - Thang Đo PP", "JRCS Q1", "Thang Đo Gốc"),
        "beatty": ("lab_projects/parsed_markdown/beatty_1998.md", "Toàn Văn: Beatty & Ferrell (1998) - Thang Đo UBI", "J. Retailing Q1", "Thang Đo Gốc"),
        "verhagen": ("lab_projects/parsed_markdown/verhagen_2011.md", "Toàn Văn: Verhagen & van Dolen (2011) - Khung S-O-R", "I&M Q1", "Khung Lý Thuyết"),
    }
    docs_to_pack.update(supporting_docs)

    bundle = {}
    for key, (rel_path, title, tag, status) in docs_to_pack.items():
        full_path = os.path.join(WORKSPACE, rel_path)
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
            bundle[key] = {"title": title, "tag": tag, "status": status, "content": content}
            print(f"Packed {key}: {len(content):,} chars")
        else:
            print(f"WARNING: Missing {full_path}")

    out_json = os.path.join(WORKSPACE, "lab_projects", "DOCUMENTS_BUNDLE.json")
    out_js = os.path.join(WORKSPACE, "lab_projects", "DOCS_INLINE.js")
    web_json = os.path.join(WORKSPACE, "web", "lab_projects", "DOCUMENTS_BUNDLE.json")
    web_js = os.path.join(WORKSPACE, "web", "lab_projects", "DOCS_INLINE.js")

    for jp in (out_json, web_json):
        os.makedirs(os.path.dirname(jp), exist_ok=True)
        with open(jp, "w", encoding="utf-8") as f:
            json.dump(bundle, f, ensure_ascii=False)

    js_str = "const INLINE_DOCS_BUNDLE = " + json.dumps(bundle, ensure_ascii=False) + ";\n"
    for jsp in (out_js, web_js):
        os.makedirs(os.path.dirname(jsp), exist_ok=True)
        with open(jsp, "w", encoding="utf-8") as f:
            f.write(js_str)

    print("[SUCCESS] Registry-driven packaging complete across all active manuscripts!")


if __name__ == "__main__":
    main()
