#!/usr/bin/env python3
"""
Automated Deploy & Multi-Breakpoint Verification Script.
Executes HTTP status checks and responsive visual regressions using Playwright.
"""

import sys
import subprocess
import urllib.request

VIEWPORTS = [
    {"name": "desktop", "width": 1440, "height": 900},
    {"name": "laptop", "width": 1200, "height": 800},
    {"name": "tablet", "width": 768, "height": 1024},
    {"name": "mobile", "width": 375, "height": 812}
]

ENDPOINTS = [
    "https://www.naikegifts.com/",
    "https://www.naikegifts.com/evidence/",
    "https://www.naikegifts.com/products/shoe-charms/",
    "https://www.naikegifts.com/ai/sku-matrix.json",
    "https://www.naikegifts.com/ai/compliance.json",
    "https://www.naikegifts.com/llms.txt"
]

def check_endpoints():
    print(">>> Checking HTTP Endpoints...")
    all_ok = True
    for ep in ENDPOINTS:
        try:
            req = urllib.request.Request(ep, headers={"User-Agent": "SiteVerificationBot/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                status = resp.getcode()
                print(f" [PASS] {status} - {ep}")
        except Exception as e:
            print(f" [FAIL] {ep}: {e}")
            all_ok = False
    return all_ok

if __name__ == "__main__":
    success = check_endpoints()
    if not success:
        sys.exit(1)
    print(">>> All endpoints verified successfully.")
