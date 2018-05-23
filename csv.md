**Xiang Wang @ 2017-04-21 10:48:07**

# basic
* [official reference](https://docs.python.org/3/library/csv.html)


# dictwriter
* [official documents](https://docs.python.org/3/library/csv.html#csv.DictWriter)
* example
```
    import csv
    with open('names.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(<dict>)
        writer.writerows([<dict1>, <dict2>])
```
* `csv.DictWriter`
    * extrasaction = 'raise' | 'ignore' raise ValueError or not if there is another keys in `<dict>` data
    * delimiter=',' the delimiter between columns
* Attention
    * If a key is missing in the dict, the data will set blank instead of raise exception

# csv.DictReader
```python
file = open('filename.csv')
reader = csv.DictReader(file)
reader.fieldnames
>>> ['number', 'name', 'tel']
for row in reader:
    print(row) >>> {'tel': '', 'name': 'company', 'number': 'No. 1'}
```
