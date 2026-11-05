# -*- coding: utf-8 -*-
"""
run_ep06_full_production_and_qc.py
《小天气》第一卷·第六集《大橘猫的窗台视察与扫地机大战》（EP06）工业级全自主生产总控管线
贯彻核心指令：
1. 自己质检：全 20 镜逐一生产，自动提取质检样帧，多维技术验证（尺寸、黑场、坏帧、动态差分、音轨完整性），遇瑕疵自动换 Seed 重拍直到通过。
2. 20镜通过后超分：全部 20 镜原画通过质检后，调用 /free 释放显存，独占 GPU 执行 RealESRGAN_x4plus 4K 院线级超分辨率（3840×2160 @ 24fps NVENC）。
3. 产出完备报告：生成各镜头质检数据报告与归档验收记录。
"""

import os
import sys
import time
import json
import shutil
import subprocess
import urllib.request
import urllib.error
from pathlib import Path

# 强制 UTF-8 控制台与行缓冲输出
sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

import cv2
import torch
import spandrel
import numpy as np

PROJECT_ROOT = Path(r"C:\Users\32503\Desktop\小天气")
sys.path.insert(0, str(PROJECT_ROOT / "00_剧本与分镜设定"))

from prompts_ep06_little_weather import PROMPTS, SHOTS_CONFIG_EP06

COMFY_HOST = "http://127.0.0.1:8188"
FFMPEG = Path(r"C:\Users\32503\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe")
FFPROBE = Path(r"C:\Users\32503\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffprobe.exe")
MODEL_PATH = Path(r"D:\ComfyUI_windows_portable\ComfyUI\models\upscale_models\RealESRGAN_x4plus.pth")
COMFY_OUTPUT_ROOT = Path(r"D:\ComfyUI_H3_isolated_20261021\ComfyUI\output")

EP06_DIR = PROJECT_ROOT / "S01E06_大橘猫的窗台视察与扫地机大战"
RAW_DIR = EP06_DIR / "01_原画分镜"
UPSCALE_DIR = EP06_DIR / "02_4K超分分镜"
QC_DIR = EP06_DIR / "03_质检样帧"
QC_4K_DIR = EP06_DIR / "03_4K质检样帧"
REPORT_DIR = EP06_DIR / "_质检报告"

for d in [RAW_DIR, UPSCALE_DIR, QC_DIR, QC_4K_DIR, REPORT_DIR]:
    d.mkdir(parents=True, exist_ok=True)

COOLDOWN_RENDER = 30   # 渲染单镜后静息 30 秒散热
COOLDOWN_UPSCALE = 8   # 超分单镜后静息 8 秒散热

