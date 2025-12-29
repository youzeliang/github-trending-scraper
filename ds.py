from pathlib import Path
from typing import Dict, Any

from ollama import chat


def describe_repo(repo_url: str) -> str:
    """Ask the model what the repository does and return the answer text."""
    response: Dict[str, Any] = chat(
        model="deepseek-r1:8b",
        messages=[
            {
                "role": "user",
                "content": f"这个仓库主要是做什么的？仓库地址：{repo_url}",
            }
        ],
    )
    content = response["message"]["content"]
    # remove <think>...</think> reasoning content if present
    if "</think>" in content:
        content = content.split("</think>", 1)[1].strip()
    return content.strip()


def main() -> None:
    csv_path = Path(__file__).with_name("github_trending.csv")
    urls = [line.strip() for line in csv_path.read_text().splitlines() if line.strip()]

    for idx, url in enumerate(urls, 1):
        print(f"{idx}. {url}")
        try:
            summary = describe_repo(url)
            print(f"   结果: {summary}")
        except Exception as exc:  # noqa: BLE001
            print(f"   调用失败: {exc}")


if __name__ == "__main__":
    main()