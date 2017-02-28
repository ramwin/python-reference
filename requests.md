#### Xiang Wang @ 2016-12-22 13:47:50


# 基础
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


# Response
## 参数
    
