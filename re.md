**Xiang Wang @ 2016-05-26 15:30:51**

[官网](https://docs.python.org/3/library/re.html#module-re)

## Regular Expression Syntax 基础知识和语法
* `.` 任意一个字符， 除了\n
```
re.match(r".*", "123\n").group() == "123"
re.match(r".*", "123\n", re.DOTALL).group() == "123\n"
```

* `(?!...)`  
后续不能出现`...`
* `\d`  *数字*
* `\D`  *非数字*
* `\s`  *空白字符*
* `\S`  *非空白字符*

* `\w`  *单词字符*
```
[a-zA-Z0-9_] 以及其他语言的字符
```

* `\W`  *非单词字符*

* `(a|bc|d)`  *a或者bc或者c*
* `[a-z]` * 小写字母  
* 是否是贪婪模式: 在匹配后面加上?表示不贪婪, 比如
```
re.match(r"\d+?", "123").group() == "1"
re.match(r"\d+", "123").group() == "123"
*?
+?
??
{4, 6}?
```

* `(?P<name>...)`  
或者匹配的时候就能用
```
m = re.match(r'(?P<index>\d+)word(?P=index)', '123word123')  # 用\1也可以
```
匹配楚Name, 之后可以获取
```
m = re.match(r'(?P<name>.*)', 'name')
print(m.group('name'))
print(m.end('name'))  # TODO
```

## Module Contents 模块内容 [官网](https://docs.python.org/3/library/re.html#module-contents)
* re.compile
```
re.compile(r'(?P<id>\d+)we').match('123we').group('id')
```
* re.A
* re.ASCII
* [ ] ...
* re.sub(pattern, repl, string, count=0, flags=0)  
```
re.sub(r'(00)*$', '', '100000')  # 把匹配到的数据变成空
```
[测试代码](library_reference/test_re.py)  
Return the string obtained by replacing the leftmost non-overlapping occurences of pattern in string by the replacement repl. The repl can be a function.
* 每次匹配把结果里面的数据拿出来  
`re.sub('a(\d)b', r'\1', 'a4bcdaba2b')`
* 替换手机号码
```
re.sub('(\d*)(\d{4})(\d{3})', r"\1****\3", "7982660")
```
* 使用函数来替换
```
>>> def dashrepl(matchobj):
...     if matchobj.group(0) == '-': return ' '
...     else: return '-'
>>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')
'pro--gram files'
```
* [ ] ...

## [Regular Expression Examples](https://docs.python.org/3/library/re.html#regular-expression-examples)
5. [Text Munging](https://docs.python.org/3/library/re.html#text-munging)
```
>>> def repl(m):
...     inner_word = list(m.group(2))
...     random.shuffle(inner_word)
...     return m.group(1) + "".join(inner_word) + m.group(3)
>>> text = "Professor Abdolmalek, please report your absences promptly."
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'
```

## 例子
* 找到字符串里面符合规则的字符串
```
    a = re.compile(r'^数据更新时间：(?P<time>[0-9: -]*)').match('数据更新时间：2016-05-25 16:00:00')
    print(a.groupdict())
```

* 把字符串里面符合规则的字符进行替换
```
    re.splite(r'\.0*', text)
```


* 删除字符串里面符合规则的字符串
