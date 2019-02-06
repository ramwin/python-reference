**Xiang Wang @ 2017-05-19 15:22:17**

# [python3官网教程](https://docs.python.org/3.6/library/urllib.parse.html)
* 基础
```
    from urllib.parse import urlencode, urlparse, unquote  #python3
    from urllib import urlencode  # python2
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

# [python2官网教程](https://docs.python.org/2/library/urlparse.html)
## urllib
* urllib.urlencode
```
>>> urllib.urlencode({'key': 'value'})  # 对应 urlparse.parse_qsl
key=value
>>> urllib.urlencode({'key': ['value']}, doseq=1)  # 对应 urlparse.parse_qs
key=value
```

* urllib.quote
```
>>> urllib.quote("我")
%E6%88%91
>>> urllib.quote('&')
"%26"
```

## urlparse
```
from urlparse import urlparse
o = urlparse('https://www.ramwin.com/testrest/text/?text=qwer')
>>> ParseResult(scheme='http', netloc='www.ramwin.com', path='/testrest/text/', params='', query='text=qwer', fragment='')
```
* 属性
    * `parse_qs`
    ```
    result urlparse.parse_qs(url)
    >>> {'name': ['name1']}  # result
    import urllib
    urllib.urlencode(result, doseq=1)
    ```
    * `parse_qsl`
    ```
    urlparse.parse_qsl(url)
    >>> [('name', 'name1')]
    ```


## ParseResult *urlparse.ParseResult*
* 属性
    * port: o.port: 80
    * scheme: o.scheme: http
    * geturl: o.geturl(): 'http://www.ramwin.com/testrest/text/?text=qwer'

```
    url = (
        "http://7xlyxj.com1.z0.glb.clouddn.com/groups-198-1508841093056?"
        "e=1508844931&token=I0J8v_OINiV1arysiBZn9oyxoQH2bt5q51BjuMnW:fL46s4ff_8wiNFm-QxWDT6b6B3U=")
    >>> urlparse(url).path
    '/groups-198-1508841093056'
    >>> urlparse(url).query
    'e=1508844931&token=I0J8v_OINiV1arysiBZn9oyxoQH2bt5q51BjuMnW:fL46s4ff_8wiNFm-QxWDT6b6B3U='

    # python2
    >>> from urlparse import urlparse
    >>> o = urlparse(url)
    >>> o.path
    '/groups-198-1508841093056'
    >>> urlparse(url).query
    'e=1508844931&token=I0J8v_OINiV1arysiBZn9oyxoQH2bt5q51BjuMnW:fL46s4ff_8wiNFm-QxWDT6b6B3U='
```
