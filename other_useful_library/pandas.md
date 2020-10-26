**Xiang Wang @ 2020-10-09 19:45:29**


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

### [Indexing and selecting data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)
```
df.loc["张三"].年龄
df.loc["张三"]["年龄"]
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
* columns: 返回字段列表`pandas.core.indexes.base.Index`
* iterrows()
```
for index, row in df.iterrows():
    print(row.客户名称)
```
* shape:
返回DataFrame的尺寸
```
df = pandas.DataFrame({"col1": [1,2,], "col2": [3,4], "col3": [5,6]})
df.shape
>>> (2, 3)
```
