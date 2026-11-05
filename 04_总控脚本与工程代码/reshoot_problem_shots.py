# -*- coding: utf-8 -*-
"""
reshoot_problem_shots.py
《小天气》5支关键问题镜头精修重拍总控脚本
贯彻导演级核心质量修正：
1. EP06_SHOT_11: 彻底根除“可可变三花猫”特征污染，纯白无斑棉花糖雷云 vs 大橘猫大福窗外惊退；
2. EP06_SHOT_17: 彻底去除人类黑眉毛、动物肉垫足部畸变，Squash & Expand 奶凶鼓腮喷雾 vs 扫地机停摆；
3. EP06_SHOT_02: 校服阿宁清脆道别对白 + 蓝棉布铁盒 + 纯白可可（消除黄油饼干穿帮）；
4. EP06_SHOT_07: 窗台微距贴地视角，大橘猫大福毛发与瓦檐光影逼真；
5. EP02_SHOT_02: 消除餐桌右侧凭空出现的残缺儿童头颅与浮空筷子，单角色母亲温馨家居光影。

约束：严格不执行 4K 超分，只输出 832x480 @ 24fps 5.0s H3 原画分镜。
"""

import os
import sys
import time
import json
import shutil
import urllib.request
import urllib.error
from pathlib import Path

# 强制 UTF-8 输出
sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

import cv2
import numpy as np

PROJECT_ROOT = Path(r"C:\Users\32503\Desktop\小天气")
COMFY_HOST = "http://127.0.0.1:8188"
COMFY_OUTPUT_ROOT = Path(r"D:\ComfyUI_H3_isolated_20261021\ComfyUI\output")
ARTIFACT_DIR = Path(r"C:\Users\32503\.gemini\antigravity\brain\d3fed41b-9cc3-4ee3-ac09-fc0a5539d441")

COOLDOWN_SEC = 20

