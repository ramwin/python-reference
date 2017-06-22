#### Xiang Wang @ 2017-05-09 11:10:45

# 基础
* [官方教程](https://openpyxl.readthedocs.io/en/default/tutorial.html)
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
    ws = wb.get_active_sheet()
```

* 写入数据
```
```
