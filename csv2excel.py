#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-02-23 19:03:33


import xlsxwriter
csv_file = open(input("输入你要转化的文件路径:"), 'r')
result_file = open(input("输入输出文件的路径:"), 'wb')
split = input("输入文件的分隔符:")
result_workbook = xlsxwriter.Workbook(result_file)
worksheet = result_workbook.add_worksheet()
for i, line in enumerate(csv_file.readlines()):
    for j, data in enumerate(line.strip().split(split)):
        worksheet.write(i, j, data)
result_workbook.close()

