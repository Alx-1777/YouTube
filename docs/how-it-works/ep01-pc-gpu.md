# How It Works #1：Every Part of a Computer, Explained in 3D (And Why AI Needs the GPU)

_英文 · 横屏 · 目标 10 分钟 · 模型：https://claude.ai/artifact/2JTuwab5Hz9adJxKqt5Ky2 · 2026-10-30_

**素材来源**：Alx 学习 PC Explainer《Every PC Component Explained in 10 minutes》后的手写笔记（5 页）+ Alx 正在学的 Karpathy micrograd。
**和那期的区别**：用我们自己的厨房比喻（不是它的"办公室"比喻）；3D 模型拆解；主线落到 AI 和 GPU；加入 Alx 自己的神经网络笔记。

**用法**：
- **粗体**是骨架，记住它，其余用自己的话说。
- 【方括号】是你在模型上要做的操作，录屏模式先按 **H**。
- 你的手写笔记本可以出镜：讲到"I took notes"时拿起来给镜头看。

---

## 1. Hook（0:00）
【模型：按 E 爆炸视图，按空格慢慢旋转。前 5 秒画面就是爆炸视图】
**This is everything inside a computer.**
I spent a week learning what every single part does. In 10 minutes, you'll know too.
**And you'll see why one of these parts matters more to AI than all the others combined.**

> **中文**：这就是一台电脑里的全部东西。我花了一周时间，弄明白了每一个部件是干什么的。10 分钟后，你也会知道。而且你会看到，其中有一个部件对 AI 来说，比其他所有部件加起来都重要。

## 2. Who I am（0:15）
I'm Alex. I'm 19, I study math at UCSD, and every day I take one thing apart and figure out how it works.
This week I studied every part of a PC. **Here are my notes.** 【拿起笔记本】
By the end of this video, you'll know what every part does, and why AI needs the GPU more than anything else.

> **中文**：我是 Alex，19 岁，在 UCSD 读数学。我每天拆开一样东西，弄明白它是怎么工作的。这周我学了电脑的每一个部件，这是我的笔记。看完这期视频，你会知道每个部件是干什么的，以及为什么 AI 最需要的是 GPU。

## 3. A computer is a kitchen（0:45）
【保持爆炸视图，开头已经按过 E】
Open up any PC and it looks like a random pile of parts. But it's not random.
**Think of it as a restaurant kitchen.** Every part has one job.
Let's meet the team.

> **中文**：打开任何一台电脑，看起来都像一堆乱七八糟的零件。但它不是乱的。把它想成一个餐厅的厨房，每个部件都只有一份工作。我们来认识一下这个团队。

## 4. CPU: the head chef（1:05）
【点 CPU】
The **CPU**, Central Processing Unit, is the **head chef**. Every time you click, type, or open an app, the CPU decides what to do.
It has **cores**. **One core is one worker.** A home PC usually has 8 to 24.
And each core has a **clock speed**, measured in **gigahertz**. Giga means a billion. So **5 gigahertz means 5 billion steps every second.**
Smart, fast, and can do anything. But there are only a few of them. Remember that, it matters later.

> **中文**：CPU，中央处理器，是主厨。每次你点击、打字、打开一个应用，都是 CPU 在决定要做什么。它有核心，一个核心就是一个工人。家用电脑一般有 8 到 24 个。每个核心有一个时钟频率，单位是吉赫兹（GHz）。吉的意思是十亿，所以 5 GHz 就是每秒 50 亿步。聪明、快、什么都能做，但数量很少。记住这一点，后面会用到。

## 5. RAM: the countertop（2:00）
【点 RAM】
The CPU needs somewhere to lay out its work. That's **RAM**, Random Access Memory. It's the **countertop**.
Your open apps, your browser tabs, the file you're editing: they all sit here, so the chef can grab them instantly.
Bigger countertop, more things open at once.
But here's what trips everyone up: **RAM is not storage.** Turn off the power, and the countertop gets wiped clean.

> **中文**：CPU 需要一个地方摊开它手头的工作，这就是 RAM，内存。它是操作台。你打开的应用、浏览器标签页、正在编辑的文件，都放在这里，主厨伸手就能拿到。操作台越大，能同时打开的东西越多。但很多人搞错的一点是：内存不是存储。一断电，操作台就被清空了。

## 6. SSD: the fridge（2:45）
【点 SSD】
So where does your stuff actually live? In storage. The **SSD**, Solid State Drive, is the **fridge**.
It keeps your files, your apps, and your whole operating system, even when the power is off.
**The countertop forgets. The fridge remembers.**
Old hard drives, called **HDDs**, Hard Disk Drives, spin a disk, like digging through a messy garage. An SSD has no moving parts. A PC that took a minute to start on a hard drive can start in seconds on an SSD.

