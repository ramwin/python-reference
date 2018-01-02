#### Xiang Wang @ 2017-05-19 15:22:17


```
    from urllib.parse import urlencode, urlparse, unquote
    url = "%s?%s" % ('http://www.ramwin.com', urlencode({'pram1': 'foo', 'param2': 'bar'}))
    unquote_url = unquote(url)
    urlparse(unquote_url).query
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

* 解码
