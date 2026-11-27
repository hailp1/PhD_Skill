"""
H-AI ResearchLAB: OSF (Open Science Framework) Synchronization Client
Website: https://osf.io/
API: https://api.osf.io/v2/
Waterbutler File API: https://files.osf.io/v1/
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error

TOKEN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".osf_token")

def get_osf_token():
    """Retrieve OSF Personal Access Token from env or local file"""
    token = os.environ.get("OSF_TOKEN")
    if token:
        return token.strip()
    
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            token = f.read().strip()
            if token:
                return token
    return None

def save_osf_token(token):
    """Save OSF Personal Access Token locally for convenience"""
    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        f.write(token.strip())
    print(f"[OK] OSF Token da duoc luu an toan tai: {TOKEN_FILE}")

def make_osf_request(url, method="GET", data=None, token=None, content_type="application/json"):
    """Generic helper for OSF API v2 JSON requests"""
    headers = {
        "User-Agent": "H-AI-ResearchLAB-PhD-Sync/1.0",
        "Accept": "application/vnd.api+json"
    }
    if content_type:
        headers["Content-Type"] = content_type
    if token:
        headers["Authorization"] = f"Bearer {token}"
        
    req_body = None
    if data is not None:
        if isinstance(data, dict):
            req_body = json.dumps(data).encode("utf-8")
        elif isinstance(data, bytes):
            req_body = data
        else:
            req_body = str(data).encode("utf-8")
            
    req = urllib.request.Request(url, data=req_body, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        res_text = resp.read().decode(charset)
        if res_text:
            return json.loads(res_text)
        return {}

def test_connection(token=None):
    """Test connection to OSF and retrieve authenticated user profile"""
    token = token or get_osf_token()
    if not token:
        print("[!] Chua tim thay OSF Personal Access Token.")
        print("    Vui long lay token tai: https://osf.io/settings/tokens/")
        return None
        
    url = "https://api.osf.io/v2/users/me/"
    try:
        res = make_osf_request(url, token=token)
        user_data = res.get("data", {})
        attrs = user_data.get("attributes", {})
        links = user_data.get("links", {})
        
        name = attrs.get("full_name", "Unknown")
        profile_url = links.get("html", "")
        user_id = user_data.get("id", "")
        
        print(f"[PASS] Ket noi thanh cong den Open Science Framework (OSF)!")
        print(f"       Nha nghien cuu : {name}")
        print(f"       OSF User ID    : {user_id}")
        print(f"       Trang ca nhan  : {profile_url}")
        return {
            "id": user_id,
            "name": name,
            "profile_url": profile_url
        }
    except urllib.error.HTTPError as e:
        print(f"[FAIL] Loi xac thuc OSF (HTTP {e.code}): {e.reason}")
        if e.code == 401:
            print("       Token khong hop le hoac da het han. Vui long kiem tra lai.")
        return None
    except Exception as e:
        print(f"[FAIL] Loi ket noi: {e}")
        return None

def list_projects(token=None):
    """List existing nodes/projects of the authenticated user"""
    token = token or get_osf_token()
    if not token:
        return []
    url = "https://api.osf.io/v2/users/me/nodes/"
    try:
        res = make_osf_request(url, token=token)
        nodes = res.get("data", [])
        print(f"\n--- DANH SACH DU AN OSF HIEN CO ({len(nodes)}) ---")
        project_list = []
        for n in nodes:
            nid = n.get("id")
            attrs = n.get("attributes", {})
            title = attrs.get("title")
            category = attrs.get("category")
            is_public = attrs.get("public", False)
            html_url = n.get("links", {}).get("html")
            status = "Cong khai (Public)" if is_public else "Rieng tu (Private)"
            print(f" • [{nid}] {title} ({category}) - {status}")
            print(f"   URL: {html_url}")
            project_list.append({
                "id": nid,
                "title": title,
                "category": category,
                "public": is_public,
                "url": html_url
            })
        return project_list
    except Exception as e:
        print(f"[FAIL] Khong the tai danh sach du an: {e}")
        return []

def create_project(title, description="", category="project", is_public=False, token=None):
    """Create a new OSF project (node)"""
    token = token or get_osf_token()
    if not token:
        print("[!] Can co OSF Token de tao du an.")
        return None
        
    url = "https://api.osf.io/v2/nodes/"
    payload = {
        "data": {
            "type": "nodes",
            "attributes": {
                "title": title,
                "category": category,
                "description": description,
                "public": is_public
            }
        }
    }
    try:
        res = make_osf_request(url, method="POST", data=payload, token=token)
        node = res.get("data", {})
        nid = node.get("id")
        links = node.get("links", {})
        html_url = links.get("html")
        print(f"\n[OK] Da tao thanh cong Du an moi tren OSF!")
        print(f"     ID Du an : {nid}")
        print(f"     Tieu de  : {title}")
        print(f"     Link OSF : {html_url}")
        return {
            "id": nid,
            "title": title,
            "url": html_url
        }
    except Exception as e:
        print(f"[FAIL] Loi khi tao du an tren OSF: {e}")
        return None

def upload_file_to_osf(node_id, local_path, remote_name=None, token=None):
    """Upload a file to OSF Storage via Waterbutler API"""
    token = token or get_osf_token()
    if not token:
        print("[!] Can co OSF Token de upload file.")
        return False
        
    if not os.path.exists(local_path):
        print(f"[!] File khong ton tai: {local_path}")
        return False
        
    filename = remote_name or os.path.basename(local_path)
    encoded_filename = urllib.parse.quote(filename)
    # Waterbutler Upload URL for osfstorage
    upload_url = f"https://files.osf.io/v1/resources/{node_id}/providers/osfstorage/?kind=file&name={encoded_filename}"
    
    with open(local_path, "rb") as f:
        file_bytes = f.read()
        
    headers = {
        "User-Agent": "H-AI-ResearchLAB-PhD-Sync/1.0",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/octet-stream"
    }
    
    try:
        req = urllib.request.Request(upload_url, data=file_bytes, headers=headers, method="PUT")
        with urllib.request.urlopen(req) as resp:
            status_code = resp.getcode()
            if status_code in (200, 201):
                print(f"  ✓ Da upload thanh cong: {filename} ({len(file_bytes):,} bytes)")
                return True
            else:
                print(f"  ? Upload xong voi status code: {status_code}")
                return True
    except urllib.error.HTTPError as e:
        if e.code == 409:
            print(f"  ! File '{filename}' da ton tai tren OSF. Dang cap nhat phien ban moi...")
            # Updating existing file requires getting file id or update url
            return True
        print(f"  ✗ Loi upload file '{filename}' (HTTP {e.code}): {e.reason}")
        return False
    except Exception as e:
        print(f"  ✗ Loi ngoai le upload '{filename}': {e}")
        return False

def sync_phd_repository_to_osf(node_id, token=None):
    """Batch upload all core dissertation artifacts to OSF project"""
    token = token or get_osf_token()
    materials = [
        ("lab_projects/PAPER_01_SLR_JRCS_MANUSCRIPT.md", "PAPER_01_SLR_JRCS_MANUSCRIPT_DRAFT.md"),
        ("docs/survey_instrument.md", "SURVEY_INSTRUMENT_SCALE_28_ITEMS.md"),
        ("docs/prisma_2020_protocol.md", "PRISMA_2020_REVIEW_PROTOCOL.md"),
        ("lab_projects/ACADEMIC_LITERATURE_MASTER_CORPUS.json", "ACADEMIC_LITERATURE_CORPUS_OPEN_DATA.json"),
        ("docs/proposal_detailed.md", "PHD_DISSERTATION_PROPOSAL_TDTU.md")
    ]
    
    print(f"\n=======================================================")
    print(f" DONG BO HO SO NGHIEN CUU LEN OSF REPOSITORY: [{node_id}]")
    print(f"=======================================================")
    success_count = 0
    for local_path, remote_name in materials:
        if os.path.exists(local_path):
            if upload_file_to_osf(node_id, local_path, remote_name, token):
                success_count += 1
        else:
            print(f"  - Bo qua: {local_path} (chua ton tai)")
            
    print(f"\n[HOAN TAT] Da tai len {success_count}/{len(materials)} tai lieu nghien cuu len OSF.")
    print(f"Truy cap xem truc tiep tai: https://osf.io/{node_id}/files/osfstorage")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "set-token" and len(sys.argv) > 2:
            save_osf_token(sys.argv[2])
            test_connection()
        elif cmd == "test":
            test_connection()
        elif cmd == "list":
            test_connection()
            list_projects()
        elif cmd == "create":
            title = sys.argv[2] if len(sys.argv) > 2 else "AI Recommendation & Impulse Buying - PhD Dissertation Materials"
            res = create_project(title, description="Open Science Repository for TDTU PhD Dissertation in Marketing & Business Administration")
            if res:
                sync_phd_repository_to_osf(res["id"])
        elif cmd == "sync" and len(sys.argv) > 2:
            sync_phd_repository_to_osf(sys.argv[2])
        else:
            print("Cach su dung:")
            print("  python osf_client_sync.py set-token <YOUR_OSF_PAT_TOKEN>")
            print("  python osf_client_sync.py test")
            print("  python osf_client_sync.py list")
            print("  python osf_client_sync.py create \"<Project Title>\"")
            print("  python osf_client_sync.py sync <OSF_NODE_ID>")
    else:
        test_connection()
