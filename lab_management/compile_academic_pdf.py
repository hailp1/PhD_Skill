"""
COMPILES ACADEMIC MANUSCRIPT TO PDF VIA HEADLESS ENGINE
Generates publication-quality A4 vector PDF directly from XEM_BAN_THAO_BAI_BAO.html
"""
import subprocess
import os
import sys

def compile_pdf():
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    
    browser_exe = None
    for p in edge_paths:
        if os.path.exists(p):
            browser_exe = p
            break
            
    if not browser_exe:
        print("[ERROR] Neither Microsoft Edge nor Google Chrome found for headless PDF printing.")
        return False

    html_file = os.path.abspath("XEM_BAN_THAO_BAI_BAO.html")
    pdf_out = os.path.abspath("lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.pdf")
    file_url = "file:///" + html_file.replace("\\", "/")

    print(f"[INFO] Using engine: {browser_exe}")
    print(f"[INFO] Source HTML: {file_url}")
    print(f"[INFO] Target PDF:  {pdf_out}")

    cmd = [
        browser_exe,
        "--headless=new",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=5000",
        f"--print-to-pdf={pdf_out}",
        "--no-pdf-header-footer",
        file_url
    ]

    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if os.path.exists(pdf_out) and os.path.getsize(pdf_out) > 10000:
            size_kb = os.path.getsize(pdf_out) / 1024
            print(f"[SUCCESS] Physical PDF generated successfully: {pdf_out} ({size_kb:.1f} KB)")
            return True
        else:
            print(f"[WARNING] Fallback to legacy headless mode...")
            cmd[1] = "--headless"
            subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if os.path.exists(pdf_out):
                print(f"[SUCCESS] PDF generated in fallback mode: {pdf_out} ({os.path.getsize(pdf_out)/1024:.1f} KB)")
                return True
    except Exception as e:
        print(f"[ERROR] Failed to compile PDF: {e}")
        return False

if __name__ == "__main__":
    compile_pdf()
