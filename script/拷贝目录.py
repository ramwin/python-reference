#!/usr/bin/env python3
"""
slow_mirror.py
异步、低磁盘压力的后台目录同步脚本（支持拷贝后删除源目录）。
"""
import asyncio
import logging
import shutil
from pathlib import Path
from typing import Tuple

import click

# ---------- 全局 logger ----------
log = logging.getLogger("slow_mirror")

# ---------- 日志 ----------
def setup_logger(verbose: bool) -> None:
    """配置日志，仅添加一次 handler。"""
    if getattr(setup_logger, "_configured", False):
        return
    level = logging.DEBUG if verbose else logging.INFO
    fmt = "%(asctime)s [%(levelname)s] %(threadName)s %(message)s"
    logging.basicConfig(level=level, format=fmt)

    from logging.handlers import RotatingFileHandler
    fh = RotatingFileHandler(
        "slow_mirror.log",
        maxBytes=10 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    fh.setFormatter(logging.Formatter(fmt))
    log.addHandler(fh)
    log.setLevel(level)
    setup_logger._configured = True  # type: ignore

# ---------- 工具 ----------
def is_empty_dir(path: Path) -> bool:
    """判断目录是否为空或者不存在"""
    try:
        return not any(path.iterdir())
    except FileNotFoundError:
        return True

async def copy_one_dir(src_dir: Path, dst_dir: Path, delete_source: bool) -> None:
    """异步拷贝一个目录，必要时删除源目录。"""
    try:
        log.info("开始拷贝 %s -> %s", src_dir, dst_dir)
        await asyncio.to_thread(
            shutil.copytree,
            src_dir,
            dst_dir,
            dirs_exist_ok=True,
            copy_function=shutil.copy2
        )
        log.info("拷贝完成 %s -> %s", src_dir, dst_dir)

        if delete_source:
            log.warning("删除源目录 %s", src_dir)
            await asyncio.to_thread(shutil.rmtree, src_dir)

    except Exception as e:
        log.exception("拷贝/删除失败 %s : %s", src_dir, e)

async def worker(queue: asyncio.Queue[Tuple[Path, Path]], interval: float, delete_source: bool) -> None:
    """worker 协程，处理队列中的拷贝任务。"""
    while True:
        src, dst = await queue.get()
        await copy_one_dir(src, dst, delete_source)
        await asyncio.sleep(interval)
        queue.task_done()

async def async_main(source: str,
                     target: str,
                     workers: int,
                     interval: float,
                     delete_source: bool,
                     verbose: bool) -> None:
    """主异步流程。"""
    setup_logger(verbose)

    src_root = Path(source).expanduser().resolve()
    dst_root = Path(target).expanduser().resolve()

    if not src_root.is_dir():
        log.error("源目录不存在: %s", src_root)
        return
    dst_root.mkdir(parents=True, exist_ok=True)

    subdirs = [p for p in src_root.iterdir() if p.is_dir()]
    log.info("共发现 %d 个一级子目录待检查", len(subdirs))

    queue: asyncio.Queue[Tuple[Path, Path]] = asyncio.Queue()
    for src_dir in subdirs:
        dst_dir = dst_root / src_dir.name
        if not dst_dir.exists() or is_empty_dir(dst_dir):
            log.info("计划拷贝 %s -> %s（目标不存在或为空）", src_dir, dst_dir)
            await queue.put((src_dir, dst_dir))
        else:
            log.debug("跳过 %s -> %s（目标已存在且非空）", src_dir, dst_dir)

    worker_tasks = [asyncio.create_task(worker(queue, interval, delete_source))
                    for _ in range(workers)]

    await queue.join()

    for w in worker_tasks:
        w.cancel()
    await asyncio.gather(*worker_tasks, return_exceptions=True)

    log.info("全部任务完成，退出。")

# ---------- Click 封装 ----------
@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument("source", type=click.Path(exists=True, file_okay=False))
@click.argument("target", type=click.Path(file_okay=False))
@click.option("-w", "--workers", default=2, show_default=True,
              help="并发拷贝任务数（建议≤2以降低磁盘压力）")
@click.option("-i", "--interval", default=0.5, show_default=True,
              help="两次拷贝之间 sleep 的秒数")
@click.option("--delete-source", is_flag=True,
              help="拷贝成功后删除源目录中的对应文件夹")
@click.option("-v", "--verbose", is_flag=True,
              help="输出 DEBUG 级别日志")
def cli(source: str, target: str, workers: int, interval: float, delete_source: bool, verbose: bool) -> None:
    """将 SOURCE 中存在的文件夹，如果 TARGET 不存在或为空，则拷贝过去。
    整个过程异步、低磁盘压力、后台慢速运行，日志写入 slow_mirror.log。
    """
    try:
        asyncio.run(async_main(source, target, workers, interval,
                               delete_source, verbose))
    except KeyboardInterrupt:
        log.warning("收到 Ctrl-C，优雅退出")

if __name__ == "__main__":
    cli()
