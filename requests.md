#### Xiang Wang @ 2016-12-26 21:21:00

# 基础
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

# 参数
* method
* url
* params
* headers
* cookies


# response
* `status_code` 状态码
* `json` JSON数据
* `content` 二进制数据
* `text` 文本数据
