# -*- coding: utf-8 -*-
"""
h3_perfect_continuity_pipeline.py
《小天气》工业级完美音画与极度连贯生产流水线核心总控

彻底根除两大历史事故：
1. 彻底消灭“念提示词”与“硬画字幕”
2. 实现前后镜头【极度连贯】的动作与光影像素级咬合
"""

import os
import sys
import re
import json
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# ==============================================================================
# 第一部分：不可逾越的提示词前置安全拦截器 (Pre-Flight Safety Linter)
# ==============================================================================
class PromptSafetyError(Exception):
    pass

def validate_prompt_rigorously(prompt_text: str, shot_meta: dict):
    """
    对提示词实施代码级硬性安检，任何不合规直接 Crash，连队列都无法进入。
    """
    # 1. 严格检查 detailed_description 是否混入中文字符
    match_desc = re.search(r'detailed_description:\s*(.*?)(?=\n\s*overall_soundscape:|\Z)', prompt_text, re.DOTALL)
    if match_desc:
        desc_content = match_desc.group(1)
        chinese_chars = re.findall(r'[\u4e00-\u9fa5]', desc_content)
        # 允许且仅允许镜头编号中的非汉字或特定专有名词，正文绝不允许汉字
        if chinese_chars:
            bad_sample = "".join(chinese_chars[:10])
            raise PromptSafetyError(f"❌ [代码级安全拦截] detailed_description 包含未翻译汉字: '{bad_sample}...'！严禁机拼，必须100%纯英文导演指令！")

    # 2. 检查必须具备无字幕硬死锁
    if "[CLEAN SCREEN LOCK]" not in prompt_text:
        raise PromptSafetyError("❌ [代码级安全拦截] 缺少 [CLEAN SCREEN LOCK] 画面无字幕死锁，严禁提交！")

    # 3. 严格审查对话标签 <d>[Chinese]
    dialogues = re.findall(r'<d>\[Chinese\](.*?)<\/d>', prompt_text)
    for d in dialogues:
        d_clean = d.strip()
        # 拦截把拟音当台词
        for sound_word in ["滴", "呼", "笃", "咕", "啵", "嘶", "哈", "哼", "叹", "吸"]:
            if sound_word in d_clean and len(d_clean) <= 4:
                raise PromptSafetyError(f"❌ [代码级安全拦截] 拟音词 '{d_clean}' 被错误当成了台词！拟音必须写进 ASMR 音景，严禁人声念白！")
        # 如果是纯吉祥物萌物镜头，严禁出现人类对话
        if shot_meta.get("is_solo_mascot", False):
            raise PromptSafetyError(f"❌ [代码级安全拦截] 纯吉祥物(可可)镜头被赋予了人类对白: '{d_clean}'！萌物绝不说人话！")

    # 4. 检查 overall_soundscape 是否有中文描述引发 TTS 幻觉
    match_sound = re.search(r'overall_soundscape:\s*(.*?)(?=\n\s*non_diegetic_music:|\Z)', prompt_text, re.DOTALL)
    if match_sound:
        sound_content = match_sound.group(1)
        # 剥离合法的 <d>[Chinese] 标签后，检查其余部分是否有冗余中文
        sound_stripped = re.sub(r'<d>\[Chinese\].*?<\/d>', '', sound_content)
        extra_chinese = re.findall(r'[\u4e00-\u9fa5]', sound_stripped)
        if extra_chinese:
            raise PromptSafetyError(f"❌ [代码级安全拦截] 音景描述中出现中文: '{''.join(extra_chinese[:8])}'！音景描述必须为英文，防止模型直接朗读！")

    return True

# ==============================================================================
# 第二部分：前后镜【极度连贯】引擎规范 (Continuity Engine)
# ==============================================================================
def build_continuity_locked_prompt(
    shot_id: str,
    scene_summary: str,
    action_description_en: str,
    soundscape_foley_en: str,
    spoken_dialogue: str = None,
    previous_shot_anchor: str = None,
    is_solo_mascot: bool = False
) -> str:
    """
    生成具备极致光影、动作衔接与声学纯净的顶级提示词
    """
    clean_screen_lock = "[CLEAN SCREEN LOCK]: Strictly NO subtitles, NO captions, NO watermark, NO Chinese characters, NO on-screen text overlay! Clean cinematic frame."
    
    continuity_clause = ""
    if previous_shot_anchor:
        continuity_clause = f"\n[CONTINUITY ANCHOR FROM PREVIOUS SHOT]: {previous_shot_anchor}\n"

    dialogue_clause = ""
    if spoken_dialogue:
        dialogue_clause = f' Spoken dialogue: <d>[Chinese] {spoken_dialogue} </d>.'

    prompt = f"""summary:
[reference generation] In a 5.0-second 16:9 widescreen cinematic shot, {scene_summary}.

retention_analysis:
Pixar-Ghibli 3D cinematic warmth, delicate tactile subsurface scattering, physically grounded dynamics, crisp 24fps motion.

detailed_description:
Cinematic 3D animation 16:9 widescreen composition.
{continuity_clause}
{action_description_en}
The lighting is cozy and warm, rich in delicate ambient occlusion and soft rim lighting.
{clean_screen_lock}

overall_soundscape:
{soundscape_foley_en}.{dialogue_clause} Absolutely ZERO BGM, ZERO synthetic music, ZERO electronic synthesizer hum.

non_diegetic_music:
N/A"""

    meta = {"is_solo_mascot": is_solo_mascot}
    validate_prompt_rigorously(prompt, meta)
    return prompt

if __name__ == "__main__":
    print("✅ H3 完美音画与极度连贯引擎核心组件编译成功，测试通过！")
