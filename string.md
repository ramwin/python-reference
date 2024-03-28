**Xiang Wang @ 2016-09-05 12:48:47**


# 方法
* islower
* isupper
* istitle

# string模块
```
'a,b,c'.split(',',1)    # 只拆分一次
string.digits   # '0123456789'
string.ascii_letters
string.ascii_lowercase
string.ascii_uppercase
<string>.count('w') # 查看字符串里面字符的数量
```

## strip
```
'a'.strip()  # 把前后空格，换行，tab删除
'a'.strip('we')  # 把前后的 w 和 e 删除。 而不是把前后的 'we' 删除
```

# [format](https://pyformat.info/)
1. basic formatting 基础
```
year = 2015; event = 'Referendum'
f'Results of the {year} {event}'
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes/(yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
'We are the {} who say "{}!"'.format('knights', 'Ni')
'{0} and {1}'.format('spam', 'eggs')
```

2. [x] [value conversion](https://pyformat.info/#conversion_flags)
```
old "%s %r" % (Data(), Data())
new '{0!s} {0!r}'.format(Data(), Data())
```

6. Numbers
```
old '%d' % 42
new '{:d}'.format(42)
old '%f' % 3.14159
new '{:f}'.format(3.14159)
```
7. padding numbers
```
old '%4d' % 32
new '{:4d}'.format(32)
output '  42'
old '%06.2f' % 3.14159
new '{:06.2f}'.format(3.14159)  # 第一个数字代表长度，第二个代表精度
output '003.14'
old '%04d' % 42
new '{:04d}'.format(42)
output '0042'
```
14. [ ] to be continued  
