# How It Works：频道主线（2026-10-30 定）

**一句话**：一个 19 岁的数学专业学生，每天拆解一样东西，用 3D 模型讲清楚它是怎么工作的。英文，高质量长视频，日更。

## 格式
- **英文**，横屏 1080p 30fps，**8–12 分钟**
- 主画面：**3D 模型录屏**（录屏模式按 H）+ 你出镜讲解（画中画或穿插）
- 每期结构：
  1. **钩子（0:00–0:30）**：一个反常识的问题或数字（"90% of a rocket is fuel"、"Why is Nvidia worth trillions?"）
  2. **拆开它**：从外到内，一个部件一个部件讲
  3. **核心原理**：一个公式、一个比喻、一个动画
  4. **为什么重要**：和钱、AI、未来联系起来（观众为什么要在乎）
  5. **结尾**：一句话总结 + 明天拆什么
- 字幕：英文 + 中文双语
- 免责：涉及公司（Nvidia、SpaceX、Tesla）时不做投资建议

## 分工流程

| 步骤 | 谁 | 产出 |
|---|---|---|
| 1. 选题 | 一起 | 从下面的选题库里挑 |
| 2. 学习 | **Alx** | 自己先学懂（Claude 可以提供学习资料清单） |
| 3. 3D 模型 | **Claude** | 交互式模型 artifact，带部件说明、动画、录屏模式 |
| 4. 脚本 | **Claude** | 英文逐段脚本 + 中文对照 + 发音提醒 |
| 5. 录制 | **Alx** | 横屏长视频，放桌面 |
| 6. 字幕、标题、简介、章节 | **Claude** | 双语字幕、中英两版标题和简介 |
| 7. 切 Shorts | **Claude** | 每期 2–3 条 30–60 秒竖屏切片，烧录字幕，放回桌面 |
| 8. 上传 | **Alx** | 手动发 YouTube / TikTok / 抖音 / 小红书 |

## 保底规则（日更不断）
- 当天来不及做长视频：用已有的模型录一条 60 秒 Short，也算完成。
- 不能连续两天不发。
- 每周日看一次数据，挑表现最好的题材做续集。

## 已有的模型
| 主题 | 模型 | 状态 |
|---|---|---|
| 火箭（Falcon 9） | https://claude.ai/artifact/LVwSz4cwN359pG2FrxyW6f | 模型 ✅，脚本有中文版（docs/scripts/ep02-how-rockets-work.md），需改英文 |
| 电脑 / GPU | https://claude.ai/artifact/2JTuwab5Hz9adJxKqt5Ky2 | 模型 ✅，脚本待写 |

## 选题库（按"大"排序：和钱、AI、热点有关的优先）

| # | 标题（英文） | 角度 |
|---|---|---|
| 1 | Why Is Nvidia Worth Trillions? I Took a Computer Apart | GPU vs CPU，AI 为什么需要显卡（模型已有） |
| 2 | Why SpaceX Lands Its Rockets | 火箭方程、90% 是燃料、回收省钱（模型已有） |
| 3 | How ChatGPT Actually Works | 神经网络、token、预测下一个词（Alx 正在学神经网络） |
| 4 | How a Humanoid Robot Works | 电机、传感器、平衡；Day 3 日记里说过 AI 时代要关注硬件 |
| 5 | How Starlink Gets Internet From Space | 低轨卫星、相控阵天线 |
| 6 | How a Tesla Motor Works | 电机、电池、为什么电动车加速快 |
| 7 | How Bitcoin Mining Works | 哈希、矿机、能源（不做投资建议） |
| 8 | How a Computer Chip Is Made | 光刻机、为什么 ASML 那么重要 |
| 9 | How a Jet Engine Works | 进气、压缩、燃烧、排气 |
| 10 | How the Internet Crosses the Ocean | 海底光缆 |
| 11 | How Noise-Cancelling Headphones Work | 反相声波 |
| 12 | How GPS Knows Where You Are | 卫星、相对论修正 |
| 13 | How a Nuclear Reactor Works | 裂变、为什么 AI 数据中心在抢核电 |
| 14 | How an iPhone Camera Works | 传感器、计算摄影 |
