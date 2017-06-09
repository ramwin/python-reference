#### Xiang Wang @ 2017-06-09 15:03:43


# OPENPYXL
* 合并单元格
    sheet.merge_cells(
        start_row=1,
        end_row=2,
        start_column=1,
        end_column=2,
    )
* 样式
    * openpyxl.styles.Alignment
        Alignment(vertical='center')

# xlrd
* 打开文件
    ```
    workbook = xlrd.open_workbook(filename)
    # 但是更多的情况是文件已经在内存的
    data = open(filename, 'rb').read()
    workbook = xlrd.open_workbook(file_contents=data)
    ```

* Sheets
    ```
    sheet = workbook.sheets()[0] # 获取 workbook 的sheets
    sheet.nrows # 获取 sheet 的行数
    sheet.row_values(1) # 获取某一行的数据(返回一个 list)
    ```
