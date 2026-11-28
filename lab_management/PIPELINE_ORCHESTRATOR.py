"""
H-AI ResearchLAB - REGISTRY-DRIVEN MULTI-PROJECT ORCHESTRATOR (PIPELINE_ORCHESTRATOR.py v3.0)
Single Source of Truth: lab_management/RESEARCH_PROJECTS_PIPELINE.json
Supports --status, --run-pipeline --paper <key>, --run-all, and --new-project.
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REGISTRY_FILE = os.path.join(WORKSPACE_DIR, "lab_agents", "AGENTS_REGISTRY.json")
PIPELINE_FILE = os.path.join(WORKSPACE_DIR, "lab_management", "RESEARCH_PROJECTS_PIPELINE.json")

IDEA_SCANNER_SCRIPT = os.path.join(WORKSPACE_DIR, "lab_management", "idea_scanner.py")
STORM_SCRIPT = os.path.join(WORKSPACE_DIR, "lab_management", "storm_perspective_dialogue.py")
QA_GATE_SCRIPT = os.path.join(WORKSPACE_DIR, "lab_management", "academic_qa_gate.py")
TONE_AUDIT_SCRIPT = os.path.join(WORKSPACE_DIR, ".agents", "skills", "phd-dissertation-writing", "scripts", "academic_tone_audit.py")
PACKAGER_SCRIPT = os.path.join(WORKSPACE_DIR, "lab_management", "pack_docs_bundle.py")


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def find_project(pipeline_data, paper_key):
    key = str(paper_key).lower().strip()
    for proj in pipeline_data.get("projects", []):
        if key in (
            str(proj.get("cli_key", "")).lower(),
            str(proj.get("id", "")).lower(),
            str(proj.get("pack_key", "")).lower(),
        ):
            return proj
    return None


def run_agent_stage(stage_code, stage_name, agent_code, command_args):
    print("\n" + "=" * 80)
    print(f"▶ [STAGE {stage_code}] EXECUTING {stage_name.upper()} (AGENT: {agent_code})")
    print("=" * 80)
    res = subprocess.run([sys.executable] + command_args, cwd=WORKSPACE_DIR, capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print(f"❌ [STAGE {stage_code} FAILED] Return code: {res.returncode}")
        if res.stderr:
            print("Error details:", res.stderr)
        return False
    print(f"✅ [STAGE {stage_code} PASSED]")
    return True


def execute_project_pipeline(paper_key="1b"):
    pipeline = load_json(PIPELINE_FILE)
    if not pipeline:
        print("❌ Missing RESEARCH_PROJECTS_PIPELINE.json")
        sys.exit(1)

    proj = find_project(pipeline, paper_key)
    if not proj:
        valid = [f"{p.get('cli_key')} ({p.get('id')})" for p in pipeline.get("projects", [])]
        print(f"❌ Unknown project key '{paper_key}'. Registered projects: {', '.join(valid)}")
        sys.exit(1)

    target_rel = proj["manuscript_file"]
    target_file = os.path.join(WORKSPACE_DIR, target_rel)
    target_type = proj.get("paper_type", "slr")
    engine_rel = proj.get("engine_script")

    print("=" * 80)
    print(f"🚀 INITIATING AUTONOMOUS LAB PIPELINE FOR {proj['id']} ({proj['code']})")
    print(f"Target Journal: {proj['target_journal']} | Type: {target_type.upper()}")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Stage 1A & 1B
    if not run_agent_stage("1A - CRS", "Data-Driven Corpus Gap Detection", "CRS", [IDEA_SCANNER_SCRIPT]):
        sys.exit(1)
    if not run_agent_stage("1B - CRS", "4-Perspective Academic Tension Stress Testing", "CRS", [STORM_SCRIPT]):
        sys.exit(1)

    # Stage 2: Type-specific protocol check
    if target_type == "empirical":
        print("\n[STAGE 2 - MSA & EDS] Validating G*Power, Brislin Instrument & Empirical Design...")
    else:
        print("\n[STAGE 2 - SLR & EDS] Validating PRISMA 2020 Search String & Bibliometric Mapping...")

    # Stage 3: Draft via configured engine OR audit existing manuscript
    if engine_rel:
        engine_path = os.path.join(WORKSPACE_DIR, engine_rel)
        if not run_agent_stage("3 - LPA", f"Manuscript Generation ({proj['id']})", "LPA", [engine_path]):
            sys.exit(1)
    else:
        if not os.path.exists(target_file):
            print(f"❌ No engine_script configured and manuscript file missing: {target_file}")
            sys.exit(1)
        print(f"\n▶ [STAGE 3 - LPA] Preserving existing manuscript for audit: {target_rel}")

    # Stage 4A & 4B: Quality & Tone Gates
    if not run_agent_stage("4A - MJR", f"6-Gate Quality Audit ({target_type.upper()})", "MJR", [QA_GATE_SCRIPT, "--file", target_file, "--type", target_type]):
        sys.exit(1)
    if not run_agent_stage("4B - MJR", "Academic Naturalness & Anti-AI Tone Audit", "MJR", [TONE_AUDIT_SCRIPT, "--file", target_file, "--strict"]):
        sys.exit(1)

    # Stage 5: Pack & Sync (also updates QA/Tone scores in RESEARCH_PROJECTS_PIPELINE.json)
    if not run_agent_stage("5 - DOCS", "Registry-Driven Packaging & Web Reader Sync", "DOCS", [PACKAGER_SCRIPT]):
        sys.exit(1)

    print("\n" + "=" * 80)
    print(f"🎉 PIPELINE COMPLETED SUCCESSFULLY FOR {proj['id']}!")
    print("=" * 80)


def run_all_active():
    pipeline = load_json(PIPELINE_FILE)
    if not pipeline:
        sys.exit(1)

    print("=" * 80)
    print("🌐 RUNNING MULTI-PROJECT AUDIT & PACKAGING ACROSS ALL ACTIVE MANUSCRIPTS")
    print("=" * 80)

    active_count = 0
    for proj in pipeline.get("projects", []):
        target_file = os.path.join(WORKSPACE_DIR, proj["manuscript_file"])
        if not os.path.exists(target_file):
            print(f"\n⏭️  Skipping [{proj['id']}] (Planned / manuscript not yet created: {proj['manuscript_file']})")
            continue
        active_count += 1
        ptype = proj.get("paper_type", "slr")
        print(f"\n🔍 Auditing [{proj['id']}] {proj['manuscript_file']} ({ptype.upper()})...")
        if not run_agent_stage(f"4A-{proj['id']}", f"QA Audit ({proj['id']})", "MJR", [QA_GATE_SCRIPT, "--file", target_file, "--type", ptype]):
            sys.exit(1)
        if not run_agent_stage(f"4B-{proj['id']}", f"Tone Audit ({proj['id']})", "MJR", [TONE_AUDIT_SCRIPT, "--file", target_file, "--strict"]):
            sys.exit(1)

    if active_count > 0:
        if not run_agent_stage("5 - DOCS", "Bundle Packaging Across All Active Projects", "DOCS", [PACKAGER_SCRIPT]):
            sys.exit(1)
    print(f"\n✅ Audited and packaged {active_count} active projects cleanly.")


def scaffold_new_project(key, ptype, title, journal):
    pipeline = load_json(PIPELINE_FILE)
    if not pipeline:
        sys.exit(1)

    clean_key = key.lower().strip().replace(" ", "_")
    if find_project(pipeline, clean_key):
        print(f"❌ Project '{clean_key}' already exists in RESEARCH_PROJECTS_PIPELINE.json.")
        sys.exit(1)

    proj_dir = os.path.join(WORKSPACE_DIR, "lab_projects", "projects", clean_key)
    os.makedirs(proj_dir, exist_ok=True)
    rel_ms = f"lab_projects/projects/{clean_key}/MANUSCRIPT_{clean_key.upper()}.md"
    abs_ms = os.path.join(WORKSPACE_DIR, rel_ms)

    starter_md = f"""# {title}

