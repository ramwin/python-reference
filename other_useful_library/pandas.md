## [pandas](https://pandas.pydata.org/docs/user_guide/index.html)


```
import pandas
df1 = pandas.DataFrame(
    {'年龄': [21,22,23,24]},
    index=pandas.Series(
        ['a张三', 'b李四', 'c王二', 'd麻子'],
        name='姓名'
    ),
    columns=["年龄"]
)
df2 = df1.iloc[0:3]
df2 = df2.sort_index(ascending=False)

>>> df1.loc[df2.index]]['年龄'] == df2['年龄']
True

index = pandas.Index(data=[], name='name')
df = pandas.DataFrame(data={'age':[]}, columns=['age'], index=index)
df.loc['张三'] = {'age': 18}
```


### [Sorting 排序](https://pandas.pydata.org/docs/user_guide/basics.html#by-values)

```
# 二分法找到最接近但不大于的数
df = pandas.read_csv(<filename>, names=["name, "age"])
df.sort_values(by='age', inplace=True)
df[df.age <= 20].max()
```

### [Indexing and selecting data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)
```
df.loc["张三"].年龄
df.loc["张三"]["年龄"]
```
* loc[slice]
寻找index某一范围内的前闭后闭区间, 注意, index一定要保证排序好了。
```
df.sort_index()
df.loc[开始: 结束]
```

* loc[key]
寻找某个key, 注意如果存在多个，返回的就是dataframe

```
In [109]: df
Out[109]: 
          b      c
a                 
amily    18  False
bob      19   True
charlie  20   True
charlie  22   True

In [110]: df.loc['bob']  # Series, df.loc['bob'].c == True
Out[110]: 
b      19
c    True
Name: bob, dtype: object

In [111]: df.loc['charlie']  # DataFrame
Out[111]: 
          b     c
a                
charlie  20  True
charlie  22  True

```

### where 过滤数据
```
df.where(df.id > 0)
df[df.id > 0)
df[df.index.notnull()]  # 过滤掉index为None的
df[~pandas.to_datetime(df.index, errors="coerce").isnull()]  # 过滤掉日期不规范的
```


* Set/reset Index

```
df2 = df.set_index("ID")
```


### Input/output


```
pandas.read_excel(filename, header=[0, 1], converters={("学校信息", "年级"): str})
最后converters会进入
ParserBase._convert_to_ndarrays()
    for c, values in dct.items():
        # c = ("学校信息", "年级")
        conv_f = None if converters is None else converters.get(c, None)
        conv_f执行
```


#### `read_csv`  
* [guide](https://pandas.pydata.org/docs/user_guide/io.html#csv-text-files)  
* [api](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)  
    * seq|delimiter: 数据分隔符,默认是`,`
    * header: 数据开始的位置. 默认infer, 当有names, 相当于None, 当没有names, 相当于0
    ```
    pandas.read_csv(<filename>, names=['name', 'age'])  # 第一列也是数据
    pandas.read_csv(<filename>, names=['name', 'age'], header=0)  # 第一列是标题,但是我们强制修改
    ```
    * names: 自定义列名
    * [ ] `index_col`
    * usecols: 使用那些列
    * `index_col`: 哪一列当作index
    * dtype: 每一列的数据
    ```
    dtype = {
        'id': int,
        'note': str,
    }
    ```
    * engine: python|c|pyarrow
    * converters: 
    ```
    converters={
        "addr": lambda x: int(x[2:], 16),  # 把十六进制转化成十进制数字
    }
    ```
    * [ ] `true_values`
    * `parse_dates`: 哪些列要当作时间。时间是TimeStamp, 所以只占用4字节
    * skipfooter: 排序底部的多少行, 开启的是否，需要设置engine="python"
    *
    * `keep_default_na`: 是否把数据解析成NAN. 我喜欢设置成False


## [API](https://pandas.pydata.org/docs/reference/index.html)
### [pandas.core.series.Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)
* iteritems
```
df['姓名'].dropna().iteritems()
[
    (0, value),
    (1, value),
]
```

### [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)
* 基础操作
```
del df[attribute]  # 删除列
```


* columns: 返回字段列表`pandas.core.indexes.base.Index`

* size
返回`shape[0] * shape[1]`

* shape:
返回DataFrame的尺寸

```
df = pandas.DataFrame({"col1": [1,2,], "col2": [3,4], "col3": [5,6]})
df.shape
>>> (2, 3)
```

* [`memory_usage`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.memory_usage.html)
```
df.memory_usage(deep=True)  # 查看各列的内存占用
```

* [empty](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.empty.html)
返回是否为空

* [ ] `set_flags`

* iterrows()


    for index, row in df.iterrows():
        print(row.客户名称)


#### [apply: 应用函数](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)
对没一行操作， 生成新的列
```
df['姓名'] = df.apply(lambda row: row['姓'] + row['名'], axis=1)  # axis: 一行一行调用
df['field'] = df['field'].apply(lambda x: x if x != '0.000000' else x)
```

* applymap  
对每个元素操作， 没啥用


* `sort_values` 根据一列来排序
```
df = df.sort_values('datetime')
df.sort_values('datetime', inplace=True)
```


* [to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)

      * 保存到csv文件, 可以直接 `df.to_csv(name.csv.gz)` 变成压缩文件
      * columns: 保存哪些字段


* drop  
删除列


```
new_df = df.drop(columns=['company'])
```

* [rename](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)
默认是更换index, 更换列名需要设置columns
```
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df.rename(columns={"A": "a", "B": "c"}, inplace=True)
```

* [`to_dict`][to_dict]
返回字典

```
df.to_dict(orient="index")
>>> {
  "张三": {
    "年龄": 25,
    "身高": 170,
  }
}
```


[to_dict]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html

## data types
### Timestamp
```
TimeStamp(str|datetime|date)
```

## Utils
* [`is_datetime64_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_dtype.html) >> Bool
```
pandas.api.types.is_datetime64_dtype(df.index)  # 判断Series是否全部是日期
```
