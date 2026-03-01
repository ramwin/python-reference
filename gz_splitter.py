#!/usr/bin/env python3
"""
Gzip 文件分割工具

功能：读取 .gz 压缩文件，按每 N 行分割成小文件保存到目标目录。
支持三种处理模式：
1. single: 单进程顺序读写
2. threaded: 单进程读取 + 线程池异步写入
3. multiprocess: 单进程读取 + 进程池处理写入

文件名格式：原始名称(无后缀)_(文件index)_(起始行号)_(终止行号)(原始后缀)
"""

import gzip
import os
import time
import click
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from pathlib import Path
from typing import Iterator, Tuple, List
import tempfile
import shutil


def generate_output_filename(
    input_path: Path, 
    index: int, 
    start_line: int, 
    end_line: int
) -> str:
    """生成输出文件名: 原始名称_索引_起始行_终止行.txt.gz"""
    stem = input_path.stem
    if stem.endswith('.txt'):
        stem = stem[:-4]
    return f"{stem}_{index}_{start_line}_{end_line}.txt.gz"


def write_chunk_to_gz(output_path: Path, lines: List[str]) -> None:
    """将行列表写入 gzip 文件"""
    with gzip.open(output_path, 'wt', encoding='utf-8') as f:
        f.writelines(lines)