> **中文**：那你的东西到底存在哪？存储里。SSD（Solid State Drive），固态硬盘，就是冰箱。它保存你的文件、应用和整个操作系统，断电也不会丢。操作台会忘，冰箱会记住。老式机械硬盘 HDD（Hard Disk Drive）靠转动的盘片存数据，找文件就像在乱糟糟的车库里翻东西；SSD 没有任何会动的零件。用机械硬盘要一分钟才能开机的电脑，换成 SSD 几秒钟就好。

## 7. Motherboard: the hallways（3:35）
【点 Motherboard】
Every part plugs into the **motherboard**. It's the kitchen's **floor and hallways**.
It doesn't cook anything. But **it sets the limits**: which CPU fits, how much RAM you can add, how many parts you can plug in later.
That's why people building a PC often **pick it first**.

> **中文**：所有部件都插在主板上，它是厨房的地面和走廊。它自己不做菜，但它决定上限：能装什么 CPU、能加多少内存、以后还能插多少部件。所以很多人装电脑时，第一个选的就是主板。

## 8. Power supply: the heart（4:10）
【点 Power Supply】
The **power supply**, or **PSU**, Power Supply Unit, is the **heart**. The wall gives you high-voltage **AC**, Alternating Current. Your parts need low-voltage **DC**, Direct Current.
**The power supply converts it and splits it out** to every part.
It won't make your PC faster, but **never go cheap on it.** A bad one can fail and take other parts down with it.

> **中文**：电源（PSU，Power Supply Unit）是心脏。墙上插座给的是高压交流电（AC，Alternating Current），电脑部件需要的是低压直流电（DC，Direct Current）。电源负责转换，再分配给每一个部件。它不会让电脑变快，但千万别买便宜的。劣质电源可能会坏，还会连带把其他部件一起烧掉。

## 9. Cooling: the exhaust fan（4:45）
【点 CPU Cooler，再点 Case Fans】
Every part that uses power makes heat. And when a chip gets too hot, **it protects itself by slowing down.** That's called **thermal throttling**.
Air cooling uses metal fins and fans. Liquid cooling pumps liquid through the hot parts, like jumping into a pool instead of standing in front of a fan.
**Cool air in the front, hot air out the back.** If your PC gets loud and slow after a few years, it might just be hot and dusty inside.

> **中文**：每个用电的部件都会发热。芯片太热的时候，会主动降速来保护自己，这叫热降频（thermal throttling）。风冷用金属散热片和风扇；水冷用液体流过发热的部件，把热量带走得更快，就像从吹风扇换成跳进泳池。前面进冷风，后面出热风。如果你的电脑用了几年变得又吵又慢，可能只是里面又热又积灰了。

## 10. GPU: the army of line cooks（5:30）
【点 GPU】
Now the star of this video. The **GPU**, Graphics Processing Unit.
Its original job: draw everything you see on screen. Millions of tiny dots called pixels, 60 times a second.
**The CPU is a few very smart workers, doing hard tasks one after another. The GPU is thousands of simple workers, all working at the same time.**
【面板：CPU vs GPU，点 Run race】
Watch this. 1,024 simple tasks. The CPU has 16 cores, so it does 16 at a time. The GPU does all of them at once.
**The CPU is one genius. The GPU is an army.**

> **中文**：现在是这期视频的主角：GPU，图形处理器，也就是显卡。它原来的工作是画出你在屏幕上看到的一切：每秒 60 次，画几百万个叫像素的小点。CPU 是几个非常聪明的工人，一件接一件地做难事；GPU 是几千个简单的工人，同时一起干活。看这个：1,024 个简单任务。CPU 有 16 个核心，一次做 16 个；GPU 一次全部做完。CPU 是一个天才，GPU 是一支军队。

## 11. Why AI needs the army（6:30）
【拿起笔记本，翻到代码那页】
Here's where it gets interesting. I'm also learning how neural networks work, and this is the very first thing you learn.
Take a tiny formula: **d = a times b plus c.** a is 2, b is minus 3, c is 10. So d is 4.
Now **nudge a by a tiny amount**, 0.0001, and see how much d changes. It goes down by about 3 times that amount. So the **slope** is minus 3.
**That's how AI learns.** It nudges millions of numbers, checks which way makes the answer better, and moves them a tiny bit. Then it does it again. And again. **Billions of times.**
Each step is simple math. There's just an insane amount of it, and most of it can happen at the same time.
**Simple math, done in parallel, billions of times. That's exactly what a GPU is built for.**
【按 1～5：AI 数据流】
So when you ask an AI a question: the model is loaded from the SSD into RAM, sent to the GPU, thousands of cores multiply numbers at the same time, and the answer comes back word by word.

