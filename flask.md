#### Xiang Wang @ 2017-07-11 14:36:50

## 基础
* [基础](#基础)
* [request](#request)
* [response](#response)
* [部署](#deploy)


<div id="基础"></div>
### 基础
```
@app.route("/proxy")
def hello():
    return "Hello world!", 200
```

<div id="request"></div>
### request
* method: `"GET", "POST"`
* json: `把json数据解析出来`


<div id="response"></div>
### response
* return "Hello world!", 200


<div id="deploy"></div>
### 部署
```
    gunicorn -w 4 -b 127.0.0.1:8000 duishangproxy:app
```
