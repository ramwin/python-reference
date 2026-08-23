#!/usr/bin/env python3
"""按 F6 时由 vim 调用: 把 Windows 截图目录里最新的一张截图移动到
当前编辑的 markdown 同目录下的 img/ 子文件夹, 并输出 markdown 图片语法.

用法:
    insert_screenshot.py <markdown文件路径>
"""

import os
import shutil
import sys
from pathlib import Path

SCREENSHOT_DIR = Path(os.environ.get('SCREENSHOT_DIR', '/mnt/c/Users/ramwi/Pictures/Screenshots'))
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}


def clean_name(name):
    """文件名规范化: 屏幕截图 -> ScreenShot, 空格 -> _"""
    return name.replace('屏幕截图', 'ScreenShot').replace(' ', '_')


def fail(msg):
    """打印错误到 stdout(让 vim 的 system() 能捕获), 并以非 0 退出."""
    print(msg)
    sys.exit(1)


def latest_screenshot():
    """截图目录里 mtime 最新的一张图片."""
    images = [p for p in SCREENSHOT_DIR.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS]
    if not images:
        fail(f'{SCREENSHOT_DIR} 里没有图片')
    return max(images, key=lambda p: p.stat().st_mtime)


def main():
    if len(sys.argv) != 2:
        fail('用法: insert_screenshot.py <markdown文件路径>')
    md_path = Path(sys.argv[1]).resolve()
    if not md_path.parent.is_dir():
        fail(f'markdown 所在目录不存在: {md_path.parent}')

    src = latest_screenshot()
    img_dir = md_path.parent / 'img'
    dest = img_dir / clean_name(src.name)
    if dest.exists():
        fail(f'{dest} 已存在, 不覆盖')

    img_dir.mkdir(exist_ok=True)
    shutil.move(str(src), str(dest))
    # 不带换行, 方便 vim 用 append() 插入成一行
    sys.stdout.write(f'![{dest.name}](./img/{dest.name})')
    sys.stdout.flush()


if __name__ == '__main__':
    main()
