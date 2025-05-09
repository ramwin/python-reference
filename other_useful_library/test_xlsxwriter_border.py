#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook("/mnt/d/demo.xlsx")

worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column("A:A", 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({"bold": True})

# Write some simple text.
worksheet.write("A1", "Hello")

# Text with formatting.
worksheet.write("A2", "World", bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

cell_format = workbook.add_format()
cell_format.set_right(1)
worksheet.set_column("D:D", 20, cell_format)
workbook.close()
