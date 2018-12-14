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
