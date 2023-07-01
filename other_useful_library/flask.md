## 基础
* [基础](#基础)
* [request](#request)
* [response](#response)
* [部署](#deploy)


### 基础
```
@app.route("/proxy")
def hello():
    return "Hello world!", 200
```

### request
* method: `"GET", "POST"`
* json: `把json数据解析出来`


### response
* return "Hello world!", 200


### 部署
```
    gunicorn -w 4 -b 127.0.0.1:8000 --access-logfile log.log duishangproxy:app
```
