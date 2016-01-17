#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-04 19:08:36

import mysql.connector

cnx = mysql.connector.connect(user='root', password='wangxiang',
                              host='127.0.0.1',
                              database='employees')
cnx.close()
print('使用connect函数链接成功\n')

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='wangxiang',
                                 host='127.0.0.1',
                                 database='employees')
cnx.close()
print('使用MySQLConnection类链接成功\n')

import mysql.connector
from mysql.connector import errorcode
print('使用try来判断是否存在数据库:')

try:
  cnx = mysql.connector.connect(user='root',password='wangxiang',
                                database='testt')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