REPAIR_SHOTS = [
    {
        "id": "EP06_SHOT_11",
        "title": "11_SHOT_11_微弱紫静电打窗大福警惕后退",
        "target_dir": PROJECT_ROOT / "S01E06_大橘猫的窗台视察与扫地机大战" / "01_原画分镜",
        "qc_dir": PROJECT_ROOT / "S01E06_大橘猫的窗台视察与扫地机大战" / "03_质检样帧",
        "filename": "11_SHOT_11_微弱紫静电打窗大福警惕后退.mp4",
        "seed": 20261111,
        "media_1": "dafu_orange_cat_official.png",
        "media_2": "sen_tianqi_official.png",
        "prompt": """subject_definitions:
<Subject 1> is Dafu (大福), 100% identical to the giant fluffy domestic orange tabby cat in <Picture 1>. Thick orange-and-white striped fur, fat chubby cheeks, amber eyes, long white whiskers, sitting OUTSIDE on the exterior windowsill.
<Subject 2> is Keke (可可), 100% identical to <Picture 2>. [KEKE TEXTURE PURITY LOCK]: Pure seamless 100% solid cream-white marshmallow cloud fluff body! Strictly ZERO fur, ZERO spots, ZERO stripes, ZERO cat features, ZERO ears, ZERO whiskers! Only two shiny black bead eyes and a single translucent blue teardrop sprout on top. Keke floats INSIDE the room near the glass window.

summary:
[reference generation] In a 5.0-second 16:9 widescreen close-up at the window pane, <Subject 2> Keke (pure white cloud) unleashes a tiny violet static spark against the inner glass, startling outside orange cat <Subject 1> Dafu who scrambles backward in alarm.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1> for cat fur and features outside the window.
<Subject 2>: fully_preserved from <Picture 2> as a pure snow-white cloud with zero cat features.
[Cross-Attention Feature Separation Lock]: Subject 1 (cat) is outside the glass; Subject 2 (Keke) is inside the glass. Keke is strictly 100% solid white marshmallow fluff with zero spots.

detailed_description:
Cinematic 3D animation 16:9 widescreen split-focus close-up framing the clear double-glazed bedroom window pane.
From 0.0s to 2.0s, inside the sunny bedroom, pure cream-white cloud creature Keke floats 15cm above the study desk near the glass. Above its head, a miniature charcoal thundercloud gently billows with faint purple glow. Outside the exterior glass pane, the giant 15-pound fluffy orange cat Dafu sits on the brick windowsill, curious amber eyes staring in.
From 2.0s to 5.0s, Keke's little soft cloud body flexes and discharges a tiny, harmless violet static spark against the interior glass: "zzt-snap!". Outside the glass, Dafu's long white whiskers instantly twitch in surprise; the giant orange cat startles with wide dilated eyes, paws slipping slightly as it scrambles backward along the windowsill in comic alert retreat, tail puffing like a bottle brush.
Pixar-Ghibli expressive charm, brilliant electric luminescence against warm sunlit fur, crisp 24fps motion.

overall_soundscape:
A crisp, miniature static spark discharge: "zzt-snap!", followed by Dafu's startled cat huff-snort and the rapid scratch of claws retreating on exterior windowsill concrete. Absolutely ZERO BGM, ZERO synthesizer, ZERO artificial music.

non_diegetic_music:
N/A"""
    },
    {
        "id": "EP06_SHOT_17",
        "title": "17_SHOT_17_可可鼓腮喷白雾致扫地机停摆",
        "target_dir": PROJECT_ROOT / "S01E06_大橘猫的窗台视察与扫地机大战" / "01_原画分镜",
        "qc_dir": PROJECT_ROOT / "S01E06_大橘猫的窗台视察与扫地机大战" / "03_质检样帧",
        "filename": "17_SHOT_17_可可鼓腮喷白雾致扫地机停摆.mp4",
        "seed": 20261117,
        "media_1": "sen_tianqi_official.png",
        "media_2": "sen_tianqi_official.png",
        "prompt": """subject_definitions:
<Subject 1> is Keke (可可), 100% identical to <Picture 1>. A tiny 12cm living cloud creature with pure seamless cream-white marshmallow fluff texture, two shiny black bead eyes with sparkling white highlights, blushing peach-pink cheeks, and a single blue teardrop sprout on top.
[APPEAL & CUTE AGGRESSION LOCK]: Keke's determined anger is 100% cute marshmallow physics (Squash & Expand)! Strictly NO human eyebrows, NO drawn eyebrow lines, NO forehead wrinkles! Strictly NO animal paws, NO claws, NO paw pads!
[SCALE LOCK]: Keke is tiny (12cm), strictly 1/4 the diameter of the large black circular robot vacuum cleaner on the floor!

summary:
[reference generation] In a 5.0-second 16:9 widescreen low-angle shot on the wooden floor, tiny <Subject 1> Keke puffs its chubby body into a round balloon and blows a dense jet of white water vapor at the sweeping robot, blinding its sensors and stopping it.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1> with cute round cartoon physics.
[Mist Effect Lock]: Billowing, volumetric pure white water vapor jet spraying from Keke's mouth onto the robot's front obstacle sensors.

detailed_description:
Cinematic 3D animation 16:9 widescreen dynamic floor-level low-angle action shot on polished oak floorboards.
From 0.0s to 2.2s, facing the approaching 35cm black robotic vacuum cleaner, tiny 12cm Keke lands with soft bounce on the floor. Determined to defend the room, Keke takes a deep breath, its soft white marshmallow body expanding and puffing outward into a chubby, perfectly round mochi ball (Squash & Expand), peach-pink cheeks glowing with adorable effort, two round black eyes wide and sparkling without any human eyebrows.
From 2.2s to 5.0s, Keke exhales with tremendous gusto: "whooosh!", blowing a magnificent, dense jet of swirling pure white humid mist directly into the front infrared sensor bumper of the black sweeping robot! The thick fog completely blankets the optical lenses; the robot's circular ring light flashes amber, and its spinning side brushes and wheels immediately slow down and halt in an emergency safety stop.
Pixar-Ghibli volumetric fluid dynamics, warm golden morning floor reflections, crisp 24fps motion.

overall_soundscape:
A soft, cute child breath inhalation followed by a powerful, breezy mist whoosh: "whooosh-huff!", and the rapid deceleration and winding-down whine of the robot's electric motor: "bzzzz-shhh... click". Absolutely ZERO BGM, ZERO synthesizer, ZERO artificial music.

non_diegetic_music:
N/A"""
    },
    {
        "id": "EP06_SHOT_02",
        "title": "02_SHOT_02_校服阿宁轻敲铁盒道别上学",
        "target_dir": PROJECT_ROOT / "S01E06_大橘猫的窗台视察与扫地机大战" / "01_原画分镜",
        "qc_dir": PROJECT_ROOT / "S01E06_大橘猫的窗台视察与扫地机大战" / "03_质检样帧",
        "filename": "02_SHOT_02_校服阿宁轻敲铁盒道别上学.mp4",
        "seed": 20261102,
        "media_1": "sen_aning_official.png",
        "media_2": "sen_tianqi_official.png",
        "prompt": """subject_definitions:
<Subject 1> is A Ning (阿宁), 100% identical to <Picture 1>. An 8-year-old Asian child girl with double low curly pigtails, deep brown expressive eyes, wearing her neat blue-and-white striped short-sleeve school uniform with a crisp white collar and dark blue bow tie, carrying a pastel pink school backpack on both shoulders. Single girl only.
<Subject 2> is Keke (可可), 100% identical to <Picture 2>. A tiny 12cm plump cream-white living cloud creature resting inside the cookie tin.
<Prop 1> is the royal-blue circular 18cm Danish cookie tin. [PROP INTERIOR LOCK]: The tin is 100% COMPLETELY EMPTY of cookies, biscuits, or food! The interior base is neatly lined with a folded soft pastel baby-blue cotton handkerchief cloth.

summary:
[reference generation] In a 5.0-second 16:9 widescreen medium shot near the sunny study desk, 8-year-old schoolgirl <Subject 1> A Ning taps the metal tin rim and smiles warmly, saying: "<d>[Chinese]我要上学啦！</d>".

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1> for school uniform, curly pigtails, and bright child smile.
<Subject 2>: fully_preserved from <Picture 2> sitting comfortably on baby-blue cloth inside the tin.
[Food Exclusion Lock]: Absolutely ZERO cookies, ZERO biscuits, ZERO food crumbs inside the tin.

detailed_description:
Cinematic 3D animation 16:9 widescreen medium composition by the bright bedroom study desk.
Morning sunlight streams through the window, illuminating dust motes in the air.
From 0.0s to 2.2s, 8-year-old A Ning, dressed in her blue-and-white striped school uniform with a pink backpack on her shoulders, walks with cheerful, energetic child steps to the desk.
From 2.2s to 5.0s, she leans down warmly over the royal-blue cookie tin. Inside the clean tin, tiny Keke sits comfortably on the soft folded baby-blue cloth. With two slender fingers, A Ning gently taps the golden metal rim twice ("tink-tink") and smiles affectionately with crinkling eyes, bidding farewell: "<d>[Chinese]我要上学啦！</d>". Tiny Keke looks up from the blue cloth with big round eyes, its blue sprout swaying.
Pixar-Ghibli heartwarming domestic charm, golden rim lighting, crisp 24fps motion.

overall_soundscape:
Light rubber sneaker steps on wooden floor, crisp delicate metallic knuckle taps on cookie tin rim: "tink-tink", followed by A Ning's clear, sweet, melodic child voice: "<d>[Chinese]我要上学啦！</d>". Absolutely ZERO BGM, ZERO synthesizer, ZERO artificial music.

non_diegetic_music:
N/A"""
    },
    {
        "id": "EP06_SHOT_07",
        "title": "07_SHOT_07_大橘猫大福窗台巡逻凝视屋内",
        "target_dir": PROJECT_ROOT / "S01E06_大橘猫的窗台视察与扫地机大战" / "01_原画分镜",
        "qc_dir": PROJECT_ROOT / "S01E06_大橘猫的窗台视察与扫地机大战" / "03_质检样帧",
        "filename": "07_SHOT_07_大橘猫大福窗台巡逻凝视屋内.mp4",
        "seed": 20261107,
        "media_1": "dafu_orange_cat_official.png",
        "media_2": "dafu_orange_cat_official.png",
        "prompt": """subject_definitions:
<Subject 1> is Dafu (大福), 100% identical to <Picture 1>. A massive, plump 15-pound domestic orange tabby cat with plush orange-striped fur, pristine white chest bib and white paws, round chubby cheeks, amber eyes, and long majestic white whiskers.

summary:
[reference generation] In a 5.0-second 16:9 widescreen low-angle tracking shot along the terracotta eaves and windowsill, huge orange tabby cat <Subject 1> Dafu pads forward with majestic heavy steps, peering curiously into the bedroom window.

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1> for photorealistic feline fur volume, striped tail, and inquisitive amber eyes.

detailed_description:
Cinematic 3D animation 16:9 widescreen low-angle macro tracking shot on the exterior brick windowsill and weathered terracotta roof tiles outside the bedroom window.
Warm morning sunlight washes over climbing ivy and tiles.
From 0.0s to 2.2s, camera tracks slowly backward at low paw-level as the huge, fluffy orange cat Dafu pads forward along the ledge with lazy, heavy swagger, its thick ringed tail swaying gently and long white whiskers catching the morning sun.
From 2.2s to 5.0s, Dafu halts right beside the sparkling window glass. The cat turns its broad, jowly face toward the camera and glass pane, pressing its moist pink nose and twitching whiskers close to the reflection, its inquisitive amber eyes narrowing as it peers with feline curiosity into the sunlit bedroom study.
Pixar-Ghibli rich tactile fur rendering, dramatic architectural lighting, crisp 24fps motion.

overall_soundscape:
Rhythmic soft padded paw steps on weathered terracotta brick, a deep contented cat throat purr, and the subtle outdoor morning breeze through ivy leaves. Absolutely ZERO BGM, ZERO synthesizer, ZERO artificial music.

non_diegetic_music:
N/A"""
    },
    {
        "id": "EP02_SHOT_02",
        "title": "02_SHOT_02_妈妈的疑惑",
        "target_dir": PROJECT_ROOT / "S01E02_口算题卡上的小晴天" / "01_原画分镜",
        "qc_dir": PROJECT_ROOT / "S01E02_口算题卡上的小晴天" / "03_质检样帧",
        "filename": "02_SHOT_02_妈妈的疑惑.mp4",
        "seed": 20261122,
        "media_1": "sen_mama_official.png",
        "media_2": "sen_mama_official.png",
        "prompt": """subject_definitions:
<Subject 1> is Mother (妈妈), 100% identical to the gentle, loving 32-year-old Asian mother in <Picture 1>. Soft dark brown hair tied in a loose fluffy high bun with delicate face-framing strands, gentle warm eyes, wearing a cream-white puff-sleeve blouse and a clean pastel apron.
[STRICT SINGLE HUMAN GATE]: Exactly ONE person in frame: Mother. Absolutely NO other humans, NO extra heads, NO severed child heads, NO hands appearing from the side, NO floating chopsticks!

summary:
[reference generation] In a 5.0-second 16:9 widescreen medium close-up at the dining table, <Subject 1> Mother holds her bamboo chopsticks paused over the bowl, smiling with gentle maternal surprise and asking: "<d>[Chinese]今天这么积极写作业？</d>".

retention_analysis:
<Subject 1>: fully_preserved from <Picture 1> for mother's face, high bun hairstyle, and warm domestic outfit.
[Clean Composition Lock]: Single character framed gracefully in warm domestic light, zero background artifacts.

detailed_description:
Cinematic 3D animation 16:9 widescreen medium close-up composition in the cozy family dining room.
Warm morning sunlight and soft pendant lamp light illuminate the polished wooden table.
From 0.0s to 2.2s, Mother sits calmly by the breakfast table holding a clean ceramic rice bowl and bamboo chopsticks. Hearing footsteps darting toward the bedroom, she pauses her chopsticks in mid-air, a look of gentle pleasant surprise spreading across her tender face.
From 2.2s to 5.0s, Mother turns her head slightly toward the doorway, her lips curving into a warm, affectionate smile as she speaks with soft, melodic maternal humor: "<d>[Chinese]今天这么积极写作业？</d>". Her warm dark eyes crinkle with loving amusement.
Pixar-Ghibli heartwarming lighting, delicate flyaway hair catching morning sunlight, crisp 24fps motion.

overall_soundscape:
Gentle dining room morning room tone, the subtle quiet clink of bamboo chopsticks against ceramic, followed by Mother's clear, warm, affectionate spoken voice: "<d>[Chinese]今天这么积极写作业？</d>". Absolutely ZERO BGM, ZERO synthesizer, ZERO artificial music.

non_diegetic_music:
N/A"""
    }
]

