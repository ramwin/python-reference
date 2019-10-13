**Xiang Wang @ 2016-12-26 21:21:00**

* [官网](http://docs.python-requests.org/en/master/)
* [上传文件代码](./requests上传文件.py)

### 基础
```
requests.requests(
    "url": "http://www.baidu.com",
    "method": "GET" | "POST",
    "headers": {
        "Content-Type": "application/json; charset=utf-8",
    },
    "data": {
        "title": "test",
    },
    "params": {
        "order": "id",
        "size": "10",
    },
    "cookies": {
        "sessionid": "fewajkgl;dsfuhgjelrkj"
    },
    "verify": False,
)
```
* 发送一个Json请求
注意, 这里如果直接使用data, 因为lib里面会判断: 不然会不传递这个参数. 而django-rest-framework哪怕是空数组也需要参数的
```
# requests的源码
class request.models.RequestEncodingMixin
    ...
    def _encode_params(data):
        ...
        elif hasattr(data, '__iter__'):
            result = []
            for k, vs in to_key_val_list(data):
                if isinstance(vs, basestring) or not hasattr(vs, '__iter__'):
                    vs = [vs]
                for v in vs:
                    if v is not None:  # 只有不为空,才会添加参数
                        result.append(
                            (k.encode('utf-8') if isinstance(k, str) else k,
                             v.encode('utf-8') if isinstance(v, str) else v))
            return urlencode(result, doseq=True)
        ...
```
示例:
```
requests.post(
    url=<url>,
    json=<dict>,
)
```

### 参数
* method
* url
* params
* headers
* cookies
* [proxies](http://docs.python-requests.org/en/master/user/advanced/#proxies) 
[代理池](http://www.xicidaili.com/)
    ```
    import requests
    proxies = {
        'http': 'http://10.10.1.10:3182',
        'https': 'http://10.10.1.10:1080',
    }
    requests.get('http://ipinfo.io', proxies=proxies)
    ```

### response
* `status_code` 状态码
* `json` JSON数据
如果报错了，会raise `simplejson.errors.JSONDecodeError`, python2里面会raise `ValueError`
* `content` 二进制数据
* `text` 文本数据

### Advanced Usage 进阶用法
#### 1. Session Objects
通过Session可以保持长链接, 请求速度会快一点.
```
s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("https://httpbin.org/cookies")
print(r.text)
```