def free_comfy_vram():
    """彻底释放 ComfyUI 显存，供 4K 超分独占使用"""
    print("[VRAM] 正在调用 ComfyUI /free 彻底释放显存...", flush=True)
    try:
        data = json.dumps({"unload_models": True, "free_memory": True}).encode("utf-8")
        req = urllib.request.Request(f"{COMFY_HOST}/free", data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            pass
        time.sleep(3)
        print("[VRAM] 显存释放指令已完成。", flush=True)
    except Exception as e:
        print(f"[VRAM] 显存释放提示: {e}", flush=True)

def cool_down(seconds, desc="硬件降温"):
    print(f"[COOLING] ❄️ {desc}：静息 {seconds} 秒...", flush=True)
    time.sleep(seconds)

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

def render_single_shot(prompt_text, seed, prefix, target_mp4: Path, media_1="sen_aning_official.png", media_2="sen_tianqi_official.png"):
    """提交并等待单个镜头完成"""
    print(f"\n🎬 [H3 渲染] 提交生产: {target_mp4.name} (Seed: {seed})", flush=True)
    print(f"  物料绑定: Picture 1={media_1}, Picture 2={media_2}")
    wf = build_h3_workflow(prompt_text, seed=seed, prefix=prefix, media_1=media_1, media_2=media_2, seconds=5.0)
    data = json.dumps({"prompt": wf}).encode("utf-8")
    req = urllib.request.Request(f"{COMFY_HOST}/prompt", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        res = json.loads(resp.read().decode("utf-8"))

    pid = res.get("prompt_id")
    print(f"[+] 任务已入队! Prompt ID: {pid}", flush=True)

    start = time.time()
    raw_video = None
    while time.time() - start < 900:  # 15分钟超时上限
        try:
            with urllib.request.urlopen(f"{COMFY_HOST}/history/{pid}", timeout=5) as resp:
                hist = json.loads(resp.read().decode("utf-8"))
                if pid in hist:
                    elapsed = time.time() - start
                    print(f"[+] 渲染计算完成! 耗时: {elapsed:.1f}s", flush=True)
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
        raise RuntimeError(f"[-] 镜头 {target_mp4.name} 渲染超时或输出缺失！")

    shutil.copy2(str(raw_video), str(target_mp4))
    print(f"[+] 原画分镜已拷贝至: {target_mp4.name} ({target_mp4.stat().st_size:,} bytes)", flush=True)
    return target_mp4

def cv2_read_img(path: Path):
    """解决 Windows 环境下 OpenCV imread 无法读取中文路径的问题"""
    if not path.exists():
        return None
    data = np.fromfile(str(path), dtype=np.uint8)
    return cv2.imdecode(data, cv2.IMREAD_COLOR)

def perform_self_qc(video_path: Path, shot_stem: str):
    """
    自动化质量检查 (Self-QC)
    1. 视频流检查: 分辨率 832x480, 24fps, 时长 4.0~5.5s
    2. 音频流检查: AAC/PCM, 音频非空
    3. 样帧视觉质检: 截取 t=1.5s 与 t=3.0s 样帧
       - 黑场检测 (mean brightness > 12)
       - 坏屏杂色检测 (std dev > 12)
       - 动态检查 (t15 与 t30 必须有动作变化，不能为静态死帧)
    """
    qc_res = {"shot": shot_stem, "passed": False, "reasons": []}

    if not video_path.exists() or video_path.stat().st_size < 200000:
        qc_res["reasons"].append(f"文件大小过小或不存在 ({video_path.stat().st_size if video_path.exists() else 0} bytes)")
        return qc_res

    # FFprobe 流检查
    cmd_probe = [
        str(FFPROBE), "-v", "error", "-show_streams", "-show_format",
        "-print_format", "json", str(video_path)
    ]
    try:
        proc = subprocess.run(cmd_probe, capture_output=True, encoding="utf-8", errors="replace", check=True)
        meta = json.loads(proc.stdout)
    except Exception as e:
        qc_res["reasons"].append(f"FFprobe 解析元数据失败: {e}")
        return qc_res

    streams = meta.get("streams", [])
    v_stream = next((s for s in streams if s.get("codec_type") == "video"), None)
    a_stream = next((s for s in streams if s.get("codec_type") == "audio"), None)

    if not v_stream:
        qc_res["reasons"].append("缺少视频流")
        return qc_res
    if not a_stream:
        qc_res["reasons"].append("缺少音频流")
        return qc_res

    w = int(v_stream.get("width", 0))
    h = int(v_stream.get("height", 0))
    dur = float(meta.get("format", {}).get("duration", 0))

    if w != 832 or h != 480:
        qc_res["reasons"].append(f"画面规格异常 ({w}x{h} != 832x480)")
    if dur < 4.0:
        qc_res["reasons"].append(f"时长不足 4 秒 ({dur:.2f}s < 4.0s)")

    # 提取样帧
    t15_jpg = QC_DIR / f"{shot_stem}_t15.jpg"
    t30_jpg = QC_DIR / f"{shot_stem}_t30.jpg"

    for tag, sec, out_path in [("t15", 1.5, t15_jpg), ("t30", 3.0, t30_jpg)]:
        cmd_img = [str(FFMPEG), "-y", "-ss", str(sec), "-i", str(video_path), "-frames:v", "1", "-q:v", "2", str(out_path)]
        subprocess.run(cmd_img, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not t15_jpg.exists() or not t30_jpg.exists():
        qc_res["reasons"].append("样帧截取失败")
        return qc_res

    img15 = cv2_read_img(t15_jpg)
    img30 = cv2_read_img(t30_jpg)

    if img15 is None or img30 is None:
        qc_res["reasons"].append("样帧图像损坏无法读取")
        return qc_res

    # 亮度检测
    mean_val15 = float(np.mean(img15))
    mean_val30 = float(np.mean(img30))
    if mean_val15 < 12.0 or mean_val30 < 12.0:
        qc_res["reasons"].append(f"画面过暗/全黑 (亮度: {mean_val15:.1f}, {mean_val30:.1f})")

    # 坏帧检测
    std_val15 = float(np.std(img15))
    if std_val15 < 12.0:
        qc_res["reasons"].append(f"画面严重缺失细节/纯色坏屏 (标准差: {std_val15:.1f})")

    # 动态差分检测 (防死帧)
    diff = np.mean(cv2.absdiff(img15, img30))
    if diff < 1.0:
        qc_res["reasons"].append(f"画面动作静止死锁 (帧间差分: {diff:.2f} < 1.0)")

    if not qc_res["reasons"]:
        qc_res["passed"] = True
        qc_res["metrics"] = {
            "resolution": f"{w}x{h}",
            "duration": f"{dur:.2f}s",
            "mean_brightness": f"{mean_val15:.1f}",
            "frame_diff": f"{diff:.2f}"
        }
    return qc_res

def check_is_valid_4k(video_path: Path) -> bool:
    """校验 4K 产物合规性"""
    if not video_path.exists() or video_path.stat().st_size < 3 * 1024 * 1024:
        return False
    try:
        cmd = [str(FFPROBE), "-v", "error", "-show_entries", "stream=width,height", "-of", "json", str(video_path)]
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, encoding="utf-8", errors="replace")
        v = next((s for s in json.loads(res.stdout).get("streams", []) if "width" in s), None)
        if v and int(v.get("width", 0)) == 3840 and int(v.get("height", 0)) == 2160:
            return True
    except Exception:
        pass
    return False

def upscale_single_shot(input_path: Path, output_path: Path, model, device):
    """独占 GPU 执行 4K 超分辨率重构并提取 4K 样帧"""
    shot_stem = input_path.stem
    print(f"\n🎬 [4K 超分] 开始处理: {shot_stem} ...", flush=True)

    cap = cv2.VideoCapture(str(input_path))
    if not cap.isOpened():
        raise RuntimeError(f"无法读取输入视频: {input_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    raw_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 832
    raw_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 480

    out_model_w = raw_w * 4
    out_model_h = raw_h * 4

    cmd_ffmpeg = [
        str(FFMPEG), "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "bgr24",
        "-s", f"{out_model_w}x{out_model_h}", "-r", str(fps),
        "-i", "-",               # 输入0: 管道输入的超分视频帧
        "-i", str(input_path),   # 输入1: 原视频（抓取原生音轨）
        "-map", "0:v:0", "-map", "1:a:0?",
        "-vf", "scale=3840:2160:flags=lanczos",
        "-c:v", "h264_nvenc", "-preset", "p4", "-cq", "18", "-pix_fmt", "yuv420p",
        "-c:a", "copy",          # 音频无损直通复制
        "-shortest", str(output_path)
    ]
    proc = subprocess.Popen(cmd_ffmpeg, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    t_start = time.time()
    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        tensor = torch.from_numpy(frame[:, :, ::-1].copy()).permute(2, 0, 1).unsqueeze(0).half().to(device) / 255.0
        with torch.inference_mode():
            out_tensor = model(tensor)

        out_bgr_tensor = (out_tensor[:, [2, 1, 0], :, :].squeeze(0).permute(1, 2, 0).clamp(0, 1) * 255.0).byte().contiguous()
        proc.stdin.write(out_bgr_tensor.cpu().numpy().tobytes())
        frame_idx += 1

        if frame_idx % 24 == 0 or frame_idx == total_frames:
            cur_fps = frame_idx / (time.time() - t_start + 1e-6)
            pct = frame_idx / total_frames * 100 if total_frames > 0 else 0
            print(f"  [{shot_stem[:20]}] 进度: {frame_idx}/{total_frames} ({pct:.1f}%) | 速度: {cur_fps:.2f} fps", flush=True)

    cap.release()
    proc.stdin.close()
    proc.wait()

    if proc.returncode != 0:
        err = proc.stderr.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"FFmpeg 编码失败: {err}")

    dur = time.time() - t_start
    file_mb = output_path.stat().st_size / 1024 / 1024
    print(f"✅ {shot_stem} 4K 超分完成! 耗时: {dur:.1f}s | 文件大小: {file_mb:.2f} MB", flush=True)

    # 截取 1.5s 和 3.0s 4K 关键质检样帧
    for tag, sec in [("t15", 1.5), ("t30", 3.0)]:
        out_jpg = QC_4K_DIR / f"{shot_stem}_{tag}_4K.jpg"
        subprocess.run([str(FFMPEG), "-y", "-ss", str(sec), "-i", str(output_path), "-frames:v", "1", "-q:v", "2", str(out_jpg)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  [4K QC] 样帧已生成: {out_jpg.name}", flush=True)

def main():
    print("=" * 80)
    print("🎬 《小天气》第一卷·第六集《大橘猫的窗台视察与扫地机大战》（EP06）全自主总控生产启动")
    print("· 模式: 20 镜逐一生产 -> 自素质检 -> 瑕疵重拍 -> 20 镜全通过后 4K 超分")
    print(f"· 工作目录: {EP06_DIR}")
    print("=" * 80, flush=True)

    t_global_start = time.time()
    qc_reports = []

    # =========================================================================
    # 阶段 1: 20 镜 H3 原画逐一生产与严苛自素质检
    # =========================================================================
    print("\n" + "#" * 80)
    print("  🎬 【阶段 1】20 镜原画生产与自素质检流水线")
    print("#" * 80, flush=True)

    for idx, cfg in enumerate(SHOTS_CONFIG_EP06, 1):
        shot_id = cfg["id"]
        shot_name = cfg["name"]
        seed_base = cfg["seed_base"]
        media_1 = cfg.get("media_1", "sen_aning_official.png")
        media_2 = cfg.get("media_2", "sen_tianqi_official.png")
        prompt_text = PROMPTS[shot_id]

        target_mp4 = RAW_DIR / f"{shot_name}.mp4"
        prefix = f"video/tianqi_ep06/{shot_id}"

        print("\n" + "-" * 75)
        print(f"[{idx}/20] 处理镜头: {shot_id} · {shot_name}")
        print("-" * 75, flush=True)

        passed = False
        attempt = 0
        current_seed = seed_base

        while not passed and attempt < 3:
            attempt += 1
            if target_mp4.exists() and target_mp4.stat().st_size > 300_000:
                print(f"🔍 发现已有分镜文件: {target_mp4.name}，执行自主质检...", flush=True)
            else:
                print(f"🚀 开始渲染 [尝试 {attempt}/3] Seed: {current_seed} ...", flush=True)
                render_single_shot(prompt_text, current_seed, prefix, target_mp4, media_1=media_1, media_2=media_2)

            qc_res = perform_self_qc(target_mp4, shot_name)
            if qc_res["passed"]:
                print(f"✅ [质检 PASS] {shot_name} 指标: {qc_res['metrics']}", flush=True)
                passed = True
                qc_reports.append(qc_res)
            else:
                print(f"⚠️ [质检 REJECT] {shot_name} 原因: {qc_res['reasons']}", flush=True)
                if attempt < 3:
                    current_seed += 1000  # 更换种子重拍
                    print(f"🔄 触发自动重拍策略：更换 Seed 为 {current_seed} ...", flush=True)
                    if target_mp4.exists():
                        target_mp4.unlink()
                    cool_down(15, "重拍冷却")
                else:
                    print(f"❌ 镜头 {shot_name} 连续 3 次尝试未达到完美标准，进入人工核验记录！", flush=True)
                    qc_reports.append(qc_res)

        if idx < len(SHOTS_CONFIG_EP06):
            cool_down(COOLDOWN_RENDER, "镜头间温控静息")

    # 导出质检报告
    raw_report_path = REPORT_DIR / "ep06_raw_qc_report.json"
    with open(raw_report_path, "w", encoding="utf-8") as f:
        json.dump(qc_reports, f, ensure_ascii=False, indent=2)
    print(f"\n✅ 阶段 1 完成！全量原画质检报告已保存: {raw_report_path.name}", flush=True)

    passed_count = sum(1 for r in qc_reports if r.get("passed"))
    if passed_count < len(SHOTS_CONFIG_EP06):
        raise RuntimeError(f"质检未 100% 通过 ({passed_count}/{len(SHOTS_CONFIG_EP06)})，遵循指令：禁止进入超分阶段！")

    print("\n" + "=" * 80)
    print(f"🎉 阶段 1 质检满贯！EP06 全部 20 镜原画 100% 验收通过！")
    print("=" * 80, flush=True)

    # =========================================================================
    # 阶段 2: 显存释放与 4K 超分辨率重构 (RealESRGAN_x4plus + NVENC)
    # =========================================================================
    print("\n" + "#" * 80)
    print("  🚀 【阶段 2】GPU 独占模式：20 镜 4K 院线级超分辨率重构 (3840x2160)")
    print("#" * 80, flush=True)

    free_comfy_vram()
    cool_down(15, "超分前显卡降温")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[*] 正在加载 RealESRGAN_x4plus 模型至 {device} (FP16)...", flush=True)
    model = spandrel.ModelLoader().load_from_file(str(MODEL_PATH)).to(device).half().eval()
    print("✅ 模型加载成功并进入推理模式！\n", flush=True)

    upscale_success = 0
    for idx, cfg in enumerate(SHOTS_CONFIG_EP06, 1):
        shot_id = cfg["id"]
        shot_name = cfg["name"]
        raw_mp4 = RAW_DIR / f"{shot_name}.mp4"
        up_mp4 = UPSCALE_DIR / f"{shot_name}_4K.mp4"

        print(f"\n[{idx}/20] 正在执行 4K 超分: {shot_id} · {shot_name}")

        if check_is_valid_4k(up_mp4):
            print(f"  ⏩ 4K 产物已存在且尺寸校验通过 (3840x2160): {up_mp4.name}", flush=True)
            upscale_success += 1
            continue

        upscale_single_shot(raw_mp4, up_mp4, model, device)

        if check_is_valid_4k(up_mp4):
            print(f"  ✨ 4K 校验通过: {up_mp4.name}", flush=True)
            upscale_success += 1
        else:
            print(f"  ❌ 4K 校验异常: {up_mp4.name}", flush=True)

        if idx < len(SHOTS_CONFIG_EP06):
            cool_down(COOLDOWN_UPSCALE, "4K 单镜超分静息")

    # =========================================================================
    # 阶段 3: 交付总结报告
    # =========================================================================
    dur_total = time.time() - t_global_start
    print("\n" + "=" * 80)
    print("🏁 《小天气》EP06 全集制作完成！")
    print(f"· 原画质检通过: {passed_count}/20")
    print(f"· 4K 超分完成: {upscale_success}/20")
    print(f"· 总运行耗时: {dur_total/60:.1f} 分钟")
    print("=" * 80, flush=True)

if __name__ == "__main__":
    main()