> **中文**：有意思的地方来了。我也在学神经网络是怎么工作的，这是入门学的第一件事。拿一个很小的公式：d = a × b + c。a 是 2，b 是 −3，c 是 10，所以 d 等于 4。现在把 a 挪一点点，0.0001，看 d 变了多少。它减少了大约这个量的 3 倍，所以斜率是 −3。AI 就是这样学习的：它把几百万个数字各挪一点点，看往哪个方向挪能让答案更好，再挪一小步。然后再来一次，再来一次，重复几十亿次。每一步都是简单的数学，只是量大得离谱，而且大部分可以同时进行。简单的数学，并行地做几十亿次，这正是 GPU 生来要干的事。所以你问 AI 一个问题时：模型从硬盘读进内存，再送进 GPU，几千个核心同时做乘法，答案再一个词一个词地传回来。

## 12. The one rule: bottlenecks（8:00）
【按 0：全景】
One idea ties the whole team together: **a computer is only as fast as its weakest worker.** That's a **bottleneck**.
A genius CPU with a slow hard drive just sits there waiting. Balance beats one superstar.
And for AI, the GPU was the bottleneck. **Whoever makes the best GPUs controls the speed of AI.** That's why Nvidia is worth so much.

> **中文**：有一个道理能把整个团队串起来：电脑的速度，取决于最弱的那个工人。这叫瓶颈。天才 CPU 配一块慢硬盘，只能干等着。均衡比一个超级明星更重要。而对 AI 来说，GPU 曾经就是那个瓶颈。谁造出最好的 GPU，谁就决定了 AI 的速度。这就是英伟达这么值钱的原因。

## 13. Gigawatts（8:40）
One more number from my notes. **A gigawatt is a billion watts, roughly the output of a large nuclear power plant.**
Some of the AI data centers being built now are planned at around that scale. Thousands of these GPUs, running all day, need their own power plant.
So tomorrow, I'm taking apart something much bigger: **how a nuclear reactor works.** 【或者换成你想拆的下一个】

> **中文**：再说我笔记里的一个数字：1 吉瓦是十亿瓦，大约是一座大型核电站的发电量。现在正在建的一些 AI 数据中心，规划的规模就在这个量级。几千块这样的 GPU 全天运转，需要一座自己的发电站。所以明天，我要拆一个大得多的东西：核反应堆是怎么工作的。

## 14. Ending（9:15）
Quick recap: the CPU is the head chef, RAM is the countertop, the SSD is the fridge, the motherboard is the hallways, the power supply is the heart, cooling keeps everyone calm, and **the GPU is the army that makes AI possible.**
**Which part surprised you the most? Tell me in the comments.**
I'm Alex, I take one thing apart every day. See you tomorrow.

> **中文**：快速回顾：CPU 是主厨，内存是操作台，SSD 是冰箱，主板是走廊，电源是心脏，散热让大家保持冷静，而 GPU 是让 AI 成为可能的那支军队。哪个部件最让你意外？评论区告诉我。我是 Alex，每天拆一样东西，明天见。

---

## 发音提醒
| 词 | 读法 |
|---|---|
| Nvidia | en-**VID**-ee-uh |
| gigahertz | **GIG**-uh-hurts（g 读硬音 /g/） |
| throttling | **THROT**-ling（th 舌尖在齿间） |
| parallel | **PAR**-uh-lel |
| neural | **NUR**-ul |
| bottleneck | **BOT**-ul-neck |

## 事实核对
- 家用 CPU 8–24 核、约 5 GHz；高端游戏显卡 16,000+ 核心：模型里的数字，一致。
- d = a·b + c，a=2, b=−3, c=10 → d=4；∂d/∂a = b = −3：和笔记一致。
- "1 GW ≈ 一座大型核电站"：笔记原话，正确；"部分在建 AI 数据中心规划在吉瓦级"：用 "some… planned at around that scale"，不说具体公司和数字。
- Nvidia 只说 "one of the most valuable companies in the world"，不报市值（会变），不做投资建议。

## 标题 / 封面（2026-10-30 定）
- EN：`Every Part of a Computer, Explained in 3D (And Why AI Needs the GPU)`
- 中文：`电脑里每个部件都在干什么？3D 拆给你看｜全英文`
- 封面：爆炸视图截图 + Alx 的脸 + 大字 "WHY AI NEEDS THIS"，箭头指向 GPU
- 为什么不用"Why Is Nvidia Worth Trillions?"：整期 7 成内容在讲各个部件，标题许诺英伟达会让观众失望（满意度低）。用"in 3D"做差异（outlier 理论：借题，加自己的角度），AI 放括号里当钩子。
- 平台：YouTube 为主阵地（老胡"先专注一个平台"），其他平台只同步。
