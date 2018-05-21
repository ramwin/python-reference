**Xiang Wang @ 2017-04-21 10:48:07**

# basic
* [official reference](https://docs.python.org/3/library/csv.html) [example](./csv_test.py)


# dictwriter
* [官网教程](https://docs.python.org/3/library/csv.html#csv.DictWriter)
* 示例
```
    # 这个可以利用dict的特性，直接赋予数值
    import csv
    with open('names.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerheader()
        writer.writerow(<dict>)
        writer.writerows([<dict1>, <dict2>])
```
* `csv.DictWriter`
    * extrasaction = 'raise' 默认如果dict里面多出了字段就会报错, 如果是ignore 就会忽略这个字段
    * delimiter=',' 列与列之间的分隔符
* 注意
    * 如果dict里面缺少了某个字段，只会使那个字段为空，而不报错

# csv.DictReader
```python
file = open('filename.csv')
reader = csv.DictReader(file)
reader.fieldnames
>>> ['序号', '企业名称', '联系电话']
for row in reader:
    print(row) >>> {'联系电话': '', '企业名称': '碧桂园控股', '序号': {...}}
```
