#### Xiang Wang @ 2016-07-13 15:47:54

## 参考
[学习网址](http://mongoengine.org/)
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
    2. primary_key=True # 设置为主键，数据库里面的`_id`就会是这个值
* ReferenceField(User)  # 保存了reference的 `ObjectId` 
* EmbeddedDocumentField(User_embedded)  # 保存了所有的信息
* required=True # 能否为空, 如果为空，保存的时候就不保存

### 特殊的自定义方法
    clean(self):  # 每次save的时候都会调用这个，用来写数据格式的正确与否
        if '@' in self.name: # 如果数据格式不正确
            raise ValidationError('There should not be @ in your name') # 则 `raise ValidationError('message')`

### 数据查询
    Book.objects(language='Eng')
    Book.objects(author__name='wangx')
    User.objects(name='wangx').fields(slice__addresses=[0,1])