def read_gz_lines(input_path: Path) -> Iterator[Tuple[int, str]]:
    """读取 gzip 文件，返回 (行号, 行内容) 的迭代器"""
    with gzip.open(input_path, 'rt', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            yield line_num, line


def split_single_process(input_path: Path, output_dir: Path, lines_per_file: int) -> int:
    """
    方案1：单进程顺序读写
    返回生成的文件数量
    """
    file_count = 0
    current_lines: List[str] = []
    start_line = 1
    
    for line_num, line in read_gz_lines(input_path):
        current_lines.append(line)
        
        if len(current_lines) >= lines_per_file:
            file_count += 1
            end_line = line_num
            filename = generate_output_filename(input_path, file_count, start_line, end_line)
            output_path_file = output_dir / filename
            write_chunk_to_gz(output_path_file, current_lines)
            
            current_lines = []
            start_line = line_num + 1
    
    # 处理剩余行
    if current_lines:
        file_count += 1
        end_line = line_num if current_lines else start_line
        filename = generate_output_filename(input_path, file_count, start_line, end_line)
        output_path_file = output_dir / filename
        write_chunk_to_gz(output_path_file, current_lines)
    
    return file_count


def split_threaded(input_path: Path, output_dir: Path, lines_per_file: int, max_workers: int = 4) -> int:
    """
    方案2：单进程读取 + 线程池异步写入
    返回生成的文件数量
    """
    file_count = 0
    current_lines: List[str] = []
    start_line = 1
    futures = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for line_num, line in read_gz_lines(input_path):
            current_lines.append(line)
            
            if len(current_lines) >= lines_per_file:
                file_count += 1
                end_line = line_num
                filename = generate_output_filename(input_path, file_count, start_line, end_line)
                output_path_file = output_dir / filename
                
                # 提交写入任务
                future = executor.submit(write_chunk_to_gz, output_path_file, current_lines.copy())
                futures.append(future)
                
                current_lines = []
                start_line = line_num + 1
        
        # 处理剩余行
        if current_lines:
            file_count += 1
            end_line = line_num if current_lines else start_line
            filename = generate_output_filename(input_path, file_count, start_line, end_line)
            output_path_file = output_dir / filename
            future = executor.submit(write_chunk_to_gz, output_path_file, current_lines)
            futures.append(future)
        
        # 等待所有任务完成
        for future in futures:
            future.result()
    
    return file_count


def _write_chunk_worker(args: Tuple[str, List[str]]) -> None:
    """
    进程池工作函数 - 必须定义在模块级别以便能被 pickle
    接收字符串路径而不是 Path 对象（为了更好的兼容性）
    """
    output_path_str, lines = args
    write_chunk_to_gz(Path(output_path_str), lines)


def split_multiprocess(input_path: Path, output_dir: Path, lines_per_file: int, max_workers: int = 4) -> int:
    """
    方案3：单进程读取 + 进程池处理写入
    返回生成的文件数量
    """
    file_count = 0
    chunks: List[Tuple[str, List[str]]] = []
    current_lines: List[str] = []
    start_line = 1
    line_num = 0
    
    # 先收集所有数据块
    for line_num, line in read_gz_lines(input_path):
        current_lines.append(line)
        
        if len(current_lines) >= lines_per_file:
            file_count += 1
            end_line = line_num
            filename = generate_output_filename(input_path, file_count, start_line, end_line)
            output_path_file = output_dir / filename
            chunks.append((str(output_path_file), current_lines.copy()))
            
            current_lines = []
            start_line = line_num + 1
    
    # 处理剩余行
    if current_lines:
        file_count += 1
        end_line = line_num if current_lines else start_line
        filename = generate_output_filename(input_path, file_count, start_line, end_line)
        output_path_file = output_dir / filename
        chunks.append((str(output_path_file), current_lines))
    
    # 使用进程池并行写入
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(executor.map(_write_chunk_worker, chunks))
    
    return file_count


@click.command()
@click.argument('input_file', type=click.Path(exists=True, path_type=Path))
@click.option('--lines', '-n', default=1000, help='每个小文件的行数')
@click.option('--output-dir', '-o', default='./output', type=click.Path(path_type=Path), help='输出目录')
@click.option('--mode', '-m', 
              type=click.Choice(['single', 'threaded', 'multiprocess', 'all'], case_sensitive=False),
              default='single', help='处理模式')
@click.option('--workers', '-w', default=4, help='线程池/进程池的工作进程数')
@click.option('--benchmark', is_flag=True, help='运行性能测试对比所有模式')
def main(
    input_file: Path, 
    lines: int, 
    output_dir: Path, 
    mode: str, 
    workers: int,
    benchmark: bool
):
    """
    分割 gzip 文件为多个小文件
    
    INPUT_FILE: 输入的 .gz 文件路径
    """
    if not input_file.suffix == '.gz':
        click.echo("错误：输入文件必须是 .gz 格式", err=True)
        return
    
    if benchmark or mode == 'all':
        run_benchmark(input_file, output_dir, lines, workers)
    else:
        # 确保输出目录存在
        output_dir.mkdir(parents=True, exist_ok=True)
        
        click.echo(f"输入文件: {input_file}")
        click.echo(f"输出目录: {output_dir}")
        click.echo(f"每文件行数: {lines}")
        click.echo(f"处理模式: {mode}")
        click.echo(f"工作进程数: {workers}")
        click.echo("-" * 50)
        
        start_time = time.time()
        
        if mode == 'single':
            count = split_single_process(input_file, output_dir, lines)
        elif mode == 'threaded':
            count = split_threaded(input_file, output_dir, lines, workers)
        elif mode == 'multiprocess':
            count = split_multiprocess(input_file, output_dir, lines, workers)
        
        elapsed = time.time() - start_time
        click.echo(f"✓ 完成！生成了 {count} 个文件，耗时: {elapsed:.3f} 秒")


def run_benchmark(input_file: Path, output_dir: Path, lines: int, workers: int):
    """运行性能测试对比三种模式"""
    import tempfile
    import shutil
    
    click.echo("=" * 60)
    click.echo("性能测试 - 对比三种处理模式")
    click.echo("=" * 60)
    click.echo(f"测试文件: {input_file}")
    click.echo(f"文件大小: {input_file.stat().st_size / 1024 / 1024:.2f} MB")
    click.echo(f"每文件行数: {lines}")
    click.echo(f"线程/进程池大小: {workers}")
    click.echo()
    
    results = []
    
    # 测试方案1：单进程
    click.echo("[1/3] 测试单进程顺序读写模式...")
    test_dir = tempfile.mkdtemp()
    try:
        start = time.time()
        count = split_single_process(input_file, Path(test_dir), lines)
        elapsed = time.time() - start
        results.append(("单进程顺序读写", elapsed, count))
        click.echo(f"    完成: {elapsed:.3f} 秒, 生成 {count} 个文件")
    finally:
        shutil.rmtree(test_dir)
    
    # 测试方案2：线程池
    click.echo("[2/3] 测试单进程读取 + 线程池异步写入模式...")
    test_dir = tempfile.mkdtemp()
    try:
        start = time.time()
        count = split_threaded(input_file, Path(test_dir), lines, workers)
        elapsed = time.time() - start
        results.append(("单进程读 + 线程池写", elapsed, count))
        click.echo(f"    完成: {elapsed:.3f} 秒, 生成 {count} 个文件")
    finally:
        shutil.rmtree(test_dir)
    
    # 测试方案3：进程池
    click.echo("[3/3] 测试单进程读取 + 进程池处理模式...")
    test_dir = tempfile.mkdtemp()
    try:
        start = time.time()
        count = split_multiprocess(input_file, Path(test_dir), lines, workers)
        elapsed = time.time() - start
        results.append(("单进程读 + 进程池处理", elapsed, count))
        click.echo(f"    完成: {elapsed:.3f} 秒, 生成 {count} 个文件")
    finally:
        shutil.rmtree(test_dir)
    
    # 输出对比结果
    click.echo()
    click.echo("=" * 60)
    click.echo("性能对比结果")
    click.echo("=" * 60)
    click.echo(f"{'模式':<25} {'耗时(秒)':<12} {'文件数':<10} {'相对速度':<10}")
    click.echo("-" * 60)
    
    best_time = min(r[1] for r in results)
    for name, elapsed, count in results:
        ratio = elapsed / best_time
        speed = f"{ratio:.2f}x" if ratio > 1 else "1.00x (最快)"
        click.echo(f"{name:<25} {elapsed:<12.3f} {count:<10} {speed:<10}")
    
    click.echo("=" * 60)
    
    # 找出最快的方法
    fastest = min(results, key=lambda x: x[1])
    click.echo(f"\n🏆 最快模式: {fastest[0]} ({fastest[1]:.3f} 秒)")


# ==================== 测试用例 ====================

import unittest


class TestGzSplitter(unittest.TestCase):
    """测试 gzip 文件分割功能"""
    
    @classmethod
    def setUpClass(cls):
        """创建测试数据"""
        cls.test_dir = Path(tempfile.mkdtemp())
        cls.test_file = cls.test_dir / "test_data.txt.gz"
        cls.output_dir = cls.test_dir / "output"
        
        # 创建测试数据：10000 行
        cls.total_lines = 10000
        cls.lines_per_file = 1000
        
        with gzip.open(cls.test_file, 'wt', encoding='utf-8') as f:
            for i in range(cls.total_lines):
                f.write(f"Line {i + 1}: This is a test line with some content.\n")
        
        print(f"\n创建测试文件: {cls.test_file}")
        print(f"总行数: {cls.total_lines}")
    
    @classmethod
    def tearDownClass(cls):
        """清理测试数据"""
        shutil.rmtree(cls.test_dir)
        print(f"\n清理测试目录: {cls.test_dir}")
    
    def setUp(self):
        """每个测试前清理输出目录"""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def test_01_single_process(self):
        """测试单进程模式"""
        print("\n[测试] 单进程顺序读写模式...")
        count = split_single_process(self.test_file, self.output_dir, self.lines_per_file)
        
        # 验证文件数量
        expected_files = self.total_lines // self.lines_per_file  # 10
        self.assertEqual(count, expected_files)
        
        # 验证文件内容（按文件名中的序号排序）
        files = sorted(self.output_dir.glob("*.gz"), 
                      key=lambda p: int(p.name.split('_')[2]))  # 按 index 排序
        self.assertEqual(len(files), expected_files)
        
        total_read = 0
        for i, f in enumerate(files, 1):
            with gzip.open(f, 'rt', encoding='utf-8') as fp:
                lines = fp.readlines()
                total_read += len(lines)
                # 验证文件名格式
                self.assertIn(f"_{i}_", f.name)
        
        self.assertEqual(total_read, self.total_lines)
        print(f"  ✓ 成功分割为 {count} 个文件")
    
    def test_02_threaded(self):
        """测试线程池模式"""
        print("\n[测试] 线程池异步写入模式...")
        count = split_threaded(self.test_file, self.output_dir, self.lines_per_file, max_workers=4)
        
        expected_files = self.total_lines // self.lines_per_file
        self.assertEqual(count, expected_files)
        
        # 验证所有文件都存在且内容正确（按文件名中的序号排序）
        files = sorted(self.output_dir.glob("*.gz"),
                      key=lambda p: int(p.name.split('_')[2]))
        self.assertEqual(len(files), expected_files)
        
        total_read = 0
        for f in files:
            with gzip.open(f, 'rt', encoding='utf-8') as fp:
                total_read += len(fp.readlines())
        
        self.assertEqual(total_read, self.total_lines)
        print(f"  ✓ 成功分割为 {count} 个文件")
    
    def test_03_multiprocess(self):
        """测试进程池模式"""
        print("\n[测试] 进程池处理模式...")
        count = split_multiprocess(self.test_file, self.output_dir, self.lines_per_file, max_workers=4)
        
        expected_files = self.total_lines // self.lines_per_file
        self.assertEqual(count, expected_files)
        
        # 验证所有文件都存在且内容正确（按文件名中的序号排序）
        files = sorted(self.output_dir.glob("*.gz"),
                      key=lambda p: int(p.name.split('_')[2]))
        self.assertEqual(len(files), expected_files)
        
        total_read = 0
        for f in files:
            with gzip.open(f, 'rt', encoding='utf-8') as fp:
                total_read += len(fp.readlines())
        
        self.assertEqual(total_read, self.total_lines)
        print(f"  ✓ 成功分割为 {count} 个文件")
    
    def test_04_filename_generation(self):
        """测试文件名生成"""
        test_path = Path("/data/test_file.txt.gz")
        
        filename = generate_output_filename(test_path, 1, 1, 100)
        self.assertEqual(filename, "test_file_1_1_100.txt.gz")
        
        filename = generate_output_filename(test_path, 5, 401, 500)
        self.assertEqual(filename, "test_file_5_401_500.txt.gz")
        
        # 测试没有 .txt 的情况
        test_path2 = Path("/data/test_file.gz")
        filename2 = generate_output_filename(test_path2, 1, 1, 100)
        self.assertEqual(filename2, "test_file_1_1_100.txt.gz")
        
        print("\n[测试] 文件名生成... ✓")
    
    def test_05_performance_comparison(self):
        """性能对比测试"""
        print("\n[性能测试] 对比三种模式的速度...")
        
        results = []
        
        # 测试单进程
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        start = time.time()
        split_single_process(self.test_file, self.output_dir, self.lines_per_file)
        single_time = time.time() - start
        results.append(("单进程顺序读写", single_time))
        print(f"  单进程顺序读写: {single_time:.3f} 秒")
        
        # 测试线程池
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        start = time.time()
        split_threaded(self.test_file, self.output_dir, self.lines_per_file, max_workers=4)
        thread_time = time.time() - start
        results.append(("单进程读 + 线程池写", thread_time))
        print(f"  线程池异步写入: {thread_time:.3f} 秒")
        
        # 测试进程池
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        start = time.time()
        split_multiprocess(self.test_file, self.output_dir, self.lines_per_file, max_workers=4)
        process_time = time.time() - start
        results.append(("单进程读 + 进程池处理", process_time))
        print(f"  进程池处理: {process_time:.3f} 秒")
        
        # 输出对比
        print("\n  性能对比:")
        best = min(results, key=lambda x: x[1])
        for name, t in results:
            ratio = t / best[1]
            marker = " 🏆" if t == best[1] else ""
            print(f"    {name}: {t:.3f}s ({ratio:.2f}x){marker}")
        
        # 断言所有模式都能正常工作（不比较具体速度，因为受机器影响）
        self.assertTrue(all(t > 0 for _, t in results))


def run_tests():
    """运行所有测试"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestGzSplitter)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == '__main__':
    import sys
    
    # 检查是否需要运行测试
    if len(sys.argv) > 1 and sys.argv[1] in ['--test', '-t']:
        # 运行测试模式
        print("运行测试用例...\n")
        success = run_tests()
        sys.exit(0 if success else 1)
    elif len(sys.argv) == 1:
        # 无参数时默认运行测试
        print("运行测试用例... (使用 --help 查看命令行用法)\n")
        success = run_tests()
        if success:
            print("\n所有测试通过！")
            print("\n使用示例:")
            print(f"  python {sys.argv[0]} input.txt.gz --lines 1000 --output-dir ./output --mode single")
            print(f"  python {sys.argv[0]} input.txt.gz --benchmark")
        sys.exit(0 if success else 1)
    else:
        # 其他情况运行 CLI (包括带文件参数或 --help 等)
        main()
