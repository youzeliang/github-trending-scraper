#!/usr/bin/env python3
"""
GitHub Trending 项目分析同步脚本

功能：
1. 同步 github_projects_analysis.csv 与 github_trending.csv
2. 删除在 analysis 中存在但不在 trending 中的项目（并加入黑名单）
3. 添加 trending 中新增的项目到 analysis
4. 生成 Markdown 格式的分析报告

用法：
    python sync_github_projects.py [--fill] [--report]
"""

import csv
import re
import sys
from pathlib import Path
from datetime import datetime

# 路径配置
PROJECT_DIR = Path(__file__).parent
TRENDING_FILE = PROJECT_DIR / "github_trending.csv"
ANALYSIS_FILE = PROJECT_DIR / "github_projects_analysis.csv"
BLOCK_FILE = PROJECT_DIR / "block_github.csv"


def load_csv(file_path: Path) -> tuple[set, list]:
    """加载CSV文件，返回URL集合和原始行数据"""
    urls = set()
    rows = []
    
    if not file_path.exists():
        return urls, rows
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0].startswith('https://github.com/'):
                urls.add(row[0].strip())
                rows.append(row)
            elif row and row[0].startswith('#'):
                rows.append(row)
    
    return urls, rows


def save_csv(file_path: Path, rows: list):
    """保存CSV文件"""
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


def load_analysis_csv(file_path: Path) -> tuple[set, dict, list]:
    """加载分析CSV文件"""
    urls = set()
    url_to_row = {}
    header = None
    rows = []
    
    if not file_path.exists():
        return urls, url_to_row, header, rows
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                header = row
                rows.append(row)
                continue
            
            # Find URL in the row (could be in column 2 or 3 depending on format)
            url = None
            for cell in row:
                if isinstance(cell, str) and 'github.com' in cell:
                    url = cell.strip()
                    break
            
            if url:
                urls.add(url)
                url_to_row[url] = row
                rows.append(row)
            elif row and row[0].startswith('#'):
                rows.append(row)
    
    return urls, url_to_row, header, rows


def save_analysis_csv(file_path: Path, rows: list, header: list):
    """保存分析CSV文件"""
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows[1:]:  # Skip header
            writer.writerow(row)


def extract_project_name(url: str) -> str:
    """从URL提取项目名"""
    match = re.search(r'github\.com/([^/]+/[^/]+)', url)
    if match:
        return match.group(1)
    return url


