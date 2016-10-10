#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-10-10 14:43:34

import xlrd
import xlsxwriter

workbook = xlrd.open_workbook('origin.xlsx')
sheet = workbook.sheets()[0]
result = {}
for row in range(sheet.nrows):
    data = sheet.row_values(row)[0].replace(' ','').replace('\t','').replace('\n','')
    if len(data) > 8:
        continue
    else:
        result[data] = True

f = open('result.xlsx', 'wb')
workbook = xlsxwriter.Workbook(f)
worksheet = workbook.add_worksheet()

index = 0
for data in result.keys():
    worksheet.write(index, 0, data)
    index += 1
workbook.close()
f.close()