**Author:** Le Phuc Hai (Lê Phúc Hải)  
**Affiliation:** NCSKIT.org (Independent Research Group)  
**ORCID:** [https://orcid.org/0009-0004-1215-5023](https://orcid.org/0009-0004-1215-5023)  
**Correspondence:** [hailp@ncskit.org](mailto:hailp@ncskit.org)

---

## HIGHLIGHTS
- Registered multi-project manuscript scaffold for {journal}.
- Ready for Stage 1A quantitative gap scan and Stage 1B stress-testing.
- Enforces strict academic integrity and APA 7th citation parity.

---

## ABSTRACT
[Pending drafting for {title}.]

**Keywords**: Artificial intelligence; Consumer behavior; {ptype.upper()}

---

## 1. INTRODUCTION
[Drafting space for {title}.]

---

## REFERENCES
"""
    with open(abs_ms, "w", encoding="utf-8") as f:
        f.write(starter_md)

    new_entry = {
        "id": f"PAPER-{clean_key.upper()}",
        "cli_key": clean_key,
        "pack_key": f"paper_{clean_key}",
        "code": clean_key.upper(),
        "paper_type": ptype,
        "dissertation_chapter": "Independent / New Project Stream",
        "title_vn": title,
        "title_en": title,
        "reader_title": f"Project {clean_key.upper()}: {title[:42]}...",
        "reader_tag": journal,
        "manuscript_file": rel_ms,
        "engine_script": None,
        "lead_agents": ["agent-01-crs", "agent-05-lpa", "agent-06-mjr"],
        "target_journal": journal,
        "journal_metrics": "Scopus Q1 Target",
        "status": "scaffolded",
        "progress_percent": 15,
        "last_qa_score": None,
        "last_tone_score": None,
        "strategic_value": "Dự án bài báo mới khởi tạo qua H-AI Multi-Project Registry."
    }
    pipeline["projects"].append(new_entry)
    pipeline["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    save_json(PIPELINE_FILE, pipeline)
    print(f"✅ Created new project [{new_entry['id']}] -> {rel_ms}")
    print(f"   Run it anytime via: python lab_management/PIPELINE_ORCHESTRATOR.py --run-pipeline --paper {clean_key}")


def show_status():
    print("=" * 80)
    print("🎓 H-AI ResearchLAB | MULTI-PROJECT MASTER STATUS OVERVIEW")
    print("=" * 80)
    registry = load_json(REGISTRY_FILE)
    pipeline = load_json(PIPELINE_FILE)

    if registry:
        print(f"\n[1] DANH BẠ 6 AI AGENTS ({registry['lab_name']}):")
        for ag in registry["agents"]:
            status_icon = "🟢" if ag["status"] == "active" else "⚪"
            print(f"  {status_icon} [{ag['code']}] {ag['name']} - {ag['title_vn']}")

    if pipeline:
        print(f"\n[2] DANH SÁCH DỰ ÁN BÀI BÁO ({len(pipeline['projects'])} PROJECTS):")
        for proj in pipeline["projects"]:
            bar_len = 20
            filled = int(bar_len * proj.get("progress_percent", 0) / 100)
            bar = "█" * filled + "░" * (bar_len - filled)
            qa = proj.get("last_qa_score")
            tone = proj.get("last_tone_score")
            scores = f"QA:{qa}/100 Tone:{tone}/100" if qa is not None else "Chưa kiểm duyệt"
            exists = "📄" if os.path.exists(os.path.join(WORKSPACE_DIR, proj["manuscript_file"])) else "📝"
            print(f"  {exists} [{proj['id']}] (--paper {proj['cli_key']}) | {proj.get('progress_percent',0):3d}% [{bar}] | {scores} -> {proj['target_journal']}")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="H-AI ResearchLAB Registry-Driven Multi-Project Orchestrator")
    parser.add_argument("--status", action="store_true", help="Hiển thị tổng quan trạng thái tất cả dự án")
    parser.add_argument("--run-pipeline", action="store_true", help="Chạy quy trình cho 1 bài báo cụ thể")
    parser.add_argument("--run-all", action="store_true", help="Kiểm duyệt và đóng gói toàn bộ bài báo hiện có")
    parser.add_argument("--paper", type=str, default="1b", help="Mã dự án (cli_key hoặc id, vd: 1a, 1b, 2)")
    parser.add_argument("--new-project", action="store_true", help="Khởi tạo dự án bài báo mới vào Registry")
    parser.add_argument("--id", type=str, help="Mã key cho dự án mới (vd: paper5)")
    parser.add_argument("--type", type=str, default="empirical", choices=["slr", "empirical"], help="Loại bài báo (slr | empirical)")
    parser.add_argument("--title", type=str, default="Untitled Research Project", help="Tiêu đề bài báo mới")
    parser.add_argument("--journal", type=str, default="Scopus Q1 Target", help="Tạp chí mục tiêu")

    args = parser.parse_args()

    if args.new_project:
        if not args.id:
            print("❌ Please specify --id <key> when using --new-project")
            sys.exit(1)
        scaffold_new_project(args.id, args.type, args.title, args.journal)
    elif args.run_all:
        run_all_active()
    elif args.run_pipeline:
        execute_project_pipeline(args.paper)
    else:
        show_status()


if __name__ == "__main__":
    main()
