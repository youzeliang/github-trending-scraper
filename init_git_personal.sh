#!/usr/bin/env bash
set -e

# === 配置区：根据需要修改 ===
GIT_USER_NAME="rolle"
GIT_USER_EMAIL="youzel@126.com"
GITHUB_HOST_ALIAS="github.com-personal"  # 对应 ~/.ssh/config 里的 Host
GITHUB_USER="youzeliang"                 # 你的 GitHub 用户名
# ==================================

# 项目路径（可选第一个参数，不传则用当前目录）
PROJECT_DIR="${1:-$(pwd)}"

cd "$PROJECT_DIR"

# 用当前目录名作为仓库名
REPO_NAME="$(basename "$PROJECT_DIR")"

echo "项目目录: $PROJECT_DIR"
echo "仓库名:   $REPO_NAME"
echo "GitHub:   $GITHUB_USER / $REPO_NAME"
echo

# 如果已经有 .git，则给出提示，避免误覆盖
if [ -d ".git" ]; then
  echo "当前目录已存在 .git，脚本不会覆盖。"
  echo "如需重新初始化，请先手动删除 .git 后再运行："
  echo "  rm -rf .git"
  exit 1
fi

echo "===> 初始化 git 仓库"
git init

echo "===> 设置本地用户信息"
git config user.name  "$GIT_USER_NAME"
git config user.email "$GIT_USER_EMAIL"

echo "===> 切换默认分支为 main"
git branch -M main

echo "===> 添加所有文件并提交"
git add .
git commit -m "Initial commit"

echo "===> 配置远程仓库 origin"
REMOTE_URL="git@${GITHUB_HOST_ALIAS}:${GITHUB_USER}/${REPO_NAME}.git"
git remote add origin "$REMOTE_URL"

echo "远程地址: $REMOTE_URL"
echo
echo "注意：GitHub 上必须先创建空仓库："
echo "  owner: $GITHUB_USER"
echo "  name : $REPO_NAME"
echo

echo "===> 推送到远程 main 分支"
set +e
git push -u origin main
PUSH_EXIT=$?
set -e

if [ $PUSH_EXIT -ne 0 ]; then
  echo
  echo "推送失败，常见原因："
  echo "  1) GitHub 上还没有创建仓库 ${GITHUB_USER}/${REPO_NAME}"
  echo "  2) 当前 SSH key 没有该仓库的写权限"
  echo
  echo "请先在 GitHub 上创建空仓库后，再运行："
  echo "  git push -u origin main"
  exit $PUSH_EXIT
fi

echo
echo "完成：项目已使用个人 SSH 账号推送到 GitHub。"

