#### Xiang Wang @ 2016-09-14 10:03:31

##  基础
[官方教程](https://docs.python.org/3/library/json.html)
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

```
    python -m json.tool <filename>
    import pprint
    pprint.pprint(data, depth=4, indent=4)
```
