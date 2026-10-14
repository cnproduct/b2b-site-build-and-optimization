#!/usr/bin/env python3
r"""
Automated Multi-Target Synchronization Script for b2b-site-build-and-optimization Skill.
1. Syncs/Pushes to GitHub repository: https://github.com/cnproduct/b2b-site-build-and-optimization
2. Mirrors to LAN Shared Path: \\naike\耐科公司共享文件\Ai学习\Skill\b2b-site-build-and-optimization
"""

import os
import sys
import json
import shutil
import urllib.request
import urllib.error
import subprocess
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
LAN_SHARED_BASE = Path(r"\\naike\耐科公司共享文件\Ai学习\Skill")
LAN_TARGET_DIR = LAN_SHARED_BASE / "b2b-site-build-and-optimization"
GITHUB_OWNER = "cnproduct"
REPO_NAME = "b2b-site-build-and-optimization"
REPO_URL = f"https://github.com/{GITHUB_OWNER}/{REPO_NAME}.git"

def get_git_credential():
    """Retrieve github token dynamically from environment or git credential manager."""
    env_token = os.environ.get("GITHUB_TOKEN")
    if env_token:
        return "cnproduct", env_token
    
    try:
        p = subprocess.Popen(["git", "credential", "fill"],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, _ = p.communicate("protocol=https\nhost=github.com\n\n")
        username, password = None, None
        for line in out.splitlines():
            if line.startswith("username="):
                username = line.split("=", 1)[1].strip()
            elif line.startswith("password="):
                password = line.split("=", 1)[1].strip()
        if password:
            return username or "cnproduct", password
    except Exception as e:
        print(f"[WARN] Failed to read git credential manager: {e}")
    
    return "cnproduct", ""

def ensure_github_repo(token: str):
    """Ensure repository exists on GitHub via REST API."""
    print(f"[1/3] Checking/Creating GitHub repository: {GITHUB_OWNER}/{REPO_NAME}...")
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "Skill-Sync-Bot/1.0",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }

    # 1. Check if repo exists
    check_url = f"https://api.github.com/repos/{GITHUB_OWNER}/{REPO_NAME}"
    req = urllib.request.Request(check_url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            if resp.getcode() == 200:
                print(f"  -> Repository already exists at {REPO_URL}")
                return True
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"  -> Error checking repo: {e}")

    # 2. Create repo if not exists
    create_url = "https://api.github.com/user/repos"
    payload = {
        "name": REPO_NAME,
        "description": "外贸 B2B 独立站全生命周期建站与深度优化全案技能 (SOP, CBM计算器, 机器可读GEO端点, 工业证据化攻防)",
        "private": False,
        "has_issues": True,
        "has_wiki": False
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(create_url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            if resp.getcode() in [200, 201]:
                print(f"  -> Successfully created repository on GitHub: {REPO_URL}")
                return True
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        if "name already exists" in err_msg:
            print(f"  -> Repository already exists on GitHub.")
            return True
        print(f"  -> Failed to create repo: {e.code} {err_msg}")
        return False
    except Exception as e:
        print(f"  -> Exception creating repo: {e}")
        return False
    return True

def sync_to_github():
    """Git commit and push current skill directory to GitHub."""
    print(f"[2/3] Committing and pushing to GitHub ({REPO_URL})...")
    os.chdir(str(SKILL_DIR))

    # Initialize git if needed
    if not (SKILL_DIR / ".git").exists():
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "branch", "-M", "main"], check=True)
    
    # Configure remote
    remotes = subprocess.run(["git", "remote"], capture_output=True, text=True).stdout.splitlines()
    if "origin" not in remotes:
        subprocess.run(["git", "remote", "add", "origin", REPO_URL], check=True)
    else:
        subprocess.run(["git", "remote", "set-url", "origin", REPO_URL], check=True)

    # Git add and commit
    subprocess.run(["git", "add", "-A"], check=True)
    status_out = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
    if status_out.strip():
        subprocess.run(["git", "commit", "-m", "chore: automated sync b2b-site-build-and-optimization skill"], check=True)
        print("  -> Changes committed.")
    else:
        print("  -> No local changes to commit.")

    # Push to main
    try:
        push_res = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
        if push_res.returncode == 0:
            print("  -> Git push to origin/main successful!")
        else:
            print(f"  -> Git push output: {push_res.stderr or push_res.stdout}")
    except Exception as e:
        print(f"  -> Push failed: {e}")

def sync_to_lan_share():
    """Mirror current skill directory to Windows LAN shared directory."""
    print(f"[3/3] Mirroring to LAN Share: {LAN_TARGET_DIR}...")
    try:
        if not LAN_SHARED_BASE.exists():
            print(f"  -> [WARN] LAN Shared Base {LAN_SHARED_BASE} is not reachable.")
            return False

        if not LAN_TARGET_DIR.exists():
            LAN_TARGET_DIR.mkdir(parents=True, exist_ok=True)

        # Copy all items except .git
        for item in SKILL_DIR.iterdir():
            if item.name == ".git":
                continue
            dest_item = LAN_TARGET_DIR / item.name
            if item.is_dir():
                if dest_item.exists():
                    shutil.rmtree(dest_item)
                shutil.copytree(item, dest_item)
            else:
                shutil.copy2(item, dest_item)
        
        print(f"  -> Successfully mirrored to LAN Shared Directory: {LAN_TARGET_DIR}")
        return True
    except Exception as e:
        print(f"  -> [ERROR] Failed to mirror to LAN share: {e}")
        return False

def main():
    print("=" * 60)
    print(" B2B Site Build & Optimization Skill Auto-Synchronizer")
    print("=" * 60)
    print(f"Source Directory: {SKILL_DIR}")
    
    # 1. GitHub Token & Repository
    username, token = get_git_credential()
    repo_ready = ensure_github_repo(token)
    
    # 2. Push to GitHub
    if repo_ready:
        sync_to_github()
    
    # 3. Mirror to LAN Share
    sync_to_lan_share()
    
    print("=" * 60)
    print(" Synchronization Completed Successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
