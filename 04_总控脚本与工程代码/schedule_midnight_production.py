# -*- coding: utf-8 -*-
"""
schedule_midnight_production.py
定时守候总控守护脚本：
精确守候至 2026-11-06 00:00:00 (24:00)，随后全自动启动 EP07~EP13 全量 140 镜原画生产与质检流水线，全部交付后自动执行关机。
"""

import os
import sys
import time
import datetime
import subprocess
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)

PROJECT_ROOT = Path(r"C:\Users\32503\Desktop\小天气")
SCRIPTS_DIR = PROJECT_ROOT / "03_总控渲染与质检工单"
LOG_FILE = SCRIPTS_DIR / "ep07_ep13_midnight_production.log"
PYTHON_EXE = Path(r"D:\ComfyUI_windows_portable\python_embeded\python.exe")
COMFY_LAUNCHER = Path(r"D:\ComfyUI_H3_isolated_20261021\launch_isolated.py")
COMFY_HOST = "http://127.0.0.1:8188"

def ensure_comfyui_online():
    print("[COMFY] 检查 ComfyUI 服务状态...", flush=True)
    for _ in range(5):
        try:
            with urllib.request.urlopen(f"{COMFY_HOST}/system_stats", timeout=3) as resp:
                if resp.status == 200:
                    print("[COMFY] ✅ ComfyUI 服务在线且响应正常！", flush=True)
                    return True
        except Exception:
            pass
        time.sleep(2)
        
    print("[COMFY] ⚠️ ComfyUI 未响应，正在拉起后台独立实例...", flush=True)
    subprocess.Popen([str(PYTHON_EXE), str(COMFY_LAUNCHER)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for i in range(20):
        time.sleep(3)
        try:
            with urllib.request.urlopen(f"{COMFY_HOST}/system_stats", timeout=3) as resp:
                if resp.status == 200:
                    print(f"[COMFY] ✅ ComfyUI 已成功启动并就绪 (等待 {i*3}s)！", flush=True)
                    return True
        except Exception:
            pass
    return False

def wait_until_midnight():
    now = datetime.datetime.now()
    # 计算目标 24:00 (即次日 00:00:00)
    target = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
    wait_seconds = (target - now).total_seconds()
    
    print("=" * 70, flush=True)
    print(f"⏰ [定时守候启动] 当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
    print(f"🎯 预定执行时间: {target.strftime('%Y-%m-%d %H:%M:%S')} (24:00)", flush=True)
    print(f"⏳ 距离启动剩余: {int(wait_seconds)} 秒 ({wait_seconds/60:.1f} 分钟)", flush=True)
    print(f"📝 生产日志落盘: {LOG_FILE}", flush=True)
    print(f"🔒 严格约束: 纯原画交付（100% 严禁超分），完成后自动执行关机", flush=True)
    print("=" * 70, flush=True)
    
    # 心跳等待至 24:00
    while True:
        now = datetime.datetime.now()
        remaining = (target - now).total_seconds()
        if remaining <= 0:
            print(f"\n🔔 [时钟触发] 24:00 已到！当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}，准时启动生产！", flush=True)
            break
        if remaining > 60:
            # 每隔 60 秒打印一次心跳
            mins = int(remaining // 60)
            secs = int(remaining % 60)
            print(f"  [倒计时心跳] 距离 24:00 启动还剩 {mins} 分 {secs} 秒...", flush=True)
            time.sleep(min(60, remaining))
        else:
            time.sleep(remaining)
            break

def main():
    wait_until_midnight()
    
    # 确保 ComfyUI 在线
    ensure_comfyui_online()
    
    # 启动生产管线
    pipeline_script = SCRIPTS_DIR / "produce_ep07_to_ep13_full_pipeline.py"
    cmd = [
        str(PYTHON_EXE),
        "-u",
        str(pipeline_script),
        "--shutdown"
    ]
    
    print(f"🚀 [生产流水线] 正在启动主总控命令: {' '.join(cmd)}", flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as lf:
        lf.write(f"\n\n{'='*70}\n[24:00 准时启动生产] {datetime.datetime.now()}\n{'='*70}\n")
        lf.flush()
        proc = subprocess.Popen(cmd, stdout=lf, stderr=subprocess.STDOUT, text=True, cwd=str(PROJECT_ROOT))
        proc.wait()
        
    print(f"🏁 生产进程已结束，退出码: {proc.returncode}", flush=True)

if __name__ == "__main__":
    main()