def sync_files():
    """同步 trending 和 analysis 文件"""
    print("🔄 开始同步文件...")
    
    # 加载 trending 数据
    trending_urls, trending_rows = load_csv(TRENDING_FILE)
    print(f"📊 Trending 文件: {len(trending_urls)} 个项目")
    
    # 加载 analysis 数据
    analysis_urls, url_to_row, header, analysis_rows = load_analysis_csv(ANALYSIS_FILE)
    print(f"📋 Analysis 文件: {len(analysis_urls)} 个项目")
    
    # 加载黑名单
    block_urls, _ = load_csv(BLOCK_FILE)
    print(f"🚫 黑名单文件: {len(block_urls)} 个项目")
    
    # 找出需要删除的项目（在analysis中但不在trending中）
    to_remove = analysis_urls - trending_urls
    to_add = trending_urls - analysis_urls
    
    removed_count = 0
    added_count = 0
    
    # 处理需要删除的项目：从 analysis 和 trending 中同时删除
    if to_remove:
        print(f"\n🗑️  需要删除 {len(to_remove)} 个项目:")
        new_analysis_rows = [analysis_rows[0]]  # 保留header
        new_trending_rows = trending_rows.copy()
        
        for url in to_remove:
            # 添加到黑名单
            if url not in block_urls:
                block_urls.add(url)
                with open(BLOCK_FILE, 'a', encoding='utf-8') as f:
                    f.write(f"{url}\n")
                print(f"  ➕ 加入黑名单: {extract_project_name(url)}")
            
            # 从 trending 中删除
            new_trending_rows = [row for row in new_trending_rows if row[0] != url]
            removed_count += 1
        
        # 从 analysis 中删除
        for row in analysis_rows[1:]:
            url_found = None
            for cell in row:
                if isinstance(cell, str) and 'github.com' in cell:
                    url_found = cell.strip()
                    break
            if url_found and url_found not in to_remove:
                new_analysis_rows.append(row)
        
        # 保存更新后的文件
        save_analysis_csv(ANALYSIS_FILE, new_analysis_rows, header)
        with open(TRENDING_FILE, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            for row in new_trending_rows:
                writer.writerow(row)
    
    # 处理需要添加的新项目
    if to_add:
        print(f"\n➕ 需要添加 {len(to_add)} 个新项目:")
        analysis_count = len(analysis_urls)
        for url in sorted(to_add):
            project_name = extract_project_name(url)
            # 添加到 analysis
            with open(ANALYSIS_FILE, 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                new_row = [analysis_count + added_count + 1, project_name, url, "TBD", "TBD", "TBD"]
                writer.writerow(new_row)
            print(f"  ➕ 新增: {project_name}")
            added_count += 1
    
    print(f"\n✅ 同步完成！")
    print(f"   - 删除: {removed_count} 个项目")
    print(f"   - 新增: {added_count} 个项目")
    print(f"   - 黑名单现有: {len(block_urls)} 个项目")


def generate_markdown_report(output_file: Path = None):
    """生成 Markdown 格式的分析报告"""
    print("\n📝 生成 Markdown 报告...")
    
    analysis_urls, url_to_row, header, rows = load_analysis_csv(ANALYSIS_FILE)
    
    if not rows or len(rows) <= 1:
        print("⚠️  没有可用的分析数据")
        return
    
    md_content = []
    md_content.append("# GitHub Trending 项目分析\n")
    md_content.append(f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    md_content.append(f"> 项目总数: {len(analysis_urls)}\n")
    md_content.append("\n---\n")
    
    for i, row in enumerate(rows[1:], 1):  # Skip header
        # Find URL and other fields
        url = None
        project_name = None
        language = None
        description = None
        features = None
        
        for cell in row:
            if isinstance(cell, str) and 'github.com' in cell:
                url = cell.strip()
                # Extract project name from URL
                match = re.search(r'github\.com/([^/]+/[^/]+)', url)
                if match:
                    project_name = match.group(1)
            elif isinstance(cell, str):
                if cell.startswith('TBD') or cell.startswith('https://'):
                    continue
                # Try to identify what field this is based on position or content
                pass
        
        # Use actual row data if available
        if len(row) >= 2:
            if not project_name and row[1]:
                project_name = str(row[1])
        if len(row) >= 4:
            language = str(row[3]) if row[3] and row[3] != 'TBD' else '未知'
        if len(row) >= 5:
            description = str(row[4]) if row[4] and row[4] != 'TBD' else '待补充'
        if len(row) >= 6:
            features = str(row[5]) if row[5] and row[5] != 'TBD' else '待补充'
        
        if not url:
            continue
            
        md_content.append(f"## {i}. {project_name or 'Unknown'}\n")
        md_content.append(f"- **GitHub**: {url}\n")
        md_content.append(f"- **语言**: {language}\n")
        md_content.append(f"- **描述**: {description}\n")
        md_content.append(f"- **主要特性**: {features}\n")
        md_content.append("\n---\n")
    
    content = ''.join(md_content)
    
    if output_file:
        output_file.write_text(content, encoding='utf-8')
        print(f"✅ 报告已保存: {output_file}")
    else:
        print(content)
    
    return content


def show_status():
    """显示当前状态"""
    print("\n📊 文件状态:")
    
    trending_urls, _ = load_csv(TRENDING_FILE)
    analysis_urls, _, _, _ = load_analysis_csv(ANALYSIS_FILE)
    block_urls, _ = load_csv(BLOCK_FILE)
    
    print(f"   Trending: {len(trending_urls)} 个项目")
    print(f"   Analysis: {len(analysis_urls)} 个项目")
    print(f"   Blocked: {len(block_urls)} 个项目")
    print(f"   差异: {len(trending_urls) - len(analysis_urls)} 个")
    
    # 显示未填充的项目
    unfilled = []
    _, url_to_row, _, rows = load_analysis_csv(ANALYSIS_FILE)
    for row in rows[1:]:
        if len(row) >= 5 and row[3] == "TBD":
            unfilled.append(row[1])
    
    if unfilled:
        print(f"\n⚠️  未填充分析的项目: {len(unfilled)} 个")
        for p in unfilled[:10]:
            print(f"   - {p}")
        if len(unfilled) > 10:
            print(f"   ... 等等 (还有 {len(unfilled) - 10} 个)")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="GitHub Trending 项目分析同步工具")
    parser.add_argument('--sync', action='store_true', help='同步 trending 和 analysis 文件')
    parser.add_argument('--report', action='store_true', help='生成 Markdown 报告')
    parser.add_argument('--status', action='store_true', help='显示当前状态')
    
    args = parser.parse_args()
    
    # 默认行为：显示状态
    if not any([args.sync, args.report, args.status]):
        args.status = True
    
    if args.status:
        show_status()
    
    if args.sync:
        sync_files()
    
    if args.report:
        output = PROJECT_DIR / "github_projects_analysis.md"
        generate_markdown_report(output)
