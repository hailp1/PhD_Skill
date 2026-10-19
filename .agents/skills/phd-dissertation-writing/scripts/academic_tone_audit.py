"""
Academic Tone & Anti-AI Audit Tool (for Doctoral Dissertations in Marketing & Management)
Scans academic text for:
1. AI Clichés & Buzzwords (English & Vietnamese)
2. Boastful assertions & Lack of Academic Hedging (Absolute claims)
3. AI structural markers (em-dash spam, empty boilerplate conclusions)
"""

import sys
import os
import re
import argparse

# Blacklist of English AI Clichés & Overused Buzzwords
EN_AI_CLICHES = [
    r"\bdelv(e|es|ed|ing)\s+into\b",
    r"\brich\s+tapestry\b",
    r"\btapestry\b",
    r"\btestament\s+to\b",
    r"\bbeacon\s+of\b",
    r"\bgame[- ]changer\b",
    r"\brevolutionary\b",
    r"\bgroundbreaking\b",
    r"\bunpack(ing)?\b",
    r"\bseamless(ly)?\b",
    r"\bvibrant\b",
    r"\bbespoke\b",
    r"\bin\s+today'?s\s+(fast-paced\s+)?digital\s+(age|world|era)\b",
    r"\bit\s+is\s+(worth\s+noting|important\s+to\s+note|crucial\s+to\s+understand)\s+that\b",
]

# Blacklist of Vietnamese AI Clichés & Sáo rỗng
VN_AI_CLICHES = [
    r"bức\s+tranh\s+toàn\s+cảnh",
    r"chiếc\s+chìa\s+khóa\s+vạn\s+năng",
    r"kim\s+chỉ\s+nam",
    r"minh\s+chứng\s+hùng\s+hồn",
    r"đào\s+sâu\s+nghiên\s+cứu",
    r"mổ\s+xẻ\s+vấn\s+đề",
    r"đột\s+phá\s+mang\s+tính\s+cách\s+mạng",
    r"không\s+thể\s+phủ\s+nhận\s+rằng",
    r"trong\s+kỷ\s+nguyên\s+số\s+hóa\s+vũ\s+bão",
    r"đóng\s+vai\s+trò\s+vô\s+cùng\s+to\s+lớn",
]

# Boastful / Absolute Claims (Lack of Academic Hedging)
ABSOLUTE_CLAIMS = [
    r"\bprove(s|d)?\s+100%\b",
    r"\bproves?\s+definitively\b",
    r"\bundeniabl(y|e)\b",
    r"\bfirst\s+and\s+only\s+study\b",
    r"\bcompletely\s+solves\b",
    r"chứng\s+minh\s+hoàn\s+toàn",
    r"chắc\s+chắn\s+100%",
    r"giải\s+quyết\s+triệt\s+để\s+mọi",
    r"nghiên\s+cứu\s+đầu\s+tiên\s+và\s+duy\s+nhất",
    r"hiệu\s+quả\s+vượt\s+trội\s+tuyệt\s+đối",
]

# Repetitive AI Conclusions
AI_CONCLUSIONS = [
    r"\bin\s+conclusion,\s+this\s+study\b",
    r"\bin\s+summary,\s+these\s+findings\b",
    r"\btóm\s+lại,\s+(nghiên\s+cứu|bài\s+viết|luận\s+án)\s+này\b",
]


def audit_academic_text(text: str) -> dict:
    lines = text.split("\n")
    issues = []
    
    em_dash_count = len(re.findall(r"—", text))
    
    for idx, line in enumerate(lines, 1):
        clean_line = line.strip()
        if not clean_line or clean_line.startswith("#"):
            continue

        # 1. Check EN AI clichés
        for pattern in EN_AI_CLICHES:
            matches = list(re.finditer(pattern, clean_line, re.IGNORECASE))
            for m in matches:
                issues.append({
                    "line": idx,
                    "type": "AI Cliché (EN)",
                    "matched": m.group(0),
                    "context": clean_line,
                    "suggestion": "Replace with precise scholarly vocabulary (examine, investigate, novel perspective, etc.)."
                })

        # 2. Check VN AI clichés
        for pattern in VN_AI_CLICHES:
            matches = list(re.finditer(pattern, clean_line, re.IGNORECASE))
            for m in matches:
                issues.append({
                    "line": idx,
                    "type": "AI Cliché (VN)",
                    "matched": m.group(0),
                    "context": clean_line,
                    "suggestion": "Tránh sáo rỗng báo chí; dùng từ học thuật trung tính (tổng thể nghiên cứu, bằng chứng thực nghiệm, phân tích sâu)."
                })

        # 3. Check Boastful / Absolute non-hedged claims
        for pattern in ABSOLUTE_CLAIMS:
            matches = list(re.finditer(pattern, clean_line, re.IGNORECASE))
            for m in matches:
                issues.append({
                    "line": idx,
                    "type": "Lack of Hedging (Tuyệt đối hóa / Chém gió)",
                    "matched": m.group(0),
                    "context": clean_line,
                    "suggestion": "Apply scholarly hedging: 'lends empirical support to', 'tends to indicate', 'bước đầu cung cấp bằng chứng', 'trong giới hạn của mẫu'."
                })

        # 4. Check Repetitive AI Conclusions
        for pattern in AI_CONCLUSIONS:
            matches = list(re.finditer(pattern, clean_line, re.IGNORECASE))
            for m in matches:
                issues.append({
                    "line": idx,
                    "type": "Repetitive AI Conclusion Formula",
                    "matched": m.group(0),
                    "context": clean_line,
                    "suggestion": "Viết đoạn kết tự nhiên, nhấn mạnh hàm ý thực nghiệm hoặc liên kết chương thay vì tóm tắt rập khuôn."
                })

    return {
        "total_lines": len(lines),
        "total_issues": len(issues),
        "em_dash_count": em_dash_count,
        "issues": issues
    }


def main():
    parser = argparse.ArgumentParser(description="Academic Tone & Anti-AI Audit for Dissertations")
    parser.add_argument("--file", type=str, required=True, help="Path to text or markdown file")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    result = audit_academic_text(content)

    print("=" * 65)
    print(f"ACADEMIC TONE & ANTI-AI AUDIT REPORT: {os.path.basename(args.file)}")
    print("=" * 65)
    print(f"Total lines analyzed: {result['total_lines']}")
    print(f"Em-dashes detected: {result['em_dash_count']} (Warning: Excessive em-dashes indicate AI generation)")
    print(f"Total issues flagged: {result['total_issues']}\n")

    if result["total_issues"] == 0:
        print("✓ EXCELLENT: No typical AI clichés, boastful claims, or boilerplate formulas detected!")
        print("The text demonstrates appropriate academic tone and scholarly hedging.")
    else:
        print("--- FLAGGED ISSUES & RECOMMENDATIONS ---")
        for i, issue in enumerate(result["issues"], 1):
            print(f"[{i}] Line {issue['line']} | Type: {issue['type']}")
            print(f"    Snippet: \"...{issue['matched']}...\"")
            print(f"    Line content: {issue['context'][:100]}")
            print(f"    Recommendation: {issue['suggestion']}")
            print("-" * 50)


if __name__ == "__main__":
    main()
