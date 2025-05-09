#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


class FileSplitter:
    def __init__(self, path, size):
        """
        初始化文件分割器。

        :param path: 文件路径
        :param size: 每个部分的最大大小（单位：字节）
        """
        self.path = path
        self.size = size
        self.total_size = os.path.getsize(path)

    def _find_newline(self, file, start, end):
        """
        从理论分割点向后搜索换行符。

        :param file: 文件对象
        :param start: 起始位置
        :param end: 结束位置
        :return: 换行符的位置
        """
        file.seek(start)
        while start < end:
            byte = file.read(1)
            if byte == b'\n':
                return start + 1
            start += 1
        return end

    def _adjust_for_utf8(self, file, position):
        """
        调整位置以确保不会将UTF-8字符拆分。

        :param file: 文件对象
        :param position: 当前位置
        :return: 调整后的位置
        """
        while position > 0:
            file.seek(position - 1)
            byte = file.read(1)
            if byte not in [b'\x80', b'\x81', b'\x82', b'\x83', b'\x84',
                             b'\x85', b'\x86', b'\x87', b'\x88', b'\x89',
                             b'\x8a', b'\x8b', b'\x8c', b'\x8d', b'\x8e',
                             b'\x8f', b'\x90', b'\x91', b'\x92', b'\x93',
                             b'\x94', b'\x95', b'\x96', b'\x97', b'\x98',
                             b'\x99', b'\x9a', b'\x9b', b'\x9c', b'\x9d',
                             b'\x9e', b'\x9f']:
                break
            position -= 1
        return position

    def split(self):
        """
        将文件分割成多个部分，每个部分的大小不超过指定大小，
        且不会将一行文字分割开来，同时确保不会将UTF-8字符拆分。

        :return: 文件位置列表，每个位置表示一个分割后的文件的起始位置和结束位置
        """
        positions = []
        with open(self.path, 'rb') as file:
            start = 0
            while start < self.total_size:
                next_pos = start + self.size
                if next_pos >= self.total_size:
                    next_pos = self.total_size
                else:
                    next_pos = self._find_newline(file, next_pos, self.total_size)
                next_pos = self._adjust_for_utf8(file, next_pos)
                positions.append((start, next_pos))
                start = next_pos
        return positions

    def split_and_save(self, output_dir):
        """
        将文件分割成多个部分，并将每个部分保存为独立的文件。

        :param output_dir: 输出目录
        :return: 输出文件路径列表
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        positions = self.split()
        output_files = []
        with open(self.path, 'rb') as file:
            for i, (start, end) in enumerate(positions):
                output_file_path = os.path.join(output_dir, f'part_{i + 1}.txt')
                with open(output_file_path, 'wb') as output_file:
                    file.seek(start)
                    data = file.read(end - start)
                    output_file.write(data)
                output_files.append(output_file_path)

        return output_files


# 示例用法
splitter = FileSplitter('分割文件.py', 1000)  # 每个部分最大10MB
positions = splitter.split()
print(positions)
