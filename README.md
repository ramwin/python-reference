#### Xiang Wang @ 2017-02-10 15:30:51

# 基础函数
* enumerate
```
    enumerate(['a','b','c'])  // [(0, 'a'), (1, 'b'), (2, 'c')]  但是不是list， 而是一个enumerate对象
```


# 包参考
* [csv](./csv.md)
* [collections](./collections.md)
* [fractions](https://docs.python.org/2/library/fractions.html#fractions.Fraction)
```
    from fractions import Fraction
    f = Fraction(1,3)
    print("1/3 = %d/%d" % (f.numerator, f.denominator))
```

# 其他包
* [jinja模板渲染](./jinjia.md)
* [openpyxl](./openpyxl.md)
* [scrapy](./scrapy/README.md)
* [peewee](./peewee.md) *简单而轻量级的sqlite3 orm，和django很像*
