** Xiang Wang @ 2016-07-13 15:47:54 **

**mongoengine**
[官网](http://docs.mongoengine.org/)
* [字段](http://docs.mongoengine.org/guide/defining-documents.html#fields)

# mongoengine基础
* example
    ```
    from mongoengine import *
    connect('tumblelog')
    connect('mongodb', host='mac', port=27017)

    class User(Document):
        name = StringField(required=True)

    class User_embedded(EmbeddedDocument):
        name = StringField(required=True)
    ```

## 数据格式
* StringField() # 字符串
    1. max_length   # 设置最长多少, 超过就会报错, 类似meta, 是python层面
    2. primary_key=True # 设置为主键，数据库里面的`_id`就会是这个值
    3. required=True # 能否为空, 如果为空，保存的时候就不保存
    4. default='we' # 创建新的对象，属性就是'we'，而不是None
* ReferenceField(User)  # 保存了reference的 `ObjectId` 
* EmbeddedDocumentField(User_embedded)  # 保存了所有的信息
* URLField()
    1. verify_exists=False  # True 每次保存都会检查url
* ListField(EmbeddedDocumentField(models))
    * 不管有没有 default = [],默认的都是 [] 而不是None
    * [删除或者添加里面的数据](http://docs.mongoengine.org/guide/defining-documents.html#one-to-many-with-listfields)
        ```
        page.update_one(pull__authors=bob)
        page.update_one(push_authors=bob)
        ```
* [ObjectIdField](http://docs.mongoengine.org/apireference.html#mongoengine.fields.ObjectIdField)
    * 自定义一个数据的id:
        ```python
        import bson
        object_id = bson.objectid.ObjectId()
        read = Read(id=object_id)
        read.save()
        assert read.id == object_id
        ```
    * str(object) 返回他的id的字符串


# 数据更新
    class.update(inc__filed=3)  # 原子操作，多线程使用
# 特殊的自定义方法
    clean(self):  # 每次save的时候都会调用这个，用来写数据格式的正确与否
        if '@' in self.name: # 如果数据格式不正确
            raise ValidationError('There should not be @ in your name') # 则 `raise ValidationError('message')`

# 数据查询
    Book.objects(language='Eng')
    Book.objects(author__name='wangx')
    User.objects(name='wangx').fields(slice__addresses=[0,1])
    User.objects(friends__contains='Lily').all()

# 其他类
    DynamicDocument:    # 如果数据库里面的数据无法正确解析到class(比如多了一个字段，就会报错。使用DynamicDocument就能解决这个问题)
