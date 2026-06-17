#!/usr/bin/env python3
"""
Fetch GitHub repository info for trending repos and generate a CSV.
Uses GitHub REST API to get description and language for each repo.
"""
import csv
import json
import time
import urllib.request
import urllib.error
import os
import re

INPUT_FILE = "/Users/youzeliang/dev/code/python/github-trending-scraper/github_trending.csv"
OUTPUT_FILE = "/Users/youzeliang/dev/code/python/github-trending-scraper/trending_repos_analysis.csv"

# Optional: set GITHUB_TOKEN env var to avoid rate limits
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

def get_repo_info(owner, repo):
    """Fetch repo info from GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "trending-scraper/1.0")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            return data
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} for {owner}/{repo}")
        return None
    except Exception as e:
        print(f"  Error for {owner}/{repo}: {e}")
        return None

def build_description(data):
    """Build a 3-5 sentence description from repo data."""
    if not data:
        return "暂无描述信息。"
    
    name = data.get("name", "")
    full_name = data.get("full_name", "")
    desc = data.get("description") or ""
    stars = data.get("stargazers_count", 0)
    forks = data.get("forks_count", 0)
    topics = data.get("topics", [])
    language = data.get("language") or "未知"
    homepage = data.get("homepage") or ""
    
    sentences = []
    
    # Sentence 1: core description
    if desc:
        sentences.append(f"{desc}。")
    else:
        sentences.append(f"{name} 是一个开源项目，托管在 GitHub 上。")
    
    # Sentence 2: stars & forks
    sentences.append(f"该项目目前拥有 {stars:,} 颗星标（Star）和 {forks:,} 次 Fork，社区活跃度较高。")
    
    # Sentence 3: topics
    if topics:
        topics_str = "、".join(topics[:6])
        sentences.append(f"项目主要涉及领域包括：{topics_str}。")
    
    # Sentence 4: homepage if available
    if homepage and homepage.startswith("http"):
        sentences.append(f"官方网站或文档地址：{homepage}。")
    
    # Sentence 5: language
    sentences.append(f"主要编程语言为 {language}，适合相关技术栈的开发者参考和使用。")
    
    return " ".join(sentences[:5])

def main():
    # Read URLs
    urls = []
    with open(INPUT_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line and "github.com/" in line:
                urls.append(line)
    
    print(f"Found {len(urls)} repos to process")
    
    results = []
    for i, url in enumerate(urls, 1):
        # Extract owner/repo from URL
        match = re.search(r"github\.com/([^/]+)/([^/\s?#]+)", url)
        if not match:
            print(f"[{i}/{len(urls)}] Skip invalid URL: {url}")
            continue
        
        owner = match.group(1)
        repo = match.group(2)
        repo = re.sub(r'\.git$', '', repo)
        
        print(f"[{i}/{len(urls)}] Fetching: {owner}/{repo}")
        
        data = get_repo_info(owner, repo)
        language = (data.get("language") or "未知") if data else "未知"
        description = build_description(data)
        
        results.append({
            "项目地址": url,
            "项目说明": description,
            "语言": language,
        })
        
        # Respect rate limits: ~60 req/min unauthenticated, 5000 req/min authenticated
        if not GITHUB_TOKEN:
            time.sleep(0.8)
        else:
            time.sleep(0.05)
    
    # Write output CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["项目地址", "项目说明", "语言"])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"\nDone! Written {len(results)} rows to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
