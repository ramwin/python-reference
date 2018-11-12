**Xiang Wang @ 2018-09-14 10:28:59**

## wechatpy
### [github链接](https://github.com/jxtech/wechatpy) [官网文档](http://docs.wechatpy.org/zh_CN/master/)
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

### 微信 OAuth 网页授权接入
#### 公众号 OAuth 网页授权接入 [官网](http://docs.wechatpy.org/zh_CN/master/oauth.html#module-wechatpy.oauth)
`class wechatpy.oauth.WeChatOAuth(app_id, secret, redirect_uri, scope="snsapi_base", state="")`
* `authorize_url`: 获取授权的跳转地址
* `qrconnect_url`: `生成扫码登录的地址`
* `fetch_access_token(code)`: 获取`access_token`
* `get_user_info(openid=None, access_token=None, lang='zh_CN')`: 获取用户信息
