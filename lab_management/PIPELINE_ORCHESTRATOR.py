"""
BAM-AI RESEARCH LAB - PIPELINE ORCHESTRATOR
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
    print("🎓 BAM-AI RESEARCH LAB | MASTER STATUS OVERVIEW")
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
            print(f"      Giai đoạn: {proj['current_stage']}")
            print(f"      Agents phụ trách: {', '.join(proj['lead_agents'])}")
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

def main():
    parser = argparse.ArgumentParser(description="BAM-AI Lab Pipeline Orchestrator")
    parser.add_argument("--status", action="store_true", help="Hiển thị tổng quan trạng thái Lab và 4 bài báo")
    parser.add_argument("--agent", type=str, help="Mã Agent cần kích hoạt (CRS, SLR, MSA, EDS, LPA, MJR)")
    parser.add_argument("--task", type=str, default="Thực thi nhiệm vụ nghiên cứu chuẩn", help="Mô tả nhiệm vụ cho Agent")

    args = parser.parse_args()

    if args.status or (not args.agent):
        show_status()
    elif args.agent:
        trigger_agent(args.agent, args.task)

if __name__ == "__main__":
    main()
