import subprocess
import os
import time
import socket
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8688
ROOT_DIR = r"d:\SE_Project\khoahoc\tools\vosviewer-online\dist\vosviewer-online"
OUT_IMG = r"d:\SE_Project\khoahoc\lab_projects\figures\figure2_vosviewer_real_network.png"

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def run_server():
    server = HTTPServer(('127.0.0.1', PORT), CustomHandler)
    server.serve_forever()

def capture_vosviewer():
    # 1. Start server in thread
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    print(f"Started local HTTP server on http://127.0.0.1:{PORT}")
    time.sleep(1)

    # 2. Setup Chrome command
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    target_url = f"http://127.0.0.1:{PORT}/?json=data/luan_an_real_network.json"

    temp_profile = r"C:\Users\IT-Backup\AppData\Local\Temp\vos_chrome_capture"
    
    cmd = [
        chrome_path,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        '--hide-scrollbars',
        '--disable-extensions',
        f'--user-data-dir={temp_profile}',
        f'--screenshot={OUT_IMG}',
        '--window-size=2400,1350',
        '--virtual-time-budget=9000',
        target_url
    ]

    print(f"Launching Chrome to capture {target_url}...")
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=25)
    print("Chrome finished. Return code:", res.returncode)
    print("Stderr:", res.stderr)
    
    if os.path.exists(OUT_IMG):
        print(f"SUCCESS! Captured authentic VOSviewer screenshot: {OUT_IMG} ({os.path.getsize(OUT_IMG)} bytes)")
    else:
        print("FAILED to capture screenshot.")

if __name__ == '__main__':
    capture_vosviewer()
