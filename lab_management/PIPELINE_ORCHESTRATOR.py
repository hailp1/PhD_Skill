"""
H-AI ResearchLAB - PIPELINE ORCHESTRATOR
Phòng Thí Nghiệm Quản Trị Kinh Doanh & Marketing Tích Hợp AI
Điều phối viên tiến trình học thuật giữa 6 Agents và Lab Director.
"""

import sys
import os
import json
import argparse
from datetime import datetime

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REGISTRY_FILE = os.path.join(WORKSPACE_DIR, "lab_agents", "AGENTS_REGISTRY.json")
PIPELINE_FILE = os.path.join(WORKSPACE_DIR, "lab_management", "RESEARCH_PROJECTS_PIPELINE.json")

def load_json(path):
    if not os.path.exists(path):
        print(f"[ERROR] Không tìm thấy file: {path}")
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def show_status():
    print("=" * 80)
    print("🎓 H-AI ResearchLAB | MASTER STATUS OVERVIEW")
    print("=" * 80)
    registry = load_json(REGISTRY_FILE)
    pipeline = load_json(PIPELINE_FILE)

    if registry:
        print(f"\n[1] DANH BẠ 6 AI AGENTS ({registry['lab_name']}):")
        for ag in registry["agents"]:
            status_icon = "🟢" if ag["status"] == "active" else "⚪"
            print(f"  {status_icon} [{ag['code']}] {ag['name']}")
            print(f"      Vai trò: {ag['title_vn']}")
            print(f"      Trọng tâm: {ag['focus'][:70]}...")

    if pipeline:
        print(f"\n[2] TIẾN ĐỘ 4 BÀI BÁO SCOPUS Q1 (PUBLICATION PIPELINE):")
        for proj in pipeline["projects"]:
            bar_len = 20
            filled = int(bar_len * proj["progress_percent"] / 100)
            bar = "█" * filled + "░" * (bar_len - filled)
            print(f"\n  📌 [{proj['id']}] {proj['code']} | {proj['progress_percent']}% [{bar}]")
            print(f"      Tiêu đề: {proj['title_vn']}")
            print(f"      Tạp chí đích: {proj['target_journal']} ({proj['journal_metrics']})")
            print(f"      Giai đoạn: {proj.get('current_stage') or proj.get('dissertation_chapter')}")
            print(f"      Agents phụ trách: {', '.join(proj.get('lead_agents', []))}")
    print("=" * 80)

def trigger_agent(agent_code, task_desc):
    registry = load_json(REGISTRY_FILE)
    if not registry:
        return
    target = None
    for ag in registry["agents"]:
        if ag["code"].upper() == agent_code.upper():
            target = ag
            break
    if not target:
        print(f"[ERROR] Không tìm thấy Agent với mã: {agent_code}")
        print("Mã hợp lệ: CRS, SLR, MSA, EDS, LPA, MJR")
        return

    print("=" * 80)
    print(f"🚀 KÍCH HOẠT NHIỆM VỤ CHO AGENT [{target['code']}]: {target['name']}")
    print(f"Vai trò: {target['title_vn']}")
    print(f"Nhiệm vụ: {task_desc}")
    print(f"Thời điểm kích hoạt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print(f"[STATUS] Agent [{target['code']}] đang tải ngữ cảnh và chuẩn bị các kỹ năng: {target['skills']}...")
    print(f"[READY] Sẵn sàng thực thi theo quy chuẩn Điều lệ Lab ({os.path.join('lab_management', 'LAB_CHARTER.md')}).")

def show_advisory():
    print("=" * 80)
    print("📚 H-AI LAB | TRUNG TÂM TƯ VẤN XUẤT BẢN & BÁO CÁO HỌC THUẬT")
    print("=" * 80)
    print("\n[1] TƯ VẤN KHỚP TẠP CHÍ MỤC TIÊU (SCOPUS Q1 / ABS 3*):")
    print("  • BÀI 1 -> Journal of Retailing and Consumer Services (JRCS) | IF: 11.0, CiteScore: 19.5")
    print("      Khẩu vị Editor: Ưa chuộng tổng quan hệ thống PRISMA 2020 kết hợp phân tích mạng lưới VOSviewer.")
    print("  • BÀI 2 -> Computers in Human Behavior (CHB) / ECRA | IF: 9.0, ABS 3*")
    print("      Khẩu vị Editor: Đòi hỏi cơ chế tâm lý nhận thức - cảm xúc rõ ràng (AI -> Accuracy/Novelty -> E-Sat -> OIB).")
    print("  • BÀI 3 -> Journal of Business Research (JBR) | IF: 10.5, ABS 3*")
    print("      Khẩu vị Editor: Đóng góp lý thuyết biên (Boundary conditions: Self-control, Ego depletion).")
    print("  • BÀI 4 -> Information & Management (I&M) | IF: 8.2, ABS 3*")
    print("      Khẩu vị Editor: Phương pháp luận hỗn hợp hiện đại (PLS-SEM + fsQCA + NCA).")

    print("\n[2] TƯ VẤN CẤU TRÚC BẢN THẢO & TRIỆT TIÊU MÙI AI:")
    print("  • Áp dụng 6 bước tu từ: Hook & Tension -> 3-prong Gap -> 4-step Deduction -> Hedging -> Discussion -> Contribution.")
    print("  • Chạy kiểm toán văn phong: python .agents/skills/phd-dissertation-writing/scripts/academic_tone_audit.py")
    print("  • Thẩm định trích dẫn thật: python .agents/skills/phd-literature-review/scripts/citation_verifier.py")

    print("\n[3] TƯ VẤN BÁO CÁO & SLIDE LUẬN ÁN TIẾN SĨ:")
    print("  • Dữ liệu Slide báo cáo đã có sẵn tại: data/processed/prisma_2020_slide_report.md")
    print("  • Xem giao diện Báo cáo Slide tại: index.html (Tab 4: Báo Cáo Slide & Tạp Chí)")
    print("=" * 80)

def main():
    parser = argparse.ArgumentParser(description="H-AI ResearchLAB Pipeline Orchestrator")
    parser.add_argument("--status", action="store_true", help="Hiển thị tổng quan trạng thái Lab và 4 bài báo")
    parser.add_argument("--agent", type=str, help="Mã Agent cần kích hoạt (CRS, SLR, MSA, EDS, LPA, MJR)")
    parser.add_argument("--task", type=str, default="Thực thi nhiệm vụ nghiên cứu chuẩn", help="Mô tả nhiệm vụ cho Agent")
    parser.add_argument("--advise", action="store_true", help="Hiển thị tư vấn xuất bản bài báo và báo cáo luận án")

    args = parser.parse_args()

    if args.advise:
        show_advisory()
    elif args.status or (not args.agent):
        show_status()
    elif args.agent:
        trigger_agent(args.agent, args.task)

if __name__ == "__main__":
    main()
