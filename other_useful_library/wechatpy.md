**Xiang Wang @ 2018-09-14 10:28:59**

## wechatpy
### [官网文档](https://github.com/jxtech/wechatpy)
### 基础
```
from wechatpy.client import WeChatClient
from wechatpy.session.redisstorage import RedisStorage
from redis import Redis
redis_client = Redis.from_url('redis://127.0.0.1:6379/0')
session_interface = RedisStorage(redis_client, prefix="wechatpy")
wechat_client = WeChatClient(
    app_id, secret, session=session_interface
)
```
