### Xiang Wang @ 2017-05-19 14:06:01


# PEEWEE *简单而轻量级的orm*
* [github链接](https://github.com/coleifer/peewee)
* [官方文档](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html#quickstart)
* [示例](https://github.com/coleifer/peewee#examples)

```
    from peewee import *
    from playhouse.sqlite_ext import SqliteExtDatabase
    import datetime
    db = SqliteExtDatabase('test.db')


    class BaseModel(Model):
        class Meta:
            database = db


    class User(BaseModel):
        username = CharField(unique=True)


    class Tweet(BaseModel):
        user = ForeignKeyField(User, related_name='tweets')
        message = TextField()
        created_date = DateTimeField(default=datetime.datetime.now)
        is_published = BooleanField(default=True)

    db.connect()
    db.create_tables([User, Tweet])

    charlie = User.create(username='charlie')
    huey = User(username='huey')
    huey.save()
```

* [返回](./README.md)
