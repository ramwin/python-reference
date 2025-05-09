```{contents}
```

# openpyxl
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

## Install
* [官方教程](https://openpyxl.readthedocs.io/)

* 安装


```
pip install openpyxl
pip install pillow  # 如果你需要插入图片
```


* 读取数据

```
from openpyxl import Workbook
from openpyxl import load_workbook
wb = load_workbook(<filename>)
ws = wb.active  # 旧版本使用 ws = wb.get_active_sheet()
for row in ws.rows:
    for cell in row:
        print(cell.value)
```


* 写入数据

```
ws['A4'] = 4
ws.cell(row=1, column=1, value=1)  # 因为excel是从1开始的，所以这里也是从1开始
```


## Workbook
* 读取workbook

```
    load_workbook(filename, data_only=True)  # data_only会把公式变成value
```


* 获取sheet, 操作sheet


```
    wb = load_workbook(filename)
    wb.sheetnames
    wb['其他sheetname']  # 获取sheet, 操作sheet
    wb.active = wb["another sheet"]  # 修改激活的sheet
```



## Simple Usage

### [Merge Cells](https://openpyxl.readthedocs.io/en/stable/usage.html#merge-unmerge-cells)
When you merge cells the column and row number starts from 1

```
>>> from openpyxl.workbook import Workbook
>>>
>>> wb = Workbook()
>>> ws = wb.active
>>>
>>> ws.merge_cells('A2:D2')
>>> ws.unmerge_cells('A2:D2')
>>> 
>>> # or equivalently
>>> ws.merge_cells(start_row=2, start_column=1, end_row=4, end_column=4)
>>> ws.unmerge_cells(start_row=2, start_column=1, end_row=4, end_column=4)
```

### [Insert an Image](https://openpyxl.readthedocs.io/en/stable/usage.html#inserting-an-image)
```
>>> from openpyxl import Workbook
>>> from openpyxl.drawing.image import Image
>>>
>>> wb = Workbook()
>>> ws = wb.active
>>> ws['A1'] = 'You should see three logos below'
>>> img = Image('logo.png')
>>> # add to worksheet and anchor next to cells
>>> ws.add_image(img, 'A1')
>>> wb.save('logo.xlsx')

>>> image = Image("logo.png")
>>> image.width = 500
>>> image.height = 370
>>> ws.add_image(image, 'B2')
```

## [Working with Styles](https://openpyxl.readthedocs.io/en/stable/styles.html#)
* 给第三列添加红色竖线
```{literalinclude} add_border.py
```

## [Worksheet Tables](https://openpyxl.readthedocs.io/en/stable/worksheet_tables.html)

* 例子
```
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

wb = Workbook()
ws = wb.active

data = [
    ['Apples', 10000, 5000, 8000, 6000],
    ['Pears',   2000, 3000, 4000, 5000],
    ['Bananas', 6000, 6000, 6500, 6000],
    ['Oranges',  500,  300,  200,  700],
]

## add column headings. NB. these must be strings
ws.append(["Fruit", "2011", "2012", "2013", "2014"])
for row in data:
    ws.append(row)

tab = Table(displayName="Table1", ref="A1:E5")

## Add a default style with striped rows and banded columns
style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                       showLastColumn=False, showRowStripes=True, showColumnStripes=True)
tab.tableStyleInfo = style
ws.add_table(tab)
wb.save("table.xlsx")
```
* max_row: 数字最大行数
* max_column: 数字最大宽度

## Utils
* `openpyxl.utils.column_index_from_string`
```
column_index_from_string('A') => 1
```

* `get_column_letter`
```
get_column_letter(1) => A
```

## xlrd
用来处理xls文件
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
