# 🌦️ 《小天气》（Little Weather）AI 动画剧集生产知识库与资产配置基准库

[![GitHub Repository](https://img.shields.io/badge/GitHub-little--weather--production--vault-blue?logo=github)](https://github.com/qianqianxiaoxianxain/little-weather-production-vault)
[![License: MIT](https://img.shields.io/badge/License-Proprietary-orange.svg)](#)
[![Resolution: 4K UHD](https://img.shields.io/badge/Resolution-3840x2160%204K-emerald)](#)
[![Framerate: 24fps](https://img.shields.io/badge/Framerate-24.0%20fps-cyan)](#)
[![Hardware: RTX 5060](https://img.shields.io/badge/Hardware-RTX%205060%208GB-green)](#)

> 本知识库是面向原创治愈系 3D AI 动画剧集《小天气》（第一卷：晴转多云的铁皮盒）的**工业级生产总纲、核心资产配置字典、深度翻车排错复盘与自动化控制工程库**。  
> 旨在彻底消灭 AI 动画生产中常见的“角色基因突变”、“电音口齿含糊”、“体型橡皮筋漂移”、“动作呆板不萌”、“运镜三脚架监控感”、“形式主义假自检”六大灾难性顽疾，沉淀永久有效的工程与艺术基准。

---

## 📂 知识库架构目录导航

```
little-weather-production-vault/
├── 01_核心教训与翻车深度复盘/
│   └── 01_CORE_LESSONS_LEARNED.md      # 鲜血换来的 7 大核心致命翻车深度复盘白皮书
├── 02_工业级生产规范总纲/
│   └── 02_PRODUCTION_PIPELINE_STANDARDS.md # 3D温润质感/可可六大锁/双轨声学母带/动感运镜总纲
├── 03_提示词字典与资产配置/
│   ├── prompts_ep01_little_weather.py   # EP01《晴转多云的铁皮盒》全 20 镜 Master 提示词字典
│   ├── prompts_ep02_little_weather.py   # EP02《口算题卡上的小晴天》全 20 镜 Master 提示词字典
│   ├── prompts_ep03_little_weather.py   # EP03《冰箱保鲜层的探险家》全 20 镜 Master 提示词字典
│   ├── prompts_ep04_little_weather.py   # EP04《滚筒里的水龙卷与茉莉花》全 20 镜 Master 提示词字典
│   ├── prompts_ep05_little_weather.py   # EP05《胡椒味的小雷嗝与留守契约》全 20 镜 Master 提示词字典
│   └── prompts_ep06_little_weather.py   # EP06《大橘猫的窗台视察与扫地机大战》全 20 镜 Master 提示词字典
├── 04_总控脚本与工程代码/
│   ├── run_ep06_full_production_and_qc.py # EP06 自动化单镜渲染、自素质检与 4K 超分调度脚本
│   ├── upscale_missing_5_shots.py       # RealESRGAN_x4plus + NVENC 4K 院线级超分引擎
│   └── audit_all_episodes.py            # 全 6 集 120 镜全量资产规格自动化验收审计工具
├── 05_交付质检报告与归档/
│   ├── EP02_EP06_MASTER_DELIVERY_REPORT.md # 第 1 至第 6 集 120 镜 4K 交付总账与技术报告
│   ├── ep06_raw_qc_report.json          # EP06 全部 20 镜自动化机器质检量化指标
│   └── spot_check_data.json             # 抽检关键帧与音轨流详细技术指标数据
└── README.md                            # 知识库主入口索引
```

---

## 🎬 第一卷前 6 集资产包全景总账

| 集数编号 | 剧集名称 | 原画分镜 (832×480) | 4K 超分分镜 (3840×2160) | 质检样帧 (t15/t30) | 机器通过率 | 状态 |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **S01E01** | 《晴转多云的铁皮盒》 | **20 / 20** | **20 / 20** | 82 张 | 100% | ✅ 交付 |
| **S01E02** | 《口算题卡上的小晴天》 | **20 / 20** | **20 / 20** | 80 张 | 100% | ✅ 交付 |
| **S01E03** | 《冰箱保鲜层的探险家》 | **20 / 20** | **20 / 20** | 80 张 | 100% | ✅ 交付 |
| **S01E04** | 《滚筒里的水龙卷与茉莉花》 | **20 / 20** | **20 / 20** | 80 张 | 100% | ✅ 交付 |
| **S01E05** | 《胡椒味的小雷嗝与留守契约》 | **20 / 20** | **20 / 20** | 80 张 | 100% | ✅ 交付 |
| **S01E06** | 《大橘猫的窗台视察与扫地机大战》 | **20 / 20** | **20 / 20** | 80 张 | 100% | ✅ 交付 |
| **总计** | **第一卷前 6 集全量资产** | **120 / 120** | **120 / 120** | **482 张** | **100.0%** | 🏆 满贯 |

---

## ⚡ 核心排错要点与六大铁律精要

详细复盘见 [`01_核心教训与翻车深度复盘/01_CORE_LESSONS_LEARNED.md`](01_核心教训与翻车深度复盘/01_CORE_LESSONS_LEARNED.md)：

1. **绝对禁止多参考图交叉污染**：在同框镜头中严禁混合大特征动物参考图与纯白云朵参考图，必须严格执行特征隔离与排他描述，严防可可长出猫斑猫耳；
2. **彻底摒弃神经音频直出**：全面推行**双轨母带分离合封架构**（纯净视频 + Demucs 分离原生拟音 + 独立纯正高保真 TTS/可可专属萌音 + 深度避让混音），消灭口齿含糊与 5200Hz 电音；
3. **锁定可可专属【咕啾~ (Gu-chiu~)】口癖**：严格规范撒娇、傲娇、受惊、奶凶四大变调体系，严禁模型随机生成怪叫；
4. **刚性环境参照物约束体型**：可可严格锁定为“8岁女孩合捧雪媚娘大小（坐高8cm/站高15cm）”、“铁盒坐高 1/2”、“扫地机体积 1/4”；
5. **赋予弹性动画魅力（Squash & Stretch）**：生气时吹成气球圆团小跳跺脚、受惊时果冻拉伸扁平滑入布褶，拒绝机械僵硬脸；
6. **动感运镜与动作匹配剪辑**：摒弃死板三脚架监控机位，采用贴地微距追踪、景深转移与动作匹配无缝转场；
7. **终结机器形式主义自检**：在技术参数检测基础上，强制实行语义层四点关键帧人眼核验门禁。
