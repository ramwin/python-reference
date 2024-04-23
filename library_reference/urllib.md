# 基础
[python3官网教程](https://docs.python.org/3.6/library/urllib.parse.html)

* 基础
```python3
from urllib.parse import urlencode, urlparse, unquote, parse_qs
url = "%s?%s" % ('http://www.ramwin.com', urlencode({'pram1': 'foo', 'param2': 'bar'}))
unquote_url = unquote(url)
urlparse(unquote_url).query  # param1=foo&param2=bar
parse_qs("a=b")  # {"a": ["b"]}
```

* 编码
```
# 把字典变成url
urlencode({"kw": "查找=kw"})
>>> 'kw=%E6%9F%A5%E6%89%BE%3Dkw'
url = 'https://duishang.net?%s' %  'kw=%E6%9F%A5%E6%89%BE%3Dkw'
# urlencode
quote('http://duishang.net')
>>> 'http%3A//duishang.net%3Few%3Dew'
```

# urllib.parse
* [ ] urlunsplit
* [`urllib.parse.urljoin(base, url, allow_fragments=True)`](https://docs.python.org/3.6/library/urllib.parse.html#urllib.parse.urljoin)  
`allow_fragments`为True代表url里面可以有#anchor, 如果为False,代表base的path里面不能有fragments, 会舍弃掉后再与url相连
```
>>> parse.urljoin('https://localhost/1/2', '3')
'https://localhost/1/3'
>>> parse.urljoin('https://localhost/1/2/', '3')
'https://localhost/1/2/3/'
>>> parse.urljoin('https://localhost/1/2/', '/3')
'https://localhost/3'
```
* [ ] urldefrag
