# 标准化输出时间
## 时间 变成 文本
    time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
## 把时间文本变成标准化的structtime        文本变成 structtime
    temp=time.strptime('20150707120000','%Y%m%d%H%M%S')

## 把structime变成时间戳
    time.mktime(structtime)
## 把时间戳变成structime
    gmtime(...)        #这个会变成标准UTC时间
    localtime()        #这个比较好,当地时间

## 时间运算
