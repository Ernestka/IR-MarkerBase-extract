"""
Check that the credentials are set up, without running the pipeline:

    python src/check_setup.py           # Gemini key + Drive (if configured)
    python src/check_setup.py --gemini  # only the Gemini key
    python src/check_setup.py --drive   # only Drive (no Gemini call, saves quota)

If DRIVE_FOLDER_ID / DRIVE_SUPPLEMENT_FOLDER_ID are not in .env yet, it looks
for folders named IR_papers / IR_supplements shared with the robot account and
writes their IDs into .env for you.

Gemini: makes one tiny call (free). Drive: lists the PDFs the service account
can see in DRIVE_FOLDER_ID (and the supplements folder, if set).
"""
import json
import os
import sys
from pathlib import Path

from pydantic import BaseModel

import llm  # also loads .env
import drive


class Ping(BaseModel):
    ok: bool


def check_gemini():
    if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
        print("✗ GEMINI_API_KEY is not set.")
        return False
    try:
        res = llm.call("flash", "Reply with ok=true.", [llm.Text("ping")], Ping, max_tokens=200)
    except llm.AllModelsFailed as e:
        print(f"✗ Your key works, but {e}")
        return False
    except Exception as e:
        print(f"✗ Gemini call failed: {e}")
        return False
    if res.parsed and res.parsed.ok:
        print(f"✓ Gemini works ({res.model_id}).")
        return True
    print(f"✗ Gemini answered but not as expected: stop={res.stop_reason} {res.error}")
    return False


ENV_FILE = Path(__file__).resolve().parent.parent / ".env"
FOLDER_NAMES = {"DRIVE_FOLDER_ID": "IR_papers", "DRIVE_SUPPLEMENT_FOLDER_ID": "IR_supplements"}


def detect_folders(svc):
    """Find the shared IR_papers / IR_supplements folders by name and write any
    missing IDs into .env. Returns the robot's email, for messages."""
    shared = svc.files().list(
        q=f"mimeType='{drive.FOLDER_MIME}' and trashed=false",
        fields="files(id,name)", pageSize=200).execute().get("files", [])
    for var, name in FOLDER_NAMES.items():
        if os.environ.get(var, "").strip():
            continue
        hits = [f for f in shared if f["name"].strip().lower() == name.lower()]
        if len(hits) == 1:
            os.environ[var] = hits[0]["id"]
            with ENV_FILE.open("a", encoding="utf-8") as fh:
                fh.write(f"{var}={hits[0]['id']}\n")
            print(f"  found '{name}' shared with the robot → wrote {var} to .env")
        elif len(hits) > 1:
            print(f"  several folders named '{name}' are shared — set {var} in .env by hand")


def check_drive():
    key = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "")
    if not key:
        print("– Drive not configured (set GOOGLE_APPLICATION_CREDENTIALS in .env).")
        return False
    if not os.path.exists(key):
        print(f"✗ Key file not found: {key}")
        return False
    robot = json.loads(Path(key).read_text()).get("client_email", "?")
    try:
        svc = drive.service()
        detect_folders(svc)
        folder = os.environ.get("DRIVE_FOLDER_ID", "").strip()
        if not folder:
            print(f"✗ Drive key works, but no folder named 'IR_papers' is shared with the robot.\n"
                  f"  In Google Drive, share IR_papers (and IR_supplements) as Viewer with:\n  {robot}")
            return False
        pdfs = drive.list_pdfs(svc, folder)
    except Exception as e:
        print(f"✗ Drive access failed: {e}")
        return False
    if not pdfs:
        print(f"✗ Drive works and IR_papers is visible, but it contains no PDFs yet — put a PDF "
              f"in IR_papers/master/ (shared with {robot}).")
        return False
    print(f"✓ Drive works: {len(pdfs)} PDF(s) visible, e.g. "
          + ", ".join(f"{p['source'] or 'root'}/{p['name']}" for p in pdfs[:5]))
    supp = os.environ.get("DRIVE_SUPPLEMENT_FOLDER_ID", "").strip()
    if supp:
        print(f"  supplements folder tree: {drive.folder_tree(svc, supp) or '(empty or not shared)'}")
    return True


if __name__ == "__main__":
    ok = True
    if "--drive" not in sys.argv:          # --drive: skip the Gemini call (saves quota)
        ok = check_gemini()
    if "--gemini" not in sys.argv:
        ok = check_drive() and ok
    sys.exit(0 if ok else 1)
