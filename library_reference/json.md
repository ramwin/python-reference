**Xiang Wang @ 2019-02-27 10:55:13**


### JSON
[官方教程](https://docs.python.org/3/library/json.html)
* 代码内使用
```
    import json
    data = {}
    text = json.dumps(data)
    data = json.loads(text)

    file_obj = open('source/test.json','r')
    data = json.load(file_obj)

    file_obj = open('source/test.json', w')
    json.dump(obj, file_obj, ensure_ascii=False)
```
* 命令行使用
```
    echo '{"json": "obj"}' | python -m json.tool
    python -m json.tool <filename>
    import pprint
    pprint.pprint(data, depth=4, indent=4)
```
* 报错
json.decoder.JSONDecodeError(python3), ValueError(python2)
