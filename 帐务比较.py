#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang (ramwin@qq.com) @ 2018-01-02 22:04:25


import csv


file_汇总 = open('汇总表.csv')
dw = csv.DictReader(file_汇总)
deleted_code_汇总 = []
add_code_汇总 = []
for i in dw:
    if i['现使用状况'] in ['毁损待报废']:
        deleted_code_汇总.append(i['资产\n编号'])
    if i['现使用状况'] in ['在用']:
        add_code_汇总.append(i['资产\n编号'])

file_减少 = open('减少.csv')
dw = csv.DictReader(file_减少)
deleted_code_减少 = []
for i in dw:
    deleted_code_减少.append(i['资产编号'])

file_增加 = open('增加.csv')
dw = csv.DictReader(file_增加)
add_code_增加 = []
for i in dw:
    add_code_增加.append(i['资产编号'])


results = []
for i in deleted_code_减少:
    if i not in deleted_code_汇总:
        results.append({
            '原因': '减少的资产编号不在汇总表里面',
            '资产编号': i
        })
for i in add_code_增加:
    if i not in add_code_汇总:
        results.append({
            '原因': '增加的资产编号不在汇总表里面',
            '资产编号': i
        })
for i in deleted_code_汇总:
    if i not in deleted_code_减少:
        results.append({
            '原因': '汇总里减少的资产不在减少表里面',
            '资产编号': i
        })
for i in add_code_汇总:
    if i not in add_code_增加 and '2017' in i:
        results.append({
            '原因': '汇总里增加的资产不在增加表里面',
            '资产编号': i
        })

with open('result.csv', 'w') as csvfile:
    fieldnames = ['原因', '资产编号']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)
