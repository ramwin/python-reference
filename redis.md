#### Xiang Wang @ 2016-12-15 17:41:21

# 基础
    ```
    import redis
    # 单独链接
    r = redis.StrictRedis(db=0)

    # 连接池
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool)

    r.get('foo')  # 如果key不存在，返回None
    r.set('foo', 'bar', ex=3600)  # 3600秒后过期。传入string也可以

    r.delete(key)   # 删除key，存在就是返回1, 否则返回0

    r.hset('dict', 'key', 'value')
    r.hdel('dict', 'key')  # 存在就返回1, 否则返回0
    ```

# list
    ```
    r.rpush(key, *args)  把args里面的数据按照顺序放入key
    r.lpop(key)  把key里面的数据pop出来，如果没有就是None
    ```
