# 基础
```
from flask import Flask

app = Flask(__name__)


@app.route("/proxy")
def hello():
    return "Hello world!", 200
```

```
[wangx@localhost]$ flask --app hello run
```

# request
* method: `"GET", "POST"`
* json: `把json数据解析出来`


# response
* return "Hello world!", 200


# 部署
```
    gunicorn -w 4 -b 127.0.0.1:8000 --access-logfile log.log duishangproxy:app
```
