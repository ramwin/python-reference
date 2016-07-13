#### Xiang Wang @ 2016-07-13 15:47:54

## 基础
    from mongoengine import *
    connect('tumblelog')

    class User(Document):
        name = StringField(required=True)

    class User_embedded(EmbeddedDocument):
        name = StringField(required=True)

### 数据格式
* StringField # 字符串
    1. max_length   # 设置最长多少, 超过就会报错, 类似meta, 是python层面
* ReferenceField(User)  # 保存了reference的 `ObjectId` 
* EmbeddedDocumentField(User_embedded)  # 保存了所有的信息
* required=True # 能否为空, 如果为空，保存的时候就不保存
