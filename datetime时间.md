### 时间
* [datetime](#datetime)
    * [formatting格式化](#formatting)
    * [timedelta](#datetime.timedelta)

#### datetime
##### [formatting格式化](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
* [参考代码](./script/time时间.py)
* %w: weekday，0周日, 6是周六
```
import datetime, time
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
time.strftime('%F %T', time.localtime())
    %d: 几号
    %b: 几月 Sep, Feb
    %F: 2016-08-30  # 不推荐使用
    %T, %X: 14:35:37
    %Y-%m-%d %H:%M:%S  # 2017-09-11 10:35:10
```

##### 各个格式之间的转化
* 文本 > structtime
```
temp=time.strptime('20150707120000','%Y%m%d%H%M%S')
datetime.datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
```
* structime > 时间戳: `time.mktime(structtime)`
* 时间戳 > structtime: 
```
time.gmtime(...)        #这个会变成标准UTC时间
time.localtime()        #这个比较好,当地时间
datetime.datetime.fromtimestamp(integer)
```
##### datetime.date
* 参数
* 方法
    * weekday: monday ==0; sunday ==6
    * isoweekday: monday == 1; sunday = 7
##### datetime.datetime
    * datetime.datetime.now()  当前时间，当前系统时间。在django里面设置时区为utc后，会自动变成utc时间

#### timedelta
[官网](https://docs.python.org/3/library/datetime.html#timedelta-objects)
* `class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`
* 方法:
    total_seconds(): 返回一共的秒数(float)

#### 其他要学习的
