# 标准化输出时间
[参考代码](./script/time时间.py)

## 时间 变成 文本
    import datetime, time
    time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    time.strftime('%F %T', time.localtime())
        %d: 几号
        %b: 几月 Sep, Feb
        %F: 2016-08-30
        %T, %X: 14:35:37
## 把时间文本变成标准化的structtime        文本变成 structtime
    temp=time.strptime('20150707120000','%Y%m%d%H%M%S')

## 把structime变成时间戳
    time.mktime(structtime)
## 把时间戳变成structime
    time.gmtime(...)        #这个会变成标准UTC时间
    time.localtime()        #这个比较好,当地时间
    datetime.datetime.fromtimestamp(integer)


## 时间运算
    a = b - c
    a = datetime.timedelta(day, second, microsecond)  # microsecond 10e-6s
    print(a.total_seconds())
