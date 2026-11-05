# -*- coding: utf-8 -*-
"""
upscale_missing_5_shots.py
补齐《小天气》EP02、EP04、EP05 缺失的 5 支 4K 院线级超分分镜：
1. EP02 SHOT_02: 02_SHOT_02_妈妈的疑惑
2. EP04 SHOT_01: 01_SHOT_01_妈妈启动洗衣机
3. EP04 SHOT_19: 19_SHOT_19_妈妈惊讶夸花
4. EP05 SHOT_05: 05_SHOT_05_爸爸转动胡椒研磨器
5. EP05 SHOT_15: 15_SHOT_15_父母出门外婆留下照看
"""

import sys
import os
import time
import json
import subprocess
from pathlib import Path

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

import cv2
import torch
import spandrel

PROJECT_ROOT = Path(r"C:\Users\32503\Desktop\小天气")
MODEL_PATH = Path(r"D:\ComfyUI_windows_portable\ComfyUI\models\upscale_models\RealESRGAN_x4plus.pth")
FFMPEG = Path(r"C:\Users\32503\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe")
FFPROBE = Path(r"C:\Users\32503\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffprobe.exe")

TARGETS = [
    {
        "ep": "EP02",
        "dir_pat": "S01E02*",
        "shot_pat": "02_SHOT_02*",
    },
    {
        "ep": "EP04",
        "dir_pat": "S01E04*",
        "shot_pat": "01_SHOT_01*",
    },
    {
        "ep": "EP04",
        "dir_pat": "S01E04*",
        "shot_pat": "19_SHOT_19*",
    },
    {
        "ep": "EP05",
        "dir_pat": "S01E05*",
        "shot_pat": "05_SHOT_05*",
    },
    {
        "ep": "EP05",
        "dir_pat": "S01E05*",
        "shot_pat": "15_SHOT_15*",
    },
]

def check_is_valid_4k(video_path: Path) -> bool:
    if not video_path.exists() or video_path.stat().st_size < 1024 * 1024:
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

def upscale_single_shot(input_path: Path, output_path: Path, qc_4k_dir: Path, model, device):
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
    qc_4k_dir.mkdir(parents=True, exist_ok=True)
    for tag, sec in [("t15", 1.5), ("t30", 3.0)]:
        out_jpg = qc_4k_dir / f"{shot_stem}_{tag}_4K.jpg"
        subprocess.run([str(FFMPEG), "-y", "-ss", str(sec), "-i", str(output_path), "-frames:v", "1", "-q:v", "2", str(out_jpg)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  [4K QC] 样帧已生成: {out_jpg.name}", flush=True)

def main():
    print("=" * 80)
    print("🚀 《小天气》EP02/EP04/EP05 缺失 5 镜 4K 院线级超分辨率流水线启动")
    print(f"· 模型: {MODEL_PATH.name}")
    print(f"· 目标: 3840x2160 Lanczos + NVENC p4 CQ18 + 原生音频直通")
    print("=" * 80, flush=True)

    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"未找到超分模型文件: {MODEL_PATH}")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[*] 正在加载 RealESRGAN_x4plus 模型至 {device} (FP16)...", flush=True)
    model = spandrel.ModelLoader().load_from_file(str(MODEL_PATH)).to(device).half().eval()
    print("✅ 模型加载成功并进入推理模式！\n", flush=True)

    total_tasks = len(TARGETS)
    success_count = 0
    t_all_start = time.time()

    for idx, target in enumerate(TARGETS, 1):
        ep = target["ep"]
        dir_pat = target["dir_pat"]
        shot_pat = target["shot_pat"]

        ep_dir = next(PROJECT_ROOT.glob(dir_pat))
        raw_dir = next(ep_dir.glob("01_*"))
        up_dir = next(ep_dir.glob("02_*"))
        qc_4k_dir = next(ep_dir.glob("03_4K*"))

        raw_file = next(raw_dir.glob(shot_pat))
        out_file = up_dir / f"{raw_file.stem}_4K.mp4"

        print(f"[{idx}/{total_tasks}] 处理 {ep} - {raw_file.name}")

        if check_is_valid_4k(out_file):
            print(f"  ⏩ 4K 产物已存在且尺寸校验通过 (3840x2160): {out_file.name}")
            success_count += 1
            continue

        upscale_single_shot(raw_file, out_file, qc_4k_dir, model, device)

        # 校验产物
        if check_is_valid_4k(out_file):
            print(f"  ✨ 4K 校验通过: {out_file.name}")
            success_count += 1
        else:
            print(f"  ❌ 4K 校验异常: {out_file.name}")

        if idx < total_tasks:
            print("  ❄️ 显卡静息降温 8 秒...", flush=True)
            time.sleep(8)

    print("\n" + "=" * 80)
    print(f"🏁 5 镜 4K 超分全部完成: 成功 {success_count}/{total_tasks} | 总耗时: {time.time() - t_all_start:.1f}s")
    print("=" * 80, flush=True)

if __name__ == "__main__":
    main()
