#### Xiang Wang @ 2017-05-19 15:22:17


```
    from urllib.parse import urlencode, urlparse, unquote
    url = "%s?%s" % ('http://www.ramwin.com', urlencode({'pram1': 'foo', 'param2': 'bar'}))
    unquote_url = unquote(url)
    urlparse(unquote_url).query
```
