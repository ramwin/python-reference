#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-01-05 10:28:07

import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', password='wangxiang', database='appdb')
cursor = cnx.cursor()

query = ("SELECT * FROM NUMBER "
         "WHERE sensor_id='%s'")

cursor.execute(query, ('3'))
