# Alx 的 YouTube 运营大本营

每次会话开始先读 `docs/channel-profile.md`（我是谁、频道定位）和 `docs/` 下的最新计划。

## 工具与凭证
- YouTube Data API v3：通过 Network secret 注入（请求头 `X-goog-api-key`），直接请求
  `https://www.googleapis.com/youtube/v3/...` 即可，不需要在代码里写 Key。
- X API：环境已接入 api.x.com（目前是 App-only 认证，只能读公开数据）。
- 剪辑：容器内有 ffmpeg / ffprobe / Python3 / Node。

## 约定
- 用中文沟通。
- 发布、上传、发推等对外操作必须先征得同意。
- 大视频文件不要提交进 Git。