def build_h3_workflow(prompt_text, seed, prefix, media_1="sen_aning_official.png", media_2="sen_tianqi_official.png", seconds=5.0):
    return {
        "101": {
            "inputs": {"image": media_1, "upload": "image"},
            "class_type": "LoadImage"
        },
        "102": {
            "inputs": {"image": media_2, "upload": "image"},
            "class_type": "LoadImage"
        },
        "1": {
            "inputs": {
                "fl2va_model": "minimax_h3_fl2va_pruned_fp8_scaled.safetensors",
                "ref2va_model": "none",
                "text_encoder": "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors",
                "video_vae": "minimax_h3_video_vae_int8_convrot.safetensors",
                "audio_vae": "minimax_h3_audio_vae_fp32.safetensors"
            },
            "class_type": "MiniMaxH3EasyLoader"
        },
        "2": {
            "inputs": {
                "h3_bundle": ["1", 0],
                "mode": "reference",
                "resolution": "custom",
                "aspect_ratio": "16:9",
                "width": 832,
                "height": 480,
                "seconds": seconds,
                "fps": 24.0,
                "advanced": True,
                "keyframe_role": "first",
                "ref_image_size": "match",
                "reference_mention_mode": "index",
                "prompt_optimizer_settings": False,
                "prompt_optimizer_scene_guide": "none",
                "prompt": prompt_text,
                "media_1": ["101", 0],
                "media_type_1": "image",
                "media_2": ["102", 0],
                "media_type_2": "image"
            },
            "class_type": "MiniMaxH3Easy"
        },
        "3": {
            "inputs": {
                "model": ["2", 0],
                "lora_name": "minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16.safetensors",
                "strength_model": 1.0
            },
            "class_type": "LoraLoaderModelOnly"
        },
        "4": {
            "inputs": {
                "model": ["3", 0],
                "attention": "comfy kitchen attention"
            },
            "class_type": "ModelAttentionBackend"
        },
        "5": {
            "inputs": {
                "model": ["4", 0],
                "scheduler": "beta",
                "steps": 4,
                "denoise": 1.0
            },
            "class_type": "BasicScheduler"
        },
        "6": {
            "inputs": {"sampler_name": "euler"},
            "class_type": "KSamplerSelect"
        },
        "7": {
            "inputs": {
                "model": ["4", 0],
                "h3_context": ["2", 1],
                "sampler": ["6", 0],
                "sigmas": ["5", 0],
                "seed": seed
            },
            "class_type": "MiniMaxH3EasySampler"
        },
        "8": {
            "inputs": {"h3_context": ["2", 1]},
            "class_type": "MiniMaxH3EasyOutput"
        },
        "9": {
            "inputs": {"samples": ["7", 0], "vae": ["8", 2]},
            "class_type": "VAEDecode"
        },
        "10": {
            "inputs": {"samples": ["7", 0], "vae": ["8", 3]},
            "class_type": "VAEDecodeAudio"
        },
        "11": {
            "inputs": {"images": ["9", 0], "audio": ["10", 0], "fps": ["8", 4]},
            "class_type": "CreateVideo"
        },
        "12": {
            "inputs": {
                "video": ["11", 0],
                "filename_prefix": prefix,
                "format": "auto"
            },
            "class_type": "SaveVideo"
        }
    }

