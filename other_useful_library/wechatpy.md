**Xiang Wang @ 2018-09-14 10:28:59**

> wechatpy 是一个微信 (WeChat) 公众平台的第三方 Python SDK, 实现了普通公众平台和企业号公众平台的解析消息、生成回复和主动调用等 API。

* [github链接](https://github.com/jxtech/wechatpy)
* [官网文档](http://docs.wechatpy.org/zh_CN/master/)

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

### 推送事件
#### 公共属性
```
name	value
id	事件 id, 64 位整型。
source	事件的来源用户，即发送消息的用户。
target	事件的目标用户。
create_time	事件的发送时间，UNIX 时间戳
type	event
event	事件的类型
```
#### 模板消息发送任务完成事件
event: "templatesendjobfinish"
status: "success"

### 微信主动调用接口
#### [模板消息相关接口](http://docs.wechatpy.org/zh_CN/master/client/template.html#)
```
wechatpy.client.api.WeChatTemplate(client=None)
```

* `get_all_private_template` 获取模板列表
```
{
    "template_list": [
        {
            "content": "{{first.DATA}}\n业务状态：{{keyword1.DATA}}\n时间：{{keyword2.DATA}}\n{{remark.DATA}}",
            "title": "业务状态通知",
            "deputy_industry": "其他",
            "template_id": "ZphdjlGNe9XxLdLoib2qYfTH6ueu-WjteQyKLsyeDkQ",
            "primary_industry": "其他",
            "example": "你好，你的合同状态有变更。\n业务状态：你的合同号为HT00001的合同已审核通过，请查阅。\n时间：2016年3月17号 \n13:18感谢你的使用\n",
        }
    ]
}
```


#### 用户接口 [官网](http://docs.wechatpy.org/zh_CN/master/client/user.html)
`wechatpy.client.api.WeChatUser(client=None)`
* `get(user_id, lange='zh_CN')` 获取**用户基本信息**(UnionId机制)
```
user_info = wechat_client.user.get('openid')
{u'subscribe': 0, u'tagid_list': [], u'openid': u'o_13fszy206hbTUZJMyxClHrjVW8'}  # 未关注
{  # 已关注
    "subscribe": 1,
    "openid": "o6_bmjrPTlm6_2sgVt7hMZOPfL2M",
    "nickname": "Band",
    "sex": 1,
    "language": "zh_CN",
    "city": "广州",
    "province": "广东",
    "country": "中国",
    "headimgurl":"http://thirdwx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/0",
    "subscribe_time": 1382694957,
    "unionid": " o6_bmasdasdsad6_2sgVt7hMZOPfL"
    "remark": "",
    "groupid": 0,
    "tagid_list":[128,2],
    "subscribe_scene": "ADD_SCENE_QR_CODE",
    "qr_scene": 98765,
    "qr_scene_str": ""
}
```

### 微信 OAuth 网页授权接入
#### 公众号 OAuth 网页授权接入 [官网](http://docs.wechatpy.org/zh_CN/master/oauth.html#module-wechatpy.oauth)
`class wechatpy.oauth.WeChatOAuth(app_id, secret, redirect_uri, scope="snsapi_base", state="")`
* `authorize_url`: 获取授权的跳转地址
* `qrconnect_url`: `生成扫码登录的地址`
* `fetch_access_token(code)`: 获取`access_token`
* `get_user_info(openid=None, access_token=None, lang='zh_CN')`: 获取用户信息
