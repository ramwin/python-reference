#### Xiang Wang @ 2016-12-15 17:41:21

# 基础
    import redis
    r = redis.StrictRedis()
    r.get('foo')  # 如果key不存在，返回None
    r.set('foo', 'bar')

    r.delete(key)   # 删除key，存在就是返回1, 否则返回0

    r.hset('dict', 'key', 'value')
    r.hdel('dict', 'key')  # 存在就返回1, 否则返回0
