# MySQLdb
    import MySQLdb
    db = MySQLdb.connect(host="localhost",user="root",passwd="wangxiang", db="test",charset="utf8")
    cursor = db.cursor()
    command = 'insert into test2 (name) values ("1中");'
    cursor.execute(command)
    command = 'insert into test2 (name) values ("1\u6211");'    # 插入了6211
    cursor.execute(command)
    cursor.close()
    db.commit()

# MySQL官方python包
[官方地址](http://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)
[下载地址](http://dev.mysql.com/downloads/connector/python/)
## 基础
    from mysql.connector import connection
    cnx = connection.MySQLConnection(
        user='wangx',
        password='wangxiang',
        host='127.0.0.1',
        database = 'testdb')    # 直接调用对象或者调用函数都可以，下面的方法是调用了函数
    cnx.commit()    # 提交数据库的操作
    cnx.close()    # 关闭数据库
    connect()连接数据库
    import mysql.connector
    config = {
      'user': 'scott',
      'password': 'tiger',
      'host': '127.0.0.1',
      'database': 'employees',
      'raise_on_warnings': True,
      'use_pure': False,
    }
    cnx = mysql.connector.connect(**config)
    cnx.close()

    读取数据库
    cursor = cnx.cursor()
    cursor.execute("select * from auth_user;")
    list = cursor.fetchall()
