#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-06-22 14:06:25

from mongoengine import *
connect('test')    # 链接到 tumblelog 这个数据库


class Text(Document):
    text = StringField()

class User(Document):
    name = StringField()
    email = StringField()
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Book1(Document):
    name = StringField(required=True)
    author = ReferenceField(User)


class User_embeded(EmbeddedDocument):
    name = StringField(required=True)


class Book2(Document):
    name = StringField(required=True)
    author = EmbeddedDocumentField(User_embeded)

w = User_embeded(name='王祥2')
b = Book2(name="第二本书2", author=w)
b.save()
w.name= '王祥4'
w.save()


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    
    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


def test_reference():
    class User(Document):  # 哪些用户看过这个书
        name = StringField()
    class Book(Document):
        name = StringField()
        users = ListField(ReferenceField(User))
    user = User(name='user1')
    user.save()
    book = Book(name='book1')
    book.save()
    book.update(push__users=user)
    user.delete()
    book = Book.objects.get(id=book.id)
    print(book.users)  # 这样生成的id是还存在，但是user已经不存在了
    book.users.pop(0)
    book.save()


if __name__ == '__main__':
    test_reference()
