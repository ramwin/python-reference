#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-05-03 15:36:31

''' 这个是python2脚本'''

import MySQLdb
# db = MySQLdb.connect("localhost","root","wangxiang", "test")
db = MySQLdb.connect(host="localhost",user="root",passwd="wangxiang", db="test",charset="utf8")
cursor = db.cursor()
command = 'insert into test2 (name) values ("1中");'
cursor.execute(command)
# command = 'insert into test2 (name) values ("1中");'  # 无法插入 UnicodeDecodeError
# cursor.execute(command)
# command = 'insert into test2 (name) values ("u中");'.decode('utf8')   无法插入
# cursor.execute(command)
# command = 'insert into test2 (name) values ("1中");'.encode('utf8') # 报错    UnicodeDecodeError
# cursor.execute(command)
command = 'insert into test2 (name) values ("1\u6211");'    # 插入了6211
cursor.execute(command)
# command = u'insert into test2 (name) values ("1中");'
# cursor.execute(command) # UnicodeEncodeError: 'latin-1' codec can't encode character u'\u4e2d' in

cursor.close()
db.commit()
