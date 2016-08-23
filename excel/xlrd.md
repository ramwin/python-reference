#### Xiang Wang @ 2016-08-23 12:37:35

## 打开文件
    workbook = xlrd.open_workbook(filename)
    # 但是更多的情况是文件已经在内存的
    data = open(filename, 'rb').read()
    workbook = xlrd.open_workbook(file_contents=data)

## Sheets
    sheet = workbook.sheets()[0] # 获取 workbook 的sheets
    sheet.nrows # 获取 sheet 的行数
    sheet.row_values(1) # 获取某一行的数据(返回一个 list)
    
