*Xiang Wang @ 2017-06-16 14:58:59*


## 智能多媒体API [官网](https://developer.qiniu.com/dora)
### [处理机制](https://developer.qiniu.com/dora/manual/1204/processing-mechanism)
* 管道处理
```
[GET] url?<fop1>|<fop2>|<fop3>|<fopN>
```
* [样式](https://developer.qiniu.com/dora/manual/1204/processing-mechanism#3)
通过命令行工作，可以把一大串的处理变成一个简短的类似`-phone`这种图片

### 图片处理
#### 图片基本处理 [官网](https://developer.qiniu.com/dora/manual/1279/basic-processing-images-imageview2)
* 接口规格
```
?imageView2/<mode>/w/
```
    * `/0/w/<longEdge>/h/<ShortEdge>` 限制长边最长，短边最长，等比缩放，适合移动端的缩略图。
    * `/1/w/<Width>/h/<Height>`: 宽最少为Width, 高最少为Height, 等比缩放， 居中裁剪 只
    * `/1/w/<Width>`: 宽和高都最少为Width, 生成正方图

#### 图片水印处理
* 接口规格
```
?watermark/1
         /image/<encodedImageURL>  URL安全的Base64编码, 使用
         /dissolve/<dissolve>
         /gravity/<gravity>
         /dx/<distanceX>
         /dy/<distanceY>
         /ws/<watermarkScale>
         /wst/<watermarkScaleType>
# 对上的水印
?watermark/1/image/aHR0cHM6Ly9wdWJsaWNzdGF0aWMuZHVpc2hhbmcubmV0L3dhdGVybWFya19zbWFsbC5wbmc=/dissolve/70/
```

#### 图片圆角处理
* 接口规格
```
roundPic/radius/<radius>
        /radiusx/<radiusx>
        /radiusy/<radiusy>
```


## SDK
* [官网](https://developer.qiniu.com/kodo/sdk/1242/python#1)
```
from qiniu import put_file, Auth
access_key = 'Zy3HE44UK9tRACuAeEL3mxc8aTTj0jgZkrjxrJAB'
secret_key = 'wLXODkNWpzFj_SI60zu5GjjOVZzxmvlNJ0tLOR3K'
qiniu_auth = Auth(access_key, secret_key)
```

### 上传文件
```
from qiniu import etag
bucket_name = 'sharegine-public-test'
key = 'avatar-user-0.png'
token = qiniu_auth.upload_token(bucket_name, key, 3600, policy={
    # 'bucket': 'sharegine-public-test',
    # 'key': 'avatar-user-0.png',
    'insertOnly': 0,
})
ret, into = put_file(token, key, './portrait.png')
assert ret["key"] == key
assert ret["hash"] == etag(localfile)
```

### 数据处理

* #### 触发持久化操作

### [资源管理](https://developer.qiniu.com/kodo/sdk/1242/python#6)
#### [ ] 修改文件存储类型
#### [移动或重命名文件](https://developer.qiniu.com/kodo/sdk/1242/python#rs-move)
```
# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth
from qiniu import BucketManager
access_key = 'Access_Key'
secret_key = 'Secret_Key'
#初始化Auth状态
q = Auth(access_key, secret_key)
#初始化BucketManager
bucket = BucketManager(q)
#你要测试的空间， 并且这个key在你空间中存在
bucket_name = 'Bucket_Name'
key = 'python-logo.png'
#将文件从文件key 移动到文件key2，可以实现文件的重命名 可以在不同bucket移动
key2 = 'python-logo2.png'
ret, info = bucket.move(bucket_name, key, bucket_name, key2)
print(info)
assert ret == {}
```
#### [ ] 复制文件副本
#### [删除空间中的文件](https://developer.qiniu.com/kodo/sdk/1242/python#rs-delete)
```
ret, info = bucket_manager.delete(bucket_name, key)
assert ret == {}
```

#### 获取指定前缀文件列表
```
ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
ret = {
    "marker": "eywehrjklew",
    "items": [
        {
            'putTime': 15687092976559020,
            'key': 'avatar-10410-9654a38253a44b5fb0f4c6b488aada04.png',
            'status': 0, 'md5': '3e99448da736a4eb742b40b525416e91',
            'fsize': 18948, 'type': 0,
            'mimeType': 'image/png', 'hash': 'FvosvnLv2SFSqqRmW4nFEfY17Kkb'
        }
    ]
}
eof = False 如果还有数据的话
assert len(ret.get('items')) is not None
```

#### [抓取网络资源到空间](https://developer.qiniu.com/kodo/sdk/1242/python#rs-fetch)
```
# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth
from qiniu import BucketManager
access_key = '...'
secret_key = '...'
bucket_name = 'Bucket_Name'
q = Auth(access_key, secret_key)
bucket = BucketManager(q)
url = 'http://7xr875.com1.z0.glb.clouddn.com/xxx.jpg'
key = 'xxx.jpg'
ret, info = bucket.fetch(url, bucket_name, key)
print(info)
assert ret['key'] == key  # 如果失败了 ret is None
```

#### [ ] 更新镜像存储空间中文件内容

### CDN相关
* #### 文件刷新
```
import qiniu
from qiniu import CdnManager
auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)
urls = [
    'http://aaa.example.com/a.gif',
    'http://bbb.example.com/b.jpg'
]
ret, info = cdn_manager.refresh_urls(urls)
assert ret['code'] == 200 and ret['error'] == 'success'
```

* #### 目录刷新


## 附录
### URL安全的Base64编码
```
from qiniu import urlsafe_base64_encode
```
