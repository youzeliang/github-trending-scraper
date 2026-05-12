#!/usr/bin/env python3
"""
Fetch GitHub repo info concurrently and write a CSV.
"""
import csv
import json
import os
import re
import time
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

INPUT_FILE = "/Users/youzeliang/dev/code/python/github-trending-scraper/github_trending.csv"
OUTPUT_FILE = "/Users/youzeliang/dev/code/python/github-trending-scraper/trending_repos_analysis.csv"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "trending-scraper/1.0",
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


def get_repo_info(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return None


def build_description(data):
    if not data:
        return "暂无描述信息。"
    name = data.get("name", "")
    desc = (data.get("description") or "").strip()
    stars = data.get("stargazers_count", 0)
    forks = data.get("forks_count", 0)
    topics = data.get("topics", [])
    language = data.get("language") or "未知"
    homepage = (data.get("homepage") or "").strip()

    sentences = []
    if desc:
        sentences.append(f"{desc}。")
    else:
        sentences.append(f"{name} 是一个开源项目，托管在 GitHub 上。")
    sentences.append(f"该项目目前拥有 {stars:,} 颗 Star 和 {forks:,} 次 Fork，受到开发者广泛关注。")
    if topics:
        sentences.append("项目涉及领域：" + "、".join(topics[:6]) + "。")
    if homepage and homepage.startswith("http"):
        sentences.append(f"官网/文档：{homepage}。")
    sentences.append(f"主要编程语言为 {language}，适合相关技术栈的开发者参考使用。")
    return " ".join(sentences[:5])


def process_url(url):
    match = re.search(r"github\.com/([^/]+)/([^/\s?#]+)", url)
    if not match:
        return url, "无效URL", "未知"
    owner, repo = match.group(1), re.sub(r"\.git$", "", match.group(2))
    data = get_repo_info(owner, repo)
    language = (data.get("language") or "未知") if data else "未知"
    description = build_description(data)
    return url, description, language


def main():
    urls = []
    with open(INPUT_FILE) as f:
        for line in f:
            line = line.strip()
            if line and "github.com/" in line:
                urls.append(line)
    print(f"Total repos: {len(urls)}")

    results_map = {}
    workers = 10 if GITHUB_TOKEN else 5
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(process_url, u): u for u in urls}
        done = 0
        for fut in as_completed(futures):
            url, desc, lang = fut.result()
            results_map[url] = (desc, lang)
            done += 1
            if done % 20 == 0:
                print(f"  Progress: {done}/{len(urls)}")

    # Write in original order
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["项目地址", "项目说明", "语言"])
        writer.writeheader()
        for url in urls:
            desc, lang = results_map.get(url, ("暂无描述", "未知"))
            writer.writerow({"项目地址": url, "项目说明": desc, "语言": lang})

    print(f"Done! {len(urls)} rows -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
