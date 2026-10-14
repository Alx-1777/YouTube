#!/usr/bin/env bash
# 在 Mac 上一键安装本项目需要的工具。在仓库根目录运行：bash scripts/setup-mac.sh
set -euo pipefail

if ! command -v brew >/dev/null 2>&1; then
  echo "没有找到 Homebrew，请先安装：https://brew.sh" >&2
  exit 1
fi

brew install ffmpeg python deno

python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install yt-dlp faster-whisper youtube-transcript-api

# 预先下载语音识别模型（约 500MB）
.venv/bin/python -c "from faster_whisper import WhisperModel; WhisperModel('small', device='cpu', compute_type='int8')"

if [ -z "${YOUTUBE_API_KEY:-}" ]; then
  echo
  echo "提醒：还没有设置 YOUTUBE_API_KEY。在终端运行："
  echo "  echo 'export YOUTUBE_API_KEY=你的key' >> ~/.zshrc && source ~/.zshrc"
fi

echo
echo "安装完成。"
