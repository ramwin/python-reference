### [pendulum](https://pendulum.eustace.io/docs/)
更加好用的时间库
```
pendulum.now()
DateTime(2022, 4, 20, 13, 5, 54, 185608, tzinfo=Timezone('Asia/Shanghai'))
pendulum.now().to_datetime_string()
"2022-04-20 13:09:14"
pendulum.parse('2022-04-20 13:09:14', tz=pendulum.local_timezone())
```

### [pytz](https://pythonhosted.org/pytz/)  *时区*
```
from datetime import datetime
from pytz import timezone
import pytz
utc = pytz.utc
shanghai = timezone("Asia/Shanghai")
fmt = "%Y-%m-%d %H:%M:%S %Z%z"
loc_datetime = shanghai.localize(datetime(2002, 10, 27, 6, 0, 0))
print(loc_datetime.strftime(fmt))
utc_time = loc_datetime.astimezone(utc)
```

### 时间
[官方文档](https://docs.python.org/3/library/datetime.html)

#### datetime

##### [Instance methods 实例方法](https://docs.python.org/3/library/datetime.html#datetime.datetime.date)
* datetime.date(): 返回时间的日期  
注意如果时区切换了，返回的结果是对应时区的日期，所以会变化  

##### Instance attributes
* datetime.year
* datetime.month
* datetime.day
* datetime.hour

##### combine
```
datetime.combine(date, time, tzinfo=self.tzinfo)
```

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

#### Date
* 构造方法
    * classmethod date.today()
    返回当天的本地日期, 等价于`date.fromtimestamp(time.time())`
    * classmethod date.fromtimestamp
    * classmethod date.fromisoformat
    ```
    date.fromisoformat('2020-12-04')
    >>> date(2020, 12, 4)
    ```
    * classmethod date.fromisocalendar
* 属性
    * day: 返回某个date的日期
