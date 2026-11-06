# 🎬 《小天气》总导演级生产宪法与防偷懒刚性铁律 (DIRECTOR_CONSTITUTION)

> **生效日期**：2026-11-06 起永久生效  
> **适用对象**：任何进入本项目进行动画创作、提示词编写、分镜渲染与质检的 AI 智能体（包括未来所有会话与新实例）  
> **核心宗旨**：**坚决杜绝“脚本提交者”思维，全员以“大导演”的空间意识与视听美学执导每一镜！物理级消灭“念提示词”与“硬画字幕”！**

---

## 🚫 绝对不可逾越的三大死罪（违反者立即代码熔断）

1. **死罪一：机拼中文进提示词**
   - 严禁将中文台本、动作大纲直接复制或粗暴拼接到 `detailed_description` 或 `summary` 中！
   - 所有视觉动作、摄影焦段、光影动力学必须 **100% 逐字转译为专业英文 3D 动画导演指令**！
   - `detailed_description` 只要检测到任何一个中文字符，代码立即 Crash 拦截！

2. **死罪二：缺少画面无字锁**
   - 每镜 `detailed_description` 结尾必须强制焊死：  
     `[CLEAN SCREEN LOCK]: Strictly NO subtitles, NO captions, NO watermark, NO Chinese characters, NO on-screen text overlay! Clean cinematic frame.`  
     缺少此锁，严禁提交 ComfyUI 队列！

3. **死罪三：拟音误作念白 / 吉祥物说人话**
   - 严禁把拟音词（如“滴”、“呼”、“笃笃”、“咕”）套上 `<d>[Chinese]` 标签！
   - 吉祥物可可（以及大橘猫等动物）**绝对禁止说人话**！所有发音全部归入英文物理 ASMR 音景；
   - 只有人类角色（阿宁、妈妈、爸爸等）在剧本中确有对白时，才允许单句挂载 `<d>[Chinese] 真实台词 </d>`。

---

## 📐 前后镜头【极度连贯】的导演级三维物理空间法则

1. **阿宁卧室 3D 舞台固定不变**：
   - 画面左侧 (Screen-Left)：大书桌、暖黄台灯、可可的皇家蓝铁皮盒、北向大窗户与薄纱窗帘；
   - 画面右侧 (Screen-Right)：进门木门、门口原木色圆面矮凳（加湿器固定安放处）；
   - 中央地面：实木地板、柔和室内散射光。
   - 摄影机必须架设在 180 度动作轴线的一侧，绝不允许跳轴导致窗户和门颠倒！

2. **前后镜动势连贯（Cutting on Action）**：
   - 相邻镜头必须遵循动作因果链与动量守恒，前一镜动作终点即后一镜起点；
   - 在提示词中显式写入 `[CONTINUITY ANCHOR FROM PREVIOUS SHOT]` 约束焦段承接与角色走位；
   - 提取前镜尾帧（End Frame）作为后镜的首帧关键参考，实现 0 帧跳跃无缝衔接。

3. **核心道具母图唯一绑定**：
   - 每集的关键核心道具（如加湿器、红铜喷壶、冰棍箱）必须有固定的设计基准，全集 20 镜必须保持 100% 同一物理模型，绝不自发突变！

---

## 🔒 自动化机械看门狗 (Mechanical Enforcer)

所有分镜渲染脚本在提交渲染前，必须强制调用：
```python
from h3_perfect_continuity_pipeline import validate_prompt_rigorously
validate_prompt_rigorously(prompt_text, shot_meta)
```
任何未通过上述检查的提示词，直接抛出 `PromptSafetyError` 强行终止，物理级剥夺粗制滥造的运行权限！
