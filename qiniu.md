*Xiang Wang @ 2017-06-16 14:58:59*


## 智能多媒体API [官网](https://developer.qiniu.com/dora)
### 图片处理
#### 图片基本处理
* 接口规格
```
?imageView/<mode>/w/
```
    * `/0/w/<longEdge>/h/<ShortEdge>`
    * `/1/w/<Width>/h/<Height>`: 宽最少为Width, 高最少为Height, 等比缩放， 居中裁剪
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

### 上传文件
```
    from qiniu import put_file, Auth
    access_key = 'Zy3HE44UK9tRACuAeEL3mxc8aTTj0jgZkrjxrJAB'
    secret_key = 'wLXODkNWpzFj_SI60zu5GjjOVZzxmvlNJ0tLOR3K'
    q = Auth(access_key, secret_key)
    bucket_name = 'sharegine-public-test'
    key = 'avatar-user-0.png'
    token = q.upload_token(bucket_name, key, 3600, policy={
        # 'bucket': 'sharegine-public-test',
        # 'key': 'avatar-user-0.png',
        'insertOnly': 0,
    })
    ret, into = put_file(token, key, './portrait.png')
    # ret, into = put_file(token, key, './android.png')
```

### 数据处理

* #### 触发持久化操作

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
