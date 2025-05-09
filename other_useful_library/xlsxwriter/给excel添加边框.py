#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import xlsxwriter


def main():
    workbook = xlsxwriter.Workbook("/mnt/d/添加边框.xlsx")
    sheet = workbook.add_worksheet()
    cell_format = workbook.add_format({"bold": True, "font_color": "red"})
    cell_format.set_right(1)
    cell_format.set_right_color("red")
    sheet.set_column("F:F", 30, cell_format)
    workbook.close()


main()
