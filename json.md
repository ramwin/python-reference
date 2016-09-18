#### Xiang Wang @ 2016-09-14 10:03:31

##  基础
    import json
    data = {}
    text = json.dumps(data)
    data = json.loads(text)

    file_obj = open('source/test.json','r')
    data = json.load(file_obj)

##  其他
    python -m json.tool <filename>
    import pprint
    pprint.pprint(data, depth=4, indent=4)


