#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GitHub趋势项目爬虫
~~~~~~~~~~~~~~~~

这个脚本可以爬取GitHub趋势页面上的热门项目信息，
支持按日期和编程语言筛选，并可将数据导出为CSV或JSON格式。
"""

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Union

import requests
from bs4 import BeautifulSoup


class GitHubTrending:
    """GitHub趋势项目爬虫类"""

    BASE_URL = "https://github.com/trending"
    BLOCKLIST_FILE = "block_github.csv"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }

    def __init__(self) -> None:
        """初始化GitHub趋势爬虫"""
        self.base_dir = Path(__file__).resolve().parent
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

    def get_trending(
        self, period: str = "daily", language: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        获取GitHub趋势项目信息

        参数:
            period: 时间范围，可选值为 'daily'(今日)、'weekly'(本周)、'monthly'(本月)，默认为'daily'
            language: 编程语言，例如'python'、'javascript'等，默认为None(所有语言)

        返回:
            包含项目信息的字典列表
        """
        # 构建URL
        url = self.BASE_URL
        if language:
            url = f"{url}/{language}"
        
        # 添加时间范围参数
        period_mapping = {"daily": "daily", "weekly": "weekly", "monthly": "monthly"}
        if period in period_mapping:
            separator = "?" if "?" not in url else "&"
            url = f"{url}{separator}since={period_mapping[period]}"

        # 从 block 列表和历史 CSV 中加载已存在的链接，避免重复
        blocklist = self._load_blocklist()

        history_urls: Set[str] = set()
        try:
            history_file = self._resolve_path("github_trending.csv")
            if history_file.exists():
                # 复用 _load_blocklist 读取简单的单列 CSV（无表头）
                history_urls = self._load_blocklist(str(history_file))
        except Exception:
            # 历史文件读取失败时，不影响本次抓取
            history_urls = set()

        existed_urls: Set[str] = blocklist | history_urls

        try:
            # 发送请求
            response = self.session.get(url, timeout=30)
            response.raise_for_status()  # 检查请求是否成功
            
            # 解析HTML
            repositories = self._parse_html(response.text)
            if not repositories:
                print(f"警告: 未能从页面解析到任何项目，URL: {url}")
                return []

            # 过滤掉已存在于 block_github.csv 和 github_trending.csv 中的链接
            filtered_repositories: List[Dict[str, Any]] = []
            seen_in_batch: Set[str] = set()
            for repo in repositories:
                url_value = repo.get('url')
                if not url_value:
                    continue
                if url_value in existed_urls:
                    continue
                if url_value in seen_in_batch:
                    continue
                seen_in_batch.add(url_value)
                filtered_repositories.append(repo)

            return filtered_repositories
        
        except requests.Timeout:
            print(f"请求超时: {url}")
            return []
        except requests.RequestException as e:
            print(f"请求出错: {e}")
            return []
        except Exception as e:
            print(f"处理过程中出错: {e}")
            return []

    def _parse_html(self, html_content: str) -> List[Dict[str, Any]]:
        """
        解析HTML内容，提取项目信息

        参数:
            html_content: HTML内容

        返回:
            包含项目信息的字典列表
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        repositories: List[Dict[str, str]] = []

        # 查找所有项目块 - 尝试多种可能的选择器
        article_blocks = soup.select('article.Box-row')
        
        # 如果没找到，尝试其他可能的选择器
        if not article_blocks:
            article_blocks = soup.select('article')
        
        for article in article_blocks:
            # 尝试多种可能的选择器来找到仓库链接
            repo_name_element = (
                article.select_one('h2.h3.lh-condensed a') or
                article.select_one('h2 a') or
                article.select_one('h3 a') or
                article.select_one('a[href*="/"]')
            )
            
            if repo_name_element:
                href = repo_name_element.get('href')
                if href:
                    # 确保URL是完整的
                    if href.startswith('http'):
                        repo_url = href
                    elif href.startswith('/'):
                        repo_url = f"https://github.com{href}"
                    else:
                        repo_url = f"https://github.com/{href}"
                    repositories.append({'url': repo_url})
        
        return repositories

    def _resolve_path(self, filename: Union[str, Path]) -> Path:
        """将相对路径解析到脚本所在目录"""
        path = Path(filename)
        if path.is_absolute():
            return path
        return self.base_dir / path

    def _load_blocklist(self, block_filename: Optional[str] = None) -> Set[str]:
        """
        加载 block 列表

        参数:
            block_filename: block列表文件名

        返回:
            包含所有 block 项目的集合
        """
        block_filename = self._resolve_path(block_filename or self.BLOCKLIST_FILE)
        blocklist: Set[str] = set()
        if not block_filename.exists():
            return blocklist

        try:
            with block_filename.open(newline='', encoding='utf-8') as block_file:
                reader = csv.reader(block_file)
                for row in reader:
                    if not row:
                        continue
                    value = row[0].strip()
                    if not value:
                        continue
                    if value.lower() == 'url' and not blocklist:
                        continue
                    blocklist.add(value)
        except OSError as e:
            print(f"读取 block 文件失败: {e}")

        return blocklist

    def add_to_blocklist(self, value: str, block_filename: Optional[str] = None) -> None:
        """
        将条目写入 block 列表文件

        参数:
            value: 要写入的字符串
            block_filename: block列表文件名
        """
        block_filename = self._resolve_path(block_filename or self.BLOCKLIST_FILE)
        value = value.strip()
        if not value:
            print("无法写入空字符串到 block 列表")
            return

        blocklist = self._load_blocklist(block_filename)
        if value in blocklist:
            print(f"{value} 已存在于 block 列表中")
            return

        needs_header = True
        if block_filename.exists():
            needs_header = block_filename.stat().st_size == 0

        try:
            with block_filename.open('a', newline='', encoding='utf-8') as block_file:
                writer = csv.writer(block_file)
                if needs_header:
                    writer.writerow(['url'])
                writer.writerow([value])
            print(f"已添加到 block 列表: {value}")
        except OSError as e:
            print(f"写入 block 文件失败: {e}")

    def save_to_csv(self, data: List[Dict[str, Any]], filename: str) -> None:
        """
        将数据保存为CSV文件

        参数:
            data: 要保存的数据
            filename: 文件名
        """
        if not data:
            print("没有数据可保存")
            return
        
        try:
            output_path = self._resolve_path(filename)
            if not data:
                return

            # 去重（同一批次内不重复）
            unique_data: List[Dict[str, Any]] = []
            batch_seen: Set[str] = set()
            for item in data:
                url_val = item.get("url")
                if not url_val:
                    continue
                if url_val in batch_seen:
                    continue
                batch_seen.add(url_val)
                unique_data.append({"url": url_val})

            if not unique_data:
                print("没有新的数据可写入")
                return

            file_exists = output_path.exists()
            file_empty = (not file_exists) or output_path.stat().st_size == 0

            # 新建文件时写入 BOM，追加时不再写 BOM
            mode = 'w' if file_empty else 'a'
            encoding = 'utf-8-sig' if file_empty else 'utf-8'

            with output_path.open(mode, newline='', encoding=encoding) as csvfile:
                for item in unique_data:
                    csvfile.write(f"{item['url']}\n")

            print(f"数据已保存到 {output_path}")
        except Exception as e:
            print(f"保存CSV文件时出错: {e}")

    def save_to_json(self, data: List[Dict[str, Any]], filename: str) -> None:
        """
        将数据保存为JSON文件

        参数:
            data: 要保存的数据
            filename: 文件名
        """
        if not data:
            print("没有数据可保存")
            return
        
        try:
            output_path = self._resolve_path(filename)
            with output_path.open('w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"数据已保存到 {output_path}")
        except Exception as e:
            print(f"保存JSON文件时出错: {e}")


def main() -> None:
    """主函数，处理命令行参数并执行爬虫"""
    parser = argparse.ArgumentParser(description='GitHub趋势项目爬虫')
    parser.add_argument('--period', type=str, default='daily',
                        choices=['daily', 'weekly', 'monthly'],
                        help='时间范围：daily(今日)、weekly(本周)、monthly(本月)')
    parser.add_argument('--language', type=str, default=None,
                        help='编程语言，例如python、javascript等')
    parser.add_argument('--output', type=str, default='github_trending.csv',
                        help='输出文件名')
    parser.add_argument('--format', type=str, default='csv',
                        choices=['csv', 'json'],
                        help='输出格式：csv或json')
    
    args = parser.parse_args()
    
    # 创建爬虫实例
    scraper = GitHubTrending()
    
    # 获取趋势项目
    print(f"正在获取GitHub {args.period} 趋势项目" + (f"（{args.language}）" if args.language else "..."))
    trending_repos = scraper.get_trending(period=args.period, language=args.language)
    
    if not trending_repos:
        print("未获取到任何数据")
        return
    
    print(f"获取到 {len(trending_repos)} 个项目")
    
    # 保存数据
    if args.format == 'csv':
        output_file = args.output if args.output.endswith('.csv') else f"{args.output}.csv"
        scraper.save_to_csv(trending_repos, output_file)
    else:
        output_file = args.output if args.output.endswith('.json') else f"{args.output}.json"
        scraper.save_to_json(trending_repos, output_file)


if __name__ == '__main__':
    main()
