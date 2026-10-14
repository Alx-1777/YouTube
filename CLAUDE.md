# Alx 的 YouTube 运营大本营

每次会话开始先读：
- `docs/claude-chat-notes.md`：已定的决策（语言路线、英语计划、频道设计、第 1 期大纲、规矩）。**以它为准。**
- `docs/channel-structure.md`：频道板块和每周排期。
- `docs/channel-profile.md`：我是谁、频道和 X 数据、对标频道。
- `docs/references/`：参考资料笔记。

注意：仓库是公开的，不要写入持仓金额、花销等隐私信息。

## 工具与凭证
本项目既在云端会话运行，也在用户的 Mac 本地运行。

**云端**
- YouTube Data API v3：通过 Network secret 注入（请求头 `X-goog-api-key`），直接请求
  `https://www.googleapis.com/youtube/v3/...` 即可，不需要在代码里写 Key。
- X API：环境已接入 api.x.com（目前是 App-only 认证，只能读公开数据）。
- 容器内有 ffmpeg / Python3 / Node；Whisper 等需要每次装进临时 venv。
- 云端 IP 被 YouTube 封锁：无法下载视频或字幕，只能用 API 拿元数据。

**本地（Mac）**
- 首次运行 `bash scripts/setup-mac.sh` 安装 ffmpeg、yt-dlp、faster-whisper 等，Python 工具在 `.venv/`。
- YouTube API Key 在环境变量 `YOUTUBE_API_KEY` 里，请求时加 `key=$YOUTUBE_API_KEY` 参数；不要把 Key 打印出来或写进文件。
- 视频素材放在 `media/`（已被 .gitignore 忽略）。

## 约定
- 用中文沟通。
- 发布、上传、发推等对外操作必须先征得同意。
- 大视频文件不要提交进 Git。
