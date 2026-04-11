#!/usr/bin/env python3
import requests
import sys

url = "https://api.github.com/repos/microsoft/VibeVoice"
headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "GitHubRepoScanner/1.0"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    print(f"Status: {response.status_code}", file=sys.stderr)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Language: {data.get('language')}", file=sys.stderr)
        print(f"Description: {data.get('description')}", file=sys.stderr)
        print("SUCCESS")
    else:
        print(f"ERROR: {response.status_code}")
        sys.exit(1)
except Exception as e:
    print(f"Exception: {e}", file=sys.stderr)
    sys.exit(1)
