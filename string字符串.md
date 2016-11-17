#### Xiang Wang @ 2016-09-05 12:48:47


# string
    'a,b,c'.split(',',1)    # 只拆分一次
    string.digits   # '0123456789'
    string.ascii_letters
    string.ascii_lowercase
    string.ascii_uppercase
    <string>.count('w') # 查看字符串里面字符的数量

# strip
    'a'.strip()  # 把前后空格，换行，tab删除
    'a'.strip('we')  # 把前后的 w 和 e 删除。 而不是把前后的 'we' 删除

# bytes

# unicode
    a = u'ew'   # python3里面默认的字符串就是unicode, python2里面默认的字符串是str, 所有有unicode这个类

## unicode转字符串
    # 因为python的unicode就是字符串，所以不需要
    u = u'我'
    u.encode('utf8')

# base64
    b = base64.encodebytes('我'.encode('utf8')) # 只有二进制才能encode,结果还是bytes
    b = base64.encodestring('我'.encode('utf8')) # 查了源码，果然这个是为了兼容python2的语法。以后避免使用这个方法

    b = base64.encodestring('我')   # python2里面的str就是二进制,结果是str(仍然是二进制)