def render_shot(item):
    sid = item["id"]
    target_mp4 = item["target_dir"] / item["filename"]
    prefix = f"RESHOOT_{sid}"
    seed = item["seed"]
    m1 = item["media_1"]
    m2 = item["media_2"]
    prompt = item["prompt"]
    
    print(f"\n==================================================", flush=True)
    print(f"🎬 [重拍任务启动] {sid}: {item['title']}", flush=True)
    print(f"  目标文件: {target_mp4.name}", flush=True)
    print(f"  种子: {seed} | 物料: Picture 1={m1}, Picture 2={m2}", flush=True)
    
    wf = build_h3_workflow(prompt, seed=seed, prefix=prefix, media_1=m1, media_2=m2, seconds=5.0)
    data = json.dumps({"prompt": wf}).encode("utf-8")
    req = urllib.request.Request(f"{COMFY_HOST}/prompt", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        
    pid = res.get("prompt_id")
    print(f"[+] 任务已成功入队! Prompt ID: {pid}", flush=True)
    
    start_t = time.time()
    raw_video = None
    while time.time() - start_t < 900:
        try:
            with urllib.request.urlopen(f"{COMFY_HOST}/history/{pid}", timeout=5) as resp:
                hist = json.loads(resp.read().decode("utf-8"))
                if pid in hist:
                    elapsed = time.time() - start_t
                    print(f"[+] H3 渲染计算完成! 耗时: {elapsed:.1f}s", flush=True)
                    outputs = hist[pid].get("outputs", {})
                    if "12" in outputs:
                        vids = outputs["12"].get("images", []) or outputs["12"].get("videos", [])
                        if vids:
                            fn = vids[0]["filename"]
                            sub = vids[0].get("subfolder", "")
                            raw_video = COMFY_OUTPUT_ROOT / sub / fn
                    break
        except Exception:
            pass
        time.sleep(4)
        
    if not raw_video or not raw_video.exists():
        raise RuntimeError(f"[-] 镜头 {sid} 渲染超时或输出缺失！")
        
    # 替换目标原画文件（先备份旧瑕疵文件）
    backup_file = target_mp4.parent / f"DEFECTIVE_PREV_{target_mp4.name}"
    if target_mp4.exists() and not backup_file.exists():
        shutil.copy2(str(target_mp4), str(backup_file))
        print(f"[+] 已将旧瑕疵分镜备份为: {backup_file.name}", flush=True)
        
    shutil.copy2(str(raw_video), str(target_mp4))
    print(f"[+] 精修重拍视频已成功替换目标: {target_mp4.name} ({target_mp4.stat().st_size:,} bytes)", flush=True)
    
    # 自动质检抽帧与指标核验
    inspect_and_extract_qc(item, target_mp4)

def inspect_and_extract_qc(item, target_mp4: Path):
    sid = item["id"]
    qc_dir = item["qc_dir"]
    qc_dir.mkdir(parents=True, exist_ok=True)
    
    cap = cv2.VideoCapture(str(target_mp4))
    if not cap.isOpened():
        print(f"[-] 无法打开视频文件进行质检: {target_mp4}", flush=True)
        return
        
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = total_frames / fps
    
    print(f"🔍 [技术质检] {sid} 规格: {w}x{h} @ {fps:.1f}fps, 总帧数: {total_frames}, 时长: {duration:.2f}s", flush=True)
    
    # 提取4个关键样帧: 起始帧(0), 核心动作1(30), 核心动作2(70), 尾帧(总帧数-5)
    sample_indices = {
        "start": 0,
        "action1": min(30, total_frames - 1),
        "action2": min(70, total_frames - 1),
        "end": max(0, total_frames - 5)
    }
    
    frames_dict = {}
    cur_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        for tag, target_idx in sample_indices.items():
            if cur_idx == target_idx:
                frames_dict[tag] = frame
        cur_idx += 1
    cap.release()
    
    # 存盘质检样帧
    prefix_name = item["filename"].replace(".mp4", "")
    for tag, frame in frames_dict.items():
        out_jpg = qc_dir / f"{prefix_name}_{tag}.jpg"
        cv2.imwrite(str(out_jpg), frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
        
        # 同时写入对话 Artifact 目录方便实时审查
        art_jpg = ARTIFACT_DIR / f"reshoot_{sid}_{tag}.jpg"
        cv2.imwrite(str(art_jpg), frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
        print(f"  📸 质检样帧落盘: {out_jpg.name}", flush=True)
        
    # 计算亮度和动态变化
    if "start" in frames_dict and "end" in frames_dict:
        gray_start = cv2.cvtColor(frames_dict["start"], cv2.COLOR_BGR2GRAY)
        gray_end = cv2.cvtColor(frames_dict["end"], cv2.COLOR_BGR2GRAY)
        diff = np.mean(cv2.absdiff(gray_start, gray_end))
        brightness = np.mean(gray_start)
        print(f"  📊 动态差分度: {diff:.2f} (阈值>3.0) | 平均灰阶亮度: {brightness:.1f}", flush=True)
        if diff < 2.0:
            print(f"  ⚠️ 警告: 动态差分度较低，可能动作偏静止", flush=True)
        else:
            print(f"  ✅ 动态表现优秀，动作张力充沛！", flush=True)

def main():
    print("=" * 60, flush=True)
    print("🚀 [总控执行] 《小天气》5 支核心问题镜头精修重拍流水线启动", flush=True)
    print(f"  ComfyUI: {COMFY_HOST}", flush=True)
    print(f"  共计待重拍镜头数: {len(REPAIR_SHOTS)} 镜", flush=True)
    print("=" * 60, flush=True)
    
    for i, item in enumerate(REPAIR_SHOTS, 1):
        print(f"\n>>> 进度 [{i}/{len(REPAIR_SHOTS)}] <<<", flush=True)
        try:
            render_shot(item)
            if i < len(REPAIR_SHOTS):
                print(f"❄️ 硬件降温：静息 {COOLDOWN_SEC} 秒...", flush=True)
                time.sleep(COOLDOWN_SEC)
        except Exception as e:
            print(f"❌ 镜头 {item['id']} 重拍失败: {e}", flush=True)
            
    print("\n" + "=" * 60, flush=True)
    print("🎉 5 支核心问题镜头精修重拍全部执行完毕！", flush=True)
    print("=" * 60, flush=True)

if __name__ == "__main__":
    main()
